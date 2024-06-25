import numpy as np
import os
import datetime
import zipfile
import logging
from tempfile import gettempdir

from PySide6.QtWidgets import QFileDialog

def promptMultiExport(data, xaxis, yaxis, datatitle = 'data', xtitle = "xaxis", ytitle = "yaxis"):
    fname = QFileDialog.getSaveFileName(
            caption = "Test",
            filter = "Zip archive (*.zip);;Numpy arrays (*.npz);;HDF5 file (*.h5 *.hdf5)")

    saveCSVZip(fname, [(data, datatitle), (xaxis, xtitle), (yaxis, ytitle)])

# Export multiple numpy arrays int CSV files and zip them
# expects an array of tuples: (data, 'label')
def saveCSVZip(zippath, arrays):# Ask user for zip file location here and abort if necessary
    tempdir = createTempDir()

    with zipfile.ZipFile(zippath, 'w') as newzip:
        for arr in arrays:
            tempfile = os.path.join(tempdir, f'{arr[1]}.csv')
            np.savetxt(tempfile, arr[0], delimiter=',', header=arr[1])
            logging.debug(f'Exported {tempfile} to temporary directory')
            newzip.write(tempfile, f'{arr[1]}.csv')
            logging.debug(f'Added {tempfile} to archive')

    logging.info(f'{zippath} exported')

def ensureTemp():
    tmpdir = os.path.join(gettempdir(), 'pymeas-ng')
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    return tmpdir

def createTempDir():
    tmproot = ensureTemp()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    newdir = os.path.join(tmproot, f'{timestamp}-export-temp')
    os.makedirs(newdir)
    return newdir
