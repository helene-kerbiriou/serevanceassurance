# User journey commune : « Rouvrir d'abord »

> Concept retenu : **un humain nommé, une date, une première aide** (`knowledge/SYNTHESE-FINALE.md`, section 4).
> Une seule journey pour les trois personas : **Élise** (à l'arrêt, trésorerie), **Yanis** (outillé, veut de la visibilité), **Odile** (proximité, s'appuie sur son agent). Les écarts entre personas sont indiqués à chaque étape.
> Données fictives. Sources : `knowledge/uxr/outputs/final/` (50 commerçants), `synthese-assureurs.md` (20 assureurs). Les éléments marqués **[hypothèse]** sont des propositions de conception, pas des constats : à valider.
> Notation : E05 = entretien commerçant n°05 (correspondance dans `synthese-commercants.md`, tableau C2). J0 = jour du sinistre.

## Acteurs
| Acteur | Rôle dans la journey |
|---|---|
| **Commerçant** (Élise, Yanis, Odile) | Déclare, fournit ses preuves, suit son dossier |
| **Agent / courtier** | Relais de proximité : peut déclarer et alimenter le dossier à la place du commerçant (Odile). Non contourné (ligne rouge de 4 assureurs sur 20) |
| **Gestionnaire sinistres** | Interlocuteur nommé ; décide de la priorité, de la première aide et des dates annoncées |
| **Expert** | Évalue les dommages (sur place ou à distance selon le cas) |
| **Produit « Rouvrir d'abord »** | Dossier unique et partagé, déclaration guidée, statut, dates en fourchette, alertes |

## Vue d'ensemble

| Phase | 1. Sinistre | 2. Déclaration | 3. Prise en charge | 4. Première aide | 5. Expertise | 6. Attente et suivi | 7. Règlement et reprise |
|---|---|---|---|---|---|---|---|
| **Repère** | J0 | J0 à J+1 | J+1 à J+3 | J+3 à J+10/14 | J+7 (attendu) | en continu | J+21 (attendu) |
| **Vécu actuel** | | appel : attente 25 min (E01) | « en cours » sans date | avance médiane J+21 | expert médiane J+9,5 | silence 1 à 3 semaines (13/50) | indemnisation médiane J+60 |
| **Émotion** [estimation] | -2 | -1 | 0 | +1 | +1 | -1 puis 0 | +2 |
| **JTBD** | 6, 12 | 3, 5, 9 | 2, 4, 6, 10 | 1, 13 | 5, 7 | 2, 11, 13 | 1, 12 |

---

## Phase 1 : Le sinistre (J0)
**Ce que fait le commerçant :** constate les dégâts, appelle sa famille et la police, prend des photos avant de toucher à quoi que ce soit (E01 : une trentaine), nettoie pour rouvrir. Se demande si c'est couvert et qui appeler.
**Pain points actuels :** ne sait pas qui appeler (brief) ; consigne impossible de garder des périssables (3/50) ; ne sait pas si sa garantie couvre (13/50).
**Ce que propose le produit :**
- Point d'entrée unique, simple, ouvrable depuis un téléphone ou par l'agent : **« J'ai subi un sinistre »**.
- Consignes immédiates en une page : ce qu'il faut photographier, ce qu'on peut jeter après photos, qui appeler. Ces consignes évitent le piège des périssables.
- **Aucune obligation de tout renseigner d'un coup** : l'ouverture du dossier ne demande que le strict minimum.
**Points de contact :** commerçant, agent (alerté).
**Variantes :** *Yanis* ouvre le dossier seul, en quelques minutes. *Odile* appelle son agent, qui ouvre le dossier pour elle. *Élise* ouvre le dossier et indique dès le début que son activité est arrêtée.
**Moment de vérité :** le commerçant n'est pas seul dès les premières minutes.

