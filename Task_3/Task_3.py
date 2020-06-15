import socket
import sys
import urllib.request

url = 'fob.zlol.lg.ua'
port = int(sys.argv[1])


def banner_grabbing(address):
    file = open('banner.txt','w')
    print("Getting service information for port: ", port)
    banner_grabber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    banner_grabber.connect((address, port))
    banner = banner_grabber.recv(100)
    file.write(str(banner))
    banner_grabber.close()
    print(banner, "\n")

# Check if port is open
def check_ports(url):
    global result
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url,port))
    if result == 0: # Check if port is open
       banner_grabbing(url)
    else:
        print (str(port) + ' Port is not open')

if port == 80:
    contents = urllib.request.urlopen('http://'+ str(url)).read()
    print(contents[:200])
else:
    check_ports(url)

