# SER3 review notes

## 2026-09-02 Update: GO:0006979 (response to oxidative stress) re-audit

Audited the existing `REMOVE` decision for the NAS annotation GO:0006979 (response to
oxidative stress), sourced to PMID:26527276 [PMID:26527276 "Here, we show that the yeast
PKM2 homolog, Pyk1, is a part of a novel protein complex named SESAME (Serine-responsive
SAM-containing Metabolic Enzyme complex), which contains serine metabolic enzymes, SAM
(S-adenosylmethionine) synthetases, and an acetyl-CoA synthetase"].

The cached record for PMID:26527276 is abstract-only (`full_text_available: false`), and
the abstract itself does not mention oxidative stress at all. The prior review pass used
this absence as grounds to `REMOVE` the annotation, reasoning that SER3's function
(serine biosynthesis) has no connection to oxidative stress.

That reasoning does not hold up under closer scrutiny of the underlying biology:

- SGD's own curation page for the SESAME complex
  (`yeastgenome.org/complex/S000377910/go`) lists "response to oxidative stress" among the
  complex's GO Slim biological-process terms. Ser3p is an established subunit of SESAME
  (this review already accepts SER3's SESAME membership as the basis for the
  `GO:1902494` "catalytic complex" and `GO:0040029` "epigenetic regulation of gene
  expression" annotations from the same reference, both correctly marked
  `MARK_AS_OVER_ANNOTATED` rather than `REMOVE`d).
- A follow-up study on SESAME-mediated H3T11 phosphorylation reports that reduced PYK1
  (the SESAME complex's kinase subunit) expression confers resistance to oxidative
  stress via H3T11 phosphorylation, tying complex activity mechanistically to an
  oxidative-stress phenotype. I attempted to fetch this follow-up paper for a citable
  quote (`just fetch-pmid`), but the candidate PMID resolved to an unrelated nursing
  tribute article, not the intended paper, so I could not add a verified inline
  citation for it; it is noted here only as corroborating context, not as a formal
  reference.
- I could not obtain full text of PMID:26527276 itself (paywalled at Cell/ScienceDirect
  and ResearchGate; 403 on direct fetch), so I cannot confirm whether Ser3p specifically
  (as opposed to Pyk1, or the complex generically) was assayed for a role in oxidative
  stress resistance in that paper.

**Conclusion**: the annotation was not fabricated or spurious — the SESAME complex
genuinely has a documented link to oxidative-stress resistance — but neither is there
direct evidence tying Ser3p's own dehydrogenase activity to that phenotype. Per project
policy (never confidently `REMOVE` an annotation on the strength of an abstract that is
simply silent on the topic; use `UNDECIDED` when full text cannot be accessed), changed
the action from `REMOVE` to `UNDECIDED` and rewrote `review.summary`/`review.reason` to
reflect this. No other annotation in this review was altered.

## 2026-09-04 Update: UNDECIDED → MARK_AS_OVER_ANNOTATED

Review feedback on PR #2943 pointed out that the decisive fact was already in the repo,
and it was not the one being cited. It is right, and it changes the call.

**The provenance is ComplexPortal, not a primary assay.** All three PMID:26527276 rows
in the GOA are `ASSIGNED BY = ComplexPortal`:

```
SER3-goa.tsv:14  involved_in  GO:0006979   response to oxidative stress          NAS  ComplexPortal
SER3-goa.tsv:15  involved_in  GO:0040029   epigenetic regulation of gene expr.   NAS  ComplexPortal
SER3-goa.tsv:16  part_of      GO:1902494   catalytic complex                     NAS  ComplexPortal
```

These are complex-level annotations on CPX-9181, propagated to every subunit.
`SER3-uniprot.txt:99` confirms the membership: `DR ComplexPortal; CPX-9181; SESAME
metabolic enzyme complex.`

That reframes the question. It is not "did Li et al. assay Ser3p?" but "does a
complex-level BP term belong on a metabolic-enzyme subunit?" — and this review already
answers that twice, marking the two siblings with **identical provenance** (same
reference, same evidence code, same assigning body) `MARK_AS_OVER_ANNOTATED`. Singling
out the third for `UNDECIDED` was inconsistent.

Crucially, the `reason` had named full-text access as the blocker. That was the wrong
diagnosis: **full text would not convert a complex-level propagation into a subunit-level
claim.** The limitation is structural, not evidentiary.

Changed the action to `MARK_AS_OVER_ANNOTATED` for consistency with GO:0040029 and
GO:1902494, and rewrote `summary`/`reason` around the checkable CPX-9181 grounding.

**Removed the uncited claims from the YAML.** `review.summary` had asserted an SGD
complex-page listing (bare URL, no `references` entry) and the PYK1/H3T11 oxidative-stress
finding that the notes above themselves admit could not be sourced — the candidate PMID
resolved to an unrelated nursing tribute article. Notes are the right home for
unverifiable corroboration; `review.summary`/`reason` are machine-readable output that
other tooling will believe. Both are now confined to this file.

Also addressed: the positional cross-reference ("the GO:1902494 annotation below") is
gone, terms are named directly; the summary no longer narrates the review file's own edit
history; the `supported_by` quote and the citation at the top of these notes were moved
off the paper title onto the abstract sentence that actually evidences Ser3p's SESAME
membership.

The two sibling annotations still carry title-only `supporting_text`, which was left
alone to keep this diff scoped to the annotation under review.
