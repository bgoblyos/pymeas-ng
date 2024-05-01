from PySide6.QtWidgets import *

from Experiments.SweepAndLockIn import SweepAndLockIn

import logging

class Experiments():

    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

        self.ui.expList.currentItemChanged.connect(self.selectionChanged)
        self.placeholder()

        self.sweepAndLockIn = SweepAndLockIn(self.ui, self.devices, self.plotter)

    def selectionChanged(self):
        currItem = self.ui.expList.currentItem().text()
        logging.debug(currItem)

        match currItem:
            case "Sweep and Lock-in":
                logging.debug("Called Sweep and Lock-in handler")
                self.sweepAndLockIn.selected()
                return

        logging.info(f"Could not find handler for {currItem}")
        self.placeholder()

    def placeholder(self):
        self.ui.expStack.setCurrentIndex(0)

