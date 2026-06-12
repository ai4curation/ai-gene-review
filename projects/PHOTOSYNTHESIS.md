# Photosynthesis Project

## Overview

Photosynthesis is the light-driven assimilation of CO2 into organic carbon. In oxygenic
photosynthesis (cyanobacteria, algae, plants) light energy captured by chlorophyll drives
electron transport from water to NADP+, producing NADPH, ATP, and O2 (the **light
reactions**), which then power the Calvin–Benson–Bassham reductive pentose-phosphate cycle
to fix CO2 (**carbon fixation**). It is arguably the most important biochemical process in
the biosphere and a major target for crop-improvement and synthetic-biology research.

Concept-level research notes (definitions, GO representation, full component breakdown, and
verified references) live in `terms/photosynthesis/photosynthesis-notes.md`.

## Scope of this first pass

Per the chosen scope, this pass delivers the **concept writeup plus a candidate-gene
checklist**; individual gene reviews are deferred. Strategy: **mix across organisms**,
choosing the best-characterized ortholog per functional module.

## Model species selection (mixed strategy)

- **Cyanobacteria — *Synechocystis* sp. PCC 6803** (UniProt species code **SYNY3**,
  taxonomy 1148) and/or ***Thermosynechococcus***: cleanest genetics for the core light
  reactions; source organisms for the landmark PSI and PSII crystal structures. Preferred
  for reaction-center and electron-transport subunits.
- **Green alga — *Chlamydomonas reinhardtii*** (**CHLRE**, taxonomy 3055): already seeded
  in this repo (psaC, CP12, LCI5); strong for CBB-cycle regulation and the
  carbon-concentrating mechanism.
- **Land plant — *Arabidopsis thaliana*** (**ARATH**): preferred for photoprotection
  (PsbS), the LHC antenna family, and nuclear-encoded Rubisco small subunit / activase.
- **Reference structural orthologs** (spinach / tobacco Rubisco; *Thermosynechococcus*
  PSII) where a module is best characterized elsewhere.

## Functional modules and candidate genes

Accessions are listed only where verified in this repository; others should be resolved
with `just fetch-gene <organism> <gene>` when each review starts (this avoids the
wrong-organism accession pitfalls seen in earlier projects).

### Module A — Photosystem II (water oxidation)
| Gene | Suggested organism | Role |
|------|--------------------|------|
| psbA (D1) | SYNY3 / plant chloroplast | reaction-center, binds P680 + Mn4CaO5 cluster |
| psbD (D2) | SYNY3 | reaction-center, partners D1 |
| psbB (CP47) / psbC (CP43) | SYNY3 | core chlorophyll antenna |
| psbO | ARATH / SYNY3 | oxygen-evolving complex extrinsic protein (GO:0009654) |

### Module B — Photosystem I
| Gene | Suggested organism | Role |
|------|--------------------|------|
| psaA / psaB | SYNY3 | reaction-center heterodimer, binds P700 |
| **psaC** | **CHLRE (Q00914)** — already seeded | terminal FA/FB Fe-S clusters |

### Module C — Electron transport & coupling
| Gene | Suggested organism | Role |
|------|--------------------|------|
| petA / petB / petC | SYNY3 | cytochrome b6f complex (Q-cycle, proton translocation) |
| petE | SYNY3 / ARATH | plastocyanin (mobile Cu carrier) |
| petF | CHLRE / ARATH | ferredoxin (mobile Fe-S carrier) |
| petH (FNR) | ARATH | ferredoxin–NADP+ reductase (makes NADPH) |
| atpA / atpB | SYNY3 / plant chloroplast | chloroplast ATP synthase CF1 |

### Module D — Light harvesting & photoprotection
| Gene | Suggested organism | Role |
|------|--------------------|------|
| LHCB1 / LHCA | ARATH / CHLRE | chlorophyll a/b-binding antenna |
| PsbS | ARATH | non-photochemical quenching (qE) photoprotection |

### Module E — Carbon fixation (Calvin–Benson–Bassham cycle)
| Gene | Suggested organism | Role |
|------|--------------------|------|
| rbcL | tobacco/spinach chloroplast or SYNY3 | Rubisco large (catalytic) subunit (GO:0016984) |
| rbcS | ARATH | Rubisco small subunit |
| rca | ARATH | Rubisco activase |
| prk (PRK) | CHLRE / ARATH | phosphoribulokinase (regenerates RuBP) |
| gapA / gapB | ARATH | chloroplastic GAPDH (redox-regulated) |
| **CP12** | **CHLRE (A6Q0K5)** — already seeded | redox switch; PRK–GAPDH–CP12 ternary complex |

