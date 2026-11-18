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
| 1 | 17:40 | Hélène | Lecture du brief (PDF, deck, protocoles) + 10 entretiens + mise en place skills/agents/knowledge | 132 610 | +45 998 | Extra usage compte : 16,15 $ → 16,66 $ (+0,51 $). 2e LLM à utiliser et à noter (contrainte du brief) |
| 2 | 18:00 | Hélène | Sous-agent UXR : synthèse des 20 assureurs (Claude Sonnet 5.5) | n/a (hors contexte principal) | 131 866 tokens (sous-agent) | 8 outils, 4 min. Fichier : synthese-assureurs.md |
| 3 | 18:10 | Hélène | Sous-agent UXR : synthèse des 50 commerçants (Claude Sonnet 5.5) | n/a (hors contexte principal) | 231 185 tokens (sous-agent) | 9 outils, 9 min. Fichier : synthese-commercants.md |
| 4 | 18:25 | Hélène | Session principale : prompt Gemini, lecture synthèse commerçants, personas, JTBD | 194 352 | +61 742 | Extra usage compte : 19,96 $ (+3,30 $ depuis la ligne 1, dont les 2 sous-agents) |
| 5 | 18:47 | Florian | Session 2e LLM (Gemini) : synthèse UXR des 50 commerçants | n/a (hors contexte principal) | 71 800 tokens nets estimés (665–765k cumulés API avant cache) | 10 outils, 4 min. Corpus 50 entretiens (44,9k) + sortie visible (15,2k) + retours outils (11,1k). Estimation (pas de get_usage ; hors thoughts ~7–14k) |
| 6 | 18:53 | Florian | Session 2e LLM (Gemini) : génération fichiers synthese-commercants.md, personas.md, jobs-to-be-done.md | n/a (hors contexte principal) | 21 000 tokens nets estimés (270–320k cumulés API avant cache) | 4 outils, 3 min. Sortie visible 20,7k (synthese 10,6k, personas 4,2k, JTBD 5,3k, vérif 110 verbatims 0,6k). Estimation hors thoughts (~3–6k) |
| 7 | 18:10 | Hélène | Sous-agent challenger : comparaison Claude vs Gemini (Claude Sonnet 5.5) | n/a (hors contexte principal) | 228 477 tokens (sous-agent) | 37 outils, 7 min 20. Fichiers : knowledge/uxr/outputs/final/ |

## Récap final
_À compléter à la fin : total tokens, répartition par étape et par personne, nombre de sous-agents, budget compte consommé (extra usage au départ : 16,15 $ / 40 $)._
