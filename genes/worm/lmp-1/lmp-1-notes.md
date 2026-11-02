# lmp-1 review notes

## Session 1 (2026-10-28)

- fetch-gene resolved Q11117 (LMP1_CAEEL, reviewed; WBGene00003053; GeneID 180912). 13 GOA rows, all CC except one IBA BP.
- Literature compiled manually in lmp-1-deep-research-manual.md (no deep-research API keys).
- Key localization evidence: lysosomal / late endosome / gut granule (LRO) membranes, phagosomes, and a plasma-membrane pool
  [PMID:22916203 "In intestinal cells LMP-1::GFP localized to the basolateral plasma membrane"];
  [PMID:22225878 "including the plasma membrane"].
- PMID:23705068 (flagged as key by the batch): read; it only uses LMP-1::GFP as a lysosome marker
  ["By examining lysosomal markers LMP-1::GFP"], no information on LMP-1 function itself.
- PMID:20133524 (phagocytic vesicle IDA) is abstract-only; abstract does not mention LMP-1. Independent support from
  PMID:18256195 abstract ["UNC-108 co-localizes with RAB-5, RAB-7 and LMP-1 to the phagosome"].
- GO:0072594 establishment of protein localization to organelle (IBA) seeded by LAMP1 (NK-cell lytic granule perforin
  delivery) and LAMP2 (chaperone-mediated autophagy); neither context exists or is shown in worm -> MARK_AS_OVER_ANNOTATED.
- No molecular function is established; core function recorded as a location-based lysosome/LRO membrane glycoprotein
  without an MF term. No NEW terms proposed (mutant granule phenotype is not participation evidence).
