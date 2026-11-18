# Synthèse des entretiens ASSUREURS : relation commerçants / assureur et parcours post-sinistre (émeutes)

> **Données fictives** : les 20 entretiens sont synthétiques (hackathon Sérévance Assurances). Cette synthèse est descriptive : elle rapporte ce que disent les interviewés, ne tranche aucune décision produit et ne mélange pas les assureurs avec les 50 commerçants (analysés à part). Tous les comptages sont « X/20 assureurs » (qualitatif, non statistique).

## Méthode
- Corpus : **20 entretiens assureurs** (`knowledge/uxr/inputs/txt/assureurs__*.txt`), lus intégralement. Entretiens de 40 à 58 min, réalisés du 02/11 au 13/11/2026.
- Grille : grille d'analyse VALIDÉE le 2026-11-18 (`knowledge/uxr/outputs/grille-analyse.md`), axes communs (pain points, besoins, motivations, freins, contexte, verbatims) + axes assureurs (rôle, qualité des déclarations et critères de tri, délais réels et causes d'allongement, visibilité du statut côté client, lignes rouges).
- Date de la synthèse : 2026-11-18.
- Lecture des comptages : « X/20 » = nombre d'entretiens où le point est explicitement évoqué. L'absence de mention n'est pas un désaccord. Les noms de fichiers sont abrégés dans les listes de comptage (ex. « 01 » = `assureurs__Assureur_01_Claire_Bonnet.txt`) ; chaque verbatim cite le fichier complet.
- Limite de contexte : les assureurs parlent des commerçants par leur propre prisme ; la parole des commerçants n'est pas dans ce livrable.

### Les 20 fichiers
01 `assureurs__Assureur_01_Claire_Bonnet.txt` · 02 `assureurs__Assureur_02_Mathieu_Garnier.txt` · 03 `assureurs__Assureur_03_Nathalie_Perrot.txt` · 04 `assureurs__Assureur_04_Gerard_Lefevre.txt` · 05 `assureurs__Assureur_05_Sabrina_Haddad.txt` · 06 `assureurs__Assureur_06_Julien_Marchand.txt` · 07 `assureurs__Assureur_07_Eric_Vasseur.txt` · 08 `assureurs__Assureur_08_Amandine_Rousseau.txt` · 09 `assureurs__Assureur_09_Frederic_Colin.txt` · 10 `assureurs__Assureur_10_Karine_Dubois.txt` · 11 `assureurs__Assureur_11_Patrice_Meunier.txt` · 12 `assureurs__Assureur_12_Bertrand_Hoarau.txt` · 13 `assureurs__Assureur_13_Isabelle_Caron.txt` · 14 `assureurs__Assureur_14_Olivier_Hamelin.txt` · 15 `assureurs__Assureur_15_Laurence_Giraud.txt` · 16 `assureurs__Assureur_16_Herve_Dumont.txt` · 17 `assureurs__Assureur_17_Elodie_Fontaine.txt` · 18 `assureurs__Assureur_18_Antoine_Delage.txt` · 19 `assureurs__Assureur_19_Sandrine_Lacour.txt` · 20 `assureurs__Assureur_20_Vincent_Moreau.txt`

---

## (a) Tableau des rôles (20/20)

