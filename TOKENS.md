# Journal de consommation de tokens

Suivi de la consommation IA pendant le hackathon (2h). Mis à jour à chaque étape clé par Claude.

## Méthode
- **Source de vérité** : relevé de la fenêtre de contexte de la session (`get_usage`) = tokens cumulés dans la conversation, plafond 1 000 000.
- Un relevé est pris à chaque jalon (fin de phase, livrable produit). La consommation d'une étape = relevé actuel − relevé précédent.
- Les sous-agents / sessions parallèles sont notés à part (leur consommation n'est pas dans le contexte de la session principale).
- Chiffres exacts pour la fenêtre de contexte. Le coût en $ n'est pas mesurable par tâche : seul le budget global du compte est visible.
- Chaque membre de l'équipe qui utilise l'IA de son côté ajoute ses propres lignes (colonne « Qui »).

## Journal

| # | Heure | Qui | Étape / livrable | Tokens contexte (cumulés) | Δ étape | Notes |
|---|-------|-----|------------------|---------------------------|---------|-------|
| 0 | 17:15 | Hélène | Démarrage : clone repo, accès Drive bloqué | 86 612 | — | Dont ~57k de base fixe (outils, prompt système, skills) |
| 1 | 17:30 | Hélène | Lecture du brief (PDF, deck, protocoles) + 10 entretiens + mise en place skills/agents/knowledge | 132 610 | +45 998 | Extra usage compte : 16,15 $ → 16,66 $ (+0,51 $). 2e LLM à utiliser et à noter (contrainte du brief) |
| 2 | 17:29 | Hélène | Sous-agent UXR : synthèse des 20 assureurs (Claude Sonnet 5.5) | n/a (hors contexte principal) | 131 866 tokens (sous-agent) | 8 outils, 4 min. Fichier : synthese-assureurs.md |
| 3 | 17:38 | Hélène | Sous-agent UXR : synthèse des 50 commerçants (Claude Sonnet 5.5) | n/a (hors contexte principal) | 231 185 tokens (sous-agent) | 9 outils, 9 min. Fichier : synthese-commercants.md |
| 4 | 17:41 | Hélène | Session principale : prompt Gemini, lecture synthèse commerçants, personas, JTBD | 194 352 | +61 742 | Extra usage compte : 19,96 $ (+3,30 $ depuis la ligne 1, dont les 2 sous-agents) |
| 5 | 18:47 | Florian | Session 2e LLM (Gemini) : synthèse UXR des 50 commerçants | n/a (hors contexte principal) | 71 800 tokens nets estimés (665–765k cumulés API avant cache) | 10 outils, 4 min. Corpus 50 entretiens (44,9k) + sortie visible (15,2k) + retours outils (11,1k). Estimation (pas de get_usage ; hors thoughts ~7–14k). ⚠ Heure à vérifier : les fichiers Gemini ont été poussés à 17:54 |
| 6 | 18:53 | Florian | Session 2e LLM (Gemini) : génération fichiers synthese-commercants.md, personas.md, jobs-to-be-done.md | n/a (hors contexte principal) | 21 000 tokens nets estimés (270–320k cumulés API avant cache) | 4 outils, 3 min. Sortie visible 20,7k (synthese 10,6k, personas 4,2k, JTBD 5,3k, vérif 110 verbatims 0,6k). Estimation hors thoughts (~3–6k). ⚠ Heure à vérifier (voir ligne 5) |
| 7 | 18:02 | Hélène | Sous-agent challenger : comparaison Claude vs Gemini (Claude Sonnet 5.5) | n/a (hors contexte principal) | 228 477 tokens (sous-agent) | 37 outils, 7 min 20. Fichiers : knowledge/uxr/outputs/final/ |
| 8 | 18:43 | Hélène | Session principale (Claude Sonnet 5.5) : journey, features, MoSCoW, user stories, prototype v1 (thème severance.md, skill Impeccable) | 402 981 | +208 629 depuis la ligne 4 (194 352) | Extra usage compte : 26,46 $ (66 % du plafond de 40 $). Sous-agents déjà comptés lignes 2, 3, 7 |
| 9 | — | Hélène | Session principale (Sonnet 5.5) : benchmark (4 recherches web, lecture repo, rédaction benchmark.md) | 100 143 (nouvelle session) | n/a (fenêtre distincte des lignes 0 à 8) | Extra usage compte : 27,02 $ (67 % du plafond de 40 $) |
| 10 | — | Hélène | 2 sous-agents web-fetch (Sonnet 5.5) : landing Rockfi | n/a (hors contexte principal) | 34 111 tokens (11 732 + 22 379) | Le 1er a lu rockfi.com (mauvaise entreprise), le 2e rockfi.fr (bonne) |
| 11 | 18:53 | Hélène | Session principale (Claude Sonnet 5.5) : prototype v2 chaleureux (recherche et téléchargement de 5 photos, réécriture complète, vérifications visuelles, mises à jour PRODUCT.md et HANDOFF.md) | 491 332 | +88 351 depuis la ligne 8 (402 981) | Extra usage compte : 29,56 $ (73 % du plafond de 40 $), budget partagé avec les lignes 9 et 10. 5 recherches web incluses dans la fenêtre |

## Lecture du tableau
- **« # » est un identifiant, pas l'ordre chronologique** : les lignes ont été ajoutées par plusieurs personnes et sessions. Les heures des lignes 1 à 4, 7, 8 et 11 ont été recalées sur l'horloge réelle (commits et fichiers du repo). Les heures des lignes 5 et 6 (Florian) sont à vérifier.
- **Session principale de Claude (lignes 0, 1, 4, 8, 11)** : une seule fenêtre de contexte, relevée à chaque jalon (86 612 → 491 332). Ce chiffre est la taille du contexte, pas le total facturé : les relectures du contexte à chaque échange ne sont pas comptées.
- **Sous-agents Claude (lignes 2, 3, 7, 10)** : tokens consommés dans leur propre fenêtre, hors session principale.
- **Gemini (lignes 5, 6)** : estimations, pas de relevé AI Studio.
- **Ligne 9** : autre session Claude (fenêtre distincte).

## Récap provisoire (à mettre à jour avant le pitch)
| Bloc | Tokens | Source |
|---|---|---|
| Claude, session principale (ligne 11) | 491 332 | relevé exact (taille de la fenêtre) |
| Claude, session benchmark (ligne 9) | 100 143 | relevé de l'autre session |
| Claude, sous-agents (lignes 2, 3, 7, 10) | 625 639 | rapports des sous-agents (131 866 + 231 185 + 228 477 + 34 111) |
| Gemini (lignes 5, 6) | ≈ 92 800 | estimation (71 800 + 21 000) |
| **Total indicatif** | **≈ 1,31 million** | somme des blocs, pour un ordre de grandeur |

- **Modèles utilisés :** Claude Sonnet 5.5 (analyse, agents, prototype) et Gemini (2e LLM, synthèse indépendante). Contrainte « 2 LLM différents » respectée.
- **Budget compte (extra usage) :** 16,15 $ au départ, 29,56 $ maintenant, soit +13,41 $ sur 40 $ de plafond, toutes sessions confondues.
- **Coût moyen par livrable :** non mesurable précisément (le coût en $ n'est visible que pour le compte, pas par tâche).

## Récap final
_À compléter à la fin : total tokens, répartition par étape et par personne, nombre de sous-agents, budget compte consommé (extra usage au départ : 16,15 $ / 40 $)._
