from PySide6.QtWidgets import QMainWindow, QApplication, QStyleFactory

import sys
import logging
import argparse
from pyvisa import ResourceManager

# Import device classes and handlers
import Devices.DeviceManager

# Import pyvisa simulator for debugging
# Helpful when working without a physical device
import Devices.Simulator

# Import UI file (generated from Qt Designer .ui file)
# Run `pyside6-uic UI/mainwindow.ui -o UI/Mainwindow.py`
# after modifying to regenerate the python file
from UI.Mainwindow import Ui_MainWindow

# Import device tree handler class to inherit
from Devices.DeviceTree import DeviceTree

# Import settings handler class to inherit
from Settings.Common import Settings

# Import GUI logger
from UI.Logger import QTextEditLogger

from Misc.CloseInheritance import CloseInheritance

# PyVisa resource manager
# rm = ResourceManager()
rm = Devices.Simulator.RMSimulator()

parser = argparse.ArgumentParser(
                    prog='PyMeas-ng',
                    description='Scientific measurement suite')

# Main GUI class, meant to glue everything together
# Always inherit CloseInheritance last, as it is meant to
# close the inheritance graph. It has a dummy __setup__()
# method and does not call super().__setup__().
class MainWindow( QMainWindow
                , Ui_MainWindow
                , Settings
                , DeviceTree
                , CloseInheritance):

    def __init__(self, rm):
        super(MainWindow, self).__init__()

        self.rm = rm

        self.setupUi(self)
        
        # Set up logging to the logBox
        logTextBox = QTextEditLogger(self.logBox)
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)

        logging.debug("Main window initialized")
        
        
        # Get connected, disconnected and unknown devices
        # using the config file
        self.devices, self.disconnected, self.unknown = Devices.DeviceManager.readConfig(self.rm)
        # Devices: nested dict ([type][name]) with objects inside
        # Disconnected: nested dict ([type][name]) with entries in the form of (model, address)
        # Unknown: list of connected, but unconfigured VISA addresses


        # Run the setup for each inherited class
        super(MainWindow, self).__setup__()
        

        # Placeholder plot
        #self.plot(
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        #    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        #)


    # Plot the given dataset
    def plot(self, xs, ys):
        self.graphWidget.plot(xs, ys)

app = QApplication(sys.argv)


# Set default style to Fusion (if it exists)
if "Fusion" in QStyleFactory.keys():
    app.setStyle("Fusion")


window = MainWindow(rm)
window.show()

#window.displayDeviceTree(devices)
app.exec()

