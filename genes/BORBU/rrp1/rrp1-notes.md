# Rrp1 review notes

## Function and localisation

The chromosomal B31 gene BB_0419 encodes a receiver/GGDEF cyclase, UniProt O51380. The decisive biochemical source is [PMID:15716451](https://pubmed.ncbi.nlm.nih.gov/15716451/), which directly identifies phosphorylation-dependent Rrp1 diguanylate cyclase activity. The original cache is abstract-only; activity and phosphorylation dependence are explicitly stated, but assay details are not inferred from that abstract. [PMID:19210621](https://pubmed.ncbi.nlm.nih.gov/19210621/) provides full-text B31-derived functional work and fractionation. The protoplasmic-cylinder fraction includes both inner membrane and cytoplasmic proteins. Together with absent predicted transmembrane spans/export signals, the authors conclude Rrp1 is most likely cytoplasmic. The membrane TreeGrafter row is therefore MODIFY to cytoplasm, not an assertion of a directly imaged cytosolic pool.

## Output specificity

[PMID:21542866](https://pubmed.ncbi.nlm.nih.gov/21542866/) uses infectious B31 clone 5A4. Deletion increases run speed while decreasing flexing, swarm spread and N-acetylglucosamine chemotaxis. The negative-motility row is retained as non-core only in the measured run-speed sense; it must not be paraphrased as a universal motile-to-sessile switch. The adhesive step GO:0043709 is over-propagated from other GGDEF proteins: its definition concerns attachment through adhesion molecules, which Rrp1 has not been shown to execute. This does not establish that Borrelia cannot aggregate.

GO:0000160 describes the phosphorelay pathway, not kinase catalytic activity, and is appropriate for a phosphorylated response-regulator component. No direct DNA-binding function is assigned to this enzyme. [PMID:24822172](https://pubmed.ncbi.nlm.nih.gov/24822172/) supplies comparative circuit context.

## Retrieval and provenance, 2026-11-05

The standard `just fetch-gene` scaffold and its raw UniProt/GOA files were pinned by the parent audit in `analysis/module_audits/bacterial_c_di_gmp_signaling/seed-baseline.yaml`. Original annotation fields are preserved; only review judgments and explicitly NEW rows are authored here. No source files were edited manually.

`just deep-research-falcon BORBU rrp1` was attempted on 2026-11-05 and failed with HTTP 403 (authentication/access failure). There is no provider-authored report; these are manual research notes. Logs are under `.cache/module-audit-logs/c-di-gmp-20261105/`. `just paint-losses BORBU rrp1` was also run. PANTHER lineage losses could not be assessed because the accession is absent from the locally available family tree (or, for PlzA, no PANTHER family is present); this is an unavailable check, not evidence that no loss exists. The seeded rows contain no IBA.

The module boundary is synthesis, degradation and receptor occupancy. Tick survival, mammalian infection, motility and nucleic-acid regulation are informative gene-level outputs, not assertions that every bacterial representative shares those outputs. No new biological-process annotations were manufactured from necessity or infection phenotypes.
