---
title: "PSEPK urease biogenesis and urea hydrolysis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ureA, ureB, ureC, ureD, ureE, ureF, ureG]
autolink_gene_symbols: false
---

# PSEPK urease biogenesis and urea hydrolysis

This batch recovers the complete reviewed `ureDABCEFG` locus at PP_2842-PP_2849
from misleading first-pass buckets. KEGG places `ureABC` on the broad
`ppu00220` arginine map, while the original partition sent `ureD`, `ureE`,
`ureF`, and `ureG` to a generic folding/turnover bucket. The curated boundary
is instead the reusable [three-subunit bacterial urease biogenesis and urea
hydrolysis module](../../../modules/urease_biogenesis_urea_hydrolysis.html).

## Workflow Status

- [x] Fetch current UniProt and GOA records for exact UreA/B/C/D/E/F/G members.
- [x] Inspect urease-specific historical artifacts from `86cf4fd8e9` without cherry-picking them.
- [x] Curate every fetched GOA row and synthesize core functions.
- [x] Build a reusable module with three substantive stages.
- [x] Launch generic module OpenScientist research with a 7200-second timeout.
- [x] Launch module + urease locus + PSEPK OpenScientist research with a 7200-second timeout.
- [x] Launch gene-level OpenScientist research for all seven selected genes.
- [ ] Reconcile completed OpenScientist reports without stopping slow jobs.
- [x] Complete annotation-reviewer and independent AIGR PR review passes.
- [ ] Validate, render, test, publish a draft PR, and verify CI/re-review triggers.

## Module Boundary

| Order | Submodule | Required PSEPK realization | Boundary decision |
|---|---|---|---|
| 1 | Apo-urease structural complex assembly | UreA Q88J06, UreB Q88J05, UreC Q88J04 | UreA/B/C are role-bearing subunits of UreABC; all contribute to complex-level urease activity, and UreC alone supplies the dinickel catalytic center. |
| 2 | Nickel delivery and GTP-dependent activation | UreD Q88J07, UreE Q88J03, UreF Q88J01, UreG Q88J00 | UreD/F scaffold and gate activation, UreE binds nickel and is inferred to deliver it, and UreG supplies GTPase activity. These are transient maturation factors, not mature urease subunits. |
| 3 | Urea hydrolysis | mature UreABC complex | GO:0009039 belongs to the mature complex; urea hydrolysis is the terminal reaction. |

**Satisfiability result: `covered by conserved-family evidence; direct KT2440
biochemical confirmation remains open`.** All seven canonical structural and
activation roles occur in one compact locus and have reviewed UniProt records.
No direct paper in the current cache assays PP_2842-PP_2849 as a KT2440 system,
so the module does not present orthologous Klebsiella evidence as a target-gene experiment.

## Selected Gene Decisions

| Gene | Locus / UniProt | Core role | Main curation decision |
|---|---|---|---|
| `ureA` | PP_2843 / Q88J06 | gamma structural chain | `GO:0009039` is represented as contributed complex activity; unsupported nickel binding is removed. |
| `ureB` | PP_2844 / Q88J05 | beta structural chain | Urease-complex membership and urea catabolism retained; independent enabling of activity is over-annotated. |
| `ureC` | PP_2845 / Q88J04 | alpha catalytic chain | Urease activity and nickel binding retained as enabled MFs; broad hydrolase parents are true but non-core. |
| `ureD` | PP_2842 / Q88J07 | apo-urease scaffold | Scaffold role retained; orthologous metal binding is retained as non-core rather than equated with selective nickel delivery. |
| `ureE` | PP_2846 / Q88J03 | nickel metallochaperone | Nickel binding retained; generic folding and assembly mappings are rejected or de-emphasized. |
| `ureF` | PP_2848 / Q88J01 | UreG recruitment/checkpoint | UreG gating retained; unsupported direct nickel binding is removed. |
| `ureG` | PP_2849 / Q88J00 | GTPase metallochaperone | GTPase and nickel binding retained; separate GTP binding is not added redundantly. |

## Explicit Exclusions

- `ureJ`/PP_2847 is locus-associated but is not one of the requested canonical
  UreA-G structural/activation roles. Its membrane-accessory function needs a
  separate review before inclusion in any transport module.
- PP_4302 and UrtABCDE are urea transport systems. Urea uptake is upstream
  context, not a part of urease assembly, metallocenter activation, or catalysis.
- Nickel uptake and homeostasis supply an input to maturation but are not
  urease-specific core parts.
- Glutamine synthetase, glutamate synthase, and other ammonia-assimilation
  reactions act downstream of the released ammonia and remain separate modules.

## Evidence

- PMID:8718850 establishes the preorganized alpha-beta-gamma apoenzyme and
  places the binickel active center in the alpha/UreC chain.
- PMID:7909161 establishes UreD-bound apo-urease and the requirement for all
  four accessory genes in metallocenter assembly.
- PMID:10500143 localizes the GTP-hydrolysis requirement to UreG in the
  UreDFG-apourease activation complex.
- PMID:8318889 establishes nickel binding and proposes donor behavior for UreE.

Current GO lacks a specific biological-process term for urease activation or
metallocenter assembly. The UreE review therefore proposes `urease metallocenter
assembly` for the direct UreD/E/F/G stage; `GO:0043419 urea catabolic process`
remains the closest existing pathway-level term but is mechanistically indirect.
- PMID:22369361 establishes the UreF-UreG interaction surface and UreF's role
  in activation fidelity, documents orthologous UreD and UreG metal binding,
  and assigns primary nickel delivery to UreE rather than UreF.

The source table, including explicit out-of-boundary rows, is retained at
[`urease_biogenesis_urea_hydrolysis.tsv`](urease_biogenesis_urea_hydrolysis.tsv).

Generated UTC: 2026-08-11
