# HANDOFF : passation du projet

> Ce fichier permet à une IA ou à une autre équipe de reprendre le projet sans contexte préalable.
> Il est mis à jour au fil du hackathon. Dernière mise à jour : 2026-11-18.

## 1. Contexte
- **Événement** : hackathon design, 2 heures, 3 product designers.
- **Projet** : serevanceassurance (assurance, nom du repo)
- **Brief** : _à renseigner, résumé du brief + lien Drive_ (https://drive.google.com/drive/folders/1C1XwL5JFA6yaBACoFFu7Ni8qmy0JboOx)
- **Problème à résoudre** : _à renseigner_
- **Équipe** : _noms + rôles_

## 2. Livrables
| Livrable | Statut | Emplacement | Auteur |
|----------|--------|-------------|--------|
| _ex. Recherche / insights_ | À faire | | |

## 3. Décisions clés
Format : décision, pourquoi, alternatives écartées.
- _à renseigner_

## 4. Ressources sources
Liste des documents du Drive utilisés et ce qu'ils contiennent.
- _à renseigner_

## 5. Structure du repo
```
README.md                    présentation courte
HANDOFF.md                   ce fichier
TOKENS.md                    journal de consommation de tokens
CLAUDE.md                    règles pour l'IA
brief/                       exercice.pdf, deck du hackathon, liens utiles
skills/uxr, skills/pm        skills (SKILL.md) ; pipeline dans skills/README.md
.claude/agents/              agent-uxr, agent-pm
knowledge/uxr/inputs/        50 entretiens commerçants, 20 assureurs, protocoles, txt/ (texte extrait)
knowledge/uxr/outputs/       grille, synthèse, personas, JTBD
knowledge/pm/outputs/        backlog (MoSCoW), user stories
tools/extract_corpus.py      PDF -> texte
```

## Contraintes du hackathon (brief/exercice.pdf et deck)
Pas de Figma/FigJam, mesure du coût en tokens, au moins 2 LLM différents, 2 h de travail (17h-19h), pitch 10-15 min max. Le pitch doit couvrir : ce qui est traité et pourquoi, la démarche et la répartition des rôles, une slide IA (modèles, coût), les personas et leur source, user journey / user flow, un prototype généré, une slide « rendre le travail réutilisable par une autre équipe », une slide « automatiser (agent, skill, workflow) ».

## Avancement
- [x] Corpus et brief importés, texte extrait
- [x] Skills UXR/PM et agents installés
- [ ] Grille d'analyse validée (proposition : knowledge/uxr/outputs/grille-analyse.md)
- [ ] Synthèse, personas, JTBD
- [ ] Choix du problème à traiter (brief + MoSCoW)
- [ ] User flow, user journey
- [ ] Prototype
- [ ] Pitch

## 6. Usage de l'IA
- Outil : Claude Code (modèle Sonnet 5.5)
- Prompts / consignes réutilisables : _à renseigner_
- Consommation : voir [TOKENS.md](TOKENS.md)

## 7. Limites connues et prochaines étapes
- _à renseigner_

## 8. Comment reprendre (pour une IA)
1. Lire ce fichier en entier, puis le brief.
2. Ne pas refaire ce qui est marqué « Fait » sans raison explicite.
3. Mettre à jour la section Livrables et Décisions à chaque modification.
4. Journaliser la consommation dans TOKENS.md.
