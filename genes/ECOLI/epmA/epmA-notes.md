# epmA (P0A8N7, E. coli K-12) review notes

## Deep research status

Provider deep research (`just deep-research`) was not run: no provider API keys are available in
this environment. No `*-deep-research-*.md` file exists for this gene. The notes below come from
the cached publications in `publications/` and the UniProt record (`epmA-uniprot.txt`).

Literature checked (cached; full text where noted): PMID:20729861 (abstract only), PMID:21841797
(full text), PMID:22128152 (abstract only), PMID:20670890 (full text), PMID:20070887 (full text),
PMID:22706199 (abstract only), PMID:23239623 (abstract only), PMID:27826291 (full text),
PMID:18304323 (full text), PMID:15690043 (abstract only). PMID:23239624 (Doerfel et al. 2013) is
cached but was not needed for annotation decisions.

## Identity and family

- Names: EpmA, GenX, PoxA, YjeA. UniProt: "Elongation factor P--(R)-beta-lysine ligase", EC 6.3.2.-.
- PANTHER PTHR42918 (LYSYL-TRNA SYNTHETASE), subfamily SF6 "ELONGATION FACTOR P--(R)-BETA-LYSINE
  LIGASE"; InterPro IPR004525 (EpmA), NCBIfam TIGR00462 (genX), HAMAP MF_00174.
- Truncated class II LysRS: keeps the catalytic core, lacks the N-terminal anticodon-binding domain
  [file:ECOLI/epmA/epmA-uniprot.txt "Was originally suggested to be a tRNA synthase, however its lack
  of an anticodon-binding domain made this highly unlikely."].

## Activity

- Lysylates EF-P [PMID:20729861 "it specifically aminoacylates EF-P with lysine"]; EF-P mimics tRNA
  [PMID:20729861 "The shape of the protein substrate mimics that of the L-shaped tRNA, and its
  lysylation site corresponds to the tRNA 3' end"].
- True substrate is (R)-beta-lysine made by EpmB [PMID:21841797 "EF-P was efficiently functionally
  modified with (R)-β-lysine but not (S)-β-lysine or genetically encoded α-amino acids"].
- Not a tRNA synthetase [PMID:21841797 "PoxA cannot aminoacylate tRNALys, indicating that while it is
  structurally similar to LysRS its activity is different from that of a canonical aaRS"].
- Kinetics (UniProt, PMID:21841797): Km 213 uM (R)-beta-lysine, 8600 uM L-alpha-lysine, 6950 uM
  (S)-beta-lysine, 206 uM ATP; kcat 36 min-1 for activation.
- GO:0052868 protein-lysine lysyltransferase activity is defined by exactly the RHEA:83435 EpmA
  reaction (checked in OLS, 2026-11-02), so it is the core MF.
- In vivo, beta-lysyl-EF-P needs both enzymes [PMID:22128152 "indicating that both enzymes, YjeA and
  YjeK, are required for β-lysylation of EF-P"]; EpmC then hydroxylates Lys34 [PMID:22706199].
- Homodimer (UniProt SUBUNIT, PMID:20729861, PMID:20823541).

## Physiology

- Modified EF-P relieves polyproline stalling [PMID:23239623 "In the absence of EF-P, ribosomes stall
  at polyproline stretches"], including for CadC.
- epmA deletion slows growth at pH 4.5, linked to CadA [PMID:27826291 "encoding the transcriptional
  regulator LeuO and the elongation factor P-β-lysine ligase EpmA, can be linked to CadA production"].
- Salmonella poxA/yjeK mutants share virulence and stress phenotypes [PMID:20670890].

## Annotation judgement summary

- LysRS-derived terms (tRNA binding, lysine-tRNA ligase, aminoacyl-tRNA ligase, tRNA aminoacylation,
  lysyl-tRNA aminoacylation) are over-propagated from PTN000502669 / InterPro2GO: REMOVE.
- GO:0043687 post-translational protein modification: ACCEPT here (EpmA performs the covalent step),
  whereas epmB's identical RCA row was MARK_AS_OVER_ANNOTATED because EpmB only supplies the donor.
- Cytoplasm rows MODIFY to cytosol (IDA PMID:18304323). Acid-ammonia ligase (UniRule) MODIFY to
  GO:0052868. Acidic pH response: KEEP_AS_NON_CORE (indirect via EF-P/CadC).
- No gocams/index.tsv entry or module references P0A8N7.
