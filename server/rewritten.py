import collections
import time
import bluetooth
import sys
import subprocess

class Wiiboard:
  def __init__(self):
    self.address = None
    # self.processor = processor
    self.calibration = []
    self.calibrationRequested = False
    self.LED = False
    self.address = None
    self.buttonDown = False
    self.status = "Disconnected"
    # self.lastEvent = BoardEvent(0, 0, 0, 0, False, False)

    # Sockets and status
    self.receivesocket = None
    self.controlsocket = None

    for i in range(3):
      self.calibration.append([10000] * 4)  # high dummy value so events with it don't register

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
  

    def connect(self, address):
      if address is None:
        print("Non existent address")
        return
      
      self.receivesocket.connect((address, 0x13))
      self.controlsocket.connect((address, 0x11))

      if self.receivesocket and self.controlsocket:
        print("Connected to Wiiboard at address " + address)
        self.status = "Connected"
        self.address = address
        self.calibrate()
        useExt = ["00", COMMAND_REGISTER, "04", "A4", "00", "40", "00"]
        self.send(useExt)
        self.setReportingType()
        print("Wiiboard connected")
      else:
        print("Could not connect to Wiiboard at address " + address)


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
  board.connect(address) # Wiiboard must be in sync mode


if __name__ == "__main__":
  main()