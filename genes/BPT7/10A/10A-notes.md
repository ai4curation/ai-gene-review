# Gene 10A (P19726) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `10A`
- **UniProtKB accession**: `P19726` (`CAPSA_BPT7`, Major capsid protein 10A)
- **Length**: 345 amino acids (~36.5 kDa; N-terminal initiator Met1 cleaved, mature chain residues 2–345)
- **Alternative products**: `P19726-1` (`10A`, canonical major capsid protein) and `P19727-1` (`10B`, minor capsid protein produced by -1 ribosomal frameshifting).
- **Domains**: `HAMAP:MF_04119` (`Phage_capsid_T7`), `InterPro:IPR039009`, `Pfam:PF21703` (`Major_capsid_10`, HK97-like fold).

## Literature & Function Summary
- **Major capsid protein forming the T=7 levo icosahedral shell** (`PMID:17437718`, `PMID:20962334`, `PMID:25313071`, `PMID:8528255`):
  - Agirrezabala et al. (2007) (`PMID:17437718`), Ionel et al. (2011) (`PMID:20962334`), and Guo et al. (2014) (`PMID:25313071`) demonstrated that 415 copies of gp10 (predominantly ~90% gp10A and ~10% gp10B) adopt a canonical HK97-like fold (N-arm, E-loop, P-domain, A-domain) and self-associate into 60 hexamers and 11 pentamers (with the 12th fivefold vertex occupied by the gp8 portal ring) to build the T=7 *levo* icosahedral capsid.
  - During maturation from procapsid to mature DNA-filled head, gp10 subunits undergo rigid-body rotation and unskewing of hexamers, expanding the capsid shell and increasing its stability (`PMID:20962334`, `PMID:25313071`).
- **Translational frameshifting near the 3' end of gene 10** (`PMID:1938901`):
  - Condron et al. (1991) (`PMID:1938901`) showed that a -1 ribosomal frameshift at overlapping phenylalanine codons near the 3' end of gene 10A mRNA occurs at ~10% frequency to produce the 398-AA minor capsid protein gp10B (`P19727`).

## Curation Decisions
- **ACCEPT**:
  - `GO:0042802` (`identical protein binding`, IPI `PMID:17437718` and IPI `PMID:8528255`).
- **KEEP_AS_NON_CORE**:
  - `GO:0075523` (`viral translational frameshifting`, IEA `GO_REF:0000043`): describes the mRNA frameshift event generating the alternative 10B isoform rather than the function of canonical gp10A.
- **MODIFY**:
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120`) -> `GO:0039620` (`T=7 icosahedral viral capsid`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`, IDA `PMID:20962334`).
  - `GO:0039620` (`T=7 icosahedral viral capsid`, `part_of`, IDA `PMID:25313071`).
  - `GO:0019069` (`viral capsid assembly`, `involved_in`, IDA `PMID:25313071`).
