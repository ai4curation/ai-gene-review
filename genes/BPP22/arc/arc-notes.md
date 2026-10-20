# arc (P03050) — Curation Notes

## Overview
- **Gene symbol**: `arc`
- **UniProt ID**: `P03050` (`RARC_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein Arc (53 AA)

## Sequence & Domain Architecture
- **Length**: 53 AA (`file:genes/BPP22/arc/arc-uniprot.txt`)
- **Quaternary structure**: Homodimer in solution; two dimers bind cooperatively to a 21-bp operator site as a homotetramer (`CC   -!- SUBUNIT: Binds DNA as a homotetramer.`, [PMID:2377232], [PMID:8107872], [PMID:9927650]).
- **Domains**:
  - Founding archetype of the ribbon-helix-helix (RHH) transcription factor superfamily (`InterPro:IPR005569` `Arc_DNA-bd_dom`, `InterPro:IPR013321` `Arc_rbn_hlx_hlx`, `InterPro:IPR010985` `Ribbon_hlx_hlx`, `Pfam:PF03869` `Arc`).
  - Residues 8–14 of each monomer intertwine to form an antiparallel two-stranded beta-sheet ("ribbon") that inserts into the major groove of each DNA subsite, flanked by N-terminal arms and two alpha-helices (helix A: residues 16–29; helix B: residues 35–46) (`PDB:1ARQ`, `PDB:1BDT`, `PDB:1PAR`, [PMID:2377232], [PMID:8107872]).

## Biological Function
- **Transcriptional repressor of the `Pant` promoter during lytic growth**:
  - Arc ("antirepressor control") is co-transcribed with `ant` from the strong `Pant` promoter in the `immI` region early after infection ([PMID:6350606], [PMID:8107872]).
  - Once synthesized, two Arc dimers bind cooperatively to a 21-bp operator (`O_arc`) overlapping `Pant` (between the `-10` and `-35` hexamers), negatively autoregulating `arc` and repressing `ant` (antirepressor) synthesis during lytic growth ([PMID:6350606], [PMID:8107872], `file:genes/BPP22/arc/arc-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:8107872]** (Raumann et al., 1994, *Nature*):
  > "Transcription of the ant gene during lytic growth of bacteriophage P22 (ref. 1) is regulated by the cooperative binding of two Arc repressor dimers to a 21-base-pair operator site. Here we report the co-crystal structure of this Arc tetramer-operator complex at 2.6 A resolution."
  > "each Arc dimer uses an antiparallel beta-sheet to recognize bases in the major groove."
- **[PMID:9927650]** (Smith & Sauer, 1999, *Proc Natl Acad Sci U S A*):
  > "Arc is a small, homodimeric repressor of the ribbon–helix–helix family of transcription factors ( 1 ). In the cocrystal structure, Arc dimers bind to adjacent subsites of a 21-bp operator, and the β-sheet and N-terminal arms of an Arc dimer are positioned to contact a DNA subsite ( 2 )."
- **[PMID:2377232]** (Breg et al., 1990, *Nature*):
  > "It shows a strongly intertwined dimer, in which residues 8-14 of different monomers form an antiparallel beta-sheet."
- **[PMID:6350606]** (Sauer et al., 1983, *Biochemistry*):
  > "This region includes the ant gene, which encodes the P22 antirepressor protein, and the mnt and arc genes, which encode proteins that negatively regulate antirepressor synthesis."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (directly binds the 21-bp `Pant` operator via its antiparallel beta-sheet).
  2. `GO:0006355` (`regulation of DNA-templated transcription`, IEA, `GO_REF:0000002`) -> `MODIFY` to `GO:0032897` (`negative regulation of viral transcription`), as Arc specifically represses viral transcription from `Pant`.
- **Proposed `NEW` annotations**:
  - `GO:0003700` (`DNA-binding transcription factor activity`, `enables`) — sequence-specific transcriptional repressor.
  - `GO:0032897` (`negative regulation of viral transcription`, `involved_in`) — represses transcription of the viral `arc` and `ant` genes from `Pant`.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cytoplasm.
