from PySide6.QtWidgets import QMainWindow, QApplication, QStyleFactory
#from PySide6.QtCore import Qt

import sys
import os
from random import uniform

# Import device classes and handlers
import Devices.Common
import Devices.LockIn
import Devices.DeviceManager

# Import pyvisa simulator for debugging
# Helpful when working without a physical device
import Devices.Simulator

# Import UI file (generated from Qt Designer .ui file)
from UI.Mainwindow import Ui_MainWindow

# Import device tree handler class to inherit
from UI.DeviceTree import DeviceTree

# Import settings handler class to inherit
from UI.Settings.Common import Settings

import pyvisa

# PyVisa resource manager
# rm = pyvisa.ResourceManager()
rm = Devices.Simulator.RMSimulator()

class MainWindow(QMainWindow, Ui_MainWindow, DeviceTree, Settings):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        # Get connected, disconnected and unknown devices
        # using the config file
        self.devices, self.disconnected, self.unknown = Devices.DeviceManager.readConfig(rm)
        # Devices: nested dict ([type][name]) with objects inside
        # Disconnected: nested dict ([type][name]) with entries in the form of (model, address)
        # Unknown: list of connected, but unconfigured VISA addresses


        self.displayDeviceTree()

        self.constructSettingsTree()

        # Placeholder plot
        self.plot(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
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

app = QApplication(sys.argv)
# Set default style to Fusion (if it exists)
if "Fusion" in QStyleFactory.keys():
    app.setStyle("Fusion")


window = MainWindow()
window.show()
#window.displayDeviceTree(devices)
app.exec()

