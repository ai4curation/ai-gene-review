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

Scope of this audit pass: it was a targeted `proposed_replacement_terms` id
audit. The other three proposed ids in the file (`GO:1903452` x3) were checked
and resolve with correct labels. The IBA, IEA and experimental annotation
*actions* elsewhere in the file were not systematically re-adjudicated in this
pass, so no claim is made about them.

## 2026-09-04 Update: dropped the replacement entirely -- the meiotic context stays

Follow-up to review feedback on PR #2941, which flagged that swapping the
meiosis-specific GOA term `GO:0051321` for `GO:0045944` (positive regulation of
transcription by RNA polymerase II) trades a specific term for a strictly less
informative one, and that the `MODIFY` on the SGD IMP was weakly justified.

Looked up whether GO has a meiosis-scoped regulation-of-transcription term, as
the review asked. It does not, and the reason is decisive: GO has **obsoleted**
that entire region of the ontology.

```
GO:0051039  obsolete positive regulation of transcription involved in meiotic cell cycle
GO:0010673  obsolete positive regulation of transcription from RNA polymerase II
            promoter involved in meiotic cell cycle
GO:0051037, GO:0051038, GO:0010672, GO:0010674, GO:0100023, GO:0100051  (also obsolete)
```

Both of the positive-regulation terms carry the same obsoletion comment --
"This term was obsoleted because it represents a GO-CAM model" -- and, crucially,
both carry these replacement pointers:

```
consider: GO:0045944
consider: GO:0051321
```

That is GO explicitly instructing curators to use the two terms **together**
rather than merged into one. So the additive shape the reviewer suggested is not
just a preference here, it is the ontology's own documented guidance, and adding
a `proposed_new_terms` entry for a meiosis-scoped transcription term would mean
proposing the re-creation of a deliberately obsoleted class.

Actions taken:

- Both `GO:0051321` entries (IEA `GO_REF:0000043` and IMP `PMID:9111339`)
  changed from `MODIFY` to `KEEP_AS_NON_CORE`, and `proposed_replacement_terms`
  removed from both. Non-core rather than `ACCEPT` because RIM15's core function
  is nutrient-responsive Ser/Thr kinase activity, with meiotic entry one
  downstream output alongside quiescence entry, stress-response induction and
  autophagy.
- The transcriptional mechanism is already captured additively by the separate
  `GO:0045944` IMP annotation on the same reference, which the review accepts --
  no new term is needed to express it.
- The IMP's `supporting_text` was changed from the paper title to the abstract
  sentence that actually evidences the term
  [PMID:9111339 "The Saccharomyces cerevisiae RIM15 gene was identified
  previously through a mutation that caused reduced ability to undergo meiosis."].
  `full_text_available: false` for this paper, so per CLAUDE.md the SGD curator's
  experimental call is not second-guessed.
- The duplicated `GO:0045959` errata prose was dropped from both `reason` fields.
  The correction is recorded above and in git history; with the replacement gone
  the erroneous id no longer appears anywhere in the file.
