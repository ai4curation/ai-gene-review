# BEH2 (Q94A43, At4g36780) review notes

## Session 1 (create review)

- fetch-gene resolved Q94A43 (Swiss-Prot, TAIR AT4G36780, GeneID 829831): correct entry.
- 12 GOA rows. Literature: see BEH2-deep-research-manual.md (manual; no API keys).
- Key full-text paper: PMID:20128883 (ASKtheta Y2H, in vitro/in vivo phosphorylation,
  nuclear CFP-BEH2). PMID:35695417 full text (constitutive nuclear localization; BR
  represses BEH2 transcription; OX RNA-seq). PMID:37926922 (source of the IDA nucleus
  and IPI rows) is abstract-only in cache.
- IPI protein binding (PMID:37926922) With/From: AT3G05840 (ASK-gamma/SK12), AT4G18710
  (BIN2), AT3G61140. AT3G61140 is CSN1/FUS6 (UniProt P45432), not a GSK3-like kinase;
  the paper examined "interaction with GSK3-like kinases", so AT3G61140 is probably a
  mis-keyed AT3G61160 (ASK-beta). Recorded as SUSPECTED source defect (CHECK); cannot
  confirm without full text.
- TAS row PMID:11970900 (Wang et al. 2002, BZR1 paper): term is right for BEH2 by
  family membership; the paper is about BZR1 (abstract) - kept, deferring to TAIR.
- Decisions: DNA-binding TF activity and cis-regulatory DNA binding accepted as core
  (family/domain + IBA from BZR1/BES1; no BEH2-specific EMSA found - flagged as question).
  DNA-templated transcription (IEA) modified to regulation of DNA-templated transcription.
  Bare protein binding removed (policy). NEW protein heterodimerization activity from
  the PMID:37926922 abstract (heterodimerization with family members).
- No NEW BP terms: OX-derived stress/photosynthesis enrichment is indirect.

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0006355 / PMID:11970900: defect withdrawn (evidence depth: ABSTRACT). QuickGO shows TAIR made the identical TAS row from this paper on the same day for all six family members (BZR1, BZR2, BEH1-4), i.e. a deliberate family-level author-statement annotation, not a mis-keyed PMID. The defect rested only on the abstract not naming homologs; nothing in the record is identifiably wrong. Full text (Dev Cell 2002) could not be obtained (403), so the family statement itself was not seen.
