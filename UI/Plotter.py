import logging
import os
from tempfile import gettempdir
import datetime

from PySide6.QtWidgets import QFileDialog

# For testing purposes, can be removed later
import numpy as np

from pyqtgraph.exporters import CSVExporter
from pyqtgraph import ImageItem
from pyqtgraph.Qt import QtGui

class Plotter():
    def __init__(self, ui):

        self.plt = ui.graphWidget
        self.colorBar = None
        self.heatmapData = None
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

    def clear(self):
        self.plt.clear()
        self.heatmapData = None

        if self.colorBar != None:
            self.colorBar.clear()
            self.colorBar.hideAxis('right')
            self.colorBar = None

    def plot(self, xs, ys, pen = None, name = None):
        return self.plt.plot(xs, ys, pen=pen, name=name)

    def emptyPlot(self, pen="w"):
        return self.plt.plot(pen=pen)

    def heatmap(self, data, xrange = (0, 1), yrange = (0, 1), cmap = "viridis"):
        self.clear()
        self.plt.plot()

        self.heatmapData = data
        img = ImageItem(data)

        xscale = (xrange[1] - xrange[0])/data.shape[0]
        yscale = (yrange[1] - yrange[0])/data.shape[1]
        tr = QtGui.QTransform()
        tr.scale(xscale, yscale)
        tr.translate(xrange[0]/xscale, yrange[0]/yscale)

        img.setTransform(tr)

        self.plt.addItem(img)
        self.colorBar = self.plt.addColorBar(img, colorMap = cmap)

    def saveAs(self):
        fileName = QFileDialog.getSaveFileName(None, "Save plot data as",
                                   #os.getcwd(),
                                   "",
                                   "CSV files (*.csv)")[0]

        # Add csv extension if it's not specified
        if fileName.split('.')[-1].lower() != "csv":
            fileName += ".csv"

        self.exportPlot(fileName)

    def quickSave(self):
        timestamp = datetime.datetime.now().astimezone().strftime('%Y-%m-%d%Z%H-%M-%S.%f')
        fileName = f"{timestamp}.csv"
        filePath = os.path.join(self.quickSaveDir, fileName)
        self.exportPlot(filePath)

    def exportPlot(self, filePath):
        if self.heatmapData is None:
            exp = CSVExporter(self.plt.plotItem)
            exp.export(filePath)
        else:
            np.savetxt(filePath, self.heatmapData, delimiter=",")

        logging.info(f"File successfully saved as {filePath}")

    def setLabels(self, title = None, xlabel = None, ylabel = None):
        self.plt.setTitle(title)
        self.plt.setLabels(bottom=xlabel, left=ylabel)