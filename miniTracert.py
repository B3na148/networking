# type: ignore
from scapy.all import *
import time
import sys
if len(sys.argv) < 2:
    print("Error expected a target")
    exit(1)
target = sys.argv[1]
for i in range(1, 255):
    req = IP(ttl=i, dst=target)/ICMP()
    snt = time.time()
    res = sr1(req)
    rcd = time.time()
    if int(res[ICMP].type) == 0:
        break
    print(str(res[IP].src))
    print("Time took:", round(1000*(rcd - snt), 2), "ms")