| Rôle | Entretiens | N | Périmètre et angle propre | Verbatim de cadrage |
|---|---|---|---|---|
| Gestionnaire sinistres | 01 Bonnet (senior entreprises, Lille), 02 Garnier (renfort cellule de crise, particuliers à l'origine, Nantes), 03 Perrot (responsable d'équipe, 8 gestionnaires, Lyon), 04 Lefèvre (grands comptes, Paris), 05 Haddad (professionnels, Bordeaux), 06 Marchand (spécialiste perte d'exploitation, Paris) | 6 | Instruction du dossier de la déclaration à l'indemnisation ; répartition, arbitrage ; pertes d'exploitation. 04 se dit hors cible : commerçants « je les croise peu ». | « Je traite environ 120 dossiers en portefeuille actif, de la déclaration à l'indemnisation. » — `assureurs__Assureur_01_Claire_Bonnet.txt` |
| Expert | 07 Vasseur (bâtiment, cabinet partenaire), 08 Rousseau (pertes d'exploitation / comptabilité, cabinet partenaire), 09 Colin (véhicules, matériels, stocks, cabinet partenaire), 10 Dubois (expertise à distance, pôle interne Sérévance) | 4 | Constat, chiffrage, rapport ; 3 sur 4 sont des cabinets partenaires, 1 est interne et à distance. | « Mon rôle est de constater, chiffrer, et conseiller sur les mesures conservatoires. » — `assureurs__Assureur_07_Eric_Vasseur.txt` |
| Agent / courtier | 11 Meunier (agent général, Roubaix, ~700 clients pro), 12 Hoarau (agent général familial, Marseille), 13 Caron (courtière CHR, Lille, Sérévance ≈ 40 % du portefeuille), 14 Hamelin (courtier en ligne, ~1 500 contrats dont 300 Sérévance) | 4 | Premier interlocuteur du commerçant, déclare et accompagne, « pont » vers la gestion sinistres. | « Je suis le visage de Sérévance dans mon quartier. » — `assureurs__Assureur_11_Patrice_Meunier.txt` |
| Cellule de crise | 15 Giraud (direction de la cellule émeutes, ~60 personnes), 16 Dumont (responsable régional Nord, volet terrain) | 2 | Pilotage de la crise, règles de priorité, mobilisation des experts, liaison avec les agents. | « J'ai coordonné une soixantaine de personnes : gestionnaires, experts, juristes, communication. » — `assureurs__Assureur_15_Laurence_Giraud.txt` |
| Digital / produit | 17 Fontaine (expérience client digitale sinistres), 18 Delage (responsable produit assurance commerçants) | 2 | 17 : espace client, formulaire, notifications, chat. 18 : garanties, franchises, tarifs ; se dit sur « des sujets un peu plus structurants que la mise en relation ». | « J'ai en charge l'espace client, le formulaire de déclaration, les notifications et le chat. » — `assureurs__Assureur_17_Elodie_Fontaine.txt` |
| Conformité / fraude | 19 Lacour (lutte anti-fraude sinistres, équipe de 6), 20 Moreau (juriste conformité et protection des données) | 2 | 19 : détection des dossiers suspects. 20 : validation des parcours, formulaires, RGPD, médiation. | « Je suis le référent RGPD pour les sinistres. » — `assureurs__Assureur_20_Vincent_Moreau.txt` |

---

## Thèmes (du plus partagé au plus marginal)

### 1. Des déclarations inégales, souvent incomplètes, en champ libre : les infos clés (situation, gravité, activité, salariés) manquent — 16/20
Fichiers concernés : 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 13, 14, 15, 16, 17, 19. (11 et 12, agents, disent que leurs propres déclarations sont complètes parce qu'ils les préparent ; 18 « pas mon sujet » ; 20 ne décrit pas de manque.)

**Constat :** Les assureurs décrivent des déclarations hétérogènes dont le contenu ne permet ni de trier ni d'instruire sans rappeler le commerçant. Mesures citées : environ un tiers de dossiers incomplets (01, 03), moins d'un dossier sur deux avec les pièces complètes côté expert (07), 20 % seulement avec état de stock exportable (09), la moitié sans la situation du commerçant fermé/ouvert (16). Le champ libre de description des dégâts est identifié comme cause du tri impossible (17, 19).

**Infos manquantes les plus citées (comptage sur les 20 entretiens) :**

| Information manquante ou demandée | N | Fichiers |
|---|---|---|
| Situation / gravité (fermé ou ouvert, arrêt total/partiel, date de fermeture et de réouverture) | 9 | 02, 05, 06, 07, 08, 14, 15, 16, 17 |
| Pièces et justificatifs (liste du stock, photos exploitables, plainte, devis, K-bis, liste des salariés) | 8 | 01, 03, 07, 09, 10, 13, 17, 19 |
| Nombre de salariés | 4 | 02, 05, 13, 17 |
| Activité réelle du commerçant | 3 | 02, 05, 17 |
| Coordonnées joignables / joignabilité | 3 | 07, 10, 17 |
| Données de perte d'exploitation (chiffre d'affaires moyen, charges fixes) | 2 | 06, 08 |
| Montant estimé fiable | 2 | 01, 06 |
| Marchandise nettoyée ou conservée avant nettoyage | 1 | 09 |

**Verbatims :**
- « Environ un tiers étaient incomplètes : pas de dépôt de plainte, pas de liste du stock, pas de photos. Et le montant estimé est souvent un chiffre au hasard. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Ce qui manque le plus dans une déclaration : l'activité réelle du commerçant. Une 'boutique' peut être un tabac, une pharmacie ou une friterie, et les garanties changent. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Les informations les plus utiles : l'activité, la situation (ouvert/fermé), le nombre de salariés et la nature du dommage. Ce que je demandais systématiquement par téléphone parce que ce n'était pas dans le formulaire. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Le formulaire actuel est en champ libre pour la description des dégâts, ce qui rend le tri impossible. On a identifié 8 champs qui feraient la différence : activité, situation, nombre de salariés, nature du dommage, estimation, pièces, urgence, joignabilité. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`
- « Pour la qualité des déclarations, la moitié manquait de la situation du commerçant (fermé ou non). » — `assureurs__Assureur_16_Herve_Dumont.txt`
- « Un bon dossier a un état de stock exportable, des photos avant nettoyage, et les factures d'achat. Seuls 20 % l'avaient. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- Contre-point côté agent : « Quand je déclare, j'ai les informations : l'activité, le contrat, les garanties, la gravité. Mon dossier est propre. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- Qualité jugée très faible (perception d'un gestionnaire senior, 04) : « Les gens écrivent 'tout est cassé', sans une ligne de détail. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`

**Implication :** les champs manquants nommés par les assureurs sont convergents (situation/gravité en tête, pièces ensuite). Le fait qu'ils soient jugés « simples à ajouter » (06, 08, 09, 14) est rapporté tel quel ; l'arbitrage sur le contenu du formulaire reste à l'équipe.

---

### 2. Des délais allongés en crise, avec le manque d'experts comme goulot principal — 16/20 donnent des chiffres
Fichiers avec chiffres : 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16. Voir section (b) pour le détail chiffré.

**Constat :** Sur les émeutes, l'expert arrive entre J+3 (visio) et J+25 selon la gravité et la zone, bien au-delà du « normal » de 4 jours cité. Les causes d'allongement les plus citées : manque d'experts (01, 02, 03, 05, 12, 15), pièces manquantes et allers-retours avec le commerçant (01, 02, 08, 19), et rapport d'expert qui attend sa validation (07, 08, 09).

**Verbatims :**
- « Normalement, expert sous 4 jours. En crise, 10 jours en moyenne, jusqu'à 25 pour les plus compliqués. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Objectif : expert sous 5 jours pour les priorités A, 10 pour B, 15 pour C. Résultat réel : A à 8 jours, B à 12, C à 20. On a manqué d'experts : 25 mobilisés pour un besoin de 60. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Le principal goulot, ce sont les experts : on en avait 25 mobilisés pour 1 000 dossiers nécessitant une visite. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « J'ai vu des dossiers où mon rapport dormait 10 jours avant d'être validé. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- « Un expert sous 10 jours, c'est très bien. Les commerçants veulent tout, tout de suite, c'est humain mais irréaliste. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`
- « Les délais de la compagnie sont mauvais, c'est connu. Un expert à 15 jours, c'est inacceptable. » — `assureurs__Assureur_12_Bertrand_Hoarau.txt`

**Implication :** les assureurs ne sont pas d'accord sur le caractère acceptable des délais (04 vs 12, 13, 15). Les causes sont à la fois en amont (qualification, pièces) et en aval (planning experts, validation), pas uniquement dans le formulaire.

---

### 3. Le tri / la priorisation reposent sur des règles informelles, orales ou personnelles, sans appui dans l'outil — 15/20
Fichiers concernés : 01, 02, 03, 04, 05, 07, 08, 10, 11, 12, 13, 15, 16, 17, 19. Voir section (c) pour le détail des règles et des biais.

**Constat :** Il n'existe pas de règle de tri inscrite dans l'outil. Les règles déclarées sont soit un critère de montant (01, 04), soit une grille A/B/C (fermé avec salariés / dommage important mais ouvert / petits dommages) transmise oralement (03), construite individuellement (05) ou qualifiée à la main (15). Les dossiers étaient aussi distribués par zone géographique (07, 16) ou par réseau personnel (11, 12).

**Verbatims :**
- « Le tri s'est fait en trois niveaux : A, les commerçants fermés avec salariés ou avec dommage structurel ; B, les dommages matériels importants mais activité maintenue ; C, les petits dommages. C'était une règle orale, pas dans l'outil. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « J'ai classé mentalement : urgence A (fermé, salariés), B (ouvert, dommage important), C (le reste). Mais c'est une règle personnelle, que mes collègues n'utilisaient pas forcément. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Pour les appliquer, il fallait que les gestionnaires qualifient chaque dossier à la main. Environ 40 % ont été qualifiés dans les 5 premiers jours. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Pour le tri, je ne savais pas quels critères appliquer, on m'a dit 'les plus gros d'abord', mais sans définition de 'gros'. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Pour le tri, on m'envoyait les dossiers par zones, pas par gravité. » — `assureurs__Assureur_07_Eric_Vasseur.txt`
- « Une règle de tri écrite et dans l'outil, pas seulement dans ma tête. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`

**Implication :** la qualification de la gravité est aujourd'hui un travail manuel et variable d'un gestionnaire à l'autre.

---

### 4. Le commerçant n'a pas de visibilité sur son dossier : statut « en cours », pas de dates, pas de nouvelles — 13/20
Fichiers concernés : 01, 02, 03, 05, 07, 09, 11, 13, 14, 15, 16, 17, 20. Voir section (d).

**Constat :** Le statut visible est générique et ne dit rien de la suite. Le premier motif de réclamation est « aucune nouvelle » (03). Les professionnels en contact avec le commerçant (experts, agents, courtiers, gestionnaires) disent ne pas pouvoir répondre à « où en est mon dossier » ou « quand serai-je payé ».

**Verbatims :**
- « Pour le client, il n'y a aucune visibilité : il ne voit que le statut 'en cours'. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « 60 % de mes appels sont des demandes de nouvelles. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Le motif numéro un : 'je n'ai aucune nouvelle'. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « Je ne vois pas l'avancement des dossiers que j'ai ouverts. J'appelle la ligne agents, qui me répond 'en cours'. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « Je constate que les commerçants me demandent presque tous 'quand est-ce que je serai payé ?' et je ne peux pas répondre. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- « Notre NPS digital sinistres est de 18, contre 45 pour la souscription. Ça dit tout : le sinistre est notre point faible. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`

**Implication :** le déficit de visibilité est cité à tous les niveaux de la chaîne, y compris par ceux qui n'ont eux-mêmes pas accès à l'information (agents, experts, équipe digitale).

---

### 5. Une satisfaction mal mesurée, liée à la fréquence et à la proactivité du contact plutôt qu'au résultat — 12/20
Fichiers concernés : pas d'indicateur systématique : 01, 02, 06, 09, 19 (5) ; indicateurs chiffrés cités : 03, 04, 10, 14, 15, 17, 20 (7).

**Constat :** Les indicateurs existent de façon dispersée et divergent : 80 % de satisfaction globale (04), 85 % pour les visios (10), 6,1/10 sur 800 questionnaires envoyés avec 30 % de réponses (15), NPS digital sinistres 18 vs 45 en souscription (17), note courtier 3,2/5 vs 4,1 pour un concurrent avec suivi SMS (14), 140 réclamations en un mois vs une vingtaine d'habitude (03), environ 30 dossiers de médiation par an sur le segment (20). Les motifs d'insatisfaction convergent : absence d'information, pièces redondantes, difficulté à joindre quelqu'un (03, 14, 15, 17).

**Verbatims :**
- « Je pense que la satisfaction est liée à la fréquence des contacts, pas au résultat. Un dossier indemnisé en 60 jours avec 3 appels est mieux perçu qu'un dossier en 30 jours sans nouvelle. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Le score de satisfaction globale est de 6,1 sur 10. Les verbatims se concentrent sur : l'absence d'information, les demandes de pièces redondantes, la difficulté à joindre quelqu'un. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Je n'ai aucun indicateur de satisfaction. Ce que je voyais, c'était le ton au téléphone : de plus en plus tendu au fil des jours. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « On a un taux de satisfaction global très correct, autour de 80 %. Les commerçants qui râlent, ce sont toujours les mêmes. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`
- « Les retours sont très bons : 85 % de satisfaction sur nos visios, d'après le questionnaire envoyé après chaque expertise. » — `assureurs__Assureur_10_Karine_Dubois.txt`
- « Je pense que le paiement est le moment de vérité. Plus il est rapide et clair, meilleur est le ressenti. » — `assureurs__Assureur_16_Herve_Dumont.txt`

**Implication :** les chiffres ne sont pas comparables entre eux (périmètres, échelles, populations différents) et ne sont pas consolidés ; 04 et 15 jugent la relation « correcte » (80 %, NPS « corrects ») quand 17 donne un NPS sinistres de 18.

---

### 6. L'avance (sans attendre le rapport) existe mais est peu connue et souvent conditionnée au rapport — 10/20
Fichiers concernés : 01, 03, 05, 06, 07, 08, 09, 10, 13, 15 (16 évoque le paiement sans parler d'avance).

**Constat :** Plusieurs dispositifs existent : avance sans expertise jusqu'à 5 000 euros (01, 15), avance forfaitaire pertes d'exploitation jusqu'à 3 mois de chiffre d'affaires moyen (06), avance quasi immédiate sur circuit visio (10), avance sous 10 jours en niveau A (03). Deux entretiens indiquent un défaut d'information : sur les collègues (01) et sur les commerçants (06). Deux experts relèvent que l'avance dépend du rapport (07, 08, 09).

**Verbatims :**
- « L'avance, nous pouvons la débloquer sans expertise jusqu'à 5 000 euros, mais beaucoup de collègues ne le savaient pas. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Beaucoup de commerçants ne savaient pas que cette avance existait. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Une avance peut être décidée beaucoup plus tôt, sur des éléments simples. Malheureusement, elle est souvent conditionnée à mon rapport, ce qui est trop long. » — `assureurs__Assureur_08_Amandine_Rousseau.txt`
- « Un rapport tardif retarde l'avance. » — `assureurs__Assureur_07_Eric_Vasseur.txt`
- « Les avances que j'ai pu accorder avant expertise : 12 cas, surtout pour des commerçants dont les salariés étaient sans paie. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`

**Implication :** point de tension rapporté sans le trancher : 09 propose qu'un rapport déclenche l'avance automatiquement ; 08 veut dissocier l'avance du rapport complet mais refuse de « généraliser des forfaits sans vérification ».

---

### 7. Les agents et courtiers sont le relais de proximité du commerçant, mais n'ont ni canal prioritaire ni visibilité — 9/20
Fichiers concernés : 01, 03, 11, 12, 13, 14, 15, 16, 17.

**Constat :** Pour le commerçant, le « visage » de Sérévance est son agent ou courtier (01, 11, 13, 16, 17). Les agents et courtiers déclarent, relancent, et ne voient pas l'avancement (11, 13, 14). Quatre entretiens (11, 12, 13, 16) expriment la crainte d'être contournés par un circuit direct commerçant-assureur.

**Verbatims :**
- « Pour eux, le visage de Sérévance, c'est leur agent ou notre ligne sinistres, très rarement nous. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Mon dossier est traité comme celui qui est arrivé via la ligne sinistres. J'aurais voulu pouvoir indiquer 'priorité A, fermé, 5 salariés'. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « Je sers de pont. » — `assureurs__Assureur_13_Isabelle_Caron.txt`
- « Sans les agents, on n'aurait pas pu traiter. » — `assureurs__Assureur_16_Herve_Dumont.txt`
- « Je voudrais une API ou un export automatique, pour synchroniser mes dossiers avec les statuts de Sérévance, et informer mes clients par SMS. » — `assureurs__Assureur_14_Olivier_Hamelin.txt`
- Position défensive : « C'est ce qu'un bon agent fait, il défend ses clients. Votre système, il va nous retirer ce pouvoir. » — `assureurs__Assureur_12_Bertrand_Hoarau.txt`

**Implication :** la priorité des dossiers d'agents repose aujourd'hui sur les contacts personnels (11, 12), « pas structurel » (11) ; ce biais est documenté en (c).

---

### 8. Garder le jugement humain : pas de décision automatique sur la priorité, le calcul ou l'indemnisation — 9/20
Fichiers concernés : 01, 02, 06, 07, 08, 10, 15, 19, 20.

**Constat :** Les assureurs acceptent une aide à la structuration mais posent des limites à l'automatisation : priorité décidée par l'humain (01, 02, 15), calcul de perte d'exploitation non présenté comme définitif (06), pas de forfait sans vérification (08), pas de décision d'indemnisation automatique (19, 20), pas d'expertise à distance imposée ni sur dommage structurel (07, 10).

**Verbatims :**
- « Ce que j'ai besoin de garder : la capacité de décider de la priorité, de poser des questions, de faire confiance à mon jugement. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Je ne voudrais pas qu'une IA décide seule de la priorité, parce qu'un commerçant qui a perdu un camion aura peut-être déclaré peu. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Mes lignes rouges : un traitement automatique d'une décision d'indemnisation sans intervention humaine. » — `assureurs__Assureur_19_Sandrine_Lacour.txt`
- « Un tri qui produit un effet significatif pour le commerçant, comme retarder une indemnisation, doit pouvoir être expliqué et contesté. Il faut une intervention humaine. » — `assureurs__Assureur_20_Vincent_Moreau.txt`
- « Ce que je ne voudrais pas : qu'un outil calcule automatiquement la perte et la présente comme définitive. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Ce que je refuse : une expertise uniquement à distance pour les dommages structurels, parce qu'on rate des choses. » — `assureurs__Assureur_07_Eric_Vasseur.txt`

**Implication :** 15 formule la position la plus précise rapportée : prioriser « automatiquement en première lecture avec validation humaine ». Aucun entretien ne demande une automatisation sans validation.

---

### 9. Ressaisies, pièces redemandées et doublons : le commerçant et les agents répètent — 8/20
Fichiers concernés : 02, 03, 11, 13, 14, 15, 17, 19.

**Constat :** Le même dossier est ouvert par plusieurs canaux, repris par plusieurs gestionnaires, ou nécessite une double saisie côté courtier. Les pièces sont redemandées. Le commerçant « recommence tout ».

**Verbatims :**
- « Certains commerçants me disaient 'vous êtes le troisième à m'appeler, je recommence tout'. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Le motif numéro deux : 'on me demande les mêmes pièces plusieurs fois'. Ça m'a convaincue qu'un portail unique de pièces est nécessaire. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « Côté Sérévance, il fallait ressaisir dans leur portail, donc double saisie. » — `assureurs__Assureur_14_Olivier_Hamelin.txt`
- « Ce qui frotte : quand le siège me demande des pièces que le commerçant a déjà envoyées. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « Ce qui allonge, c'est le manque de pièces, les doubles saisies, et les dossiers ouverts par plusieurs canaux. Un identifiant unique de dossier réduirait les doublons de moitié. » — `assureurs__Assureur_19_Sandrine_Lacour.txt`

**Implication :** 13 note aussi que le portail courtiers ne permet pas de joindre un gros fichier de pièces et qu'il n'y a pas de numéro de dossier unique par sinistre (`assureurs__Assureur_13_Isabelle_Caron.txt`).

---

### 10. Prudence sur l'engagement de délais : une fourchette plutôt qu'une promesse — 8/20
Fichiers concernés : 01, 02, 03, 05, 15, 17, 18, 20. Voir section (e).

**Constat :** Aucun assureur ne soutient une promesse ferme. Deux positions coexistent : 18 voit dans l'affichage de délais un risque juridique à éviter ; 03, 15, 17, 20 (et 13, 14 côté courtiers) acceptent ou demandent une fourchette indicative avec conditions.

**Verbatims :**
- « Mes lignes rouges : qu'un outil envoie automatiquement des promesses de délai que je ne pourrai pas tenir. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Mieux vaut une fourchette honnête. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « Il faut un délai fourchette, avec des conditions. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Les délais, ce sont des promesses commerciales dangereuses. Si on affiche un délai, on s'expose à des litiges. » — `assureurs__Assureur_18_Antoine_Delage.txt`
- « On peut afficher des délais prévisionnels, à condition qu'ils soient présentés comme indicatifs, avec des conditions. » — `assureurs__Assureur_20_Vincent_Moreau.txt`
- « Les gestionnaires hésitent à s'engager. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`

**Implication :** 17 note qu'elle n'a pas la donnée sur les délais d'expertise dans ses outils pour afficher une fourchette.

---

### 11. Des outils de gestion qui ne portent ni la priorité, ni la vue d'ensemble, ni les statuts — 7/20
Fichiers concernés : 01, 02, 03, 05, 15, 16, 17.

**Constat :** L'outil de gestion sinistres ne permet pas de qualifier ou trier facilement, n'expose pas les statuts en temps réel et laisse des notes parfois inexistantes. Les gestionnaires ont compensé avec des tableaux Excel personnels et un tableau de bord alimenté à la main.

**Verbatims :**
- « Ce qui m'a aidée : un tableau Excel personnel avec les priorités. Ce qui m'a gênée : aucune vue d'ensemble dans l'outil. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Ensuite, on a mis en place un tableau de bord, mais il était alimenté à la main. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Mes freins : la dépendance à l'outil de gestion sinistres, très ancien, qui n'expose pas les statuts en temps réel. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`
- « Les notes dans l'outil étaient parfois inexistantes. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Ce qui m'a manqué : une vue consolidée des dossiers par zone, avec leur gravité. » — `assureurs__Assureur_16_Herve_Dumont.txt`

**Implication :** les contraintes techniques (dépendance au SI existant) sont signalées par 17 seulement ; les autres décrivent le manque d'outil sans traiter la faisabilité. Faisabilité technique : non couvert par les entretiens.

---

### 12. Fraude, conformité et données : exigences posées dès la conception — 6/20
Fichiers concernés : 01, 03, 15, 18, 19, 20. (09 et 10 évoquent la suspicion de façon ponctuelle.) Voir section (e).

**Constat :** La lutte anti-fraude demande des données structurées, un identifiant unique, la traçabilité et l'horodatage des photos ; la conformité demande le consentement, la minimisation des données, un hébergement en Europe, la traçabilité des décisions et un droit d'accès. En crise, un contrôle allégé a été appliqué sous 5 000 euros (19). La collecte via WhatsApp ou mail par les gestionnaires est un point de risque (20). Les deux profils précisent que la fraude ne doit pas ralentir les commerçants honnêtes (19) et que cela « ne bloque pas le projet » (20).

**Verbatims :**
- « Les déclarations structurées nous aident énormément : on repère les incohérences, les doublons, les montants atypiques. Un champ libre est inutilisable. » — `assureurs__Assureur_19_Sandrine_Lacour.txt`
- « La lutte anti-fraude doit venir après la priorité de gravité : on ne doit pas retarder un commerçant fermé parce qu'on soupçonne un dossier voisin. » — `assureurs__Assureur_19_Sandrine_Lacour.txt`
- « La collecte de photos et de pièces par des canaux non sécurisés comme WhatsApp ou mail, que les gestionnaires ont utilisés par pragmatisme. » — `assureurs__Assureur_20_Vincent_Moreau.txt`
- « Mes contraintes : la fraude, la conformité RGPD, et la responsabilité. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Je ne vois pas d'obstacle majeur, si c'est conçu avec nous dès le départ. » — `assureurs__Assureur_20_Vincent_Moreau.txt`

**Implication :** voir section (e) pour les lignes rouges chiffrées.

---

### 13. Le commerçant est mal préparé à la déclaration et au contrat (pédagogie avant le sinistre, pièces non conservées) — 5/20
Fichiers concernés : 04, 06, 08, 09, 18.

**Constat :** Les assureurs constatent une méconnaissance des garanties, de la perte d'exploitation (indemnisation de la marge brute, avec franchises), des obligations de preuve et de comptabilité. Les registres diffèrent : 06, 08 et 09 décrivent un besoin de pédagogie et d'accompagnement ; 04 et 18 formulent un jugement plus sévère sur les commerçants.

**Verbatims :**
- « Le plus gros problème, c'est qu'ils découvrent ça après le sinistre. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Les commerçants qui ont un comptable réactif sont mieux indemnisés et plus vite. Ça crée une inégalité. Les plus petits, sans comptable, sont pénalisés. » — `assureurs__Assureur_08_Amandine_Rousseau.txt`
- « Les commerçants sont souvent honnêtes, mais l'inventaire est rarement fiable. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- « Le travail pédagogique avant le sinistre n'est pas fait, et nous, on le paie en réclamations. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`
- « Ils achètent un contrat de base et s'étonnent après. » — `assureurs__Assureur_18_Antoine_Delage.txt`

**Implication :** le périmètre « avant sinistre » est signalé comme un sujet en amont du parcours étudié.

---

### 14. Les pertes d'exploitation : un sous-parcours technique avec des besoins de données propres — 4/20 (06, 08 centraux ; 01, 18 en mention)
**Constat :** Sur 3 400 dossiers, environ 900 comportaient une demande de perte d'exploitation (06). Le délai normal est de 60 à 90 jours (06) ; l'expert comptable attend 3 à 5 semaines pour un rapport complet (08). Les données utiles : arrêt total ou partiel, durée estimée (06) ; date de fermeture, date de réouverture, charges fixes, chiffre d'affaires moyen (08).

**Verbatims :**
- « Sur les émeutes, mon activité a explosé : sur 3 400 dossiers, environ 900 avaient une demande de perte d'exploitation. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Ce sont quatre champs simples qui me permettraient de proposer une avance en 48 heures. » — `assureurs__Assureur_08_Amandine_Rousseau.txt`
- « Je suis intervenue assez tard dans le processus, parfois à J+30, alors qu'on aurait pu m'impliquer plus tôt pour cadrer l'avance. » — `assureurs__Assureur_08_Amandine_Rousseau.txt`

**Implication :** les attentes sur ce sous-parcours (3 questions chez 06, 4 champs chez 08) sont décrites en section (f).

---

### 15. L'expertise à distance (visio, photos) : rapide et bien perçue pour les petits dommages, avec des limites — 4/20
Fichiers concernés : 03, 07, 10, 15.

**Constat :** Visio à J+3, rapport sous 24 h, avance quasi immédiate si dossier conforme (10). Utilisée pour les dossiers C pendant la crise (03, 10) et étendue par la cellule (15). Limites posées : pas pour les dommages structurels (07, 10), non imposée à un commerçant mal à l'aise (10), réseau mauvais ou détresse (10).

**Verbatims :**
- « Visio à J+3 en moyenne, rapport sous 24h, avance quasi immédiate si le dossier est conforme. C'est l'un des circuits les plus rapides de la compagnie. » — `assureurs__Assureur_10_Karine_Dubois.txt`
- « L'expertise à distance, nous l'avons utilisée pour les dossiers C, et ça a marché. » — `assureurs__Assureur_03_Nathalie_Perrot.txt`
- « Pour les petits dommages, je pense qu'une expertise sur photos est suffisante, et ça libérerait du temps pour les dossiers lourds. » — `assureurs__Assureur_07_Eric_Vasseur.txt`
- « Il faut proposer, pas obliger. » — `assureurs__Assureur_10_Karine_Dubois.txt`

**Implication :** critères d'éligibilité actuels de la visio : montant estimé inférieur à 15 000 euros, pas de dommage structurel, pas de suspicion (10).

---

### 16. Scepticisme et résistances au projet — 3/20
Fichiers concernés : 04, 12, 18.

**Constat :** Trois interviewés sont réservés, voire hostiles, au projet, pour des raisons différentes : lassitude des « nouveaux outils » (04), perte de pouvoir et de commissions de l'agent (12), exigence d'un business case (18). Les trois se déclarent aussi peu concernés par le sujet. Leurs propos sont rapportés tels quels pour documenter les freins d'adhésion interne.

**Verbatims :**
- « Chaque année on lance un outil qui devait révolutionner la relation client, et on retombe sur nos pieds. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`
- « Mes lignes rouges : qu'on me court-circuite, qu'on mette mes clients en contact direct avec le siège, et qu'on me retire des commissions au profit d'une plateforme. » — `assureurs__Assureur_12_Bertrand_Hoarau.txt`
- « Si vous me dites qu'une plateforme réduit les coûts de gestion de 15 %, je vous écoute. Sinon, c'est un projet de communication. » — `assureurs__Assureur_18_Antoine_Delage.txt`

**Implication :** les coûts de gestion et le business case ne sont chiffrés par aucun entretien : non couvert par les entretiens.

---

## (b) Volumes et délais réels côté assureur ; causes d'allongement

**Volumes (tels que déclarés ; valeurs fictives, parfois non cohérentes d'un entretien à l'autre) :**

| Indicateur | Valeur déclarée | Source |
|---|---|---|
| Déclarations émeutes | ~3 000 en 2 semaines (vs ~100 habituellement sur le segment) | 01 |
| | 3 400 sur 12 jours ; 600 dans les 48 premières heures | 03, 06, 15 |
| Dossiers avec perte d'exploitation | ~900 sur 3 400 | 06 |
| Dossiers nécessitant une visite | ~1 000 pour 25 experts mobilisés (besoin : 60 experts) | 03, 15 |
| Région Nord | 520 sinistres, 12 experts dont 5 externes | 16 |
| Part du formulaire en ligne | 55 % des déclarations | 17 |
| Espace client commerçants créé | 35 % | 17 |
| Visios | ~600 en 12 jours (vs ~30 par semaine) | 10 |
| Charge individuelle gestionnaire | ~120 dossiers en portefeuille, 40 en parallèle (01) ; 70 nouveaux dossiers en une semaine, portefeuille ~90 (05) ; 60 dossiers repris sans historique (02) | 01, 02, 05 |
| Charge expert | 4 expertises/jour normal, 6 à 8 en crise (07) ; ~60 visites en 3 semaines, 1 h 30 en moyenne (09) | 07, 09 |
| Agents / courtiers | 85 appels en 2 jours, ~50 déclarations remplies à la place des commerçants, ~15 visites (11) ; 40 sinistres en une semaine (12) ; 60 clients sinistrés dont 25 chez Sérévance (13) ; 140 demandes en 3 jours dont 40 Sérévance (14) | 11, 12, 13, 14 |
| Réclamations | 140 en un mois (vs ~20 habituellement) ; ~30 dossiers de médiation par an sur le segment | 03, 20 |
| Fraude | 3 à 4 % d'alertes en temps normal ; en crise ~4 %, soit une centaine, dont une dizaine confirmés douteux | 19 |
| Appels « demandes de nouvelles » | 60 % des appels d'une gestionnaire | 01 |
| Attente ligne sinistres | jusqu'à 40 minutes | 01 |

**Délais réels étape par étape :**

| Étape | Valeur déclarée | Source |
|---|---|---|
| Déclaration → appel du gestionnaire | 2 à 3 jours | 05 |
| Premier appel → décision d'expertise | 3 jours | 02 |
| Déclaration → mission d'expert | parfois 7 jours ; mission à J+5 | 07, 09 |
| Mission → visite | 3 à 5 jours ; visite à J+8 | 07, 09 |
| Expert (normal) | sous 4 jours | 01 |
| Expert (crise, moyenne) | 10 jours, jusqu'à 25 (01) ; 8 à 12 jours à Bordeaux (05) ; 9 jours région Nord, 15 pour les mal classés (16) ; J+5 à J+20 (11) ; J+7 à J+15 (13) ; J+10 (14) ; 15 jours (12) | 01, 05, 11, 12, 13, 14, 16 |
| Expert : objectif vs réel (cellule) | A 5 j / B 10 j / C 15 j (objectif) ; A 8 j / B 12 j / C 20 j (réel) | 15 |
| Expert : niveaux (gestionnaire) | A sous 5 j, B 10 j, C 15 j, « on n'a pas toujours tenu » | 03 |
| Expertise à distance | visio J+3 ; rapport sous 24 h | 10 |
| Rapport d'expert | sous 48 h (07) ; sous 3 jours (09) ; 3 à 5 semaines pour perte d'exploitation (08) | 07, 08, 09 |
| Validation du rapport | « dormait 10 jours » | 09 |
| Avance | niveau A sous 10 j (03) ; quasi immédiate en visio (10) ; sans expertise jusqu'à 5 000 € (01, 15) ; forfaitaire perte d'exploitation jusqu'à 3 mois (06) | 01, 03, 06, 10, 15 |
| Examen fraude (alerte) | 3 à 5 jours | 19 |
| Indemnisation | 30 à 90 jours (11) ; J+35 à J+80 (13) ; J+45 (14) ; 70 % des dossiers clos en moins de 60 jours (15) ; perte d'exploitation normale 60 à 90 jours (06) | 06, 11, 13, 14, 15 |

**Causes d'allongement citées :**

| Cause | N | Fichiers |
|---|---|---|
| Manque d'experts / planning experts | 6 | 01, 02, 03, 05, 12, 15 |
| Pièces manquantes, allers-retours, réponse tardive du commerçant, pièces comptables | 5 | 01, 02, 08, 11, 19 |
| Mauvais classement de gravité (commerçants très touchés attendant 15 jours) | 3 | 07, 13, 16 |
| Rapport d'expert non validé / avance conditionnée au rapport | 3 | 07, 08, 09 |
| Doubles saisies, dossiers multi-canaux, doublons | 3 | 13, 14, 19 |
| Reprise de dossiers par plusieurs gestionnaires / dossier sur plusieurs gestionnaires (dommage + vol + PE) | 2 | 02, 03 |
| Saturation des lignes ; renforts non formés au segment | 3 | 01, 02, 12 |
| Qualification manuelle des dossiers (40 % qualifiés en 5 jours) | 1 | 15 |
| Avance non connue des gestionnaires ou des commerçants | 2 | 01, 06 |
| Délai de validation interne entre rapport et décision | 1 | 09 |

**Verbatims :**
- « Ce qui allonge : le manque d'experts, les pièces manquantes, et les allers-retours avec les commerçants. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Entre la déclaration et la mission, parfois 7 jours. Mon rapport est rendu sous 48 heures. » — `assureurs__Assureur_07_Eric_Vasseur.txt`
- « Un gros goulot à Bordeaux : peu d'experts disponibles. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Je savais que certains commerçants, très touchés, attendaient 15 jours parce qu'ils avaient été mal classés. J'ai corrigé à la main, mais ça aurait pu être évité. » — `assureurs__Assureur_16_Herve_Dumont.txt`

Remarque de cohérence : 01 parle de ~3 000 déclarations en deux semaines, 03/06/15 de 3 400 en 12 jours ; 19 indique ~4 % soit « une centaine » de dossiers à examiner. Ces écarts sont conservés tels que déclarés.

---

## (c) Comment le tri / la priorisation est fait aujourd'hui, et qualité des déclarations

**Règles et pratiques déclarées :**

| Pratique de tri | Nature | Fichiers |
|---|---|---|
| Montant estimé et présence d'une garantie perte d'exploitation | Implicite, « brut » | 01 |
| « Les plus gros d'abord » sans définition | Consigne orale | 02 |
| Montant (« 200 000 euros passe avant 3 000 ») | Logique déclarée par un gestionnaire grands comptes | 04 |
| Grille A / B / C (fermé avec salariés ou dommage structurel ; dommage important mais ouvert ; petits dommages) | **Règle orale**, transmise en réunion, appliquée « un peu variable », pas dans l'outil | 03 |
| Grille A / B / C personnelle (fermé+salariés ; ouvert+dommage important ; reste) | **Règle personnelle**, non partagée | 05 |
| Trois catégories de priorité fixées par la cellule de crise | Qualification manuelle (40 % en 5 jours), puis tableau de bord alimenté à la main | 15 |
| Distribution des dossiers par zones géographiques (experts) | Organisation logistique | 07, 16 |
| Carte par quartier classée selon ce que disent les agents au téléphone | Informel | 16 |
| Critères d'éligibilité visio : montant < 15 000 €, pas de dommage structurel, pas de suspicion | Critères d'orientation formels (par le gestionnaire) | 10 |
| Contrôle fraude allégé < 5 000 €, renforcé au-delà | Décision de crise | 19 |
| Priorité via contacts personnels (directeur régional) ou « un peu d'avance » | Informel, non structurel | 11, 12 |
| Durée de fermeture comme critère principal « bien avant le montant des dégâts » | Position d'expert | 08 |
| Critère contractuel (garantie perte d'exploitation) | Position produit | 18 |
| Fraude derrière la gravité | Position anti-fraude | 19 |

**Formel ou implicite ?** Aucune règle de tri n'est dans l'outil (03, 05, 15, 17). Les seules règles explicites sont orales ou personnelles (03, 05) ou ponctuelles de crise (15, 19). 11/20 plaident explicitement pour que la fermeture / la gravité / la situation du commerçant soit le critère de tête (01, 03, 05, 06, 07, 08, 11, 13, 15, 16, 19). Le critère montant est défendu par 04 (et 18 : critère contractuel).

**Biais identifiés par les interviewés :**
- Biais de montant déclaré : « ceux qui déclarent gros passent devant, parfois à tort » (01). À l'inverse, un commerçant avec une perte lourde peut avoir déclaré peu (02).
- Biais de réseau : le traitement plus rapide des clients d'agents via des contacts personnels (11, 12).
- Biais de zone : dossiers expertisés par zone et non par gravité, des commerçants fermés attendant derrière des vitrines fissurées (07).
- Variabilité entre gestionnaires : règle orale appliquée « avec leur jugement, donc de façon un peu variable » (03).
- Mauvais classement : 15 jours d'attente pour des commerçants très touchés (16).
- Point de vue minoritaire : « Qu'un petit commerçant attende deux semaines, ce n'est pas dramatique pour la compagnie » et « la trésorerie des commerçants, ce n'est pas notre rôle » (04), à mettre en regard des avances accordées à des commerçants « dont les salariés étaient sans paie » (05).

**Verbatims :**
- « Pour le tri, on a utilisé le montant estimé et la présence ou non d'une garantie perte d'exploitation, mais c'était brut. Les dossiers de commerçants fermés avec salariés auraient mérité d'être traités avant, mais l'outil ne le permet pas facilement. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Oui, c'est ça, avec un biais : ceux qui déclarent gros passent devant, parfois à tort. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Les dossiers de mes commerçants sont traités avec un peu d'avance, je crois, grâce à des contacts personnels, mais ce n'est pas structurel. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « J'ai fait passer en priorité mes plus gros clients, ceux avec des salariés. » — `assureurs__Assureur_12_Bertrand_Hoarau.txt`
- « Je me suis basé sur ce que les agents me disaient au téléphone, pas sur les dossiers. » — `assureurs__Assureur_16_Herve_Dumont.txt`
- « Un dossier à 200 000 euros passe avant un dossier à 3 000. » — `assureurs__Assureur_04_Gerard_Lefevre.txt`
- « Pour le tri, la durée de fermeture est le critère principal, bien avant le montant des dégâts. » — `assureurs__Assureur_08_Amandine_Rousseau.txt`

**Qualité des déclarations :** voir thème 1 (16/20 évoquent des manques ; tableau des informations manquantes les plus citées : situation/gravité 9, pièces 8, salariés 4, activité 3, joignabilité 3).

---

## (d) Ce que le commerçant voit du statut de son dossier

| Élément | Ce que disent les entretiens | Source |
|---|---|---|
| Statut | Un statut générique « en cours », qui ne dit rien de la suite | 01, 11, 17 |
| Accusé de réception | Mail générique sans date prévue ; accusé immédiat côté digital mais « ça ne dit rien du reste » | 17 |
| Visibilité sur les délais d'expertise | Aucune dans les outils digitaux ; la donnée n'est pas disponible | 17 |
| Visibilité des agents et courtiers | Ne voient pas l'avancement ; la ligne agents répond « en cours » ; pas de numéro de dossier unique par sinistre | 11, 13, 14 |
| Visibilité des experts | Ne peuvent pas répondre sur le paiement ni le montant ; le commerçant ne voit pas que le rapport est fait | 07, 09 |
| Contact | Le premier contact humain est souvent l'expert ; le commerçant relance ou est rappelé proactivement quand le gestionnaire a pris l'habitude de le faire | 05, 07 |
| Moments aveugles cités | Après la visite d'expert, avant le paiement (« pas de nouvelles du paiement ») | 16 |
| Taux d'usage de l'espace client | 35 % des commerçants ont créé un espace client | 17 |
| Concurrence | Concurrent cité avec expert sous 48 h ou suivi par SMS (note 4,1/5 vs 3,2/5) | 13, 14 |

**Verbatims :**
- « Du côté digital, le délai d'accusé est immédiat, mais ça ne dit rien du reste. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`
- « Le client ne voit rien de tout ça : il lui manque un statut avec des dates. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Ce que je refuserais : un statut automatique qui dit 'expertise en cours' alors que rien n'est planifié. Ça serait mensonger. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Les commerçants me disent souvent que je suis le premier contact humain depuis la déclaration. » — `assureurs__Assureur_07_Eric_Vasseur.txt`
- « Les commentaires parlent presque tous de l'attente sans information. » — `assureurs__Assureur_14_Olivier_Hamelin.txt`

Non couvert par les entretiens : l'interface exacte vue par le commerçant dans l'espace client ou le portail (aucun écran décrit au-delà du statut « en cours » et de l'accusé).

---

## (e) Contraintes et lignes rouges pour un nouveau circuit (fréquences sur 20)

| Contrainte / ligne rouge | N | Fichiers | Précision |
|---|---|---|---|
| Promesses de délai automatiques ou non tenables (donner une fourchette, pas un engagement ferme) | 8 | 01, 02, 03, 05, 15, 17, 18, 20 | 01 : ligne rouge explicite. 03, 15, 20 : fourchette avec conditions. 05 : refuse un statut « expertise en cours » mensonger. 18 : refuse tout affichage de délai (risque de litige). 02, 17 : constat d'impossibilité de s'engager aujourd'hui. |
| Perte de jugement humain / décision automatique (priorité, calcul, indemnisation) | 7 | 01, 02, 06, 08, 15, 19, 20 | 15 : « validation humaine » ; 19, 20 : pas de décision d'indemnisation automatique ; 20 : décision explicable et contestable. |
| Anti-fraude : données structurées, traçabilité, identifiant unique, photos horodatées ; pas de scoring visible du commerçant ou de l'agent ; la fraude ne doit pas retarder les honnêtes | 5 | 01, 03, 15, 18, 19 | 01 : données exploitables par la LAF. 19 : scoring en arrière-plan uniquement. 09, 10 : suspicion comme critère d'expertise ciblée. |
| Conformité / RGPD / données (consentement, minimisation, hébergement UE, droit d'accès, confidentialité bancaire et comptable, usage tarification) | 5 | 03, 15, 18, 19, 20 | 20 : associer la conformité « dès la conception, pas à la fin ». 18 : crainte que les données alimentent la tarification. |
| Ne pas contourner les agents / courtiers (le client « reste le mien ») | 4 | 11, 12, 13, 16 | 12 : refuse tout circuit qui retire des commissions. |
| Pas de ressaisie imposée aux courtiers ; pas de portail sans intégration | 2 | 13, 14 | 14 : API de suivi. |
| Expertise à distance non imposée, pas pour dommages structurels | 2 | 07, 10 | |
| Pas de forfaits généralisés sans vérification ; pas de calcul de perte présenté comme définitif | 2 | 06, 08 | 08 accepte « une avance forfaitaire encadrée ». |
| Règle de preuve claire pour les commerçants sans marchandise conservée (périssable) | 1 | 09 | |
| Pas d'IA seule pour prioriser (risque de sous-déclaration d'un sinistre grave) | 1 | 02 | |
| Canaux de collecte sécurisés (interdire WhatsApp) | 1 | 20 | |
| Business case exigé (réduction de coûts de gestion) | 1 | 18 | |
| Dépendance à l'outil de gestion existant | 1 | 17 | |

**Verbatims :**
- « Mes lignes rouges : qu'un outil envoie automatiquement des promesses de délai que je ne pourrai pas tenir, et que les données soient exploitables par la lutte anti-fraude. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « On ne peut pas afficher un délai qu'on ne tient pas. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Mes lignes rouges : un traitement automatique d'une décision d'indemnisation sans intervention humaine, et un affichage de scoring de fraude visible du commerçant ou de l'agent. » — `assureurs__Assureur_19_Sandrine_Lacour.txt`
- « Mes conditions : consentement et information clairs, minimisation des données, hébergement en Europe, traçabilité des décisions, pas de décision purement automatisée sur l'indemnisation. » — `assureurs__Assureur_20_Vincent_Moreau.txt`
- « Je veux que les agents soient intégrés dans le circuit, pas contournés. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « Je refuse qu'on exige de moi de ressaisir ce que le client a déjà fourni. Et je veux que le client reste le mien. » — `assureurs__Assureur_13_Isabelle_Caron.txt`
- « Je refuse qu'on exige trop de preuves quand le commerçant n'a pas pu garder la marchandise périssable. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- « Ça ne bloque pas le projet, ça l'encadre. » — `assureurs__Assureur_20_Vincent_Moreau.txt`

**Implication :** les lignes rouges citées ne sont pas incompatibles avec un affichage de fourchettes et une priorisation assistée avec validation humaine (15, 20), mais 18 maintient un refus de principe sur l'affichage de délais. Ce désaccord est à arbitrer par l'équipe.

---

## (f) Attentes d'un meilleur circuit (fréquences sur 20)

| Attente | N | Fichiers |
|---|---|---|
| Déclaration structurée qui capte gravité / situation / activité à la source (fiche d'identité du commerçant, champs dédiés, pièces classées) | 14 | 01, 02, 03, 06, 07, 08, 09, 10, 13, 14, 15, 16, 17, 19 |
| Statut lisible avec dates ou fourchettes (timeline) | 7 | 01, 03, 13, 14, 15, 17, 20 |
| Visibilité pour les agents et courtiers (tableau de bord, portail, API de suivi) | 5 | 11, 13, 14, 15, 16 |
| Vue partagée du même dossier entre agent, expert, gestionnaire ; expert corrige la gravité sur place ; rapport déposé dans le même espace | 3 | 07, 15, 16 |
| Pièces uniques / pas de redemande ; portail unique de pièces | 4 | 01, 02, 03, 13 |
| Identifiant unique de dossier, traçabilité | 2 | 13, 19 |
| Photos horodatées dès la déclaration ; dire au commerçant avant nettoyage quoi garder et photographier | 3 | 07, 09, 19 |
| Dire dès le premier appel que l'avance existe ; dissocier l'avance du rapport complet | 3 | 01, 06, 08 |
| Orientation des petits dossiers vers la visio dès la déclaration | 1 | 10 |
| Relances automatiques / alerte « sans nouvelle depuis X jours » pour le gestionnaire | 1 | 05 |
| Notifications SMS à chaque étape ; humain joignable | 2 | 14, 17 |
| Règle de tri écrite et dans l'outil | 1 | 03 |
| Priorisation automatique en première lecture avec validation humaine | 1 | 15 |
| Associer la conformité dès la conception | 1 | 20 |
| Aucune attente déclarée (scepticisme) | 3 | 04, 12, 18 (18 : business case chiffré) |

**Verbatims :**
- « Un circuit de mise en relation qui me donnerait des dossiers structurés, avec les pièces déjà classées, ce serait un gain énorme. » — `assureurs__Assureur_01_Claire_Bonnet.txt`
- « Un dossier qui arrive avec une fiche d'identité du commerçant claire, des pièces classées, une gravité estimée et une case 'priorité'. Ça m'aurait épargné deux jours. » — `assureurs__Assureur_02_Mathieu_Garnier.txt`
- « Une déclaration qui capte la gravité à la source. » — `assureurs__Assureur_15_Laurence_Giraud.txt`
- « Je voudrais un parcours qui capte le contexte, qui affiche une timeline avec des fourchettes de délais, qui notifie par SMS à chaque étape, et qui permet de joindre un humain. » — `assureurs__Assureur_17_Elodie_Fontaine.txt`
- « Un tableau de bord agent avec le statut de chaque dossier. » — `assureurs__Assureur_11_Patrice_Meunier.txt`
- « Un outil qui automatise les relances d'information, sans que je les écrive. Qui me dit : 'ce commerçant est sans nouvelle depuis 6 jours'. » — `assureurs__Assureur_05_Sabrina_Haddad.txt`
- « Dire dès le premier appel que l'avance existe. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Dire au commerçant avant le nettoyage quoi garder et quoi photographier. » — `assureurs__Assureur_09_Frederic_Colin.txt`
- « Je voudrais que la déclaration capte l'arrêt d'activité et son ampleur, en 3 questions. » — `assureurs__Assureur_06_Julien_Marchand.txt`
- « Une fiche avant la visite, avec la gravité et la situation du commerçant. » — `assureurs__Assureur_07_Eric_Vasseur.txt`

---

## Points non couverts par les entretiens
- Coût de gestion, budget, retour sur investissement : non couvert par les entretiens (18 demande un chiffrage et cite une cible de 15 % à titre de condition, sans donnée).
- Faisabilité technique d'intégration avec l'outil de gestion sinistres existant : non couvert par les entretiens (17 signale seulement la dépendance).
- Vue directe des commerçants (leur propre parole) : non couvert par ce corpus (analysé séparément).
- Délais d'indemnisation consolidés toutes catégories hors perte d'exploitation : non couvert au-delà des fourchettes individuelles (06, 11, 13, 14, 15).
- Taux de fraude réel et efficacité du contrôle allégé sous 5 000 € : non couvert au-delà des chiffres de crise de 19.
- Maturité numérique des commerçants (aisance) : seulement 35 % d'espaces clients (17) et « plutôt à l'aise avec la visio, même les plus âgés » (10) ; non couvert pour le reste.

## Résumé (comptage de fichiers lus : 20/20)
Thèmes principaux : déclarations incomplètes (16), délais et goulot d'experts (16), tri informel (15), absence de statut visible (13), satisfaction mal mesurée (12), avance méconnue (10), agents/courtiers relais (9), jugement humain à préserver (9), ressaisies (8), délais en fourchette (8).
