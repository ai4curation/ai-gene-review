# Irs2 (rat) review notes

- 2026-10-28: fetch-gene resolved F1MAL5 (RGD:69316, GeneID 29376), as expected; 71 GOA rows.
- Deep research API unavailable; literature summary in `Irs2-deep-research-manual.md`.
- Full text read: PMID:18406357 (ET-1 IEG in cardiomyocytes; Irs2 only a passing finding), PMID:22912850
  (14-3-3 binding, Fao cells). Abstract only: PMID:12850498, PMID:12891559, PMID:16574657, PMID:9495343, PMID:7675087.
- Core: RTK (IR/IGF1R) adaptor activity (GO:0005068) + PI3K activator activity (GO:0141038), cytosol,
  insulin and IGF-1 receptor signalling, PI3K/PKB signal transduction.
- General adaptor terms (signaling adaptor, protein-macromolecule adaptor, protein kinase binding) MODIFY to GO:0005068;
  cytoplasm -> cytosol; cellular response to insulin stimulus -> insulin receptor signaling pathway;
  ARBA "positive regulation of transport" -> positive regulation of D-glucose import across plasma membrane.
- Grb2 IPI (WITH RGD:619758, the rat Grb2 id used in GRB2 IBA donor lists) on protein domain specific binding -> SH2 domain binding.
- Downstream physiological ISO terms from mouse (B cell, mesenchymal proliferation, lipid/glucose metabolism,
  insulin secretion, brain/mammary development): KEEP_AS_NON_CORE as pleiotropic consequences of IRS-2 signalling.
- Sun et al. 1995 (IRS-2 cloning) is PMID:7675087.
