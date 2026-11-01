# parA (PA5563, soj, Q9HT11), Pseudomonas aeruginosa PAO1

## 2026-10-23: initial review

**GOA has no annotation for this protein**, although it has been characterized experimentally since
2007. Its Pfam (AAA_31) and PANTHER (PTHR13696:SF52) matches bring no GO. NCBI names the WP_
protein "chromosome partitioning protein Soj" from BlastRule NBR012933, which carries no GO.

**Experimental evidence (Jagura-Burdzy lab, strain PAO1161).**
- Cytosolic, about 600 molecules per cell in exponential phase, falling about fivefold in
  stationary phase. parA inactivation or overexpression gives anucleate cells and motility
  changes, and parA loss destabilises ParB [PMID:17545287 "ParA is a cytosolic protein present
  at a level of around 600 molecules per cell in exponential phase"]. Abstract only in the cache.
- ATPase activity of purified ParA-His6; dimerization and ParB-interaction region E67-L85. The
  parA84 allele (no dimerization, no ParB binding) phenocopies the null; parA67 (no ParB binding)
  is milder [PMID:25139949 "ParA-His6 demonstrated ATPase activity (Fig. 3) of ~1.2 pmol Pi
  released min−1 (pmol ParA)−1."; "Only PAO1161 parA84 was visibly impaired in terms of
  chromosome segregation, growth rate and motility, similar to a parA-null mutant."].
- The parA and parB mutant transcriptomes overlap: a "Par regulon" of 536 genes [PMID:24498062].
- Disrupting ParABS is very detrimental in P. aeruginosa [PMID:23658532 "We also showed that
  disrupting the ParABS system is very detrimental in P. aeruginosa."].
- DnaA regulates the gidAB-parAB operon from oriCII [PMID:42156454].

**Not proposed.** DNA binding (inferred only from conserved Soj arginines, PMID:18077387) and ParB
stimulation of ATPase (shown in Myxococcus, PMID:40998818, not in P. aeruginosa). Both are listed
as suggested questions.

**Decisions.** NEW ATP hydrolysis activity (IDA), chromosome segregation (IMP), protein
homodimerization activity (IPI, two-hybrid only) and cytoplasm (IDA; the source abstract
says "cytosolic", but the method is not stated and ParA-family proteins are expected to
associate with the nucleoid, so the broader term is used).
