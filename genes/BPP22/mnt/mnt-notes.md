# mnt (P03049) — Curation Notes

## Overview
- **Gene symbol**: `mnt`
- **UniProt ID**: `P03049` (`RMNT_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein Mnt (83 AA; 82 AA after initiator methionine removal)

## Sequence & Domain Architecture
- **Length**: 83 AA (`file:genes/BPP22/mnt/mnt-uniprot.txt`)
- **Quaternary structure**: Homotetramer in solution (`CC   -!- SUBUNIT: Binds DNA as a homotetramer.`, [PMID:7999761], [PMID:10426954]).
- **Domains**:
  - **N-terminal ribbon-helix-helix (RHH) DNA-binding domain (residues 2–52)**: `InterPro:IPR005569` (`Arc_DNA-bd_dom`), `InterPro:IPR013321` (`Arc_rbn_hlx_hlx`), `InterPro:IPR010985` (`Ribbon_hlx_hlx`), `Pfam:PF03869` (`Arc`). Forms an intertwined dimer with an antiparallel two-stranded beta-ribbon that contacts operator DNA (`PDB:1MNT`, [PMID:7999761]).
  - **C-terminal tetramerization domain (residues 53–83)**: `InterPro:IPR024421` (`Phage_P22_Mnt`), `Pfam:PF11423` (`Repressor_Mnt`). Forms a dimer of two antiparallel alpha-helical coiled coils with a right-handed twist (`PDB:1QEY`, [PMID:10426954]).

## Biological Function
- **Transcriptional repressor of the `immI` region (`Pant` promoter)**:
  - Mnt ("maintenance of lysogeny") is encoded in the `immI` region of phage P22 and maintains lysogeny by binding as a homotetramer to the `O_mnt` operator site overlapping the `Pant` promoter, repressing transcription of the rightward `arc`-`ant` operon and thereby preventing synthesis of the Ant antirepressor in lysogens ([PMID:6350606], [PMID:7999761], `file:genes/BPP22/mnt/mnt-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:6350606]** (Sauer et al., 1983, *Biochemistry*):
  > "The arc and ant genes are transcribed rightward from the Pant promoter, while mnt is transcribed leftward from a promotor that may overlap Pant. The Mnt protein apparently acts by binding to an operator site located immediately adjacent to the startpoint of Pant transcription."
- **[PMID:7999761]** (Burgering et al., 1994, *Nature*):
  > "Wild-type Mnt repressor of Salmonella bacteriophage P22 is a tetrameric protein of 82 residues per monomer. A C-terminal deletion mutant of the repressor denoted Mnt (1-76) is a dimer in solution."
- **[PMID:10426954]** (Nooren et al., 1999, *Nat Struct Biol*):
  > "The solution structure of its C-terminal tetramerization domain, which holds together the two dimeric DNA-binding domains, has been determined by NMR spectroscopy. This structure reveals an assembly of four alpha-helical subunits, consisting of a dimer of two antiparallel coiled coils with a unique right-handed twist."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (binds `O_mnt` operator via N-terminal RHH beta-sheet domain).
  2. `GO:0006355` (`regulation of DNA-templated transcription`, IEA, `GO_REF:0000002`) -> `MODIFY` to `GO:0032897` (`negative regulation of viral transcription`), as Mnt specifically represses viral transcription from `Pant`.
- **Proposed `NEW` annotations**:
  - `GO:0003700` (`DNA-binding transcription factor activity`, `enables`) — sequence-specific transcriptional repressor.
  - `GO:0032897` (`negative regulation of viral transcription`, `involved_in`) — represses transcription of the viral `arc` and `ant` genes from `Pant`.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cytoplasm.
