import numpy as np
import os
import datetime
import zipfile
import logging
from tempfile import gettempdir

from PySide6.QtWidgets import QFileDialog

def promptMultiExport(data, xaxis, yaxis, datatitle = 'data', xtitle = "xaxis", ytitle = "yaxis"):
    choice = QFileDialog.getSaveFileName(
            caption = "Test",
            filter = "Zip archive (*.zip);;Numpy arrays (*.npz)")

    fname = choice[0]

    if fname == '':
        logging.warning('No filename chosen for export, aborting!')
        return

    ext = fname.split('.')[-1].lower()

    if choice[1] == 'Zip archive (*.zip)':
        if ext != 'zip':
            fname += '.zip'

        saveCSVZip(fname, [(data, datatitle), (xaxis, xtitle), (yaxis, ytitle)])
    else:
        if ext != 'npz':
            fname += '.npz'

        np.savez(fname, data=data, xaxis=xaxis, yaxis=yaxis)


# Export multiple numpy arrays int CSV files and zip them
# expects an array of tuples: (data, 'label')
def saveCSVZip(zippath, arrays):# Ask user for zip file location here and abort if necessary
    tempdir = createTempDir()

    with zipfile.ZipFile(zippath, 'w') as newzip:
        for arr in arrays:
            tempfile = os.path.join(tempdir, f'{arr[1]}.csv')
            np.savetxt(tempfile, arr[0], delimiter=',', header=arr[1])
            logging.debug(f'Exported {tempfile} to temporary directory')
            logging.debug(f'Type of newzip: {type(newzip)}')
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
