'''write script for list cleanup: remove duplicates and sort ip addresses

Input: 
    ips = ["192.168.1.10", "10.0.0.1", "192.168.1.10"]
output: 
    ['10.0.0.1', '192.168.1.10']'''
########################################################################################################
ips = ["192.168.1.10", "10.0.0.1", "192.168.1.10"]
ips = list(set(ips))
ips.sort()
print (ips)