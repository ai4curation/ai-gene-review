# liuA (Pseudomonas aeruginosa PAO1) curation notes

- Reviewed as an experimentally characterized bacterial exemplar of the distal L-leucine catabolism module
  (`modules/leucine_catabolism.yaml`); the P. aeruginosa liuRABCDE cluster (PA2011-PA2016) carries the
  direct enzymology and genetics that the P. putida KT2440 orthologs lack.
- Deep research: no provider deep-research file was generated for this gene in this session. The review
  rests on the cached PubMed records cited in the review (PMID:16517656, PMID:16820476, PMID:16272386,
  PMID:18469096, PMID:18625020, PMID:19459965, PMID:19597963, PMID:22158123), all abstract-only except
  PMID:22158123, and on the UniProt record.
- Acyclic terpene terms: the Atu pathway joins the Liu pathway at methylcrotonyl-CoA
  [PMID:16272386 "enters that of leucine/isovalerate (Liu, leucine and isovalerate utilization) at the level of methylcrotonyl-CoA"],
  so enzymes downstream of that point perform steps of acyclic monoterpenoid catabolism; PseudoCAP
  isoprenoid/terpene rows are refined to GO:0016100 monoterpenoid catabolic process, matching the liuC review.
- LiuA is upstream of methylcrotonyl-CoA and purified LiuA does not oxidize citronellyl-CoA or
  5-methyl-hex-4-enoyl-CoA [PMID:18625020 "citronellyl-CoA or 5-methyl-hex-4-enoyl-CoA were not utilized"],
  yet the complemented liuA mutant cannot grow on terpenes. The isoprenoid IMP row is therefore UNDECIDED:
  the requirement is shown, the step LiuA performs is not.
