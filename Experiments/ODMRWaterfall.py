import logging
import numpy as np

from PySide6.QtCore import QTimer

class ODMRWaterfall():
    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

        # Connect start button
        self.ui.ODMRWaterfallStart.clicked.connect(self.prepare)

        logging.debug("Waterfall initialized")

        # Set up timer for progress bar
        # (and for waiting until the sweep is done)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateSweepProgress)

        # Reset progress bars
        #self.ui.sweepAndLockProgress.setValue(0)
        #self.ui.sweepAndLockTotalProgress.setValue(0)

    def selected(self):
        # Switch to correct page
        self.ui.expStack.setCurrentIndex(2)

    def prepare(self):
        
        # Set up data storage (TODO: implement)
        self.data = np.zeros((self.fsteps, self.isteps), float)

    def updateSweepProgress(self):
        logging.debug("ODMR Waterfall progress updated")
