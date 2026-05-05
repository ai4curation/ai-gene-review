# STM review notes

Review scope: Arabidopsis thaliana STM / SHOOT MERISTEMLESS, UniProt Q38874,
At1g62360. Files reviewed: `STM-ai-review.yaml`, `STM-goa.tsv`,
`STM-uniprot.txt`, `STM-deep-research-falcon.md`, local cached publications
referenced by GOA, and PANTHER family context `PTHR11850`.

Key synthesis:

- STM is a class I KNOX/TALE homeobox transcription factor. UniProt states it is
  required for shoot apical meristem formation and probably binds the DNA
  sequence 5'-TGAC-3' [file:ARATH/STM/STM-uniprot.txt "Required for shoot
  apical meristem (SAM) formation during embryogenesis"; "Probably binds to the
  DNA sequence 5'-TGAC-3'"].
- STM suppresses differentiation and promotes cell division in the meristem
  independently of WUS [PMID:12070094 "STM suppresses differentiation
  independently of WUS and is required and sufficient to promote cell division"].
- STM contributes to CLV3/stem-cell homeostasis with WUS at later developmental
  stages [PMID:12068101 "At later developmental stages, WUS promotes the level
  of CLV3 expression, together with STM"].
- STM/KNOXI activity activates cytokinin biosynthesis, including AtIPT7 induction
  and increased cytokinin levels [PMID:16139212 "activation of cytokinin
  biosynthesis mediates KNOXI function in meristem maintenance"].
- STM nuclear localization depends on BLH/BELL partner heterodimerization
  [PMID:16513846 "STM is targeted into the nuclear compartment through
  heterodimerization with BLH partner proteins"].
- STM trafficking is regulated by FTIP3/FTIP4 and is tied to nuclear recycling,
  plasma membrane localization, and intercellular trafficking [PMID:29742441
  "This facilitates STM recycling to the nucleus"; "STM localizes substantially
  to the plasma membrane, which promotes intercellular trafficking"].
- Generic `protein binding` rows were not treated as core functions. Targeted
  KNOX-BELL interaction evidence was modified to `protein heterodimerization
  activity`; high-throughput generic interaction rows were removed or marked
  over-annotated where they did not add mechanistic STM evidence.
- The RNA-binding GOA row was removed. The accessible PMID:17965274 text supports
  MPB2C as an RNA and HD motif binding protein, and UniProt describes STM RNA
  binding as "By similarity", not direct Arabidopsis STM evidence.
