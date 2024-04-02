import yaml
from os.path import isfile
import Devices.LockIn

# Dictionary for calling the correct class for each model
models = {
    "sr830": Devices.LockIn.SR830
}

types = {
    "lockin": "Lock-in amplifier"
}

def readConfig(rm):

    # Enumerate connected devices to avoid loading
    # those that are not connected

    # connectedDevices = rm.list_resources()

    # Placeholder:
    connectedDevices = ("GPIB0::9::INSTR", "GPIB0::10::INSTR", "GPIB0::11::INSTR", "GPIB0::12::INSTR")

    # Nested dictionary to be populated and returned
    devices = {
        "lockin": {}
    }

    # Check if the config file has .yaml or .yml extension
    # In the future, the config should be moved into
    # a standardized location
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

            # Check if device is connected
            if address not in connectedDevices:
                print(f"{name} not connected (address: {address})")
                continue

        else:
            print(f"No GPIB entry found for {name}, skipping to next device.")
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
            if model not in models:
                print(f"{name} has unknown model {model}.")
                print(f"The following models are supported: {list(models.keys())}.")
                continue
        else:
            print(f"No model entry found for {name}, skipping to next device.")
            continue

        devices[deviceType][name] = models[model](rm, address)
        print(f"Loaded device {name} with attributes:")
        print(f"\tType: {deviceType}")
        print(f"\tModel: {model}")
        print(f"\tAddress: {address}\n")

    return devices
