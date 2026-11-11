# rexA (P68924) - Curation Notes

## Overview
- **Gene symbol**: `rexA`
- **UniProt ID**: `P68924` (`REXA_LAMBD`)
- **Protein name**: Protein rexA (279 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Cytoplasmic sensor/activator of the two-component RexAB abortive infection (superinfection exclusion) system**: `rexA` and `rexB` are co-transcribed with `cI` from the lysogenic maintenance promoter `PRM` (`P_M`) in lambda lysogens and exclude superinfecting phages such as coliphage T4 `rII` mutants, as well as certain phage T5, T7, and lambda `ren` mutants [PMID:2530135, "The rexA and rexB genes of bacteriophage lambda are expressed from the prophage and cause the exclusion of many superinfecting mutant phages."; PMID:1372278, "The rexA and rexB genes of bacteriophage lambda encode a two-component system that aborts lytic growth of bacterial viruses."].
- **Mechanism of RexB channel activation**: According to the Parma et al. model validated by genetic and physiological studies, cytoplasmic RexA senses a macromolecular signal produced during superinfecting phage replication/recombination (such as protein-DNA complexes) and binds at a stoichiometry of at least two RexA molecules per membrane-embedded RexB monomer to open the RexB inner-membrane ion channel [PMID:11790759, "The model of Parma et al. ( 13 ) predicts that RexB protein forms an inner membrane pore that is opened upon direct interaction with at least two RexA proteins"].
- **Physiological consequences of RexA-mediated RexB activation**: Opening of the RexB pore collapses the proton motive force (membrane potential), causes a precipitous drop in intracellular ATP, halts macromolecular synthesis (DNA, RNA, protein) and amino acid transport, and arrests host cell growth (or causes altruistic cell death), thereby aborting lytic multiplication of the superinfecting phage [PMID:2530135, "However, induction of rexA in the presence of limiting rexB activity caused an immediate cessation of cell growth. All macromolecular synthesis abruptly ceased and amino acid transport was severely inhibited. Intracellular levels of adenosine 5'-triphosphate also dropped."; PMID:11790759, "We found that the Rex system can channel lysogenic cells into an arrested growth phase that gives an overall protective ability to the host despite some associated killing."].

## Review of Existing GO Annotations
- `rexA` currently has **no existing GO annotations** in GOA (`existing_annotations: []`).
- Based on the published experimental literature (`PMID:11790759`, `PMID:2530135`, `PMID:1372278`), RexA's core function is binding and activating the prophage-encoded inner-membrane pore RexB (`GO:0005515` protein binding / ion channel regulator) in the host cell cytoplasm (`GO:0030430`) to mediate superinfection exclusion (`GO:0098670`).
