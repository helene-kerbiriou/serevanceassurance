# Benchmark consolidé : humaniser la relation assureur ↔ commerçant sinistré

> Objectif : alimenter les choix produit et le ton de Sérévance ("Rouvrir d'abord" : un humain nommé, une date, une première aide).
> Date : 2026-11-18. Recherche web faite dans la session ; les compléments marqués 🔎 viennent de la connaissance générale et sont **à vérifier avant le pitch**.
> Les données de nos personas sont synthétiques ; ce benchmark, lui, porte sur des acteurs réels.

## 1. En une page

| Ce que montre le marché | Pourquoi ça compte pour Sérévance |
|---|---|
| Rockfi vend la **personne** avant l'offre : photo, nom, ville, rendez-vous de 30 min. | Notre promesse "un humain nommé" a un modèle d'exécution éprouvé. |
| Bpifrance donne **montant, durée, conditions, démarche** en une fiche, sans jargon d'assureur. | Les commerçants comparent implicitement notre aide à celle-ci : clarté et rapidité sont l'étalon. |
| Alan cadre son ton par trois mots (légèreté, attention, ludique sans être comique). | Il nous faut un cadre équivalent, mais calibré pour des gens **stressés**, pas pour des gens en bonne santé. |
| Le suivi de colis et les assurtechs montrent le **suivi par étapes** et la déclaration par photo. | Ce sont des modèles mentaux que Yanis possède déjà. |

**Tension de design à assumer** : `severance.md` (thème Lumon) est volontairement froid, institutionnel, "passif et sans personne". Tous les benchmarks chaleureux font l'inverse. Notre produit est donc un **contraste voulu** : l'habillage institutionnel porte une voix très humaine. C'est cohérent avec PRODUCT.md, mais ça doit être dit au pitch, sinon ça passera pour une incohérence.

## 2. Les benchmarks demandés

### 2.1 Rockfi (gestion privée, France) : la proximité mise en scène

Source : lecture de https://www.rockfi.fr (page d'accueil uniquement) + presse.

**Ce qu'ils font**
- Titre : « La nouvelle gestion privée. » ; sous-titre : « Pensez-nous comme un Family Office moderne… ».
- Vouvoiement systématique, « nous » pour l'entreprise, « je » **uniquement** dans les citations d'associés nommés.
- Proximité = **preuves concrètes**, pas adjectifs : grille d'environ 40 conseillers avec photo, nom et ville ; 18 bureaux ; pages par ville ; « Trouver votre conseiller » ; « Nos conseillers près de chez vous ».
- Confiance = transparence : « Un taux fixe pour un conseil objectif » (~1 % des encours), « La stratégie avant les produits », mentions ORIAS / ACPR / AMF en pied de page.
- Un seul CTA répété partout : « Prendre rendez-vous » et « Planifier 30 min d'échange ». Le rendez-vous est cadré : **un premier échange de 30 minutes**.
- Chiffres de crédibilité : 1 Md€ conseillé, 1 500 familles, 15 ans d'expérience moyenne.

**À retenir pour Sérévance**
1. **Nommer + photographier + localiser** la personne qui suit le dossier (on le fait déjà dans le prototype ; ajouter ville ou agence).
2. **Cadrer l'interaction dans le temps** ("un appel de 10 min", pas "contactez-nous").
3. **Un seul CTA humain** répété à chaque étape importante.
4. Montrer la transparence sur "comment on décide" (notre G2 : l'humain décide) comme Rockfi le fait sur ses frais.

**À ne pas copier**
- Registre luxe / patrimoine ("Family Office", "philanthropie") : trop lointain d'Odile.
- Aucun numéro de téléphone visible en accueil : pour nous, le numéro direct doit être visible (principe 4).
- Les affirmations de proximité et de satisfaction sont **auto-déclarées** ; je n'ai trouvé aucun avis client indépendant.

⚠️ Piège rencontré : rockfi.com est une entreprise américaine sans rapport. Le bon site est rockfi.fr.

### 2.2 Bpifrance : Prêt Solidarité Commerce : l'aide lisible

Sources : legifiscal.fr, selectra.info, boursedescredits.com, les-aides.fr (une seule source quasi officielle repérée ; **à confirmer sur bpifrance.fr**).

**Ce que c'est** (et oui, c'est bien le bon objet pour nous) : un prêt à taux zéro pour les entreprises individuelles, TPE et PME du commerce **sinistrées par les dégradations des 17-18 octobre 2026**.
- 5 000 à 50 000 €, 36 mois, différé de remboursement du capital 12 mois, sans sûreté personnelle ni réelle.
- Usage : reconstituer les stocks, faire face aux échéances immédiates.
- Éligibilité signalée : entreprise commerciale de plus d'un an, 12 mois de comptabilité (sources divergentes).
- Plateforme dédiée ouverte le 23 octobre 2026 ; numéro d'assistance 0 806 807 807.

