# MAX2 (ORE9/PPS/KAI1, At2g42620, UniProt Q9SIM9) curation notes

Context: `strigolactone_signaling_shoot_branching` module. Falcon deep research failed (all providers);
notes from cached publications.

## Identity and complex
- F-box/LRR protein; F-box binds ASK1 [PMID:11487692 "The F-box motif of ORE9 interacts with ASK1 (Arabidopsis Skp1-like 1), a component of the plant SCF complex."].
- SCF(MAX2) in planta, nuclear, acts locally at node [PMID:17346265 "Myc-epitope-tagged MAX2 interacts with the core SCF subunits ASK1 and AtCUL1 in planta."].

## Strigolactone signalling
- SMXL6/7/8 co-IP with MAX2, MAX2-dependent SL-induced SMXL6 ubiquitination [PMID:26546446 "Collectively, these data indicate that the D53-like SMXLs are subject to D14- and MAX2-dependent degradation in response to SL signaling."].
- D14-MAX2-ASK1 SL-induced complex [PMID:27479325].

## Karrikin signalling
- [PMID:21555559 "karrikin signaling requires the F-box protein MAX2"]; SMAX1 vs SMXL6/7/8 division of labour [PMID:26546447].

## Other phenotypes (non-core)
- Senescence (ore9) [PMID:11487692]; photomorphogenesis/germination (pps) [PMID:17951458];
  drought, cuticle [PMID:24198318]; auxin transport [PMID:16546078]; WRKY41 ubiquitination in
  freezing tolerance [PMID:37622245 "MAX2 ubiquitinates WRKY41, thus marking it for cold-induced degradation"].

## Curation decisions
- ubiquitin ligase complex -> MODIFY to SCF ubiquitin ligase complex; ubiquitin-dependent protein
  catabolic process -> MODIFY to SCF-dependent proteasomal term.
- protein binding (D14) -> MODIFY to GO:1990756; HT Y2H rows -> REMOVE.
- NEW: GO:1990756 ubiquitin-like ligase-substrate adaptor activity; GO:1902348 cellular response to
  strigolactone; GO:0080167 response to karrikin.
