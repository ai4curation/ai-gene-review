# Curation Notes for Escherichia phage lambda `ninG` (P03770)

## Summary of Gene Product
Bacteriophage lambda recombination protein NinG (`ninG`, also known as `rap` [recombination adept with plasmid] or `ORF204`, UniProt `P03770`, 204 AA, `InterPro:IPR008713` `Phage_lambda_NinG`) is a phage-encoded branched-DNA structure-specific endonuclease (Holliday junction / D-loop crossover junction endodeoxyribonuclease, functionally analogous to *Escherichia coli* RuvC / RusA) encoded in the `ninR` region between `P` and `Q` [PMID:9811830, "In the presence of manganese ions, Rap acts as an endonuclease that cleaves at the branch point of Holliday and D-loop substrates."; file:LAMBD/ninG/ninG-uniprot.txt]. During phage lambda homologous recombination, NinG resolves Holliday junctions and branched D-loop intermediates (`GO:0008821`, `crossover junction endodeoxyribonuclease activity`; `GO:0006310`, `DNA recombination`) [PMID:9811830; PMID:15223317, "Here, we demonstrate that Rap can mediate symmetrical resolution of 50 bp and chi Holliday structures containing larger homologous cores."].

## Structural and Mechanistic Architecture
- **N-terminal zinc-binding / DNA-recognition domain and C-terminal catalytic nuclease domain**: Contains conserved cysteine/histidine motifs in the N-terminal half and a C-terminal metal-dependent endonuclease domain (`InterPro:IPR008713`, `Pfam:PF05766`) that cleaves four-way Holliday junctions and three-way branched DNA structures [PMID:9811830; PMID:15223317].

## Review of Existing GO Annotations
- `existing_annotations` is currently empty (`[]`) in GOA for `P03770`.
- **Core function**: `GO:0008821` (`crossover junction endodeoxyribonuclease activity`) directly involved in `GO:0006310` (`DNA recombination`), supported by biochemical characterization of purified Rap/NinG on synthetic Holliday junction and D-loop substrates [PMID:9811830; PMID:15223317] and its conserved `Phage_lambda_NinG` (`InterPro:IPR008713`) classification in UniProt [file:LAMBD/ninG/ninG-uniprot.txt].
