# kdpE curation notes

## Evidence assessment

KdpE combines two separable activities: phosphorelay response-regulator activity
and sequence-specific regulatory DNA binding. In the E. coli system, KdpE with
an intact phosphorylation site is required for kdpFABC expression, and
phosphorylated KdpE binds the cognate DNA site [PMID:14534307, "kdpFABC
expression requires the corresponding response regulator KdpE with an intact
phosphorylation site"]. PSEPK Q88FE0 has the conserved receiver and DNA-binding
architecture [file:PSEPK/kdpE/kdpE-uniprot.txt].

## Curation decision

Two core-function entries represent the receiver/phosphorelay role and the
DNA-binding transcriptional-activation role independently. Generic DNA binding
and self-binding terms remain non-core or over-annotated where more informative
terms are present.

## 2026-11-01 re-review

- Provider deep research was not run in this pass; no deep-research file exists.
- GO:0000976 and GO:0003677 -> MODIFY to GO:0000987; GO:0005737 -> MODIFY to GO:0005829;
  GO:0006355 -> MODIFY to GO:0045893; GO:0042802 -> MODIFY to GO:0042803 (orthology with
  E. coli KdpE receiver-domain dimer, PMID:16322582).
- E. coli KdpE papers cited as orthology-based support (shared PTHR48111:SF50, receiver and
  OmpR/PhoB DNA-binding domains). The two KdpE core functions (GO:0000156, GO:0000987) remain
  separate.
