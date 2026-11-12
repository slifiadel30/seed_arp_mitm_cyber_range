#!/usr/bin/env python3
# ------------------------------------------------------------------
# TP ARP Cache Poisoning - Tache 1C : gratuitous ARP
# ------------------------------------------------------------------
# Caracteristiques d'un paquet gratuitous ARP (voir sujet) :
#   - IP source == IP destination == IP de la machine qui l'emet
#   - MAC destination (Ethernet ET ARP) = broadcast ff:ff:ff:ff:ff:ff
#   - aucune reponse n'est attendue
#
# A COMPLETER.
# ------------------------------------------------------------------

from scapy.all import *

VM_B_IP = "10.0.2.7"   # IP que M usurpe aupres de TOUTES les machines du LAN

E = Ether()     # TODO : hwdst = broadcast
A = ARP()       # TODO : op, hwsrc, psrc=pdst=VM_B_IP, hwdst=broadcast

pkt = E / A
sendp(pkt, iface="eth0")
print("[+] Gratuitous ARP envoye en broadcast")
