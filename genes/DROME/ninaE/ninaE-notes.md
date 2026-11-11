# ninaE notes

## 2026-10-28 session

- fetch-gene resolved P06002 (OPS1_DROME, FlyBase FBgn0002940, GeneID 42367); 44 GOA rows.
- No deep-research API keys; literature summarised manually in `ninaE-deep-research-manual.md`.
- PMID:22105348 (Pocha et al. 2011, Crumbs/MyoV) read in full: it concerns Rh1 as MyoV cargo
  transported to the rhabdomere [PMID:22105348 "Loss of MyoV in crb mutant photoreceptors was accompanied by defective transport of the MyoV cargo Rh1 to the light-sensing organelle, the rhabdomere."].
  It supports rhabdomere localisation and dependence of Rh1 delivery on MyoV; it is not the
  source of any ninaE GOA row.

## Decisions

- Core: GO:0008020 G protein-coupled photoreceptor activity, in GO:0030265 PLC-activating opsin
  signalling (Gq/NorpA) [PMID:7759511], located in rhabdomere membrane.
- Generic GPCR rows (GO:0004930, GO:0007186, GO:0071482) MODIFIED to the specific photoreceptor
  terms already present on the gene.
- Bare protein binding with Arr2 (PMID:15014127) MODIFIED to arrestin family protein binding.
- membrane / plasma membrane MODIFIED to rhabdomere membrane.
- INAD signalling complex kept as non-core: Rh1 association with the signalplex is reported but
  is thought to be transient.
- Behavioural/developmental rows (phototaxis, optomotor, thermotaxis, rhabdomere development,
  photoreceptor morphogenesis) kept as non-core.
- "negative regulation of compound eye retinal cell programmed cell death" (PMID:15014127) is a
  phenotype-derived inference from a dominant degeneration allele: over-annotated.
- "adult locomotory behavior" (PMID:16111941, abstract only, gap-climbing visual task): over-annotated.
- NEW: GO:0016918 retinal binding (chromophore Schiff base at K319).
