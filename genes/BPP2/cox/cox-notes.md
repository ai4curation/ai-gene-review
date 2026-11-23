# Bacteriophage P2 Gene cox (Excisionase / Repressor protein Cox; UniProt P07695)

## Overview
Gene **cox** (*control of excision*) of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a multifunctional 91-amino-acid winged-helix DNA-binding protein (10.3 kDa; `UniProt:P07695`) that acts as both the developmental switch repressor (functional analog of phage lambda Cro) and the architectural recombination directionality factor / excisionase (functional analog of phage lambda Xis) (`PMID:3475531`, `PMID:2826134`, `file:BPP2/cox/cox-uniprot.txt`).
1. **Transcriptional repression (`Pc` and `Pe`)**: Cox binds the `Pc` promoter region to inhibit synthesis of the immunity repressor C (preventing lysogenization and promoting lytic growth) and negatively autoregulates the early lytic promoter `Pe` (`PMID:2826134`).
2. **Prophage excision (`attL` x `attR`)**: Cox binds `attP`/`attR` DNA and bends it to promote excisive site-specific recombination in concert with P2 integrase (`Int`) while inhibiting integrative recombination (`PMID:3475531`, `PMID:2826134`, `file:BPP2/cox/cox-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:3475531** (*DNA sequences of bacteriophage P2 early genes cox and B and their regulatory sites.*):
  - Sequenced `cox`: `"Part of the early operon of the temperate phage P2 of Escherichia coli, including genes cox (involved in prophage excision) and B (required for phage specific DNA synthesis), was sequenced."`
  - `"In addition, the data provide amino acid sequences for the Cox and B proteins of 91 and 166 residues, respectively"`
- **PMID:2826134** (*The cox protein of bacteriophage P2 inhibits the formation of the repressor protein and autoregulates the early operon.*):
  - Demonstrated transcriptional regulation: `"The results show that the Cox protein negatively autoregulates the early operon and inhibits the formation of the repressor C."`
  - `"The presence of a cloned cox gene drastically stimulated the formation of free phage from a P2-lysogen and dramatically reduced the frequency of lysogenization after P2 infection. We conclude that the pleiotropic effects of the cox (control of excision) gene, namely effects on lysogenization, formation of free phage and site-specific P2 recombination, can be explained by the effect of the Cox protein on the activity of the promoters Pc and Pe."`
- **UniProtKB P07695 (`file:BPP2/cox/cox-uniprot.txt`)**:
  - Documents dual function in transcriptional repression of `Pc`, negative autoregulation of `Pe`, and architectural role in excisive recombination (`attL`/`attR` $\rightarrow$ `attP`/`attB`).

## Curation Decisions
- **Molecular Function**:
  - `GO:0003677` (`DNA binding`, IEA): **MODIFY** to `GO:0000976` (`transcription cis-regulatory region binding`) and `GO:0001217` (`DNA-binding transcription repressor activity`).
  - Add `NEW` for `GO:0001217` (`DNA-binding transcription repressor activity`) and `GO:0000976` (`transcription cis-regulatory region binding`) supported by `PMID:2826134`.
- **Biological Process**:
  - Add `NEW` for `GO:0045892` (`negative regulation of DNA-templated transcription`) and `GO:0032359` (`provirus excision`) supported by `PMID:2826134` and `PMID:3475531`.
- **Cellular Component**:
  - Add `NEW` for `GO:0030430` (`host cell cytoplasm`).
