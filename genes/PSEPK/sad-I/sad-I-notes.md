# sad-I evidence notes

## 2026-08-11

Q88K05 is an unreviewed submitter-name assignment to NAD-dependent
succinate-semialdehyde dehydrogenase, while its PANTHER subfamily label and
UniProt keyword point toward NADP. Characterized Sad/YneI-family enzymes can use
both cofactors with NAD preference, so this review uses the substrate-specific,
cofactor-neutral GO:0009013 as core. [PMID:23229889]

An older biochemical study separated two succinate-semialdehyde dehydrogenases
from *P. putida*. The smaller enzyme was induced by 4-hydroxyphenylacetate and
preferred NAD while retaining 9% activity with NADP; the larger enzyme was
NADP-dependent and putrescine-induced. The abstract does not name a strain,
gene, or accession, so it supports organism-level enzyme diversity but does not
identify either activity as Q88K05. [PMID:3355840 "Two forms of succinic-semialdehyde dehydrogenase have been isolated in Pseudomonas putida."]

The completed OpenScientist report proposes that Q88K05 is the Sad/YneI-like,
NAD-preferring candidate and maps the published YneI cofactor determinant to
Q88K05 Lys157. Those residue and protein-to-activity assignments are
provider-generated alignments, not results reported in PMID:3355840 or
PMID:23229889, and remain hypotheses pending a reproducible sequence analysis
and direct assay. [file:PSEPK/sad-I/sad-I-deep-research-openscientist.md]

No direct assay of Q88K05 or pathway-specific KT2440 phenotype was located.


## 2026-10-26 — complete target and source audit

PP_2488/Q88K05 has the NAD-dependent SSADH FunFam 3.40.605.10:FF:000012 and GabD1-like CDD cd07100 classifications. Retain NAD-capable succinate-semialdehyde oxidation as a qualified family inference, not an exact-target assay. The previous NADP-keyword argument is superseded: an ARBA keyword or a subfamily label does not experimentally exclude NAD, and the NAD GO reaction does not assert that NADP is unusable. General catalytic terms now MODIFY to the supported SSADH activity instead of being called non-core.

PMID:23229889 identifies Salmonella YneI and states "YneI can use both NAD(+) and NADP(+) as cofactors". PMID:3355840 resolves P. putida isoenzymes, but the accessible abstract gives no gene or strain assignment connecting either enzyme to PP_2488. Both papers remained abstract-only after actual normal forced retrieval. Their measured kinetics are not copied onto this target. The genuine OpenScientist report's residue mapping remains an unreproduced research lead; classification support comes from the independent database family records. There is no established cognate Gbd partner or dominant GABA/4HB/putrescine route.

Workflow: all original annotation fields, order and flags and both raw source hashes were captured before changes. Existing genuine OpenScientist research was reused; no replacement report was fabricated. Normal publication caching and bacterial fitness retrieval were attempted; FEBA was unreachable and no fitness artifact was created. Manual primary/domain review supplies the decisions. No new annotation row was added.


## PR #5591 source and cofactor follow-up — 2026-10-26

Reassessed the exact Q88K05 NAD-dependent FunFam and NADP-named PANTHER SF2 at the same computational evidence level. The existing NAD-capacity row is retained explicitly as contested family inference, not measured target kinetics or NADP exclusion. Broad refinements and the core now use cofactor-general GO:0009013. PMID:3355840 separates P. putida isoenzymes but does not map them to PP_2488; PMID:23229889 assays Salmonella YneI. Neither settles this locus. QuickGO confirms GO:0009013 is below the broad oxidoreductase terms but not GO:0004030; the latter change is a substrate-specific semantic correction, not a claimed descendant refinement. All original annotation payloads, qualifiers, actions and raw UniProt/GOA bytes are preserved. No NEW annotation was added. Independent bounded consultation agreed that NAD capacity does not imply NADP exclusion. Focused validation, source checks, renders and preservation checks are recorded in the PR #5591 follow-up report.
