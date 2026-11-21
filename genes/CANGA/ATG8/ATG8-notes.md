# CANGA ATG8 manual review notes

## 2026-11-21

Reviewed the newly seeded *Candida glabrata* `ATG8` rows for the fungal
`PTHR10969` ATG8/LC3/GABARAP PAINT family follow-up.

### Inputs checked

- `Q6FXR8` is the CBS138/Nakaseomyces glabratus Atg8 member of `PTHR10969`;
  the cached `PTHR10969-entries.csv` has `Q6FXR8,Autophagy-related protein
  8,protein,284593,Candida glabrata`.
- The cached PAINT slice places six core ATG8 rows at the eukaryotic node
  `PTN000103522`: autophagosome membrane, phosphatidylethanolamine binding,
  autophagosome assembly, mitophagy, cellular response to nitrogen starvation,
  and autophagosome maturation. It places fungal-type vacuole membrane on the
  fungal node `PTN000861115`.
- The C. glabrata UniProt record curates the same PTHR10969 family membership
  and transfers the canonical Atg8 precursor/PE-conjugation and
  autophagosome/vacuole-membrane statements from budding yeast.
- PMID:27347716 is cached with full text. It shows that iron depletion induces
  C. glabrata mitophagy, that `CgATG8` expression rises with `CgATG32` before
  strong mitochondrial degradation, and that `CgATG1` and `CgATG11` are
  required for mtDHFR-GFP processing in iron-depleted medium.
- PMID:29385574 is abstract-only in the cache. The abstract reports ATG8-PE and
  increased `ATG8` expression in nutrient-stress conditions, supporting Atg8
  lipidation during C. glabrata autophagy-like stress.
- PMID:42305147, found in the 2024-2026 update search, is abstract-only in the
  cache. The abstract reports a C. glabrata `drs2` mutant with defective
  autophagy, but it does not name ATG8 and was kept as medium-relevance context
  rather than direct support for a row.

### Literature search

Searched the web on 2026-11-21 for `Candida glabrata ATG8`, `Q6FXR8`,
`CAGL0A04675g`, `CgATG8`, and combinations with autophagy and mitophagy. The
direct hits were the 2016 iron-depletion mitophagy paper (PMID:27347716), the
2018 vacuolar-protease/autophagy-like nutrient-stress paper (PMID:29385574),
and the newer 2026 Drs2 autophagy paper (PMID:42305147). I did not find direct
C. glabrata papers assaying ATG8-dependent Cvt delivery, piecemeal nuclear
microautophagy/nucleophagy, ER-phagy, vacuole-isolation membrane contact site
localization, lipid-droplet formation, or heat-induced vacuolar invagination.

### Curation decisions

- Accepted conserved Atg8 rows for autophagosome assembly, phagophore assembly
  site/autophagosome membrane, fungal-type vacuole membrane,
  phosphatidylethanolamine binding, protein tag activity, membrane fusion and
  vacuolar targeting. The C. glabrata protein is a compact fungal PTHR10969
  member and direct papers support Atg8-PE formation during autophagy-like
  nutrient stress plus mitophagy induction under iron depletion.
- Accepted the mitochondrial autophagy row and kept mitochondrial membrane as a
  non-core mitophagy-contextual location. C. glabrata iron-depletion mitophagy
  is directly demonstrated, but Atg8's central activity remains on autophagic
  membranes.
- Accepted the CGD `GO:0003674 molecular_function` ND row under the
  `INFERABLE` no-data rule because the more specific molecular functions in
  this review are all inferred from PAINT, budding-yeast transfer or conserved
  Atg8 sequence features.
- Modified generic `cytoplasm`, `vacuolar membrane`, `autophagy`, and
  `regulation of macroautophagy` to more informative descendants.
- Marked S. cerevisiae-only EnsemblFungi transfers as over-annotated when the
  C. glabrata evidence does not establish the exact pathway or secondary
  location: ER-to-Golgi transport, Cvt delivery, piecemeal microautophagy of
  the nucleus/nucleophagy, ER-phagy, VICS localization, lipid-droplet
  localization/formation and heat-induced regulation of vacuolar membrane
  invagination.