**À retenir**
1. **Une fiche = 5 chiffres** (montant, durée, différé, garanties, usage). Notre "première aide" doit pouvoir se dire pareil : combien, quand, à quelles conditions.
2. **Plateforme dédiée et ouverte vite** (6 jours après l'événement) : la rapidité d'ouverture est un message en soi.
3. **Numéro d'assistance affiché** : même logique que notre repli humain.
4. Le public est nommé précisément ("entreprises individuelles, TPE, PME du commerce") : parler à *ce* commerçant.

**Ce que ça change pour notre produit**
- Le commerçant a **déjà** une aide à taux zéro sur la table. Notre première aide n'est pas seule : il faut l'**articuler** (une section "autres aides auxquelles vous pouvez prétendre" serait un vrai plus, hypothèse à valider).
- Contrairement à un prêt, notre avance est une **indemnité** : ne pas laisser croire que c'est un crédit, et inversement.
- Le montant d'avance de 5 000 € (un seul entretien assureur) est **à comparer** à la fourchette Bpifrance 5-50 k€ avant de le présenter comme "rapide et suffisant".

**À ne pas copier** : un parcours en ligne pur sans humain nommé (la demande passe par une plateforme ; aucun interlocuteur personnel n'est mis en avant).

### 2.3 Alan : la chaleur cadrée

Sources : Selectra, Clubic, TechCrunch, blog Alan (mascotte). Je n'ai trouvé ni guide de style ni analyse détaillée des messages dans l'app ; **tester l'app** pour compléter.

**Ce qu'ils font**
- Promesse : assurance "ultra-réactive" dans une app unique ; ligne directe 7j/7 avec des professionnels de santé.
- Ton cadré par trois mots : *légèreté, attention, ludique mais pas comique* ; mascotte "assez douce pour être chaleureuse, assez joueuse pour être la nôtre".
- Avis utilisateurs : app intuitive, service client réactif ; **réserve** : le canal vocal reste indirect (demande de rappel depuis le chat, parfois plusieurs jours).

**À retenir**
1. **Définir la voix en 3 mots maximum** et les utiliser comme filtre de relecture.
2. L'humain réactif est la preuve de la chaleur, pas l'illustration.
3. La faiblesse relevée (rappel qui traîne) est exactement notre principe 5 : **si on promet un rappel, on donne sa fenêtre horaire**.

**À ne pas copier** : le "ludique" et la mascotte. Pour un commerçant qui a perdu son stock, l'humour est un risque. Notre registre est plutôt : *présent, calme, précis*.

### 2.4 Sidecar : 🔎 identification incertaine

La recherche ne trouve pas d'"app d'assurance Sidecar". Le plus proche est **Sidecare** : un **néo-courtier** (services gratuits pour le client, rémunéré par les assureurs) centré sur les contrats collectifs et la gestion RH (affiliations, DUE, suivi S/P, application mobile) ; le contenu est B2B, sans détail produit exploitable.
**→ À confirmer avec vous** : est-ce bien Sidecare, ou un autre acteur (Lovys, Leocare, Luko, Acheel…) ? En attendant, la section 3 couvre les néo-assureurs mobiles.

## 3. Compléments proposés (pour élargir au-delà des 4)

Rappel : 🔎 = à vérifier.

| Acteur | Pourquoi | Pattern réutilisable |
|---|---|---|
| **Lovys / Leocare / Luko** (néo-assureurs mobiles) | Source de la recherche : déclaration de sinistre dans l'app avec photos et vidéos. | Déclarer **une fois**, par photo, sur mobile (notre principe 3 "ne demander qu'une fois"). |
| **Lemonade** 🔎 | Référence mondiale de la déclaration rapide ; l'IA instruit une partie des sinistres. | À regarder comme **contre-modèle** pour notre G2 : on veut l'humain qui décide, eux automatisent. Utile pour justifier notre positionnement. |
| **Suivi de colis (La Poste, Chronopost, Vinted)** 🔎 | Modèle mental universel du suivi par étapes avec date estimée. | Frise d'étapes + **fenêtre de date**. Nos "plages de dates" ressemblent à "livraison prévue entre le 20 et le 22". |
| **Qonto** 🔎 | Néobanque TPE : ton direct, support humain facilement joignable, interface sobre pour dirigeants pressés. | Prouve que le **sobre et institutionnel peut être humain** : bon argument pour garder le thème Lumon. |
| **Doctolib** 🔎 | Prise de rendez-vous avec un professionnel nommé, rappels, annulation simple. | Prise de **créneau d'appel** avec le gestionnaire nommé. |
| **Pennylane / Indy** 🔎 | Outils comptables TPE : justificatifs importés automatiquement. | Réutiliser les **données déjà détenues** comme preuve (besoin de Yanis). |

## 4. Matrice comparative

| Critère | Rockfi | Bpifrance PSC | Alan | Néo-assureurs (Lovys…) | Suivi colis | **Sérévance (cible)** |
|---|---|---|---|---|---|---|
| Humain nommé | ✅ photo + nom + ville | ❌ plateforme | 🟡 équipe soignante, pas toujours nommée | ❌ | ❌ | ✅ **obligatoire** |
| Date / délai annoncé | 🟡 "30 min" | ✅ 36 mois, 12 de différé | 🟡 "réactif" | 🟡 | ✅ | ✅ plage validée |
| Chiffres clés lisibles | ✅ | ✅ 5 chiffres | 🟡 | 🟡 | ✅ | ✅ |
| Repli humain visible | 🟡 RDV, pas de tél. en accueil | ✅ n° d'assistance | 🟡 rappel parfois lent | ❌ | ❌ | ✅ n° direct + rappel avec fenêtre |
| Ton | Posé, vouvoiement, sobre | Administratif | Chaleureux, léger | Léger | Neutre | **Présent, calme, précis** |
| Transparence sur la décision | ✅ frais fixes | ✅ conditions | 🟡 | 🟡 | n/a | ✅ "l'humain décide" |
| Adapté à un stress élevé | ❌ (cible aisée) | 🟡 | ❌ (léger) | 🟡 | ✅ | ✅ à concevoir |

## 5. Principes réutilisables (liés à PRODUCT.md)

| Principe PRODUCT.md | Preuve du benchmark | Règle de design / copy |
|---|---|---|
| 1. Une personne, puis une date | Rockfi (grille nommée), colis (date) | Chaque écran : prénom + fonction + ville, et "d'ici le X–Y". |
| 2. L'humain décide | Rockfi (transparence), Lemonade (contre-modèle) | Verbes d'action au nom du gestionnaire : "Camille examine votre dossier". Jamais "le système a décidé". |
| 3. Demander une fois | Néo-assureurs, Pennylane | Pré-remplir ; accepter ses propres données comme preuve. |
| 4. Jamais seul devant un écran | Bpifrance (n° d'assistance), Rockfi (RDV) | Numéro cliquable + "Être rappelé entre 14 h et 16 h" à chaque étape. |
| 5. Honnête sur l'inconnu | Faiblesse d'Alan (rappel flou) | "À confirmer d'ici jeudi" au lieu de "en cours". |

## 6. Voix proposée (hypothèse à valider par l'équipe)

Trois mots : **présent, calme, précis**.
- *Présent* : une personne parle, avec son prénom. "Je" dans les messages d'un gestionnaire, "nous" pour Sérévance.
- *Calme* : pas d'exclamation, pas d'humour, pas de pression.
- *Précis* : chiffres, dates, plages. Aucun jargon d'assureur.

Vouvoiement (comme Rockfi et Bpifrance ; adapté à Odile).

| Au lieu de | Écrire |
|---|---|
| « Votre dossier est en cours de traitement. » | « Camille, votre gestionnaire, examine votre dossier. Elle vous répond d'ici jeudi ou vendredi. » |
| « Pièce justificative manquante. » | « Il nous manque une seule chose : la facture de la vitrine. Une photo suffit. » |
| « Une avance pourra être accordée selon conditions. » | « Camille étudie une première aide pour que vous puissiez rouvrir. Elle décide, et vous le dit d'ici vendredi. » |
| « Contactez le service client. » | « Appelez Camille au 01 XX XX XX XX, ou demandez à être rappelé entre 14 h et 16 h. » |

Ces exemples sont des **propositions** (noms et numéros fictifs).

## 7. Anti-patterns à éviter
1. Humour ou mascotte (Alan) dans un contexte de perte.
2. Registre luxe ou jargon financier (Rockfi) : "patrimoine", "stratégie", "accompagnement sur mesure".
3. Parcours 100 % plateforme sans interlocuteur nommé (Bpifrance).
4. Un rappel promis sans fenêtre horaire (reproche fait à Alan).
5. Une promesse de délai ferme (contraire à G1) : toujours une plage.
6. Une aide présentée comme un crédit, ou l'inverse.

## 8. Hypothèses et vérifications ouvertes
- Confirmer "Sidecar" (§2.4).
- Vérifier les conditions du Prêt Solidarité Commerce sur bpifrance.fr (sources divergentes sur l'ancienneté et la comptabilité).
- Tester l'app Alan et le parcours Lovys/Leocare pour passer de la presse à l'observation directe.
- Ne lire que la page d'accueil de Rockfi : les pages /nos-conseillers et /contact-conseiller sont à parcourir.
- Les lignes 🔎 de la section 3 viennent de la connaissance générale, non vérifiées dans cette session.
- Valider l'articulation avec les aides de l'État : hypothèse, pas décision.

## 9. Sources
- [Rockfi (site)](https://www.rockfi.fr)
- [Maddyness : Rockfi déploie ses ailes](https://www.maddyness.com/2024/04/23/gestion-privee-rockfi-deploie-ses-ailes-pour-adresser-un-marche-de-4-800-milliards-deuros/)
- [Maddyness : levée de 18 M€](https://www.maddyness.com/2025/03/24/gestion-privee-rockfi-leve-18-millions-deuros-et-vise-le-milliard-deuros-dactifs-sous-gestion-dici-fin-2026/)
- [Legifiscal : Prêt Solidarité Commerce](https://www.legifiscal.fr/actualites-fiscales/4711-pret-solidarite-commerce-pret-taux-zero-bpifrance-commercants-sinistres.html)
- [Selectra : prêt à taux zéro Bpifrance 50 000 €](https://selectra.info/finance/actualites/marche/commerce-pille-pret-taux-zero-bpifrance-50000)
- [Les-aides.fr : Prêt Solidarité Commerce](https://les-aides.fr/aide/dyB_IBwSTCTCFOMv/bpifrance/pret-solidarite-commerce.html)
- [Alan : blog mascotte](https://website-pages.alan.com/en/blog/discover-alan/a/how-our-mascot-came-to-life)
- [Selectra : avis Alan](https://selectra.info/assurance/assureurs/alan)
- [Sidecare : application mobile](https://www.sidecare.com/fonctionnalites-produits/application-mobile)
- [Moneyvox : offres low cost auto et habitation](https://www.moneyvox.fr/assurance/actualites/84945/mutuelle-assurance-auto-et-habitation-que-valent-les-offres-low-cost)
