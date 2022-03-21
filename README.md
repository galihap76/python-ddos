## Python DDOS
I build small python script DDOS syn flooding you can modify my script.

## What Is DDOS On Syn Flood Attack?
Ok i will share a article on <a href="https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python">thepythoncode</a>. A SYN flood attack is a common form of a denial of service attack in which an attacker sends a sequence of SYN requests to the target system (can be a router, firewall, Intrusion Prevention Systems (IPS), etc.) in order to consume its resources, preventing legitimate clients to establish a normal connection.
TCP SYN flood exploits the first part of the TCP three-way handshake, and since every connection using the TCP protocol requires it, this attack proves to be dangerous and can take down several network components.
In order to understand SYN flood, we first need to talk about TCP three-way handshake:

![3-way-tcp-handshake](https://user-images.githubusercontent.com/83481679/159235337-388bc0b2-a077-4f06-a1cb-7f5ae479232f.png)

When a client wants to establish a connection to a server via TCP protocol, the client and server exchanges series of messages:
- The client requests a connection by sending SYN message to the server
- The server responds with SYN-ACK message (acknowledges the request)
- The clients responds back with an ACK, and then the connection is started

SYN flood attack involves a malicious user that sends SYN packets repeatedly without responding with ACK, and often with different source ports, which makes the server unaware of the attack, and responds to each attempt with a SYN-ACK packet from each port (The red and green part of the above image). In this way, the server will quickly be unresponsive to legitimate clients.

## Install 
**Windows & Linux**
```
git clone https://github.com/galihap76/python-ddos.git
```

**Termux**
- pkg update && pkg upgrade
- pkg install python3 
- pkg install git
- git clone https://github.com/galihap76/python-ddos.git
- cd python-ddos
- python3 main.py -d <ip target> -p <port target>

## Usage
**windows**
```
main.py -d <ip target> -p <port target>
```
**linux**
```
python3 main.py -d <ip target> -p <port target>
```

## Note
If you want do attack ddos on website first i recommend you to need learn networking.
