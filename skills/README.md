# Skills UXR + PM : pipeline du hackathon

Les skills sont dans `skills/uxr/` et `skills/pm/` (chaque dossier contient un `SKILL.md`). Les agents qui les utilisent sont dans `.claude/agents/`.

## Pipeline

```
Entretiens (knowledge/uxr/inputs/txt/)
   │  1. grille d'analyse VALIDÉE par l'équipe   -> knowledge/uxr/outputs/grille-analyse.md
   ▼
uxr/synthese    -> knowledge/uxr/outputs/synthese.md
   ▼
uxr/personas    -> knowledge/uxr/outputs/personas.md   (2 à 3 personas, ancrés)
uxr/jtbd        -> knowledge/uxr/outputs/jobs-to-be-done.md
   ▼
pm/brief        -> challenge du brief (hypothèses, angles morts)
   ▼
pm/moscow       -> knowledge/pm/outputs/backlog.md   (priorisation du problème à traiter)
   ▼
pm/user-story   -> knowledge/pm/outputs/us.md
   ▼
User flow + user journey (à produire ensuite, à partir des personas et JTBD)
   ▼
uxr/export-html -> knowledge/uxr/outputs/personas.html (UNIQUEMENT après validation explicite)
```

## Adaptations par rapport aux skills d'origine (les `SKILL.md` n'ont pas été modifiés)
- Les sources sont des **PDF**, pas des `.docx` : citer les verbatims avec le nom du fichier texte, par exemple `commercants__Entretien_01_Karim_Benali.txt`.
- Le corpus est séparé en **deux populations** : 50 commerçants et 20 assureurs. Ne jamais les mélanger dans les comptages (« X/50 commerçants », « Y/20 assureurs »).
- Les skills disent « 10/16 interviewés » : lire « X/N de la population concernée ».
- Les données sont **fictives** (entretiens synthétiques du hackathon). Le dire dans les livrables.
- Les chemins `knowledge/uxr/outputs/` et `knowledge/pm/outputs/` existent déjà dans le repo.

## Règles communes
1. Aucun constat sans verbatim sourcé. Aucun verbatim inventé.
2. Pas de synthèse avant validation de la grille.
3. Journaliser les tokens de chaque étape dans `TOKENS.md`, et mettre à jour `HANDOFF.md`.
4. Les décisions produit restent humaines : l'IA signale, l'équipe tranche.
