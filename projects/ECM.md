---
title: "Extracellular Matrix (ECM) Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [AGRN, HSPG2, EPYC, SPOCK1, SPOCK2, SPOCK3, NID1, FN1, DCN, SPARC]
last_reviewed: 2026-10-04
manifest:
  slides:
    - href: ECM/slides/ECM-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/GsehR2DwujN5p72k3Y33K4
      title: Project brief
---

# Extracellular Matrix (ECM) Project

**Bottom line:** the extracellular matrix is the protein and proteoglycan
network that gives tissues mechanical support, basement-membrane polarity and
adhesive signalling cues. This project actioned every row in a ten-gene human
ECM pilot spanning basement-membrane proteoglycans (`AGRN`, `HSPG2`, `NID1`),
interstitial matrix components (`FN1`, `DCN`, `EPYC`, `SPARC`) and the three
testicans (`SPOCK1`, `SPOCK2`, `SPOCK3`). As of 2026-10-04, those files contain
635 review rows: 284 ACCEPT, 193 KEEP_AS_NON_CORE, 70 REMOVE, 63 MODIFY, 13 NEW,
5 MARK_AS_OVER_ANNOTATED and 7 UNDECIDED. Eight review YAMLs are `COMPLETE`;
`AGRN` is still `DRAFT`, `NID1` is still `INITIALIZED`, `DCN` still needs
`core_functions`, and the first basement-membrane `ModuleReview` remains to be
drafted. Those follow-ups are tracked in
[#4070](https://github.com/ai4curation/ai-gene-review/issues/4070).

The largest single clean-up was `FN1`: its review removed 52 generic IPI
`protein binding` rows and modified 38 `extracellular region` rows to the more
specific `extracellular matrix`. The testican reviews kept the SPOCK paralogs
separate: `SPOCK1` and `SPOCK3` retain metalloendopeptidase-inhibitor activity,
whereas `SPOCK2` rows were modified toward endopeptidase-regulator and
cell-motility terms because SPOCK2 counter-inhibits SPOCK1/3. `EPYC` gained NEW
collagen-binding, collagen-fibril-organization and matrix-constituent rows.

## Overview

Extracellular-matrix proteins are large, secreted and domain-rich, and many of
their GOA rows come from high-throughput interaction or ECM-proteomics screens.
That makes them a useful test for separating true molecular roles — collagen
binding, basement-membrane scaffolding, peptidase inhibition, fibril assembly —
from generic `protein binding`, broad `extracellular region` localizations and
downstream developmental phenotypes.

The pilot deliberately mixed three slices of ECM biology:

- **Basement membrane:** `AGRN`, `HSPG2`, and `NID1` organize perlecan/agrin,
  laminin and collagen-IV-rich sheets.
- **Testicans:** `SPOCK1`, `SPOCK2` and `SPOCK3` test paralog-specific review
  because SPOCK2 antagonizes the peptidase-inhibitory logic of SPOCK1 and
  SPOCK3.
- **Interstitial/matricellular components:** `FN1`, `DCN`, `EPYC` and `SPARC`
  cover fibronectin assembly, small leucine-rich proteoglycans and collagen
  regulation.

## Review Set

| Phase | Genes | Current state | Main curation signal |
| --- | --- | --- | --- |
| 1 — basement-membrane proteoglycans + EPYC | `AGRN`, `HSPG2`, `EPYC` | `HSPG2`/`EPYC` complete; `AGRN` row review actioned but still `DRAFT` | Agrin/perlecan core basement-membrane functions; EPYC gained explicit collagen/matrix terms |
| 2 — testican/SPOCK paralogs | `SPOCK1`, `SPOCK2`, `SPOCK3` | Complete | SPOCK1/3 inhibit metalloendopeptidases; SPOCK2 counter-inhibits SPOCK1/3 rather than sharing the same MF |
| 3 — diverse ECM components | `NID1`, `FN1`, `DCN`, `SPARC` | `FN1`/`DCN`/`SPARC` complete; `NID1` row review actioned but still `INITIALIZED` | FN1 generic interaction cleanup; nidogen basement-membrane bridging; decorin/SPARC collagen regulation |

### 2026-10-04 action snapshot

| Gene | Rows | Status | Action mix |
| --- | ---: | --- | --- |
| `FN1` | 196 | COMPLETE | 62 ACCEPT · 39 KEEP_AS_NON_CORE · 38 MODIFY · 54 REMOVE · 3 NEW |
| `HSPG2` | 106 | COMPLETE | 45 ACCEPT · 52 KEEP_AS_NON_CORE · 6 MODIFY · 2 MARK_AS_OVER_ANNOTATED · 1 UNDECIDED |
| `AGRN` | 102 | DRAFT | 54 ACCEPT · 36 KEEP_AS_NON_CORE · 6 MODIFY · 1 REMOVE · 5 UNDECIDED |
| `DCN` | 72 | COMPLETE | 17 ACCEPT · 41 KEEP_AS_NON_CORE · 8 MODIFY · 4 REMOVE · 2 MARK_AS_OVER_ANNOTATED |
| `SPARC` | 43 | COMPLETE | 29 ACCEPT · 7 KEEP_AS_NON_CORE · 1 MODIFY · 5 REMOVE · 1 NEW |
| `NID1` | 40 | INITIALIZED | 32 ACCEPT · 7 KEEP_AS_NON_CORE · 1 REMOVE |
| `SPOCK1` | 32 | COMPLETE | 18 ACCEPT · 8 KEEP_AS_NON_CORE · 3 REMOVE · 2 NEW · 1 UNDECIDED |
| `SPOCK2` | 17 | COMPLETE | 10 ACCEPT · 2 KEEP_AS_NON_CORE · 4 MODIFY · 1 REMOVE |
| `SPOCK3` | 17 | COMPLETE | 14 ACCEPT · 3 NEW |
| `EPYC` | 10 | COMPLETE | 3 ACCEPT · 1 KEEP_AS_NON_CORE · 1 MARK_AS_OVER_ANNOTATED · 1 REMOVE · 4 NEW |

## Key Findings

- **FN1 drove most removals and modifications.** The review removed 52 IPI
  `protein binding` rows and modified 38 bulk `extracellular region` rows to
  `extracellular matrix`.
- **SPOCK2 needs different terms from its paralogs.** SPOCK2 inhibits the
  inhibitory action of SPOCK1/3 and was not kept as a metalloendopeptidase
  inhibitor itself.
- **EPYC was under-annotated.** It gained NEW rows for `collagen binding`,
  `collagen fibril organization`, `extracellular matrix structural constituent`
  and `extracellular matrix organization`.
- **NID1 connects the basement-membrane network.** Its core functions center on
  structural matrix activity plus laminin and collagen binding.
- **DCN remains structurally unfinished.** The 72 annotation rows are all
  actioned, but the review still needs a `core_functions` synthesis.

## Status and Next Steps

- [x] Phase 1 row review: AGRN, HSPG2, EPYC
- [x] Phase 2 row review: SPOCK1, SPOCK2, SPOCK3
- [x] Phase 3 row review: NID1, FN1, DCN, SPARC
- [x] Validate all ten current review files
- [ ] Finalize the `AGRN` and `NID1` review statuses
  ([#4070](https://github.com/ai4curation/ai-gene-review/issues/4070))
- [ ] Add `DCN` core functions
  ([#4070](https://github.com/ai4curation/ai-gene-review/issues/4070))
- [ ] Draft a basement-membrane ECM `ModuleReview` for NID1/HSPG2/AGRN plus
  laminin/collagen IV context
  ([#4070](https://github.com/ai4curation/ai-gene-review/issues/4070))

## Component Notes

**SPOCK proteins (Testican family):**
- Proteoglycans belonging to the SPARC/osteonectin family
- Modular structure with follistatin-like and extracellular calcium-binding domains
- Chondroitin/heparan sulfate chains
- **Key finding**: SPOCK2 uniquely acts as counter-inhibitor, blocking SPOCK1/3 MMP inhibition
- Roles in ECM assembly, neurogenesis, angiogenesis, and cancer

**Diverse ECM proteins:**
- **NID1**: Bridges laminin to collagen IV networks in basement membranes
- **FN1**: Cell adhesion, migration, wound healing
- **DCN**: Collagen fibrillogenesis, TGF-β regulation
- **SPARC**: Parent family member, Ca²⁺ binding, collagen binding, anti-adhesive
