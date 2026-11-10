# Stxbp1 (rat, P61765) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Stxbp1` resolved P61765 (Swiss-Prot, RGD:3785, GeneID 25558); 107 GOA rows.
- No deep-research provider; literature synthesis in `Stxbp1-deep-research-manual.md`.
- Full text read: PMID:19255244, PMID:20801887, PMID:21193638, PMID:24532794, PMID:26030875,
  PMID:26876096. Everything else is abstract-only in the cache; PMC full text for PMID:22810233
  could not be retrieved (empty body from PMC).
- Extra papers fetched to check human donor rows used by ISO/IEA: PMID:12773094 (platelets),
  PMID:23091057 (sperm acrosome), PMID:17543282 (syntaxin trafficking).

### Key judgments

- Core: syntaxin-1 / SNARE binding; template (adaptor) for SNARE complex assembly; synaptic
  vesicle priming; SNARE-mediated fusion; neuroendocrine dense-core vesicle exocytosis
  [PMID:20801887 "Exocytosis in silenced PC-12 cells was fully rescued (to levels observed in native
  PC12 cells) by introducing a fluorescent fusion of wild type munc18"].
- "Regulation of" priming/exocytosis rows were modified to the process itself: Munc18-1 is part of
  the priming/fusion machinery (it templates SNARE assembly) rather than a modulator
  [PMID:19255244 "Munc18-1 binding to SNARE complexes mediates synaptic vesicle priming"].
- PMID:22810233 (RGD IDA/IGI) rows: vesicle membrane tethering activity, vesicle tethering complex
  and calcium-activated phospholipid scrambling conflict with the paper's own abstract (Syt1 does
  the docking; Munc18-1 acts after docking; no lipid scrambling assay). Marked over-annotated, not
  removed (full text not seen), with source_defects for RGD.
- Platelet degranulation/aggregation ISO/IEA rest on peptide-inhibition data in which Munc18c is
  the dominant SM protein [PMID:12773094]; marked over-annotated.
- KO-phenotype ISO rows (axon target recognition, neuron apoptosis, LTD, SV maturation,
  GABAergic negative regulation, IFN-gamma response) are downstream consequences of loss of
  release; marked over-annotated.
- No NEW rows proposed.
