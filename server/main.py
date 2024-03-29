import RPi.GPIO as GPIO
from hx711 import HX711
from ISStreamer.Streamer import Streamer


# GPIO variables
DOUT = 5
PD_SCK = 6


# InitialState variables
IS_BUCKET_KEY = 'JU7LEGUYKGCX'
IS_ACCESS_KEY = 'ist_OZVQ3ePTE04kTXweWIzTkjtfIeftBfg8'


def status(format_code, message):
    escape_code = '\033[0m'
    message = message[:6]
    total_spaces = 6 - len(message)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    s = ' ' * left_spaces + message + ' ' * right_spaces
    return '[' + format_code + s + escape_code + '] '


def get_weight_average(hx, quantity):
    data = 0.0
    for i in range(quantity):
        print(status('\033[34m', 'SYNC') + f'Reading weight {i + 1}/{quantity}')
        data += hx.get_weight_mean()
    print(status('\033[32m', 'OK') + 'Set weight data')
    print(status('\033[34m', 'SYNC') + 'Calculating average weight')
    return data /quantity


def pound_conversion(grams):
    pounds = grams * 0.00220462
    return pounds


def send_weight_to_initialstate(bucket_key, access_key, weight):
    streamer = Streamer(access_key=access_key, bucket_key=bucket_key)
    print(status('\033[32m', 'OK') + 'Streamer object created')
    
    try:
        print(status('\033[34m', 'SYNC') + 'Streaming to InitialState')
        streamer.log("Weight", weight)
        print(status('\033[32m', 'OK') + 'Weight data sent successfully to InitialState')
    except Exception as e:
        print(status('\033[31m', 'FAILED') + f'Error sending weight data to InitialState: {e}')
    finally:
        print(status('\033[34m', 'SYNC') + 'Closing streamer connection')
        streamer.close()
        print(status('\033[32m', 'OK') + 'Streamer object closed')
        

def main():
    try:
        GPIO.setwarnings(False)
        print(status('\033[32m', 'OK') + 'All GPIO warnings disabled')
        
        GPIO.setmode(GPIO.BCM)
        print(status('\033[32m', 'OK') + 'Set GPIO mode to BCM')
        
        hx = HX711(dout_pin=DOUT, pd_sck_pin=6)
        print(status('\033[32m', 'OK') + 'Set DOUT pin to ' + str(DOUT))
        print(status('\033[32m', 'OK') + 'Set PD_SCK pin to ' + str(PD_SCK))
        
        print(status('\033[34m', 'SYNC') + 'Reading offset value')
        hx.zero()
        print(status('\033[32m', 'OK') + 'Set offset value')
        
        input(status('\033[35m', 'IN') + 'Place known weight on scale and press enter')
        print(status('\033[34m', 'SYNC') + 'Reading data')
        reading = hx.get_data_mean(readings=100)
        print(status('\033[32m', 'OK') + 'Set default readings')
        
        known_weight = float(input(status('\033[35m', 'IN') + 'Enter the known weight in grams and press enter: '))
        print(status('\033[32m', 'OK') + 'Set known weight')
        print(status('\033[34m', 'SYNC') + 'Calculating scale ratio')
        ratio = reading / known_weight
        hx.set_scale_ratio(ratio)
        print(status('\033[32m', 'OK') + 'Set scale ratio')
        
        input(status('\033[35m', 'IN') + 'Step on scale and press enter')
        weight = get_weight_average(hx, 10)
        print(status('\033[32m', 'OK') + 'Set average weight')
        
        print(status('\033[32m', 'OK') + f'Average weight: {str(weight)}g')
        
        print(status('\033[34m', 'SYNC') + 'Calculating weight in lbs')
        weight_lbs = pound_conversion(weight)
        print(status('\033[32m', 'OK') + 'Set weight in lbs')
        print(status('\033[32m', 'OK') + f'Average weight: {str(weight_lbs)}lb')
        
        print(status('\033[32m', 'OK') + 'Start uploading weight to InitialState')
        send_weight_to_initialstate(IS_BUCKET_KEY, IS_ACCESS_KEY, weight_lbs)
    except (KeyboardInterrupt, SystemExit):
        print('\n' + status('\033[32m', 'OK') + 'Ending processes')
        GPIO.cleanup()
    finally:
        print(status('\033[32m', 'OK') + 'Ending processes')
        GPIO.cleanup()


if __name__ == "__main__":
    main()