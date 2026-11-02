# sieB (P03762) - Curation Notes

## Overview
- **Gene symbol**: `sieB`
- **UniProt ID**: `P03762` (`SIEB_LAMBD`)
- **Protein name**: Superinfection exclusion protein B (184 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Prophage-encoded inner-membrane superinfection exclusion protein**: The `sieB` gene of bacteriophage lambda is located between `ral` and `N` in the left arm of the genome, but is transcribed rightward (counter to `PL` transcription) from its own promoter that remains active in the lysogenic state [PMID:8335629, "The sieB gene of coliphage lambda was also identified. The promoter for lambda sieB was identified by homology to that of P22 sieB."].
- **Homology to Salmonella phage P22 SieB and abortive infection mechanism**: Lambda SieB (184 AA) is an integral inner-membrane protein (predicted two transmembrane helices, residues 7-27 and 36-56) homologous to the SieB protein of Salmonella phage P22 (`PMID:8335629`). In lysogens, SieB aborts lytic development of superinfecting heteroimmune lambdoid and related phages (such as *Salmonella* phage P22 `sieB`-sensitive derivatives or coliphage Mu/lambdoid hybrids lacking the `esc` escape determinant) by arresting macromolecular synthesis at the onset of late gene expression. An overlapping reading frame or alternative translation initiation (`esc`) produces a shorter truncated polypeptide that antagonizes SieB exclusion, allowing lambda itself to escape its own SieB system during lytic infection.

## Review of Existing GO Annotations
- `GO:0033644` (host cell membrane, IEA, `GO_REF:0000044`): **ACCEPT**. SieB contains two N-terminal transmembrane helices and localizes to the host cell inner membrane, where it mediates superinfection exclusion (`GO:0098670`).
