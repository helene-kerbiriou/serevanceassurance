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
severance.md                 couche design du prototype (thème Lumon / Severance)
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
- [x] Grille d'analyse validée (knowledge/uxr/outputs/grille-analyse.md)
- [x] Synthèses : synthese-commercants.md (50), synthese-assureurs.md (20)
- [x] Personas (Élise, Yanis, Odile) et JTBD : proposés, **à valider par l'équipe**
- **Pause levée.** Analyse Gemini obtenue et challengée. Synthèse finale : knowledge/SYNTHESE-FINALE.md (personas finaux Élise / Yanis / Odile, 13 JTBD, concept retenu **B « Rouvrir d'abord »** : un humain nommé, une date, une première aide).
- **User journey commune faite** : knowledge/product/user-journey.md (7 phases J0 -> reprise, 17 features candidates FEAT-01 à FEAT-17, hypothèses à valider).
- **Features formalisées** : knowledge/pm/outputs/features.md (FEAT-01 à FEAT-18, aucun JTBD orphelin).
- **MoSCoW fait** : knowledge/pm/outputs/backlog.md (6 Must, 7 Should, 4 Could, 1 Won't), priorités à valider.
- **User stories faites** : knowledge/pm/outputs/us.md (29 stories : 6 Must + 7 Should).
- **Prototype fait** : prototype/index.html (HTML autonome, thème severance.md, ton humain ; vues : accueil, déclaration en 3 étapes, ouverture, suivi du dossier). Contexte produit : PRODUCT.md. Non fait : vue gestionnaire, vue agent, DESIGN.md.
- **Prochaines étapes :** (user journey, features, MoSCoW, user stories, prototype faits) -> relecture équipe, pitch -> prototype avec severance.md (design, à ajouter au repo) -> pitch.
- **Benchmark fait** : knowledge/product/benchmark.md (Rockfi lu sur rockfi.fr, Bpifrance Prêt Solidarité Commerce, Alan, "Sidecar" non identifié avec certitude, compléments 🔎 à vérifier, matrice, principes réutilisables, voix proposée "présent, calme, précis"). À valider par l'équipe : identité de "Sidecar", articulation avec le prêt Bpifrance, voix.
- Décisions ouvertes : règle de gravité, E22/E24/E28/E48/E50, biens de clients, montant de l'avance (voir SYNTHESE-FINALE.md section 5).
- (historique) En pause avant continuation : obtenir l'analyse Gemini puis la comparer à celle de Claude.
- [ ] Gemini : synthèse + personas + JTBD (prompts/gemini-synthese-commercants.md) -> à enregistrer dans knowledge/uxr/outputs/gemini/
- [ ] agent-challenger (.claude/agents/agent-challenger.md) : compare les deux analyses -> knowledge/uxr/outputs/final/ (comparaison.md, personas-final.md, jobs-to-be-done-final.md)
- [ ] Les personas et JTBD finaux remplacent les versions provisoires pour la suite (brief, MoSCoW)
- [ ] Valider la règle de gravité (durée de fermeture) et l'aisance numérique déduite du texte
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
