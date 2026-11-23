# sad-II evidence notes

## 2026-08-11

Q88I50 is an unreviewed submitter-name assignment to NAD-dependent
succinate-semialdehyde dehydrogenase, but its UniProt keyword points toward
NADP. Characterized Sad/YneI-family enzymes can use both cofactors with NAD
preference, so this review uses the substrate-specific, cofactor-neutral
GO:0009013 as core. [PMID:23229889]

An older biochemical study separated two succinate-semialdehyde dehydrogenases
from *P. putida*. The smaller enzyme was induced by 4-hydroxyphenylacetate and
preferred NAD while retaining 9% activity with NADP; the larger enzyme was
NADP-dependent and putrescine-induced. The abstract does not name a strain,
gene, or accession, so it supports organism-level enzyme diversity but does not
identify either activity as Q88I50. [PMID:3355840 "Two forms of succinic-semialdehyde dehydrogenase have been isolated in Pseudomonas putida."]

The completed OpenScientist report proposes that Q88I50 is a Sad/YneI-like,
NAD-preferring candidate and maps the published YneI cofactor determinant to
Q88I50 Lys159. Those residue and protein-to-activity assignments are
provider-generated alignments, not results reported in PMID:3355840 or
PMID:23229889, and remain hypotheses pending a reproducible sequence analysis
and direct assay. [file:PSEPK/sad-II/sad-II-deep-research-openscientist.md]

No direct assay of Q88I50 or pathway-specific KT2440 phenotype was located.


## 2026-10-26 — complete target and source audit

PP_3151/Q88I50 has the NAD-dependent SSADH FunFam 3.40.605.10:FF:000012 and GabD1-like CDD cd07100 classifications. Retain NAD-capable succinate-semialdehyde oxidation as a qualified family inference; the old ARBA NADP-keyword conflict is not a reason to reject NAD capacity. Generic catalytic ancestors are refined rather than marked peripheral. Matched substrate/cofactor kinetics remain an expert question, and no NADP exclusion is asserted.

PMID:32256468 calls PP_3151 "SadI", whereas this accession's current symbol is sad-II. The locus resolves this nomenclature difference: it is mentioned as an annotated SSA-oxidation candidate, not assayed individually. PMID:23229889 is Salmonella YneI; PMID:3355840 does not resolve its Pseudomonas enzyme preparations to this locus. Both remained abstract-only after actual full-text recovery attempts.

Full PMID:40410945 identifies PP_3151 in engineered multigene deletions and cites the vanillin-induced proteome study PMID:25026441. This establishes relevant context, not isolated Sad-II vanillin turnover: altered production in strains deleting many oxidoreductases cannot be assigned to this one enzyme. The original 2014 cache remains abstract-only. No new vanillin process annotation is proposed. PR4748's genuine source-boundary distinctions are retained; provider residue alignments are not promoted to reproduced analyses.

Workflow: all original annotation fields, order and flags and both raw source hashes were captured before changes. Existing genuine OpenScientist research was reused; no replacement report was fabricated. Normal publication caching and bacterial fitness retrieval were attempted; FEBA was unreachable and no fitness artifact was created. Manual primary/domain review supplies the decisions. No new annotation row was added.


## PR #5591 source and cofactor follow-up — 2026-10-26

Distinguished PP_3151 from Sad-I: its PANTHER SF1 is explicitly NAD(P)-named and is compatible with the NAD-dependent FunFam, rather than a competing NADP-only classification. Retained NAD capacity as family inference without target-specific kinetics, exclusion of NADP or mapped physiological pathway. Broad refinements and the core now use GO:0009013. PMID:3355840 and PMID:23229889 remain contextual, not exact-target assays. GO:0004030 to GO:0009013 is a semantic correction, not a claimed is_a refinement. All original annotation payloads, qualifiers, actions and raw UniProt/GOA bytes are preserved. No NEW annotation was added. Independent bounded consultation agreed that NAD capacity does not imply NADP exclusion. Focused validation, source checks, renders and preservation checks are recorded in the PR #5591 follow-up report.
