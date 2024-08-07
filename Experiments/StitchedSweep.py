from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from random import uniform

from math import ceil
from numpy import array, linspace, concatenate, zeros, maximum

import logging

# Only for debugging purposes
from time import sleep

from Misc.Prefix import formatPrefix

# Exporter
from Misc.Exporter import promptSweepExport

class StitchedSweep():
    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

        # Initialize data
        self.data1 = array([])
        self.data2 = array([])
        self.freqs = array([])

        # Connect start button
        self.ui.StitchedSweepStartButton.clicked.connect(self.prepare)
        self.ui.StitchedSweepStartButton.setEnabled(True)

        # Connect export button
        self.ui.StitchedSweepExportButton.clicked.connect(self.export)

        # Connect cancel button
        self.ui.StitchedSweepCancelButton.clicked.connect(self.cancel)
        self.ui.StitchedSweepCancelButton.setEnabled(False)

        # Set up timer for progress bar
        # (and for waiting until the sweep is done)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateProgress)

        # Reset progress bars
        self.ui.StitchedSweepSweepProgress.setValue(0)
        self.ui.StitchedSweepTotalProgress.setValue(0)

        # Add devices to selection box
        for sweeper in self.devices["sweeper"]:
            self.ui.StitchedSweepSweeperSelection.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.ui.StitchedSweepLockInSelection.addItem(lockin)

        # Reset selections
        self.ui.StitchedSweepLockInSelection.setCurrentIndex(0)
        self.ui.StitchedSweepSweeperSelection.setCurrentIndex(0)

        # Read back instrument settings when the selection is changed
        self.ui.StitchedSweepLockInSelection.currentIndexChanged.connect(self.resetLockIn)
        self.ui.StitchedSweepSweeperSelection.currentIndexChanged.connect(self.resetSweeper)

        # Recalculate data point estimates when settings change
        self.ui.sweepAndLockSweepTime.valueChanged.connect(self.updateEstimates)
        self.ui.sweepAndLockSampleFreq.currentIndexChanged.connect(self.updateEstimates)

        # Set up display selection checkboxes
        self.ui.StitchedSweepDisp1Check.checkStateChanged.connect(self.display1Toggled)
        self.display1Toggled()
        self.ui.StitchedSweepDisp2Check.checkStateChanged.connect(self.display2Toggled)
        self.display2Toggled()

    def export(self):
        promptSweepExport(self.freqs, self.data1, self.data2)

    def cancel(self):
        self.ui.StitchedSweepCancelButton.setEnabled(False)

        self.timer.stop()

        # Disable sweeper output
        self.sweeper.powerOff()

        self.lockin.pause()

        # Reset sweep progress bar
        self.ui.StitchedSweepSweepProgress.setRange(0, 1)
        self.ui.StitchedSweepSweepProgress.setValue(0)

        # Reset total progress bar
        self.ui.StitchedSweepTotalProgress.setRange(0, 1)
        self.ui.StitchedSweepTotalProgress.setValue(0)

        self.ui.StitchedSweepStartButton.setEnabled(True)

    def display1Toggled(self):
        if self.ui.StitchedSweepDisp1Check.isChecked():
            self.ui.StitchedSweepDisp1Selection.setEnabled(True)
        else:
            self.ui.StitchedSweepDisp1Selection.setEnabled(False)

    def display2Toggled(self):
        if self.ui.StitchedSweepDisp2Check.isChecked():
            self.ui.StitchedSweepDisp2Selection.setEnabled(True)
        else:
            self.ui.StitchedSweepDisp2Selection.setEnabled(False)

    def prepare(self):
        self.channel1 = self.ui.StitchedSweepDisp1Check.isChecked()
        self.channel2 = self.ui.StitchedSweepDisp2Check.isChecked()
        
        if not (self.channel1 or self.channel2):
            logging.warning("At least one channel must be enabled!")
            return
        
        if self.channel1:
            disp = self.ui.StitchedSweepDisp1Selection.currentIndex()
            self.lockin.setDisplay(1, disp)

        if self.channel2:
            disp = self.ui.StitchedSweepDisp2Selection.currentIndex()
            self.lockin.setDisplay(2, disp)
        
        self.data1 = array([])
        self.data2 = array([])
        self.freqs = array([])
        
        #TODO: Disable start and enable cancel
        self.ui.StitchedSweepStartButton.setEnabled(False)
        self.ui.StitchedSweepCancelButton.setEnabled(True)

        logging.debug("Started Stitched Sweep measurement")
       
        self.numSweeps = self.ui.StitchedSweepNumSweeps.value()

        self.overlap = self.ui.StitchedSweepOverlap.value() / 100
        lengthFactor = 1 + self.overlap

        self.discard = self.overlap = self.ui.StitchedSweepDiscard.value()

        # Sweeper parameters
        self.sweepTime = self.ui.StitchedSweepSweepTime.value()
        startFreq = self.ui.StitchedSweepStartFreq.value()
        endFreq = self.ui.StitchedSweepEndFreq.value()
        self.endFreqs, stepSize = linspace(startFreq, endFreq, self.numSweeps + 1, retstep=True)
        self.endFreqs = self.endFreqs[1:]
        self.startFreqs = maximum(self.endFreqs - (stepSize * lengthFactor), startFreq)
        
        self.sweepCounter = 0

        # Set power level and turn off continous sweep
        self.sweeper.setPowerLevel(self.ui.StitchedSweepPower.value())
        self.sweeper.setContSweep(False)

        # Lock-in setup
        freq = self.ui.StitchedSweepLockInFreq.value()
        self.lockin.setFreq(freq)

        tau = self.ui.StitchedSweepTau.currentIndex()
        self.lockin.setTau(tau)

        sens = self.ui.StitchedSweepSens.currentIndex()
        self.lockin.setSens(sens)

        self.data1 = array([])
        self.data2 = array([])

        self.curve1 = self.plotter.emptyPlot("r")
        self.curve2 = self.plotter.emptyPlot("g")

        # Reset total progress bar
        self.ui.StitchedSweepTotalProgress.setRange(0, self.numSweeps)
        self.ui.StitchedSweepTotalProgress.setValue(0)

        # Set total step count per run
        self.totalSteps = 2*(ceil(self.sweepTime) + 1)

        self.startRun()

    def startRun(self):
        startFreq = self.startFreqs[self.sweepCounter]
        endFreq = self.endFreqs[self.sweepCounter]

        # TODO: Update these
        self.sweeper.setupSweep(startFreq, endFreq, self.sweepTime)

        # Update sweep time in case it got clamped
        # From here on, we can use this value, as it's not changed
        # until the end of the measurement
        self.sweepTime = self.sweeper.readSweepTime()

        sampleFreq = self.ui.StitchedSweepSampleRate.currentIndex()
        (self.numPoints, self.padding) = self.lockin.armTimedMeasurement(self.sweepTime, sampleFreq)
        logging.debug(f"{self.numPoints} points will be measured")

        # Reset progress bar and step counter
        self.ui.StitchedSweepSweepProgress.setRange(0, self.totalSteps)
        self.ui.StitchedSweepSweepProgress.setValue(0)
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
            self.ui.StitchedSweepSweepProgress.setValue(self.currentStep)

    def completeRun(self):

        # Stop the timer so updateProgress stops running
        self.timer.stop()
        logging.info("Sweep completed, extracting data...")
        

        # Set progress bar to indeterminate
        pbar = self.ui.StitchedSweepSweepProgress
        pbar.setRange(0, 0)
        pbar.setValue(0)

        # Disable sweeper output
        self.sweeper.powerOff()

        # Pause lock-in and stop sweeper to stop data collection
        #self.sweeper.stopSweep()
        self.lockin.pause()

        padding = zeros(self.padding)
        
        # Extract dataset(s)
        logging.debug(f"{self.numPoints} points will be extracted")
        logging.debug(f"The buffer contains {self.lockin.query('SPTS?')}")
        if self.channel1:
            newdata = array(self.lockin.readBuffer(1, 0, self.numPoints))[self.discard:]
            logging.debug(f"Register 1 extracted")
            self.data1 = concatenate((self.data1, newdata, padding))

        if self.channel2:
            newdata = array(self.lockin.readBuffer(2, 0, self.numPoints))[self.discard:]
            logging.debug(f"Register 2 extracted")
            self.data1 = concatenate((self.data2, newdata, padding))

        logging.info("Data extracted")

        # Read back sweep parameters from the instrument
        start, end, _ = self.sweeper.readSweepParams()
        newfreqs = linspace(start, end, self.numPoints, endpoint=False)[self.discard:]
        self.freqs = concatenate((self.freqs, newfreqs))

        # Plot the data 
        if self.channel1:
            self.curve1.setData(self.freqs, self.data1)
        if self.channel2:
            self.curve2.setData(self.freqs, self.data2)

        # Set progress bar to full
        pbar.setRange(0, 1)
        pbar.setValue(1)

        # Update the total progress
        self.sweepCounter += 1
        self.ui.StitchedSweepTotalProgress.setValue(self.sweepCounter)

        # Run again if we're not done yet
        if self.numSweeps > self.sweepCounter:
            self.startRun()
        else:
            self.ui.StitchedSweepStartButton.setEnabled(True)


    def selected(self):
        self.ui.expStack.setCurrentIndex(3)
        self.resetLockIn()
        self.resetSweeper()

    def resetSweeper(self):
        self.sweeper = self.devices["sweeper"][self.ui.StitchedSweepSweeperSelection.currentText()]

        # Power
        currentPower = self.sweeper.readPowerLevel()
        self.ui.StitchedSweepPower.setRange(*self.sweeper.powerRange)
        self.ui.StitchedSweepPower.setValue(currentPower)

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

        # Display 1
        self.ui.StitchedSweepDisp1Selection.clear()
        for disp in self.lockin.display1List:
            self.ui.StitchedSweepDisp1Selection.addItem(disp)

        currentDisplay1 = self.lockin.readDisplay(1)
        self.ui.StitchedSweepDisp1Selection.setCurrentIndex(currentDisplay1)

        # Display 2
        self.ui.StitchedSweepDisp2Selection.clear()
        for disp in self.lockin.display2List:
            self.ui.StitchedSweepDisp2Selection.addItem(disp)

        currentDisplay2 = self.lockin.readDisplay(2)
        self.ui.StitchedSweepDisp2Selection.setCurrentIndex(currentDisplay2)

        self.updateEstimates()

    def updateEstimates(self):

        logging.debug("Expected data points updated")
        sampleFreqIndex = self.ui.StitchedSweepSampleRate.currentIndex()
        sampleFreq = self.lockin.sampleFreqList[sampleFreqIndex]
        maxBins = self.lockin.bufferSize
        sweepTime = self.ui.sweepAndLockSweepTime.value()

        points = round(sweepTime*sampleFreq)

        self.ui.StitchedSweep.setText(f"{points} ({maxBins} max)")
