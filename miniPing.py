# type: ignore
from scapy.all import *
target = input("Enter target IP: ")
req = IP(dst=target)/ICMP(type='echo-request')
count = 0
print("Sending 4 requests")
for i in range(4):
    res = sr1(req, timeout=1)
    if res and res[ICMP].type == 0:
        count += 1
print("Received ",count," reply packages")
    
        