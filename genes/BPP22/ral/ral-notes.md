# ral (P14113) — Curation Notes

## Overview
- **Gene symbol**: `ral`
- **UniProt ID**: `P14113` (`RAL_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Antirestriction protein Ral (64 AA)

## Sequence & Domain Architecture
- **Length**: 64 AA (`file:genes/BPP22/ral/ral-uniprot.txt`)
- **Domains**:
  - `InterPro:IPR022759` (`Antirestriction_protein_Ral`), `Pfam:PF11058` (`Ral`)

## Biological Function
- **Antirestriction protein that modulates host Type I restriction-modification methyltransferase activity**:
  - Semerjian et al. ([PMID:2738922]) sequenced the P22 `PL` operon and demonstrated that P22 `ral` is both sequence-homologous and functionally analogous to coliphage lambda `ral`.
  - P22 Ral alleviates restriction of unmodified phage DNA by host Type I restriction-modification systems (such as EcoK / StyLT) by stimulating the DNA methyltransferase activity of the host enzyme on unmethylated target sites, allowing progeny phage to escape restriction cleavage ([PMID:2738922], `file:genes/BPP22/ral/ral-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:2738922]** (Semerjian et al., 1989, *Gene*):
  > "In addition, three new genes have been identified: ral, kil and arf. Genes ral and c3 are homologous, as well as functionally analogous, to lambda ral and cIII, respectively."
- **`file:genes/BPP22/ral/ral-uniprot.txt`**:
  > `CC   -!- FUNCTION: Ral interferes with the cleavage of DNA by E.coli EcoK restriction-modification system, by modifying the activity of the host methylase (By similarity). This modulation allows incoming, unmodified phages to escape the host's restriction system (PubMed:2738922). {ECO:0000250|UniProtKB:P03703, ECO:0000269|PubMed:2738922}.`

## GO Annotation Decisions
- **Existing GOA** (3 rows):
  1. `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`), which is already present on the record.
  2. `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`).
  3. `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA, `GO_REF:0000043`) -> `ACCEPT` (core biological process).
- **Proposed `NEW` annotations**:
  - `GO:0030234` (`enzyme regulator activity`, `enables`) — Ral modifies the activity of the host Type I restriction-modification methyltransferase to promote de novo methylation of unmodified phage DNA (`file:genes/BPP22/ral/ral-uniprot.txt`).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
