# tth (A0A5P9XPU3, GCD22_00683) — Acidithiobacillus thiooxidans ATCC 19377

No provider deep research available; notes from cached publications and the family
analysis in `ACIF2/tth/tth-bioinformatics/RESULTS.md` (script `compare_teth.py`).

## Key finding: this entry is a fragment of a disrupted tth copy
- UniProt A0A5P9XPU3 is 235 aa (TrEMBL, PE 4), with no signal peptide; it is the conceptual
  translation of GCD22_00683 (CP045571.1:619853..620560) from a PacBio-only assembly.
- It covers only the central part of the TetH propeller
  [file:ACIF2/tth/tth-bioinformatics/RESULTS.md "A0A5P9XPU3 (A. thiooxidans ATCC 19377, GCD22_00683): 140/235 = 59.6% identity; covers 47.1% of B7J3C9."].
  The upstream ORF GCD22_00682 (QFX95165, 107 aa) holds the signal-peptide N-terminus in
  another frame, and no C-terminal (B7J3C9 350-499 equivalent) segment was found within 2 kb
  downstream: a frame-shifted, C-terminally truncated tth copy (pseudogene or assembly indel error;
  not distinguishable here).
- The catalytic Asp is present in the fragment (D212 aligned to Af-Tth D325), but a protein lacking
  ~110 N-terminal (including the export signal) and ~150 C-terminal residues of an eight-bladed
  propeller is not expected to fold, be exported, or be active. Nothing has been measured.
- The same genome encodes an intact 503-aa tth: UniProtKB A0A5P9XS05 (GCD22_02315,
  CP045571.1:2055336..2056847), 58.6% identical to Af-Tth over 97.8% of its length and 83.8%
  identical to the fragment over its 234 aligned residues — i.e. a different copy, not the
  same gene.

## Relevant A. thiooxidans literature (other strains)
- Marine strain SH TetH is outer-membrane associated, unlike earlier periplasmic reports for
  A. thiooxidans [PMID:29303046 "Although 4THases from A. thiooxidans and the closely related Acidithiobacillus caldus strain have been reported to be periplasmic enzymes, SH-Tth seems to be localized on the outer membrane of the cell, and acts as a peripheral protein."].
- In A. thiooxidans tetH and doxDA are clustered [PMID:37761912 "thiooxidans, the tetH and doxDA genes are found in a cluster (Figure 4), whereas they are located separately in the genomes of the iron-oxidizing strains A."].

## Annotation decisions
- No GOA rows and no NEW annotations: I do not transfer tetrathionate hydrolase activity or any
  location to a fragmentary product without an export signal. The activity belongs on A0A5P9XS05.
- No core function asserted.

## Notes on CMMMech's claim (do not edit CMMMech)
CMMMech uses UniProtKB:A0A5P9XPU3 as the A. thiooxidans ATCC 19377 TetH example ("Periplasmic
tetrathionate hydrolase (tth) in Acidithiobacillus thiooxidans ATCC 19377 disproportionating
tetrathionate into sulfate and sulfuric acid protons ..."). This is the wrong representative:
it is a 235-aa fragment of a disrupted copy with no signal peptide. The intact
A0A5P9XS05 (GCD22_02315, 503 aa) should be the grounding protein. "Periplasmic" is also unproven
for this species (strain SH enzyme is outer-membrane associated), and "disproportionating into
sulfate and protons" omits thiosulfate/sulfur products.
