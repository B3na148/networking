# type: ignore
# This file will be my mini nmap self created.
from scapy.all import *
target = input("Enter target IP or domain name: ")
open_ports = []
for i in range(20, 1025):
    syn_req = IP(dst=target)/TCP(flags='S',dport=i,seq=123)
    ret = sr1(syn_req, timeout=0.2)
    if ret:
        if ret[TCP].flags == 'SA':
            open_ports.append(i)
        else:
            print(i, "is closed (a)")
    else:
        print(i, "is closed (b)")

print("open ports: ", open_ports)
    