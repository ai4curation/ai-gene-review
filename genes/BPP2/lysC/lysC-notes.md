# Bacteriophage P2 Gene lysC (Spanin, outer lipoprotein subunit gpLysC; UniProt Q8LTD0)

## Overview
Gene **lysC** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 96-amino-acid outer-membrane lipoprotein spanin subunit (o-spanin; 10.6 kDa precursor, mature residues 23–96 after signal peptidase II cleavage at `Cys-23`; `UniProt:Q8LTD0`) (`PMID:8051010`, `file:BPP2/lysC/lysC-uniprot.txt`). Encoded in an overlapping reading frame at the 3' end of `lysB`, LysC is lipid-modified at `Cys-23` (N-acyl-S-diacylglyceryl-cysteine) and sorted to the inner leaflet of the *Escherichia coli* host outer membrane (`UniProtKB-SubCell:SL-0376`), where it forms the periplasm-spanning two-component spanin complex with the inner-membrane subunit LysB (`UniProt:P51770`) to disrupt the outer membrane during the final step of host cell lysis (`PMID:8051010`, `file:BPP2/lysC/lysC-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:8051010** (*Functions involved in bacteriophage P2-induced host cell lysis and identification of a new tail gene.*):
  - Sequenced the P2 lysis region containing `lysC` overlapping `lysB`.
- **UniProtKB Q8LTD0 (`file:BPP2/lysC/lysC-uniprot.txt`)**:
  - `"Component of the spanin complex that disrupts the host outer membrane and participates in cell lysis during virus exit."`
  - Subcellular location: `"Host cell outer membrane; Lipid-anchor"` (`SL-0376`).

## Curation Decisions
- **Molecular Function**:
  - No experimental or computational GO annotations are currently assigned in GOA; `existing_annotations` and `core_functions` are therefore left empty pending experimental characterization.
- **Biological Process**:
  - `GO:0031640` (`killing of cells of another organism`, IEA): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`).
  - `GO:0044659` (`viral release from host cell by cytolysis`): **NEW** supported by `file:BPP2/lysC/lysC-uniprot.txt`.
- **Cellular Component**:
  - `GO:0020002` (`host cell plasma membrane`, IEA from `GO_REF:0000044` with `supporting_entities: [UniProtKB-SubCell:SL-0376]`): Note that `GO_REF:0000044` maps `SL-0376` (`Host cell outer membrane`) conservatively to `GO:0020002` (`host cell plasma membrane`) or `GO:0044163` (`host cell outer membrane` — let's check if `GO:0044163` is in the ontology or if `GO:0020002` is the standard GO term; let's check via `validate_batch.py`!).