### Module F — Carbon-concentrating mechanism (algae/cyano)
| Gene | Suggested organism | Role |
|------|--------------------|------|
| **LCI5** | **CHLRE (Q94ET8)** — already seeded | low-CO2 inducible thylakoid protein |
| LCIA / LCIB, CCM1/CIA5, carbonic anhydrases | CHLRE / SYNY3 | inorganic-carbon uptake/concentration |

### Module G — Pigment biosynthesis (supporting context)
| Gene | Suggested organism | Role |
|------|--------------------|------|
| CHLH / CHLD / CHLI | ARATH | magnesium chelatase (committed chlorophyll step) |
| POR | ARATH | protochlorophyllide oxidoreductase |

## Annotation watch-points (apply during review)

- Prefer `GO:0019253` (reductive pentose-phosphate cycle) over the broad `GO:0015977`
  (carbon fixation) for CBB-cycle enzymes.
- Reaction-center subunits often inherit generic `GO:0009765` (light harvesting) or
  `GO:0016168` (chlorophyll binding) from electronic pipelines — consider
  `MARK_AS_OVER_ANNOTATED` / `MODIFY` toward charge-separation / electron-transport terms.
- Non-catalytic structural subunits (e.g. PsbO) may inherit catalytic MF terms from
  family rules — flag as the cellulosome project did for scaffoldins.

## Why study photosynthesis?

1. **Food security / crop yield** — Rubisco efficiency and CBB-cycle engineering.
2. **Climate / carbon cycle** — primary route of CO2 fixation into the biosphere.
3. **Bioenergy & synthetic biology** — engineered carbon-concentrating mechanisms,
   artificial photosynthesis.
4. **Basic science** — model supramolecular machines (PSI/PSII) and redox signalling (CP12).

## Key references

According to PubMed (verified):
- Umena et al. 2011, *Nature* 473:55–60 — PSII 1.9 Å structure. PMID:21499260.
- Jordan et al. 2001, *Nature* 411:909–917 — PSI 2.5 Å structure. PMID:11418848.
- Andersson & Backlund 2008, *Plant Physiol Biochem* 46:275–291 — Rubisco. PMID:18294858.
- Shao et al. 2021, *Cell Commun Signal* 19:38 — CP12 / CBB regulation. PMID:33761918.

---
# STATUS

## Concept writeup
- [x] `terms/photosynthesis/photosynthesis-notes.md` created (manual notes; deep-research provider unavailable)
- [x] GO representation verified against `cache/go/terms.csv` + GOlr
- [x] Key references PubMed-verified

## Gene reviews (deferred — first pass is concept writeup only)
### Already seeded
- [x] CHLRE/psaC (Q00914) — pre-existing
- [~] CHLRE/CP12 (A6Q0K5) — pre-existing (DRAFT)
- [~] CHLRE/LCI5 (Q94ET8) — pre-existing

### To do (candidates)
- [ ] Module A — PSII: psbA, psbD, psbB/psbC, psbO
- [ ] Module B — PSI: psaA, psaB
- [ ] Module C — electron transport: petA/B/C, petE, petF, petH, atpA/atpB
- [ ] Module D — antenna/photoprotection: LHCB1, PsbS
- [ ] Module E — CBB cycle: rbcL, rbcS, rca, PRK, gapA/gapB
- [ ] Module F — CCM: LCIA/B, CCM1, carbonic anhydrases
- [ ] Module G — pigment biosynthesis: CHLH, POR

# NOTES

## 2026-06-12 (Session 1)

**Project created.** Scope for this pass: concept writeup + candidate-gene checklist;
individual reviews deferred. Mixed-organism strategy chosen (Synechocystis for core light
reactions, Chlamydomonas for CBB/CCM — already partly seeded — and Arabidopsis for
antenna/photoprotection and nuclear CBB genes).

Attempted `just term-deep-research-falcon "Photosynthesis"`; the provider run failed
because `templates/concept_research.md.j2` embeds a literal `{concept}` placeholder that is
not substituted, so the model received an empty concept and returned a "cannot be
completed" non-report. The empty file was discarded (not kept as
`-deep-research-falcon.md`) and `terms/photosynthesis/photosynthesis-notes.md` was authored
manually instead, with all GO IDs and PMIDs independently verified.

**Follow-up infra note:** the `{concept}` → `{{ concept }}` template substitution bug in
`templates/concept_research.md.j2` affects *all* concept deep-research runs and is worth
fixing separately before the next `term-deep-research` invocation.
</content>
