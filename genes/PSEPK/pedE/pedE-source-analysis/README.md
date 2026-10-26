# PedE/PedH source and preservation trace

The pre-edit reviews contained 11 PedE and 13 PedH rows, including five inherited proposals. The JSON records every original non-review payload and four raw-record hashes. Run `uv run python genes/PSEPK/pedE/pedE-source-analysis/verify_preservation.py` from the repository root.

PedE's curated filename and gene_symbol are normalized from legacy `pede` to current UniProt `pedE` (Q88JH5 / PP_2674); the independently retrieved identity JSON is retained here. Raw/provider names and content are unchanged. PedH is Q88JH0 / PP_2679. Historical history records remain append-only.

Primary source grounding: full PMID28655819, PMID30158283 and PMID34513815 distinguish recombinant PMS/DCPIP assays, native metal-dependent phenotypes and unresolved cytochrome identity. Full PMID23023748 distinguishes ethylene-glycol bioconversion from growth and strains. PMID18177365 is abstract-only strain-U context. Primary RCSB 6ZCW deposition verifies mature PedH/PQQ/praseodymium. Normal DOI10.1021/acscatal.0c01789 retrieval returned unavailable article text; no quotes from that article are asserted. Genuine pre-existing provider reports were reused as retrieval aids rather than quoted as primary evidence. Actual fitness retrieval failed; no fitness phenotype is inferred.

GO0052934 covers primary alcohol to aldehyde, whereas GO0016614 retains secondary alcohol chemistry; aldehyde oxidation is retained in broad-MF refinement using GO0016903. No new BP annotation is manufactured. PedH's inherited reporter-supported expression-feedback proposal remains outside the catalytic core, with mechanism unresolved.

The Git index confirmed the historical parent directory was lowercase `pede`. Two-step git mv, authorized specifically for the nine renamed paths, canonicalized the directory. `case_rename` records exact original/new paths and SHA-256 values; every raw/provider file is byte-identical. Curated YAML/HTML contents are intentionally reviewed. Historical history files remain under their original directory.

## PR 5588 exact-case and proposal follow-up

The preceding text describes the first audit state. The raw/provider filename repair now completes canonical `pedE-` stems; provider bytes remain unchanged and the legacy OpenScientist artifact-directory spelling is retained for its immutable relative links. Histories now live in the successor directory with old identities and explicit `superseded_by` metadata. The four author-created metabolic proposals now use IC with the measured-turnover primary source; the PedH expression proposal is withdrawn to UNDECIDED with `retired: true` denoting a prior proposal, not GOA history. `pr5588-proposal-supersession.json` records exact before/after payloads and source-path renames. Original snapshot contents remain immutable. The verification script checks all original machine payloads and only permits those enumerated proposal changes.
