# puuA-I curation notes

Q88KW1 is assigned to PTHR43785:SF12, a mixed subfamily containing both
glutamine synthetases and E. coli PuuA P78061
[file:interpro/panther/PTHR43785/PTHR43785-entries.csv]. Subfamily membership
therefore does not distinguish the two activities by itself. Purified E. coli
PuuA "catalyzed the ATP-dependent gamma-glutamylation of putrescine"
[PMID:18495664], providing the characterized same-subfamily exemplar.

The target locus PP_2178 is adjacent to PP_2179, a PuuD-family
gamma-glutamyl-GABA hydrolase, and PP_2180, a polyamine transaminase
[file:projects/P_PUTIDA/deep-research/PSEPK__gamma-glutamyl-putrescine-catabolism__ppu00330-deep-research-openscientist.md].
This synteny independently supports a polyamine-catabolic role. In Pseudomonas,
however, SpuC is described as "the major putrescine-pyruvate transaminase" and
gamma-glutamylation as an alternative route [PMID:18192388], so native KT2440
flux through PuuA-I remains an experimental question.

## 2026-11-11 completion pass

- Generic MF parents (catalytic activity, ligase activity) changed to MODIFY
  toward GO:0034024; the glutamine synthetase row changed from REMOVE to
  MARK_AS_OVER_ANNOTATED, consistent with E. coli PuuA and puuA-II (no assay
  excludes ammonium; KT2440 GlnA is in PTHR43407).
- The TreeGrafter polyamine catabolic process row can only derive from
  PTN001839150, the PuuA/PauA clade, the sole PTHR43785 node with GO:0006598.
- Deep research by an external provider was not run in this session.
