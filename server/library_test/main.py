import time
from hx711 import HX711

def clean_and_exit():
    print("Cleaning...")
    if hx is not None:
        hx.power_down()
    print("Bye!")
    sys.exit()

hx = HX711(dout_pin=5, pd_sck_pin=6)

# I'm setting the reference unit to 1 for now. You will need to calibrate your scale.
# Each scale will need individual calibration.
hx.set_reference_unit(1)

hx.reset()
hx.tare()

print("Tare done! Add weight now...")

# To get weight from the HX711 module
while True:
    try:
        val = hx.get_weight(5)
        print(f"Weight: {val} grams")

        # To get more accurate readings,
        # you may want to discard the first few readings
        # and average several readings together

        hx.power_down()
        hx.power_up()
        time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        clean_and_exit()