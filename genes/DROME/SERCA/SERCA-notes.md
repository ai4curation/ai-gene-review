# SERCA (DROME, P22700) review notes

## Session 2026-10-28

- `just fetch-gene DROME SERCA` resolved P22700 (Swiss-Prot ATC1_DROME; FlyBase FBgn0263006;
  GeneID 49297). GOA has 37 rows. All 11 GOA PMIDs plus PMID:22952921 cached.
- No deep-research API keys; literature synthesis written by hand in `SERCA-deep-research-manual.md`.
- Full text available locally: PMID:22952921, 23434461, 24098595, 26205122, 28399403. Abstract only:
  PMID:15520268, 16899722, 19317464, 2148477, 23970561, 24807223, 33892078. PubMed MCP full-text
  for PMC6673814 (PMID:16899722) returned no body.

### Key points

- Core function: P-type Ca2+-ATPase pumping cytosolic Ca2+ into the ER/SR lumen
  [PMID:24807223 "SERCA, an endoplasmic reticulum (ER) calcium pump, is solely responsible for transporting cytosolic calcium into the ER lumen."].
- Only SERCA in the fly [PMID:23434461 "knockdown of Ca-P60A, the only SERCA expressed in Drosophila"].
- PMID:22952921 (photoreceptor lamina, Astorga et al. 2012): thapsigargin and sercaTS at 41 C reduce
  depolarization-induced FM dye labelling of photoreceptor boutons by about half/64%
  [PMID:22952921 "These results support the notion that Ca2+ released from the ER contributes to synaptic activity in the lamina."].
  This is a downstream (store-filling) role; it does not justify a NEW process annotation on SERCA by
  the NEW bar (SERCA does not perform exocytosis), so it is used only as background.

### Decisions worth flagging

- `GO:0045202 synapse` IEA (GO_REF:0000108) is inferred from the BP row neuromuscular synaptic
  transmission; a process phenotype cannot establish a location. REMOVE + source_defects (GO_CENTRAL).
- Generic `membrane`, `endomembrane system`, `calcium ion transport`, `calcium ion transmembrane
  transport` and the SR rows are MODIFIED to the specific terms the gene already carries
  (ER membrane, SR membrane, calcium ion transport from cytosol to ER).
- `stabilization of membrane potential` IGI (PMID:16899722): abstract does not mention membrane
  potential; full text not readable here. UNDECIDED.
- Notch-dependent developmental rows (stem cell differentiation, ISC homeostasis, follicle cell
  development) are indirect consequences of defective Notch receptor maturation; MARK_AS_OVER_ANNOTATED.
- `adaptive thermogenesis` IMP (PMID:28399403): the heat-producing experiments were on THADA mutants;
  SERCA itself performs the uncoupled ATP hydrolysis, so the involvement is plausible, but fly-specific
  SERCA thermogenesis was not directly measured. KEEP_AS_NON_CORE.
