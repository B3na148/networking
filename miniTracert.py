# type: ignore
from scapy.all import *

for i in range(1, 255):
    req = IP(ttl=i, dst='www.google.com')/ICMP()
    res = sr1(req)
    if int(res[ICMP].type) == 0:
        break
    print(str(res[IP].src))

