import pyvisa

class GPIBIntrument():
    def __init__(self, rm, address):
        self.device = rm.open_resource(address)
        print(f'Opened device on {address}')
    
    def writeStr(self, string)
        print(f'Simulated writing {string}')

    def writeParam(self, param, value):
        self.writeStr(param + " " + str(value))

    def readValue(self):
        printf(f'Simulated reading value')
        return "123"
