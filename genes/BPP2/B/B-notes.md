# Bacteriophage P2 Gene B (Replication protein B / gpB; UniProt P07696)

## Overview
Gene **B** of *Escherichia phage P2* (`BPP2`) encodes the 166-amino-acid early replication protein gpB (19.0 kDa; `UniProt:P07696`), required for phage-specific lagging-strand DNA synthesis (`PMID:3475531`). gpB belongs to the phage P2 B replication protein family (`InterPro:IPR009652` / `PF06841`) and functions as a replicative helicase loader/interactor that interacts with the *Escherichia coli* host DnaB helicase (`PMID:3475531`, `file:BPP2/B/B-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:3475531** (*DNA sequences of bacteriophage P2 early genes cox and B and their regulatory sites.*):
  - Sequenced the P2 early operon covering `cox` and `B`: `"Part of the early operon of the temperate phage P2 of Escherichia coli, including genes cox (involved in prophage excision) and B (required for phage specific DNA synthesis), was sequenced."`
  - Determined protein size: `"In addition, the data provide amino acid sequences for the Cox and B proteins of 91 and 166 residues, respectively"`
  - Noted similarity to DnaB-interacting proteins: `"Slight structural similarities between the P2 Cox protein and the analogous Xis protein of phage lambda were noted and the P2 B gene product was compared with proteins that interact with the DnaB protein of E. coli."`
- **UniProtKB P07696 (`file:BPP2/B/B-uniprot.txt`)**:
  - Function: `"Required for lagging-strand synthesis during lytic DNA replication."`

## Curation Decisions
- **Molecular Function**:
  - No specific molecular function term is directly assayed in the cached literature; `core_functions` therefore records the biological process (`GO:0039693`) and cellular location (`GO:0030430`) without asserting a molecular function term.
- **Biological Process**:
  - `GO:0006260` (`DNA replication`, IEA) and `GO:0071897` (`DNA biosynthetic process`, IEA): **MODIFY** to `GO:0039693` (`viral DNA genome replication`).
  - `GO:0039693` (`viral DNA genome replication`): **NEW** supported by `PMID:3475531` and `file:BPP2/B/B-uniprot.txt`.
- **Cellular Component**:
  - `GO:0030430` (`host cell cytoplasm`): **NEW** as gpB recruits host DnaB during cytoplasmic phage DNA replication in *E. coli* (`PMID:3475531`).
