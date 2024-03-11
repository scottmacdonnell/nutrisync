import RPi.GPIO as GPIO
from hx711 import HX711

def status(escape, message):
    return '[' + escape + message + '\x1b[0m]'
    

def main():
    print(status('\x1b[0;32;40', '  OK  '))
    GPIO.setmode(GPIO.BCM)
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    
    hx.zero()
    
    input('[' + '\x1b[0m]' + 'Place known weight on scale and press enter')
    reading = hx.get_data_mean(readings=100)
    
    known_weight = float(input('Enter the known weight in grams and press enter: '))
    ratio = reading / known_weight
    hx.set_scale_ratio(ratio)
    
    try:
        while True:
            weight = hx.get_weight_mean()
            print(weight)
    except (KeyboardInterrupt, SystemExit):
        print("Cleaning up...")
        GPIO.cleanup()


if __name__ == "__main__":
    main()