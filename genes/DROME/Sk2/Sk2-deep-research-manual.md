# Sk2 (Drosophila melanogaster; UniProt Q9VZW0; FBgn0052484; CG32484) - manual literature research

No deep-research provider was available for this session. This file records a manual
literature survey done from cached publications in `publications/` and PubMed searches
(queries: "Drosophila sphingosine kinase Sk2"; "sphingosine kinase[Title/Abstract] AND
Drosophila[Title/Abstract]"; 7 hits, 4 of them about fly Sk2).

## Identity and family

- Q9VZW0 is an unreviewed TrEMBL entry, 661 aa, gene Sk2 (synonyms CG32484, CG2159, SphK2).
  UniProt places it in PANTHER PTHR12358 (sphingosine kinase) and annotates a DAGKc domain
  (PROSITE PS50146, residues 212-358) with PROSITE-ProRule ATP-binding positions 222-226, 254,
  280-286 and 313 (file:DROME/Sk2/Sk2-uniprot.txt).
- Drosophila has two sphingosine kinases, Sk1 (FBgn0030300) and Sk2; they are 39% identical
  [PMID:21321100 "Drosophila Sk1 and Sk2 proteins are 39% identical and 63% similar to each other"].
- The conserved catalytic motif GSGN312-315 lies in the DAGKc domain of Q9VZW0 (checked against
  the displayed sequence: residues 312-315 are G-S-G-N), matching the motif mutated to make a
  catalytically dead Sk2 [PMID:21321100 "We introduced substitutions (GSGN312–315 to DDDD) in the
  corresponding conserved domain of Drosophila Sk2"].

## Enzymatic activity

- Herr et al. 2004 (abstract only cached): both Sk1 and Sk2 complement a yeast sphingosine kinase
  mutant, have predominantly cytosolic activities, and phosphorylate several sphingoid bases
  [PMID:14722126 "Both genes functionally and biochemically complement a yeast sphingosine kinase
  mutant, express predominantly cytosolic activities, and are capable of phosphorylating a range of
  endogenous and non-endogenous sphingoid base substrates"].
- Yonamine et al. 2011 (full text): Sk1 and Sk2 phosphorylate sphingosine and dihydrosphingosine
  (DHS) [PMID:21321100 "Sk1 and Sk2 use both sphingosine and DHS as substrates and generate S1P and
  DHS1P"]. Sk2 overexpression in heads preferentially raises DHS1P
  [PMID:21321100 "However, Sk2 overexpressors preferentially accumulate DHS1P compared with Sk1"].
- The kinase-dead GSGN->DDDD Sk2 transgene does not reproduce overexpression phenotypes,
  showing that those phenotypes require catalytic activity
  [PMID:21321100 "Targeted overexpression of this mutant form of Sk2 does not lead to photoreceptor degeneration"].

## Loss of function and metabolite levels

- The Sk2 P-element allele (Sk2^KG05894) raises long-chain base levels and impairs flight and
  ovulation [PMID:14722126 "A null Sk2 transposon insertion mutant demonstrated elevated long chain
  base levels, impaired flight performance, and diminished ovulation"].
- Yonamine et al. later found this allele is a hypomorph, not a null
  [PMID:21321100 "The Sk2 P-element mutant reported earlier is a hypomorph and not a null mutant
  because we could detect a transcript and a small amount of protein (unpublished data)"].
  This contradicts the "null" description in PMID:14722126.
- sk1 and sk2 mutants accumulate sphingosine and DHS
  [PMID:21321100 "both sk1 and sk2 accumulate sphingosine and DHS"]; the two kinases are partly
  redundant [PMID:21321100 "although single mutants are viable, Sk1 and Sk2 double mutants are
  lethal (unpublished data)"].

## Subcellular location

- In S2 cells stably expressing Sk2 (pMT promoter) and Lamp1-GFP, anti-Sk2 staining is cytoplasmic
  with an additional lysosomal-membrane pool [PMID:21321100 "Sk2 shows cytoplasmic staining;
  additionally, we found that Sk2 can localize to lysosomal membranes, as seen by its
  colocalization with GFP-tagged Drosophila lysosome-associated membrane protein 1 (Lamp1), a
  lysosomal marker"]. Sk2 did not colocalize with early endosome or Golgi markers (Fig. S3).
  Caveats: the cells overexpress Sk2, and light-microscope colocalization with Lamp1 cannot tell the
  membrane surface from the lumen. For a soluble kinase without a TM segment, cytosolic-face
  association is the plausible reading.

## Physiological roles (phenotypes; not used for new GO process terms)

- Photoreceptors: GMR-driven Sk2 overexpression causes retinal degeneration and enhanced lysosomal
  degradation of Rh1 and TRP, which is suppressed in a carnation (Vps33A) mutant (PMID:21321100).
  These are overexpression and metabolite-feeding results. Endogenous sk2 mutants did not show
  clear changes in Rh1 or TRP levels [PMID:21321100 "sk2 flies do not show considerable
  differences in their levels"].
- Glial Sk2 in perineurial glia is needed for presynaptic homeostatic potentiation at the larval
  NMJ (PMID:37669862, abstract only).
- Sk2 mutants have been used as a genetic obesity model with lipid accumulation, sleep
  fragmentation and neuroinflammation (PMID:42230987), and Sk2 was found in a screen as an enhancer
  of FXTAS CGG-repeat toxicity (PMID:30476102).
- The interactome (PMID:38944040, abstract only) reports a binary interaction with CG33523
  (Q9VRR4). Its function is unknown.

## Synthesis

Sk2 is a cytosolic sphingoid-base kinase of the DAGK-fold sphingosine kinase family. It makes
S1P and DHS1P, and part of the protein sits on lysosomal membranes. Most other reported roles
(flight, ovulation, photoreceptor maintenance, synaptic homeostasis, lipid storage) are
downstream consequences of sphingoid-base/phosphate balance.
