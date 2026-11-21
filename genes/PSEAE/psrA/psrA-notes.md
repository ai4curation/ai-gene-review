# psrA (PA3006) review notes

Locus PA3006, UniProt Q9HZJ9 (unreviewed, PE 1; crystal structure PDB 2FBQ from
structural genomics), 233 aa. TetR-family regulator: TetR_N HTH (PF00440, PROSITE
PS50977, residues 4-64) plus a PsrA-specific C-terminal domain (PF17939 TetR_C_30,
IPR041586). No deep-research provider was available; PubMed MCP searches ("psrA
aeruginosa", "PsrA Pseudomonas aeruginosa fatty acid TetR structure") returned API
errors or no hits on 2026-11-05, so the review rests on the three cached papers
cited in GOA.

## Literature

- PsrA represses the fadBA5 beta-oxidation operon and long-chain fatty acids
  relieve repression by disrupting PsrA DNA binding
  [PMID:18524913 "Electrophoretic mobility shift assays indicate specific binding of PsrA to the fadBA5 promoter region. This binding is disrupted by specific LCFAs"]
  (abstract only).
- PsrA is an rpoS activator and negative autoregulator; it binds the motif
  G/CAAAC N2-4 GTTTG/C and regulates further targets positively and negatively
  [PMID:15899403 "The PsrA transcriptional regulator is involved in stationary phase induced transcriptional regulation of rpoS and in negative auto-regulation in Pseudomonas aeruginosa."]
  [PMID:15899403 "Promoters PA0506 and PA2952-PA2951 were regulated negatively whereas promoters of PA2953 and PA3571 were regulated positively by PsrA."]
  (abstract only).
- PsrA is required for full transcription of the T3SS regulatory operon exsCEBA
  and binds its promoter with low affinity; secretion of T3SS effectors falls in
  the deletion mutant and is restored by complementation
  [PMID:16428760 "Using transcriptional fusions, we demonstrated that PsrA is required for the full activation of transcription of the TTSS regulatory operon exsCEBA and effector exoS"]
  [PMID:16428760 "The psrA mutant showed a marked decrease in the secretion of the type III effectors"]
  (full text read). The authors note that activation could be indirect
  [PMID:16428760 "PsrA may activate the TTSS directly at the level of the pC or indirectly via another unknown TTSS regulator(s) controlled by itself."].

## Annotation notes

- GO:0050714 positive regulation of protein secretion (IMP, PseudoCAP): the
  secretion phenotype follows from reduced transcription of the T3SS genes.
  Under GO's convention a transcription factor may be annotated to the process its
  target genes carry out, so it is kept as non-core. No GO term exists for
  regulation of type III secretion specifically.
- MF: PsrA both represses and activates, so GO:0003700 (not repressor or activator)
  is the appropriate MF level. Sequence-specific binding to a defined palindromic
  motif supports GO:0000987 over GO:0000976 and GO:0003677.

## PseudoCAP IBA-seed assessment

PsrA seeds the PTN004738546 GO:0006355 IBD (19 seeds) through its experimental
regulation rows; the PseudoCAP contribution is the IMP GO:0045893 row (a
descendant of GO:0006355). Two CollecTF rows (EXP, IDA GO:0045892) also support
the seeding, so PsrA's seed status does not rest on PseudoCAP. The node is shared
with nfxB, nalC, PA3678, atuR and nalD, reviewed in parallel; the shared-node
(GO_CENTRAL) verdict is recorded on those genes, and no duplicate GO_CENTRAL
defect is recorded here.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045893 positive regulation of DNA-templated transcription, IMP, PMID:16428760 (PseudoCAP); also CollecTF GO:0045892 EXP PMID:18524913 and IDA PMID:15899403 | 18 others, incl. E. coli AcrR (P0ACS9), M. tuberculosis TetR regulators, P. aeruginosa mexZ, PA4596, PA3678 | Yes | SOUND | Full text read. Transcriptional fusions in an in-frame deletion mutant, complementation, and EMSA binding of rPsrA to the exsCEBA promoter show that PsrA positively regulates exsCEBA transcription. Whether the activation is direct is left open by the authors, but GO:0045893 only needs PsrA to regulate transcription positively, and PsrA is an established DNA-binding regulator (fadBA5, rpoS, its own promoter). The generic node term suits a TetR clade. No PseudoCAP defect. |

Shared-node verdict: recorded on nfxB/nalC/PA3678/atuR/nalD by the parallel review.
