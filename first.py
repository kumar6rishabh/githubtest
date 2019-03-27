from scapy.all import *
from scapy.all import rdpcap
import math
p = rdpcap('/root/Downloads/udp_refined.pcap')
src_addr = []
for i in range(len(p)):
    if p[i]['IP'].src not in src_addr:
        src_addr.append(p[i]['IP'].src)
print(src_addr)

src_addr_count = []
src_addr_count = [0]*(len(src_addr))
for i in range(len(p)):
    for j in range(len(src_addr)):
        if p[i]['IP'].src == src_addr[j]:
            src_addr_count[j]+=1
print(src_addr_count)
for i in range(len(src_addr)):
    print("number of 100 threshold alerts for " + str(src_addr[i]) + " is " + str(int(math.floor(src_addr_count[i]/100))))
    print("number of 1000 threshold alerts for "+ str(src_addr[i]) + " is " + str(int(math.floor(src_addr_count[i]/1000))))
    print("number of 5000 threshold alerts for "+ str(src_addr[i]) + " is " + str(int(math.floor(src_addr_count[i]/5000))))
    print("number of 10000 threshold alerts for "+str(src_addr[i]) + " is " + str(int(math.floor(src_addr_count[i]/10000))))
print("")
print("")
subnet = []
for i in range(len(src_addr)):
    l = src_addr[i].split(".")
    if(l[2] not in subnet):
        subnet.append(l[2])
print(subnet)
print("")
print("")
subnet_count = []
subnet_count = [0]*(len(subnet))
for i in range(len(p)):
    for j in range(len(subnet)):
        l = (str(p[i]['IP'].src)).split(".")
        if(l[2] == subnet[j]):
            subnet_count[j]+=1
print(subnet_count) 
print("")
print("")
for i in range(len(subnet)):
    print("100      " + str(int(math.floor(subnet_count[i]/100))))
    print("1000     " + str(int(math.floor(subnet_count[i]/1000))))

print("")
print("")

c = 0
port = []

port_count = 0
for i in range(len(subnet)):
    for j in range(len(p)):
        if(subnet[i] == ((str(p[j]['IP'].src)).split("."))[2]):
            if(p[j].sport not in port):
                port.append(p[j].sport)
                port_count+=1 
print(port)
print(port_count)
print("")
print("")

for i in range(len(port)):
    for j in range(len(subnet)):
        for k in range(len(p)):
            if((subnet[j] == ((str(p[k]['IP'].src)).split("."))[2])):
                if(p[k].sport == port[i]):
                    c = c + 1
print(c) 
c=0

