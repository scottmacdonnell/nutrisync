import RPi.GPIO as GPIO
import time
from hx711 import HX711

DOUT = 5
PD_SCK = 6

def read_HX711():
    count = 0
    GPIO.output(PD_SCK, False)
    
    # Wait for the HX711 to become ready
    while GPIO.input(DOUT) == 1:
        pass
    
    # Read out 24-bit data from HX711
    for i in range(24):
        GPIO.output(PD_SCK, True)
        count = count << 1
        GPIO.output(PD_SCK, False)
        if GPIO.input(DOUT) == 0:
            count += 1
            
    # Set the channel and gain factor for next reading
    GPIO.output(PD_SCK, True)
    count ^= 0x800000  # XOR to flip the 25th bit
    GPIO.output(PD_SCK, False)
    
    return count


def get_weight():
    value = read_HX711()
    
    # TODO: Calibrate the following values as per your load cell and HX711
    reference_unit = 204  # Set to the value obtained during calibration
    offset = 411352.82843137255  # Set to the value obtained during calibration
    
    weight = (value - offset) / reference_unit
    return weight


def main():
    # Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    # GPIO.setup(PD_SCK, GPIO.OUT)
    # GPIO.setup(DOUT, GPIO.IN)
    hx = HX711(dout=5, pd_sck=6)
    
    try:
        while True:
            # total_weight = get_weight()
            # print(f"Total Weight: {total_weight} grams")
            # time.sleep(5)
            reading = hx.get_raw_data_mean()
            print(reading)
    except (KeyboardInterrupt, SystemExit):
        print("Cleaning up...")
        GPIO.cleanup()


if __name__ == "__main__":
    main()