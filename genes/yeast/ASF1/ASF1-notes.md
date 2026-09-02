# ASF1 curation notes

## 2026-09-02 Update: audit fix — erroneous proposed_replacement_terms entry

While auditing the existing review, found that the `GO:0005515 protein binding` IPI
annotation (original_reference_id: PMID:11404324, documenting the ASF1–Cac2/CAF-1
interaction) listed `GO:0030515 "positive regulation of cation transport"` as a
`proposed_replacement_terms` entry alongside the correct `GO:0042393 histone binding`.

`GO:0030515` ("positive regulation of cation transport") is a transmembrane-transport
regulation term with no documented connection to ASF1's histone-chaperone /
chromatin-assembly biology in any of the cited literature, the deep-research reports, or
UniProt (P32447) — ASF1 has no known role in ion transport. This appears to be a
copy/paste or generation artifact unrelated to the annotation it was attached to. Removed
the erroneous term; kept the correct `GO:0042393 histone binding` replacement suggestion,
which is well supported by ASF1's defining H3-H4 histone-binding activity documented
throughout this review (e.g. [PMID:15840725 "Structural basis for the interaction of
Asf1 with histone H3 and its functional implications."]).

No other changes made — the rest of the review (annotation actions, core_functions,
description) is well-supported by the cited evidence and deep-research reports.
