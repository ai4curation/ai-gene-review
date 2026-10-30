# F9ZNI0 (Atc_1595, TetH) — Acidithiobacillus caldus SM-1

No provider deep research available; notes from cached publications and
`ACIF2/tth/tth-bioinformatics/RESULTS.md`.

## Identity
- TrEMBL entry, PE 4 (predicted), no GOA annotations, no gene name (ordered locus Atc_1595);
  submitter name "Tetrathionate hydrolase TetH". Signal peptide 1-24 (SignalP), two PQQ_2
  (PF13360) repeat regions — the TetH beta-propeller.
- 99.2% identical over 503 aligned residues to the A. caldus KU (ATCC 51756) TetH (ABP38225)
  [file:ACIF2/tth/tth-bioinformatics/RESULTS.md "F9ZNI0 vs ABP38225 (A. caldus KU TetH): 99.2% over 503 aligned."].
  The KU tetH gene was tied to the purified enzyme by peptide sequencing
  [PMID:17873067 "Trypsin digestion and N-terminal sequencing of the tetrathionate hydrolase protein provided three peptide sequences (SITPVLQPGNPFDPDSPFARLYLPQNA, GVQWNFP, and GEIPGAVNTG) that were used to confirm the corresponding gene in the genome sequence of A."].
  The mature N-terminus of F9ZNI0 after its predicted 24-aa signal peptide begins
  SITPVLQPGNPFDPDS..., identical to the sequenced N-terminal peptide of the purified KU enzyme,
  which also confirms the SignalP cleavage site.
- 58.9% identical to the structurally characterised Af-Tth (B7J3C9); catalytic Asp conserved (D323).

## Activity and localization of the A. caldus enzyme (strain KU)
- [PMID:14717695 "Tetrathionate hydrolase was shown to be a homodimer with a molecular mass of 103 kDa (composed from two 52 kDa monomers). The purified enzyme had optimum activity at pH 3.0 and 40 degrees C and an isoelectric point of 9.8."]
- Periplasmic by differential fractionation [PMID:14717695 "The periplasmic localization of the enzyme was determined by differential fractionation of A. caldus cells."].
- Products reported as thiosulfate and pentathionate for this enzyme [PMID:14717695 "Detected products of the tetrathionate hydrolase reaction were thiosulfate and pentathionate as confirmed by RP-HPLC analysis."], differing from the sulfur/thiosulfate/sulfate reported for Af-Tth.
- An o-quinone moiety was detected but it is not PQQ [PMID:17873067 "However, the fact that the TetH extract did not restore the function of the apo form of glucose dehydrogenase suggests that this cofactor is not PQQ."].
- Expression induced by tetrathionate, thiosulfate and pyrite [PMID:17873067 "Western blot analysis also indicates upregulation of TetH in the presence of tetrathionate, thiosulfate, and pyrite."]; operon rsrR-rsrS-tetH-doxD; RsrS-RsrR positively regulates the S4I genes (A. caldus MTH-04) [PMID:27857710 "Transcriptional analysis of the tetH cluster in the wild type and mutant strains revealed positive regulation of the S4I pathway by the RsrS-RsrR system."].

## Annotation decisions
- NEW GO:0016828 hydrolase activity, acting on sulfur-sulfur bonds (ISS to A. caldus KU TetH).
- NEW GO:0042597 periplasmic space (ISS to KU TetH fractionation; consistent with SignalP and acid optimum).
- No process term: none of the evidence is in SM-1 itself, and the only accurate GO process term
  is the broad sulfur compound metabolic process, which I keep for the experimentally studied Af-Tth.

## Notes on CMMMech's claim
CMMMech: "Periplasmic tetrathionate hydrolase TetH (Atc_1595) in Acidithiobacillus caldus SM-1
hydrolyzing tetrathionate into thiosulfate, sulfur, and sulfate protons at moderately thermophilic
leaching temperatures." Periplasmic is reasonable by orthology to strain KU. Product list follows
Af-Tth; the A. caldus enzyme was reported to give thiosulfate and pentathionate. No experiment was
done on SM-1 itself; "at moderately thermophilic leaching temperatures" is context, not evidence of
in-leach activity (KU enzyme optimum 40 °C in vitro).
