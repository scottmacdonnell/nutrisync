import RPi.GPIO as GPIO
import time

# Define the pins we're using
DOUT = 5
PD_SCK = 6

# We're using the BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define DOUT as an input pin and PD_SCK as an output pin
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(PD_SCK, GPIO.OUT)

# This function will read data from the HX711
def read_HX711():
    count = 0
    # Make sure the chip is ready
    GPIO.output(PD_SCK, False)
    while GPIO.input(DOUT) == 1:
        time.sleep(0.01)

    # Read 24 bits of data
    for i in range(24):
        GPIO.output(PD_SCK, True)
        count = count << 1

        GPIO.output(PD_SCK, False)
        if GPIO.input(DOUT) == 1:
            count += 1

    # This will trigger the next conversion
    GPIO.output(PD_SCK, True)
    count = count ^ 0x800000
    GPIO.output(PD_SCK, False)
    
    return count

# This function will convert the data to weight
def get_weight():
    value = read_HX711()
    # Set your calibration factor here, which you'll need to determine experimentally
    calibration_factor = -7050
    weight = value / calibration_factor
    return weight

try:
    # Infinite loop to continuously check the weight
    while True:
        weight = get_weight()
        print(f"Total Weight: {weight} grams")
        time.sleep(5)

# Clean up cleanly on Ctrl+C
except (KeyboardInterrupt, SystemExit):
    print("Cleaning up...")
    GPIO.cleanup()