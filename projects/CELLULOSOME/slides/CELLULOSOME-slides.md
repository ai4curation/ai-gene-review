---
title: "Cellulosome Project"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# The Cellulosome

### A giant extracellular multi-enzyme complex for degrading crystalline cellulose

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

# Why the cellulosome?

The cellulosome is a large extracellular multi-enzyme complex produced by anaerobic cellulolytic bacteria for efficient degradation of plant cell wall polysaccharides.

It is **one of the most efficient natural systems** for degrading crystalline cellulose and lignocellulosic biomass.

Motivations for study:

- **Biofuels / biorefinery** — consolidated bioprocessing for cellulosic ethanol
- **Industrial enzymes** — understanding synergistic enzyme action
- **Protein engineering** — modular architecture enables "designer cellulosomes"
- **Basic science** — model for supramolecular enzyme complexes
- **Synthetic biology** — engineering organisms for biomass conversion

---

# Cellulosome architecture

Three functional classes of components:

1. **Scaffoldins** — non-catalytic proteins containing cohesins that organize the complex
2. **Catalytic subunits** — enzymes containing dockerins that bind to cohesins
3. **Cell surface anchors** — proteins that attach the cellulosome to the cell wall

**Key assembly logic (cohesin–dockerin):**

- Type I dockerin (on enzymes) binds Type I cohesin (on the CipA scaffoldin)
- Type II dockerin (on CipA) binds Type II cohesin (on anchor proteins, e.g. SdbA / OlpB)

This modular system lets many enzymes be organized on one scaffold, then anchored to the cell surface.

---

# The approach: AI-assisted gene review

- Apply the AI gene review framework to systematically review existing GO annotations against the literature and bioinformatics.
- Each gene gets a structured review YAML; annotations are kept, modified, removed, or flagged as over-annotated.

**Primary model: *Acetivibrio thermocellus*** (formerly *Clostridium thermocellum*)

- UniProt code ACET2 (taxonomy ID 1515)
- The organism in which cellulosomes were discovered (as "cellulose-binding factor")
- Best-characterized system; ~79 cellulosomal genes
- Thermophilic (~60 °C) and industrially relevant

**Second model: *Clostridium cellulovorans*** (CLOCL) — mesophilic, produces both cellulosomal AND free cellulases (57 cellulosomal genes).

---

# Genes reviewed — *A. thermocellus* (1/2)

**Priority 1 — Scaffoldins and anchors (architectural, non-catalytic):**

| Gene | UniProt | Protein |
|------|---------|---------|
| cipA | Q06851 | Cellulosomal-scaffolding protein A |
| cipB | Q01866 | Cellulosomal-scaffolding protein B |
| sdbA | P71143 | Scaffolding dockerin binding protein A |
| ancA | Q06848 | Cellulosome-anchoring protein |

**Priority 2 — Key cellulases (GH-family enzymes):**

| Gene | Protein |
|------|---------|
| celS | Cellulose 1,4-beta-cellobiosidase CelS (GH48) |
| celK | Cellulose 1,4-beta-cellobiosidase CelK |
| celA / celC / celD | Endoglucanases A, C, D |
| celX (P15329) | Putative endoglucanase X |

---

# Genes reviewed — *A. thermocellus* (2/2)

**Priority 3 — Hemicellulases and other activities:**

| Gene | UniProt | Protein |
|------|---------|---------|
| xynY | P51584 | Endo-1,4-beta-xylanase Y |
| xynX | P38535 | Exoglucanase XynX |
| xghA | Q70DK5 | Xyloglucanase Xgh74A |
| licB | Q84C00 | Beta-glucanase (lichenase) |

**Priority 4 — Additional cellulosomal proteins:**

| Gene | UniProt | Protein |
|------|---------|---------|
| celE | P10477 | Cellulase/esterase CelE |
| xynZ | P10478 | Xylanase Z (with feruloyl esterase domain) |
| celM | P55742 | Putative aminopeptidase |

**All 17 *A. thermocellus* genes reviewed and validated.**

---

# Second model — *Clostridium cellulovorans*

Mesophilic complement to thermophilic *A. thermocellus*; produces both cellulosomal and free cellulases.

| Gene | UniProt | Protein |
|------|---------|---------|
| cbpA | P38058 | Cellulose-binding protein A (scaffoldin) |
| engK | Q9RGE8 | Glucanase/Endoglucanase K (GH9) |
| engL | Q9RGE6 | Endoglucanase L (GH9) |
| engO | Q6DTY2 | Endoglucanase O (GH9, **non-cellulosomal**) |
| hbpA | Q9RGE7 | Hydrophobic protein A (accessory scaffoldin) |