## Phase 2 : La déclaration (J0 à J+1)
**Ce que fait le commerçant :** décrit les dégâts, joint des photos, estime des montants.
**Pain points actuels :**
- Appel : attente de 25 minutes puis renvoi vers l'espace client où tout est à ressaisir (E01).
- Ressaisie ou pièces redemandées : 11/50.
- Estimation de montants « au hasard » dans l'urgence : un tiers des déclarations arrivent incomplètes côté assureur (16/20 les jugent incomplètes ou en champ libre).
- Le tri actuel se fonde sur le montant déclaré, ce qui biaise (assureurs).
**Ce que propose le produit :**
- **Déclaration guidée et structurée à la source** : situation (fermé ou ouvert, nombre de salariés, activité), photos, dommages par catégorie (vitrine, stock, matériel, biens de clients). 14/20 assureurs attendent exactement cela.
- **On ne demande pas de montant** quand le commerçant ne le connaît pas ; seule la situation compte pour la priorité (JTBD-13, ligne rouge de E05 : « qu'on classe mon dossier sur une estimation faite dans l'urgence »).
- **Preuves alternatives** acceptées dès la déclaration : export du logiciel de caisse ou de stock, numéros de série, IMEI, bordereaux, photos (JTBD-5, 15/50).
- **Chaque information n'est demandée qu'une fois**, et elle est ensuite réutilisée (JTBD-3).
**Points de contact :** commerçant, agent (peut alimenter le dossier), produit.
**Variantes :** *Yanis* importe ses données de logiciel. *Odile* dicte à son agent ou à un conseiller, qui saisit. *Élise* peut joindre une liste de stock existante.
**Garde-fous :** données partagées avec accord explicite ; vérification humaine de toute lecture automatique de pièces (E36) ; données exploitables par l'anti-fraude (assureurs).
**Moment de vérité :** « Là j'ai dû ressaisir adresse, contrat, description. » (E01) ne doit plus arriver.

## Phase 3 : La prise en charge (J+1 à J+3)
**Ce que fait le commerçant :** attend la confirmation que son dossier existe et qu'il est couvert.
**Pain points actuels :**
- Un simple mail avec un numéro de dossier, puis rien (E01).
- Le commerçant rappelle, à chaque fois quelqu'un de différent (E01, 12/50 pour l'interlocuteur unique).
- 60 % des appels reçus par un gestionnaire sont des demandes de nouvelles (E-assureur 01, Claire Bonnet).
- Information sur la couverture tardive (13/50), alors que l'accord de principe rapide est très apprécié (E44, J+1).
**Ce que propose le produit :**
- **Un gestionnaire nommé**, avec son nom et un numéro direct, **dès le premier jour** (verbatim E05).
- **Un premier retour sur la couverture** : ce qui est a priori couvert, ce qui ne l'est pas, ce qui reste à confirmer. Le gestionnaire valide ce message [hypothèse sur le format].
- **Priorisation visible** : le gestionnaire classe le dossier selon la situation réelle (fermé, salariés, saison, trésorerie), et le commerçant voit pourquoi son dossier passe avant ou après un autre (JTBD-13). Le produit propose un classement, **le gestionnaire décide** (ligne rouge de 7 assureurs sur 20 contre la décision automatique).
- **Une première date, en fourchette**, validée par le gestionnaire. Jamais une promesse ferme (ligne rouge de 8 assureurs sur 20).
**Points de contact :** gestionnaire, agent (informé), commerçant.
**Variantes :** *Odile* reçoit l'appel du gestionnaire ou de son agent, pas un message d'appli seul. *Yanis* reçoit une notification avec la date. *Élise* voit en premier l'étape « première aide ».
**Moment de vérité :** le commerçant sait qui s'occupe de lui, et pour quand.

