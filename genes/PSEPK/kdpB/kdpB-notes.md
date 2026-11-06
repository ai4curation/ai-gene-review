# kdpB curation notes

## Evidence assessment

PSEPK A0A140FWL1 is the P-type ATPase subunit of KdpFABC. Structural work on the
E. coli ortholog establishes the division of labor in which KdpA handles the
potassium pathway and ATP energy is harnessed by KdpB [PMID:28636601, "the
energy of ATP is harnessed by KdpB"]. UniProt independently identifies the
P-type ATPase family, ATP-binding region, and catalytic phosphorylation cycle
[file:PSEPK/kdpB/kdpB-uniprot.txt].

## Curation decision

ATP hydrolysis activity (GO:0016887) is KdpB's direct catalytic molecular
function. P-type potassium transmembrane transporter activity (GO:0008556) is a
property of the assembled pump, so KdpB contributes to it but does not provide
the complete activity independently.

## 2026-11-01 re-review pass

- Provider deep research was not run in this pass; the upgrade relies on the UniProt record
  (HAMAP/InterPro/NCBIfam family evidence) and cached E. coli ortholog publications, cited as
  orthology-based support.
- Every row now has a reason and verbatim support; correct-but-general terms changed to MODIFY
  with the specific term the gene already carries; a NEW part_of GO:0031004 (ISO from the E. coli
  ortholog) row added so the complex used in core_functions is reflected in annotations.
