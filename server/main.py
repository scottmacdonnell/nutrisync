import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

# hx = HX711(dout_pin=5, pd_sck_pin=6)

GPIO.input(5)

GPIO.cleanup()
