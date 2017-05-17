import re
test = "?????? (xxx.xxx.x.xxx) em xx:xx:xx:xx:xx:xx [xx] em xx"
mac = re.findall('\S+:\S+',test)
print(test)
print(mac)