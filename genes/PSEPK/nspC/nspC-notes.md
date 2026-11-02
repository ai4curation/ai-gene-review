# nspC evidence notes

## 2026-08-11

The exact KT2440 record assigns NspC to the carboxyspermidine/
carboxynorspermidine decarboxylase subfamily and gives EC 4.1.1.96. Its adjacency
to PP_2928 matches the paired dehydrogenase/decarboxylase organization of the
alternative pathway established in Vibrio cholerae. [PMID:19196710 "Genetic
deletion of the V. cholerae CANSDC led to accumulation of
carboxynorspermidine"]

No direct KT2440 NspC assay is available. The current GO molecular-function
annotation is only the broad carboxy-lyase parent, so a specific EC 4.1.1.96
term is proposed.

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

- Replaced the NEW spermidine-process support that quoted the UniProt `DR GO`
  line (a label restating an electronic annotation) with the curated function
  statement, the PTHR43727:SF1 classification and primary genetics from other
  bacteria: C. jejuni [PMID:22025614 "the carboxynorspermidine decarboxylase
  orthologue is responsible for synthesizing spermidine and not
  sym-norspermidine in vivo"] and B. thetaiotaomicron [PMID:27118128
  "carboxyspermidine decarboxylase is essential for synthesizing spermidine in
  B. thetaiotaomicron"].
- GO:0003824 catalytic activity changed from MARK_AS_OVER_ANNOTATED to
  TOO_GENERAL, matching the new Vibrio cholerae NspC (Q9KRL4) review; the term is
  true but entailed by the accepted carboxy-lyase activity.
- The GO:0008836 diaminopimelate decarboxylase REMOVE is now also backed by the
  PTHR43727 family review (interpro/panther/PTHR43727/PTHR43727-review.yaml),
  which judges the PAINT node PTN000159906 to need pruning at the NspC
  subfamily SF1. The V. vulnificus orthologue showed no activity with
  meso-diaminopimelate [PMID:19196710 "no activity with l -arginine, l -lysine,
  and meso -diaminopimelate"].
- No gene-level deep-research file exists for this gene; none was generated in
  this session (provider not run). The module and P. putida project
  OpenScientist reports were used for retrieval.
