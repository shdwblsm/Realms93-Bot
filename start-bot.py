import time
from datetime import datetime
import sys
import telnetlib
from telnetlib import Telnet 
import interact
 




tn = telnetlib.Telnet("www.windows93.net", 8082)  



# initiate telnet connection for ....

botName = input("Bot Name: ")
password = input("Bot Password: ")
host = "www.windows93.net"
botState = "active"

# Open Session
tn.open(host, 8082)

print("Opening Session")

tn.read_until(b"Please enter your name, or \"new\" if you are new.")
tn.write(botName.encode('ascii') + b"\n")
tn.read_until(b"Please enter your password.")
tn.write(password.encode('ascii') + b"\n")
             
# Look in world
             
# tn.write(b"look\n")

time.sleep(1)

online = "Coming Online..."

tn.write(online.encode('ascii') + b"\n")

while True:    
    
    Output = tn.read_very_eager().decode('ascii')
    now = datetime.now()
    tstamp = now.strftime("[%m/%d/%Y %H:%M] ")
    
    if Output == "":
        continue;
        
    else:
           
        
        # Save a log
        file = open("realms93-log", "a")
        file.write(tstamp + Output)
        file.close()
        
       
        print(Output)
        # Assess Situation

     
        takeAction = interact.assess(Output,botState,botName)
        
        # print('TakeAction variable is ' + takeAction)
        
        
           
        if (takeAction is None):
            continue

            
        else:
            tn.write(takeAction.encode('ascii') + b"\n")

            print('===== GATHERING NEW INPUT =====')

            continue


    
