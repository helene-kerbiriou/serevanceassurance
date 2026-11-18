# Features : « Rouvrir d'abord »

> Dérivées de la user journey (`knowledge/product/user-journey.md`), des JTBD finaux (`knowledge/uxr/outputs/final/jobs-to-be-done-final.md`) et des contraintes assureurs (`knowledge/uxr/outputs/synthese-assureurs.md`). Données fictives.
> Une feature décrit une **capacité** (intention), pas une interface : le design appartient à l'étape prototype. Aucune priorité ici : elle vient du MoSCoW. Chaque feature remonte à au moins un JTBD.
> Statut : proposition à valider par l'équipe. FEAT-18 a été ajoutée par rapport à la journey (JTBD-12 n'était pas assez couvert).

## Garde-fous communs (valables pour toutes les features)
- **G1** Pas de promesse de délai automatique : toute date annoncée est une fourchette validée par un gestionnaire (ligne rouge de 8/20 assureurs).
- **G2** Pas de décision automatique : le produit propose, le gestionnaire décide (7/20).
- **G3** Ni robot ni chatbot pour décider d'une indemnisation (13/50 commerçants).
- **G4** L'agent et le courtier ne sont pas contournés (4/20 assureurs ; agent cité comme point fort par 33/36 commerçants qui en ont un).
- **G5** Données partagées avec accord explicite, exploitables par la conformité et l'anti-fraude ; ton non soupçonneux.
- **G6** Chaque écran important a un repli humain (numéro direct, rappel).

## Vue d'ensemble
| ID | Feature | Phase | JTBD | Personas |
|---|---|---|---|---|
| FEAT-01 | Ouverture de dossier par un point d'entrée unique | 1 | 6, 9 | Yanis, Odile, Élise |
| FEAT-02 | Consignes immédiates après sinistre | 1 | 5, 6 | tous |
| FEAT-03 | Déclaration guidée et structurée | 2 | 3, 5 | tous |
| FEAT-04 | Import de preuves alternatives | 2 | 5 | Yanis, Élise |
| FEAT-05 | Gestionnaire nommé avec contact direct | 3 | 4, 10 | Odile, Élise |
| FEAT-06 | Premier retour sur la couverture | 3 | 6 | tous |
| FEAT-07 | Priorisation proposée, visible et décidée par le gestionnaire | 3 | 13, 12 | Élise, Yanis |
| FEAT-08 | Première aide : signalement et suivi | 4 | 1 | Élise, Odile |
| FEAT-09 | Dates en fourchette validées | 3, 6 | 2, 11 | tous |
| FEAT-10 | Vue unique du dossier | 6 | 2, 4 | tous |
| FEAT-11 | Alertes proactives par canal choisi | 6 | 2, 9, 11 | tous |
| FEAT-12 | Alerte retard côté gestionnaire | 6 | 2, 11 | tous |
| FEAT-13 | Vue agent : visibilité et alimentation du dossier | 1, 2, 6 | 4, 9 | Odile |
| FEAT-14 | Expertise à distance ou sur place selon le dommage | 5 | 7 | Yanis, Élise |
| FEAT-15 | Suivi des versements et explication des retenues | 7 | 1, 12 | Élise |
| FEAT-16 | Suivi à part des biens de clients | 7 | 8 | cas limite |
| FEAT-17 | Retour du commerçant en fin de parcours | 7 | 11 | tous |
| FEAT-18 | Information préalable sur les contrôles | 3, 5 | 12 | Élise, Odile |

---

