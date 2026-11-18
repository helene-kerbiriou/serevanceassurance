# User stories : « Rouvrir d'abord »

> Skill appliqué : `skills/pm/user-story/SKILL.md`. Entrées : `backlog.md` (priorités MoSCoW, à valider), `features.md` (FEAT-01 à FEAT-18, hypothèses de travail), `knowledge/product/user-journey.md`, personas et JTBD finaux. Données fictives.
> **Périmètre :** les 6 Must et les 7 Should (29 stories). Les Could (FEAT-02, 15, 17, 18) et le Won't (FEAT-16) n'ont pas de story pour l'instant ; elles pourront être écrites si le périmètre change.
> **Acteurs :** les trois personas (Élise, Yanis, Odile) et trois rôles internes (gestionnaire sinistres, agent ou courtier, expert). Le « je veux » décrit une intention, jamais une interface. Le design relève du prototype (`severance.md`).
> **Hypothèses de travail transverses** (posées dans `features.md`) : aucune promesse ferme de délai, uniquement des fourchettes validées (G1) ; le produit propose, le gestionnaire décide (G2) ; pas de robot pour décider d'une indemnisation (G3) ; l'agent n'est pas contourné et agit avec le consentement du commerçant (G4) ; accord explicite sur les données (G5) ; repli humain à chaque étape importante (G6).
> Format : `US-xx`, feature parente, besoin, contexte pour le designer (issu des personas et de la synthèse), critères d'acceptation vérifiables pour le développeur, incertitudes. Aucune estimation de charge.

## Sommaire
| Feature | Priorité | Stories |
|---|---|---|
| FEAT-01 Ouverture de dossier | Must | US-01, US-02 |
| FEAT-03 Déclaration guidée et structurée | Must | US-03, US-04, US-05, US-06 |
| FEAT-05 Gestionnaire nommé | Must | US-07, US-08 |
| FEAT-08 Première aide | Must ⚠ | US-09, US-10 |
| FEAT-09 Dates en fourchette | Must | US-11, US-12 |
| FEAT-10 Vue unique du dossier | Must | US-13, US-14, US-15 |
| FEAT-04 Preuves alternatives | Should | US-16, US-17 |
| FEAT-06 Retour sur la couverture | Should ⚠ | US-18, US-19 |
| FEAT-07 Priorisation | Should | US-20, US-21 |
| FEAT-11 Alertes proactives | Should | US-22, US-23 |
| FEAT-12 Alerte retard | Should | US-24, US-25 |
| FEAT-13 Vue agent | Should ⚠ | US-26, US-27 |
| FEAT-14 Expertise selon le dommage | Should ⚠ | US-28, US-29 |

---

# MUST HAVE

## FEAT-01 : Ouverture de dossier par un point d'entrée unique

### US-01 : Ouvrir un dossier avec le strict minimum
**Feature parente :** FEAT-01
En tant que **Yanis** (commerçant outillé),
je veux ouvrir un dossier de sinistre en ne donnant que les informations indispensables,
afin de ne pas perdre de temps pendant que je remets mon commerce en état.

**Contexte (designer) :** Yanis déclare en 10 à 15 minutes quand le formulaire est simple (E04, E15, E32). Les commerçants ont déjà dû ressaisir adresse et contrat après un appel (E01). Le dossier peut se compléter après l'ouverture.
**Critères d'acceptation (dev) :**
- Étant donné un commerçant identifié, quand il ouvre un dossier, alors un numéro de dossier est créé avec uniquement : identité du commerce, contrat, date du sinistre et une description libre.
- Étant donné un dossier ouvert avec ce minimum, quand le commerçant revient plus tard, alors il peut compléter les informations manquantes sans repartir de zéro.
- Étant donné une identification impossible (contrat introuvable), quand le commerçant valide, alors le produit propose un repli humain avec un numéro direct (G6).
**Notes / incertitudes :** méthode d'identification du commerçant non définie.

### US-02 : Ouvrir un dossier par téléphone, sans devoir utiliser une application
**Feature parente :** FEAT-01 (voir aussi US-27)
En tant que **Odile** (commerçante de proximité, aisance numérique faible),
je veux faire ouvrir mon dossier par une personne que je connais, au téléphone,
afin de déclarer mon sinistre sans devoir me débrouiller seule avec un outil numérique.

