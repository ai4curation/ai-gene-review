# 23 (P57020) — Curation Notes

## Overview
- **Gene symbol**: `23`
- **UniProt ID**: `P57020` (`REGQ_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Putative antitermination protein gp23 (207 AA), closely homologous (201/207 identical AA) to phage lambda late gene regulator Q.

## Sequence & Domain Architecture
- **Length**: 207 AA (`file:genes/BPP22/23/23-uniprot.txt`)
- **Sequence identity to lambda Q**: Differ by only 6 of 207 amino acids ([PMID:12562822]).
- **Domains & Motifs**:
  - `HAMAP:MF_04158` (`Antitermination_lambda`)
  - `InterPro:IPR003222` (`Antitermntn`), `InterPro:IPR038500` (`Antitermination_sf`), `Pfam:PF03589` (`Antiterm`)
  - `InterPro:IPR036410` (`HSP_DnaJ_Cys-rich_dom_sf`) — C4-type zinc finger domain at residues 118–147 (`FT   ZN_FING 118..147`, coordinating `Zn(2+)` via Cys-118, Cys-121, Cys-144, Cys-147).
  - Helix-turn-helix DNA-binding motif at residues 171–192 (`FT   DNA_BIND 171..192`).

## Biological Function
- **DNA-binding late transcriptional antiterminator**:
  - P22 gp23 controls late lytic gene expression from `PR'` via a transcription antitermination mechanism identical to that of phage lambda Q ([PMID:11053393], [PMID:12562822], `file:genes/BPP22/23/23-uniprot.txt`).
  - gp23 binds a specific DNA Q-binding element (`QBE`) between the `-35` and `-10` elements of the late promoter `PR'`, engages host RNA polymerase (interacting with the RpoB beta-flap and sigma-70 domain 4) while paused early in elongation, and becomes a persistent subunit of the elongation complex (aided by host NusA) to read through the `tR'` terminator into the late lysis and morphogenetic operon (`file:genes/BPP22/23/23-uniprot.txt`, [PMID:11053393]).

## Key Literature & Verbatim Evidence
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "Late gene expression is regulated, as it is in coliphage λ, in an antitermination-dependent mechanism involving gp23, a Q homologue ( 48 )."
  > "The antitermination protein involved in controlling late transcription is defined by gene 23 . This protein is highly homologous to a group of proteins from phage including lambda, HK022, and PS34, suggesting similar types of regulation of late-gene expression in these morphologically different viruses."
- **[PMID:12562822]** (Pedulla et al., 2003, *J Bacteriol*):
  > "For example, the DNA sequences of gene 23 of P22 (where a number of the differences between P22 and P22-pbi lie) and gene Q of phage λ differ by 30 nucleotides, but the encoded protein sequences differ by only six amino acids."

## GO Annotation Decisions
- **Existing GOA** (6 rows):
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (binds the `QBE` DNA element at `PR'`).
  2. `GO:0006353` (`DNA-templated transcription termination`, IEA, `GO_REF:0000120`) -> `MODIFY` to `GO:0031564` (`transcription antitermination`), as gp23 prevents rather than promotes termination.
  3. `GO:0006355` (`regulation of DNA-templated transcription`, IEA, `GO_REF:0000120`) -> `MODIFY` to `GO:0031564` (`transcription antitermination`) and `GO:0050434` (`positive regulation of viral transcription`).
  4. `GO:0008270` (`zinc ion binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (conserved C4 zinc finger `Cys118-Cys121-Cys144-Cys147`).
  5. `GO:0031564` (`transcription antitermination`, IEA, `GO_REF:0000104`) -> `ACCEPT` (core biological process).
  6. `GO:0046872` (`metal ion binding`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0008270` (`zinc ion binding`).
- **Proposed `NEW` annotations**:
  - `GO:0050434` (`positive regulation of viral transcription`, `involved_in`) — activates expression of the late lytic operon by antitermination.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