## Phase 4 : La première aide (J+3 à J+10/14)
**Ce que fait le commerçant :** cherche à payer son stock, ses salariés, le vitrier ; avance souvent sur sa trésorerie (4 800 euros pour E01, stock racheté sur économies, famille, crédit fournisseur).
**Pain points actuels :**
- Avance attendue en médiane 12 jours (7 à 21) ; vécue en médiane J+21, et citée par seulement 9 des 30 sinistrés Sérévance.
- Côté assureur, l'avance jusqu'à 5 000 euros peut être débloquée sans expertise, **mais beaucoup de gestionnaires l'ignorent** (E-assureur 01) ; l'avance est souvent liée au rapport d'expert (10/20).
**Ce que propose le produit :**
- Le produit **signale au gestionnaire** les dossiers éligibles à une première aide dès que le dossier est complet (situation, activité arrêtée, salariés). **Le gestionnaire décide.**
- Le commerçant voit à tout moment **où en est sa première aide** : demandée, à l'étude, accordée, versée, avec une fourchette de dates.
- Montant, seuil et conditions : **à fixer par l'équipe** (hypothèse du pitch, le corpus ne tranche pas).
**Points de contact :** gestionnaire (décideur), produit (signal et suivi), commerçant.
**Variantes :** *Élise* : c'est son moment clé. *Odile* : l'avance obtenue grâce à son agent est un moment positif cité (E29 : « L'avance de 5 000 euros à J+10, grâce à l'agent, m'a permis de rouvrir »). *Yanis* : moins central, mais veut le paiement rapide de la partie incontestable (E09).
**Moment de vérité :** « Moi, je pense qu'une avance de 30 % sous 10 jours aurait tout changé. » (E05)

## Phase 5 : L'expertise (J+7 attendu)
**Ce que fait le commerçant :** attend l'expert, prépare l'inventaire, rouvre ou non.
**Pain points actuels :**
- Expert vécu en médiane J+9,5 (de 4 à 25), attendu ~7 jours (48 h pour les périssables).
- Manque d'experts : cause d'allongement la plus citée côté assureurs (6/20).
- Un deuxième expert parce que le premier n'avait pas chiffré le stock (E05) ; expert pas spécialiste du métier (E24).
- Inventaire manuel de plusieurs jours (3 à 5 jours : E02, E05, E12, E16, E42).
**Ce que propose le produit :**
- **Mode d'expertise adapté** : à distance (visio) pour les petits dommages, acceptée par E04, E43, E45, E50 ; sur place quand il y a du stock à vérifier (réserve de E47) [hypothèse sur les critères].
- Le dossier arrive **déjà structuré** chez l'expert (pièces classées, situation), ce qui lui fait gagner du temps (attente de Claire Bonnet : dossiers structurés, pièces déjà classées).
- **Expert qui connaît le métier** quand c'est possible (JTBD-7, faible fréquence : ne pas sur-promettre).
- Un seul expert par dossier quand c'est possible.
**Points de contact :** expert, gestionnaire, commerçant.
**Variantes :** *Yanis* : expertise à distance plus facile, données du logiciel comme base. *Odile* : l'agent assiste à l'expertise. *Élise* : un seul expert pour tout le stock.
**Moment de vérité :** l'expert est le meilleur moment du parcours actuel (12/50) : il faut le préserver.

## Phase 6 : L'attente et le suivi (en continu)
**Ce que fait le commerçant :** attend, relance, tient son activité.
**Pain points actuels :**
- Silence ou relances sans réponse : 13/50, de 1 à 3 semaines (E05 : « trois semaines sans nouvelles, j'ai relancé quatre fois, à chaque fois une personne différente »).
- Le statut visible se résume à « en cours » (13 assureurs sur 20).
- « L'incertitude est pire que l'attente. » (E02)
**Ce que propose le produit :**
- **Une vue unique du dossier** : étape en cours, prochaine étape, **fourchette de dates**, qui est en charge, ce qui manque (JTBD-2, 23/50).
- **Alertes proactives** à chaque changement d'étape, par le canal choisi par le commerçant : SMS, appel, application [hypothèse : l'aisance numérique varie ; E36 et E47 apprécient les SMS, E04 une barre de progression].
- **Alerte retard** : si une date est dépassée, le gestionnaire est alerté **avant** que le commerçant relance, et le commerçant reçoit un message expliquant le retard.
- **Appel proactif** possible une fois en cas de silence (E01 : « Qu'on m'appelle une fois, de façon proactive »).
- **Visibilité pour l'agent** : il voit l'état du dossier et peut renseigner son client (9 assureurs sur 20 signalent que les agents et courtiers n'ont pas de visibilité).
**Points de contact :** produit, gestionnaire, agent, commerçant.
**Variantes :** *Yanis* : barre de progression et dates. *Odile* : appel de l'agent ou du gestionnaire. *Élise* : dates de première aide et de règlement en priorité.
**Garde-fous :** fourchettes validées par un gestionnaire ; jamais de promesse automatique ; pas d'écran « en cours » sans date.
**Moment de vérité :** « Une date. Toujours une date. » (E08)

## Phase 7 : Le règlement et la reprise (J+21 attendu)
**Ce que fait le commerçant :** reçoit l'indemnisation (matériel, stock, perte d'exploitation), rouvre ou reprend à plein régime.
**Pain points actuels :**
- Indemnisation finale médiane J+60 (de 21 à 120) pour des commerçants qui en attendaient ~21 jours.
- La perte d'exploitation est la plus lente (E06, E17, E25).
- Méthode de calcul non expliquée (E30, E39, E43).
- Part retenue faute de preuve (E07, E38 : moitié).
- Biens de clients non réglés (7/50, cas limite).
**Ce que propose le produit :**
- Suivi des versements : ce qui est versé, ce qui reste, **pourquoi** (explication de chaque retenue).
- **Paiement rapide de la partie incontestable** (E09), à confirmer par l'équipe.
- Clôture avec **retour du commerçant** sur le parcours (aujourd'hui la satisfaction n'est pas mesurée de façon systématique, 12/20 assureurs).
- **Biens de clients** : suivi à part pour que le commerçant ne devienne pas l'intermédiaire de ses propres clients (JTBD-8, cas limite).
**Points de contact :** gestionnaire, commerçant, agent.
**Moment de vérité :** le commerçant a rouvert, et l'explication de ce qu'il a reçu est claire.

---

## Courbe d'émotion (estimation à partir des verbatims, échelle -2 à +2)
| Phase | Aujourd'hui | Avec « Rouvrir d'abord » [hypothèse] |
|---|---|---|
| 1 Sinistre | -2 | -2 (inévitable) |
| 2 Déclaration | -1 (appel long, ressaisie) | 0 |
| 3 Prise en charge | -1 (« en cours ») | +1 (humain nommé, date) |
| 4 Première aide | -2 (trésorerie) | +1 |
| 5 Expertise | +1 | +1 |
| 6 Attente | -2 (silence) | 0 |
| 7 Règlement | 0 | +1 |

## Les trois promesses sur la journey
| Promesse | Phases où elle se joue | Preuve |
|---|---|---|
| **Un humain nommé** | 3, 5, 6, 7 | 12/50 interlocuteur unique ; 26/50 humain si grave ; 13/50 refusent le robot |
| **Une date** | 3, 4, 6, 7 | 23/50 ; fourchettes validées (7/20 assureurs) |
| **Une première aide** | 3, 4 | 25/50 ; avance attendue ~12 j contre J+21 |

## Garde-fous (issus des assureurs, à respecter dans tous les écrans)
- Pas de promesse de délai automatique : fourchette validée par un gestionnaire.
- Pas de décision automatique : le produit propose, le gestionnaire décide.
- Données exploitables par la conformité et l'anti-fraude ; ton non soupçonneux (3/50 se sentent traités en suspects).
- L'agent et le courtier ne sont pas contournés.
- Ni robot ni chatbot pour décider d'une indemnisation.

## Features qui en découlent (amorce pour les user stories et le MoSCoW)
Liste à relire et à compléter par l'équipe. Chaque feature remonte à un JTBD.
| ID | Feature | JTBD |
|---|---|---|
| FEAT-01 | Ouverture de dossier en un point d'entrée, y compris par l'agent | 6, 9 |
| FEAT-02 | Consignes immédiates après sinistre | 6, 5 |
| FEAT-03 | Déclaration guidée et structurée (situation, photos, catégories de dommages) | 3, 5 |
| FEAT-04 | Import de preuves alternatives (logiciel, IMEI, bordereaux) | 5 |
| FEAT-05 | Gestionnaire nommé avec numéro direct | 4, 10 |
| FEAT-06 | Retour sur la couverture validé par le gestionnaire | 6 |
| FEAT-07 | Priorisation proposée, visible, décidée par le gestionnaire | 13, 12 |
| FEAT-08 | Première aide : signalement au gestionnaire et suivi de la demande | 1 |
| FEAT-09 | Dates en fourchette validées par un gestionnaire | 2, 11 |
| FEAT-10 | Vue unique du dossier (étape, prochaine étape, ce qui manque) | 2, 4 |
| FEAT-11 | Alertes proactives par canal choisi (SMS, appel, appli) | 2, 9, 11 |
| FEAT-12 | Alerte retard côté gestionnaire | 2, 11 |
| FEAT-13 | Vue agent : visibilité et alimentation du dossier | 4, 9 |
| FEAT-14 | Expertise à distance ou sur place selon le dommage | 7 |
| FEAT-15 | Suivi des versements et explication des retenues | 1, 12 |
| FEAT-16 | Suivi à part des biens de clients | 8 |
| FEAT-17 | Retour du commerçant en fin de parcours | 11 |

## Hypothèses à valider ou décisions d'équipe
1. Montant, seuil et conditions de la première aide.
2. Format du premier retour sur la couverture (qui l'écrit, avec quelle garantie).
3. Critères de priorisation (salariés, saison, trésorerie, qualité de preuve), non tranchés par le corpus.
4. Critères pour choisir expertise à distance ou sur place.
5. Canal de notification par défaut selon le persona.
6. Rôle exact de l'agent dans l'ouverture et l'alimentation du dossier.
7. Biens de clients : cas limite ou persona.
