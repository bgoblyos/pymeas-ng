import logging
import numpy as np

class ODMRWaterfall():
    def __init__(self, ui, devices, plotter):

        self.ui = ui
        self.devices = devices
        self.plotter = plotter

        # Connect start button
        self.ui.ODMRWaterfallStart.clicked.connect(self.prepare)

        logging.debug("Waterfall initialized")

    def selected(self):
        # Switch to correct page
        self.ui.expStack.setCurrentIndex(2)

    def prepare(self):
        
        # Set up data storage (TODO: implement)
        self.data = np.zeros((self.fsteps, self.isteps), float)
