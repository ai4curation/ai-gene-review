# RIM15 curation notes

## 2026-09-02 Update: fixed incorrect proposed_replacement_terms id

While auditing the existing review, found that two `existing_annotations` entries
for `GO:0051321` (meiotic cell cycle, IEA and IMP evidence) proposed
`GO:0045959` as a replacement term, with two different (and both incorrect)
labels attached in different places ("positive regulation of mitotic gene
expression" in one entry, "positive regulation of meiotic gene expression" in
the other).

Verified via QuickGO
(https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045959) that
`GO:0045959` actually denotes "negative regulation of complement activation,
classical pathway" -- a term with no relationship to meiosis, gene expression,
or cell-cycle regulation. Neither proposed label matches the real term, and a
web search confirms there is no GO term literally named "positive regulation
of meiotic gene expression" or "... mitotic gene expression".

Replaced the erroneous id in both entries with `GO:0045944` (positive
regulation of transcription by RNA polymerase II, verified via QuickGO:
https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045944), which
matches the review's own stated rationale that RIM15 stimulates transcription
of early meiotic genes (e.g. IME2, a Pol II gene) via Ime1p/Ume6p
[PMID:9111339 "Ime1p activates early meiotic genes through its interaction
with Ume6p, and analysis of Rim15p-dependent regulatory sites at the IME2
promoter indicates that activation through Ume6p is defective"]. No exact
"meiotic gene expression" GO term exists, so the closest verifiably-correct
term was used instead, with a note in `reason` flagging the prior id as wrong
rather than silently swapping it.

No other issues found in this review during this audit pass -- the IBA,
IEA, and experimental annotation calls elsewhere in the file are
well-supported and consistent with the cited literature.
