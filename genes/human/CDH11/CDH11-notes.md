# CDH11 curation notes

## 2026-10-10: original ClinGen review

Reviewed all 43 seeded annotations and preserved both machine-derived protein isoforms. The normal fetch initially stalled during reference retrieval; its partial output was retained and the same CLI completed sequentially with a transport timeout. Falcon and the explicit perplexity-lite fallback both genuinely timed out; these notes record manual primary-source research. No provider report was fabricated.

The [standing project instruction](https://github.com/ai4curation/ai-gene-review/blob/f7dc8b60bf8be80744f75955c3c1a3c16bd73888/projects/CLINGEN_MENDELIAN.md#curation-instructions) governs generic binding. This seed has no GO:0005515 rows.

### Functional synthesis and assay boundaries

CDH11 supplies the adhesive interaction itself. Existing cadherin binding is refined to cadherin binding involved in cell-cell adhesion, preserving IBA provenance. Calcium binding remains a correct, less informative supporting activity. Broad adhesion and membrane ancestors remain accepted; the core lists the informative processes and locations rather than every parent.

[PMID:33811546](https://pmc.ncbi.nlm.nih.gov/articles/PMC9245547/) Methods and Fig5 distinguish CDH11-transduced mouse L cells adhering to human CDH11-Fc from E279Q patient fibroblast migration/focal-adhesion phenotypes. Neither experiment establishes direct collagen binding or an intrinsic Rho-family regulatory activity. Its genuine normal full-text cache is available.

[PMID:16525026](https://pmc.ncbi.nlm.nih.gov/articles/PMC1446095/) Methods and Results/Figs1–3 establish full-length human CDH11 and tail mutants in mouse L cells. The canonical tail recruits catenins and organizes junctions. Its normal cache is abstract-only; authentic external full HTML was read, including exact construct and assay descriptions, but figure pixels and every supplement were not newly inspected. [PMID:10320525](https://pubmed.ncbi.nlm.nih.gov/10320525/) distinguishes intact, tail-truncated and proteolytically secreted products. The truncated isoform is not assigned canonical beta-catenin binding. The secreted fragment justifies the separate extracellular-region row. [PMID:9556063](https://pubmed.ncbi.nlm.nih.gov/9556063/) independently supports human osteoblast junctional CDH11/catenin association; its HAV-peptide perturbation is not treated as CDH11-specific.

### Tissue context and remaining uncertainty

Valve/migration [PMID:26188246](https://pmc.ncbi.nlm.nih.gov/articles/PMC4841269/) was read externally at Methods and selected Results depth, with a normal abstract-only cache. WITH F1RFU7 is pig, and the paper also uses mouse and chick experiments. [PMID:11450702](https://pubmed.ncbi.nlm.nih.gov/11450702/) adds mouse bone-density/mineralization evidence to the early suggestive skeletal annotations; those remain non-core rather than being promoted to a defining molecular function.

Exact QuickGO mouse donor records trace neural transfers to [PMID:10860580](https://pubmed.ncbi.nlm.nih.gov/10860580/). The normal abstract supports hippocampal synaptic localization and CA1 potentiation; this is retained as ortholog-inferred context. The donor cytoplasmic observation from [PMID:12139922](https://pubmed.ncbi.nlm.nih.gov/12139922/) remains unresolved. The full [PMID:29112946](https://pmc.ncbi.nlm.nih.gov/articles/PMC5675431/) studies pathological hypodermal fibrosis, so the electronic transfer to normal skin development is marked over-annotated after checking the GO definition. The [PMID:23533145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) exosome main text was read, but its exact CDH11 table entry was not recovered; table downloads returned a preparation page, and Europe PMC reported the supplement unavailable.

Reactome events were checked individually. The R-NUL event deliberately combines human CDH11 with mouse catenins; it is not a wrong-species attribution. Product-localization events do not imply that CDH11 performs translation or cleavage of itself. The accompanying evidence JSON retains exact machine donor/participant fields and source URLs/hashes. These records corroborate provenance, not independent experimental replication.

Supporting quotations are sparse and source-specific, with no repetition in these notes. The 25-word aggregate authoring limit is not represented as a repository validation rule.

### Independent specificity and coherence check

The final MF uses GO:0098641 because the adhesive ligand is itself a cadherin, a more specific fit than generic cell-cell adhesion mediator activity. Both unqualified cell-migration assertions are accepted as core, preserving the pig/valve scope of the ISS evidence. The skin-development decision concerns process scope, not rejection of the experimental fibrosis phenotype. No PAINT-node reassessment is claimed.
