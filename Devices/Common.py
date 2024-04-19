import pyvisa
import struct

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
    
    # Send a query and read out the raw reponse into a byte array
    def queryBinary(self, param):
        # Increse timeout, otherwise the transfer takes too long
        oldTimeout = self.device.timeout
        self.device.timeout = 60000 # 1 minute

        self.device.write(param)
        response = self.device.read_raw() 

        # Reset the timeout
        self.device.timeout = oldTimeout
        
        return response
    
    def queryBinaryFloat(self, param):
        response = self.queryBinary(param)
        entries = len(response) // 4
        data = struct.unpack(f"{entries}f", response)
        return data
