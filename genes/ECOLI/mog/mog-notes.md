# mog (P0AF03) notes, E. coli K-12

Deep research providers were unavailable for this session (no API keys), so no
`-deep-research-<provider>.md` file exists. The review is built from the UniProt record
and the cached publications (abstract-only except PMID:18304323). PMID:18154309 (Bevers et
al. 2008) was cached for this review.

## Identity

- UniProt P0AF03, molybdopterin adenylyltransferase, EC 2.7.7.75; synonyms chlG, mogA, yaaG;
  b0009. MoaB/Mog family; PANTHER PTHR43764 (subfamily SF1 is named "MOLYBDOPTERIN
  MOLYBDOTRANSFERASE", a family name only, not an activity claim on MogA).
- Curated function [file:ECOLI/mog/mog-uniprot.txt "Catalyzes the adenylation of molybdopterin as part of the biosynthesis of the molybdenum-cofactor."].

## Biochemistry

- Homotrimer; Asp49 and Asp82 essential [PMID:10636880 "a putative active site was identified, including two residues that are essential for the catalytic mechanism"].
  The 2000 paper proposed MogA as the molybdochelatase; later work assigns Mo insertion to MoeA
  and MPT adenylylation to MogA.
- mogA(-) cells make MPT but cannot insert Mo [PMID:12006571 "moeA(-) and mogA(-) cells are able to synthesize molybdopterin, but both are deficient in molybdenum incorporation"].
- MogA stimulates MoeA in an ATP/Mg-dependent way [PMID:15632135 "MogA stimulates this activity in an ATP-dependent manner"].
- MogA, not E. coli MoaB, adenylylates MPT [PMID:18154309 "only MogA is able to catalyze MPT adenylylation, whereas E. coli MoaB is inactive"].

## Curation decisions

- Bare protein binding removed per policy.
- GO:0032324 rows (IBA, IDA, IMP) MODIFY to GO:0006777: correct but general, and the
  molybdenum-specific descendant is supported and already carried by the gene (IEA).
  Contrast PYRFU/moaB, where the general term is kept because P. furiosus makes tungsten
  cofactor.
- Identical protein binding (trimer) kept as non-core; no trimer-specific MF term exists.
- No crossover rows: E. coli MogA GOA carries no molybdotransferase (GO:0061599) term.
