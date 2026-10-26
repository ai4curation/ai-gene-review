# ASP3-1 notes

- Asparaginase II, one of four identical tandem copies (ASP3-1..4) near rDNA [UniProt "The 4 identical copies ASP3-1, ASP3-2, ASP3-3 and ASP3-4 are arranged in"].
- Signal peptide 1-25; secreted/periplasmic [UniProt "SUBCELLULAR LOCATION: Secreted. Periplasm."]; externally active, N-starvation induced [PMID:238936 "The appearance of the external asparaginase is stimulated by nitrogen starvation"].
- NCR-regulated at mRNA level [PMID:3042786 "nitrogen catabolite repression of asparaginase II is achieved by alteration in mRNA levels."].
- ASP3 cluster arose by horizontal transfer from Wickerhamomyces and is absent from many strains (League et al. 2012, FEMS Yeast Res, PMID:22776361; found by WebSearch, not cached, not cited in the review YAML).
- YeastCyc cytosol RCA wrong for this secreted enzyme -> REMOVE.


## 2026-10-26 comparative annotation audit

Reviewed all 17 existing rows and the core-function synthesis for yeast/ASP3-1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 10, 'MODIFY': 3, 'UNDECIDED': 2, 'REMOVE': 1, 'KEEP_AS_NON_CORE': 1}.

The four S288C loci encode identical 362-residue proteins: reading the four downloaded UniProt sequences gives identical SHA256 prefix `3749e855f2aee99f`. This supports shared protein chemistry but does not create four independent locus-specific biochemical assays. PMID:238936 distinguishes external nitrogen-induced activity from constitutive internal activity, and PMID:3042786 clones ASP3 and resolves differently processed N termini. Catalysis and mature cell-wall/periplasm localization remain supported; cytosol RCA imports are not appropriate for the mature secreted enzyme. General extracellular/periplasm/cell-periphery terms refine to the specific fungal periplasm, and amino-acid metabolism refines to asparagine catabolism.

Added full PMID:36040324. Its larger survey detects ASP3 in 117 of 1,680 S. cerevisiae genome assemblies, with strain-variable copy number; conserved synteny favors ancestral retention/loss over the earlier recent-HGT proposal in PMID:22776361. The latter reference is explicitly DISPUTED for that historical claim, while its S288C copy description remains useful. Broader ancestral reconstruction remains provisional. Heterologous S. uvarum::ASP3 improves sole-asparagine growth but not apple-juice growth, so neither ecological benefit nor flux is universal. No locus-specific phenotype or four independent catalytic routes is inferred.

The two HDA nuclear-envelope/ER rows from PMID:11914276 are UNDECIDED. A normal force fetch remained abstract-only; publisher returned403 and PMC was inaccessible. The target-specific images/construct could not be checked. Neither nuclear-envelope residence nor an ER-transit/tag artifact is established by the generic abstract. This corrects the earlier confident interpretation, while preserving the original HDA payloads.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ASP3-1-research.log` and `aspartate-yeast-ASP3-1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ASP3-1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
