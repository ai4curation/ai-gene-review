# Msed_0639 (A4YEG2) notes — methylmalonyl-CoA epimerase

Automated deep research was unavailable for this gene (no `*-deep-research-*.md`
file). The literature below was located manually (Europe PMC / NCBI E-utilities /
web search) and the cited PMIDs are cached in `publications/`.

## Identity

- UniProt A4YEG2 (unreviewed), 140 aa, "Methylmalonyl-CoA epimerase", EC 5.1.99.1.
  VOC (vicinal oxygen chelate) fold: PROSITE PS51819, InterPro IPR017515
  (MeMalonyl-CoA_epimerase), NCBIfam TIGR03081 (metmalonyl_epim), CDD cd07249 (MMCE),
  PANTHER PTHR43048:SF3 [file:METS5/Msed_0639/Msed_0639-uniprot.txt "Methylmalonyl-CoA epimerase"].
- Gene is adjacent to Msed_0638 (MCM catalytic subunit).

## Literature

- Ramos-Vera et al. 2011: [PMID:21169482 "the conversion of methylmalonyl-CoA to succinyl-CoA, which is catalyzed by methylmalonyl-CoA epimerase and methylmalonyl-CoA mutase (MCM)"].
- Han et al. 2012 (abstract read; full text inaccessible):
  [PMID:22752162 "the gene encoding MCE (Msed_0639) is adjacent to that encoding the catalytic subunit of MCM-α (Msed_0638)"];
  [PMID:22752162 "The expression of all three genes was significantly upregulated under autotrophic compared to heterotrophic growth conditions, implying a role in CO(2) fixation."];
  [PMID:22752162 "MCE is a homodimer and MCM is a heterotetramer (α(2)β(2)) with specific activities of 218 and 2.2 μmol/min/mg, respectively, at 75°C."];
  [PMID:22752162 "MCE was activated by divalent cations (Ni(2+), Co(2+), and Mg(2+))"];
  [PMID:22752162 "The two enzymes together catalyzed the two-step conversion of (S)-methylmalonyl-CoA to succinyl-CoA, consistent with their proposed role in the 3-HP/4-HB cycle."];
  [PMID:22752162 "Based on the highly conserved occurrence of single copies of MCE and MCM in Sulfolobaceae genomes, the M. sedula enzymes are likely to be representatives of these enzymes in the 3-HP/4-HB cycle in crenarchaeal thermoacidophiles."]
- Loder et al. 2016: [PMID:27771364 "characterization of MCE and MCM was reported previously (Han et al., 2012)"].

## Conclusions

- Msed_0639 is the recombinantly verified homodimeric, divalent-cation-activated
  methylmalonyl-CoA epimerase of the 3HP/4HB cycle, converting the (S)-methylmalonyl-CoA
  made by propionyl-CoA carboxylase to (R)-methylmalonyl-CoA for MCM; transcription is
  induced under autotrophy. No genetic (knockout) evidence exists.
- GO:0004493 accepted; GO:0046491 L-methylmalonyl-CoA metabolic process kept as non-core (the
  enzyme interconverts the two methylmalonyl-CoA epimers, so L-methylmalonyl-CoA is its
  substrate or product in either direction; note the GO definition itself mixes 'L-' and
  'S-', whereas L-methylmalonyl-CoA is conventionally the (R)-epimer used by MCM); GO:0015977 carbon fixation NEW.
- Metal activation (Ni, Co, Mg) is consistent with the VOC fold but the bound metal in
  vivo is not known; no metal-binding term is proposed.
