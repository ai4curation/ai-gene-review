# ATP11 curation notes

## 2026-09-02 Update: audit fix — non-verbatim finding supporting_text

While auditing the existing review, `just validate` / `ai-gene-review validate --terms`
flagged an ERROR: the `references[].findings` entry for `PMID:36596815` ("The mitochondrial
Hsp70 controls the assembly of the F(1)F(O)-ATP synthase.") carried a paraphrased
`supporting_text` ("Mitochondrial Hsp70 cooperates with the assembly factors Atp11 and
Atp12 to form the F1 domain.") that is not a verbatim substring of the cached publication.

The cached abstract's actual text is: "...it cooperates with the assembly \nfactors Atp11
and Atp12 to form the F1 domain of the ATP synthase." [PMID:36596815 "it cooperates with
the assembly...factors Atp11 and Atp12 to form the F1 domain of the ATP synthase."] — this
exact quote (bridging the abstract's line-wrap with `...`) was already used correctly
elsewhere in this same review's `existing_annotations` entries for `GO:0033615`. Replaced
the paraphrase with this verbatim quote so the `references[].findings` entry now matches
the same evidence already cited correctly in the annotation review.

No other changes: the rest of the review (annotation actions, core_functions, description)
is well-supported by the cited evidence. Four pre-existing WARNINGs remain for
abstract-only-cached PMIDs (1532796, 2142305, 10681564, 12829692) where the finding quotes
are not present in the cached abstract text — these are expected per project convention
(`full_text_available: false` for all four) and were left as-is; they do not block
validation (`✓ Valid (with 4 warnings)`).
