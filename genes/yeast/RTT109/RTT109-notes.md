# RTT109 curation notes

## 2026-09-02 Update: added missing R-loop-suppression citation and proposed new term

While auditing the existing review, found that both the top-level `description`
and the `core_functions` entry for `GO:0010484` (histone H3 acetyltransferase
activity) already asserted that RTT109 "prevents DNA-RNA hybrid accumulation" /
contributes to "R-loop suppression" through H3K14/H3K23 acetylation, but no
reference anywhere in the file actually cited or quoted the paper establishing
this. The gene's own working file `RTT109-CURATION-REVIEW.md` (an untracked
scratch document in this folder) explicitly flagged this: "R-loop/DNA-RNA
hybrid prevention not explicitly annotated but supported (NEW annotation
should be added)" -- but that follow-up was never done in the actual
`RTT109-ai-review.yaml`.

Identified and fetched the source paper: PMID:35866610, Cañas et al. 2022,
Genetics, "A role for the Saccharomyces cerevisiae Rtt109 histone
acetyltransferase in R-loop homeostasis and associated genome instability"
[PMID:35866610 "Rtt109 prevents DNA-RNA hybridization by the acetylation of
histone H3 lysines 14 and 23"]. Full text now cached at
`publications/PMID_35866610.md` via `ai-gene-review fetch-pmid`.

Checked whether an existing GO term could be used for a direct `NEW`
`existing_annotations` entry (as done for e.g. ROF1's filamentous-growth
annotation). Searched QuickGO for "R-loop" and "DNA-RNA hybrid": the only
R-loop *process* term is `GO:0062176` (R-loop processing), whose definition is
explicitly R-loop *disassembly* -- the opposite direction from what RTT109
does (RTT109 loss increases R-loop levels; RTT109 activity prevents their
formation). No term for "negative regulation of R-loop formation" exists in
GO. Per project convention (never force a mismatched id onto a real finding),
recorded this as a `proposed_new_terms` entry instead, with `PMID:35866610` as
support and `GO:0006325` (chromatin organization, already used elsewhere in
this review) as a defensible `proposed_parent`.

Also added `PMID:35866610` to `references:` with a `reference_review` (HIGH
relevance, VERIFIED -- PubMed/PMC-verified, full text cached) and attached
`supported_by` provenance to the `GO:0010484` core-function block that was
making the previously-uncited claim.

No other issues found in this review during this audit pass. The bulk of the
70 `existing_annotations` entries (H3K56/K9/K27/K14/K23 acetyltransferase
activity, chromatin assembly, DNA damage response, etc.) are well-supported
by the cited literature and internally consistent.
