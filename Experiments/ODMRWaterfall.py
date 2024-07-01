import logging
import numpy as np

from PySide6.QtCore import QTimer

from Misc.Prefix import formatPrefix, formatTime
from Misc.Exporter import promptMultiExport

class ODMRWaterfall():
    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

        # Add devices to selection box
        for sweeper in self.devices["sweeper"]:
            self.ui.ODMRWaterfallSweeperSelection.addItem(sweeper)
        for lockin in self.devices["lockin"]:
            self.ui.ODMRWaterfallLockInSelection.addItem(lockin)
        for psu in self.devices["psu"]:
            self.ui.ODMRWaterfallPSUSelection.addItem(psu)

        # Connect buttons
        self.ui.ODMRWaterfallStart.clicked.connect(self.prepare)
        self.ui.ODMRWaterfallCancel.clicked.connect(self.cancel)
        self.ui.ODMRWaterfallExport.clicked.connect(self.export)

        # Disable cancel button
        self.ui.ODMRWaterfallCancel.setEnabled(False)

        # Set up timer for progress bar
        # (and for waiting until the sweep is done)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateSweepProgress)

        # Set up timer for waiting while the current settles
        self.PSUSettleTimer = QTimer()
        self.PSUSettleTimer.setInterval(5000)
        self.PSUSettleTimer.timeout.connect(self.startSweep)
        self.PSUSettleTimer.setSingleShot(True)

        # Set up timer for gracefully stopping the power supply
        self.PSUStopTimer = QTimer()
        self.PSUStopTimer.setInterval(200)
        self.PSUStopTimer.timeout.connect(self.PSUGracefulStopStep)

        # Set up progress bars
        self.sweepProgress = self.ui.ODMRWaterfallSweepProgress
        self.totalProgress = self.ui.ODMRWaterfallTotalProgress
        self.sweepProgress.setValue(0)
        self.totalProgress.setValue(0)

        # Set up display selection radio buttons
        self.ui.ODMRWaterfallDisplay1Radio.toggled.connect(self.displayToggleChanged)
        self.displayToggleChanged()

        # Read back instrument settings when the selection is changed
        self.ui.ODMRWaterfallLockInSelection.currentIndexChanged.connect(self.resetLockIn)
        self.ui.ODMRWaterfallSweeperSelection.currentIndexChanged.connect(self.resetSweeper)
        self.ui.ODMRWaterfallPSUSelection.currentIndexChanged.connect(self.resetPSU)

        # Recalculate data point estimates when settings change
        self.ui.ODMRWaterfallSweepTime.valueChanged.connect(self.updateEstimates)
        self.ui.ODMRWaterfallLockInSampleRate.currentIndexChanged.connect(self.updateEstimates)
        self.ui.ODMRWaterfallPowerSteps.valueChanged.connect(self.updateEstimates)
        self.ui.ODMRWaterfallSettleTime.valueChanged.connect(self.updateEstimates)
        self.ui.ODMRWaterfallInitialSettleTime.valueChanged.connect(self.updateEstimates)

        # Initialize data storage with None
        self.data = None
        self.sweepRange = None
        self.currents = None

        logging.debug("Waterfall initialized")

    def selected(self):
        # Switch to correct page
        self.ui.expStack.setCurrentIndex(2)

        # Read back instrument settings
        self.resetLockIn()
        self.resetSweeper()
        self.resetPSU()

    def displayToggleChanged(self):
        if self.ui.ODMRWaterfallDisplay1Radio.isChecked():
            self.channel = 1
            self.ui.ODMRWaterfallDisplay1.setEnabled(True)
            self.ui.ODMRWaterfallDisplay2.setEnabled(False)
        else:
            self.channel = 2
            self.ui.ODMRWaterfallDisplay2.setEnabled(True)
            self.ui.ODMRWaterfallDisplay1.setEnabled(False)

    def prepare(self):
        logging.debug("Started ODMR Waterfall measurement")

        # Reset data storage
        self.data = None

        # Enable cancel button and disable start
        self.ui.ODMRWaterfallCancel.setEnabled(True)
        self.ui.ODMRWaterfallStart.setEnabled(False)

        # Sweeper setup
        sweepTime = self.ui.ODMRWaterfallSweepTime.value()
        startFreq = self.ui.ODMRWaterfallSweepStart.value()
        endFreq = self.ui.ODMRWaterfallSweepEnd.value()

        self.sweeper.setupSweep(startFreq, endFreq, sweepTime)
        self.sweepRange = (startFreq, endFreq)

        # Update sweep time in case it got clamped
        # From here on, we can use this value, as it's not changed
        # until the end of the measurement
        self.sweepTime = self.sweeper.readSweepTime()

        # Set power level and turn off continous sweep
        self.sweeper.setPowerLevel(self.ui.ODMRWaterfallSweepPower.value())
        self.sweeper.setContSweep(False)

        # Lock-in setup
        freq = self.ui.ODMRWaterfallLockInFreq.value()
        self.lockin.setFreq(freq)

        tau = self.ui.ODMRWaterfallLockInTau.currentIndex()
        self.lockin.setTau(tau)

        sens = self.ui.ODMRWaterfallLockInSens.currentIndex()
        self.lockin.setSens(sens)

        if self.channel == 1:
            disp = self.ui.ODMRWaterfallDisplay1.currentIndex()
            self.lockin.setDisplay(1, disp)
        else:
            disp = self.ui.ODMRWaterfallDisplay2.currentIndex()
            self.lockin.setDisplay(2, disp)

        # Read in PSU settings
        self.startCurrent = self.ui.ODMRWaterfallStartCurrent.value()
        self.endCurrent = self.ui.ODMRWaterfallEndCurrent.value()
        self.currentSteps = self.ui.ODMRWaterfallPowerSteps.value()
        self.currentCounter = 0
        self.currents = np.linspace(self.startCurrent, self.endCurrent, self.currentSteps)

        self.voltage = self.ui.ODMRWaterfallVoltage.value()

        # Reset total progress bar
        self.ui.ODMRWaterfallTotalProgress.setRange(0, self.currentSteps)
        self.ui.sweepAndLockTotalProgress.setValue(0)

        # Set total step count per run
        self.sweepSteps = 2*(np.ceil(self.sweepTime) + 1)

        self.setupSweep()

    def setupSweep(self):
        # Set up power supply
        self.actualCurrent = self.currents[self.currentCounter]

        if abs(self.actualCurrent) < self.psu.currentRange[0]:
            logging.info("Current too low, power source turned off")
            self.currents[self.currentCounter] = 0
            self.psu.disableOutput()
        else:
            if self.actualCurrent < 0:
                self.psu.setVoltage(-self.voltage)
                logging.debug('Voltage should be set to negative')
            else:
                self.psu.setVoltage(self.voltage)
                logging.debug('Voltage should be set to positive')

            self.psu.setCurrent(abs(self.actualCurrent))
            self.psu.enableOutput()


        # Set up lock-in
        sampleFreq = self.ui.ODMRWaterfallLockInSampleRate.currentIndex()
        (self.numPoints, self.padding) = self.lockin.armTimedMeasurement(self.sweepTime, sampleFreq)
        self.totalPoints = self.numPoints + self.padding
        logging.debug(f"{self.numPoints} points will be measured")


        # Reset progress bar and step counter
        self.ui.ODMRWaterfallSweepProgress.setRange(0, self.sweepSteps)
        self.ui.ODMRWaterfallSweepProgress.setValue(0)
        self.sweepCounter = 0

        #self.PSUSettleTimer.start()
        if self.currentCounter == 0:
            waitTime = round(1000 * self.ui.ODMRWaterfallInitialSettleTime.value())
        else:
            waitTime = round(1000 * self.ui.ODMRWaterfallSettleTime.value())

        self.PSUSettleTimer.setInterval(waitTime)
        self.PSUSettleTimer.start()
        logging.info(f'Waiting {waitTime} ms for PSU current to settle')

    def startSweep(self):
        # Read back PSU current after giving it time to settle
        if self.currents[self.currentCounter] != 0:
            self.currents[self.currentCounter] = self.psu.getCurrent()

        # Start sweep
        self.sweeper.powerOn()
        self.sweeper.startSweep()

        self.timer.start()
        logging.info('Current settled\nStarting sweep')

    def updateSweepProgress(self):
        # Check if the run is completed
        if self.sweepCounter >= self.sweepSteps:
            self.completeSweep()
        else:
            # Increment counter and progress bar
            self.sweepCounter += 1
            self.ui.ODMRWaterfallSweepProgress.setValue(self.sweepCounter)

    def completeSweep(self):

        # Stop the timer so updateProgress stops running
        self.timer.stop()
        logging.info("Sweep completed, extracting data")

        # Set progress bar to indeterminate
        pbar = self.sweepProgress
        pbar.setRange(0, 0)
        pbar.setValue(0)

        # Disable sweeper output
        self.sweeper.powerOff()

        # Pause lock-in and stop sweeper to stop data collection
        #self.sweeper.stopSweep()
        self.lockin.pause()

        # Extract selected dataset
        logging.debug(f"{self.numPoints} points will be extracted")
        logging.debug(f"The buffer contains {self.lockin.query('SPTS?')}")
        newdata = np.array(self.lockin.readBuffer(self.channel, 0, self.numPoints))
        logging.debug(f"Register {self.channel} extracted")

        # Pad the data if necessary
        paddingLength = self.totalPoints - len(newdata)
        newdata = np.pad(newdata, (0, paddingLength), 'constant')
        logging.info("Data extracted")

        if self.data is None:
            # If it's the first run, save our new data
            self.data = np.array([newdata])
            # Also update theplot labels
            self.plotter.setLabels("ODMR with variable magnetic field", "Frequency (GHz)", ("Electromagnet current", "A"))

        else:
            # Otherwise, concatenate it
            self.data = np.vstack((self.data, newdata))

        currentRange = (self.startCurrent, self.actualCurrent)
        logging.debug(f"Heatmap current range: {currentRange}")
        logging.debug(f"Heatmap frequency range: {self.sweepRange}")

        self.plotter.heatmap(np.transpose(self.data), self.sweepRange, currentRange)


        # Set progress bar to full
        pbar.setRange(0, 1)
        pbar.setValue(1)

        self.currentCounter += 1

        # Update the total progress
        self.totalProgress.setValue(self.currentCounter)

        # Run again if we're not done yet
        if self.currentSteps > self.currentCounter:
            self.setupSweep()
        else:
            # Else, turn off the power supply
            #self.psu.disableOutput()
            self.PSUGracefulStop()

            # And inform the user
            logging.info("Measurement completed")

            # Enable start button and disable cancel
            self.ui.ODMRWaterfallCancel.setEnabled(False)
            #self.ui.ODMRWaterfallStart.setEnabled(True)

    def cancel(self):
        # Stop sweep timer
        self.timer.stop()
        self.PSUSettleTimer.stop()

        # Disable PSU
        # self.psu.disableOutput()
        self.PSUGracefulStop()

        # Disable sweeper output
        self.sweeper.powerOff()

        # Pause lock-indata collection
        self.lockin.pause()

        # Reset progress bars
        self.sweepProgress.setRange(0, 1)
        self.sweepProgress.setValue(0)
        self.totalProgress.setRange(0, 1)
        self.totalProgress.setValue(0)

        # Enable start button and disable cancel
        self.ui.ODMRWaterfallCancel.setEnabled(False)

        logging.info("Measurement canceled")

    def export(self):
        if self.data is None:
            logging.warning("No data to be exported! Did you run the experiment?")
        elif self.currents is None:
            logging.warning("Current range not found. Did you run the experiment?")
        elif self.sweepRange is None:
            logging.warning("Sweep range not found. Did you run the experiment?")
        else:
            freqs = np.linspace(self.sweepRange[0], self.sweepRange[1], self.totalPoints)
            promptMultiExport(
                data = self.data, datatitle = 'odmrwaterfall',
                xaxis = freqs, xtitle = 'frequency',
                yaxis = self.currents, ytitle = 'current')


    def resetSweeper(self):
        self.sweeper = self.devices["sweeper"][self.ui.ODMRWaterfallSweeperSelection.currentText()]

        # Power
        currentPower = self.sweeper.readPowerLevel()
        self.ui.ODMRWaterfallSweepPower.setValue(currentPower)
        self.ui.ODMRWaterfallSweepPower.setRange(*self.sweeper.powerRange)

        # Sweep limits
        start, end, time = self.sweeper.readSweepParams()
        self.ui.ODMRWaterfallSweepStart.setValue(start)
        self.ui.ODMRWaterfallSweepEnd.setValue(end)
        self.ui.ODMRWaterfallSweepTime.setValue(time)

        self.ui.ODMRWaterfallSweepStart.setRange(*self.sweeper.freqRange)
        self.ui.ODMRWaterfallSweepEnd.setRange(*self.sweeper.freqRange)
        self.ui.ODMRWaterfallSweepTime.setRange(*self.sweeper.timeRange)

        self.updateEstimates()

    def resetLockIn(self):
        self.lockin = self.devices["lockin"][self.ui.ODMRWaterfallLockInSelection.currentText()]

        # Sensitivity
        self.ui.ODMRWaterfallLockInSens.clear()
        for sens in self.lockin.sensList:
            self.ui.ODMRWaterfallLockInSens.addItem(formatPrefix(sens, 'V'))

        currentSens = self.lockin.readSens()
        self.ui.ODMRWaterfallLockInSens.setCurrentIndex(currentSens)

        # Tau
        self.ui.ODMRWaterfallLockInTau.clear()
        for tau in self.lockin.tauList:
            self.ui.ODMRWaterfallLockInTau.addItem(formatPrefix(tau, 's'))

        currentTau = self.lockin.readTau()
        self.ui.ODMRWaterfallLockInTau.setCurrentIndex(currentTau)

        # Sample rate
        self.ui.ODMRWaterfallLockInSampleRate.clear()
        for sample in self.lockin.sampleFreqList:
            self.ui.ODMRWaterfallLockInSampleRate.addItem(formatPrefix(sample, 'Hz'))

        currentSampleFreq = self.lockin.readSampleRate()
        self.ui.ODMRWaterfallLockInSampleRate.setCurrentIndex(currentSampleFreq)

        # Display 1
        self.ui.ODMRWaterfallDisplay1.clear()
        for disp in self.lockin.display1List:
            self.ui.ODMRWaterfallDisplay1.addItem(disp)

        currentDisplay1 = self.lockin.readDisplay(1)
        self.ui.ODMRWaterfallDisplay1.setCurrentIndex(currentDisplay1)

        # Display 2
        self.ui.ODMRWaterfallDisplay2.clear()
        for disp in self.lockin.display2List:
            self.ui.ODMRWaterfallDisplay2.addItem(disp)

        currentDisplay2 = self.lockin.readDisplay(2)
        self.ui.ODMRWaterfallDisplay2.setCurrentIndex(currentDisplay2)

        # Internal oscillator frequency
        currentFreq = self.lockin.readFreq()
        self.ui.ODMRWaterfallLockInFreq.setValue(currentFreq)

        self.updateEstimates()

    def resetPSU(self):
        self.psu = self.devices["psu"][self.ui.ODMRWaterfallPSUSelection.currentText()]

        maxCurrent = self.psu.currentRange[1]
        self.ui.ODMRWaterfallStartCurrent.setMaximum(maxCurrent)
        self.ui.ODMRWaterfallStartCurrent.setMinimum(-maxCurrent)
        self.ui.ODMRWaterfallEndCurrent.setMaximum(maxCurrent)
        self.ui.ODMRWaterfallEndCurrent.setMinimum(-maxCurrent)

        current = self.psu.getCurrent()
        self.ui.ODMRWaterfallEndCurrent.setValue(current)

        voltage = self.psu.getVoltage()
        self.ui.ODMRWaterfallVoltage.setValue(voltage)

    def updateEstimates(self):
        sampleFreqIndex = self.ui.ODMRWaterfallLockInSampleRate.currentIndex()
        sampleFreq = self.lockin.sampleFreqList[sampleFreqIndex]
        maxBins = self.lockin.bufferSize
        sweepTime = self.ui.ODMRWaterfallSweepTime.value()

        points = round(sweepTime*sampleFreq)

        self.ui.ODMRWaterfallSweepResolutionLabel.setText(f"{points} ({maxBins} max)")

        currentSteps = self.ui.ODMRWaterfallPowerSteps.value()
        self.ui.ODMRWaterfallTotalResolutionLabel.setText(f"{points} x {currentSteps}")

        roundTime = sweepTime + self.ui.ODMRWaterfallSettleTime.value() + 2
        firstRoundExtra = self.ui.ODMRWaterfallInitialSettleTime.value() - self.ui.ODMRWaterfallSettleTime.value()

        expectedTime = currentSteps * roundTime + firstRoundExtra
        timeStr = formatTime(expectedTime)
        self.ui.ODMRWaterfallExpectedTimeLabel.setText(timeStr)

        worstTime = currentSteps * (roundTime + 5) + firstRoundExtra
        timeStr = formatTime(worstTime)
        self.ui.ODMRWaterfallWorstTimeLabel.setText(timeStr)

    def PSUGracefulStop(self):
        self.totalProgress.setRange(0,0)
        self.totalProgress.setValue(0)

        current = self.psu.getCurrent()
        mincurrent = self.psu.currentRange[0]

        currentStep = self.ui.ODMRWaterfallShutdownStepSize.value()
        waitTime = round(1000 * self.ui.ODMRWaterfallShutdownInterval.value())
        self.PSUStopTimer.setInterval(waitTime)

        self.PSUStopCurrents = np.flip(np.arange(mincurrent, current, currentStep))
        self.PSUStopCounter = 0
        self.PSUStopSteps = len(self.PSUStopCurrents)

        # Disable start button while shutting down the power supply
        self.ui.ODMRWaterfallStart.setEnabled(False)
        self.PSUStopTimer.start()

    def PSUGracefulStopStep(self):
        if self.PSUStopCounter >= self.PSUStopSteps:
            self.PSUStopTimer.stop()
            self.psu.disableOutput()
            self.ui.ODMRWaterfallStart.setEnabled(True)

            self.totalProgress.setRange(0,1)
            self.totalProgress.setValue(0)

            logging.info("Power supply successfully shut down")
        else:
            current = self.PSUStopCurrents[self.PSUStopCounter]
            self.psu.setCurrent(current)
            self.PSUStopCounter += 1
