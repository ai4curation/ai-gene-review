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

## 2026-09-07 Update: review follow-up (non-verbatim `supported_by` quote, GO:0051082 action, `file:` provenance)

Addressing the second round of PR review feedback.

**1. Non-verbatim `supported_by` quote (blocking).** The earlier sweep covered
`references[].findings[]` but missed `existing_annotations[].review.supported_by`. The quote
backing the `REMOVE` of GO:0005515 read "we generated a high-quality proteome-wide
inter-interactome network map", which occurs nowhere in `publications/PMID_27107014.md`
(`full_text_available: true`; `grep -c` for both "proteome-wide" and "high-quality" returns 0).
Replaced with the verbatim text [PMID:27107014 "systematically probed the yeast and human
proteomes for interactions between...proteins from these two species"]. The substance of the
REMOVE is unchanged and still sound: all five GOA rows are IPI/PMID:27107014 differing only in
`WITH/FROM`, and every partner is a human accession.

**2. GO:0051082 now `KEEP_AS_NON_CORE`, not `MODIFY`.** Both experimental unfolded-protein-binding
annotations were being replaced by GO:0140777. That discards a well-grounded IDA and diverges
from this repo's recorded gene-specific determination in `projects/UNFOLDED_PROTEIN_BINDING.md`
(ATP11 listed as NON_CORE for UPB). The deciding evidence is that Atp11's chaperone activity is
demonstrated on a *non-client* substrate: [PMID:12829692 "molecular chaperone function as
determined in vitro with both a surrogate substrate (reduced insulin) and the natural substrate
(F1 beta)"]. Suppressing aggregation of reduced insulin is the canonical unfolded-protein-binding
assay and is not client-specific complex stabilization, so GO:0140777 does not subsume it. Both
GO:0051082 entries were set to `KEEP_AS_NON_CORE` (setting only one triggers a validator warning
about inconsistent actions for the same term). GO:0140777 remains the `core_functions` MF.

**3. `file:` reference quotes made verbatim.** Five `supporting_text` values on `file:` references
were paraphrases. These are never flagged (the `file:` prefix is in `skip_prefixes`), but the
schema asks for exact substrings, so they were replaced with real substrings of their sources —
`ATP11-deep-research-falcon.md` (three) and `PTHR13126-metadata.yaml` (two, now quoting
`accession: PTHR13126...name: CHAPERONE ATP11` rather than a sentence the file does not contain).

**4. Curation commentary removed from `description`.** The closing sentence compared annotation
informativeness, which CLAUDE.md reserves for `review.reason`/notes. Replaced with the biological
fact that motivates the GO:0051082 decision (in vitro holdase activity on reduced insulin).

`just validate yeast ATP11` → ✓ Valid, zero warnings.

Not addressed here (out of scope for this PR, flagged by the reviewer): `UNFOLDED_PROTEIN_BINDING.md:538`
describes ATP11 as the "Atp12p assembly factor", but Atp11 handles F1 beta/Atp2 and Atp12 handles
F1 alpha/Atp1. That page needs a separate fix.
