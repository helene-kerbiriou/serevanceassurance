# Prompt Gemini : synthèse indépendante des 50 entretiens commerçants

**Modèle :** Gemini (AI Studio, aistudio.google.com), le modèle le plus capable proposé dans la liste.
**Fichier à importer :** `knowledge/uxr/inputs/corpus-commercants-gemini.txt` (50 entretiens, séparés par des lignes `######## FICHIER : … ########`).
**Objectif :** produire une synthèse indépendante, à comparer à celle de Claude (`knowledge/uxr/outputs/synthese-commercants.md`). Ne pas montrer à Gemini le résultat de Claude.
**Après l'envoi :** noter dans `TOKENS.md` le modèle, les tokens d'entrée et de sortie affichés par AI Studio.

---

## Prompt à coller (après avoir importé le fichier)

```
Tu es chercheur UX (UXR). Le fichier joint contient 50 retranscriptions d'entretiens de commerçants sinistrés lors d'émeutes, dans le cadre d'une étude exploratoire pour l'assureur fictif « Sérévance Assurances ». Les données sont fictives. Chaque entretien commence par une ligne « ######## FICHIER : nom_du_fichier ######## ».

MISSION
Produis une synthèse thématique fidèle et traçable des 50 entretiens. Lis les 50 entretiens en entier, pas un échantillon. Réponds en français.

GRILLE D'ANALYSE (à appliquer à chaque entretien)
1. Pain points (frictions, irritants, blocages)
2. Besoins explicites et latents
3. Motivations / déclencheurs
4. Freins / objections
5. Contexte d'usage
6. Verbatims marquants
Axes spécifiques :
- Segment : activité, taille, ancienneté, canal de souscription (agent / courtier / en ligne), aisance numérique, gravité du sinistre, assureur (Sérévance sinistré / non sinistré / autre assureur)
- Timeline vécue : J0, expert, avance, indemnisation (en jours)
- Délais attendus vs vécus
- Déclaration et suivi : canal, relances, ressaisies, visibilité sur le statut
- Émotion : meilleur et pire moment, recommandation
- Lignes rouges : robot / chatbot, partage de données, priorisation perçue comme injuste, ressaisie, estimation dans l'urgence, besoin d'un humain pour un gros sinistre

LIVRABLE (format Markdown exact)
# Synthèse des entretiens commerçants
## Méthode : corpus N = 50, grille, date.
## Thèmes (du plus partagé au plus marginal)
### 1. [Titre] — X/50 interviewés
**Constat :** 1 à 2 phrases factuelles.
**Verbatims :**
- « … » — nom_du_fichier
**Implication :** pour le design / le produit, sans trancher.
(… autant de thèmes que nécessaire)
## Timeline vécue vs attendue
Tableau : délai pour l'expert, l'avance, l'indemnisation. Donne pour chacun la médiane et la fourchette (min–max) du vécu, et du délai attendu quand il est cité.
## Lignes rouges
Tableau avec le nombre de commerçants concernés sur 50 pour chacune.
## Segmentation
Tableau : une ligne par entretien avec gravité (fermé durablement / avec salariés / reprise rapide), aisance numérique (faible / moyenne / forte, déduite du texte), canal, assureur.
## Cas limites et incertitudes
Ce que tu n'as pas pu déterminer.

RÈGLES STRICTES
- Chaque constat contient au moins 1 verbatim copié mot pour mot, avec le nom du fichier source. Ne reformule jamais un verbatim.
- Ne jamais inventer. Si une donnée manque : écris « non couvert par les entretiens ».
- Les comptages sont des nombres réels « X/50 » que tu as vérifiés. Pas de pourcentages statistiques.
- Reste descriptif : rapporte ce que les gens disent et font, ne prends aucune décision produit.
- Avant de répondre, vérifie que tu as bien lu les 50 fichiers et indique à la fin le nombre de fichiers lus.
```

---

## Prompt 2 : personas et JTBD (dans la même conversation, juste après la synthèse)

Ne donne à Gemini ni les personas ni les JTBD de Claude. Il construit les siens à partir de sa propre synthèse et du corpus.

```
À partir de ta synthèse et du corpus des 50 entretiens, produis maintenant deux livrables en Markdown.

LIVRABLE 1 : PERSONAS (2 à 3 maximum)
Méthode : segmente par GRAVITÉ DU SINISTRE croisée avec l'AISANCE NUMÉRIQUE (déduite du texte). Un segment = au moins 3 entretiens. Un cas isolé n'est pas un persona : classe-le en « cas limite ». Les 10 commerçants non sinistrés ne servent pas d'ancrage.
Pour chaque persona :
## [Prénom] : [étiquette courte]
- Profil (synthèse du segment, pas une personne réelle)
- Objectifs
- Frustrations
- Motivations / déclencheurs
- Contexte d'usage
- Citation représentative (verbatim exact)
- Ancrage : liste des fichiers d'entretien sources
Ajoute : ce que les personas partagent, les divergences à arbitrer, les cas limites.

LIVRABLE 2 : JOBS TO BE DONE
Format : « Quand [situation], je veux [motivation], afin de [résultat attendu] ». Aucune solution ni fonctionnalité dans un job. Classe-les en fonctionnels, émotionnels et sociaux.
Pour chaque job : le nombre d'interviewés concernés (X/50), au moins 1 verbatim exact avec le fichier source, les personas liés.

RÈGLES : aucun persona sans ancrage, aucun verbatim inventé, aucun trait non présent dans les données, pas plus de 3 personas, « non couvert par les entretiens » quand la donnée manque. Les données sont fictives. Précise à la fin les choix de segmentation que tu as faits et ceux dont tu n'es pas sûr.
```

Après réponse, enregistrer les trois sorties de Gemini dans `knowledge/uxr/outputs/gemini/` :
`synthese-commercants.md`, `personas.md`, `jobs-to-be-done.md`. Puis lancer `agent-challenger` (voir `.claude/agents/agent-challenger.md`).
