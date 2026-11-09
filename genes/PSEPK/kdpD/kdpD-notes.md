# kdpD curation notes

## Evidence assessment

KdpD is a membrane sensor kinase with large cytosolic input and transmitter
domains. E. coli experiments establish that membrane-bound KdpD controls
KdpE-dependent kdpFABC expression and describe four transmembrane segments plus
cytoplasmic domains [PMID:14534307, "The membrane-bound sensor kinase KdpD
consists of an N-terminal input domain"]. UniProt predicts the corresponding
multi-pass topology for PSEPK Q88FD9 [file:PSEPK/kdpD/kdpD-uniprot.txt].

## Curation decision

The full-length protein is assigned to the plasma membrane. The ARBA cytoplasm
annotation likely reflects its extensive cytosolic domains, but `located_in
cytoplasm` misstates the location of the integral membrane gene product and is
therefore removed.

## 2026-11-01 re-review

- Provider deep research was not run in this pass; no deep-research file exists.
- Thin rows upgraded with reasons and support. Correct-but-general terms (GO:0004673,
  GO:0016301, GO:0016740, GO:0016772, GO:0007165, GO:0016020) changed from
  KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED to MODIFY with the specific term already on the gene.
- E. coli KdpD papers (PMID:9099740, PMID:8223625, PMID:7499326, PMID:14534307) cited as
  orthology-based support; Q88FD9 shares PANTHER PTHR45569:SF1 and KdpD N-terminal/TM signatures.
- Open question: whether the E. coli N-terminal atypical serine kinase activity (KdpB S162
  phosphorylation, PMID:38622146) is conserved in KT2440; not annotated.
