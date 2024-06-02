import Devices.Common

class GenericPSU(Devices.Common.CommonInstrument):
    def __init__(self, rm, address):
        super().__init__(rm, address)

    def setCurrent(self, current):
        self.writeParam("curr", current)

    def getCurrent(self):
        res = self.query("curr?")
        return float(res)

    def setVoltage(self, voltage):
        self.writeParam("volt", voltage)

    def getVoltage(self):
        res = self.query("volt?")
        return float(res)

    def enableOutput(self):
        self.writeParam("outp", 1)

    def disableOutput(self):
        self.writeParam("outp", 0)

class IT6431(GenericPSU):
    def __init__(self, rm, address):
        super().__init__(rm, address)
        self.model = "IT6431"
        self.currentRange = (0.01, 10.05)
