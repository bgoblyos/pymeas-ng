import logging

class ODMRWaterfall():
    def __init__(self, ui, devices, plotter):
        
        self.ui = ui
        self.devices = devices
        self.plotter = plotter
        
        logging.debug("Waterfall initialized")

    def selected(self):
        self.ui.expStack.setCurrentIndex(2)
