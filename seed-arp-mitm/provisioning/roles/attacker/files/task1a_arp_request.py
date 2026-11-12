#!/usr/bin/env python3
# ------------------------------------------------------------------
# TP ARP Cache Poisoning - Tache 1A : empoisonnement via ARP request
# ------------------------------------------------------------------
# Objectif : depuis M, forger un paquet ARP request envoye a A, tel
# que le cache ARP de A associe l'IP de B a l'adresse MAC de M.
#
# Rappel (voir le sujet) : ls(ARP) dans un shell python3 affiche les
# champs disponibles : hwtype, ptype, hwlen, plen, op, hwsrc, psrc,
# hwdst, pdst.
#
# A COMPLETER : definissez hwsrc, psrc, pdst, hwdst, op et l'adresse
# MAC de destination de la trame Ethernet.
# ------------------------------------------------------------------

from scapy.all import *

VM_A_IP = "10.0.2.6"   # Client (A) - la victime dont on empoisonne le cache
VM_B_IP = "10.0.2.7"   # Serveur (B) - l'IP que l'on veut usurper
MY_MAC  = get_if_hwaddr("eth0")  # Adressez-vous l'interface correcte si besoin

E = Ether()     # TODO : hwdst = adresse MAC de A
A = ARP()       # TODO : op, hwsrc, psrc, pdst

pkt = E / A
sendp(pkt, iface="eth0")
print("[+] Paquet ARP request envoye a %s" % VM_A_IP)
