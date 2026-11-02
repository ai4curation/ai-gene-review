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

## 2026-11-02

Completion pass for the module bar (precedent PR #3222).

- Overlap check: open PR #5076 carries an older, pre-generalization copy of this
  module (status DRAFT, KT2440-only exemplars) and no new PANTHER grounding beyond
  the SF1/SF19 subfamilies already used here, so it was not adopted. Open PR #2170
  adds a separate KT2440 `phosphonoacetaldehyde_degradation` module and edits
  `genes/PSEPK/phnW`; it does not rework this module, but the two modules overlap in
  scope and should be reconciled when #2170 is resolved.
- Generalization: unchanged. The module was already species-neutral (Bacteria
  envelope, Salmonella/Bacillus biochemical anchors, KT2440 as one exemplar).
- New family review `interpro/panther/PTHR42778/PTHR42778-review.yaml` (PhnW).
  `just fetch-panther-paint PTHR42778` found 25 PTN nodes and no node-level PAINT
  annotations, so there are no IBD nodes to assess.
- Gene reviews: KT2440 phnW and phnX promoted to COMPLETE. The cytosol rows of all
  three PhnX reviews (KT2440, Salmonella, Bacillus) moved from UNDECIDED to
  KEEP_AS_NON_CORE, consistent with the PTHR43434 family review's SOUND assessment
  of the cytosol IBD at PTN001291474 and with transporter-dependent intracellular
  phosphonate catabolism (PMID:37836707).
- Knowledge-gap provenance now records `reference_section_type`; recommended-field
  compliance is 100%, gene-review summary 6/6 complete.
