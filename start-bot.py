
# coding: utf-8

# In[1]:


import time
import sys
import telnetlib
from telnetlib import Telnet 

tn = telnetlib.Telnet("www.windows93.net", 8082)  
        
# initiate telnet connection for ....


user = input("Bot Name: ")
password = input("Bot Password: ")
host = "www.windows93.net"

# Open Session
tn.open(host, 8082)

print("Opening Session")

tn.read_until(b"Please enter your name, or \"new\" if you are new.")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Please enter your password.")
tn.write(password.encode('ascii') + b"\n")
             
# Look in world
             
tn.write(b"look\n")

time.sleep(1)

Output = tn.read_very_eager().decode('ascii')

print(Output)


             
       
#


# In[2]:


tn.close()

