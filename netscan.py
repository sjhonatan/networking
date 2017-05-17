import subprocess
import time
from subprocess import *
import sys

if not len(sys.argv) > 1:
    print("[*] pass an IP as argument")
else:
    ip = sys.argv[1]
    ip,Range = ip.split("-")

first = ip.split(".")[-1]
ip = ip[:-len(first)]

for i in range(int(first),int(Range)):
    ip2 = ip + str(i)
    cmd = "ping -c 4 " + ip2
    try:
        host = str(subprocess.check_output(cmd,shell=True))
        if "4 received" in host:
            print("[*] Host is up : " + ip2)
            cmd = "host " + ip2 
            hostName = str(subprocess.check_output(cmd,shell=True)).split(" ")[-1].split(".")[0]
            print("[***] Host name : " + hostName)

    except Exception:
        print("[-] Host down : " + ip2)