**Contexte (designer) :** Odile passe par son agent (« Une appli pour les jeunes, mais moi j'ai la conseillère. », E46 ; « Je ne veux pas d'appli », E20). 5/50 refusent explicitement l'appli. **[Hypothèse]** : le dossier peut être ouvert par un conseiller ou l'agent avec son accord.
**Critères d'acceptation (dev) :**
- Étant donné que le commerçant appelle son agent ou la ligne sinistres, quand il donne son accord, alors un dossier est ouvert à son nom par la personne qui prend l'appel.
- Étant donné un dossier ouvert pour un tiers, quand il est créé, alors le commerçant est informé qu'il a été ouvert et par qui, sur le canal qu'il a choisi (voir US-22).
- Étant donné l'absence d'accord explicite du commerçant, quand un tiers tente d'ouvrir un dossier, alors le dossier n'est pas créé (G5).
**Notes / incertitudes :** droits des agents et consentement : hypothèse de travail à valider (voir `features.md`).

---

## FEAT-03 : Déclaration guidée et structurée

### US-03 : Décrire ma situation sans devoir chiffrer mes pertes
**Feature parente :** FEAT-03
En tant que **Élise** (commerçante à l'arrêt),
je veux indiquer si mon commerce est ouvert ou fermé, depuis quand, avec combien de salariés, sans avoir à donner un montant,
afin que mon dossier soit compris dans sa gravité même si je ne sais pas encore ce que j'ai perdu.

**Contexte (designer) :** les montants déclarés sont « un chiffre au hasard » (assureur 01) et le tri sur le montant biaise (ceux qui déclarent gros passent devant). E05 refuse « qu'on classe mon dossier sur une estimation faite dans l'urgence ».
**Critères d'acceptation (dev) :**
- Étant donné une déclaration, quand le commerçant indique la situation (ouvert ou fermé, date de fermeture, nombre de salariés, saison), alors le dossier est enregistré sans qu'aucun montant ne soit obligatoire.
- Étant donné un montant renseigné, quand il est enregistré, alors il est marqué comme « estimation du commerçant » et n'est jamais le seul critère de priorisation.
- Étant donné une information de situation manquante, quand le commerçant valide, alors le produit signale ce qui manque sans bloquer l'ouverture du dossier.
**Notes / incertitudes :** liste exacte des informations de situation à valider avec les gestionnaires.

### US-04 : Joindre des photos et pièces classées par type de dommage
**Feature parente :** FEAT-03
En tant que **Yanis**,
je veux décrire mes dommages par catégorie (vitrine, stock, matériel, autre) et y rattacher mes photos,
afin que l'expert et le gestionnaire comprennent ma situation sans me poser de questions déjà traitées.

**Contexte (designer) :** E01 a pris une trentaine de photos avant de toucher à quoi que ce soit ; un tiers des déclarations arrivent sans photos, liste de stock ou plainte (assureur 01). E24 signale un formulaire sans case pour son matériel de tatouage.
**Critères d'acceptation (dev) :**
- Étant donné une déclaration, quand le commerçant ajoute une photo, alors il peut la rattacher à une catégorie de dommage.
- Étant donné un type de commerce non prévu, quand le commerçant décrit un dommage, alors il peut saisir une catégorie libre.
- Étant donné un envoi de pièces volumineux, quand la connexion est interrompue, alors les pièces déjà envoyées sont conservées.
**Notes / incertitudes :** liste des catégories par métier à construire.

### US-05 : Ne jamais redonner une information déjà fournie
**Feature parente :** FEAT-03
En tant que **Yanis**,
je veux que chaque information que j'ai donnée soit réutilisée par la suite,
afin de ne plus devoir refaire mon inventaire ni renvoyer la même photo.

**Contexte (designer) :** 11/50 ressaisissent (E01, E04, E09, E15, E28). « Je refuse qu'on me redemande des pièces déjà fournies. » (E15).
**Critères d'acceptation (dev) :**
- Étant donné une information déjà enregistrée dans le dossier, quand une étape ultérieure la nécessite, alors elle est préremplie et non redemandée.
- Étant donné qu'un gestionnaire ou un expert a besoin d'une pièce déjà fournie, quand il la consulte, alors il la voit dans le dossier sans solliciter le commerçant.
- Étant donné une pièce vraiment manquante, quand elle est demandée, alors la demande indique pourquoi et la liste de ce qui a déjà été reçu.

### US-06 : Reprendre une déclaration interrompue
**Feature parente :** FEAT-03
En tant que **Élise**,
je veux pouvoir interrompre ma déclaration et la reprendre plus tard,
afin de la remplir en plusieurs fois pendant que je gère les urgences de mon commerce.

**Contexte (designer) :** **[Hypothèse]** : le corpus ne documente pas directement les interruptions ; E22 mentionne « une heure » pour tout lister.
**Critères d'acceptation (dev) :**
- Étant donné une déclaration partielle, quand le commerçant la quitte, alors les informations saisies sont conservées.
- Étant donné un dossier partiel, quand le commerçant revient, alors il voit ce qui reste à compléter.
- Étant donné une coupure de connexion, quand elle se produit, alors aucune information déjà validée n'est perdue.
**Notes / incertitudes :** hypothèse de conception, à valider.

---

## FEAT-05 : Gestionnaire nommé avec contact direct

### US-07 : Connaître la personne qui s'occupe de mon dossier
**Feature parente :** FEAT-05
En tant que **Odile**,
je veux connaître le nom et le numéro direct de la personne qui gère mon dossier dès le premier jour,
afin de ne plus rappeler « quelqu'un de différent » à chaque fois.

**Contexte (designer) :** « Que quelqu'un soit désigné, avec un nom et un numéro direct, dès le premier jour. » (E05) ; « J'ai rappelé deux fois, à chaque fois quelqu'un de différent. » (E01) ; 12/50 demandent un interlocuteur unique.
**Critères d'acceptation (dev) :**
- Étant donné un dossier ouvert, quand un gestionnaire lui est attribué, alors le commerçant voit son nom et son numéro direct.
- Étant donné un changement de gestionnaire, quand il a lieu, alors le commerçant est prévenu avec le nom du nouveau gestionnaire et la raison.
- Étant donné un dossier pas encore attribué, quand le commerçant le consulte, alors il voit la date prévue d'attribution (fourchette) et un numéro de repli (G6).
**Notes / incertitudes :** charge réelle des gestionnaires en crise (jusqu'à 40 dossiers en parallèle, assureur 01) ; règles d'attribution non définies.

### US-08 : Joindre un humain, ou être rappelé
**Feature parente :** FEAT-05
En tant que **Odile**,
je veux pouvoir joindre un humain, ou demander à être rappelée,
afin de ne jamais me retrouver face à un robot pour un sinistre important.

**Contexte (designer) :** 26/50 demandent un humain, 13/50 refusent robot, chatbot ou IA ; « Un robot au téléphone, non. » (E01) ; « Et je veux pouvoir parler à un humain si le sinistre est gros, pas qu'un chatbot. » (E04).
**Critères d'acceptation (dev) :**
- Étant donné un dossier ouvert, quand le commerçant demande à être rappelé, alors le gestionnaire reçoit la demande avec le dossier.
- Étant donné une demande de rappel, quand elle est enregistrée, alors le commerçant voit une fourchette de délai de rappel validée par le gestionnaire (G1).
- Étant donné une question portant sur une indemnisation, quand le commerçant la pose, alors la réponse vient d'une personne et non d'un automate (G3).
**Notes / incertitudes :** délai de rappel tenable en crise (non couvert).

---

## FEAT-08 : Première aide, signalement et suivi ⚠

### US-09 : Être alerté des dossiers éligibles à une première aide
**Feature parente :** FEAT-08
En tant que **gestionnaire sinistres**,
je veux être alerté des dossiers qui répondent aux critères d'une première aide,
afin de décider rapidement d'une avance sans attendre le rapport d'expert.

**Contexte (designer) :** l'avance jusqu'à 5 000 euros peut être débloquée sans expertise mais beaucoup de gestionnaires ne le savent pas (assureur 01) ; avances forfaitaires en crise (assureur 03) ; demande de dissocier l'avance du rapport complet (assureur 08). 7/20 assureurs refusent la décision automatique.
**Critères d'acceptation (dev) :**
- Étant donné un dossier dont la situation correspond à la règle d'éligibilité paramétrée par l'assureur, quand il est suffisamment complet, alors il est signalé au gestionnaire avec la raison.
- Étant donné un dossier signalé, quand le gestionnaire ne se prononce pas, alors aucun versement n'est déclenché automatiquement (G2).
- Étant donné la règle d'éligibilité, quand l'assureur la modifie, alors le signalement suit la nouvelle règle sans changement du produit.
**Notes / incertitudes :** ⚠ montant, seuil et conditions : hypothèse de travail, valeurs d'exemple dans le prototype (plafond de 5 000 euros cité par un gestionnaire).

### US-10 : Suivre l'état de ma demande de première aide
**Feature parente :** FEAT-08
En tant que **Élise**,
je veux voir où en est ma demande de première aide,
afin de savoir quand je pourrai racheter du stock et payer mes salariés.

**Contexte (designer) :** 25/50 en tension de trésorerie ; « Un acompte rapide, meme petit, pour tenir. » (E22) ; avance attendue ~12 jours, vécue à J+21 (9 cas) ; trésorerie sur épargne, famille ou crédit fournisseur.
**Critères d'acceptation (dev) :**
- Étant donné une demande de première aide, quand son état change (demandée, à l'étude, accordée, versée), alors le commerçant voit le nouvel état et la date du changement.
- Étant donné une aide à l'étude, quand le commerçant la consulte, alors il voit une fourchette de date de décision validée par le gestionnaire (G1).
- Étant donné une aide refusée ou reportée, quand le gestionnaire le décide, alors le commerçant reçoit l'explication rédigée par une personne et un contact direct (G6).
**Notes / incertitudes :** ⚠ conditions d'octroi non tranchées.

---

## FEAT-09 : Dates en fourchette validées

### US-11 : Voir la date de la prochaine étape, en fourchette
**Feature parente :** FEAT-09
En tant que **Yanis**,
je veux connaître la date prévue de la prochaine étape, sous forme de fourchette,
afin de planifier mon activité et ma trésorerie.

**Contexte (designer) :** « Une date. Toujours une date. » (E08) ; « L'incertitude est pire que l'attente. » (E02) ; 23/50 demandent une date ; 7/20 assureurs acceptent une fourchette, 8/20 refusent toute promesse ferme.
**Critères d'acceptation (dev) :**
- Étant donné un dossier à une étape donnée, quand le commerçant le consulte, alors la prochaine étape est affichée avec une fourchette de dates.
- Étant donné une fourchette affichée, quand elle est présentée, alors elle est formulée comme une estimation et non comme un engagement (G1).
- Étant donné une étape sans fourchette validée, quand le commerçant consulte son dossier, alors le produit indique « fourchette en cours de validation » et la date à laquelle elle sera donnée, jamais « en cours » seul.
**Notes / incertitudes :** méthode de calcul de la fourchette : hypothèse de conception.

### US-12 : Valider ou ajuster une fourchette avant sa publication
**Feature parente :** FEAT-09
En tant que **gestionnaire sinistres**,
je veux valider ou corriger la fourchette de dates proposée avant qu'elle ne soit visible du commerçant,
afin de ne jamais annoncer un délai que je ne pourrai pas tenir.

**Contexte (designer) :** la ligne rouge de 8/20 assureurs est la promesse de délai automatique ; « des délais affichés qui engagent juridiquement » (assureur 18).
**Critères d'acceptation (dev) :**
- Étant donné une fourchette proposée par le produit, quand le gestionnaire la valide ou la modifie, alors elle devient visible du commerçant.
- Étant donné une fourchette non validée, quand le délai de validation est dépassé, alors le gestionnaire est alerté (voir US-24) et le commerçant voit « fourchette en cours de validation ».
- Étant donné une fourchette modifiée après publication, quand le changement est enregistré, alors le commerçant est prévenu du changement et de sa raison.

---

## FEAT-10 : Vue unique du dossier

### US-13 : Voir l'étape en cours et la suivante
**Feature parente :** FEAT-10
En tant que **Yanis**,
je veux voir à tout moment l'étape en cours, la prochaine étape et la personne qui en est chargée,
afin de ne plus avoir à relancer pour savoir où en est mon dossier.

**Contexte (designer) :** 13/20 assureurs constatent que le commerçant ne voit que le statut « en cours » ; « Une barre de progression, comme pour un colis. » (E04) ; « Fluide au début, opaque ensuite. » (E15) ; 60 % des appels reçus par un gestionnaire sont des demandes de nouvelles (assureur 01).
**Critères d'acceptation (dev) :**
- Étant donné un dossier, quand le commerçant le consulte, alors il voit l'étape en cours, la prochaine étape, la personne en charge et la fourchette de dates.
- Étant donné un changement d'étape, quand il a lieu, alors la vue est mise à jour avec sa date.
- Étant donné un dossier sans changement depuis plusieurs jours, quand le commerçant le consulte, alors la vue indique la date du dernier changement et ce qui est attendu.
**Notes / incertitudes :** découpage exact des étapes à valider avec les gestionnaires.

### US-14 : Voir ce qui manque à mon dossier
**Feature parente :** FEAT-10
En tant que **Élise**,
je veux voir clairement les pièces ou informations qui manquent à mon dossier,
afin de ne pas retarder mon indemnisation sans le savoir.

**Contexte (designer) :** « J'ai appris par ma banque que l'expert avait demandé des pièces comptables, et personne ne m'avait prévenue. » (E06) ; un tiers des déclarations arrivent incomplètes (assureur 01).
**Critères d'acceptation (dev) :**
- Étant donné un dossier incomplet, quand le commerçant le consulte, alors la liste des éléments manquants est visible avec la raison de chaque demande.
- Étant donné un élément fourni, quand il est enregistré, alors il disparaît de la liste et le gestionnaire en est informé.
- Étant donné un élément que le commerçant ne peut pas fournir, quand il le signale, alors un repli est proposé (voir US-17).

### US-15 : Retrouver toutes les pièces dans un seul dossier
**Feature parente :** FEAT-10
En tant que **Élise**,
je veux que toutes mes pièces et échanges soient dans un seul dossier,
afin de ne pas retrouver des demandes différentes selon l'interlocuteur.

**Contexte (designer) :** « Je veux un seul interlocuteur et un seul dossier, avec toutes les pièces au même endroit. » (E02) ; « Ils ont eu l'air de traiter deux dossiers différents, avec deux numéros. » (E26).
**Critères d'acceptation (dev) :**
- Étant donné un sinistre, quand plusieurs personnes y travaillent (gestionnaire, expert, agent), alors toutes les pièces et échanges sont rattachés au même dossier.
- Étant donné une pièce déjà dans le dossier, quand un intervenant en a besoin, alors il la consulte sans créer de doublon.
- Étant donné deux dossiers ouverts pour un même sinistre, quand le doublon est détecté, alors le gestionnaire est alerté pour les fusionner.

---

# SHOULD HAVE

## FEAT-04 : Import de preuves alternatives

### US-16 : Apporter mes données numériques comme preuve
**Feature parente :** FEAT-04
En tant que **Yanis**,
je veux apporter mes données de gestion (stock, caisse, numéros de série, IMEI) comme preuve de mes pertes,
afin d'être indemnisé sur la base de ce que j'ai réellement perdu.

**Contexte (designer) :** « Qu'on accepte le logiciel de gestion comme preuve. » (E09) ; « Pour moi, le IMEI et le logiciel, ça devrait être une preuve suffisante. » (E13) ; 15/50 décrivent une exigence de preuves lourde.
**Critères d'acceptation (dev) :**
- Étant donné un dossier, quand le commerçant joint un export de ses données, alors il est enregistré comme preuve rattachée au dossier.
- Étant donné un export joint, quand il est lu automatiquement, alors un gestionnaire vérifie le résultat avant toute utilisation (G2, E36 : « pas lues par une machine sans que quelqu'un vérifie »).
- Étant donné un format non reconnu, quand l'envoi échoue, alors le commerçant voit pourquoi et peut joindre le fichier tel quel pour lecture humaine.
**Notes / incertitudes :** ce que l'assureur peut légalement accepter comme preuve (non couvert).

### US-17 : Signaler une preuve impossible et en proposer une autre
**Feature parente :** FEAT-04
En tant que **Élise**,
je veux pouvoir dire qu'une preuve demandée n'existe plus ou n'a jamais existé et proposer autre chose,
afin de ne pas être pénalisée pour des justificatifs volés, détruits ou jamais émis.

**Contexte (designer) :** « Je refuse qu'on me demande des preuves d'achat pour des objets d'occasion, c'est impossible à fournir. » (E35) ; factures volées ou détruites (E02) ; moitié retenue faute de preuve (E07, E38).
**Critères d'acceptation (dev) :**
- Étant donné une pièce demandée, quand le commerçant indique qu'il ne peut pas la fournir, alors il peut en proposer une autre (bon de commande, mail, relevé bancaire, photo).
- Étant donné une alternative proposée, quand elle est reçue, alors le gestionnaire l'évalue et la réponse est enregistrée au dossier avec sa raison.
- Étant donné une alternative refusée, quand le gestionnaire la rejette, alors la raison est communiquée par une personne.
**Notes / incertitudes :** critères d'acceptation côté assureur non couverts.

---

## FEAT-06 : Premier retour sur la couverture ⚠

### US-18 : Recevoir un premier retour sur ce qui est couvert
**Feature parente :** FEAT-06
En tant que **Élise**,
je veux savoir rapidement ce qui est a priori couvert, ce qui ne l'est pas et ce qui reste à confirmer,
afin de savoir quels frais engager sans attendre l'expertise.

**Contexte (designer) :** 13/50 ; « Dire vite si c'est couvert, avant même l'expertise. » (E34) ; « Je refuse les clauses que je découvre au moment du sinistre. » (E39) ; réponse attendue entre 24 h et 3 jours ; accord de principe à J+1 très apprécié (E44).
**Critères d'acceptation (dev) :**
- Étant donné un dossier avec situation et description, quand le gestionnaire a validé le message, alors le commerçant reçoit un retour qui distingue « a priori couvert », « non couvert » et « à confirmer ».
- Étant donné un retour envoyé, quand il est présenté, alors il indique qu'il n'a pas valeur d'engagement (hypothèse de travail).
- Étant donné un élément « à confirmer », quand le commerçant le consulte, alors il voit ce qui sera vérifié et la fourchette de date de confirmation.
**Notes / incertitudes :** ⚠ valeur juridique d'un message préliminaire non connue ; contenu à valider par la conformité.

### US-19 : Valider le message sur la couverture avant envoi
**Feature parente :** FEAT-06
En tant que **gestionnaire sinistres**,
je veux relire et valider le message sur la couverture avant qu'il parte,
afin de ne pas engager l'assureur au-delà de ce qui est certain.

**Contexte (designer) :** G1, G2 ; ligne rouge des assureurs sur les promesses automatiques.
**Critères d'acceptation (dev) :**
- Étant donné un message préparé par le produit, quand le gestionnaire le valide ou le modifie, alors seul le message validé est envoyé.
- Étant donné un message non validé, quand le délai prévu est dépassé, alors le gestionnaire est alerté (voir US-24).
- Étant donné une garantie citée dans le message, quand elle n'a pas été vérifiée, alors elle est présentée comme « à confirmer ».

---

## FEAT-07 : Priorisation proposée, visible et décidée par le gestionnaire

### US-20 : Voir et ajuster un classement proposé des dossiers
**Feature parente :** FEAT-07
En tant que **gestionnaire sinistres**,
je veux voir un classement proposé des dossiers à partir de la situation réelle des commerçants et pouvoir le corriger,
afin de traiter en premier ceux qui ne peuvent pas rouvrir.

**Contexte (designer) :** le tri actuel repose sur le montant déclaré, avec un biais (assureur 01) et il est informel dans 15/20 entretiens ; critères cités par les commerçants : salariés, outil de travail, trésorerie, saison, qualité de preuve (E06, E26, E42, E21) ; ligne rouge de 7/20 assureurs sur la décision automatique.
**Critères d'acceptation (dev) :**
- Étant donné des dossiers avec leur situation, quand le gestionnaire ouvre sa liste, alors un classement est proposé avec les critères utilisés pour chaque dossier.
- Étant donné un classement proposé, quand le gestionnaire le modifie, alors son choix prévaut et le motif est enregistré (G2).
- Étant donné un critère non renseigné, quand il manque, alors le dossier est signalé comme incomplet plutôt que classé bas par défaut.
**Notes / incertitudes :** critères de priorisation non tranchés par le corpus (arbitrage équipe).

### US-21 : Comprendre pourquoi mon dossier passe avant ou après un autre
**Feature parente :** FEAT-07
En tant que **Élise**,
je veux comprendre sur quels critères mon dossier est placé,
afin d'accepter l'ordre de traitement et d'organiser mon attente.

**Contexte (designer) :** « Être passé après des gens plus touchés, je comprends, à condition qu'on me le dise et qu'on me donne une date. » (E01) ; « Ce que je refuse : être mise dans le même sac qu'un petit dégât. » (E06) ; 6/50.
**Critères d'acceptation (dev) :**
- Étant donné un dossier classé, quand le commerçant le consulte, alors il voit les critères qui ont compté (par exemple : commerce fermé, salariés) sans voir les dossiers des autres.
- Étant donné un classement qui change, quand cela affecte la fourchette de dates, alors le commerçant est prévenu avec la nouvelle fourchette.
- Étant donné une contestation, quand le commerçant la formule, alors elle est transmise au gestionnaire (G6).

---

## FEAT-11 : Alertes proactives par canal choisi

### US-22 : Choisir comment je suis prévenu
**Feature parente :** FEAT-11
En tant que **Odile**,
je veux choisir d'être prévenue par appel, SMS ou application,
afin de recevoir les nouvelles sous la forme qui me convient.

**Contexte (designer) :** « mettez les deux » (E16) ; « Une appli pour les jeunes, mais moi j'ai la conseillère. » (E46) ; « Les SMS à chaque étape, oui, à conserver. » (E36) ; 5/50 réticents au numérique, 29/50 ouverts sous conditions.
**Critères d'acceptation (dev) :**
- Étant donné un dossier, quand le commerçant choisit son canal, alors toutes les alertes suivantes l'utilisent.
- Étant donné un commerçant sans choix, quand le dossier est ouvert, alors un canal par défaut est appliqué et modifiable à tout moment.
- Étant donné un canal injoignable (ligne coupée, par exemple E16), quand l'alerte échoue, alors un autre canal ou l'agent est utilisé.
**Notes / incertitudes :** canal par défaut selon le persona à décider.

### US-23 : Être prévenu à chaque changement d'étape
**Feature parente :** FEAT-11
En tant que **Yanis**,
je veux être prévenu dès que mon dossier change d'étape,
afin de ne jamais avoir à relancer pour savoir si quelque chose a bougé.

**Contexte (designer) :** 13/50 vivent un silence de 1 à 3 semaines ; « Ce qui m'a énervé cest quon me rappelle jamais, cest toujours moi qui rappelle. » (E03) ; « Qu'on m'appelle avant que j'appelle. » (E41).
**Critères d'acceptation (dev) :**
- Étant donné un changement d'étape, quand il est enregistré, alors le commerçant reçoit une alerte sur son canal avec la nouvelle étape et la prochaine fourchette.
- Étant donné un silence prolongé, quand aucune étape n'a changé depuis un seuil défini, alors le commerçant reçoit un message disant où en est le dossier et quand il aura des nouvelles.
- Étant donné un commerçant qui a demandé un appel proactif, quand le silence dépasse le seuil, alors un appel est proposé au gestionnaire (E01).
**Notes / incertitudes :** seuil de silence à définir.

---

## FEAT-12 : Alerte retard côté gestionnaire

### US-24 : Être alerté avant qu'une date soit dépassée
**Feature parente :** FEAT-12
En tant que **gestionnaire sinistres**,
je veux être alerté quand une date annoncée risque d'être dépassée,
afin de prévenir le commerçant avant qu'il ne relance.

**Contexte (designer) :** « Je refuse qu'on me laisse deux semaines sans réponse. » (E44) ; 60 % des appels reçus sont des demandes de nouvelles (assureur 01).
**Critères d'acceptation (dev) :**
- Étant donné une fourchette annoncée, quand sa borne haute approche sans avancement de l'étape, alors le gestionnaire est alerté avec le dossier concerné.
- Étant donné une alerte, quand le gestionnaire ne réagit pas, alors elle remonte à un responsable défini.
- Étant donné un retard confirmé, quand le gestionnaire met à jour la fourchette, alors le commerçant est prévenu (voir US-25).

### US-25 : Recevoir une explication en cas de retard
**Feature parente :** FEAT-12
En tant que **Élise**,
je veux recevoir une explication quand une date est repoussée,
afin de comprendre la raison et d'ajuster mon activité.

**Contexte (designer) :** « Je refuse qu'on me dise 'on vous recontacte' sans date. » (E08) ; « Fluide au début, opaque ensuite. » (E15).
**Critères d'acceptation (dev) :**
- Étant donné un retard, quand la fourchette est repoussée, alors le commerçant reçoit la nouvelle fourchette, la raison du retard et un contact direct.
- Étant donné un retard sans raison connue, quand le gestionnaire valide l'envoi, alors le message indique ce qui est en cours de vérification et quand une réponse sera donnée.
- Étant donné un retard supérieur à la fourchette initiale, quand il se produit, alors le gestionnaire est invité à appeler le commerçant (G6).

---

## FEAT-13 : Vue agent, visibilité et alimentation du dossier ⚠

### US-26 : Voir l'état des dossiers de mes clients
**Feature parente :** FEAT-13
En tant qu'**agent ou courtier**,
je veux voir l'état des dossiers de mes clients commerçants,
afin de les renseigner sans devoir appeler la ligne agents.

**Contexte (designer) :** « Un tableau de bord agent avec le statut de chaque dossier. » (Patrice Meunier, agent général) ; « Un portail courtier avec statut et dates prévues. » (Isabelle Caron, courtier) ; 9/20 assureurs signalent que les agents et courtiers n'ont pas de visibilité ; 33/36 commerçants qui en ont un le citent comme point fort.
**Critères d'acceptation (dev) :**
- Étant donné un agent ou courtier rattaché à un commerçant, quand il consulte ses dossiers, alors il voit l'étape, les fourchettes de dates et le gestionnaire en charge.
- Étant donné un dossier d'un commerçant qui n'est pas son client, quand l'agent tente de le consulter, alors l'accès est refusé (G5).
- Étant donné un commerçant sans agent ni courtier, quand son dossier est ouvert, alors le gestionnaire nommé tient ce rôle.
**Notes / incertitudes :** ⚠ droits (lecture seule en hypothèse), statut agent général ou courtier, RGPD : à valider.

### US-27 : Alimenter le dossier de mon client avec son accord
**Feature parente :** FEAT-13 (voir aussi US-02)
En tant que **Odile**, via son agent,
je veux que mon agent puisse ajouter des informations et des pièces à mon dossier avec mon accord,
afin de ne pas avoir à utiliser moi-même un outil numérique.

**Contexte (designer) :** « Mon agent est une pépite. » (E29) ; « Madame Giraud est venue sur place le troisième jour, de sa propre initiative. » (E05) ; ligne rouge de 4/20 assureurs : ne pas contourner les agents. Un agent général dit favoriser ses plus gros clients (assureur 12) : risque de biais à surveiller.
**Critères d'acceptation (dev) :**
- Étant donné l'accord explicite du commerçant, quand l'agent ajoute une information ou une pièce, alors elle apparaît dans le dossier avec la mention de l'auteur.
- Étant donné un accord retiré, quand le commerçant le révoque, alors l'agent ne peut plus modifier le dossier.
- Étant donné une modification par l'agent, quand elle a lieu, alors le commerçant en est informé sur son canal (US-22).
**Notes / incertitudes :** ⚠ périmètre exact des droits non tranché.

---

## FEAT-14 : Expertise à distance ou sur place selon le dommage

### US-28 : Se voir proposer le bon mode d'expertise
**Feature parente :** FEAT-14
En tant que **Yanis**,
je veux que l'expertise soit proposée à distance quand le dommage s'y prête et sur place quand il faut vérifier du stock,
afin d'obtenir mon expert plus vite sans perdre en fiabilité.

**Contexte (designer) :** expert médiane J+9,5 contre ~7 jours attendus (de 4 à 25) ; visio acceptée pour les petits dommages (E04, E43, E45, E50) ; réserve : pas de visio quand il y a du stock à vérifier (E47) ; « Ça marche parce que l'expertise est à distance. » (E43).
**Critères d'acceptation (dev) :**
- Étant donné un dossier avec ses dommages, quand le gestionnaire valide le mode d'expertise, alors le commerçant voit le mode choisi, la raison et une fourchette de date.
- Étant donné une expertise à distance, quand le commerçant la refuse, alors une expertise sur place est proposée avec sa fourchette.
- Étant donné un dossier contenant du stock à vérifier, quand le mode est proposé, alors l'expertise sur place est suggérée par défaut.
**Notes / incertitudes :** ⚠ critères de choix et disponibilité des experts non couverts (manque d'experts cité par 6/20 assureurs).

### US-29 : Recevoir le dossier déjà structuré
**Feature parente :** FEAT-14
En tant qu'**expert**,
je veux recevoir un dossier dont les pièces et la situation sont déjà classées,
afin d'évaluer les dommages sans solliciter à nouveau le commerçant.

**Contexte (designer) :** « Un circuit de mise en relation qui me donnerait des dossiers structurés, avec les pièces déjà classées, ce serait un gain énorme. » (assureur 01) ; un deuxième expert envoyé parce que le premier n'avait pas chiffré le stock (E05).
**Critères d'acceptation (dev) :**
- Étant donné une expertise attribuée, quand l'expert ouvre le dossier, alors il voit la situation, les dommages par catégorie, les photos et les pièces déjà fournies.
- Étant donné un élément manquant, quand l'expert le demande, alors la demande passe par le dossier et n'est pas redemandée si déjà fournie (US-05).
- Étant donné un même sinistre, quand un deuxième expert est nécessaire, alors la raison est enregistrée au dossier.
**Notes / incertitudes :** un seul expert par dossier quand c'est possible (hypothèse).

---

## Non couvert par ces stories
- **Could et Won't** (FEAT-02, 15, 17, 18, 16) : pas de story pour l'instant.
- **Estimation de charge :** non faite (hors périmètre de ce skill).
- **Critères d'acceptation chiffrés** (seuils de silence, délais de rappel, délai de validation) : à définir avec l'assureur.
- **Contraintes réglementaires et juridiques** des messages sur la couverture, de la première aide et du partage avec les agents : non couvertes par les entretiens.
