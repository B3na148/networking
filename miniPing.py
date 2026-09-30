# type: ignore
from scapy.all import *
target = input("Enter target IP: ")
req = IP(dst=target)/ICMP(type='echo-request')
packet_count = int(input("How many packets do you want to send?"))
print("Sending ", packet_count, "requests")
ans, unans = sr(req * packet_count, timeout = 2)
print("Received ",len(ans)," reply packages")
    
        