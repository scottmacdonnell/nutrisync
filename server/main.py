import RPi.GPIO as GPIO
from hx711 import HX711

def status(format_code, message):
    escape_code = '\033[0m'
    message = message[:6]
    total_spaces = 6 - len(message)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    s = ' ' * left_spaces + message + ' ' * right_spaces
    return '[' + format_code + s + escape_code + '] '
    

def main():
    GPIO.setmode(GPIO.BCM)
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    
    hx.zero()
    
    input(status('\033[32m', 'OK') + 'Place known weight on scale and press enter')
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