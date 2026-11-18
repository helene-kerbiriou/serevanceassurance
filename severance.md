# Severance / Lumon Industries : Website Theme Guide

## Overview
This theme draws from the visual world of Severance (Apple TV+), specifically the design language of Lumon Industries. The aesthetic has been described by production designer Jeremy Hindle as a blend of mid-century modernism, brutalist corporate architecture, and retrofuturism : a world that feels simultaneously vintage and unplaceable in time. The goal is to evoke a sense of quiet authority, institutional calm, and subtle unease. Clean without being cold. Orderly without being obvious.

The guiding emotion: familiar, yet slightly wrong.

## Design Style Names
The style sits at the intersection of several named movements:

- **Mid-Century Corporate Modernism** : the dominant mode; think Bell Labs, IBM offices of the 1960s–70s, Dieter Rams-era product design. Hindle and director Ben Stiller independently converged on Eero Saarinen and Kevin Roche as the primary architectural influences.
- **Late International Style** : emphasis on volume over mass, lightweight industrial materials, rejection of ornament and color, repetitive modular forms, flat surfaces alternating with glass. The Severance aesthetic lands in the style's twilight period (~1979–82), when cookie-cutter execution had turned its clean rationalism into something suffocating and inhuman.
- **Brutalist Minimalism** : heavy, unadorned surfaces; architecture that communicates power through simplicity and mass. Monumental concrete volumes and repetitive modular geometry.
- **Cassette Futurism** : a subset of retrofuturism describing an alternate present where technology stayed analog. Round glass monitors, integrated trackballs, archaic-looking personal computers that feel both dated and advanced. The 1970s–80s vision of computing that never quite arrived.
- **Corporate Institutionalism** : the visual grammar of government facilities, medical research labs, and large bureaucratic organizations.
- **Liminal Space** : the eerie emptiness of transitional, depopulated architecture. Corridors and rooms that feel like office-furniture catalog photos from 1979 that nobody actually worked in.
- **Cult Branding** : everything feels proprietary, self-contained, and slightly devotional; no external brands exist in this world.

## Color Palette

### Primary Colors
| Name | Description | Hex Approximate |
|---|---|---|
| Lumon White | Flat, cool white, not warm, not stark. The white of institutional walls and lab coats. | #F0F0EE |
| Severed Green | The signature MDR department carpet color. A deep, slightly muted olive-teal, evocative of both grass and government. | #4A6B5A |
| Corridor Gray | The dominant neutral. A blue-tinged gray for walls, panels, and large UI surfaces. | #9AA3A8 |
| Terminal Blue | The cool, slightly desaturated blue of the MDR computer screens and the sofa upholstery. | #5B7B9A |
| Lumon Black | Used sparingly. Very dark blue-gray, not pure black. Found on countertops and equipment trim. | #1E2328 |

### Secondary / Accent Colors
| Name | Description | Hex Approximate |
|---|---|---|
| Kier Gold | A muted, bureaucratic gold used for corporate seals, icons, and moments of institutional "reward." | #B89A5A |
| Break Room Teal | A slightly brighter, more saturated teal, used in moments of controlled positivity (like a motivational poster). | #3D7A72 |
| Waxy Cream | The off-white of Lumon paperwork, nameplates, and Dieter Rams-style product surfaces. | #E8E4D9 |
| Alert Red | Flat, institutional red, used only for errors, warnings, and high-stakes UI moments. Never decorative. | #C0392B |

### Usage Principles
- Backgrounds should use Lumon White or Corridor Gray exclusively. No gradients.
- Text should use Lumon Black on light surfaces or Lumon White on dark surfaces. High contrast, no mid-tone text colors.
- Accent colors (gold, teal) are used with extreme restraint, appearing perhaps once per screen.
- Never use warm colors (orange, yellow, red) for anything ambient or decorative. They are reserved for anomalies and alerts.

## Typography

### Philosophy
Type in this world is functional, impersonal, and authoritative. It communicates institutional trust, not personality. Every word feels like it was approved by a committee before being printed.

### Recommended Fonts
- **Primary / UI:** A geometric sans-serif with mid-century proportions, e.g., Helvetica Neue, IBM Plex Sans, Aktiv Grotesk, or Suisse Int'l. Slightly wider letterforms preferred over compressed ones.
- **Secondary / Body:** A clean, neutral grotesque: Inter, DM Sans, or Work Sans. Should feel like it came from an office memo.
- **Monospace / Data:** For terminal-style elements, numbers, and code: IBM Plex Mono or Courier Prime. This signals "Lumon-made technology."
- **Display / Headers:** Same as primary font, but set in all-caps with generous letter-spacing (tracking ~0.1–0.2em). No decorative or serif fonts unless used as a propaganda-style counterpoint.

### Type Treatment
- Hierarchy is established through weight and size, not through color or decoration.
- Line heights should be generous: copy should breathe.
- All-caps labels with wide tracking for section headers, navigation, and button labels.
- Numbers and data should appear in monospace to evoke terminal readouts.

## Spatial Design Notes
The physical spaces of Lumon inform the digital layout language:

- 26 shades of white were tested to find the exact wall tone: flat, cool, institutional.
- Corridors subtly shift in width as they progress, creating subliminal disorientation.
- Low ceilings compress the vertical dimension, producing claustrophobia.
- Vast open rooms with a single cluster of desks marooned in the center emphasize isolation and surveillance. Four workstations share a central pillar in the MDR department.
- Generic furniture: Blu Dot Daily Task Chairs (2016), contemporary yet anonymous, chosen to evoke corporate sameness. Metallic office furniture reinforces the institutional tone.
- Pressable divider walls between departments can be physically manipulated: boundaries exist but are not permanent.

