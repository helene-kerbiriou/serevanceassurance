# Backlog MoSCoW : « Rouvrir d'abord »

> Skill appliqué : `skills/pm/moscow/SKILL.md`. Entrées : `knowledge/pm/outputs/features.md` (FEAT-01 à FEAT-18), `knowledge/uxr/outputs/final/jobs-to-be-done-final.md`, `personas-final.md`, `knowledge/product/user-journey.md`. Données fictives.
> Question posée à chaque feature : **que se passe-t-il si elle n'est pas dans la première version ?** La « première version » est celle qui tient la promesse du concept : *un humain nommé, une date, une première aide*.
> La complexité technique n'est **pas** un critère. Priorités = **proposition à valider par l'équipe**. Les priorités **fragiles** (qui reposent sur une hypothèse assureur non tranchée) sont marquées ⚠.

## Résultat en un coup d'œil
| Priorité | Features | Nombre |
|---|---|---|
| **Must have** | FEAT-01, FEAT-03, FEAT-05, FEAT-08 ⚠, FEAT-09, FEAT-10 | 6 |
| **Should have** | FEAT-04, FEAT-06 ⚠, FEAT-07, FEAT-11, FEAT-12, FEAT-13 ⚠, FEAT-14 ⚠ | 7 |
| **Could have** | FEAT-02, FEAT-15, FEAT-17, FEAT-18 | 4 |
| **Won't have (cette fois)** | FEAT-16 | 1 |

**Contrôle du quota (étape 4 du skill) :** 6 Must sur 18, soit un tiers. Le noyau est réduit et le backlog penche vers Should et Could : pas de signal d'alerte.

