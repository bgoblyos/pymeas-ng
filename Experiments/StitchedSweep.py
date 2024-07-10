from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from random import uniform

from math import ceil
from numpy import array, linspace, concatenate, zeros

import logging

# Only for debugging purposes
from time import sleep

from Misc.Prefix import formatPrefix

class StitchedSweep():
    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

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
            self.ui.StitchedSweepSweeperSelection.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.ui.StitchedSweepLockInSelection.addItem(lockin)

        # Reset selections
        self.ui.sweepAndLockSelectLockIn.setCurrentIndex(0)
        self.ui.sweepAndLockSelectSweeper.setCurrentIndex(0)

        # Read back instrument settings when the selection is changed
        self.ui.sweepAndLockSelectLockIn.currentIndexChanged.connect(self.resetLockIn)
        self.ui.sweepAndLockSelectSweeper.currentIndexChanged.connect(self.resetSweeper)

        # Recalculate data point estimates when settings change
        self.ui.sweepAndLockSweepTime.valueChanged.connect(self.updateEstimates)
        self.ui.sweepAndLockSampleFreq.currentIndexChanged.connect(self.updateEstimates)


    def prepare(self):
        logging.debug("Started Sweep and Lock-in measurement")
        # Sweeper setup
        sweepTime = self.ui.sweepAndLockSweepTime.value()
        startFreq = self.ui.sweepAndLockStartFreq.value()
        endFreq = self.ui.sweepAndLockEndFreq.value()

        self.sweeper.setupSweep(startFreq, endFreq, sweepTime)

        # Update sweep time in case it got clamped
        # From here on, we can use this value, as it's not changed
        # until the end of the measurement
        self.sweepTime = self.sweeper.readSweepTime()

        # Set power level and turn off continous sweep
        self.sweeper.setPowerLevel(self.ui.sweepAndLockPower.value())
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

        self.curve1 = self.plotter.emptyPlot("r")
        self.curve2 = self.plotter.emptyPlot("g")

        # Reset total progress bar
        self.ui.sweepAndLockTotalProgress.setRange(0, self.totalRuns)
        self.ui.sweepAndLockTotalProgress.setValue(0)

        # Set total step count per run
        self.totalSteps = 2*(ceil(self.sweepTime) + 1)

        self.startRun()

    def startRun(self):

        sampleFreq = self.ui.sweepAndLockSampleRate.currentIndex()
        (self.numPoints, self.padding) = self.lockin.armTimedMeasurement(self.sweepTime, sampleFreq)
        logging.debug(f"{self.numPoints} points will be measured")

        # Reset progress bar and step counter
        self.ui.sweepAndLockProgress.setRange(0, self.totalSteps)
        self.ui.sweepAndLockProgress.setValue(0)
        self.currentStep = 0

        # Start sweep
        logging.debug(f"Sweeper state: {self.sweeper.query('*OPC?')}")
        self.sweeper.powerOn()
        self.sweeper.startSweep()

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

        # Pause lock-in and stop sweeper to stop data collection
        #self.sweeper.stopSweep()
        self.lockin.pause()

        # Extract both datasets
        logging.debug(f"{self.numPoints} points will be extracted")
        logging.debug(f"The buffer contains {self.lockin.query('SPTS?')}")
        data1 = array(self.lockin.readBuffer(1, 0, self.numPoints))
        logging.debug(f"Register 1 extracted")
        data2 = array(self.lockin.readBuffer(2, 0, self.numPoints))
        logging.debug(f"Register 2 extracted")

        # Pad the data if necessary
        padding = zeros(self.padding)
        data1 = concatenate((data1, padding))
        data2 = concatenate((data2, padding))
        logging.info("Data extracted")


        if self.currentRun == 1:
            # If it's the first run, save our new data
            self.data1 = data1
            self.data2 = data2

            # Read back sweep parameters from the instrument
            start, end, _ = self.sweeper.readSweepParams()
            self.freqs = linspace(start, end, len(self.data1))

            # Plot the first set of data 
            self.curve1.setData(self.freqs, self.data1)
            self.curve2.setData(self.freqs, self.data2)

        else:
            # If there's already data, we add our new data to it
            # elementwise
            self.data1 += data1
            self.data2 += data2

            normalized1 = self.data1 / self.currentRun
            normalized2 = self.data2 / self.currentRun

            # We update the y axis data with our new average
            self.curve1.setData(self.freqs, normalized1)
            self.curve2.setData(self.freqs, normalized2)

        # Set progress bar to full
        pbar.setRange(0, 1)
        pbar.setValue(1)

        # Update the total progress
        self.ui.sweepAndLockTotalProgress.setValue(self.currentRun)

        # Run again if we're not done yet
        if self.totalRuns > self.currentRun:
            self.currentRun += 1
            self.startRun()


    def selected(self):
        self.ui.expStack.setCurrentIndex(3)
        self.resetLockIn()
        self.resetSweeper()

    def resetSweeper(self):
        self.sweeper = self.devices["sweeper"][self.ui.StitchedSweepSweeperSelection.currentText()]

        # Power
        currentPower = self.sweeper.readPowerLevel()
        self.ui.StitchedSweepPower.setValue(currentPower)
        self.ui.StitchedSweepPower.setRange(*self.sweeper.powerRange)

        # Sweep limits
        start, end, time = self.sweeper.readSweepParams()
        self.ui.StitchedSweepStartFreq.setValue(start)
        self.ui.StitchedSweepEndFreq.setValue(end)
        self.ui.StitchedSweepSweepTime.setValue(time)

        self.ui.StitchedSweepStartFreq.setRange(*self.sweeper.freqRange)
        self.ui.StitchedSweepEndFreq.setRange(*self.sweeper.freqRange)
        self.ui.StitchedSweepSweepTime.setRange(*self.sweeper.timeRange)

        self.updateEstimates()

    def resetLockIn(self):
        self.lockin = self.devices["lockin"][self.ui.StitchedSweepLockInSelection.currentText()]

        self.ui.StitchedSweepSens.clear()
        for sens in self.lockin.sensList:
            self.ui.StitchedSweepSens.addItem(formatPrefix(sens, 'V'))

        currentSens = self.lockin.readSens()
        self.ui.StitchedSweepSens.setCurrentIndex(currentSens)

        self.ui.StitchedSweepTau.clear()
        for tau in self.lockin.tauList:
            self.ui.StitchedSweepTau.addItem(formatPrefix(tau, 's'))

        currentTau = self.lockin.readTau()
        self.ui.StitchedSweepTau.setCurrentIndex(currentTau)

        self.ui.StitchedSweepSampleRate.clear()
        for sample in self.lockin.sampleFreqList:
            self.ui.StitchedSweepSampleRate.addItem(formatPrefix(sample, 'Hz'))

        currentSampleRate = self.lockin.readSampleRate()
        self.ui.StitchedSweepSampleRate.setCurrentIndex(currentSampleRate)

        currentFreq = self.lockin.readFreq()
        self.ui.StitchedSweepLockInFreq.setValue(currentFreq)

        self.updateEstimates()

    def updateEstimates(self):

        logging.debug("Expected data points updated")
        sampleFreqIndex = self.ui.StitchedSweepSampleRate.currentIndex()
        sampleFreq = self.lockin.sampleFreqList[sampleFreqIndex]
        maxBins = self.lockin.bufferSize
        sweepTime = self.ui.sweepAndLockSweepTime.value()

        points = round(sweepTime*sampleFreq)

        self.ui.sweepAndLockDataPointsLabel.setText(f"{points} ({maxBins} max)")
