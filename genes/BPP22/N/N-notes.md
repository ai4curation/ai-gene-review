# N (P04891) — Curation Notes

## Overview
- **Gene symbol**: `N` (gene `24` in standard P22 genetic nomenclature; `REGN_BPP22`)
- **UniProt ID**: `P04891` (`REGN_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Antitermination protein N / gp24 (100 AA)

## Sequence & Domain Architecture
- **Length**: 100 AA (`file:genes/BPP22/N/N-uniprot.txt`)
- **Domains & Motifs**:
  - `InterPro:IPR057902` (`N_peptide`), `Pfam:PF25694` (`N_peptide`)
  - Arginine-rich basic RNA-binding motif (ARM, residues 14–32) that folds into a bent alpha-helix (residues 17–31, `FT   HELIX 17..31 /evidence="ECO:0007829|PDB:1A4T"`) upon adaptive binding to the major groove of the nascent `boxB` (`nut`) RNA hairpin (`PDB:1A4T`, [PMID:9501914]).

## Biological Function
- **RNA-binding transcriptional antiterminator of early phage operons**:
  - P22 N protein (gp24) is the functional and structural analog of coliphage lambda N ([PMID:3157001], [PMID:9501914], [PMID:11053393]).
  - It binds specifically to the nascent `boxB` stem-loop hairpin within the `nutL` and `nutR` (N-utilization) sites on early `PL` and `PR` transcripts via its N-terminal basic arginine-rich peptide, recruiting host Nus factors (NusA, NusB, NusE/S10, NusG) and modifying host RNA polymerase into a termination-resistant elongation complex that reads through intrinsic and Rho-dependent terminators to express delayed-early (middle) phage genes ([PMID:3157001], [PMID:9501914], [PMID:11053393], `file:genes/BPP22/N/N-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:9501914]** (Cai et al., 1998, *Nat Struct Biol*):
  > "We have determined the solution structure of a 15-mer boxB RNA hairpin complexed with a 20-mer basic peptide of the N protein involved in bacteriophage P22 transcriptional antitermination. Complex formation involves adaptive binding with the N peptide adopting a bent alpha-helical conformation that packs tightly through hydrophobic and electrostatic interactions against the major groove face of the boxB RNA hairpin, orienting the open opposite face for potential interactions with host factors and/or RNA polymerase."
- **[PMID:3157001]** (Franklin, 1985, *J Mol Biol*):
  > "Comparisons are made among DNA sequences upstream from terminators in both leftwards and rightwards early operons of related coliphages lambda, phi 21 and P22. These sequences include both left and right determinants of response to phage-coded antitermination proteins, "N", as well as the N structural genes themselves."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "The early proteins are 24, a λ N homologue which functions as a transcriptional antiterminator, and Cro, which functions to inhibit transcription from P RM and generally down-regulate transcription from P L and P R , thereby favoring lytic development."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0006353` (`DNA-templated transcription termination`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0031564` (`transcription antitermination`) and `GO:0050434` (`positive regulation of viral transcription`), because N prevents termination (antitermination) rather than causing transcription termination.
- **Proposed `NEW` annotations**:
  - `GO:0003723` (`RNA binding`, `enables`) — directly binds the nascent `boxB` RNA hairpin in `nut` sites (`PDB:1A4T`, [PMID:9501914]).
  - `GO:0031564` (`transcription antitermination`, `involved_in`) — mediates transcriptional antitermination of the `PL` and `PR` operons ([PMID:9501914], [PMID:11053393]).
  - `GO:0050434` (`positive regulation of viral transcription`, `involved_in`) — enables processive transcription of delayed-early viral genes ([PMID:11053393]).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