## FEAT-01 : Ouverture de dossier par un point d'entrée unique
- **Capacité :** le commerçant, ou son agent à sa place, ouvre un dossier de sinistre avec le strict minimum d'informations, par un seul point d'entrée.
- **JTBD :** 6 (savoir à qui s'adresser), 9 (canal maîtrisé). **Phase :** 1.
- **Pourquoi :** le brief note que les commerçants « ne savent pas qui appeler ». Attente de 25 min au téléphone puis renvoi vers l'espace client (E01).
- **Garde-fous :** G4, G6.
- **Dépendances :** alimente FEAT-03, FEAT-13.
- **Inconnues :** identité et authentification du commerçant ou de l'agent.

## FEAT-02 : Consignes immédiates après sinistre
- **Capacité :** dès l'ouverture, le commerçant reçoit ce qu'il doit photographier, ce qu'il peut jeter après photos, qui prévenir.
- **JTBD :** 5, 6. **Phase :** 1.
- **Pourquoi :** consigne de garder des périssables impossible à respecter (E07, E20, E36 : 3/50), moitié retenue faute de preuve (E07).
- **Garde-fous :** G5.
- **Inconnues :** contenu validé par l'assureur et la conformité (non couvert par les entretiens).

## FEAT-03 : Déclaration guidée et structurée
- **Capacité :** recueil structuré de la situation (activité, ouvert ou fermé, nombre de salariés, saison), des photos et des dommages par catégorie. Aucun montant obligatoire quand le commerçant ne le connaît pas. Chaque information n'est demandée qu'une fois.
- **JTBD :** 3, 5. **Phase :** 2.
- **Pourquoi :** ressaisie 11/50 ; 16/20 assureurs reçoivent des déclarations incomplètes ou en champ libre ; 14/20 attendent une déclaration structurée à la source ; estimation dans l'urgence refusée (E05).
- **Garde-fous :** G5, G6.
- **Dépendances :** base de FEAT-07, FEAT-08, FEAT-10, FEAT-14.
- **Inconnues :** liste des catégories de dommages par métier (E24 : pas de case « matériel de tatouage »).

## FEAT-04 : Import de preuves alternatives
- **Capacité :** le commerçant peut apporter comme preuve un export de logiciel de caisse ou de stock, des numéros de série ou IMEI, des bordereaux, des mails, des relevés bancaires.
- **JTBD :** 5. **Phase :** 2.
- **Pourquoi :** 15/50 ; « Qu'on accepte le logiciel de gestion comme preuve. » (E09) ; moitié retenue faute de preuve (E07, E38).
- **Garde-fous :** G5, vérification humaine de toute lecture automatique de pièces (E36).
- **Inconnues :** ce que l'assureur peut légalement accepter comme preuve (non couvert).

## FEAT-05 : Gestionnaire nommé avec contact direct
- **Capacité :** chaque dossier a un gestionnaire identifié (nom, numéro direct) dès le premier jour, visible du commerçant et de l'agent.
- **JTBD :** 4, 10. **Phase :** 3.
- **Pourquoi :** 12/50 interlocuteur unique ; « Un gestionnaire dédié, c'est ce qui change tout. » (E25) ; 60 % des appels reçus par les gestionnaires sont des demandes de nouvelles (assureur 01).
- **Garde-fous :** G3, G6.
- **Inconnues :** charge réelle des gestionnaires en crise (jusqu'à 40 dossiers en parallèle, assureur 01).

## FEAT-06 : Premier retour sur la couverture
- **Capacité :** dans un délai court, le commerçant reçoit ce qui est a priori couvert, ce qui ne l'est pas et ce qui reste à confirmer, validé par le gestionnaire.
- **JTBD :** 6. **Phase :** 3.
- **Pourquoi :** 13/50 ; réponse attendue entre 24 h et 3 jours ; accord de principe à J+1 très apprécié (E44) ; « Je refuse les clauses que je découvre au moment du sinistre. » (E39).
- **Garde-fous :** G1, G2, G3.
- **Inconnues :** délai possible et valeur juridique d'un retour préliminaire (non couvert).

## FEAT-07 : Priorisation proposée, visible et décidée par le gestionnaire
- **Capacité :** le produit propose un classement des dossiers à partir de la situation réelle (fermé, salariés, saison, trésorerie), le gestionnaire décide, et le commerçant voit sur quels critères son dossier est placé.
- **JTBD :** 13, 12. **Phase :** 3.
- **Pourquoi :** 6/50 ; le tri actuel est informel dans 15/20 entretiens assureurs et biaisé par le montant déclaré ; « Ce que je refuse : être mise dans le même sac qu'un petit dégât. » (E06).
- **Garde-fous :** G2 (essentiel), G5.
- **Dépendances :** FEAT-03.
- **Inconnues :** critères non tranchés par le corpus (arbitrage équipe).

## FEAT-08 : Première aide : signalement et suivi
- **Capacité :** dès que le dossier est suffisamment complet, le produit signale au gestionnaire les dossiers éligibles à une première somme ; le commerçant suit l'état de sa demande (demandée, à l'étude, accordée, versée) avec une fourchette de dates.
- **JTBD :** 1. **Phase :** 4.
- **Pourquoi :** 25/50 ; avance attendue ~12 jours, vécue à J+21 (9 cas) ; avance jusqu'à 5 000 euros possible sans expertise mais peu connue des gestionnaires (assureur 01).
- **Garde-fous :** G1, G2.
- **Dépendances :** FEAT-03, FEAT-05, FEAT-09.
- **Inconnues :** **montant, seuil et conditions : décision d'équipe**, le corpus ne tranche pas.

## FEAT-09 : Dates en fourchette validées
- **Capacité :** à chaque étape, une fourchette de dates est annoncée, validée par le gestionnaire, et mise à jour si elle change.
- **JTBD :** 2, 11. **Phases :** 3, 6.
- **Pourquoi :** 23/50 ; « Une date. Toujours une date. » (E08) ; 7/20 assureurs acceptent une fourchette, 8/20 refusent une promesse ferme.
- **Garde-fous :** G1 (essentiel).
- **Inconnues :** méthode de calcul de la fourchette (hypothèse de conception).

## FEAT-10 : Vue unique du dossier
- **Capacité :** une vue partagée affichant l'étape en cours, la prochaine étape, les dates en fourchette, la personne en charge, les pièces reçues et ce qui manque.
- **JTBD :** 2, 4. **Phase :** 6.
- **Pourquoi :** 23/50 ; le statut visible se limite à « en cours » (13/20 assureurs) ; pièces éparpillées (E02).
- **Garde-fous :** G5, G6.
- **Dépendances :** FEAT-03, FEAT-09.

## FEAT-11 : Alertes proactives par canal choisi
- **Capacité :** à chaque changement d'étape, le commerçant est prévenu par le canal qu'il a choisi (SMS, appel, application), avec un appel proactif possible en cas de silence.
- **JTBD :** 2, 9, 11. **Phase :** 6.
- **Pourquoi :** 13/50 silence vécu ; « Les SMS à chaque étape, oui, à conserver. » (E36) ; E16 : « mettez les deux » ; Odile attend un appel.
- **Garde-fous :** G3, G4, G6.
- **Inconnues :** canal par défaut selon le persona (hypothèse).

## FEAT-12 : Alerte retard côté gestionnaire
- **Capacité :** quand une date annoncée risque d'être dépassée, le gestionnaire est alerté avant que le commerçant relance, et le commerçant reçoit une explication.
- **JTBD :** 2, 11. **Phase :** 6.
- **Pourquoi :** « Je refuse qu'on me laisse deux semaines sans réponse. » (E44) ; silences de 1 à 3 semaines (13/50).
- **Garde-fous :** G1, G2.
- **Dépendances :** FEAT-09.

## FEAT-13 : Vue agent : visibilité et alimentation du dossier
- **Capacité :** l'agent ou le courtier voit l'état des dossiers de ses clients, peut ouvrir et alimenter un dossier à leur place et répondre à leurs questions.
- **JTBD :** 4, 9. **Phases :** 1, 2, 6.
- **Pourquoi :** agent point fort pour 33 des 36 commerçants qui en ont un ; 9/20 assureurs signalent que les agents et courtiers n'ont pas de visibilité ; Odile (aisance numérique faible).
- **Garde-fous :** G4 (essentiel), G5.
- **Inconnues :** rôle exact de l'agent et périmètre de ses droits (décision équipe).

## FEAT-14 : Expertise à distance ou sur place selon le dommage
- **Capacité :** le mode d'expertise est proposé selon le type de dommage et le stock à vérifier ; le dossier arrive structuré chez l'expert ; un seul expert par dossier quand c'est possible.
- **JTBD :** 7. **Phase :** 5.
- **Pourquoi :** expert médiane J+9,5 contre ~7 jours attendus ; visio acceptée pour les petits dommages (E04, E43, E45, E50), pas pour le stock (E47) ; 3/50 demandent un expert qui connaît leur métier (à ne pas sur-promettre).
- **Garde-fous :** G2.
- **Inconnues :** critères de choix et disponibilité des experts (manque cité par 6/20 assureurs).

## FEAT-15 : Suivi des versements et explication des retenues
- **Capacité :** le commerçant voit ce qui a été versé, ce qui reste à verser, et pourquoi chaque retenue a été appliquée, y compris le calcul de la perte d'exploitation.
- **JTBD :** 1, 12. **Phase :** 7.
- **Pourquoi :** « personne ne m'a expliqué la méthode de calcul. » (E30) ; part retenue faute de preuve (E07, E38) ; perte d'exploitation la plus lente (E06, E17, E25).
- **Garde-fous :** G1, G2, G5.

## FEAT-16 : Suivi à part des biens de clients
- **Capacité :** les biens de clients déposés chez le commerçant ont un suivi distinct, sans que le commerçant ait à servir d'intermédiaire.
- **JTBD :** 8. **Phase :** 7.
- **Pourquoi :** 7/50 ; « Je refuse de faire l'intermédiaire entre mes clients et l'assureur. » (E49).
- **Statut :** cas limite (hors personas), à arbitrer par l'équipe.

## FEAT-17 : Retour du commerçant en fin de parcours
- **Capacité :** à la clôture, le commerçant donne son retour sur le parcours, que l'assureur peut exploiter.
- **JTBD :** 11. **Phase :** 7.
- **Pourquoi :** la satisfaction est mal mesurée (12/20 assureurs) ; les retours portent sur l'absence d'information (assureur 01).
- **Garde-fous :** G5.

## FEAT-18 : Information préalable sur les contrôles *(ajoutée)*
- **Capacité :** le commerçant est prévenu à l'avance des contrôles (visite de l'expert, enquêteur, pièces demandées) et de leur raison, avec un ton non soupçonneux.
- **JTBD :** 12. **Phases :** 3, 5.
- **Pourquoi :** 3/50 se sentent traités en suspects (E07, E17, E27) ; ils comprennent la lutte contre la fraude, l'irritant est le ton (E17) ; 5/20 assureurs ont l'anti-fraude comme ligne rouge.
- **Garde-fous :** G5.

