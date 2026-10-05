# tomt (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: tomt encodes transmembrane O-methyltransferase (TOMT/mercury), an ER/Golgi/basolateral membrane protein required in zebrafish hair cells for TMC1/2 trafficking into stereocilia and mechanotransduction-complex assembly. Its catechol O-methyltransferase-like activity is retained as by-similarity biochemical context, but the core zebrafish role is hair-cell mechanotransduction machinery organization independent of methyltransferase activity.
- Key UniProt support: Required for transportation of TMC1 and TMC2 proteins into the mechanically sensitive stereocilia.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.


## 2026-09-20 full-gene re-review

Reviewed all 20 source rows and the Falcon report body. The actual PTHR43836 lineage (separate JSON, full response hash retained) places A0A193KX02 below all four positive IBDs at PTN000053580. Restored broad developmental and metabolic assertions: a mechanotransduction role does not establish loss of another ancestral function. PMID:28534737 full text shows that H183A is a **mouse** TOMT transgene, and mouse TOMT/TMC1 were co-immunoprecipitated in HEK cells. Do not transfer mammalian active-site substitutions to zebrafish or claim experimentally proven zebrafish chaperone activity. Native physiological methyl acceptor remains unknown.

Endocytosis remains UNDECIDED: PMID:10526320 is abstract-only, interprets rapid FM1-43 loading; PMID:11549711 establishes MET-channel permeation in mouse cochlear cells, and PMID:28534737 directly attributes mercury to absent MET/Tmc trafficking. Independent vesicle-uptake evidence in the original target study must be assessed. A focused parent-coordinated adjudication was requested; no duplicate report was run. Development/behavior/location positives were assessed individually and retained with assay scope. No NEW assertions were added; all source fields preserved.
