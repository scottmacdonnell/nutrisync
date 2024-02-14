import bluetooth
import struct
import time

CONTINUOUS_REPORTING = b'\x04'
COMMAND_REPORTING = b'\x12'
INPUT_READ_DATA = b'\x21'
EXTENSION_8BYTES = b'\x32'

# Bluetooth device name of the Wii Balance Board
BLUETOOTH_NAME = "Nintendo RVL-WBC-01"

class WiiBalanceBoard:
    def __init__(self, address):
        self.address = address
        self.sock = None
        self.connected = False

    def connect(self):
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
            self.sock.connect((self.address, 0x13))
            self.connected = True
            print("Connected to Wii Balance Board")

            # Set reporting type
            self.sock.send(CONTINUOUS_REPORTING + COMMAND_REPORTING + EXTENSION_8BYTES)

        except Exception as e:
            print(f"Error: {e}")
            self.disconnect()

    def disconnect(self):
        if self.connected:
            self.sock.close()
            self.connected = False
            print("Disconnected from Wii Balance Board")

     def read_data(self):
        if not self.connected:
            print("Not connected to Wii Balance Board")
            return None

        try:
            data = self.sock.recv(25)
            input_type = data[2]

            if input_type == INPUT_READ_DATA:
                raw_data = struct.unpack('>hhhhhhhh', data[6:22])  # Adjust the index to start from 6
                return {
                    'top_right': raw_data[0],
                    'bottom_right': raw_data[1],
                    'top_left': raw_data[2],
                    'bottom_left': raw_data[3],
                    'total_weight': raw_data[4]
                }

        except Exception as e:
            print(f"Error reading data: {e}")

        return None
         
if __name__ == "__main__":
    # Discover Wii Balance Board
    print("Discovering Wii Balance Board...")
    address = None
    while not address:
        devices = bluetooth.discover_devices(lookup_names=True, duration=8)
        for addr, name in devices:
            if name == BLUETOOTH_NAME:
                address = addr
                break
        if not address:
            print("Wii Balance Board not found. Make sure it's in sync mode.")
            time.sleep(2)

    print(f"Found Wii Balance Board at address {address}")

    # Connect to Wii Balance Board
    wii_board = WiiBalanceBoard(address)
    wii_board.connect()

    try:
        while True:
            sensor_data = wii_board.read_data()
            if sensor_data:
                print(sensor_data)
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    finally:
        wii_board.disconnect()