### Spacing & Layout
- Generous whitespace: rooms in Lumon are conspicuously empty. UI should feel the same.
- Prefer wide, low containers over tall vertical stacking. Echoes the horizontal layout of the MDR office.
- Consistent, rigid grid. Nothing should feel organically placed: every element implies deliberate positioning by an unseen authority.
- Content should never feel crowded. If in doubt, add more space.
- Centered layouts for hero/focal elements; left-aligned for content.

## Visual Texture & Surface
- Flat surfaces: no drop shadows on UI elements unless absolutely necessary for depth. Shadows, when used, should be very subtle and cool-toned (blue-gray, not warm).
- No gradients. All fills are solid.
- Matte over glossy. Inspired by matte paint finishes, linoleum floors, and powder-coated metals.
- Subtle texture can be applied to large background areas: very faint noise or a barely-visible grid pattern, like institutional ceiling tiles or wall panel seams.
- Borders and dividers should be thin, single-pixel lines in a slightly lighter or darker tone than the surface. Never bold or decorative.

## Imagery & Iconography

### Photography Style
- Desaturated and cool-toned. Images should feel like they were shot under fluorescent light.
- Wide-angle, symmetrical compositions. Subjects should feel slightly small within their environment: the architecture dominates.
- No natural light, or if present, it appears distant and inaccessible (a window that cannot be opened).
- Subjects are posed with deliberate stillness: not candid, never chaotic.

### Illustration / Icons
- Line icons should be thin-stroked, geometric, and sans-serif in spirit: nothing rounded or playful.
- Iconography should suggest function over identity. No personality, no "fun" icons.
- Inspired by the visual grammar of mid-century corporate signage, government wayfinding, and early computing interfaces.
- Motivational or branded graphic elements (if used) should evoke the unsettling positivity of Lumon's in-office propaganda posters: simple, flat, institutional.

## Motion & Interaction
- Slow and deliberate transitions. Nothing snappy or energetic.
- Prefer linear or ease-in-out easing with slightly longer durations (300–500ms) over quick, springy animations.
- Page transitions, if used, should feel like doors opening or closing: a slow reveal, not a slide or bounce.
- Hover states: subtle color shifts, never movement.
- Loading states should feel like a terminal booting up: perhaps a blinking cursor or sequential character reveal.
- No parallax. No physics-based animation. The world of Lumon does not move loosely.

## UI Component Personality
- **Buttons:** Flat, rectangular (no rounded corners, or only very slightly rounded: 2px max). All-caps labels. Generous padding. Primary actions in Lumon White on Terminal Blue or Severed Green. Secondary actions are outlined.
- **Forms:** Inputs should look like fields on an institutional form. Clean borders, no floating labels. Placeholder text should read like a directive, not a suggestion.
- **Cards / Panels:** No drop shadows. Thin borders or slight background color changes to delineate. Content should feel like it belongs in a manila folder or a corporate binder.
- **Navigation:** Horizontal, understated, all-caps, widely tracked. No hamburger menus if avoidable: suggest permanence and institutional structure.
- **Tables & Data:** Inspired by Lumon's terminal readouts. Monospace numbers, thin row dividers, no zebra stripes (prefer a faint hover highlight instead).

## Tone & Voice (Copywriting Complement)
The visual theme should be matched by copy that is:

- Precise and formal, never casual. Contractions are acceptable but rare.
- Passive-voice-adjacent: authority comes from the institution, not a person.
- Subtly benevolent but ambiguous: like an employee handbook that sounds helpful but tells you very little.
- Avoids exclamation points. Periods only.
- Example headline register: "Your work is meaningful. Your contribution is valued."

## Reference Points

### Architecture & Interior Design
- Bell Labs Holmdel Complex, NJ (Eero Saarinen & Kevin Roche, 1962): filming location for Lumon's exterior, lobby, and atrium; the single most important architectural reference.
- John Deere World Headquarters (Saarinen, 1964): informed the interior workstation design; Hindle described it as "powerful" and "dominant," with custom-made desks that belong to the space.
- Burolandschaft concept / Herman Miller Action Office: the open-plan office system precursors that Lumon's MDR department distorts into something alienating.
- 1970s IBM offices: the corporate technology aesthetic and product design language.

### Product & Material Design
- Dieter Rams / Braun product design: the definitive material reference for objects, equipment, and UI components.
- 70s-era office furniture catalogs: the idealized workspace imagery that no real office matched, but that we collectively "remember."

### Photography & Graphic Art
- Lars Tunbjörk and Lynne Cohen's empty office photography: the emotional register of space.
- Soviet-era workplace murals: the propaganda-positive graphic language.

### Film & Media
- 2001: A Space Odyssey (Kubrick, 1968): the primary cinematic reference per Hindle: "really 2001 as an office."
- Playtime (Jacques Tati, 1967): dystopic corporate architecture; the comedy of humans dwarfed by rationalist glass-and-steel environments.
- A Clockwork Orange (Kubrick, 1971): the uncanny domestic interior pushed into institutional space.
- Brazil (Gilliam, 1985): bureaucratic dystopia and retro-futurist office technology.

This theme is designed to feel like it was created by someone who has never left the building and sees nothing wrong with that.
