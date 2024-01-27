from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket

def test_port_number(host, port):

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((host, port))
            return True
        except:
            return False

def port_scan(host, port):
    print(f'Scanning {host}...')
    for port in port:
        if test_port_number(host, port):
            print(f'> {host}:{port} open')
        else:
            print('This port is closed')
HOST = input("Enter domian namw")
PORTS = range(1024)
port_scan(HOST, PORTS)
