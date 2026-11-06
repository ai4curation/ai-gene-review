# PdeB review notes

## Direct evidence and reaction granularity

B31 BB_0374 (O50161) is an HD-GYP phosphodiesterase. [PMID:21670168](https://pubmed.ncbi.nlm.nih.gov/21670168/) assays purified full-length protein (379 aa) and its HD-GYP fragment (aa90–305); both degrade c-di-GMP with GMP as the measured endpoint. MnCl2 enhances activity. Native phenotype experiments use B31-A3-K2Δbbe002, a B31 derivative with altered plasmid content and the bbe002 transformation barrier removed. The study supports increased flexing and reduced tick survival after deletion, but not a general defect after needle inoculation into mice.

The fetched seed has zero GOA rows. A NEW GO:0071111 row is justified by the enzyme chemistry, with IC rather than IDA: the GO definition is only the c-di-GMP-to-pGpG ring-opening step, whereas this source measured GMP. Ring opening is intrinsic to the demonstrated overall hydrolysis, but released pGpG or its accumulation was not separately observed. No pGpG kinetic constants or release mechanism are invented. The core function describes the complete measured reaction and the ontology's narrower step. This evidence is independent of the retracted RpfG work.

[PMID:24822172](https://pubmed.ncbi.nlm.nih.gov/24822172/) places PdeB with the distinct EAL enzyme PdeA. PdeB's GMP endpoint must not be copied onto PdeA, whose direct product is pGpG.

## Retrieval and provenance, 2026-11-05

The standard `just fetch-gene` scaffold and its raw UniProt/GOA files were pinned by the parent audit in `analysis/module_audits/bacterial_c_di_gmp_signaling/seed-baseline.yaml`. Original annotation fields are preserved; only review judgments and explicitly NEW rows are authored here. No source files were edited manually.

`just deep-research-falcon BORBU pdeB` was attempted on 2026-11-05 and failed with HTTP 403 (authentication/access failure). There is no provider-authored report; these are manual research notes. Logs are under `.cache/module-audit-logs/c-di-gmp-20261105/`. `just paint-losses BORBU pdeB` was also run. PANTHER lineage losses could not be assessed because the accession is absent from the locally available family tree (or, for PlzA, no PANTHER family is present); this is an unavailable check, not evidence that no loss exists. The seeded rows contain no IBA.

The module boundary is synthesis, degradation and receptor occupancy. Tick survival, mammalian infection, motility and nucleic-acid regulation are informative gene-level outputs, not assertions that every bacterial representative shares those outputs. No new biological-process annotations were manufactured from necessity or infection phenotypes.
