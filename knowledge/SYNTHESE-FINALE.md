# Synthèse finale : analyse UXR, personas, JTBD et concept « Rouvrir d'abord »

> Hackathon design <> IA, Sérévance Assurances (données fictives). Document de référence pour la suite du projet et pour la passation.
> Sources : `knowledge/uxr/outputs/final/` (`personas-final.md`, `jobs-to-be-done-final.md`, `comparaison.md`), issues du croisement de l'analyse Claude et de l'analyse Gemini, vérifiées sur le corpus de 50 entretiens commerçants. Contraintes assureurs : `knowledge/uxr/outputs/synthese-assureurs.md` (20 entretiens).

## 1. Démarche
1. Corpus : 50 commerçants (30 Sérévance sinistrés, 10 Sérévance non sinistrés, 10 autre assureur) et 20 assureurs (gestionnaires, experts, agents et courtiers, cellule de crise, digital, conformité).
2. Grille d'analyse validée par l'équipe. Segmentation des personas : **gravité du sinistre × aisance numérique**. Synthèse des assureurs séparée.
3. Deux analyses indépendantes, avec **deux LLM différents** : Claude (Sonnet 5.5) et Gemini.
4. **Agent challenger** : vérification mot pour mot des verbatims, recomptage des thèmes, comparaison des personas et des JTBD, arbitrage sur le corpus.
5. Résultat de la vérification : Claude 202 verbatims exacts sur 204, Gemini 110 sur 110. Les écarts de comptage viennent surtout de Gemini (trésorerie 37 au lieu de 25 à 30, preuves 20 au lieu de 15, priorisation 13 au lieu de 6). Les deux analyses convergent sur le fond et sur les médianes de timeline.

## 2. Les 3 personas finaux
| | **Élise** | **Yanis** | **Odile** |
|---|---|---|---|
| Étiquette | À l'arrêt, à bout de trésorerie | Outillé, veut de la visibilité et que ses données comptent | Commerçante de proximité qui s'appuie sur son agent |
| Ancrage vérifié | 11 entretiens (E02, E05, E06, E12, E17, E22, E24, E28, E42, E48, E50) | 10 entretiens (E04, E08, E09, E10, E13, E15, E21, E43, E45, E47) | 10 entretiens (E07, E11, E14, E16, E23, E26, E29, E41, E44, E46) + 2 en soutien (E03, E20) |
| Profil | Fermée 3 semaines ou plus, 1 à 4 salariés, aisance moyenne à forte | Rouvre en quelques jours à quelques semaines, contrat en ligne ou courtier, aisance forte | Commerce de longue date, assurée par un agent, aisance faible à moyenne |
| Besoin n°1 | Une première somme sous 10 à 14 jours | Une date à chaque étape, preuves reconnues | Son agent, un humain, un canal maîtrisé |
| Frustration clé | Indemnisation finale en médiane J+60, trésorerie sur épargne ou crédit fournisseur | Déclaration fluide puis « vide » ; refaire ce qu'il a fourni | Compagnie lente et floue, peur de perdre l'agent ou d'être obligée d'utiliser une appli |
| Citation | « Moi, je pense qu'une avance de 30 % sous 10 jours aurait tout changé. » (E05) | « Une date. Toujours une date. » (E08) | « Mon agent est une pépite. Je recommande Sérévance à cause de lui, pas pour la compagnie. » (E29) |

