# PANTHER Family Review: PTHR47435

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47435 |
| **Family Name** | Glucosinolate-derived Nitrile Specifier (GlcNitrile_Specifier) |
| **Total Proteins** | 4,032 |
| **Taxonomic Breadth** | 3,754 taxa (1,545 proteomes) |
| **Subfamilies** | 9 |
| **Representative Structure** | 5A10 (Ta-TFP, thiocyanate-forming protein from *Thlaspi arvense*) |
| **Anchor gene** | *Thlaspi arvense* TFP (G1FNI6), subfamily PTHR47435:SF7 |

## Executive Summary

PTHR47435 is the plant **glucosinolate-breakdown specifier protein** family — the
non-hydrolytic accessory proteins of the Brassicales glucosinolate–myrosinase ("mustard
oil bomb") defence system. After a myrosinase (β-thioglucosidase, EC 3.2.1.147) hydrolyses
a glucosinolate, the unstable aglucone spontaneously rearranges to an isothiocyanate;
specifier proteins instead **capture the aglucone and redirect its rearrangement** toward
alternative products. The conserved core is a **Kelch-repeat six-bladed β-propeller**,
**non-heme Fe(2+) lyase** activity (carbon-sulfur lyase / sulfolyase, GO:0016846; EC
4.8.1.x) with a conserved central-pore **EXXXDXXXH iron-binding triad**
(mbudu2026biochemicalcharacterizationof; eisenschmidt-bonn2019; backenkohler2018).

Three biochemical sub-activities are distinguished by the product they favour:
- **NSP** (nitrile-specifier proteins) → simple **nitriles**
- **ESP** (epithiospecifier proteins) → **epithionitriles** (from alkenyl glucosinolates)
- **TFP** (thiocyanate-forming proteins) → organic **thiocyanates**

Evolutionarily, **NSP activity is ancestral**, **ESPs arose monophyletically from NSPs**,
and **TFP activity evolved convergently** in multiple Brassicaceae lineages
(kuchernig2012evolutionofspecifier). This convergence is visible in the family tree itself:
the two TFP-named members here fall in **different** subfamilies (*Thlaspi* TFP in SF7,
*Lepidium* TFP in the ESP subfamily SF2), consistent with independent acquisition of
thiocyanate-forming activity rather than common descent of "TFP".

**Key annotation caveat (family-level over-propagation risk):** the family is plant-specific
in function, but PANTHER PTHR47435 also contains a **fungal Kelch-repeat outlier** —
*Verticillium dahliae* KeR1 (G2XER2, SF4). Fungi have **no glucosinolates and no myrosinase
system**, so any electronic/phylogenetic propagation of glucosinolate-pathway terms
(e.g. GO:0019760 glucosinolate metabolic process, GO:0019762 glucosinolate catabolic
process, GO:0080028 nitrile biosynthetic process) to KeR1 would be **biologically incorrect**.
KeR1 should be treated as an uncharacterised Kelch-repeat protein, not a specifier protein.

## Conserved core function

| Aspect | Assignment | Notes |
|--------|------------|-------|
| **Molecular function** | carbon-sulfur lyase activity (GO:0016846); EC 4.8.1.x | Fe(2+)-dependent specifier/sulfolyase that eliminates sulfate from the glucosinolate aglucone; historically (and still in many IEA pipelines) mis-described as "enzyme regulator activity" |
| **Biological process** | glucosinolate catabolic process (GO:0019762); nitrile biosynthetic process (GO:0080028) | product class (nitrile / epithionitrile / thiocyanate) varies by subfamily |
| **Cofactor** | Fe(2+) (non-heme), EXXXDXXXH central-pore triad | e.g. Ta-TFP E266/D270/H274 |
| **Structure** | Kelch-repeat six-bladed β-propeller; often homodimeric | rep. structure 5A10 |
| **Cellular component** | cytosol (GO:0005829) | acts where myrosinase-generated aglucones become available after tissue damage; no organellar targeting established |
| **Taxonomic scope (functional)** | Brassicales (glucosinolate-producing plants) | fungal/other members are family homologues without the plant defence role |

## Subfamily Analysis

Subfamily assignments are drawn from the curated reviewed members in `PTHR47435-entries.csv`.

### PTHR47435:SF7 — EPITHIOSPECIFIER PROTEIN (anchor subfamily)
**Representative members**: *Thlaspi arvense* **TFP** (G1FNI6).
**Function**: Thiocyanate-forming protein (Ta-TFP). Fe(2+)-dependent specifier that converts
allylglucosinolate (post-myrosinase) to allylthiocyanate and 3,4-epithiobutanenitrile;
the structural prototype of the family (PDB 5A10/5A11). Anchor for this review. TFP activity
here is convergent with the SF2 *Lepidium* TFP (see below).

### PTHR47435:SF2 — EPITHIOSPECIFIER PROTEIN
**Representative members**: *Arabidopsis thaliana* **ESP** (Q8RY71); *Lepidium sativum* **TFP**
(A1XLE2).
**Function**: Epithiospecifier proteins promoting epithionitrile formation from alkenyl
glucosinolates; AtESP is the canonical ESP. The *Lepidium* "TFP" co-classifying here (rather
than with *Thlaspi* TFP in SF7) supports the convergent origin of thiocyanate-forming activity.

### PTHR47435:SF5 — NITRILE-SPECIFIER PROTEIN 1-RELATED
**Representative members**: *Arabidopsis* **NSP1** (Q9SDM9), **NSP2** (O49326), **NSP3**
(O04318), **NSP4** (O04316).
**Function**: Nitrile-specifier proteins promoting simple-nitrile formation; represents the
inferred **ancestral** activity of the family. NSP2-NSP4 carry additional lectin-type
sequence relative to the minimal Kelch core.

### PTHR47435:SF3 — NITRILE-SPECIFIER PROTEIN 5
**Representative members**: *Arabidopsis* **NSP5** (Q93XW5).
**Function**: Nitrile-specifier protein; a short (single-domain) NSP.

### PTHR47435:SF4 — KELCH REPEAT PROTEIN (fungal outlier)
**Representative members**: *Verticillium dahliae* **KeR1** (G2XER2).
**Function**: Uncharacterised fungal Kelch-repeat protein. **Not** part of the plant
glucosinolate defence system (fungi lack glucosinolates/myrosinase). Flagged as the principal
target for over-annotation guarding — glucosinolate/nitrile GO terms must not be propagated
to this member.

## Annotation guidance / over-annotation assessment

1. **Molecular function should be a lyase, not a regulator.** Many IEA pipelines annotate
   these proteins with "enzyme regulator activity" (GO:0030234), reflecting the outdated view
   of specifier proteins as accessory modulators of myrosinase. Structural and biochemical
   work (eisenschmidt-bonn2019; backenkohler2018; mbudu2026) establishes them as **catalysts
   — Fe(2+)-dependent carbon-sulfur lyases (GO:0016846, EC 4.8.1.x)**. Prefer the lyase term;
   the gene-level *Thlaspi* TFP review (THLAR/TFP) MODIFYs GO:0030234 → GO:0016846 on this basis.

2. **Product-class BP terms are subfamily-specific.** NSP→nitrile, ESP→epithionitrile,
   TFP→thiocyanate. Family-wide IBA of a single product term (e.g. only nitrile biosynthesis)
   under-describes ESP/TFP members; conversely thiocyanate-formation should not be propagated
   to NSP-only members.

3. **Do not propagate glucosinolate-pathway terms to non-Brassicales members** (notably the
   fungal SF4 KeR1). Glucosinolate metabolic/catabolic process and nitrile biosynthetic
   process are valid only for the plant defence context.

4. **Localization** is cytosolic for the characterised plant members; no organellar (nuclear,
   chloroplast) localization is supported — guard against AtSubP/TreeGrafter-style predicted
   compartments.

## Anchor gene cross-reference

This family review is anchored on *Thlaspi arvense* **TFP** (G1FNI6), reviewed at
`genes/THLAR/TFP/TFP-ai-review.yaml`, whose curation decisions (lyase MF; cytosolic
localization; glucosinolate catabolic + nitrile biosynthetic BP) are consistent with and
generalised by this family-level assessment.

## References

Supporting evidence is summarised in the family deep-research report
`interpro/panther/PTHR47435/PTHR47435-deep-research-falcon.md` (Falcon/Edison, 34 citations),
which draws on:
- Kuchernig et al. 2012 — evolution of specifier proteins (NSP ancestral; ESP monophyletic;
  TFP convergent).
- Eisenschmidt-Bönn et al. 2019 (PMID:30900313) — structural diversification of glucosinolate
  breakdown; specifier proteins as Fe(2+)-dependent lyases.
- Backenköhler et al. 2018 — iron as an essential cofactor of specifier proteins.
- Mbudu et al. 2026 — biochemical characterization of specifier proteins (Kelch β-propeller,
  EXXXDXXXH triad).
- Wei et al. (Ta-TFP crystal structure, PMID:26260516) — representative structure 5A10.
