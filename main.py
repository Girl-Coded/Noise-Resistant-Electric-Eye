import machine 
import time
import utime
import environment
from sms_internet import connect_to_internet, send_sms


button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

def connect_wifi():
    ssid = environment.SSID
    password = environment.PASSWORD
    connect_to_internet(ssid, password)
    
def delay_alot():
    for i in 30000:
        d+=1

def main():
    #global message_sent
    connect_wifi()
    
    #if not message_sent:
    while True:
        
        print(button.value())
        if button.value() != 0:
            
            current_time = utime.localtime()  # Gets current date and time
            formatted_time = "{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=current_time[3], MM=current_time[4], SS=current_time[5])
            formatted_date = "{month:>02d}/{day:>02d}/{year:>04d}".format(month=current_time[1], day=current_time[2], year=current_time[0])
            message = 'Critical Safety Event at ' + formatted_time + ' on ' + formatted_date
            send_sms(environment.recipient, environment.sender, message, environment.auth_token, environment.account_sid)
            while button.value() != 0:
                time.sleep(0.1)
                print(button.value())
        time.sleep(0.1)
        
if __name__ == "__main__":
    main()

