from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import Devices.DeviceManager
from Settings.GenericLockIn import GenericLockIn

import logging

class Settings():
    # Method for setting up the settings page
    # Called by main using super
    def __init__(self, ui, devices):

        self.ui = ui
        self.devices = devices
        self.genericLockIn = GenericLockIn(self.ui)

        # Call the settings handler when the settings device tree selection changes
        self.ui.deviceSelectionTree.currentItemChanged.connect(self.selectionChanged)

        # Set the default device config page to the placeholder
        self.placeholderPage()

        self.constructSettingsTree()

        logging.debug("Completed Settings setup")

    def placeholderPage(self):
        self.ui.settingsStack.setCurrentIndex(0)

    # Construct the settings device tree
    def constructSettingsTree(self):
        for deviceType in self.devices:
            typeItem = QTreeWidgetItem(self.ui.deviceSelectionTree)
            typeItem.setText(0, Devices.DeviceManager.types[deviceType])
            typeItem.setExpanded(True)
            typeItem.setFlags(typeItem.flags() & ~Qt.ItemIsSelectable)

            for name in self.devices[deviceType]:
                entry = QTreeWidgetItem(typeItem)
                entry.setText(0, name)

    def selectionChanged(self):
        currItem = self.ui.deviceSelectionTree.currentItem()

        # Do nothing if a top-level item is selected
        # This shouldn't be necessary, but for some reason
        # disabling the top level items does not work.
        if currItem.parent() == None:
            return

        deviceName = currItem.text(0)
        # Convert the top level user-facing name back to the dictionary key
        # This is a really hacky solution, but the it's the best I could come up with
        # Refactoring it later might be a good idea
        deviceType = Devices.DeviceManager.typesInverted[currItem.parent().text(0)]
        logging.debug(f"Type: {deviceType}\nName: {deviceName}")

        device = self.devices[deviceType][deviceName]

        match device.model:
            case "placeholder":
                print("This is where device-specific handlers go")
                return

        match deviceType:
            case "lockin":
                self.genericLockIn.selected(device)
                return

        # Set the device config page to the placeholder if no handler is found
        self.placeholderPage()
        print("Selected device does not have a settings handler")


