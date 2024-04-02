import pyvisa

# Common GPIB instrument class
# Handles opening the device with pyvisa
# and performs read/writes operations
class GPIBInstrument():
    def __init__(self, rm, address):
        #self.device = rm.open_resource(address)
        self.address = address
        print(f'Opened device on {address}')

    def writeStr(self, string):
        print(f'Simulated writing {string}')

    def writeParam(self, param, value):
        self.writeStr(param + " " + str(value))

    def readValue(self):
        printf(f'Simulated reading value')
        return "123"
