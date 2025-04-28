'''Write function to Parse Tuple Configuration

Input:
    config = ("localhost", "192.168.1.1", 22)

Output:
    Host: localhost
    IP: 192.168.1.1
    Port: 22'''
########################################################################################################
config = ("localhost", "192.168.1.1", 22)
def parse_tuple (config):
    host, ip, port = config
    print ("host:", host)
    print ("IP:", ip)
    print ("port:", port)

parse_tuple(config)
    