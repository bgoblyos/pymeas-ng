from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from random import uniform

from math import ceil

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

        for sweeper in self.devices["sweeper"]:
            self.sweepAndLockSelectSweeper.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.sweepAndLockSelectLockIn.addItem(lockin)

        self.sweepAndLockSelectLockIn.currentIndexChanged.connect(self.sweepAndLockInResetLockIn)
        self.sweepAndLockSelectSweeper.currentIndexChanged.connect(self.sweepAndLockInResetSweeper)

        self.sweepAndLockSelectLockIn.setCurrentIndex(0)
        self.sweepAndLockSelectSweeper.setCurrentIndex(0)

        
    def sweepAndLockInStart(self):
        logging.debug("Started Sweep and Lock-in measurement")
        # Sweeper setup
        sweeper = self.sweepAndLockInCurrentSweeper
        sweepTime = self.sweepAndLockSweepTime.value()

        # Lock-in setup
        lockin = self.sweepAndLockInCurrentLockIn

        freq = self.sweepAndLockFreq.value()
        lockin.setFreq(freq)

        tau = self.sweepAndLockTau.currentIndex()
        lockin.setTau(tau)

        sens = self.sweepAndLockSens.currentIndex()
        lockin.setSens(sens)
        
        sampleFreq = self.sweepAndLockSampleFreq.currentIndex()
        (self.sweepAndLockInNumPoints, self.sweepAndLockInPadding) = lockin.armTimedMeasurement(sweepTime, sampleFreq)


        self.sweepAndLockInTotalSteps = 2*(ceil(sweepTime) + 2)
        self.sweepAndLockInStepCounter = 0

        self.sweepAndLockProgress.setRange(0, self.sweepAndLockInTotalSteps)
        self.sweepAndLockProgress.setValue(0)
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

        # Copy data and plot it
        lockin = self.sweepAndLockInCurrentLockIn
        lockin.pause()
        sleep(2)

        pbar.setRange(0, 1)
        pbar.setValue(1)

        logging.info("Data extracted")

    def sweepAndLockInHandler(self):
        self.expStack.setCurrentIndex(1)
        self.sweepAndLockInResetLockIn()
        self.sweepAndLockInResetSweeper()

    def sweepAndLockInResetSweeper(self):
        self.sweepAndLockInCurrentSweeper = self.devices["sweeper"][self.sweepAndLockSelectSweeper.currentText()]
        # Update power limits
        self.sweepAndLockInUpdateTime()
        
    def sweepAndLockInResetLockIn(self):
        self.sweepAndLockInCurrentLockIn = self.devices["lockin"][self.sweepAndLockSelectLockIn.currentText()]
        
        self.sweepAndLockSens.clear()
        for sens in self.sweepAndLockInCurrentLockIn.sensList:
            self.sweepAndLockSens.addItem(formatPrefix(sens, 'V'))

        currentSens = self.sweepAndLockInCurrentLockIn.readSens()
        self.sweepAndLockSens.setCurrentIndex(currentSens)

        self.sweepAndLockTau.clear()
        for tau in self.sweepAndLockInCurrentLockIn.tauList:
            self.sweepAndLockTau.addItem(formatPrefix(tau, 's'))

        currentTau = self.sweepAndLockInCurrentLockIn.readTau()
        self.sweepAndLockTau.setCurrentIndex(currentTau)

        self.sweepAndLockSampleFreq.clear()
        for sample in self.sweepAndLockInCurrentLockIn.sampleFreqList:
            self.sweepAndLockSampleFreq.addItem(formatPrefix(sample, 'Hz'))

        currentSampleFreq = self.sweepAndLockInCurrentLockIn.readSampleRate()
        self.sweepAndLockSampleFreq.setCurrentIndex(currentSampleFreq)
        
    def sweepAndLockInUpdateTime(self):
        print("lololo")
