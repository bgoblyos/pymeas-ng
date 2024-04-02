from PySide6.QtWidgets import *
import pyqtgraph as pg
import sys

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
        self.plot(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [30, 32, 34, 32, 33, 31, 29, 32, 35, 45],
        )

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

app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.displayDeviceTree(devices)
app.exec()

