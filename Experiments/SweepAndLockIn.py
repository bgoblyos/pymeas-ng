from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from random import uniform

from math import ceil
from numpy import array, linspace, concatenate, zeros

import logging

# Only for debugging purposes
from time import sleep

from Misc.Prefix import formatPrefix

class SweepAndLockIn():
    def __init__(self, ui, devices):

        self.ui = ui
        self.devices = devices

        # Connect start button
        self.ui.sweepAndLockStart.clicked.connect(self.prepare)

        # Set up timer for progress bar
        # (and for waiting until the sweep is done)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateProgress)

        # Reset progress bars
        self.ui.sweepAndLockProgress.setValue(0)
        self.ui.sweepAndLockTotalProgress.setValue(0)

        # Add devices to selection box
        for sweeper in self.devices["sweeper"]:
            self.ui.sweepAndLockSelectSweeper.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.ui.sweepAndLockSelectLockIn.addItem(lockin)

        # Reset selections
        self.ui.sweepAndLockSelectLockIn.setCurrentIndex(0)
        self.ui.sweepAndLockSelectSweeper.setCurrentIndex(0)

        # Read back instrument settings when the selection is changed
        self.ui.sweepAndLockSelectLockIn.currentIndexChanged.connect(self.resetLockIn)
        self.ui.sweepAndLockSelectSweeper.currentIndexChanged.connect(self.resetSweeper)

        # Recalculate data point estimates when settings change
        self.ui.sweepAndLockSweepTime.valueChanged.connect(self.updateTime)
        self.ui.sweepAndLockSampleFreq.currentIndexChanged.connect(self.updateTime)


    def prepare(self):
        logging.debug("Started Sweep and Lock-in measurement")
        # Sweeper setup
        sweepTime = self.ui.sweepAndLockSweepTime.value()
        startFreq = self.ui.sweepAndLockStartFreq.value()
        endFreq = self.ui.sweepAndLockEndFreq.value()

        self.sweeper.setupSweep(startFreq, endFreq, sweepTime)
        # Update sweep time in case it got clamped
        sweepTime = sweeper.readSweepTime()

        # Set power level and turn off continous sweep
        self.sweeper.setPowerLevel(self.sweepAndLockPower.value())
        self.sweeper.setContSweep(False)

        # Lock-in setup
        freq = self.ui.sweepAndLockFreq.value()
        self.lockin.setFreq(freq)

        tau = self.ui.sweepAndLockTau.currentIndex()
        self.lockin.setTau(tau)

        sens = self.ui.sweepAndLockSens.currentIndex()
        self.lockin.setSens(sens)

        self.totalRuns = self.ui.sweepAndLockNumRuns.value()
        self.currentRun = 1

        self.data1 = array([])
        self.data2 = array([])

        # Reset total progress bar
        self.ui.sweepAndLockTotalProgress.setRange(0, self.sweepAndLockInNumRuns)
        self.ui.sweepAndLockTotalProgress.setValue(0)

        self.startRun()

    def startRun(self):

        sweepTime = self.sweeper.readSweepTime()
        sampleFreq = self.ui.sweepAndLockSampleFreq.currentIndex()
        (self.numPoints, self.padding) = self.lockin.armTimedMeasurement(sweepTime, sampleFreq)


        self.totalSteps = 2*(ceil(sweepTime) + 1)
        self.currentStep = 0

        # Reset progress bar
        self.ui.sweepAndLockProgress.setRange(0, self.totalSteps)
        self.ui.sweepAndLockProgress.setValue(0)

        # Start sweep
        sweeper.powerOn()
        sweeper.startSweep()

        self.timer.start()

    def updateProgress(self):
        # Check if the run is completed
        if self.currentStep >= self.totalSteps:
            self.completeRun()
        else:
            # Increment counter and progress bar
            self.currentStep += 1
            self.ui.sweepAndLockProgress.setValue(self.currentStep)


    def completeRun(self):

        # Stop the timer so updateProgress stops running
        self.timer.stop()
        logging.info("Sweep completed, extracting data...")

        # Set progress bar to indeterminate
        pbar = self.ui.sweepAndLockProgress
        pbar.setRange(0, 0)
        pbar.setValue(0)

        # Disable sweeper output
        self.sweeper.powerOff()

        # Pause lock-in to stop data collection
        self.lockin.pause()

        # Extract both datasets
        data1 = array(lockin.readBuffer(1, 0, self.numPoints))
        data2 = array(lockin.readBuffer(2, 0, self.numPoints))

        # Pad the data if necessary
        padding = zeros(self.sweepAndLockInPadding)
        data1 = concatenate((data1, padding))
        data2 = concatenate((data2, padding))
        logging.info("Data extracted")


        if len(self.data1) == 0 or len(self.data2):
            # If there's no data yet, overwrite the variables
            # with our new data
            self.data1 = data1
            self.data2 = data2
        else:
            # If there's already data, we add our new data to it
            # elementwise
            self.data1 += data1
            self.data2 += data2

        # Set progress bar to full
        pbar.setRange(0, 1)
        pbar.setValue(1)

        # Update the total progress
        self.ui.sweepAndLockTotalProgress.setValue(self.currentRun)

        if self.numRuns <= self.currentRun:
            # Normalize data
            self.sweepAndLockInData /= self.sweepAndLockInNumRuns

            # Read back sweep parameters from the instrument
            start, end, _ = self.sweeper.readSweepParams()
            freqs = linspace(start, end, len(self.data1))

            # TODO: implement with an object passed on from main.py
            # Plot the resulting data
            #self.plot(freqs, self.sweepAndLockInData)
        else:
            self.currentRun += 1
            self.startRun()


    def selected(self):
        self.ui.expStack.setCurrentIndex(1)
        self.resetLockIn()
        self.resetSweeper()

    def resetSweeper(self):
        self.sweeper = self.devices["sweeper"][self.ui.sweepAndLockSelectSweeper.currentText()]

        # Power
        currentPower = self.sweeper.readPowerLevel()
        self.ui.sweepAndLockPower.setValue(currentPower)
        self.ui.sweepAndLockPower.setRange(*self.sweeper.powerRange)

        # Sweep limits
        start, end, time = self.sweeper.readSweepParams()
        self.ui.sweepAndLockStartFreq.setValue(start)
        self.ui.sweepAndLockEndFreq.setValue(end)
        self.ui.sweepAndLockSweepTime.setValue(time)

        self.ui.sweepAndLockStartFreq.setRange(*self.sweeper.freqRange)
        self.ui.sweepAndLockEndFreq.setRange(*self.sweeper.freqRange)
        self.ui.sweepAndLockSweepTime.setRange(*self.sweeper.timeRange)

        self.updateTime()

    def resetLockIn(self):
        self.lockin = self.devices["lockin"][self.ui.sweepAndLockSelectLockIn.currentText()]

        self.ui.sweepAndLockSens.clear()
        for sens in self.lockin.sensList:
            self.ui.sweepAndLockSens.addItem(formatPrefix(sens, 'V'))

        currentSens = self.lockin.readSens()
        self.ui.sweepAndLockSens.setCurrentIndex(currentSens)

        self.ui.sweepAndLockTau.clear()
        for tau in self.lockin.tauList:
            self.ui.sweepAndLockTau.addItem(formatPrefix(tau, 's'))

        currentTau = self.lockin.readTau()
        self.ui.sweepAndLockTau.setCurrentIndex(currentTau)

        self.ui.sweepAndLockSampleFreq.clear()
        for sample in self.lockin.sampleFreqList:
            self.ui.sweepAndLockSampleFreq.addItem(formatPrefix(sample, 'Hz'))

        currentSampleFreq = self.lockin.readSampleRate()
        self.ui.sweepAndLockSampleFreq.setCurrentIndex(currentSampleFreq)

        currentFreq = self.lockin.readFreq()
        self.ui.sweepAndLockFreq.setValue(currentFreq)

    def updateTime(self):
        logging.debug("Time estimations should be updated now")
        sampleFreqIndex = self.ui.sweepAndLockSampleFreq.currentIndex()
        sampleFreq = self.lockin.sampleFreqList[sampleFreqIndex]
        maxBins = self.lockin.bufferSize
        sweepTime = self.ui.sweepAndLockSweepTime.value()

        points = round(sweepTime*sampleFreq)
        maxTime = round(maxBins/sampleFreq)

        self.ui.sweepAndLockMaxTimeLabel.setText(f"{maxTime} s")
        self.ui.sweepAndLockDataPointsLabel.setText(f"{points} ({maxBins} max)")
