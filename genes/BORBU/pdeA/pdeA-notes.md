# PdeA review notes

## Enzyme and construct distinction

B31 BB_0363 (O51338) is the EAL-family branch of c-di-GMP degradation. [PMID:20444101](https://pubmed.ncbi.nlm.nih.gov/20444101/) directly measures conversion to pGpG. Full-length recombinant expression was unsuccessful; the assayed recombinant construct lacks the first 385 residues and retains the catalytic EIL/EAL region (aa427–670). The apparent Km of 0.054 micromolar belongs to that fragment, not a measured native full-length protein. Native deletion and complementation used low-passage virulent B31-A3, a B31 derivative lacking cp9.

Both seeded GO:0071111 rows are ACCEPT on the same biochemical evidence. The curated EC/Rhea mapping agrees with the experimental product and does not need an invented more specific term. The gene product executes phosphodiester hydrolysis, while effects on motility and infection are downstream outputs. No new process terms or unsupported cellular compartment are added. [PMID:24822172](https://pubmed.ncbi.nlm.nih.gov/24822172/) compares this EAL branch with PdeB.

## Retrieval and provenance, 2026-11-05

The standard `just fetch-gene` scaffold and its raw UniProt/GOA files were pinned by the parent audit in `analysis/module_audits/bacterial_c_di_gmp_signaling/seed-baseline.yaml`. Original annotation fields are preserved; only review judgments and explicitly NEW rows are authored here. No source files were edited manually.

`just deep-research-falcon BORBU pdeA` was attempted on 2026-11-05 and failed with HTTP 403 (authentication/access failure). There is no provider-authored report; these are manual research notes. Logs are under `.cache/module-audit-logs/c-di-gmp-20261105/`. `just paint-losses BORBU pdeA` was also run. PANTHER lineage losses could not be assessed because the accession is absent from the locally available family tree (or, for PlzA, no PANTHER family is present); this is an unavailable check, not evidence that no loss exists. The seeded rows contain no IBA.

The module boundary is synthesis, degradation and receptor occupancy. Tick survival, mammalian infection, motility and nucleic-acid regulation are informative gene-level outputs, not assertions that every bacterial representative shares those outputs. No new biological-process annotations were manufactured from necessity or infection phenotypes.
