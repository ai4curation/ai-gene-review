---
title: "Parasite Immune Modulators"
maturity: IN_PROGRESS
last_reviewed: "2026-10-05"
tags: [BIOLOGY_DOMAIN]
species: [DESRO]
sidecars:
  slide_figures:
    - PARASITE_IMMUNE_MODULATORS/slides/candidate-funnel.svg
    - PARASITE_IMMUNE_MODULATORS/slides/host-targets.svg
manifest:
  slides:
    - href: PARASITE_IMMUNE_MODULATORS/slides/PARASITE_IMMUNE_MODULATORS-slides.html
      description: AI generated
---

# Parasite Immune Modulators

**Bottom line:** blood-feeders and parasites secrete proteins that blunt host
clotting, inflammation and immunity. This project now serves as a broad
umbrella rather than the working queue for those reviews: vampire-bat saliva is
handled by [VAMPIROME](VAMPIROME.md), while non-bat parasites are handled by the
[PARASITES](PARASITES.md) umbrella. The vampire-bat scoping pass extracted 45
Vampirome salivary transcripts and mapped 35 to UniProt accessions, all
unreviewed TrEMBL entries. The current DESRO corpus has 14 review YAMLs with
136 reviewed annotation rows: 66 ACCEPT, 27 MODIFY, 21 MARK_AS_OVER_ANNOTATED,
8 KEEP_AS_NON_CORE, 7 UNDECIDED, 4 NEW and 3 REMOVE. Twelve reviews already
have core functions; K9IUF6 and K9J2R0 still need final synthesis, and the
`CALCA/vCGRP` seed only has a mapping-analysis folder because the peptide did not
map cleanly to a DESRO UniProt entry. [#3994](https://github.com/ai4curation/ai-gene-review/issues/3994)
tracks the DESRO backlog.

## Overview

Blood-feeding animals and parasites repeatedly evolve secreted proteins that
interfere with host hemostasis, inflammation, antimicrobial defense and tissue
repair. The initial experiment was vampire-bat saliva because the Vampirome
transcriptome/proteome study supplied a candidate list for *Desmodus rotundus*,
a species with no Swiss-Prot entries in that set. As reviews accumulated, the
working files were split into two more precise projects:

- [VAMPIROME](VAMPIROME.md) owns the DESRO salivary candidate list, UniProt
  mapping files and gene reviews.
- [PARASITES](PARASITES.md) is the umbrella for non-bat parasite genes,
  including host-modulating nematode secreted proteins.

## Vampirome scoping

| Step | Count | Location / status |
|---|---:|---|
| Salivary transcripts extracted from Vampirome Table 4 | 45 | [table4_extract.md](VAMPIROME/table4_extract.md) |
| Transcripts mapped to UniProt | 35 | [uniprot_mapping.md](VAMPIROME/uniprot_mapping.md); all are TrEMBL |
| DESRO review YAMLs | 14 | first hemostasis / immune shortlist plus K9IMD0 Draculin |
| DESRO reviews with synthesized core functions | 12 | K9IUF6 and K9J2R0 remain synthesis TODOs |
| Reviewed DESRO annotation rows | 136 | 132 imported GOA rows plus 4 NEW proposals; 66 ACCEPT, 27 MODIFY, 21 MARK_AS_OVER_ANNOTATED, 8 KEEP_AS_NON_CORE, 7 UNDECIDED, 3 REMOVE |

The first 14 reviews cover the high-priority hemostasis and immune candidates:
plasminogen activator K9IJK6, Kunitz inhibitor K9IZA2, C1-inhibitor-like serpin
K9IYM3, DNase K9J287, CCL28-like chemokine K9IFY6, lymphotoxin-alpha K9IWR0,
beta-defensin K9IFT7, lysozyme K9IWH5, TSG-6 K9IIP0, ADAMTS1-like K9IUF6,
natriuretic peptide K9IWC0, CAP/CRISP protein K9IWX5, DPP4 K9J2R0 and
Draculin / lactotransferrin K9IMD0.

`CALCA/vCGRP` has a `genes/DESRO/CALCA/` mapping-analysis directory but no review
YAML: the reported peptide could not yet be tied to a DESRO UniProt accession.

## Status / next steps

- **DESRO reviews.** Finish VAMPIROME synthesis for K9IUF6 and K9J2R0; resolve
  `CALCA/vCGRP`; then continue through the remaining mapped lipocalin, serpin,
  cystatin, TIMP and other TrEMBL salivary candidates. Tracked in
  [#3994](https://github.com/ai4curation/ai-gene-review/issues/3994).
- **Non-bat parasites.** Fold non-bat parasite host modulators into
  [PARASITES](PARASITES.md), starting with literature-backed seed choices rather
  than a duplicated checklist here. Tracked in
  [#3992](https://github.com/ai4curation/ai-gene-review/issues/3992).

## Related projects

- [VAMPIROME](VAMPIROME.md) — vampire bat salivary gland proteins that modulate
  host hemostasis and immunity.
- [PARASITES](PARASITES.md) — parasitic nematodes and other parasite genes,
  including non-bat secreted host modulators.
