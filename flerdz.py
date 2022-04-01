#!/usr/bin/env python
# coding: utf-8
'''
Project 5 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
print("Quick script to flood a port while learning about Scapy for Network sniffing and modification. Limited to 15 packets. DO NOT MODIFY.")

from scapy.all import *

def floodz(source,target):
	for source_p in range(10,25):
		IPlayer=IP(src=source,dst=target)
		TCPlayer=TCP(sport=source_p,dport=600)
		pkt=IPlayer/TCPlayer
		send(pkt)

source="127.0.0.1"
target="138.197.13.202"
floodz(source,target)

print("\nThat was the weakest flood I've ever seen. Not even a trickle.")

