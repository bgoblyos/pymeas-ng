from PySide6.QtWidgets import *

from Experiments.SweepAndLockIn import SweepAndLockIn

import logging

class Experiments(SweepAndLockIn):
    
    def __setup__(self):

        self.expList.currentItemChanged.connect(self.expHandler)
        self.expStack.setCurrentIndex(0)
        SweepAndLockIn.__setup__(self)

    def expHandler(self):
        currItem = self.expList.currentItem().text()
        logging.debug(currItem)

        match currItem:
            case "Sweep and Lock-in":
                self.sweepAndLockInHandler()
                logging.debug("Called Sweep and Lock-in handler")
                return
        
        self.expStack.setCurrentIndex(0)
        logging.info(f"Could not find handler for {currItem}")


