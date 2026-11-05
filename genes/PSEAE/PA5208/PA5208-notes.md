# PA5208 (Q9HTY2) notes

## Identity

- UniProt Q9HTY2, unreviewed, 225 aa; locus PA5208, no gene name. Name
  "TIGR00153 family protein" is ProtNLM-generated. Domains: Pfam PF01865
  PhoU_div (DUF47), InterPro IPR018445 Put_Phosphate_transp_reg, IPR038078
  PhoU-like superfamily, NCBIfam TIGR00153, PANTHER PTHR36536 (UPF0111
  protein HI_1603). No TM segment, no signal peptide in the entry.
- Neighbour PA5207 is annotated "Phosphate transporter" (Pit family) in the
  PAO1 UniProt list (.cache/paint/pao1.tsv); TIGR00153/DUF47 proteins are
  commonly encoded next to Pit transporters and described as putative
  Pit-accessory, PhoU-like regulators. No experimental characterisation of
  PA5208 or of any member of the family was found (PubMed search for PA5208,
  TIGR00153, UPF0111, "Pit accessory protein").

## Literature

- The only paper is the Overhage et al. 2007 mini-Tn5-lux swarming screen of
  PAO1 (PMID:17158671; full text cached). PA5208 is one of 36
  swarming-deficient insertion mutants
  [PMID:17158671 "36 mutants were identified with Tn5 insertions in genes for
  the synthesis or function of flagellin and type IV pilus, in genes for the
  Xcp-related type II secretion system, and in regulatory, metabolic,
  chemosensory, and hypothetical genes with unknown functions."], and has a
  growth defect [PMID:17158671 "and a PA5208 mutant that had a slight growth
  defect"]. Biofilm: most non-flagellar, non-pilus mutants made somewhat less
  biofilm [PMID:17158671 "all but five of the non-flagellum- or
  non-pilus-related mutants showed a statistically significant"]. The screen
  used a 62 mM phosphate medium; Table 1 records possible polar effects of each
  insertion on downstream genes (the cached text does not include the table
  values), and PA5208 lies next to the Pit transporter gene PA5207.

## Participation test

What entity performs swarming? The flagellum, its stators, pili and
rhamnolipid surfactant. PA5208 is a cytoplasmic PhoU-like protein of unknown
activity; a single insertion with a growth defect reduces swarming and biofilm,
which is necessity evidence at most, and possibly a polar or
phosphate-homeostasis effect. Neither row passes the participation test.

Clade check: the PTN002194937 leaves are Coxiella burnetii CBU_0015 (Pit
accessory protein; non-motile), Haemophilus influenzae HI_1603 (non-motile,
no flagellar genes), Shewanella SO_3770, Vibrio cholerae VC_2441 ("phosphate
transport regulator") and PA5208. A flagellum-dependent swarming term cannot
hold for organisms without flagella, so the IBD is wrong for the clade as well
as for the seed.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002194937 | GO:0071978 bacterial-type flagellum-dependent swarming motility | 1 (sole) | 5 (5 taxa) | GO:0071978, IMP, PMID:17158671 (PseudoCAP) | INDIRECT-PHENOTYPE | A transposon-screen hit with a growth defect; PA5208 is a PhoU-like putative Pit-transporter accessory protein, not a motility component. The node also propagates a flagellar term to non-flagellated Haemophilus and Coxiella. Withdraw the IBD. |

## Decisions summary

- REMOVE: swarming IBA (over-propagation to non-motile taxa, unsupported seed).
- MARK_AS_OVER_ANNOTATED: swarming IMP and single-species biofilm formation
  IMP (screen phenotypes), with PSEUDOCAP defects.
- No core function: the molecular activity is unknown (PhoU-like domain,
  putative Pit regulator).
