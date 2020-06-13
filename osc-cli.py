#!/usr/bin/python

import sys, getopt
from pythonosc import udp_client

def send_osc(ip, port, msg):
    client = udp_client.SimpleUDPClient(ip, port)
    client.send_message(msg.pop(0), msg)

def main(argv):
    ip = "127.0.0.1"
    port = 57120
    oscmsg = ""
    help = "-a <ip> -p <port> message"
    try:
        opts, args = getopt.getopt(argv,"ha:p:",["ip=", "port="])
    except getopt.GetoptError:
        # print("-a <ipaddress> -p <port>")
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            # print('test.py -a <ipaddress> -p <port>')
            print(help)
            sys.exit()
        elif opt in ("-a", "--ip"):
            ip= arg
        elif opt in ("-p", "--port"):
            port = arg
        else:
            oscmsg = arg
    print("Sending to {}:{}".format(ip, port))
    print("OSC: ", args)
    send_osc(ip, port, args)

if __name__ == "__main__":
        main(sys.argv[1:])
