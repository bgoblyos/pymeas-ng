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
    def __setup__(self):
        self.sweepAndLockStart.clicked.connect(self.sweepAndLockInStart)
        self.sweepAndLockInTimer = QTimer()
        self.sweepAndLockInTimer.setInterval(500)
        self.sweepAndLockInTimer.timeout.connect(self.sweepAndLockInUpdateProgress)
        self.sweepAndLockProgress.setValue(0)
        self.sweepAndLockTotalProgress.setValue(0)

        for sweeper in self.devices["sweeper"]:
            self.sweepAndLockSelectSweeper.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.sweepAndLockSelectLockIn.addItem(lockin)

        self.sweepAndLockSelectLockIn.currentIndexChanged.connect(self.sweepAndLockInResetLockIn)
        self.sweepAndLockSelectSweeper.currentIndexChanged.connect(self.sweepAndLockInResetSweeper)

        self.sweepAndLockSelectLockIn.setCurrentIndex(0)
        self.sweepAndLockSelectSweeper.setCurrentIndex(0)

        # Recalculate data point estimates
        self.sweepAndLockSweepTime.valueChanged.connect(self.sweepAndLockInUpdateTime)
        self.sweepAndLockSampleFreq.currentIndexChanged.connect(self.sweepAndLockInUpdateTime)

        
    def sweepAndLockInStart(self):
        logging.debug("Started Sweep and Lock-in measurement")
        # Sweeper setup
        sweeper = self.sweepAndLockInCurrentSweeper

        sweepTime = self.sweepAndLockSweepTime.value()
        startFreq = self.sweepAndLockStartFreq.value()
        endFreq = self.sweepAndLockEndFreq.value()

        sweeper.setupSweep(startFreq, endFreq, sweepTime)
        # Update sweep time in case it got clamped
        sweepTime = sweeper.readSweepTime()

        sweeper.setPowerLevel(self.sweepAndLockPower.value())
        sweeper.setContSweep(False)

        # Lock-in setup
        lockin = self.sweepAndLockInCurrentLockIn

        freq = self.sweepAndLockFreq.value()
        lockin.setFreq(freq)

        tau = self.sweepAndLockTau.currentIndex()
        lockin.setTau(tau)

        sens = self.sweepAndLockSens.currentIndex()
        lockin.setSens(sens)

        self.sweepAndLockInNumRuns = self.sweepAndLockNumRuns.value()
        self.sweepAndLockInCurrentRun = 1

        self.sweepAndLockInData = array([])

        self.sweepAndLockTotalProgress.setRange(0, self.sweepAndLockInNumRuns)
        self.sweepAndLockTotalProgress.setValue(0)

        self.sweepAndLockInStartRun()

    def sweepAndLockInStartRun(self):
        sweeper = self.sweepAndLockInCurrentSweeper
        lockin = self.sweepAndLockInCurrentLockIn

        sweepTime = sweeper.readSweepTime()
        sampleFreq = self.sweepAndLockSampleFreq.currentIndex()
        (self.sweepAndLockInNumPoints, self.sweepAndLockInPadding) = lockin.armTimedMeasurement(sweepTime, sampleFreq)


        self.sweepAndLockInTotalSteps = 2*(ceil(sweepTime) + 1)
        self.sweepAndLockInStepCounter = 0

        self.sweepAndLockProgress.setRange(0, self.sweepAndLockInTotalSteps)
        self.sweepAndLockProgress.setValue(0)

        # Start sweep
        sweeper.powerOn()
        sweeper.startSweep()

        self.sweepAndLockInTimer.start()
        #self.sweepAndLockInUpdateProgress()

    def sweepAndLockInUpdateProgress(self):
        if self.sweepAndLockInStepCounter >= self.sweepAndLockInTotalSteps:
            self.sweepAndLockInComplete()
        else:
            self.sweepAndLockInStepCounter += 1
            self.sweepAndLockProgress.setValue(self.sweepAndLockInStepCounter)


    def sweepAndLockInComplete(self):
        self.sweepAndLockInTimer.stop()
        logging.info("Sweep completed, extracting data...")
        pbar = self.sweepAndLockProgress
        pbar.setRange(0, 0)
        pbar.setValue(0)

        # Disable sweeper output
        self.sweepAndLockInCurrentSweeper.powerOff()

        # Copy data and plot it
        lockin = self.sweepAndLockInCurrentLockIn
        sweeper = self.sweepAndLockInCurrentSweeper

        lockin.pause()
        data = array(lockin.readBuffer(1, 0, self.sweepAndLockInNumPoints))
        padding = zeros(self.sweepAndLockInPadding)
        data = concatenate((data, padding))
        logging.info("Data extracted")
        if len(self.sweepAndLockInData) == 0:
            self.sweepAndLockInData = data
        else:
            self.sweepAndLockInData += data

        pbar.setRange(0, 1)
        pbar.setValue(1)

        self.sweepAndLockTotalProgress.setValue(self.sweepAndLockInCurrentRun)

        if self.sweepAndLockInNumRuns == self.sweepAndLockInCurrentRun:
            # Normalize data
            self.sweepAndLockInData /= self.sweepAndLockInNumRuns
        
            start, end, _ = sweeper.readSweepParams()
            freqs = linspace(start, end, len(self.sweepAndLockInData))
            self.plot(freqs, self.sweepAndLockInData)
        else:
            self.sweepAndLockInCurrentRun += 1
            self.sweepAndLockInStartRun()
            

    def sweepAndLockInHandler(self):
        self.expStack.setCurrentIndex(1)
        self.sweepAndLockInResetLockIn()
        self.sweepAndLockInResetSweeper()

    def sweepAndLockInResetSweeper(self):
        self.sweepAndLockInCurrentSweeper = self.devices["sweeper"][self.sweepAndLockSelectSweeper.currentText()]
        sweeper = self.sweepAndLockInCurrentSweeper
        # Power
        currentPower = sweeper.readPowerLevel()
        self.sweepAndLockPower.setValue(currentPower)
        self.sweepAndLockPower.setRange(*sweeper.powerRange)

        # Sweep limits
        start, end, time = sweeper.readSweepParams()
        self.sweepAndLockStartFreq.setValue(start)
        self.sweepAndLockEndFreq.setValue(end)
        self.sweepAndLockSweepTime.setValue(time)

        self.sweepAndLockStartFreq.setRange(*sweeper.freqRange)
        self.sweepAndLockEndFreq.setRange(*sweeper.freqRange)
        self.sweepAndLockSweepTime.setRange(*sweeper.timeRange)

        self.sweepAndLockInUpdateTime()
        
    def sweepAndLockInResetLockIn(self):
        self.sweepAndLockInCurrentLockIn = self.devices["lockin"][self.sweepAndLockSelectLockIn.currentText()]
        lockin = self.sweepAndLockInCurrentLockIn

        self.sweepAndLockSens.clear()
        for sens in lockin.sensList:
            self.sweepAndLockSens.addItem(formatPrefix(sens, 'V'))

        currentSens = lockin.readSens()
        self.sweepAndLockSens.setCurrentIndex(currentSens)

        self.sweepAndLockTau.clear()
        for tau in lockin.tauList:
            self.sweepAndLockTau.addItem(formatPrefix(tau, 's'))

        currentTau = lockin.readTau()
        self.sweepAndLockTau.setCurrentIndex(currentTau)

        self.sweepAndLockSampleFreq.clear()
        for sample in lockin.sampleFreqList:
            self.sweepAndLockSampleFreq.addItem(formatPrefix(sample, 'Hz'))

        currentSampleFreq = self.sweepAndLockInCurrentLockIn.readSampleRate()
        self.sweepAndLockSampleFreq.setCurrentIndex(currentSampleFreq)

        currentFreq = lockin.readFreq()
        self.sweepAndLockFreq.setValue(currentFreq)
        
    def sweepAndLockInUpdateTime(self):
        logging.debug("Time estimations should be updated now")
        sampleFreqIndex = self.sweepAndLockSampleFreq.currentIndex()
        sampleFreq = self.sweepAndLockInCurrentLockIn.sampleFreqList[sampleFreqIndex]
        maxBins = self.sweepAndLockInCurrentLockIn.bufferSize
        sweepTime = self.sweepAndLockSweepTime.value()

        logging.debug(maxBins)
        points = round(sweepTime*sampleFreq)
        maxTime = round(maxBins/sampleFreq)

        self.sweepAndLockMaxTimeLabel.setText(f"{maxTime} s")
        self.sweepAndLockDataPointsLabel.setText(f"{points} ({maxBins} max)")
