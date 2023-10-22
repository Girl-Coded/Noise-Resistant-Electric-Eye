import machine 
import time
import utime
import environment
from sms_internet import connect_to_internet, send_sms

def connect_wifi():
    ssid = environment.SSID
    password = environment.PASSWORD
    connect_to_internet(ssid, password)

message_sent = False
def main():
    global message_sent
    connect_wifi()
    if not message_sent:
        current_time = utime.localtime()  # Gets current date and time
        formatted_time = "{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(year=current_time[0],
                                                                                         month=current_time[1], day=current_time[2],HH=current_time[3], MM=current_time[4], SS=current_time[5])
        
        message = 'Testing sending at ' + formatted_time
        send_sms(environment.recipient, environment.sender, message, environment.auth_token, environment.account_sid)
        message_sent = True
        time.sleep(2)
    time.sleep(5)    
        
if __name__ == "__main__":
    main()