**Cas limites (hors personas) :** biens de clients en dépôt (7/50), soupçon de fraude (3/50), données de santé de la pharmacie (E25), non sinistrés (10/50, utiles pour l'information sur la couverture), E20 (données contradictoires).

## 3. Les 13 JTBD finaux
Comptages vérifiés (X/50). Détail, verbatims et formulation complète dans `jobs-to-be-done-final.md`.

| # | Job | Nature | Fréquence | Persona principal |
|---|---|---|---|---|
| 1 | Tenir financièrement pendant que le dossier avance | Fonctionnel | 25/50 | Élise |
| 2 | Savoir où en est mon dossier et à quelle date | Fonctionnel | 23/50 | Yanis (et tous) |
| 3 | Ne fournir chaque information qu'une seule fois | Fonctionnel | 11/50 | Yanis |
| 4 | Un seul interlocuteur identifié et un seul dossier | Fonctionnel | 12/50 | Odile |
| 5 | Faire reconnaître mes pertes avec les preuves dont je dispose | Fonctionnel | 15/50 | Yanis |
| 6 | Savoir ce qui est couvert, avant ou très tôt après | Fonctionnel | 13/50 | les trois |
| 7 | Expert qui connaît mon métier | Fonctionnel | 3/50 (faible) | Élise |
| 8 | Ne pas devenir l'intermédiaire entre mes clients et l'assureur | Fonctionnel | 7/50 | cas limite |
| 9 | Passer par un canal que je maîtrise | Fonctionnel | 5/50 | Odile |
| 10 | Être pris en charge par un humain quand c'est grave | Émotionnel | 26/50 (13 refusent robot, chatbot ou IA) | les trois |
| 11 | Ne pas rester seul et dans le flou | Émotionnel | 13/50 silence, 5/50 détresse | Élise, Odile |
| 12 | Être cru et traité comme un client honnête | Social | 3/50 | Élise, Odile |
| 13 | Comprendre pourquoi mon dossier passe avant ou après un autre | Social | 6/50 | Élise, Yanis |

**Repères chiffrés (commerçants Sérévance sinistrés) :** expert médiane J+9,5 (attendu ~7 jours) ; avance médiane J+21 pour les 9 qui l'ont reçue (attendue ~12 jours) ; indemnisation finale médiane J+60 (attendue ~21 jours).

## 4. Concept produit retenu : « Rouvrir d'abord »
**Décision de l'équipe : concept B.**

**Promesse :** *Un humain nommé, une date, une première aide.* Le sinistre est un moment, pas un dossier : on vise la reprise d'activité, le règlement vient ensuite.

| Pilier | JTBD | Preuve dans les entretiens |
|---|---|---|
| **Première aide** | 1, 6 | 25/50 en tension de trésorerie ; avance attendue ~12 j contre J+21 vécue ; côté assureurs, avance jusqu'à 5 000 € possible sans expertise mais peu connue |
| **Une date** | 2, 11, 13 | 23/50 ; les assureurs acceptent une fourchette (7/20), pas une promesse ferme |
| **Un humain nommé** | 4, 9, 10 | 12/50 interlocuteur unique ; 26/50 humain si grave ; 13/50 refusent le robot |
| **Dossier structuré dès le départ** (moyen, pas promesse) | 3, 5 | 14/20 assureurs attendent une déclaration structurée à la source ; 11/50 ressaisie |

**Garde-fous issus des assureurs :** pas de promesse de délai automatique (fourchette validée par un gestionnaire), pas de décision automatique, jugement humain conservé, données exploitables par l'anti-fraude, l'agent n'est pas contourné (il est le point fort cité par 33 des 36 commerçants qui en ont un).

**Alignement avec le brief :** « mise en relation commerçants / assureur post-sinistre » ; pistes du brief couvertes : déclarations structurées, priorité aux graves, bon interlocuteur, commerçant rassuré, visibilité sur le délai.

## 5. Décisions encore ouvertes (à trancher par l'équipe)
1. **Règle de gravité** : 3 semaines de fermeture (Claude) ou 2 semaines (Gemini) ; 16 sinistrés changent de case.
2. **Cinq commerçants à la fois en ligne et fermés longtemps** (E22, E24, E28, E48, E50) : Élise par gravité, Yanis par canal.
3. **Biens de clients** : cas limite (retenu pour l'instant) ou persona.
4. **Avance** : montant, seuil et conditions (hypothèse à poser dans le pitch, le corpus ne tranche pas).
5. Rôle exact de l'agent, critères de priorisation, statut des non sinistrés.

## 6. Prochaines étapes
1. **User journey** du produit « Rouvrir d'abord » : une journey par persona ou une journey commune avec variantes, de J0 (sinistre) à la reprise d'activité, avec les moments de vérité (déclaration, première aide, expert, date) et les points de contact humains.
2. **User stories** déduites de la journey (skill `skills/pm/user-story`). Point d'attention : ce skill exige une feature parente `FEAT-xx` ; il faut donc d'abord lister les features qui ressortent de la journey.
3. **Challenge MoSCoW** (skill `skills/pm/moscow`) : chaque priorité justifiée par un JTBD ; surveiller qu'il n'y ait pas plus de la moitié de Must.
4. **Prototype** construit avec `severance.md` comme couche design du projet. *Ce fichier n'est pas encore dans le repo : à ajouter avant de commencer.*
5. **Pitch (10 à 15 min)** : à préparer en parallèle (slide IA avec modèles et coût, démarche et rôles, personas, journey, prototype, réutilisabilité, automatisation). Les tokens sont suivis dans `TOKENS.md`.

## 7. Éléments pour le pitch (déjà disponibles)
- **Démarche et IA :** deux LLM (Claude, Gemini) comparés par un agent challenger ; vérification des verbatims (0 faux côté Gemini, 2 déformés côté Claude) ; humain qui décide (segmentation, concept).
- **Personas, comment on les a obtenus :** 50 entretiens synthétiques, segmentation gravité × aisance numérique, ancrage vérifié.
- **Réutilisable par une autre équipe :** repo structuré (`skills/`, `.claude/agents/`, `knowledge/`), `HANDOFF.md`, `TOKENS.md`.
- **Automatisable :** pipeline de skills et d'agents (synthèse, personas, JTBD, challenge), relançable sur un nouveau corpus avec `tools/extract_corpus.py`.
