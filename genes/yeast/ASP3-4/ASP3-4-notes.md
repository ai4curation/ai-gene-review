# ASP3-4 notes

## Identity
- ASP3-4 is one of four identical copies (ASP3-1..ASP3-4) encoding asparaginase II, EC 3.5.1.1 [file:yeast/ASP3-4/ASP3-4-uniprot.txt "The 4 identical copies ASP3-1, ASP3-2, ASP3-3 and ASP3-4 are arranged in"]. Sequence identical to the other copy reviewed in this batch (ASP3-3/ASP3-4 SQ blocks identical).
- Reaction: [file:yeast/ASP3-4/ASP3-4-uniprot.txt "Reaction=L-asparagine + H2O = L-aspartate + NH4(+);"]
- Signal peptide 1-25, secreted / periplasm [file:yeast/ASP3-4/ASP3-4-uniprot.txt "SUBCELLULAR LOCATION: Secreted. Periplasm."]

## Evidence
- External, nitrogen-starvation-induced asparaginase distinct from an internal constitutive one [PMID:238936 "these strains of S. cerevisiae have an externally active asparaginase as well as an internally active one"; "The appearance of the external asparaginase is stimulated by nitrogen starvation, requires an available energy source, and is prevented by cycloheximide."]
- ASP3 is the structural gene; NCR acts at mRNA level [PMID:3042786 "nitrogen catabolite repression of asparaginase II is achieved by alteration in mRNA levels"]

## Curation decisions
- Core: asparaginase activity / L-asparagine catabolic process / cell wall-bounded periplasmic space.
- REMOVE RCA cytosol (YeastPathways pathway default; fits ASP1, not secreted ASP3).
- amino acid metabolic process IEA: over-annotation (parent of the specific process).
- cellular response to nitrogen starvation IDA: kept as non-core (regulated expression / N scavenging).

## Module notes
- ASP1 (cytoplasmic asparaginase I) vs ASP3 (periplasmic asparaginase II): both catalyse the same YeastPathways reaction in different compartments; ASP3 acts on external asparagine. ASP3 cluster is copy-number variable (4 copies in S288C).


## 2026-10-26 comparative annotation audit

Reviewed all 16 existing rows and the core-function synthesis for yeast/ASP3-4; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 10, 'MODIFY': 4, 'REMOVE': 1, 'KEEP_AS_NON_CORE': 1}.

The four S288C loci encode identical 362-residue proteins: reading the four downloaded UniProt sequences gives identical SHA256 prefix `3749e855f2aee99f`. This supports shared protein chemistry but does not create four independent locus-specific biochemical assays. PMID:238936 distinguishes external nitrogen-induced activity from constitutive internal activity, and PMID:3042786 clones ASP3 and resolves differently processed N termini. Catalysis and mature cell-wall/periplasm localization remain supported; cytosol RCA imports are not appropriate for the mature secreted enzyme. General extracellular/periplasm/cell-periphery terms refine to the specific fungal periplasm, and amino-acid metabolism refines to asparagine catabolism.

Added full text of PMID:36040324. Its larger survey detects ASP3 in 117 of 1,680 S. cerevisiae genome assemblies, with strain-variable copy number; conserved synteny favors ancestral retention/loss over the earlier recent-HGT proposal in PMID:22776361. The latter reference is explicitly DISPUTED for that historical claim, while its S288C copy description remains useful. Broader ancestral reconstruction remains provisional. Heterologous S. uvarum::ASP3 improves sole-asparagine growth but not apple-juice growth, so neither ecological benefit nor flux is universal. No locus-specific phenotype or four independent catalytic routes is inferred.

The cell-periphery HDA claim is retained in refined form as fungal periplasm, using the independent secreted-enzyme evidence. No detection screen is treated as an independent catalytic assay.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP 403 authentication failure; Perplexity returned HTTP 401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ASP3-4-research.log` and `aspartate-yeast-ASP3-4-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ASP3-4-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting.