## Le noyau : ce que forment les 6 Must
Les six Must couvrent la promesse du concept et rien de plus :
- **Un humain nommé :** FEAT-05.
- **Une date :** FEAT-09 (les dates) et FEAT-10 (où elles s'affichent).
- **Une première aide :** FEAT-08.
- **Condition de tout le reste :** FEAT-01 (ouvrir un dossier) et FEAT-03 (des données structurées dès la source).

---

## Must have

### FEAT-01 : Ouverture de dossier par un point d'entrée unique
**JTBD couverts :** JTBD-6, JTBD-9
**Priorité :** Must have
**Justification :** Sans point d'entrée, aucun dossier n'existe dans le produit et donc aucune promesse n'est tenue. Le brief note que les commerçants « ne savent pas qui appeler » et E01 raconte 25 minutes d'attente puis un renvoi vers l'espace client.

### FEAT-03 : Déclaration guidée et structurée
**JTBD couverts :** JTBD-3, JTBD-5
**Priorité :** Must have
**Justification :** Ce sont les données structurées qui permettent la priorisation, le signalement de la première aide, la vue du dossier et l'expertise. 14/20 assureurs attendent une déclaration structurée à la source, 16/20 reçoivent des déclarations incomplètes, et 11/50 commerçants ressaisissent (Yanis : « Je refuse de refaire un inventaire à la main », E09).

### FEAT-05 : Gestionnaire nommé avec contact direct
**JTBD couverts :** JTBD-4, JTBD-10
**Priorité :** Must have
**Justification :** C'est le premier pilier de la promesse. Sans interlocuteur nommé, Odile n'a personne à qui parler et Élise relance « une personne différente » à chaque fois (E05). 12/50 demandent un interlocuteur unique, 26/50 un humain quand c'est grave, et 60 % des appels reçus par un gestionnaire sont des demandes de nouvelles (assureur 01).

### FEAT-08 : Première aide, signalement et suivi ⚠
**JTBD couverts :** JTBD-1
**Priorité :** Must have
**Justification :** C'est le cœur du concept « Rouvrir d'abord » : sans première aide, Élise reste sans trésorerie, avec une avance attendue à ~12 jours et vécue à J+21 (25/50 en tension). Côté assureurs, l'avance jusqu'à 5 000 euros est déjà possible sans expertise mais peu connue (assureur 01).
**⚠ Priorité fragile :** montant, seuil, éligibilité et conditions anti-fraude ne sont pas tranchés par le corpus. Hypothèse de travail : signalement au gestionnaire, **qui valide toujours** (voir `features.md`).

### FEAT-09 : Dates en fourchette validées
**JTBD couverts :** JTBD-2, JTBD-11
**Priorité :** Must have
**Justification :** C'est le deuxième pilier de la promesse. 23/50 demandent une date (« Une date. Toujours une date. », E08), 13/50 vivent un silence de 1 à 3 semaines. Les assureurs acceptent la fourchette (7/20) mais pas la promesse ferme (8/20) : la fourchette validée est la seule forme tenable.

### FEAT-10 : Vue unique du dossier
**JTBD couverts :** JTBD-2, JTBD-4
**Priorité :** Must have
**Justification :** Sans lieu où le commerçant lit l'étape, la prochaine étape, les dates et la personne en charge, les dates de FEAT-09 n'ont nulle part où apparaître et le statut reste « en cours » (13/20 assureurs). Elle rassemble aussi les pièces au même endroit (« un seul dossier », E02).

---

## Should have

### FEAT-04 : Import de preuves alternatives
**JTBD couverts :** JTBD-5
**Priorité :** Should have
**Justification :** Le produit reste utilisable sans elle : le commerçant peut joindre photos et factures via FEAT-03. Mais Yanis voit ses données propres (logiciel, IMEI) ignorées, et 15/50 décrivent une exigence de preuves lourde ou impossible, avec une part retenue faute de preuve (E07, E38).
**Arbitrage persona :** surtout Yanis ; Élise en profite pour son stock. Odile n'est pas concernée.

### FEAT-06 : Premier retour sur la couverture ⚠
**JTBD couverts :** JTBD-6
**Priorité :** Should have
**Justification :** 13/50 découvrent la couverture trop tard, et l'accord de principe à J+1 est très apprécié (E44), mais le produit tient sa promesse sans ce message : le gestionnaire peut répondre à la demande.
**⚠ Priorité fragile :** la valeur juridique d'un message préliminaire n'est pas connue. Hypothèse de travail : message « à confirmer », sans valeur d'engagement, validé par un gestionnaire.

### FEAT-07 : Priorisation proposée, visible et décidée par le gestionnaire
**JTBD couverts :** JTBD-13, JTBD-12
**Priorité :** Should have
**Justification :** Le brief cite la priorité aux sinistrés graves, et le tri actuel est informel (15/20 assureurs) et biaisé par le montant déclaré. Mais sans cette feature le gestionnaire priorise comme aujourd'hui, au prix d'une expérience dégradée : ce n'est pas bloquant pour la promesse du concept.
**Arbitrage persona :** Élise propose les critères salariés, saison, trésorerie ; Yanis propose la qualité du dossier (E21). Les critères ne sont pas tranchés par le corpus : à décider par l'équipe.

### FEAT-11 : Alertes proactives par canal choisi
**JTBD couverts :** JTBD-2, JTBD-9, JTBD-11
**Priorité :** Should have
**Justification :** Contournement acceptable à court terme : le commerçant consulte la vue de FEAT-10 ou le gestionnaire l'appelle. Mais 13/50 vivent le silence, et « Les SMS à chaque étape, oui, à conserver. » (E36). Odile doit recevoir un appel, pas seulement une notification.
**Arbitrage persona :** Yanis préfère SMS ou en ligne, Odile l'appel : le canal par défaut reste à décider.

### FEAT-12 : Alerte retard côté gestionnaire
**JTBD couverts :** JTBD-2, JTBD-11
**Priorité :** Should have
**Justification :** Elle protège la promesse « une date » quand une fourchette risque d'être dépassée (E44 : deux semaines sans réponse). Sans elle, le retard est découvert quand le commerçant relance, ce qui est le comportement actuel.

### FEAT-13 : Vue agent, visibilité et alimentation du dossier ⚠
**JTBD couverts :** JTBD-4, JTBD-9
**Priorité :** Should have
**Justification :** Les agents et courtiers demandent la visibilité (assureurs 11, 13, 14) et 33/36 commerçants qui en ont un le citent comme point fort. Mais le gestionnaire nommé suffit à servir Odile pour la première version.
**⚠ Priorité fragile :** droits de l'agent, consentement et statut agent général ou courtier non tranchés. Hypothèse de travail : lecture, ouverture avec consentement.
**Arbitrage persona :** Must pour Odile si l'agent est son canal principal, non-sujet pour Yanis. Maintenu en Should faute d'éléments sur le rôle réel de l'agent.

### FEAT-14 : Expertise à distance ou sur place selon le dommage ⚠
**JTBD couverts :** JTBD-7
**Priorité :** Should have
**Justification :** Le brief cite « accélère les expertises » et l'expert arrive en médiane à J+9,5 pour ~7 jours attendus, mais la promesse du concept tient sans ce choix de mode. La visio est acceptée pour les petits dommages (E04, E43, E45, E50), pas pour le stock (E47).
**⚠ Priorité fragile :** JTBD-7 n'est exprimé explicitement que par 3/50 ; disponibilité des experts non couverte par les entretiens commerçants (6/20 assureurs citent le manque d'experts).

---

## Could have

### FEAT-02 : Consignes immédiates après sinistre
**JTBD couverts :** JTBD-5, JTBD-6
**Priorité :** Could have
**Justification :** Confort : la déclaration guidée (FEAT-03) recueille déjà les photos. Les consignes évitent le piège des périssables (3/50), mais leur contenu doit être validé par l'assureur.

