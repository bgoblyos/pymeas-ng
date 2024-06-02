# This file contains a simulated implementation
# of the pyvisa resource manager to facilitate
# development without access to the instruments

import logging
import struct
import numpy as np

# Resource manager implementing list_resources() (using a predefined list)
# and open_resource(address)
# Interactivity controls whether or not to ask for input on read operations
# that are performed on objects returned by open_resource (see DeviceSimulator)
class RMSimulator():
    def __init__(self, interactive = False):
        self.interactive = interactive

    def list_resources(self):
        resources = [
            "GPIB0::7::INSTR",
            "GPIB0::8::INSTR",
            "GPIB0::9::INSTR",
            "GPIB0::10::INSTR",
            "GPIB0::11::INSTR",
            "USB0::0x2EC7::0x6431::800626011777710004::INSTR",
        ]
        return resources

    def open_resource(self, GPIB):
        return DeviceSimulator(GPIB, self.interactive)


# Device simulator, implementing write(string), read() and query()
# If interactivity is set, the user will be asked to provide the simulated
# output of the device through the terminal. If set to non-interactive,
# all read operations will return "1"
# In the future, more sophisticated simulations might be implemented,
# inluding device-specific canned responses
class DeviceSimulator():
    def __init__(self, GPIB, interactive):
        self.gpib = GPIB
        self.interactive = interactive

        xs = np.linspace(0, 2*np.pi, 16383)
        self.sample1 = list(np.sin(xs))
        self.sample2 = list(np.cos(xs))

    def write(self, string):
        logging.info(f"{string} written to {self.gpib}.")

        substrings = string.split()

        if substrings[0] == "TRCB":

            if int(substrings[2].strip(',')) == 1:
                sample = self.sample1
            else:
                sample = self.sample2

            sample += np.random.normal(scale=0.5, size=len(sample))

            start = int(substrings[3].strip(','))
            num = int(substrings[4].strip(','))
            end = start+num

            sample = sample[start:end]
            logging.info(sample)
            self.binary = struct.pack(f"{len(sample)}f", *sample)
            logging.info(self.binary)

    def read(self):
        if self.interactive:
            res = input(f"Enter response from {self.gpib}: ")
        else:
            res = "1"
        return res

    def read_raw(self):
        return self.binary

    def query(self, string):
        if self.interactive:
            res = input(f"Enter response from {self.gpib} to {string}: ")
        else:
            logging.info(f"Query {string} sent to {self.gpib}.")
            res = "1"
        return res

    def timeout(self, n):
        logging.info(f"Timeout changed to {n}s")
