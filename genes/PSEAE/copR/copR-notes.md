# copR (PA2809) review notes

UniProt: Q9I034 (unreviewed, 226 aa), "Two-component response regulator, CopR".
Locus PA2809; cognate sensor kinase CopS is PA2810.

## What is established

- CopR is the response regulator of the copper-responsive CopR-CopS
  two-component system, and it is a new negative regulator of the porin gene
  oprD, linking copper, zinc and imipenem resistance
  [PMID:17449606 "This study shows that CopR is a new negative regulator of OprD
  porin and that it links Zn, Cu, and imipenem resistances by interacting with the
  CzcRS TCS."].
- Overproduction of CopR in PAO1-derived PT5 and in a czcRS deletion strain
  lowers oprD mRNA, abolishes OprD protein, and raises czcC and czcR-czcS
  transcription
  [PMID:17449606 "Altogether these results show that the CopR regulator, like CzcR,
  negatively regulates oprD and positively regulates the czcCBA operon (Fig. 5 )."].
  So the same paper supports both a negative and a positive transcriptional role.
- Direct promoter binding was not demonstrated in that work; it is inferred
  from the *P. syringae* CopR cop box
  [PMID:17449606 "It is therefore very likely that the P. aeruginosa CopR regulator
  binds to this cop box, thus activating the transcription of the czcR - czcS genes
  which led to that of the czcCBA operon (Fig. 2A and 5 )."].
- Later work confirms a CopRS regulon that is induced by external Cu2+ and that
  is constitutively on when CopS is absent, consistent with CopS controlling the
  phosphorylation state of CopR
  [PMID:33361129 "In contrast, the ΔcopS mutant strain showed a constitutive
  activation of all the genes of the CopRS regulon, even in the absence of the Cu2+
  stimulus."], [PMID:33361129 "However, in the absence of Cu, CopS shuts down the
  transcriptional response to Cu+, likely dephosphorylating CopR."].
- CopR is 55% identical to CzcR, the zinc-responsive regulator
  [PMID:17449606 "CopR was found to display 73% similarity and 55% identity with the
  CzcR regulator, as determined by pairwise sequence alignment."].

## Literature search

Europe PMC, 2026-11-05: `aeruginosa AND CopR AND copper AND regulon`. Cached and
used: PMID:17449606 (full text), PMID:33361129 (full text). Also returned:
PMID:28760827 and PMID:38861577 (copper homeostasis network reviews), not needed
for the annotation calls.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000724188 | GO:0006355 regulation of DNA-templated transcription | 33 | 475 (45 taxa) | GO:0045892 negative regulation of DNA-templated transcription, IDA, PMID:17449606 (PseudoCAP) | SOUND | Full text read. CopR overproduction drops oprD mRNA by qRT-PCR and abolishes OprD protein by western blot, in the wild type and in a czcRS deletion background, so the repression is attributable to CopR itself and is measured in the organism. The one caveat is that the paper does not show CopR at the oprD promoter, so whether repression is direct is not settled; this does not affect the annotated term, which is regulation rather than promoter binding, nor the IBD, whose node term is the generic parent GO:0006355. | 32 further seeds, including E. coli ArcA (P0A9Q1), OmpR (P0AA16), PhoB (P0AFJ5), CpxR (P0AE88), six M. tuberculosis regulators, Vibrio and plant/cyanobacterial regulators, and the PAO1 genes Q9I034 (this gene) and Q9I0I1 | Yes - overwhelmingly. The node term rests on dozens of characterised response regulators. No `GO_CENTRAL` defect. |

### Node-level judgement for PTN000724188 (recorded here for the batch)

This node is the OmpR/PhoB winged-helix response-regulator node. It carries five
IBDs: GO:0000156 (10 seeds), GO:0006355 (33), GO:0000976 (12), GO:0032993 (7) and
GO:0005829 (4). Each term is at the family level and each is seeded by
experimentally characterised bacterial response regulators, mostly from E. coli.
The terms suit a clade of this size and breadth: every member has a receiver
domain plus a DNA-binding output domain, and the node makes no claim about which
regulon or which direction of regulation. No `GO_CENTRAL` defect is filed, and
the same judgement is applied to `genes/PSEAE/parR` (ParR, Q9I2U3), the other
leaf of this node in this batch, whose notes cross-reference this table.

PseudoCAP defects from this gene: none. The seed row is sound and, unusually for
this project, rests on data in the organism rather than on a mutant phenotype.
One `NEW` row is proposed from the same paper: GO:0045893 positive regulation of
DNA-templated transcription, for the CopR-dependent increase in czcR-czcS and
czcC transcription measured in the same qRT-PCR experiments.
