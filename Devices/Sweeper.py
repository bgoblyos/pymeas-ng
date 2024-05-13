import Devices.Common

class SweeperCommon(Devices.Common.CommonInstrument):
    def __init__(self, rm, address):
        super().__init__(rm, address)

    def readFreq(self):
        return float(self.query("FREQ?"))
    
class HP83751A(SweeperCommon):
    def __init__(self, rm, address):
        super().__init__(rm, address)
        self.freqRange = (2,20)
        self.powerRange = (-80,20)
        self.timeRange = (0,100)

    def setupSweep(self, min, max, time):
        self.writeStr("FREQ:MODE SWE")
        self.writeStr(f"FREQ:STAR {min} GHZ")
        self.writeStr(f"FREQ:STOP {max} GHZ")
        self.writeStr(f"SWE:TIME {time} s")

    def readSweepParams(self):
        start = float(self.query("FREQ:STAR?"))/1e9
        end = float(self.query("FREQ:STOP?"))/1e9
        time = float(self.query("SWE:TIME?"))
        return (start, end, time)

    def readSweepTime(self):
        return float(self.query("SWE:TIME?"))

    def resetMarkers(self):
        self.writeStr("MARK:AOFF")
    
    def setMarker(self, markNum, freq):
        self.writeStr(f"MARK{markNum}:STATE ON; FREQ {freq} GHz")

    def setPowerLevel(self, level):
        self.writeStr(f"POWER:LEV {level} DBM")

    def readPowerLevel(self):
        return float(self.query("POWER:LEV?"))

    def powerOn(self):
        self.writeStr("POW:STATE ON")

    def powerOff(self):
        self.writeStr("POW:STATE OFF")

    def setContSweep(self, cont):
        if cont:
            self.writeStr("INIT:CONT ON")
        else:
            self.writeStr("INIT:CONT OFF")

    def startSweep(self):
        #self.writeStr("INIT:IMM")
        self.writeStr("*TRG")

    model = "HP83751A"