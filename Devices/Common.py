import pyvisa

# Common instrument class
# Handles opening the device with pyvisa
# and performs read/writes operations
class CommonInstrument():
    def __init__(self, rm, address):
        self.device = rm.open_resource(address)
        self.address = address
        print(f'Opened device on {address}')

    def writeStr(self, string):
        # print(f'Simulated writing {string}')
        self.device.write(string)

    def writeParam(self, param, value):
        self.writeStr(param + " " + str(value))

    def readValue(self):
        #response = input("Enter device response: ")
        response = self.device.read()
        return response
    
    def query(self, param):
        response = self.device.query(param)
        return response
