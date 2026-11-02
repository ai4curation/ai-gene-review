# Syt3 (rat) review notes

- 2026-10-28: Created review. fetch-gene resolved P40748 (SYT3_RAT, RGD:3805, GeneID 25731) as expected.
- No deep research API; manual synthesis in Syt3-deep-research-manual.md.
- Full text read: PMID:18508778, PMID:12860971, PMID:11823420. Abstract-only: 7791877, 10373432, 30545844, 9830048, 36261524, 17179206, 23999003.
- Key judgements:
  - Core MF: calcium ion sensor activity + Ca-dependent phospholipid binding + SNARE binding; positive regulation of vesicle fusion (in vitro, PMID:18508778).
  - Location: plasma membrane / synaptic membrane (pre and post), NOT synaptic vesicle [PMID:10373432 "synaptotagmin III is highly enriched in synaptic plasma membranes but not in synaptic vesicles"]. So exocytic vesicle IBA and transport vesicle membrane IEA marked over-annotated.
  - PMID:12860971 notes Syt3 was not detected in PC12 cells [PMID:12860971 "Syts III, IV, and VII were not detected at the level of sensitivity adequate for isoforms I and IX"]: the IMP row (regulation of Ca-dependent exocytosis) is fragment interference with other syts; claim still true via PMID:11823420/36261524, so accepted with caveat.
  - Response to calcium ion (IDA, in vitro fusion) is a GO over-annotation of an in vitro Ca response.
  - Positive regulation of dendrite extension (ISO from human): melanocyte "dendrites" are not neuronal dendrites (GO:0030425 is a neuron projection); human source rests on an overexpression screen (PMID:23999003, about SYT14L). Marked over-annotated, source defect POSSIBLE.
  - Protein binding rows: Gria2 -> ionotropic glutamate receptor binding; Syt1 -> protein heterodimerization activity.
- No NEW terms proposed: presynaptic replenishment/short-term plasticity (PMID:36261524) is knockout phenotype evidence only.
