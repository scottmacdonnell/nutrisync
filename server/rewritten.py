import collections
import time
import bluetooth
import sys
import subprocess

class Wiiboard:
  def __init__(self):
    self.address = None

    try:
      self.receivesocket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
      self.controlsocket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    except ValueError:
      raise Exception("Error: Bluetooth not found")


  def discover(self):
    print("Press the red sync button on the board now")

    address = None

    bluetooth_devices = bluetooth.discover_devices(duration = 6, lookup_names = True)

    for bluetooth_device in bluetooth_devices:
      if bluetooth_device[1] == "Nintendo RVL-WBC-01":
        address = bluetooth_device[0]
        print("Found Wiiboard at address " + address)

    if address is None:
      print("No Wiiboards discovered")
    
    return address
  

    

def main():
  board = Wiiboard()

  address = input("Enter the Wiiboard address (or press Enter to discover): ")

  if not address:
    print("Discovering board...")
    address = board.discover()
    
    try:
      # Disconnect already-connected devices.
      # This is basically Linux black magic just to get the thing to work.
      subprocess.check_output(["bluez-test-input", "disconnect", address], stderr=subprocess.STDOUT)
      subprocess.check_output(["bluez-test-input", "disconnect", address], stderr=subprocess.STDOUT)
    except:
      pass

    print("Trying to connect...")

    ## CONNECT FUNCTION - Start

    # if address is None:
    #   print("Non existent address")
    #   return


  



if __name__ == "__main__":
  main()