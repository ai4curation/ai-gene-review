# HNF1A (P20823) — review notes

Deep research: the client timed out, so the review was grounded in UniProt, GOA and cached
abstracts. The provider finished afterwards and `HNF1A-deep-research-falcon.md` is committed; it
was checked against this review on 2026-10-11.

- It agrees on the core annotation: HNF1A is a nuclear, sequence-specific dimeric transcriptional
  regulator, not an enzyme or a transporter, binding the inverted palindrome GTTAATNATTAAC through
  a POU-specific region plus an atypical POU homeodomain, with an N-terminal dimerization domain
  and a C-terminal transactivation region.
- It supports the DCoH/PCBD1 call: PCBD1 can stabilize the dimer, but the dimerization-domain
  protein also dimerizes without it, so the cofactor is not required for dimerization.
- It names the direct targets with the strongest human-cell support, each of which the review
  should treat as transcriptional regulation and not as HNF1A performing the downstream function:
  the pancreatic HNF4A P2 promoter (2.3 A crystal structure of the DBD-P2 complex), hepatic PCSK9
  (mutating the HNF1 element cut reporter activity to about 5% of wild type, cooperating with
  SREBP2), and renal SLC51B.
- It adds a caution the review already observes: a ChIP-seq peak assigned to its nearest gene is
  an annotation resource, not proof of regulation. Peak counts differ between preparations (739 in
  day-20 endocrine progenitors, 427 in islets, 4,791 in HepG2).
- It notes that purified protein shows phase separation and an intrinsically disordered C-terminal
  activation region in vitro, which does not establish functional condensates in human beta cells.
  Nothing in this review annotates that.

- Homeodomain/POU-like TF binding GTTAATNATTAAC as dimer [PMID:12453420 "Two identical protein molecules are bound to the"];
  coactivator DCoH/PCBD1 [PMID:10966642 "which binds the coactivator, dimerization cofactor of HNF-1 (DCoH)"].
- Renal SGLT2/glucose reabsorption [PMID:11269503 "MODY3 patients are also characterized by a"].
- PMID:1989880 is the TCF-1 (TCF7, HMG-box, T-cell) cloning paper [PMID:1989880 "TCF-1 contained a single"]; the three
  HNF1A IDA annotations citing it (DNA binding, DNA-binding TF activity, positive regulation of transcription) are
  likely alias (TCF1) confusion -> UNDECIDED, reference_review MISCITED. Activities themselves are correct for HNF1A.
- HI link is weaker than for HNF4A: [PMID:17407387 "Birthweight and prevalence of neonatal hypoglycaemia were not increased in HNF1A-mutation carriers."]
- insulin secretion (InterPro2GO) MARK_AS_OVER_ANNOTATED; positive regulation of insulin secretion kept NON-CORE.
