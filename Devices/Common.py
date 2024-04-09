import pyvisa

# Common instrument class
# Handles opening the device with pyvisa
# and performs read/writes operations
class CommonInstrument():
    def __init__(self, rm, address):
        #self.device = rm.open_resource(address)
        self.address = address
        print(f'Opened device on {address}')

    def writeStr(self, string):
        print(f'Simulated writing {string}')

    def writeParam(self, param, value):
        self.writeStr(param + " " + str(value))

    def readValue(self):
        response = input("Enter device response: ")
        return response
