# C1 (P03041) — Curation Notes

## Overview
- **Gene symbol**: `C1` (`c1`)
- **UniProt ID**: `P03041` (`RPC1_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein C1 (92 AA), the homolog and functional analog of phage lambda cII.

## Sequence & Domain Architecture
- **Length**: 92 AA (`file:genes/BPP22/C1/C1-uniprot.txt`)
- **Quaternary structure**: Homotetramer composed of four identical ~10 kDa subunits ([PMID:1385814], `file:genes/BPP22/C1/C1-uniprot.txt`).
- **Domains**:
  - `InterPro:IPR001387` (`Cro/C1-type_HTH`), `InterPro:IPR010982` (`Lambda_DNA-bd_dom_sf`)
  - `InterPro:IPR007933` (`Transcrpt_activ_CII`), `Pfam:PF05269` (`Phage_CII`)
  - Helix-turn-helix (HTH) motif at residues 26–45 (`FT   DNA_BIND 26..45 /note="H-T-H motif"`).

## Biological Function
- **Sequence-specific DNA-binding transcriptional activator**:
  - P22 C1 is the functional and sequence homolog of coliphage lambda cII ([PMID:1385814], [PMID:11053393]).
  - It binds as a homotetramer to a direct-repeat `TTGCN6TTGC/T` (`TTGC(N6)TTGY`) motif flanking the `-35` region of two phage promoters—`PRE` (promoter for repressor establishment, driving `c2` synthesis) and `Pa23` (an antisense promoter within gene `23`, the P22 `Q` homolog, inhibiting late lytic gene expression)—activating RNA polymerase transcription from both promoters in vitro and in vivo to establish lysogeny ([PMID:1385814], [PMID:11053393], `file:genes/BPP22/C1/C1-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:1385814]** (Ho et al., 1992, *J Biol Chem*):
  > "P22 C1 was shown to be a tetrameric protein composed of four identical subunits with M(r) = 10,000. Moreover, we identified and characterized two P22 C1-dependent phage promoters, P(RE) and Pa23, whose function was completely dependent on C1 both in vitro and in vivo. These two promoters share a common TTGCN6TTGC/T motif in their -35 regions, the same motif recognized by the analogous phage lambda transcription activator protein cII."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "The P22 homologue, C1 protein, also stimulates transcription from P RE and P a23 (the P22 Q homologue) ( 27 ). P22 C1-binding sites, have the recognition motif TTGC(N 6 )TTGY ( 27 ), while its homologue, lambda CII protein, recognizes TTGC(N 6 )TTGC ( 28 )."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (directly binds `TTGCN6TTGC/T` repeats at `PRE` and `Pa23`).
  2. `GO:0006355` (`regulation of DNA-templated transcription`, IEA, `GO_REF:0000002`) -> `MODIFY` to `GO:0050434` (`positive regulation of viral transcription`), as C1 specifically activates viral transcription from `PRE` and `Pa23`.
- **Proposed `NEW` annotations**:
  - `GO:0003700` (`DNA-binding transcription factor activity`, `enables`) — sequence-specific transcriptional activator.
  - `GO:0050434` (`positive regulation of viral transcription`, `involved_in`) — activates transcription from phage promoters `PRE` and `Pa23`.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cytoplasm.
