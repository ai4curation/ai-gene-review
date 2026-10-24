# Curation Notes: Mycobacterium phage L5 Gene 65 (gp65, Q05279)

## Overview
- **UniProt ID:** Q05279 (`VG65_BPML5`)
- **Gene Symbol:** `65`
- **Length:** 268 amino acids (29.5 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome within the early DNA replication cluster (`gp56`–`gp65`) [PMID:8459766].

## Domain & Family Architecture
- **InterPro:**
  - `IPR007694` (`DNA_helicase_DnaB-like_C`, DnaB-like helicase C-terminal domain)
  - `IPR003593` (`AAA+_ATPase`, AAA+ ATPase domain)
  - `IPR027417` (`P-loop_NTPase`, P-loop containing nucleoside triphosphate hydrolase)
- **Pfam:** `PF03796` (`DnaB_C`, residues 24–260)
- **PROSITE:** `PS50213` (`DNAB`, DnaB-like helicase C-terminal domain profile, residues 21–261)
- **SUPFAM:** `SSF52540` (`P-loop containing nucleoside triphosphate hydrolases`)

## Biological Role & Existing GOA Review
- L5 gp65 encodes the C-terminal P-loop NTPase / RecA-like catalytic domain of a DnaB-type replicative DNA helicase (`PF03796` / `IPR007694` / `PS50213`), which couples ATP hydrolysis to double-stranded DNA unwinding at the phage replication fork.
- Review of existing GOA annotations:
  - `GO:0000166` (`nucleotide binding`, IEA, `GO_REF:0000043`, `KW-0547`): **MODIFY** to `GO:0005524` (`ATP binding`), which is already present on this entry and more specific.
  - `GO:0003678` (`DNA helicase activity`, IEA, `GO_REF:0000002`, `IPR007694`): **ACCEPT**. Directly supported by the DnaB-like helicase domain (`IPR007694`, `PF03796`, `PS50213`).
  - `GO:0003824` (`catalytic activity`, IEA, `GO_REF:0000117`, `ARBA:ARBA00027533`): **MODIFY** to `GO:0003678` (`DNA helicase activity`) and `GO:0016887` (`ATP hydrolysis activity`). `GO:0003824` is a root-level enzyme term that is far too general.
  - `GO:0005524` (`ATP binding`, IEA, `GO_REF:0000120`, `IPR007694`/`KW-0067`): **ACCEPT**. P-loop NTPase / DnaB helicase catalytic domain binds ATP.
  - `GO:0006260` (`DNA replication`, IEA, `GO_REF:0000002`, `IPR007694`): **MODIFY** to `GO:0039693` (`viral DNA genome replication`), the phage-specific descendant process.
- Propose `NEW` annotations:
  - `GO:0016887` (`ATP hydrolysis activity`, IEA, `file:BPML5/65/65-uniprot.txt`): DnaB-family AAA+/P-loop helicases hydrolyze ATP to drive translocation and DNA unwinding.
  - `GO:0003677` (`DNA binding`, IEA, `file:BPML5/65/65-uniprot.txt`): required for DNA helicase translocation along single-stranded DNA at the replication fork.
  - `GO:0039693` (`viral DNA genome replication`, IEA, `file:BPML5/65/65-uniprot.txt`): phage-specific DNA replication process replacing `GO:0006260`.
