# ASF1 curation notes

## 2026-09-02 Update: audit fix — erroneous proposed_replacement_terms entry

While auditing the existing review, found that the `GO:0005515 protein binding` IPI
annotation (original_reference_id: PMID:11404324, documenting the ASF1–Cac2/CAF-1
interaction) carried a bogus `proposed_replacement_terms` entry — id `GO:0030515` paired
with the label `"positive regulation of cation transport"` — alongside the correct
`GO:0042393 histone binding`.

The id and the label did not go together. `GO:0030515` is in fact **`snoRNA binding`**
("Binding to a small nucleolar RNA"), confirmed against the committed ontology cache
(`cache/ontologies/go.tsv` → `GO:0030515<TAB>snoRNA binding`) and against OLS. The string
"positive regulation of cation transport" is not a GO label at all; it does not occur
anywhere in the ontology cache. So the entry was a hallucinated id+label pair, not a
copy/paste of a real term from another review — precisely the failure mode CLAUDE.md warns
about, where a plausible-looking label conceals a wrong id. Note that
`src/ai_gene_review/tools/fix_labels.py` deliberately skips `proposed_replacement_terms`
(they "may contain hallucinated GO IDs"), so no automated label check would have caught
this.

The removal stands either way: snoRNA binding is as unrelated to ASF1's
histone-chaperone / chromatin-assembly biology as ion transport would have been. ASF1 has
no documented snoRNA-binding or ion-transport role in any of the cited literature, the
deep-research reports, or UniProt (P32447). Removed the erroneous term; kept the
`GO:0042393 histone binding` replacement suggestion, which is well supported by ASF1's
defining H3-H4 histone-binding activity documented throughout this review (e.g.
[PMID:15840725 "Structural basis for the interaction of Asf1 with histone H3 and its
functional implications."]).

Left open (flagged as non-blocking by review, needs curator judgment rather than a
mechanical edit): the retained `GO:0042393 histone binding` replacement does not match
that particular IPI's own evidence, which is an ASF1–Cac2/CAF-1 protein interaction, and
the sibling protein-binding IPIs carry no replacement terms at all; the `supporting_text`
on that annotation is also the paper title rather than substantive evidence.

No other changes made — the rest of the review (annotation actions, core_functions,
description) is well-supported by the cited evidence and deep-research reports.
