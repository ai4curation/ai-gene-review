---
title: "PSEPK ppu00270 bacterial methionine cycle batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [metK, ahcY, metH, metE]
autolink_gene_symbols: false
---

# PSEPK ppu00270: bacterial methionine cycle

- Module seed: `bacterial_methionine_cycle`
- KEGG candidate genes from membership table: 46
- Selected cycle/remethylation genes: 4
- Curated review files in this batch: 4
- Adjacent module retained unchanged: `methionine_biosynthesis`
- Existing eukaryotic modules retained unchanged: `methionine_cycle`, `sam_cycle`, `homocysteine_metabolism`

## Required Workflow

- [x] Curate a dedicated species-neutral bacterial module.
- [ ] Complete module-level OpenScientist deep research.
- [ ] Complete module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch missing selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Complete OpenScientist deep research for newly fetched genes.
- [x] Audit every selected gene review semantically.
- [x] Curate the newly fetched gene reviews.
- [x] Validate and render module, project page, and gene reviews.
- [ ] Open one draft PR for this module/pathway.

## Selected Genes

| Done | Gene | Locus | UniProt | Primary bucket | Review | OpenScientist | Module interpretation |
|---|---|---|---|---|---|---|---|
| [x] | `metK` | PP_4967 | Q88D60 | kegg:ppu00999 | CURATED | RUNNING | covered: SAM synthesis |
| [x] | `ahcY` | PP_4976 | A0A140FWS3 | kegg:ppu00670 | CURATED | RUNNING | covered: direct one-step SAH hydrolysis |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | CURATED | PRESENT | covered: cobalamin-dependent remethylation |
| [x] | `metE` | PP_2698 | Q88JF1 | kegg:ppu00450 | CURATED | PRESENT | candidate: compact cobalamin-independent remethylation enzyme |

## Boundary Decisions

The reusable module begins with methionine adenosylation by MetK, represents the
distributed SAM-dependent transmethylation load, processes SAH to homocysteine,
and closes the cycle through folate-dependent methionine synthase activity. De
novo production of methionine from homoserine remains in the existing
`methionine_biosynthesis` module and is not duplicated here.

The module models both verified bacterial SAH-processing strategies: direct AhcY
hydrolysis and the two-step MtnN/Pfs plus LuxS route. KT2440 is supported by the
AhcY route. PP_3254 (Q88HU9) is a predicted MtnN-family SAH/MTA nucleosidase, but
no KT2440 LuxS protein was found in the local proteome metadata or an
organism-restricted UniProt query. PP_3254 therefore does not establish a
complete alternative SAH-to-homocysteine route and is not included in the focused
gene-review set.

Cysteine biosynthesis, sulfur assimilation, transsulfuration, methionine
degradation, methionine-sulfoxide repair, and methylthioadenosine salvage are
outside this cycle. KEGG ppu00270 membership alone is not evidence that those
genes belong in this module.

Generated UTC: 2026-08-11T00:00:00Z

## Research Job Status At Draft Publication

The module-level OpenScientist run was allowed to consume its full
`--timeout 7200` window and exited with timeout code 124 without producing a
report. The module + ppu00270 + PSEPK run and the new `metK` and `ahcY`
gene-level runs were still active when the draft PR was prepared. No partial or
hand-authored file was saved under an OpenScientist provider filename.