---

## Contrôle de couverture (étape 1 du skill MoSCoW)
| JTBD | Features | Couvert |
|---|---|---|
| 1 Tenir financièrement | FEAT-08, FEAT-15 | oui |
| 2 Savoir où en est mon dossier | FEAT-09, 10, 11, 12 | oui |
| 3 Ne fournir qu'une fois | FEAT-03 | oui |
| 4 Interlocuteur et dossier uniques | FEAT-05, 10, 13 | oui |
| 5 Preuves alternatives | FEAT-02, 03, 04 | oui |
| 6 Couverture claire | FEAT-01, 02, 06 | oui |
| 7 Expert qui connaît mon métier | FEAT-14 | oui, faiblement (3/50) |
| 8 Biens de clients | FEAT-16 | oui, cas limite |
| 9 Canal maîtrisé | FEAT-01, 11, 13 | oui |
| 10 Humain si c'est grave | FEAT-05 et garde-fous G3, G6 | oui |
| 11 Pas seul dans le flou | FEAT-09, 11, 12, 17 | oui |
| 12 Être cru | FEAT-07, 15, 18 | oui |
| 13 Ordre de traitement compris | FEAT-07 | oui |

**Aucun JTBD orphelin.** Les 13 JTBD sont couverts par au moins une feature.

