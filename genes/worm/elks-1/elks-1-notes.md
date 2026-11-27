# elks-1 (C. elegans ELKS/CAST, UniProt O44490) - curation notes

## Identity
- TrEMBL entry O44490_CAEEL, 836 aa, ORF F42A6.9; annotated as "ELKS/RAB6-interacting/CAST family
  member 2" and, by ARBA, as a presynapse protein [file:worm/elks-1/elks-1-uniprot.txt]. Sole worm
  ELKS/CAST ortholog (vertebrates: ERC1/ERC2).
- The worm protein shares only ~20% identity with its two rat homologs, with the C terminus most
  conserved, including the terminal Ile-Trp-Ala PDZ-binding motif
  [PMID:15976086 "sharing 20% identity to its two rat homologs with the C terminus exhibiting the most similarity"].

## Core biology: auxiliary active-zone scaffold that binds the RIM PDZ domain
- ELKS-1 is an active-zone protein: antibody staining gives discrete puncta in the nerve ring and
  both nerve cords, restricted (within the nervous system) to synapse-rich regions and more punctate
  than the vesicle marker RAB-3, and strongly colocalized with RIM
  [PMID:15976086 "Immunocytochemistry revealed that ELKS staining is found in discrete puncta in the nerve ring and along both the ventral and dorsal cords"; "we found that RIM and ELKS are strongly colocalized throughout the C. elegans nervous system"].
  Note the qualifier "In the nervous system, ELKS staining was restricted to synapse-rich regions",
  which implies additional non-neuronal staining and is the likely basis of the basement-membrane
  annotation from the same paper.
- Direct interaction with RIM: the C-terminal 126 residues of ELKS-1 bind a GST fusion of the RIM
  PDZ domain, but not GST alone [PMID:15976086 "the ELKS protein bound to GST-PDZ"].
- ELKS-1 is dispensable for release in the worm: elks deletion animals are as aldicarb-sensitive as
  wild type (whereas unc-10 nulls are fully resistant) and show no physiological defect
  [PMID:15976086 "elks mutants exhibit neither the behavioral nor the physiological"; "animals that lack RIM ( md1117 ) are completely aldicarb resistant"].
- Reciprocal localization is redundant: RIM localizes normally without ELKS-1 and vice versa, and
  ELKS-1 is also not required for UNC-13 localization
  [PMID:15976086 "These data demonstrate that ELKS is not required for localizing RIM or UNC-13 to the active zone in vivo"].
  ELKS-1 does contribute: a minimal RIM PDZ+C2A construct requires ELKS-1 for targeting, so ELKS-1
  plays a real but non-essential part in RIM localization
  [PMID:15976086 "These data suggest that ELKS plays a role, but not an essential role"].
- The authors' summary of the worm function is an auxiliary scaffold
  [PMID:15976086 "Our data indicate that ELKS acts as an auxiliary scaffolding protein at the active zone"].

## Unrelated genetic-interaction annotation
- In an RNAi modifier screen, elks-1 depletion suppressed the embryonic lethality of rfl-1(or198ts)
  and partially restored CUL-3 neddylation
  [PMID:19528325 "We observed partial restoration of CUL-3 neddylation reproducibly after depletion of six of the nine specific suppressors: most clearly with elks-1"].
  The authors state the mechanism is unclear and possibly indirect
  [PMID:19528325 "Their influence on neddylation could be direct and of importance to other processes that involve neddylation, or it could be indirect"], so the
  deneddylation-regulation annotation is treated as an over-annotation.

## GO decisions (summary)
- Core: structural constituent of the presynaptic active zone (GO:0098882) in the active-zone
  cytoplasmic component (GO:0098831, GO:0048786), acting through PDZ-domain binding to RIM
  (GO:0030165).
- Active-zone-structure maintenance (GO:0048790, IBA) is retained as non-core: the vertebrate
  scaffold role is plausible for family membership, but worm elks-1 nulls have normal behaviour,
  normal physiology and normal RIM/UNC-13 localization.
- Basement membrane (IDA) is retained as non-core, extra-synaptic staining.
