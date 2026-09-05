# ATP11 curation notes

## 2026-09-02 Update: audit fix — non-verbatim finding supporting_text

While auditing the existing review, `just validate` / `ai-gene-review validate --terms`
flagged an ERROR: the `references[].findings` entry for `PMID:36596815` ("The mitochondrial
Hsp70 controls the assembly of the F(1)F(O)-ATP synthase.") carried a paraphrased
`supporting_text` ("Mitochondrial Hsp70 cooperates with the assembly factors Atp11 and
Atp12 to form the F1 domain.") that is not a verbatim substring of the cached publication.

The cached record's actual text is: "...it cooperates with the assembly \nfactors Atp11
and Atp12 to form the F1 domain of the ATP synthase." [PMID:36596815 "it cooperates with
the assembly...factors Atp11 and Atp12 to form the F1 domain of the ATP synthase."] — this
exact quote (bridging the line-wrap with `...`) was already used correctly
elsewhere in this same review's `existing_annotations` entries for `GO:0033615`. Replaced
the paraphrase with this verbatim quote so the `references[].findings` entry now matches
the same evidence already cited correctly in the annotation review.

Note on severity: `PMID_36596815.md` has `full_text_available: true`, and the validator
escalates a non-verbatim finding quote to ERROR only when the cached record is not
abstract-only. That is why this one reference errored while others merely warned — the
severity difference reflects cache completeness, not whether the quote was defensible.

## 2026-09-03 Update: fixed the four remaining non-verbatim finding quotes

Follow-up to PR review feedback. The four remaining WARNINGs (PMIDs 1532796, 2142305,
10681564, 12829692) were the *same* defect as the one fixed above — paraphrases in
`references[].findings[].supporting_text` — downgraded to WARNING only because those four
records are `full_text_available: false`. The earlier note claiming the source text was
"not present in the cached abstract text" and that this was "expected per project
convention" was wrong on both counts: I re-read all four cached abstracts and the verbatim
text is present in every one, and in each case the correct verbatim quote was *already in
use* elsewhere in this same review file. There is no convention permitting paraphrase here.

Replaced each with the verbatim string already validated in-file:

- PMID:1532796 [PMID:1532796 "vitro import assays of ATP11 precursor and immunochemical
  evidence indicate that...the protein is located in mitochondria."]
- PMID:2142305 [PMID:2142305 "explanation for the mutant phenotype is a block in the
  assembly of the F1...oligomer."]
- PMID:10681564 [PMID:10681564 "evidence that Atp11p binds selectively to the beta-subunit
  of F(1)."] (the paraphrase differed only by `F1` vs the abstract's `F(1)`)
- PMID:12829692 [PMID:12829692 "Atp11p yields a subfragment of the protein (called
  Atp11pTRNC) that retains...molecular chaperone function...the natural substrate (F1
  beta)."]

No other changes: the rest of the review (annotation actions, core_functions, description)
is well-supported by the cited evidence and was left untouched. The review now validates
with zero warnings.
