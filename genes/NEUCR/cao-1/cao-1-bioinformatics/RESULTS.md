# CAO-1 substrate specificity: structural analysis of the co-crystal H-bond network

## Objective

Test whether the CAO-1 (Q7S860) co-crystal structures **explain** the empirical substrate
specificity reported by Díaz-Sánchez et al. 2013 (PMID:23893079): CAO-1 cleaves resveratrol and
piceatannol but not trans-stilbene, 4-monohydroxystilbene, pinosylvin (3,5-diOH), trismethoxy-
resveratrol, or a 4′-methoxy-stilbene glucoside — the authors concluding a requirement for "a minimal
number of unmodified hydroxyl groups."

## Method

Analysis of **existing** co-crystal structures (not de-novo docking):
- **5U90** — Co-CAO1 · resveratrol (PDB ligand `STL`)
- **5U97** — Co-CAO1 · piceatannol (PDB ligand `PIT`)

For each ligand oxygen we enumerate protein polar atoms (N/O), water, and metal within
H-bonding distance (≤3.5 Å), and measure the scissile interphenyl alkene relative to the active-site
metal. Reproducible: `uv run python analyze_specificity.py` → `hbond_contacts.tsv`.

Note: these are **cobalt-substituted** structures (catalytically inert Co(II) replaces the native
Fe(II) so a Michaelis-like substrate complex can be trapped for crystallography); the substrate
poses are taken as representative of the productive binding mode.

## Result: a two-ring-anchor recognition model

Ligand O···O distances confirm the ring assignment (O2–O3 = 4.8 Å, meta on the resorcinol ring;
O1 is ~11 Å away on the opposite ring; O1–OAD = 2.8 Å, adjacent on that ring):

| Ligand OH | Ring / position | Protein H-bond partners (distance) |
|---|---|---|
| **O1** | ring A, **4′-OH** | **Tyr133-OH (2.5 Å) + Lys164-NZ (2.6 Å)** — bidentate anchor |
| O2 | ring B, 3- or 5-OH | water (2.5 Å) — water-mediated only |
| **O3** | ring B, 3- or 5-OH (resorcinol) | **Glu383-OE2 (2.7 Å)** (+ His313-ND1) — acidic anchor |
| OAD (piceatannol only) | ring A, **3′-OH** | Thr151-OG1 (2.8 Å) (+ Lys164, Asn150) — bonus H-bond |

The shared 3,5,4′ hydroxyls contact identical residues in both structures; piceatannol's extra 3′-OH
adds a Thr151 H-bond (independently matching the Sui et al. 2017 text). The scissile alkene (C7=C8)
sits **~4.6 Å from the metal** — reproducing the "substrates bind ~4.7 Å from the iron" statement in
PMID:28493664. The recovered binding residues (positions **133, 164, 383**) match the UniProt
`BINDING` annotations exactly, validating the pipeline.

**Interpretation:** productive binding uses **two anchors on opposite rings** — a 4′-OH → Tyr133/Lys164
(ring A) and a 3/5-OH → Glu383 (ring B) — which together clamp the substrate with its interphenyl
double bond positioned over the metal/O2 site.

## This explains the empirical SAR

| Compound | 4′-OH (ring A / Tyr133-Lys164) | 3or5-OH (ring B / Glu383) | Predicted | Observed (PMID:23893079) |
|---|---|---|---|---|
| resveratrol (3,5,4′) | ✓ | ✓ | cleaved | **cleaved** ✓ |
| piceatannol (3,5,3′,4′) | ✓ (+3′→Thr151) | ✓ | cleaved | **cleaved** ✓ |
| 4-hydroxystilbene (4′) | ✓ | ✗ | not cleaved | **not cleaved** ✓ |
| pinosylvin (3,5) | ✗ | ✓ | not cleaved | **not cleaved** ✓ |
| trans-stilbene (none) | ✗ | ✗ | not cleaved | **not cleaved** ✓ |
| trismethoxy-resveratrol | blocked | blocked | not cleaved | **not cleaved** ✓ |
| 4′-methoxy-stilbene glucoside | blocked (4′-OMe) | blocked (glycoside) | not cleaved | **not cleaved** ✓ |

The two-anchor model accounts for **all seven** panel compounds. Crucially it resolves the puzzle the
gene-review text flagged: a free 4′-OH is *necessary but not sufficient* — 4-hydroxystilbene has the
4′-OH (ring A anchor) yet is not cleaved because it lacks a ring-B (Glu383) anchor. So the requirement
is not "a 4′-OH" per se but **a hydroxyl on each ring** engaging the two anchors, which is why ≥2 well-
placed free hydroxyls are needed and fully-blocked stilbenes fail.

## Status of the claim (important)

This is a **retrospective structural rationalization**, not a validated predictor:
- Only the two **substrates** were co-crystallized; the five **non-substrates were not** — their loss
  of anchors is inferred from which hydroxyls are absent/blocked, not observed.
- No docking or binding-energy calculation was performed; this is H-bond geometry only.
- Co(II)-substituted structures; single active-site copy (chain A) analyzed.

So the honest status advances from "empirical + structure-consistent" to **"structure-explained"** —
the co-crystals contain a coherent two-anchor mechanism that reproduces the entire SAR — but a
predictive test would require docking/assaying the non-substrates (and diagnostic new probes below).

## Falsifiable predictions
- **4,4′-dihydroxystilbene** and **3,4′-dihydroxystilbene** (one OH per ring, both anchors satisfiable)
  should be cleaved, unlike the single-ring pinosylvin/4-hydroxystilbene.
- **Tyr133Phe / Lys164 / Glu383 mutants** should selectively abolish cleavage of substrates relying on
  the corresponding anchor.

## Provenance
- Structures: RCSB 5U90, 5U97 (Sui et al. 2017, PMID:28493664).
- Empirical SAR: Díaz-Sánchez et al. 2013 (PMID:23893079); non-substrate list per UniProt Q7S860.
- Script + raw contacts: `analyze_specificity.py`, `hbond_contacts.tsv` (this folder).