### FEAT-15 : Suivi des versements et explication des retenues
**JTBD couverts :** JTBD-1, JTBD-12
**Priorité :** Could have
**Justification :** La phase 7 vient après la reprise d'activité ciblée par le concept. Elle répond à un besoin réel (méthode de calcul non expliquée, E30 ; part retenue, E07, E38), mais la promesse « rouvrir d'abord » est tenue sans elle.

### FEAT-17 : Retour du commerçant en fin de parcours
**JTBD couverts :** JTBD-11
**Priorité :** Could have
**Justification :** Utile à l'assureur, qui mesure mal la satisfaction (12/20), mais invisible pour le commerçant pendant qu'il rouvre son commerce.

### FEAT-18 : Information préalable sur les contrôles
**JTBD couverts :** JTBD-12
**Priorité :** Could have
**Justification :** Cas exprimé par 3/50 (E07, E17, E27) ; les commerçants comprennent la lutte contre la fraude et l'irritant porte sur le ton. Le JTBD-12 est déjà en partie couvert par FEAT-07 et FEAT-15.

---

## Won't have (cette fois)

### FEAT-16 : Suivi à part des biens de clients
**JTBD couverts :** JTBD-8
**Priorité :** Won't have (cette fois)
**Justification :** Besoin réel (7/50) mais cas limite sans persona : aucun des trois personas ne le porte. Exclu du périmètre actuel par choix, pas par oubli.
**À retrouver plus tard :** le garder documenté pour une itération future. « Je refuse de faire l'intermédiaire entre mes clients et l'assureur. » (E49)
**⚠ Alerte (étape 1 du skill) :** JTBD-8 n'a **aucune autre feature**. Il n'est donc couvert que par un Won't. C'est assumé, car il s'agit d'un cas limite ; à confirmer par l'équipe (« biens de clients : persona ou cas limite »).

---

## Arbitrages entre personas
| Arbitrage | Décision proposée |
|---|---|
| **Élise** veut la première aide, **Yanis** veut que ses preuves comptent, **Odile** veut son agent | Le Must retient la première aide (FEAT-08), la date (FEAT-09) et l'humain (FEAT-05), communes à tous. Preuves (FEAT-04) et agent (FEAT-13) passent en Should : chacun ne sert qu'un persona. |
| **Yanis** accepte tout numérique, **Odile** veut papier, téléphone ou agent | Le canal d'alerte (FEAT-11) reste un choix du commerçant ; aucun parcours 100 % numérique imposé. |
| **Élise** et **Yanis** proposent des critères de priorité différents | FEAT-07 en Should : ne pas figer les critères avant décision de l'équipe. |

## Priorités fragiles (reposent sur une hypothèse non validée)
| Feature | Hypothèse | À valider avec |
|---|---|---|
| FEAT-08 (Must) | Montant, éligibilité, validation par un gestionnaire | Cellule de crise, direction sinistres, conformité |
| FEAT-06 (Should) | Valeur d'un message préliminaire | Conformité, juridique |
| FEAT-13 (Should) | Droits et consentement de l'agent | Direction du réseau |
| FEAT-14 (Should) | Disponibilité des experts, choix du mode | Cellule de crise |

## Couverture des JTBD après priorisation
| JTBD | Couvert par | Priorité la plus haute |
|---|---|---|
| 1 Tenir financièrement | FEAT-08, 15 | Must |
| 2 Savoir où en est mon dossier | FEAT-09, 10, 11, 12 | Must |
| 3 Ne fournir qu'une fois | FEAT-03 | Must |
| 4 Interlocuteur et dossier uniques | FEAT-05, 10, 13 | Must |
| 5 Preuves alternatives | FEAT-03, 04, 02 | Must |
| 6 Couverture claire | FEAT-01, 06, 02 | Must |
| 7 Expert qui connaît mon métier | FEAT-14 | Should |
| 8 Biens de clients | FEAT-16 | Won't (cas limite assumé) |
| 9 Canal maîtrisé | FEAT-01, 11, 13 | Must |
| 10 Humain si c'est grave | FEAT-05 | Must |
| 11 Pas seul dans le flou | FEAT-09, 11, 12, 17 | Must |
| 12 Être cru | FEAT-07, 15, 18 | Should |
| 13 Ordre de traitement compris | FEAT-07 | Should |

Aucun JTBD n'a disparu du backlog. Le seul qui n'est couvert que par un Won't est le JTBD-8, signalé ci-dessus.

## Décisions qui reviennent à l'équipe
1. Valider ou changer les 6 Must, en particulier FEAT-08 (⚠) et le choix de laisser FEAT-07 en Should.
2. Statut de FEAT-13 : le passer en Must si l'agent est considéré comme canal principal d'Odile.
3. Statut de FEAT-16 : cas limite assumé ou persona.
4. Critères de priorisation de FEAT-07 (salariés, saison, trésorerie, qualité de preuve).
5. Canal de notification par défaut (FEAT-11).
