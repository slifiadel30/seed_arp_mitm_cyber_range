#!/usr/bin/env python3
# ------------------------------------------------------------------
# TP ARP Cache Poisoning - Tache 3 : MITM sur Netcat
# ------------------------------------------------------------------
# Un message est echange automatiquement toutes les ~15 secondes
# entre A (10.0.2.6) et B (10.0.2.7, port 9090) via Netcat.
#
# Etape 1 (sniffing) : une fois le MITM en place (voir tache 2),
# capturez ce trafic en clair et lisez le code secret transmis.
#
# Etape 2 (bonus, optionnel) : comme dans le sujet original, modifiez
# le programme pour remplacer chaque occurrence du mot de code par
# une sequence de 'A' de meme longueur avant de retransmettre le
# paquet vers B (attention a ne pas casser les numeros de sequence
# TCP : la longueur du payload doit rester identique).
# ------------------------------------------------------------------

from scapy.all import *

VM_A_IP = "10.0.2.6"
VM_B_IP = "10.0.2.7"
NC_PORT = 9090

def handle_pkt(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == NC_PORT and pkt[TCP].payload:
        data = bytes(pkt[TCP].payload)
        print("[SNIFF] %s -> %s : %r" % (pkt[IP].src, pkt[IP].dst, data))
        # TODO (bonus) : construire ici un paquet de substitution avec
        # scapy (comme dans task2_sniff_spoof_telnet.py) et le renvoyer
        # a la place du paquet original.

sniff(filter="tcp port %d" % NC_PORT, prn=handle_pkt)
