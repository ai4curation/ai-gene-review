# Curation Notes: Mycobacterium phage L5 Gene 58 (gp58, Q05271)

## Overview
- **UniProt ID:** Q05271 (`VG58_BPML5`)
- **Gene Symbol:** `58`
- **Length:** 130 amino acids (14.4 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome immediately upstream of gene `57` (the TOPRIM primase catalytic core) and within the early replication module [PMID:8459766].

## Domain & Family Architecture
- **InterPro:**
  - `IPR036977` (`DNA_primase_Znf_CHC2`, DNA primase zinc finger CHC2-type superfamily)
  - `IPR002694` (`DNA_primase_Znf_bac/phage`, Bacterial/phage DNA primase CHC2-type zinc finger)
- **PANTHER:** `PTHR30313:SF2` (`DNA PRIMASE`)
- **Pfam:** `PF01807` (`Zn_ribbon_DnaG`)
- **SUPFAM:** `SSF57776` (`Zn-binding domain of primase-helicase`)

## Biological Role & Existing GOA Review
- L5 gp58 encodes the N-terminal CHC2-type zinc-ribbon DNA-binding domain of the phage DnaG-like DNA primase, while the adjacent downstream gene `57` encodes the catalytic TOPRIM core domain (`cd01029` / `PF13155`) [PMID:8459766].
- Review of existing GOA annotations:
  - `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000002`, `IPR002694`/`IPR036977`): **ACCEPT**. The CHC2 zinc-ribbon domain of DnaG-type primases binds single-stranded DNA templates and recognizes primase initiation sites.
  - `GO:0003899` (`DNA-directed RNA polymerase activity`, IEA, `GO_REF:0000002`, `IPR002694`): **MODIFY** to `GO:0003896` (`DNA primase activity`). `GO:0003899` is overly general; the domain is specifically a DnaG-type DNA primase subunit/domain (`PTHR30313:SF2`), so `GO:0003896` (`DNA primase activity`) is the appropriate specific child term.
  - `GO:0006260` (`DNA replication`, IEA, `GO_REF:0000002`, `IPR002694`/`IPR036977`): **MODIFY** to `GO:0039693` (`viral DNA genome replication`), which is the specific descendant process for a bacteriophage replication primase.
  - `GO:0008270` (`zinc ion binding`, IEA, `GO_REF:0000120`, `IPR002694`/`IPR036977`/`KW-0863`): **ACCEPT**. The conserved CHC2 motif coordinates a structural Zn2+ ion.
  - `GO:0046872` (`metal ion binding`, IEA, `GO_REF:0000043`, `KW-0479`): **MODIFY** to `GO:0008270` (`zinc ion binding`), which is already present in GOA and more specific.
- Add `NEW` entries for `GO:0003896` (`DNA primase activity`, `contributes_to` or `enables`) and `GO:0039693` (`viral DNA genome replication`, `involved_in`).