## Points d'attention avant le MoSCoW
1. Les JTBD 7 et 8 sont peu fréquents (3/50 et 7/50 mais cas limite) : ne pas les sur-prioriser.
2. Certaines features dépendent d'une décision de l'assureur qui n'est pas tranchée : FEAT-06 (valeur d'un retour sur la couverture), FEAT-08 (aide), FEAT-13 (rôle de l'agent).
3. Le MoSCoW ne tient pas compte de l'effort de développement : ne pas retirer une feature parce qu'elle est complexe.
4. Si plus de la moitié des 18 features arrivent en Must, il faudra rouvrir l'arbitrage.

---

## Décisions assureur à poser, et hypothèses de travail retenues
> Décision d'équipe : poser ces hypothèses de travail pour avancer (user stories, prototype, pitch). Elles sont **à afficher comme hypothèses** et présentées comme les questions à poser à Sérévance. Le produit ne tranche pas ces règles : il les rend paramétrables par l'assureur.

### FEAT-08 : première aide
- **Ce que dit le corpus :** avance possible sans expertise jusqu'à 5 000 euros mais peu connue (assureur 01) ; avances forfaitaires en crise (assureur 03) ; demande de dissocier l'avance du rapport d'expert (assureur 08) ; un assureur veut un déclenchement automatique, 7/20 refusent toute décision automatique.
- **Ce qui manque :** qui décide ; plafond et mode de calcul ; critères d'éligibilité (fermeture, salariés, dossier complet, gravité) ; risque de trop-versé ; conditions anti-fraude ; déclenchement automatique ou non. Interlocuteurs : manager de cellule de crise, direction sinistres, conformité.
- **Hypothèse de travail :** le produit **signale** au gestionnaire les dossiers éligibles selon une règle paramétrable de l'assureur ; valeurs d'exemple dans le prototype (plafond de 5 000 euros cité par un gestionnaire) ; **un gestionnaire valide toujours** (jamais de versement automatique).

### FEAT-06 : premier retour sur la couverture
- **Ce que dit le corpus :** quasi rien côté assureurs ; un seul signale que des délais affichés « engagent juridiquement » (assureur 18). Côté commerçants : 13/50, réponse attendue entre 24 h et 3 jours.
- **Ce qui manque :** qui peut dire « couvert » avant expertise ; valeur juridique d'un message préliminaire ; garanties citables ; délai tenable en crise. Interlocuteurs : conformité, juridique, gestionnaires.
- **Hypothèse de travail :** message **« à confirmer »**, rédigé ou validé par un gestionnaire, **sans valeur d'engagement**, qui distingue « a priori couvert », « non couvert » et « à confirmer ». Contenu à faire valider par la conformité.

### FEAT-13 : rôle de l'agent
- **Ce que dit le corpus :** agents et courtiers demandent la visibilité (tableau de bord avec statut de chaque dossier, assureur 11 ; portail courtier avec statut et dates prévues, assureur 13 ; API de suivi, assureur 14) et refusent d'être contournés. Un agent général dit faire passer ses plus gros clients en priorité (assureur 12).
- **Ce qui manque :** droits (lecture seule ou ouverture et alimentation du dossier) ; consentement du commerçant ; différence de statut entre agent général et courtier indépendant ; risque de biais dans le tri ; qui joue ce rôle pour les 14/50 commerçants en ligne sans agent ; partage de données (RGPD). Interlocuteurs : direction du réseau, conformité.
- **Hypothèse de travail :** l'agent et le courtier ont une **visibilité en lecture** sur les dossiers de leurs clients ; ils **ouvrent ou alimentent un dossier seulement avec le consentement du commerçant** ; droits plus étendus à valider. Pour un commerçant sans agent, le gestionnaire nommé tient le rôle d'interlocuteur.
