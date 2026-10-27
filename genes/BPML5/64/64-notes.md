# Curation Notes: Mycobacterium phage L5 Gene 64 (gp64, Q05277)

## Overview
- **UniProt ID:** Q05277 (`VG64_BPML5`)
- **Gene Symbol:** `64`
- **Length:** 128 amino acids (14.4 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome immediately downstream of the DnaB-like replicative helicase gene (`65`) [PMID:8459766].

## Domain & Family Architecture
- **InterPro:** `IPR058243` (`Phage_VG64`, Phage Gene 64 Protein Family)
- **Pfam:** `PF25682` (`Phage_VG64`)

## Biological Role & GO Annotation Decisions
- L5 gp64 is a 128-amino-acid protein belonging to the conserved `Phage_VG64` family (`PF25682` / `IPR058243`), located immediately adjacent to the DnaB-like replicative DNA helicase `gp65`.
- Note: While the UniProt text record (`64-uniprot.txt`) lists an unverified `KW-0238` (`DNA-binding`) keyword, there are no GO annotations in `64-goa.tsv` (`existing_annotations` is empty in the stub), no InterPro/Pfam DNA-binding domain signature (`PF25682` is a phage family of unknown function), and no experimental characterization of gp64 DNA binding in the literature. Therefore, no speculative GO annotations are added, and the putative nucleic-acid-binding/replication-accessory hypothesis is captured in `suggested_questions` and `suggested_experiments`.
