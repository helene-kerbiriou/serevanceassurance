# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Static HTML/CSS/JS, single standalone file (confirmed by the user). No framework. Figma and FigJam are forbidden by the hackathon brief.

## Users
Primary: shopkeepers (commerçants) hit by the riots, filing and following a claim with their insurer Sérévance Assurances. Three personas from 50 synthetic interviews (`knowledge/uxr/outputs/final/personas-final.md`):
- **Élise**, shop closed for 3+ weeks, cash-strapped. Job: get a first payment fast and a date.
- **Yanis**, equipped, quick back to business. Job: declare once, know the date of every step, have his own data accepted as proof.
- **Odile**, long-standing neighbourhood shopkeeper, low digital ease, leans on her agent. Job: a named human, a canal she controls.
Secondary (not in the first prototype): the claims handler (gestionnaire), the agent or broker, the expert.

## Product Purpose
"Rouvrir d'abord": a relationship layer between a shopkeeper and the insurer after a claim. The promise: **a named human, a date, a first aid**. The claim is a moment, not a file: the goal is to reopen the shop, settlement follows. Success: the merchant knows who handles the claim, when the next step happens (as a range), and whether a first payment is on its way, without having to chase.

## Positioning
A relationship product, not a claims portal. Every screen names a person and a date. The insurer proposes, a human handler decides: no automatic promise of a deadline, no automatic payout, no robot deciding an indemnity.

## Operating Context
Hackathon "Design <> IA", 2 hours, team of three product designers, pitch of 10 to 15 minutes. All interview data is synthetic (fictional). Merchants use a phone, often in the shop after the incident, sometimes with an agent on the phone instead of the app.

## Capabilities and Constraints
Prototype scope confirmed by the user: **merchant claim declaration** and **merchant claim follow-up** (US-01 to US-15 in `knowledge/pm/outputs/us.md`). Out of scope for this prototype: gestionnaire view, agent view.
Constraints from the insurers (`knowledge/pm/outputs/features.md`, G1 to G6): dates are ranges validated by a handler, never firm promises; the product proposes and the handler decides; no chatbot for indemnity decisions; the agent is never bypassed; data shared with explicit consent; a human fallback (direct number, callback) at every important step.
Undecided (working hypotheses, to display as hypotheses): first-aid amount and rules, wording of the coverage message, agent rights.

## Brand Commitments
- Name shown in the product: **Sérévance** (the insurer's own mark, no separate product name).
- Binding visual constraint volunteered by the user: use `severance.md` (Lumon / Severance theme) as the design layer.
- Binding voice, stated by the user: **very human tone of voice**, to bring humanity into an institutional-looking system. The product speaks as a named person, not as an institution.

## Evidence on Hand
All data is fictional and must be labelled synthetic: merchants, handlers, agents, dates. Real interview quotes are in `knowledge/uxr/inputs/txt/` (synthetic corpus). No real customers, no real policies, no real amounts. The 5,000 euro advance ceiling comes from one insurer interview and is only an example value.

## Product Principles
1. A person, then a date: every state names who is in charge and when the next step is expected, as a range.
2. The human decides: the product proposes, a named handler validates anything that engages the insurer.
3. Ask once: never request information already given; never require an amount the merchant cannot know.
4. Never leave anyone alone with a screen: a direct number or a callback is always one step away.
5. Honest about what is not known: say "to be confirmed" and when the answer comes, instead of "in progress".

## Accessibility & Inclusion
Odile has low digital ease: large touch targets, plain language, no jargon, phone fallback. The merchant is stressed and tired: short screens, one task at a time, no time pressure. WCAG AA contrast is required (small text on Terminal Blue fails AA, use Severed Green or Lumon Black). Never use red decoratively.
