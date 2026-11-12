# TP Securite des Systemes - ARP Cache Poisoning & MITM

Scenario pour la **CyberRangeCZ Platform**, adapte du *SEED Labs "ARP Cache
Poisoning Attack Lab"* (Wenliang Du) et construit sur le meme format que
le jeu `library-junior-hacker`.

## Resume des niveaux

- Introduction (mise en situation)
- Acces au sandbox
- Cartographie du reseau (`nmap` / `arp-scan`)
- ARP Cache Poisoning via **ARP request** (Task 1A)
- ARP Cache Poisoning via **ARP reply** et **gratuitous ARP** (Tasks 1B/1C)
- Attaque **Man-In-The-Middle** complete sur **Telnet**, avec IP forwarding (Task 2)
- Modification du trafic Telnet a la volee avec un script *sniff-and-spoof* (Task 2 suite)
- Attaque **Man-In-The-Middle** sur **Netcat** (Task 3)

Note sur 20 points, penalites d'indice de -0.5 a -2 points selon le niveau.
Duree estimee : environ 30 minutes.

## Topologie

| Hote | Image | Flavor | IP |
|---|---|---|---|
| attacker (M) | seed | m1.medium | 10.0.2.5 |
| client (A) | seed | m1.medium | 10.0.2.6 |
| server (B) | seed | m1.medium | 10.0.2.7 |

Les 3 machines sont sur le **meme segment reseau** (pas de routeur), ce qui
est indispensable pour que l'attaque ARP fonctionne (necessite la meme
couche 2 / le meme domaine de diffusion).

## Anti-triche (reponses variables / APG)

Le fichier `variables.yml` declare deux variables generees aleatoirement
pour chaque sandbox :

- `motd_secret` : texte injecte dans la banniere Telnet de **B**
  (`/etc/issue.net`), visible uniquement par un sniffing reussi pendant
  la session Telnet A<->B (niveau 5).
- `secret_name` : mot de code echange automatiquement entre **A** et
  **B** via Netcat toutes les 15 secondes (niveau 7).

Ces deux flags sont donc **differents pour chaque etudiant/sandbox** :
impossible de recopier la reponse d'un camarade. Pour que ce mecanisme
fonctionne, la training definition doit etre importee avec l'option
**Generate variant sandboxes** activee (champ `variant_sandboxes: true`
deja positionne dans `training.json`), et le pool de sandboxes doit etre
un pool **APG**.

Les autres flags (port telnet, valeur du champ `op` ARP, nom "gratuitous",
nom du champ `chksum`) sont volontairement des faits techniques/protocolaires
identiques pour tous : ils ne sont pas sensibles a la triche et servent de
verification de comprehension, comme dans le scenario `library-junior-hacker`
original.

## Deploiement

1. Importer ce depot comme **Sandbox Definition** dans CyberRangeCZ Platform.
2. Creer un **pool APG** avec cette definition (le fichier `variables.yml`
   sera automatiquement pris en compte).
3. Importer `training.json` comme **Training Definition** (lineaire).
4. Creer une instance de training, lui assigner le pool, et lancer.

## Licence

- Le code (topologie, Ansible, scripts Python) est sous licence MIT.
- Le scenario pedagogique (`training.json`, `game_design.md`) est sous
  licence Creative Commons Attribution 4.0 (CC BY 4.0).
- Le contenu technique du TP est adapte de : **SEED Labs - ARP Cache
  Poisoning Attack Lab**, Copyright (c) 2019 Wenliang Du. Usage gratuit
  pour un usage pedagogique non commercial uniquement (voir `ATTRIBUTION.txt`).
- La structure du depot (topology.yml / provisioning / training.json)
  s'inspire du scenario `library-junior-hacker` (MUNI, CC BY 4.0).
