import yaml
from os.path import isfile
import Devices.LockIn
import Devices.Sweeper
import Devices.PowerSupply
import copy
import logging

def invertDict(inDict):
    outDict = {}
    for key in inDict:
        value = inDict[key]
        outDict[value] = key

    return outDict


# Dictionary for calling the correct class for each model
models = {
    "lockin": {
        "sr830": Devices.LockIn.SR830
    },
    "sweeper": {
        "hp83751a": Devices.Sweeper.HP83751A
    },
    "psu": {
        "it6400": Devices.PowerSupply.IT6400
    }
}

types = {
    "lockin": "Lock-in amplifier",
    "sweeper": "Sweeper",
    "psu": "Power supply"
}

# Converts pretty user-facing name back into the
# internally used one.
typesInverted = invertDict(types)

template = {}
for deviceType in types:
    template[deviceType] = {}

def readConfig(rm):

    # Enumerate connected devices
    connectedDevices = rm.list_resources()

    # Nested dictionaries to be populated
    devices = copy.deepcopy(template)
    disconnected = copy.deepcopy(template)

    # List to better track connected devices
    connected = []

    # Unkown device list
    unknown = []

    # Check if the config file has .yaml or .yml extension
    # In the future, the config should be moved into
    # a standardized location (XDG-config, AppData, etc.)
    if isfile("config.yaml"):
        confFile = "config.yaml"
    elif isfile("config.yml"):
        confFile = "config.yml"
    else:
        print("No config file found, no devices loaded.")
        return devices

    # Read yaml config into a dictionary
    with open(confFile) as file:
        conf = yaml.safe_load(file)

    # Check if config has a devices entry
    if "devices" not in conf:
        print("Config file contains no 'devices' top-level entry, no devices can be loaded")
        return devices

    # Iterate through entries in the config
    for device in conf["devices"]:
        # Check if entry has a name field
        if "name" in device:
            name = device["name"]
        else:
            print("Invalid entry (no name specified)")
            continue


        # Check if device type is specified
        if "type" in device:
            # Check if the type is known
            deviceType = device["type"].lower()
            if deviceType not in devices:
                print(f"{name} has unknown type {deviceType}.")
                print(f"The following types are available: {list(devices.keys())}.")
                continue
        else:
            print(f"No type entry found for {name}, skipping to next device.")
            continue

        # Check if model is specified
        if "model" in device:
            # Check if the model is known
            model = device["model"].lower()
            if model not in models[deviceType]:
                print(f"{name} has unknown model {model}.")
                print(f"The following models are supported: {list(models[deviceType].keys())}.")
                continue
        else:
            print(f"No model entry found for {name}, skipping to next device.")
            continue

        # Process adresses
        address = None
        
        # Process GPIB field
        if "gpib" in device:
            if "string" in device["gpib"]:
                address = device["gpib"]["string"]

            # Construct address string from bus and device ID
            elif "address" in device["gpib"]:
                deviceID = device["gpib"]["address"]

                # The interface is optional, defaults to 0
                busID = 0
                if "bus" in device["gpib"]:
                    busID = device["gpib"]["bus"]

                address = f"GPIB{busID}::{deviceID}::INSTR"

            else:
                print(f"GPIB entry incomplete for {name}.")
                print("Either an address string (string:) or a device number (address:) must be specified.")
                continue

        # Process 
        if "usb" in device:
            if "string" in device["usb"]:
                address = device["usb"]["string"]
            else:
                logging.warning(f"USB entry incomplete for {name}.")
                continue

        # Check if we have an address
        if address is None:
            logging.warning(f"Device {name} has no VISA address specified.")
            continue

        # Check if device is connected
        if address in connectedDevices:
            # Add connected device
            devices[deviceType][name] = models[deviceType][model](rm, address)
            # Track connected device addresses
            connected.append(address)
            print(f"Loaded connected device {name} with attributes:")
            print(f"\tType: {deviceType}")
            print(f"\tModel: {model}")
            print(f"\tAddress: {address}\n")
        else:
            disconnected[deviceType][name] = (model, address)
            print(f"Loaded disconnected device {name} with attributes:")
            print(f"\tType: {deviceType}")
            print(f"\tModel: {model}")
            print(f"\tAddress: {address}\n")


    for connectedDevice in connectedDevices:
        if connectedDevice not in connected:
            unknown.append(connectedDevice)


    return (devices, disconnected, unknown)
