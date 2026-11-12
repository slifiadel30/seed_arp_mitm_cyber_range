#!/usr/bin/env python3
# ------------------------------------------------------------------
# TP ARP Cache Poisoning - Tache 1B : empoisonnement via ARP reply
# ------------------------------------------------------------------
# Objectif : contrairement a la tache 1A, on envoie ici directement
# une ARP reply (non sollicitee) a A, sans qu'aucune requete n'ait
# ete emise au prealable. Comparez le resultat avec la tache 1A :
# fonctionne-t-elle aussi ? Pourquoi ?
#
# A COMPLETER : definissez op=2 (is-at), hwsrc, psrc, pdst, hwdst.
# ------------------------------------------------------------------

from scapy.all import *

VM_A_IP = "10.0.2.6"
VM_B_IP = "10.0.2.7"

E = Ether()     # TODO
A = ARP()       # TODO : op=2 ...

pkt = E / A
sendp(pkt, iface="eth0")
print("[+] Paquet ARP reply envoye a %s" % VM_A_IP)
