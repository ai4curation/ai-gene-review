# cro (P09964) — Curation Notes

## Overview
- **Gene symbol**: `cro`
- **UniProt ID**: `P09964` (`RCRO_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein Cro (61 AA)

## Sequence & Domain Architecture
- **Length**: 61 AA (`file:genes/BPP22/cro/cro-uniprot.txt`)
- **Domains**:
  - `InterPro:IPR010982` (`Lambda_DNA-bd_dom_sf`)
  - `Pfam:PF14549` (`P22_Cro`)
  - Helix-turn-helix (HTH) DNA-binding motif at residues 13–32 (`FT   DNA_BIND 13..32 /note="H-T-H motif"`).
- **Structural biology**:
  - NMR solution structure (`PDB:1RZS`, [PMID:15062080]): P22 Cro adopts an all-alpha-helical five-helix bundle fold (unlike phage lambda Cro, which has a mixed alpha+beta fold with a C-terminal beta-hairpin), demonstrating structural evolution within the Cro superfamily.

## Biological Function
- **Transcriptional repressor of `PRM` and early lytic promoters (`PL`, `PR`)**:
  - P22 Cro binds specifically to the three operator sites in `OR` (`OR3`, `OR1`, `OR2`, in order of decreasing affinity; `KD` for `OR3` ~ 6 x 10^-9 M) as well as `OL` ([PMID:3954988], `file:genes/BPP22/cro/cro-uniprot.txt`).
  - By preferentially occupying `OR3`, Cro represses transcription of the `c2` repressor gene from `PRM` and down-regulates early transcription from `PL` and `PR` at higher concentrations, thereby committing the phage to the lytic cycle and enabling late lytic growth ([PMID:3954988], [PMID:11053393]).

## Key Literature & Verbatim Evidence
- **[PMID:3954988]** (Poteete et al., 1986, *J Mol Biol*):
  > "Cro protein binds specifically to the three repressor binding sites in the P22 right operator; in order of decreasing affinity, these are OR3, OR1, and OR2."
- **[PMID:15062080]** (Newlove et al., 2004, *Structure*):
  > "The folds of P22 Cro and lambda Cro share a three alpha helix fragment comprising the N-terminal half of the domain. However, P22 Cro's C terminus folds as two helices, while lambda Cro's folds as a beta hairpin."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "The early proteins are 24, a λ N homologue which functions as a transcriptional antiterminator, and Cro, which functions to inhibit transcription from P RM and generally down-regulate transcription from P L and P R , thereby favoring lytic development."

## GO Annotation Decisions
- **Existing GOA (`GO:0003677` DNA binding, IEA)**: `ACCEPT` (direct operator binding via HTH motif).
- **Proposed `NEW` annotations**:
  - `GO:0003700` (`DNA-binding transcription factor activity`, `enables`) — sequence-specific transcriptional repressor at `OR` and `OL`.
  - `GO:0032897` (`negative regulation of viral transcription`, `involved_in`) — represses transcription from `PRM`, `PL`, and `PR`.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cytoplasm.
