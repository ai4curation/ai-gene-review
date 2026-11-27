# Gene 10B (P19727) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `10B`
- **UniProtKB accession**: `P19727` (`CAPSB_BPT7`, Minor capsid protein 10B)
- **Length**: 398 amino acids (~41.8 kDa; N-terminal initiator Met1 cleaved, mature chain residues 2–398)
- **Alternative products**: `P19727-1` (`10B`, minor frameshift isoform) and `P19726-1` (`10A`, canonical major capsid protein).
- **Domains**: `HAMAP:MF_04119` (`Phage_capsid_T7`), `InterPro:IPR039009`, `Pfam:PF21703` (`Major_capsid_10`, residues 1–341) plus a unique 57-residue C-terminal extension (residues 342–398, `file:genes/BPT7/10B/10B-uniprot.txt`).

## Literature & Function Summary
- **Minor capsid protein produced by -1 ribosomal frameshifting** (`PMID:1938901`, `PMID:20962334`):
  - Condron et al. (1991) (`PMID:1938901`) demonstrated that a -1 ribosomal frameshift near the 3' end of the gene 10A coding region (at overlapping Phe codons) occurs during ~10% of translation events, extending the polypeptide by 53 amino acids in the -1 frame to generate the 398-AA minor capsid protein gp10B (`P19727`).
  - Incorporated alongside gp10A (~40–45 copies of gp10B and ~370–375 copies of gp10A per capsid, totaling 415 subunits) into the T=7 *levo* icosahedral capsid shell, with its C-terminal extension exposed on the outer capsid surface (`PMID:20962334`, `file:genes/BPT7/10B/10B-uniprot.txt`).

## Curation Decisions
- **KEEP_AS_NON_CORE**:
  - `GO:0075523` (`viral translational frameshifting`, IEA `GO_REF:0000043`): describes the translational frameshift mechanism generating gp10B from gene 10 mRNA rather than the structural function of mature gp10B.
- **MODIFY**:
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120`) -> `GO:0039620` (`T=7 icosahedral viral capsid`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`, IDA `PMID:20962334`).
  - `GO:0039620` (`T=7 icosahedral viral capsid`, `part_of`, IDA `PMID:20962334`).
  - `GO:0019069` (`viral capsid assembly`, `involved_in`, IDA `PMID:20962334`).
