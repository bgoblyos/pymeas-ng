from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import pyqtgraph as pg
import sys
from random import uniform

import Devices.Common
import Devices.LockIn
from Devices.DeviceManager import readConfig

rm = "Placeholder"

devices = readConfig(rm)

uiclass, baseclass = pg.Qt.loadUiType("UI/mainwindow.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.constructSettingsTree()

        # Placeholder plot
        self.plot(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [30, 32, 34, 32, 33, 31, 29, 32, 35, 45],
        )

        # Call the settings handler when the settings device tree selection changes
        self.deviceSelectionTree.currentItemChanged.connect(self.settingsHandler)

        # Set the default device config page to the placeholder
        self.settingsStack.setCurrentIndex(0)

        # Set up generic lock-in frequency randomizer button
        self.genericLockInRandomButton.clicked.connect(self.genericLockInRandomFreq)
        
        # Set up generic lock-in apply button
        self.genericLockInApplyButton.clicked.connect(self.genericLockInApply)

    # Plot the given dataset
    def plot(self, xs, ys):
        self.graphWidget.plot(xs, ys)

    def displayDeviceTree(self, devices):
        # Every device category becomes a top-level foldable item
        for deviceType in devices:
            modelItem = QTreeWidgetItem(self.deviceTree)
            modelItem.setText(0, Devices.DeviceManager.types[deviceType])
            modelItem.setExpanded(True)
            # Each item in a given categrory is added to the list
            for name in devices[deviceType]:
                entry = QTreeWidgetItem(modelItem)
                entry.setText(1, name)
                entry.setText(2, devices[deviceType][name].model)
                entry.setText(3, devices[deviceType][name].address)
                #modelItem.addChild(entry)

        self.deviceTree.resizeColumnToContents(0)

    # Construct the settings device tree
    def constructSettingsTree(self):
        for deviceType in devices:
            typeItem = QTreeWidgetItem(self.deviceSelectionTree)
            typeItem.setText(0, Devices.DeviceManager.types[deviceType])
            typeItem.setExpanded(True)
            typeItem.setFlags(typeItem.flags() & ~Qt.ItemIsSelectable)

            for name in devices[deviceType]:
                entry = QTreeWidgetItem(typeItem)
                entry.setText(0, name)

    def settingsHandler(self):
        currItem = self.deviceSelectionTree.currentItem()
    
        # DO nothing if a top-level item is selected
        # This shouldn't be necessary, but for some reason
        # disabling the top level items does not work.
        if currItem.parent() == None:
            return

        deviceName = currItem.text(0)
        # Convert the top level user-facing name back to the dictionary key
        # This is a really hacky soluion, but the it's the best I could come up with
        # Refactoring it later might be a good idea
        deviceType = Devices.DeviceManager.typesInverted[currItem.parent().text(0)]
        print(f"Type: {deviceType}\nName: {deviceName}")

        device = devices[deviceType][deviceName]

        # We need to save the device so the apply handler can access it
        self.currentSettingsDevice = device

        match device.model:
            case "placeholder":
                print("This is where device-specific handlers go")
                return

        match deviceType:
            case "lockin":
                self.genericLockInHandler(device)
                return

        print("Selected device does not have a settings handler")


    def genericLockInHandler(self, device):
        # Switch to the correct widget layer
        self.settingsStack.setCurrentIndex(1)

        # Set up frequency field
        freq = device.readFreq()
        index = 0;
        
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
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.displayDeviceTree(devices)
app.exec()

