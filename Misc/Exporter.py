import numpy as np
import os
import datetime
import zipfile
from tempfile import gettempdir

def exportHeatmap(data, xaxis, yaxis, datatitle = 'Data', xtitle = "X axis", ytitle = "Y axis"):
    zippath = '/tmp/testzip.zip'
    # Ask user for zip file location here and abort if necessary
    tempdir = createTempDir()
    datafile = os.path.join(tempdir, 'data.csv')
    xaxisfile = os.path.join(tempdir, 'xaxis.csv')
    yaxisfile = os.path.join(tempdir, 'yaxis.csv')

    np.savetxt(datafile, data, delimiter=',', header=datatitle)
    np.savetxt(xaxisfile, xaxis, delimiter=',', header=xtitle)
    np.savetxt(yaxisfile, yaxis, delimiter=',', header=ytitle)

    with zipfile.ZipFile(zippath, 'w') as newzip:
        newzip.write(datafile, 'data.csv')
        newzip.write(xaxisfile, 'xaxis.csv')
        newzip.write(yaxisfile, 'yaxis.csv')

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

print(createTempDir())

xs = np.linspace(0, 1, 10)
ys = np.linspace(1, 2, 20)
data = np.random.rand(10,20)

exportHeatmap(data, xs, ys)
