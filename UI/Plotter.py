import logging
import os
from tempfile import gettempdir
import datetime

from PySide6.QtWidgets import QFileDialog

# For testing purposes, can be removed later
import numpy as np

from pyqtgraph.exporters import CSVExporter

class Plotter():
    def __init__(self, ui):

        self.plt = ui.graphWidget
        self.clear()

        ui.plotClearButton.clicked.connect(self.clear)
        ui.saveAsButton.clicked.connect(self.saveAs)
        ui.quickSaveButton.clicked.connect(self.quickSave)

        tempDir = gettempdir()
        self.quickSaveDir = os.path.join(tempDir, "pymeas-ng")

        # Create directory if it does not exist
        if not os.path.exists(self.quickSaveDir):
            os.makedirs(self.quickSaveDir)
            logging.debug(f"Created {self.quickSaveDir}")

        # Placeholder
        xs = np.linspace(0, 4*np.pi, 1000)
        y1s = np.cos(xs)
        y2s = np.cos(2*xs)
        self.plot(xs, y1s, pen = "r", name = "Dataset 1")
        self.plot(xs, y2s, pen = "g", name = "Dataset 2")


    def clear(self):
        self.plt.clear()

    def plot(self, xs, ys, pen = None, name = None):
        return self.plt.plot(xs, ys, pen=pen, name=name)

    def emptyPlot(self, pen="w"):
        return self.plt.plot(pen=pen)

    def saveAs(self):
        fileName = QFileDialog.getSaveFileName(None, "Save plot data as",
                                   #os.getcwd(),
                                   "",
                                   "CSV files (*.csv)")[0]

        # Add csv extension if it's not specified
        if fileName.split('.')[-1].lower() != "csv":
            fileName += ".csv"

        exp = CSVExporter(self.plt.plotItem)
        exp.export(fileName)
        logging.info(f"File successfully saved as {fileName}")

    def quickSave(self):
        timestamp = datetime.datetime.now().astimezone().isoformat()
        fileName = f"{timestamp}.csv"
        filePath = os.path.join(self.quickSaveDir, fileName)

        exp = CSVExporter(self.plt.plotItem)
        exp.export(filePath)
        logging.info(f"File successfully saved as {filePath}")

