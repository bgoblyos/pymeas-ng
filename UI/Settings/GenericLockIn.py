from PySide6.QtWidgets import *

from random import uniform

import Devices.Common
import Devices.LockIn
import Devices.DeviceManager

class GenericLockInSettings():
    def genericLockInHandler(self):
        device = self.currentSettingsDevice

        # Switch to the correct widget layer
        self.settingsStack.setCurrentIndex(1)

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

        self.genericLockInFreqPrefix.setCurrentIndex(index)
        self.genericLockInFreqBox.setValue(freq)

        # Read in amplitude
        amp = device.readAmp()
        self.genericLockInAmp.setValue(amp)

        # Read in phase
        phase = device.readPhase()
        self.genericLockInPhase.setValue(phase)

        # Set up Tau combo box
        for tau in device.tauDict:
            self.genericLockInTau.addItem(tau)

        currentTau = device.readTau()
        self.genericLockInTau.setCurrentIndex(currentTau)

        # Set up Sensitivity combo box
        for sens in device.sensDict:
            self.genericLockInSens.addItem(sens)

        currentSens = device.readSens()
        self.genericLockInSens.setCurrentIndex(currentSens)

    # Randomize frequency
    def genericLockInRandomFreq(self):
        randFreq = uniform(1, 1000)
        self.genericLockInFreqBox.setValue(randFreq)

    # Apply settings
    def genericLockInApply(self):
        # We saved the device object in the menu handler
        device = self.currentSettingsDevice

        freqVal = self.genericLockInFreqBox.value()
        freqPrefix = 3 * self.genericLockInFreqPrefix.currentIndex()
        freq = freqVal * 10**freqPrefix
        device.setFreq(freq)

        amp = self.genericLockInAmp.value()
        device.setAmp(amp)

        phase = self.genericLockInPhase.value()
        device.setPhase(phase)

        tau = self.genericLockInTau.currentIndex()
        device.setTau(tau)

        sens = self.genericLockInSens.currentIndex()
        device.setSens(sens)

