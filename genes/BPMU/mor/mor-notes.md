# Curation Notes for Escherichia phage Mu mor (P23848)

## Summary of Gene Function
- **Gene symbol**: `mor` (locus tag `Mup17`; UniProt `P23848`, Middle operon regulator Mor)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Middle operon regulator Mor (`Mup17`, 129 aa) is a sequence-specific homodimeric winged helix-turn-helix DNA-binding transcription activator (`GO:0001216` `DNA-binding transcription activator activity`, `GO:0003677` `DNA binding`) that activates transcription from the middle promoter `Pm` of bacteriophage Mu (`GO:0045893` `positive regulation of DNA-templated transcription`, `GO:0019083` `viral transcription`) [PMID:14729670, file:BPMU/mor/mor-uniprot.txt].
- **Mechanism of Middle Promoter Activation**: Mor forms a domain-swapped homodimer whose C-terminal HTH domains bind an imperfect dyad-symmetric sequence centered at position `-43.5` of the `Pm` promoter (which lacks a canonical `-35` element) and recruits bacterial RNA polymerase through direct protein-protein contacts with the C-terminal domains of the host RNAP alpha (`RpoA`) and sigma70 (`RpoD`) subunits [PMID:14729670, file:BPMU/mor/mor-uniprot.txt]. Activation of `Pm` drives expression of the middle operon, including the late transcription activator `C` (`Mup21`), which is required for the transition to late viral gene expression [file:BPMU/mor/mor-uniprot.txt].

## Literature & Reference Notes
- **PMID:14729670** (Kumaraswami et al., 2004, J Mol Biol, "Crystal structure of the transcriptional activator protein Mor of bacteriophage Mu"): Reports the 2.2 Å crystal structure of the Mor homodimer, revealing an N-terminal two-helix dimerization bundle linked via a beta-strand to a C-terminal HTH DNA-binding domain, and summarizes how Mor activates `Pm` via contacts with the C-terminal domains of the alpha and sigma subunits of bacterial RNA polymerase.

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA): `ACCEPT`.
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `NEW` `GO:0001216` (`DNA-binding transcription activator activity`, `enables`): Captures Mor's direct molecular function as a sequence-specific transcriptional activator at `Pm`.
- `NEW` `GO:0045893` (`positive regulation of DNA-templated transcription`, `involved_in`): Captures Mor's positive regulation of `Pm` transcription.
- `NEW` `GO:0019083` (`viral transcription`, `involved_in`): Captures Mor's essential role in phage Mu middle operon transcription.
