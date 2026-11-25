# Rac1 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Rac1` resolved Q6RUV5 (RAC1_RAT, Swiss-Prot; RGD:619755; GeneID 363875),
  as expected. GOA file is keyed to Q6RUV5, 202 annotation rows.
- No deep-research key; wrote `Rac1-deep-research-manual.md` by hand.
- Sequence check: rat, human and mouse RAC1 identical (192/192)
  [file:rat/Rac1/Rac1-bioinformatics/RESULTS.md]. All ISO/ISS rows are therefore sound as
  transfers; decisions turn on the biology of each term.
- PMID:20472934 (Dovas et al. 2010): RhoGDIalpha pulldowns from rat embryo fibroblast lysate
  retain Rac1 ["When Ser-34 was mutated to Asp, there was significantly reduced RhoGDIα binding
  to RhoA (by around 75%) but not Rac1 or Cdc42."]. Used as support for Rho GDI binding.

### Decisions

- Core MF: GO:0003925 G protein activity (switch). GTPase activity rows (EXP, IDA, IBA, IEA,
  ISO) MODIFIED to G protein activity, which is_a GTPase activity (checked with OAK). GTP
  binding kept.
- Bare protein binding (4 rows) REMOVED per policy; the Arhgdia row (Q5XI73) MODIFIED to Rho
  GDP-dissociation inhibitor binding instead.
- GABA-ergic synapse IMP row (SynGO, PMID:25284783): a mutant phenotype cannot establish a
  location; same action as the IDA/EXP rows, with a WRONG_EVIDENCE_CODE CHECK source defect.
- PMID:20696765 abstract/title say human glioma cells; RGD/UniProt annotate rat. Protein is
  identical, claims are true for Rac1, but the taxon of the experiment should be checked; raised
  as a suggested question rather than as a defect because the full text is not available.
- Developmental/organismal ISO phenotype rows from MGI marked over-annotated (downstream
  consequences of Rac1 loss); cytoskeletal/migratory ones kept as non-core.
- No NEW rows proposed: the core terms are already present in GOA.
