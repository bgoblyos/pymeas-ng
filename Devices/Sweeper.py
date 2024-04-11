import Devices.Common

class SweeperCommon(Devices.Common.CommonInstrument):
    def __init__(self, rm, address):
        super().__init__(rm, address)

    def readFreq(self):
        return float(self.query("FREQ?"))
    
class HP83751A(SweeperCommon):
    def __init__(self, rm, address):
        super().__init__(rm, address)

    model = "HP83751A"