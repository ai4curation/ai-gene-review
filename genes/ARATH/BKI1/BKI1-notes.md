# BKI1 (At5g42750, UniProtKB:Q9FMZ0) curation notes

Session 2026-10-05/06 (brassinosteroid_signaling module curation).

- Identity checked: BKI1_ARATH, Q9FMZ0, At5g42750.
- Falcon deep research attempted; provider returned HTTP 402 (no report produced).
- BKI1 is a BRI1-interacting negative regulator [PMID:16857903 "We report a BRI1-interacting protein, BKI1, which is a negative regulator of brassinosteroid signaling."]
- Mechanism: limits BRI1-BAK1 association [PMID:16857903 "BKI1 is a substrate of BRI1 kinase and limits the interaction of BRI1 with its proposed coreceptor, BAK1"]
- Release by Tyr phosphorylation in [KR][KR] membrane motif [PMID:21289069 "Phosphorylation occurs within a reiterated [KR][KR] membrane targeting motif, releasing BKI1 into the cytosol"]
- Positive role of released BKI1 via 14-3-3 [PMID:22075146 "the cytosolic BKI1 antagonizes the 14-3-3 s and enhances accumulation of BRI1 EMS SUPPRESSOR 1 (BES1)/BRASSINAZOLE RESISTANT 1 (BZR1) in the nucleus"]
- GO:0010423 (negative regulation of BR biosynthesis) IMP + IBA: sign looks inconsistent with BKI1 being an inhibitor of signalling (signalling represses biosynthesis); left UNDECIDED since PMID:16857903 is abstract-only.
- Added NEW GO:1900458 negative regulation of BR mediated signaling pathway (BKI1 performs the inhibitory step itself).
- Nuclear ISM prediction removed (no evidence; polybasic motif likely mis-read as NLS).

## Follow-up (resolving UNDECIDED rows)
- Europe PMC: PMID:16857903 has no PMC/open-access full text.
- Web search: Wang et al. 2011 Dev Cell (PMID:22075146) reportedly shows that BKI1-YFP overexpression increases CPD and DWF4 expression. If so, the sign of GO:0010423 (negative regulation of BR biosynthesis) is doubtful. Not verified from cached text.
- Decision: the IMP is kept as KEEP_AS_NON_CORE, deferring to the curator with the sign caveat. The IBA (node seeded only by BKI1's own IMP) is set to MARK_AS_OVER_ANNOTATED with a propagation_review (SOURCE_WEAK_OR_INFERRED; REGULATORY_SIGN_INVERSION, ROLE_CONFLATION).
