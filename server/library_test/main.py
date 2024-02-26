import RPi.GPIO as GPIO
from hx711 import HX711

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)

reading = hx.get_raw_data_mean()
print(reading)