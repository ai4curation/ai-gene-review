# FLCN (horse, A0A3Q2LPC0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Cohort: DONKEY40_HORSE_PARTNER (horse partner of donkey FLCN A0A8C4MM62, reviewed separately in
`genes/EQUAS/FLCN/`). No ProtNLM2 output was opened or used.

### Provenance and data

- Created with `just fetch-gene HORSE A0A3Q2LPC0 --alias FLCN`; stub id confirmed as A0A3Q2LPC0.
- Deep research: `just deep-research-falcon HORSE FLCN --fallback perplexity-lite` failed (falcon failed and
  the perplexity-lite fallback timed out at 600 s). No deep-research file exists; the review relies on
  cached full-text papers (PMID:24095279, PMID:31672913, PMID:31704029, PMID:32612235, PMID:34381247) and
  the human (Q8NFG4) and mouse (Q8QZS3) Swiss-Prot records fetched into `FLCN-bioinformatics/`.
- GOA: 17 rows, all IBA or IEA (no experimental horse annotations), as expected for a TrEMBL PE 3 entry.

### Identity

- A0A3Q2LPC0 is the canonical, full-length horse FLCN product (578 aa vs human 579 aa), not a fragment or
  isoform [file:HORSE/FLCN/FLCN-bioinformatics/RESULTS.md "Aligned pairs: 578; identical: 548; identity:
  94.81%"]. Differences cluster in the disordered N-terminal segment (horse 31-82); the uDENN FLCN/SMCR8
  domain (86-557) is complete.
- Evolutionary grounding: PANTHER PTHR31441:SF2 (FOLLICULIN) for both horse and human; IBA rows descend
  from PAINT nodes PTN002833743 (seeded by yeast Lst7, fission yeast Bhd1, human FLCN, fly), PTN001265854
  (mouse + human, transcription) and PTN001265856 (mouse, TGF-beta). Donkey FLCN is in the same subfamily.
- Catalytic and other experimentally defined residues conserved [file:HORSE/FLCN/FLCN-bioinformatics/RESULTS.md
  "SITE human R164 -> horse R164 (Essential for GTPase activation (GAP) activity)"].

### Function (human experimental, transferred on subfamily membership + residue conservation)

- FLCN-FNIP is a GAP for RagC/D [PMID:24095279 "we identified the FLCN-FNIP complex as a potent GTPase
  activating protein (GAP) for RagC/D"]; Arg164 is the arginine finger [PMID:31704029 "the conserved Arg164
  residue on FLCN is the catalytic arginine finger that simulates GTP hydrolysis by RagC"].
- In starvation, FLCN is held inactive on lysosomes in the LFC [PMID:31672913 "FLCN clustered on
  LAMP2-positive lysosomes in amino acid-depleted conditions and became dispersed in the cytosol upon
  refeeding"].
- The RagC/D GAP specifically licenses mTORC1 phosphorylation of TFEB/TFE3, not S6K/4E-BP1
  [PMID:32612235 "cells lacking FLCN, a specific GAP for RagC/D16–18, still showed phosphorylation of S6K and
  4E-BP1"]. Effects on transcription (TFE3/TFEB targets) are therefore indirect.
- LDHA inhibition (human, PMID:34381247) is a single-lab finding; the N-terminal region is highly
  conserved in horse but the exact loop is not mapped in the cached text, so no NEW term is added.

### Decisions

- ACCEPT: GTPase activator activity (IBA contributes_to; IEA enables), FNIP-folliculin RagC/D GAP,
  positive regulation of TORC1 signaling, lysosomal membrane, cytosol (IBA + IEA).
- MODIFY: positive regulation of TOR signaling (ARBA) -> positive regulation of TORC1 signaling.
- KEEP_AS_NON_CORE: nucleus (IBA + IEA), centrosome, spindle, cilium, negative regulation of transcription by
  RNA pol II (IBA + IEA; indirect via TFE3/TFEB), positive regulation of TGF-beta receptor signaling (IBA).
- MARK_AS_OVER_ANNOTATED: negative regulation of signal transduction (ARBA).
- No NEW annotations.

### Relative

- Human FLCN (Q8NFG4), same PANTHER subfamily PTHR31441:SF2 and the experimental donor of most PAINT
  nodes. No `genes/human/FLCN` review exists in the repo -> needs review.
- No module in `modules/` names FLCN; closest pathway modules are `modules/pi3k_akt_mtor.yaml` (mTORC1) and
  `modules/dmel_torc1_nutrient_sensing.yaml` (fly TORC1 nutrient sensing).
- TGF-beta IBA seed: mouse IMP from PMID:21258407 (cached full text, Bhd-null ES cells) [PMID:21258407
  "general loss of TGFβ-dependent chromatin modifications and transcription"]; perturbation evidence only,
  hence non-core.
