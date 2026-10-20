# Curation Notes for Salmonella phage P22 `eaa` (Q03544)

## Summary of Gene Product
`eaa` encodes protein EaA (UniProt `Q03544`, 317 amino acids, 35.5 kDa) of *Salmonella* phage P22 [PMID:11053393]. Located in the early leftward (`P_L`) `ea` accessory region between `int` and `erf`, EaA was originally identified by SDS-PAGE as one of the early phage-encoded proteins synthesized in UV-irradiated *Salmonella* cells upon P22 infection [PMID:11053393, PMID:12562822].

## Molecular Function, Biological Process, and Domain Context
- **Genomic context and dispensability**: The `ea` region (`int` to `erf`) is non-essential for P22 lytic growth or lysogeny under standard laboratory conditions [PMID:11053393, PMID:12562822].
- **Conserved domains**: Sequence analysis in `file:genes/BPP22/eaa/eaa-uniprot.txt` indicates that EaA contains an N-terminal MazZ-like dATP/dGTP diphosphohydrolase domain (`IPR007538` `dATP/dGTP_dipphydrolase_MazZ`, `PF04447` `dATP-dGTP_PPHyd`) and a C-terminal domain of unknown function (`IPR007539` `DUF551`, `PF04448` `DUF551`). While homologous phage proteins with the `PF04447` domain have been implicated in nucleotide pool modulation during host takeover or anti-defense, P22 EaA itself has not been biochemically assayed, so `core_functions` is left empty (`[]`).

## Subcellular Localization
- No transmembrane helices or signal peptides are predicted in `file:genes/BPP22/eaa/eaa-uniprot.txt`, and subcellular localization has not been experimentally determined.

## Domain Architecture
- InterPro: `IPR007538` (`dATP/dGTP_dipphydrolase_MazZ`), `IPR007539` (`DUF551`)
- Pfam: `PF04447` (`dATP-dGTP_PPHyd`), `PF04448` (`DUF551`)
