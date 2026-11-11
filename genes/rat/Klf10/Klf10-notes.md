# Klf10 (rat) review notes

- 2026-10-28: fetch-gene resolved O08876 (KLF10_RAT, RGD:621652, GeneID 81813) as expected; 25 GOA rows.
- Read PMID:18406357 full text: Klf10 only appears in the ET-1 microarray/qPCR survey, a small (<2-fold)
  delayed increase [PMID:18406357 "The increases in expression of Klf9 and Klf10 were relatively small"].
  Supports the IEP response-to-endothelin row only; kept as non-core.
- PMID:20070857 (abstract only): TIEG1 represses Bmal1 via GC boxes; knockdown shortens period. Supports
  core repressor activity, nucleus, regulation of circadian rhythm.
- Core function chosen: GO:0001227 DNA-binding transcription repressor activity, RNA pol II-specific
  (Bmal1, Pepck, Smad7 targets; Sin3A recruitment via alpha-HRM, PMID:11438660). Activator activity
  (Smad2, Runx2; PMID:12244575, PMID:21559363) kept as non-core.
- General transcription-regulation rows MODIFIED to GO:0000122 (and GO:0045944 for the bidirectional
  RNA pol II term); GO:0000981 MODIFIED to GO:0001227 + GO:0001228.
- Phenotype-based ISO rows (bone mineralization, osteoclast differentiation) kept as non-core;
  cellular response to starvation marked over-annotated (fasting hyperglycemia is a KO phenotype, and
  Klf10 is glucose/feeding-induced); somatic stem cell maintenance UNDECIDED (source not identified).
- No NEW terms proposed.
