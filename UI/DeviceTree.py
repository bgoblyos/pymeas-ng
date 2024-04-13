from PySide6.QtWidgets import *
#from PySide6.QtCore import Qt

import Devices.DeviceManager

class DeviceTree():
    def displayDeviceTree(self):
        # Connected devices
        connectedItem = QTreeWidgetItem(self.deviceTree)
        connectedItem.setText(0, "Connected")
        connectedItem.setExpanded(True)
        # Every device category becomes a top-level foldable item
        for deviceType in self.devices:
            modelItem = QTreeWidgetItem(connectedItem)
            modelItem.setText(1, Devices.DeviceManager.types[deviceType])
            modelItem.setExpanded(True)
            # Each item in a given categrory is added to the list
            for name in self.devices[deviceType]:
                entry = QTreeWidgetItem(modelItem)
                entry.setText(2, name)
                entry.setText(3, self.devices[deviceType][name].model)
                entry.setText(4, self.devices[deviceType][name].address)
                #modelItem.addChild(entry)

        # Disconnected, but configured devices
        disconnectedItem = QTreeWidgetItem(self.deviceTree)
        disconnectedItem.setText(0, "Disconnected")
        disconnectedItem.setExpanded(True)
        # Every device category becomes a top-level foldable item
        for deviceType in self.disconnected:
            modelItem = QTreeWidgetItem(disconnectedItem)
            modelItem.setText(1, Devices.DeviceManager.types[deviceType])
            modelItem.setExpanded(True)
            # Each item in a given categrory is added to the list
            for name in self.disconnected[deviceType]:
                entry = QTreeWidgetItem(modelItem)
                entry.setText(2, name)
                entry.setText(3, self.disconnected[deviceType][name][0]) # Model
                entry.setText(4, self.disconnected[deviceType][name][1]) # Address
                #modelItem.addChild(entry)

        unknownItem = QTreeWidgetItem(self.deviceTree)
        unknownItem.setText(0, "Unknown")
        unknownItem.setExpanded(True)
        for address in self.unknown:
            entry = QTreeWidgetItem(unknownItem)
            entry.setText(1, "N/A")
            entry.setText(2, "N/A")
            entry.setText(3, "N/A")
            entry.setText(4, address)

        self.deviceTree.resizeColumnToContents(0)
        self.deviceTree.resizeColumnToContents(1)

