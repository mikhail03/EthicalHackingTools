#!/usr/bin

from datetime import datetime
from socket import *
import sys, time



# Delcaring host settings and prompts
host = ''
max_port = 1024 # Limiting the maximum amount of port to scan
min_port = 1

# This function defines how  the host is scanned
# Using the OS Socket to connect to the intended target
def scan_host(host, port, r_code =1):
    try:
        s = socket(AF_INET, SOCK_STREAM) # Initiates the Socket
        code = s.connect_ex((host, port)) # Executes the connect function and captures the connection results

        if code == 0:
            r_code = code # code that is use to determine if a port is live; 0 = open, 1 = close
        s.close()
    except Exception as e:
        pass
    return r_code

 # initiating Program
 #  This try and except all for only necessary display message
 #  when the user Interrupts the code
try:
    # Request the target address asinput from user
    host = input("[*] Enter Target Host Address: ")
except keyboardInterrupt:
    print("\n\n[*] User Requested An Interrupt.")
    print("[*] Application Shutting Down.")
    sys.exit(1)

# This function simply returns the IP numberic values of a host address or URL, simolar to nslookup
hostip = gethostbyname(host)
print("\n [*] Host: %s IP: %s" % (host, hostip))
print("[*] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port) # Takess to arguments

        if response == 0:
            print("[*] Port %d: Open" % (port))
    except Exception as e:
        pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scanning Finished At %s ..." % (time.strftime("%H:%M:%S")))
print("[*] Scanning Duration: %s ..."% (total_time_duration))
print("[*] Reconnaissance Complete!")
