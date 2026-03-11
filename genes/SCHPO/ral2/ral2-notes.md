# ral2 (SPBC21.05c) - Research Notes

## Gene Identity

- UniProt: P15258
- Systematic name: SPBC21.05c
- 611 amino acids, 69.8 kDa
- Contains 3 Kelch repeats (aa 43-91, 96-149, 175-224) and a Kelch-type beta propeller domain
- Also contains SKP1/BTB/POZ superfamily domain
- Phosphorylated at Ser-604 [PMID:18257517]

## Core Function

Ral2 is a Ras1-Scd pathway protein essential for mating/conjugation and cell morphology in S. pombe. It functions upstream of Ras1 in a signaling pathway that controls both mating pheromone response and elongated cell shape via the Ras1-Scd1-Cdc42 axis.

### Key Evidence

- ral2 deletion mutants are spherical (not rod-shaped), have no mating activity, and do not respond to mating pheromone, phenocopying ras1- mutants [PMID:2586528 "The disruptants showed the same phenotype as the original ral2 isolates, i.e., they had spherical cells, had no detectable mating activity, and exhibited no response to the mating pheromone"]
- Activated ras1 (ras1Val-17) rescues ral2 mutants, placing ral2 upstream of ras1 [PMID:2586528 "Either multiple copies or even a single copy of the ras1Val-17 allele...restored rodlike cell morphology and ability to respond to the mating factor to ral2 mutants"]
- Genetic epistasis: ral1, ral2, ras1 function in a common pathway in that order [PMID:3071741 "the ral1, ral2 and ras1 genes may function in a common pathway in that order"]
- Multiple copies of ral2 or ral3 partially rescue ral1- strains [PMID:3071741]
- ral2 deletion increases cell width, along with other Cdc42-pathway deletions (scd1, scd2, rga4, ras1, efc25) [PMID:21551073]

### Pathway Context

The Ras1 signaling pathway in S. pombe:
- **Morphology branch**: Ras1 -> Scd1 (GEF for Cdc42) -> Cdc42 -> Shk1 (PAK kinase) -> cell polarity
- **Mating branch**: Ras1 -> Byr2 -> MAPK cascade -> mating gene expression
- Ral2 acts upstream of Ras1, likely facilitating Ras1 activation
- The Kelch repeats in ral2 mediate protein-protein interactions with pathway components

### Protein Interactions (from BioGRID)
- Interacts with Gef1 (Cdc42 GEF) and Skp1 (SCF ubiquitin ligase component)
- The P. oryzae homolog PoRal2's kelch domain is sufficient for interaction with Scd1, Gef1, and Mst50 [PMID:34354729, Frontiers in Plant Science 2021]

## Localization

- Endoplasmic reticulum by high-throughput assay [PMID:16823372 - HDA evidence, global ORFeome localization study]
- Cytosol by phylogenetic inference (IBA) - but this is from the peroxiredoxin family assignment, likely incorrect

## Critical Issue: PANTHER Family Assignment

Ral2 is assigned to PANTHER family PTHR43503 (Peroxiredoxin family, Prx6 subfamily). This appears to be an INCORRECT family assignment:

1. Ral2 is 611 AA with Kelch repeats - peroxiredoxins are typically ~200 AA with thioredoxin folds
2. Ral2 has no catalytic cysteine residues characteristic of peroxiredoxins
3. Ral2's InterPro domain annotations are Kelch-type beta propeller (IPR015915) and SKP1/BTB/POZ superfamily (IPR011333) - not thioredoxin/peroxiredoxin domains
4. All IBA annotations (peroxidase activity GO:0004601, cytosol GO:0005829, cell redox homeostasis GO:0045454) derive from this likely incorrect PANTHER family grouping
5. The IEA annotation for cellular oxidant detoxification (GO:0098869) also derives from GO_REF:0000108 logical inference, likely downstream of the same incorrect family

## Molecular Function

The specific molecular function of ral2 is not well characterized at the biochemical level. It is NOT a GEF, GAP, or kinase. Based on its kelch repeat domain and genetic interactions, it likely functions as a **signaling adaptor/scaffold** that facilitates Ras1 activation, possibly by:
- Bringing together pathway components via kelch-mediated protein-protein interactions
- Facilitating the action of a Ras GEF on Ras1
- The ND (no biological data) annotation for MF is appropriate given the lack of biochemical characterization

## Vegetative Growth

ral2 deletion does NOT affect vegetative growth - only mating and cell morphology are impaired [PMID:2586528].
