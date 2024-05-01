from PySide6.QtWidgets import *

from random import uniform

import Devices.Common
import Devices.LockIn
import Devices.DeviceManager

from Misc.Prefix import formatPrefix

class GenericLockIn():
    def __init__(self, ui):

        self.ui = ui

        # Set up generic lock-in frequency randomizer button
        self.ui.genericLockInRandomButton.clicked.connect(self.randomFreq)
        # Set up generic lock-in apply button
        self.ui.genericLockInApplyButton.clicked.connect(self.apply)

    def selected(self, device):
        self.device = device

        # Switch to the correct widget layer
        self.ui.settingsStack.setCurrentIndex(1)

        # Set up frequency field
        freq = device.readFreq()
        index = 0

        # Set the prefix according to the value
        if freq > 1e10:
            index = 3
            freq /= 1e9
        elif freq > 1e7:
            index = 2
            freq /= 1e6
        elif freq > 1e4:
            index = 1
            freq /= 1e3

        self.ui.genericLockInFreqPrefix.setCurrentIndex(index)
        self.ui.genericLockInFreqBox.setValue(freq)

        # Read in amplitude
        amp = self.device.readAmp()
        self.ui.genericLockInAmp.setValue(amp)

        # Read in phase
        phase = self.device.readPhase()
        self.ui.genericLockInPhase.setValue(phase)

        # Set up Tau combo box
        self.ui.genericLockInTau.clear()
        for tau in self.device.tauList:
            self.ui.genericLockInTau.addItem(formatPrefix(tau, 's'))

        currentTau = self.device.readTau()
        self.ui.genericLockInTau.setCurrentIndex(currentTau)

        # Set up Sensitivity combo box
        self.ui.genericLockInSens.clear()
        for sens in self.device.sensList:
            self.ui.genericLockInSens.addItem(formatPrefix(sens, 'V'))

        currentSens = self.device.readSens()
        self.ui.genericLockInSens.setCurrentIndex(currentSens)

    # Randomize frequency
    def randomFreq(self):
        randFreq = uniform(1, 1000)
        self.ui.genericLockInFreqBox.setValue(randFreq)

    # Apply settings
    def apply(self):

        freqVal = self.ui.genericLockInFreqBox.value()
        freqPrefix = 3 * self.ui.genericLockInFreqPrefix.currentIndex()
        freq = freqVal * 10**freqPrefix
        self.device.setFreq(freq)

        amp = self.ui.genericLockInAmp.value()
        self.device.setAmp(amp)

        phase = self.ui.genericLockInPhase.value()
        self.device.setPhase(phase)

        tau = self.ui.genericLockInTau.currentIndex()
        self.device.setTau(tau)

        sens = self.ui.genericLockInSens.currentIndex()
        self.device.setSens(sens)

