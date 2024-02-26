import RPi.GPIO as GPIO
import time
from hx711 import HX711

def clean_and_exit():
    print("Cleaning...")
    GPIO.cleanup()  # Clean up GPIO to reset pins
    print("Bye!")
    sys.exit()

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=5, pd_sck_pin=6)

hx.zero()

while True:
    try:
        val = hx.get_weight(5)
        print(f"Weight: {val} grams")
        hx.power_down()
        hx.power_up()
        time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        clean_and_exit()