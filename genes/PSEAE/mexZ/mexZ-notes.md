# mexZ (PA2020) review notes

Locus PA2020, UniProt G3XCU9 (Swiss-Prot reviewed, PE 1), 210 aa. TetR-family
repressor (PF00440 TetR_N, HTH residues 10-70; crystal structure PDB 2WUI).
No deep-research provider was available; PubMed MCP searches returned API
errors on 2026-11-05, so this review rests on the GOA-cited papers, all of which
are cached (23441219 and 31527038 full text; the rest abstract only), and the
curated UniProt entry.

## Literature

- MexZ is the repressor of the mexXY multidrug efflux operon (aminoglycoside
  resistance) [PMID:31527038 "The expression of mexXY operon is negatively regulated by MexZ repressor."].
- Purified MexZ binds a specific site in the mexZ-mexX intergenic DNA, probably as
  a dimer [PMID:15336398 "Highly purified MexZ showed direct binding with a specific site of the mexZ-mexX intergenic DNA when probed by a gel retardation assay."];
  the site is a 20-bp palindrome [PMID:19589837 "MexZ binds to a 20 bp palindromic sequence"].
- Antibiotic induction of mexXY works through the anti-repressor ArmZ (PA5471),
  which binds MexZ and reduces its DNA binding
  [PMID:19589837 "interaction between PA5471 and MexZ reduced MexZ DNA-binding ability, leading to mexXY transcription"];
  the ArmZ interface is the MexZ N-terminal DNA-binding domain
  [PMID:31527038 "the N-terminal part of MexZ, encompassing the DNA-binding domain, is required for interaction with ArmZ"].
- Loss of mexZ raises mexXY expression about 5-fold
  [PMID:23441219 "In a mutant strain lacking the mexZ gene encoding a repressor of mexXY gene expression, expression of the efflux operon increases modestly (5-fold)"].
- mexZ mutations in CF isolates cause MexXY overproduction and moderate
  aminoglycoside resistance; complementation with mexZ lowers MICs
  [PMID:15105120 "Complementation of these bacteria with a plasmid-borne mexZ gene dramatically reduced the MICs of AGs"].

## Annotation notes

- GO:0032410 negative regulation of transporter activity (IMP, PseudoCAP,
  PMID:15105120): GO defines this as a process that reduces the *activity* of a
  transporter. MexZ represses transcription of the mexXY genes, so it lowers the
  amount of pump, not the pump's activity; nothing in the abstract suggests MexZ
  acts on MexXY protein. REMOVE with a PseudoCAP WRONG_TERM defect (PROBABLE:
  abstract-only, but the abstract names mexZ as the repressor gene of the operon).
- GO:0034763 negative regulation of transmembrane transport (same paper): correct
  under the GO convention for transcription factors regulating target genes in a
  process; MODIFY to GO:1905700 negative regulation of xenobiotic detoxification
  by transmembrane export across the plasma membrane (aminoglycoside efflux by
  MexXY), non-core.
- Protein binding (IPI with ArmZ, Q9HT99): REMOVE under the protein-binding
  policy; the interaction is real and is recorded in the core-function text.
  MexZ is the target of the inhibitor, not itself an inhibitor, so no informative
  MF term replaces it.

## PseudoCAP IBA-seed assessment

MexZ seeds all three PTN004738546 IBDs (GO:0006355, GO:0000976, GO:0003700). The
worklist lists the GO:0006355 seeding, with a PseudoCAP IDA (PMID:15336398) among
several supporting rows (CollecTF and UniProt rows support it independently). The
node is shared with nfxB, nalC, PA3678, atuR and nalD, reviewed in parallel; the
shared-node (GO_CENTRAL) verdict is recorded on those genes, and no duplicate
GO_CENTRAL defect is recorded here.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0006355, IDA, PMID:15336398 (PseudoCAP); also GO:0045892 IMP PMID:15336398 (PseudoCAP), IDA/IEP PMID:19589837 (CollecTF), IMP PMID:23441219 and PMID:31527038 (UniProt) | 18 others, incl. E. coli AcrR (P0ACS9), M. tuberculosis TetR regulators, P. aeruginosa psrA, PA4596, PA3678 | Yes | SOUND | The abstract states that purified MexZ binds a specific site in the mexZ-mexX intergenic DNA (gel retardation) and that this explains MexZ repression of mexXY. This is direct evidence for a DNA-binding transcriptional regulator. The seed is under-specific (GO:0045892 is shown) but not wrong. The generic node term suits a TetR clade. No PseudoCAP defect on the seed. |

Non-seed PseudoCAP row with a defect: GO:0032410 (PMID:15105120), WRONG_TERM,
PROBABLE (see above).

Shared-node verdict: recorded on nfxB/nalC/PA3678/atuR/nalD by the parallel review.
