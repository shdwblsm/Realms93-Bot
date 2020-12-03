#####################################
#      Provide Ways to Interact     #
#####################################
import telnetlib
from telnetlib import Telnet
from datetime import datetime
import sys

tn=telnetlib.Telnet("www.windows93.net", 8082)

def see():
    while True:    
        Output = tn.read_very_eager().decode('ascii')
        now = datetime.now()
        tstamp = now.strftime("[%m/%d/%Y %H:%M] ")
                    
        if Output == "":
            continue;
        else:
            print(Output)
            
                                                              
            # Save a log
            file = open("realms93-log", "a")
            file.write(tstamp + Output)
            file.close()

