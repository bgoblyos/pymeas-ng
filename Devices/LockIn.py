import Devices.Common
from Misc.Prefix import formatPrefix

import logging

# Common class for Stanford Research Lock-In Amplifiers
# Implements several common control commands and r/w operations
class SRCommon(Devices.Common.CommonInstrument):
    def __init__(self, rm, address):
        super().__init__(rm, address)

        self.display1list = [
            "X",
            "R",
            "X Noise",
            "Aux in 1",
            "Aux in 2"
        ]

        self.display2list = [
            "Y",
            "Theta",
            "Y Noise",
            "Aux in 3",
            "Aux in 4"
        ]

    def clear(self):
        self.writeStr('*CLS;REST')

    def readXY(self):
        response = self.query("SNAP? 1,2")
        responseList = response.split(',')
        x = float(responseList[0])
        y = float(responseList[1])
        return (x, y)

    def setFreq(self, f):
        self.writeParam('FREQ', f)

    def setAmp(self, amp):
        if float(amp)>0.004 and float(amp) < 5:
            self.writeParam('SLVL', amp)
        else:
            print("Invalid amplitude, must be between 0.004 and 5.0")

    def setPhase(self, phase):
        if float(phase) > -360 and float(phase) < 729.99:
            self.writeParam('PHAS', phase)
        else:
            print("Invalid phase, must be between -360 and 730")

    def setTau(self, tc):
        self.writeParam('OFLT', tc)

    def setSens(self, sens):
        self.writeParam('SENS', sens)

    def readFreq(self):
        return float(self.query('FREQ?'))

    def readAmp(self):
        return float(self.query('SLVL?'))

    def readPhase(self):
        return float(self.query('PHAS?'))

    def readTau(self):
        return int(self.query('OFLT?'))

    def readSens(self):
        return int(self.query('SENS?'))

    def triggerStartScan(self, state):
        self.writeParam('TSTR', state)

    def sampleRate(self, state):
        self.writeParam('SRAT ', state)

    def readSampleRate(self):
        return int(self.query('SRAT?'))

    def aux(self, channel, value):
        if float(value) > -10.5 and float(value) < 10.5:
            self.writeStr('AUXV '+ channel + ',' + value)

    def display(self, channel, value, ratio):
        self.writeStr('DDEF ' + channel + ',' + value + ',' + ratio)

    def readDisplay(self, channel):
        self.query(f"DDEF ? {channel}")
        # TODO implement separating the values into a tuple

    def readBinNum(self):
        res = self.query('SPTS?')
        return int(res)

    def harmDet(self, value):
        self.writeParam('HARM', value)

    def rest(self):
        self.writeStr('REST')

    def trigger(self):
        self.writeStr('TRIG')

    def pause(self):
        self.writeStr('PAUS')

    # TODO: test this with actual hardware
    def readBuffer(self, buffer, firstPoint = 0, numPoints = 0):
        bufferSize = self.readBinNum()

        if bufferSize == 0:
            logging.warning("The lock-in buffer is empty, nothing could be retrieved.")
            return []

        if numPoints <= 0:
            numPoints = bufferSize - firstPoint

        if (firstPoint >= bufferSize) or (firstPoint < 0):
            logging.warning(f"Starting index is out of bounds (requested index {firstPoint} from {bufferSize} elements)")
            return []

        if (firstPoint + numPoints) > bufferSize:
            logging.info("Requested too many points, clamping it.")
            numPoints = bufferSize - firstPoint

        queryStr = f"TRCB ? {buffer}, {firstPoint}, {numPoints}"
        return self.queryBinaryFloat(queryStr)


    def setDisplay(self, display, value, ratio = 0):
        self.writeParam("DDEF", f"{display}, {value}, {ratio}")

    def maxSampleRate(self):
        tau = self.tauList[self.readTau()]
        maxfreq = 1/tau
        # Iterate over the list in reverse
        for i in reversed(range(0, len(self.sampleFreqList))):
            if self.sampleFreqList[i] < maxfreq:
                return i

        print("No appropriate sample rate found, setting it to the lowest available.")
        return 0

    def armTimedMeasurement(self, time, chosenFreqIndex):
        maxFreqIndex = self.maxSampleRate()
        maxFreq = self.sampleFreqList[maxFreqIndex]
        chosenFreq = self.sampleFreqList[chosenFreqIndex]

        if chosenFreq > maxFreq:
            logging.warning(f"{formatPrefix(chosenFreq, 'Hz')} is too high, clamping it to {formatPrefix(maxFreq, 'Hz')}")
            self.writeParam("SRAT", maxFreqIndex)
        else:
            self.writeParam("SRAT", chosenFreqIndex)

        # Read it back from the device just to be sure
        actualFreq = self.sampleFreqList[self.readSampleRate()]

        numpoints = round(time * actualFreq)
        padding = 0
        if numpoints > self.bufferSize:
            logging.warning("The buffer cannot store every datapoint.")
            logging.warning("The result will be padded with zeroes.")
            padding = numpoints - self.bufferSize
            numpoints = self.bufferSize

        # Set to oneshot mode
        self.writeParam("SEND", 1)

        # Clear buffer
        self.writeStr("REST")

        logging.info("Lock-in is armed, waiting for trigger")
        return (numpoints, padding)



    # TODO: Review this
    def freqSweepSetup(self):
        tau = self.readTau()

        self.display('1', '1', '0')
        self.harmDet('1')
        self.triggerStartScan('1')
        if tau==9:
            self.sampleRate('5')
            sampling = 1.0/2.0
        elif tau==8:
            self.sampleRate('7')
            sampling=1.0/8.0
        elif tau==7:
            self.sampleRate('9')
            sampling=1.0/32.0
        elif tau==6:
            self.sampleRate('11')
            sampling=1.0/128.0
        elif tau==5:
            self.sampleRate('13')
            sampling=1.0/512.0
        else:
            print("Invalid time constant")
            sampling = -1
        return sampling

# SR830 class, contains dictionaries for
# sensitivity and time constant settings 
class SR830(SRCommon):
    def __init__(self, rm, address):
        super().__init__(rm, address)
        self.bufferSize = 16383

        self.sensList = [
            2e-9,
            5e-9,
            10e-9,
            20e-9,
            50e-9,
            100e-9,
            200e-9,
            500e-9,
            1e-6,
            2e-6,
            5e-6,
            10e-6,
            20e-6,
            50e-6,
            100e-6,
            200e-6,
            500e-6,
            1e-3,
            2e-3,
            5e-3,
            10e-3,
            20e-3,
            50e-3,
            100e-3,
            200e-3,
            500e-3,
            1
        ]

        # Machine-readable time constant list
        # Try to migrate to this format for displaying it as well
        self.tauList = [
            10e-6,
            30e-6,
            100e-6,
            300e-6,
            1e-3,
            3e-3,
            10e-3,
            30e-3,
            100e-3,
            300e-3,
            1,
            3,
            10,
            30,
            100,
            300,
            1e3,
            3e3,
            10e3,
            30e3,
        ]

        self.sampleFreqList = [
            62.5e-3,
            125e-3,
            250e-3,
            500e-3,
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512
        ]

        self.model = "SR830"

        
