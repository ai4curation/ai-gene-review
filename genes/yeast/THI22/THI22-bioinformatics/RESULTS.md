# THI22 vs THI20 paralog alignment — catalytic-residue conservation

## Purpose

THI22 (Q06490, YPR121W) is one of three paralogous members of the *S. cerevisiae*
thiaminase-II / HMP-P-kinase family (THI20, THI21, THI22). The primary literature
(PMID:10383756) demonstrated HMP-P kinase activity for only two of the three members, and
UniProt records a CAUTION that no HMP-P kinase activity could be demonstrated for THI22
despite its high homology. The curation question addressed here: is THI22's lack of
demonstrable activity explained by loss of catalytic residues (a residue-dead pseudoenzyme),
or does it retain an intact active site (sequence-intact but activity not demonstrated)?

## Method

Pairwise global alignment of THI22 (Q06490) against the biochemically characterized paralog
THI20 (Q08224) using Biopython's `Align.PairwiseAligner` (global mode; match +2, mismatch -1,
gap-open -5, gap-extend -0.5). The three THI20 functional residues annotated in UniProt were
mapped through the alignment onto THI22:

- BINDING 64 — HMP substrate binding (N-terminal ThiD-like HMP/HMP-P kinase domain)
- ACT_SITE 468 — nucleophile (C-terminal TenA/thiaminase-II domain)
- ACT_SITE 540 — proton donor (C-terminal TenA/thiaminase-II domain)

Reproduce with: `python align_paralogs.py` (requires biopython). The script prints its
findings and does not hardcode any conclusion.

## Results (from `align_paralogs.py`)

```
THI22 length: 572  THI20 length: 551
Identity: 420/550 = 76.4% over aligned positions

THI20 64  (BINDING HMP substrate, N-term kinase domain):        THI20=Q -> THI22=Q (THI22 pos 86)  [CONSERVED]
THI20 468 (ACT_SITE nucleophile, C-term TenA/thiaminase-II):    THI20=C -> THI22=C (THI22 pos 489) [CONSERVED]
THI20 540 (ACT_SITE proton donor, C-term TenA/thiaminase-II):   THI20=E -> THI22=E (THI22 pos 561) [CONSERVED]

All three THI20 functional residues are conserved in THI22
```

Additional motif observations (from inline inspection of the sequences):

- The ribokinase-family glycine-rich phosphate-binding motif is present in THI22
  (`...IAGSDSSGGAGV...`, ~res 52-63; THI20 has `...AGTDPSGGAGIE...`).
- The `GGHIP` kinase motif is present in THI22 (~res 222).
- THI22 positions are offset from THI20 by ~21-22 residues because of THI22's N-terminal
  signal-peptide extension (residues 1-19), which THI20/THI21 lack.

## Interpretation

THI22 is a close paralog (~76% identity) that **retains all annotated substrate-binding and
catalytic residues of both the kinase and the thiaminase-II domain**. It is therefore **not a
residue-dead pseudoenzyme**. Consequently:

- A domain- or pseudoenzyme-based REMOVE of the kinase/thiaminase molecular-function terms is
  **not justified** — the machinery is intact.
- Equally, the intact machinery does **not** demonstrate activity: the one direct enzymatic
  assay that tested THI22 (PMID:10383756) did not detect HMP-P kinase activity. The molecular
  function terms are best treated as domain-plausible but THI22-unproven (non-core /
  over-annotated as appropriate per evidence), and the lack of demonstrable activity is a
  genuine biological knowledge gap (possible cryptic/conditional activity, divergent
  substrate, or functional divergence toward pseudoenzyme status).

## Data provenance

Sequences taken from the committed UniProt record for THI22
(`genes/yeast/THI22/THI22-uniprot.txt`, Q06490) and from UniProt Q08224 (THI20); THI20
functional-residue positions taken from the UniProt Q08224 feature table (ACT_SITE 468/540,
BINDING 64).
