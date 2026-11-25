# moaD (P30748) notes, E. coli K-12

Deep research providers were unavailable for this gene (no API keys in this session), so no
`-deep-research-<provider>.md` file was generated. This review is built from the UniProt record
and the cached publications in `publications/`, most of which are abstract-only.

## Identity

- UniProt P30748, molybdopterin synthase sulfur carrier subunit; synonyms chlA4, chlM; b0784.
  Fourth gene of moaABCDE. MoaD family, ubiquitin-like beta-grasp fold, C-terminal Gly80-Gly81.

## Function

- Thiocarboxylate carrier [PMID:17223713 "which in its active form contains a transferrable sulfur in the form of a thiocarboxylate group"].
- Shuttles between MoeB (adenylation) and MoaE (MPT synthase) complexes
  [PMID:17223713 "MoaD cycles between two different heterotetrameric complexes, one with MoaE to form MPT synthase and the other with MoeB"].
- MoeB forms MoaD-AMP; a sulfurtransferase then makes the thiocarboxylate
  [PMID:11713534 "Subsequently, a sulphurtransferase converts the MoaD acyl-adenylate to a thiocarboxylate that acts as the sulphur donor during Moco biosynthesis."].
  UniProt PTM line credits IscS.

## Curation decisions

- Nine bare GO:0005515 IPI rows (MoaE, MoeB, RplL): REMOVE per protein-binding policy; the
  informative content is in GO:1990140 / GO:1990133 (accepted) and the NEW MF.
- NEW GO:0097163 sulfur carrier activity (IDA, PMID:17223713); matches the NEW row in
  genes/PSEPK/moaD. Core MF GO:0097163, complex GO:1990140.
- GO:1990133 (IBA, IPI) ACCEPT: GO definition names MoaD as a subunit.
