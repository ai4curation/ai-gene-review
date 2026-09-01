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
- Ral2's Kelch repeats suggest a protein-interaction role, but its direct partners
  and biochemical mechanism in this pathway remain unresolved.

### Protein Interactions (from BioGRID)
- Interacts with Gef1 (Cdc42 GEF) and Skp1 (SCF ubiquitin ligase component)
- The P. oryzae homolog PoRal2's kelch domain is sufficient for interaction with Scd1, Gef1, and Mst50 [PMID:34354729, Frontiers in Plant Science 2021]

## Localization

- PomBase records endoplasmic-reticulum `is_active_in` from the proteome-wide YFP
  screen, but the accessible PMID:16823372 record contains only the study-level abstract,
  not the Ral2-specific image or classification. No independent Ral2 localization
  study was recovered, so this annotation is UNDECIDED and ER is not used as a core
  location. [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding
  to approximately 90% of the fission yeast proteome, by tagging each ORF with the
  yellow fluorescent protein."]

## PANTHER family interpretation

PTHR43503 is a heterogeneous family whose broad ancestral node contains peroxiredoxins,
but Ral2 is correctly classified in subfamily PTHR43503:SF2, "NEGATIVE REGULATOR OF
SPORULATION MDS3-RELATED," together with fungal Mds3/Pmd1-like Kelch proteins. PAINT
records explicit IRD function-loss edges from the peroxiredoxin ancestor to the
Ral2/Mds3 node PTN005166285 for peroxidase activity, cytosol, and cell redox homeostasis.
Those obsolete redox-related GOA rows have now disappeared. The current IBA to regulation
of conjugation is placed directly on PTN005166285 and is grounded by Ral2's own
experimental phenotype; it is accepted rather than treated as a bad family transfer.

## Molecular Function

The specific molecular function of ral2 is not well characterized at the biochemical level. It is NOT a GEF, GAP, or kinase. Based on its kelch repeat domain and genetic interactions, it likely functions as a **signaling adaptor/scaffold** that facilitates Ras1 activation, possibly by:
- Bringing together pathway components via kelch-mediated protein-protein interactions
- Facilitating the action of a Ras GEF on Ras1
- The ND (no biological data) annotation for MF is appropriate given the lack of biochemical characterization

## Vegetative Growth

ral2 deletion does NOT affect vegetative growth - only mating and cell morphology are impaired [PMID:2586528].

## 2026-09-01 re-review journal

- Refreshed Ral2 through `just fetch-gene SCHPO ral2 --force`. Current GOA contains
  five unique review tuples. Removed four stale redox/peroxiredoxin-derived annotations
  that are no longer present in GOA, consistent with the PAINT IRD loss edges at the
  Ral2/Mds3 node.
- Accepted the new GO:0031137 IBA because the node is grounded by Ral2's direct mating
  phenotype; Ral2 appearing in its own source set is expected experimental grounding,
  not circularity. [PMID:2586528 "The disruptants showed the same phenotype as the
  original ral2 isolates, i.e., they had spherical cells, had no detectable mating
  activity, and exhibited no response to the mating pheromone, but their vegetative
  growth was apparently normal."]
- Accepted GO:2000784 because activated ras1Val-17 restores rod-like morphology to
  ral2 mutants, directly placing Ral2 upstream of Ras1 in cell-polarity control.
  [PMID:2586528 "Either multiple copies or even a single copy of the ras1Val-17 allele,
  which is an activated form of ras1, restored rodlike cell morphology and ability
  to respond to the mating factor to ral2 mutants."]
- Refreshed PMID:2586528 and PMID:2038319 through the publication wrapper. PMC exposes
  only abstract and document furniture for these scanned-era articles, so their
  records remain abstract-only and no unavailable full-text claims are made.
- Launched a focused OpenScientist job for the GO:0005783 ER HDA through
  `just gene-hypothesis-research`. The external provider produced no output or
  artifact after more than one hour and the polling process was stopped. With no
  gene-specific image available from PMID:16823372 and no independent localization
  study recovered, the annotation remains UNDECIDED rather than being accepted,
  rejected, or used as a core location.
