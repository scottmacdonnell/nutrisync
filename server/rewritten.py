import collections
import time
import bluetooth
import sys
import subprocess

def main():
  address = input("Enter the Wiiboard address (or press Enter to discover): ")

  if not address:
    print("Discovering board...")
    
    ## DISCOVER FUNCTION - Start

    print("Press the red sync button on the board now")
    bluetooth_devices = bluetooth.discover_devices(duration = 6, lookup_names = True)

    for bluetooth_device in bluetooth_devices:
      if bluetooth_device[1] == "Nintendo RVL-WBC-01":
        address = bluetooth_device[0]
        print("Found Wiiboard at address " + address)
      if address is None:
        print("No Wiiboards discovered")

    ## DISCOVER FUNCTION - End




if __name__ == "__main__":
  main()