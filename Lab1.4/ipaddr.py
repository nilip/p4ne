from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def _init_(self):
        IPv4Network.__init__(self)
    def regular(self):
        return not self.is_private
    def key_value(self):
        return int(self.network_address) + int(self.netmask)

l=[]
for x in range(0,5):
    ip1 = IPv4RandomNetwork((random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)
    if ip1.regular():
        l.append(ip1)


for y in sorted(l,key=IPv4RandomNetwork.key_value):
    print(y)