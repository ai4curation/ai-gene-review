# SER3 review notes

## 2026-09-02 Update: GO:0006979 (response to oxidative stress) re-audit

Audited the existing `REMOVE` decision for the NAS annotation GO:0006979 (response to
oxidative stress), sourced to PMID:26527276 [PMID:26527276, "Serine and SAM Responsive
Complex SESAME Regulates Histone Modification Crosstalk by Sensing Cellular Metabolism"].

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