- CbpA scaffoldin: 9 cohesin domains and 4 SLH domains.
- Gene cluster: cbpA–exgS–engH–engK–hbpA–engL–manA–engM–engN.
- **All 5 genes reviewed and validated.**

---

# Finding: scaffoldins are non-catalytic — fix the annotations

Scaffoldins (cipA, cipB, sdbA, cbpA) organize the complex but **do not catalyze** cellulose degradation. Several IEA annotations were incorrectly propagated:

- **GO:0004553** (hydrolase activity) — incorrectly propagated from dockerin domains to non-catalytic scaffoldins → flagged
- **GO:0030246** (carbohydrate binding) — incorrectly attributed to cohesin domains, which bind **dockerins (proteins)**, not carbohydrates → flagged
- For CbpA: GO:0071555 (cell wall organization) marked for **REMOVAL**

**Recommended additions** to capture true function:

- GO:0043263 (cellulosome) — cellular component
- GO:0044575 (cellulosome assembly) — biological process
- GO:1990308 / 1990309 / 1990311 / 1990312 — specific cohesin–dockerin domain binding

---

# Finding: cellulases — right activity, sharpen the context

Cellulases (celS, celA, celC, celD, celK, celX) — annotations mostly correct. Recommendations:

- Add **GO:0043263** (cellulosome) as cellular component
- Add **GO:1990311** (type-I cohesin domain binding) for the dockerin function
- Mark overly general process terms (polysaccharide catabolic, carbohydrate metabolic) as **over-annotated**, in favor of specific **GO:0030245 (cellulose catabolic process)**

EngK / EngL (GH9, *C. cellulovorans*):

- Accepted GO:0008810 (cellulase activity), GO:0030245 (cellulose catabolic process)
- Added GO:0043263 (cellulosome), GO:1990311 (type-I cohesin domain binding)

---

# Finding: cellulosomal vs free — EngO is the contrast case

**EngO (Q6DTY2)** is a GH9 endoglucanase that is **NOT** part of the cellulosome:

- Lacks a dockerin; instead carries its own **CBM** for substrate targeting
- Functions as a **free secreted enzyme** that complements the cellulosome
- Added GO:0030248 (cellulose binding) for its CBM function
- **No** cellulosome annotations, unlike the dockerin-bearing EngK / EngL

This distinction — dockerin-anchored vs. free CBM-targeted — is exactly what GO annotations must capture correctly.

**HbpA (Q9RGE7)** — accessory scaffoldin: GO:0000272 (polysaccharide catabolic) marked for REMOVAL (non-catalytic); CBM-style GO:0030246 marked UNDECIDED (possible artifact); added type-I dockerin binding + cellulosome assembly.

---

# Challenges

- **Modular, multi-domain proteins** — a single protein mixes catalytic domains, dockerins/cohesins, CBMs, and SLH anchors; annotations get cross-propagated between domains incorrectly.
- **Complex assembly** — cohesin–dockerin interactions are protein–protein, not protein–carbohydrate; easy to mis-annotate as carbohydrate binding.
- **GO representation of multi-enzyme complexes** — capturing "cellulosome" as a component and "cellulosome assembly" as a process, distinct from the catalytic activities.
- **Data quality** — several literature-derived UniProt IDs mapped to the wrong organism (e.g. Q9RGE9 = cysN from *C. jejuni*; Q9L3K5 = cheA from *B. cereus*; P23661 = celB from *R. albus*) and had to be removed.

---

# Status and future directions

**Status — complete:**

- 17 *A. thermocellus* genes reviewed and validated
- 5 *C. cellulovorans* genes reviewed and validated (after pruning mis-mapped IDs)
- Systematic corrections: removed mis-propagated catalytic / carbohydrate-binding terms on scaffoldins; added cellulosome, cellulosome assembly, and specific cohesin–dockerin binding terms

**Future directions:**

- Expand to *Ruminococcus flavefaciens* (FD-1) — the most complex cellulosome described, **223 dockerin-containing proteins**, unique cohesin–dockerin binding modes
- Deeper review of remaining *C. cellulovorans* proteins still lacking validated UniProt entries

---

<!-- _class: lead -->

# Thank you

Cellulosome Project — AI-Assisted Gene Review

Chris Mungall | 2026-06-22

Key references: CAZypedia (Cellulosome); Global View of the *C. thermocellum* Cellulosome; Enzymatic diversity of the *C. thermocellum* cellulosome
