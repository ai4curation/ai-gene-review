# tetH (A0A060URH6, AFERRI_30062) — Acidithiobacillus ferrivorans CF27

No provider deep research available; notes from cached publications and
`ACIF2/tth/tth-bioinformatics/RESULTS.md`.

## Identity
- TrEMBL, PE 4 (predicted), no GOA annotations. Source genome ENA PRJEB5721, strain CF27
  (UniProt RC line gives "STRAIN=PRJEB5721"; the ENA project title is "Acidithiobacillus ferrivorans CF27").
- 503 aa, SignalP signal peptide 1-22, two PQQ_2 propeller regions.
- 98.8% identical to A. ferrivorans SS3 tetH1 (Acife_0037), but only 35% to the SS3 paralog tetH2
  [file:ACIF2/tth/tth-bioinformatics/RESULTS.md "A0A060URH6 vs AEM46280 (A. ferrivorans SS3 tetH1): 98.8% over 503 aligned; vs tetH2 (AEM48684) only 35.4%."].
- 57.9% identical to Af-Tth (B7J3C9) and 71.7% to A. caldus SM-1 TetH; catalytic Asp conserved (D323).

## Evidence in A. ferrivorans (all transcript/genomic; no enzymology)
- SS3 carries two tetH genes [PMID:23183980 "ferrivorans genome also contains two genes coding for tetrathionate hydrolase ( tetH1 [Acife_0037] and tetH2 [Acife_2602])."]
  and tetH1 was the more likely ISC gene [PMID:23183980 "These analyses suggested that sqr1 and tetH1 were more likely to be involved in ISC metabolism."].
- RNA-seq on tetrathionate [PMID:26956550 "RNA transcripts suggested that tetrathionate was hydrolyzed by the tetH1 gene product to form thiosulfate, elemental sulfur and sulfate."].
- No purification, localization or mutant data for A. ferrivorans TetH.

## Annotation decisions
- NEW GO:0016828 hydrolase activity, acting on sulfur-sulfur bonds, ISS from Af-Tth/A. caldus TetH
  (full-length family membership, conserved catalytic Asp), supported by tetH1 transcript data.
- No cellular-component term: only one line (signal peptide); characterised relatives disagree
  (periplasm in A. caldus, outer membrane in A. ferrooxidans and A. thiooxidans SH).
- No process term (no organism-specific functional data beyond transcripts).

## Notes on CMMMech's claim
CMMMech: "Periplasmic tetrathionate hydrolase (tetH) in Acidithiobacillus ferrivorans hydrolyzing
tetrathionate into thiosulfate, elemental sulfur, and sulfate, generating sulfuric acid protons."
Localization is not established for A. ferrivorans (relatives disagree between periplasm and
outer membrane). The activity is inferred by homology plus transcript data, not measured. The
CMMMech example also uses the generic species taxon (NCBITaxon:160808) while the sequence comes
from strain CF27; the RNA-seq evidence comes from strain SS3 (98.8% identical tetH1).
