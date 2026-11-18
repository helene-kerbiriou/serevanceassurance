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

## Récap final
_À compléter à la fin : total tokens, répartition par étape et par personne, nombre de sous-agents, budget compte consommé (extra usage au départ : 16,15 $ / 40 $)._
