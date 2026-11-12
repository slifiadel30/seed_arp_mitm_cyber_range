# TP Securite des Systemes - ARP Cache Poisoning & MITM

Adapte du *SEED Labs "ARP Cache Poisoning Attack Lab"* (Wenliang Du, 2019).
Note sur **20 points**. Duree estimee : **~30 minutes**.

## Disclaimer

TP a but strictement pedagogique, dans un environnement isole. Toute
utilisation des techniques enseignees contre un systeme sans autorisation
explicite est illegale

## Topologie

3 machines SEED sur un **meme segment reseau** (aucun routeur), flavor
`m1.medium` :

- **M** (`attacker`, `10.0.2.5`) : poste de l'etudiant / attaquant.
- **A** (`client`, `10.0.2.6`) : victime 1, client Telnet / Netcat.
- **B** (`server`, `10.0.2.7`) : victime 2, serveur Telnet / Netcat.

## Niveau 2 : Cartographie du reseau local (3 pts)

**Objectif pedagogique** : reconnaissance reseau avec `nmap` / `arp-scan`.
**Flag** : `23` (port Telnet de B).

## Niveau 3 : ARP Cache Poisoning via ARP request - Task 1A (3 pts)

**Objectif pedagogique** : forger un paquet ARP avec Scapy, comprendre les
champs `op`, `hwsrc`, `psrc`, `hwdst`, `pdst`.
**Flag** : `1` (valeur du champ `op` pour un ARP request).

## Niveau 4 : ARP reply et gratuitous ARP - Tasks 1B / 1C (2 pts)

**Objectif pedagogique** : comparer 3 techniques d'empoisonnement ARP
(request, reply non sollicite, gratuitous ARP en broadcast).
**Flag** : `gratuitous`.

## Niveau 5 : MITM complet sur Telnet - Task 2 (4 pts, flag variable)

**Objectif pedagogique** : empoisonnement bidirectionnel, activation de
`ip_forward`, observation du trafic Telnet en clair via Wireshark/tcpdump.
**Flag** : contenu de la variable `motd_secret` (unique par sandbox),
injecte dans la banniere Telnet de B et visible uniquement en sniffant
le trafic A<->B relaye par M.

## Niveau 6 : Modification du trafic Telnet - Task 2 suite (4 pts)

**Objectif pedagogique** : ecrire un programme *sniff-and-spoof* avec
Scapy qui remplace chaque caractere tape par une lettre fixe, en
recalculant correctement les sommes de controle.
**Flag** : `chksum` (champ a supprimer pour forcer le recalcul).

## Niveau 7 : MITM sur Netcat - Task 3 (4 pts, flag variable)

**Objectif pedagogique** : etendre la technique de sniffing a un second
protocole en clair (Netcat), lire un message intercepte.
**Flag** : contenu de la variable `secret_name` (unique par sandbox),
transmis automatiquement en clair entre A et B toutes les 15 secondes.
Extension non notee : remplacer le mot de code par une sequence de `A`
de meme longueur avant retransmission (fidelite a la Task 3 du sujet
original).

## Anti-triche

Les niveaux 5 et 7 utilisent le mecanisme **APG (reponses variables)** de
CyberRangeCZ Platform (`variables.yml` + `answer_variable_name` +
`variant_answers: true` + `variant_sandboxes: true`) : chaque sandbox
recoit une valeur aleatoire differente pour `motd_secret` et
`secret_name`, rendant le partage de reponses entre etudiants inoperant
pour ces deux niveaux.
