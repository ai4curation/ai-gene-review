# PhnWX cross-species audit

## 2026-10-25

Literature searches included `2-aminoethylphosphonate PhnW PhnX review phosphonates
bacteria phosphonatase` and `PhnW Salmonella typhimurium phosphonoacetaldehyde
hydrolase Bacillus cereus characterization`. The comparative review
[PMID:37836707](https://pubmed.ncbi.nlm.nih.gov/37836707/) was fetched with full text.
Sections 3.1, 6 and 7 support the pathway boundary, patchy bacterial distribution
and regulatory variation. Its sentence describing a beta-carbonyl group of AEP
is chemically misleading and is deliberately not used as mechanistic support.
The review is useful for comparative context but does not replace protein-specific
biochemical evidence.

The two reactions are anchored by Salmonella PhnW biochemistry
[PMID:12107130](https://pubmed.ncbi.nlm.nih.gov/12107130/) and comparative
Bacillus/Salmonella PhnX characterization
[PMID:9649311](https://pubmed.ncbi.nlm.nih.gov/9649311/). Each leaf and the connecting
intermediate now carry literature evidence. KT2440 remains an inferred realization:
experiments on NG2, BIRD-1, Salmonella or Bacillus are not experiments on Q88KT0/Q88KT1.

[PMID:37876809](https://pubmed.ncbi.nlm.nih.gov/37876809/) establishes oxidative
alternatives to PhnW. This matters to module interpretation: a PhnX homolog is
insufficient evidence for the complete PhnWX route. PhnWAY, oxidative entry routes,
and C-P lyase remain outside this module. Transporters and phosphate-starvation
regulation also remain outside the conserved two-step boundary.

UniProt REST queries confirmed the following records and exact PANTHER subfamily
cross-references; the repository member validator provides a second check:

| Organism | PhnW | PhnX | Evidence distinction |
|---|---|---|---|
| P. putida KT2440 | Q88KT0 / PTHR42778:SF1 | Q88KT1 / PTHR43434:SF19 | Inferred from curated family assignments and pathway context |
| S. typhimurium LT2 | P96060 / PTHR42778:SF1 | Q7ZAP3 / PTHR43434:SF19 | Recombinant biochemical characterization |
| B. cereus | Q8RLU1 / PTHR42778:SF1 | O31156 / PTHR43434:SF19 | PhnX directly characterized; PhnW probable fragment with a sequence caution |

Both steps therefore sample Pseudomonadota and Bacillota. Bacteria (NCBITaxon:2,
verified through the UniProt taxonomy API) is their shared taxonomic envelope;
it does not assert that all bacteria possess the pathway or infer an ancestral
origin. No PAINT node is manufactured from the exemplar list. Q8RLU1 remains
useful as a qualified family representative, but must not be used as proof of an
intact experimentally tested Bacillus enzyme or of a complete strain genome.

Six individual gene reviews accompany this audit. Existing phosphoglycolate
phosphatase/DNA-repair annotations to PhnX are evaluated against its specialized
phosphonatase chemistry rather than accepted solely from broad HAD-superfamily
inheritance. Native cytosolic localization remains UNDECIDED where no independent
localization evidence was found.
