import machine
import time
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
        message = 'Testing sending.'
        send_sms(environment.recipient, environment.sender, message, environment.auth_token, environment.account_sid)
        message_sent = True
        time.sleep(2)
    time.sleep(5)    
        
if __name__ == "__main__":
    main()

