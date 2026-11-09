# tusC (E. coli K-12) curation notes

## Sources checked

- UniProtKB record (genes/ECOLI/tusC/tusC-uniprot.txt), GOA table, and the cached
  abstracts of PMID:16387657 and PMID:16472754 (both abstract-only in the cache).
- No provider deep-research file was generated for this gene; the review rests on
  the two primary papers that define the Tus relay and the UniProt record.

## Findings

- TusC was identified with the other tus genes in a genome-wide screen for
  2-thiouridylation of mnm5s2U [PMID:16387657 "We identified five genes yhhP,
  yheL, yheM, yheN, and yccK (named tusA, tusB, tusC, tusD, and tusE,
  respectively) that are essential for 2-thiouridylation of mnm5s2U"].
- It is a subunit of the TusBCD heterohexamer [PMID:16472754 "forming a
  heterohexamer composed of a dimer of the heterotrimer"]; the sulfur-carrying
  cysteine of the complex is on TusD, not TusC [PMID:16472754 "only Cys78, in the
  TusD subunit, participates in sulfur transfer during the s2U modification
  process"].
- TusC is therefore modelled as a structural subunit that contributes to the
  complex's sulfur-carrier activity (core function uses
  contributes_to_molecular_function GO:0097163), not as an independent carrier.
- The broad GO:0008033 tRNA processing row is MODIFIED to GO:0002143.
