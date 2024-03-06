import RPi.GPIO as GPIO
import time

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
    # Read the data
    value = read_HX711()
    
    # TODO: Calibrate the following values as per your load cell and HX711
    reference_unit = 1  # Set to the value obtained during calibration
    offset = 8435475  # Set to the value obtained during calibration
    
    weight = (value - offset) / reference_unit
    return weight


# def get_weight():
#     value = read_HX711()
    
#     # Put the known weight on the scale and run this script. Replace `known_weight` with your known weight value.
#     known_weight = 204  # Change this to your known weight in grams
    
#     # If running for the first time, set offset to the value read with no weight
#     # After the first run, uncomment the next line and update the offset value
#     offset = 4352  # Replace 0 with the value from the first run with no weight

#     # If running for the first time, comment out the following line until you've obtained the offset
#     reference_unit = (value - offset) / known_weight
    
#     weight = (value - offset) / reference_unit
#     return weight, reference_unit  # Also returning reference unit for calibration



def main():
    # Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PD_SCK, GPIO.OUT)
    GPIO.setup(DOUT, GPIO.IN)
    
    try:
        while True:
            total_weight = get_weight()
            print(f"Total Weight: {total_weight} grams")
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        print("Cleaning up...")
        GPIO.cleanup()


if __name__ == "__main__":
    main()