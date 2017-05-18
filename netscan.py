import subprocess
from subprocess import *
import re
import sys
import progressbar as pbar

if not len(sys.argv) > 1:
    print("[*] pass an IP as argument")
else:
    ip = sys.argv[1]
    ip,Range = ip.split("-")

arp_table = str(subprocess.check_output("arp -a",shell = True))
arp_table = arp_table.split('\\n')

first = ip.split(".")[-1]
ip = ip[:-len(first)]
j = 0
macAddresses = []
hostUp = []
hostNames = []

print('\n')

for i in range(int(first),int(Range)):
    ip2 = ip + str(i)
    mac = 'None'
    hostName = 'None'
    cmd = "ping -c 1 -w 0.1 "  + ip2
    j+=1
    msg = "Scanning network "
    pbar.printProgressBar(j,int(Range)-int(first), prefix = msg,\
                          suffix = 'Complete',length = 30)
    try:
        host = str(subprocess.check_output(cmd,shell=True))
        if "1 received" in host:
            hostUp.append(ip2)
            cmd = "host " + ip2 
            hostName = str(subprocess.check_output(cmd,shell=True)).split(" ")[-1].split(".")[0]
            for arp in arp_table:
                if hostName in arp:
                    mac = re.findall('\S+:\S+',arp)
            hostNames.append(hostName)
            macAddresses.append(mac[0])
    
    except Exception:
        pass


for i in range(len(hostUp)):
    print('\n')
    print("[***] Host Ip :" + hostUp[i])
    print("[***] Host Mac Address : " +macAddresses[i])
    print("[***] Host Name : " +hostNames[i])
