# Chrm1 (rat) review notes

- Fetched P08482 (ACM1_RAT), RGD:2342, GeneID 25229. GOA: 43 rows, collapsed to 40 review rows.
- No deep-research provider available; see `Chrm1-deep-research-manual.md`.
- Core: G protein-coupled acetylcholine receptor activity (GO:0016907) at the plasma membrane,
  driving Gq/11-PLC signalling [PMID:2846274 "The cloned receptors mediated both adenylate
  cyclase inhibition and phosphoinositide hydrolysis, but by different mechanisms."].
- Rat GOA lacks the PLC-branch pathway term; proposed NEW GO:0007207 on rat receptor data
  (PMID:2846274, PMID:1317867). The receptor initiates this pathway, so it passes the
  participation bar (it performs ligand recognition and G-protein activation).
- GO:0090316 (IDA, PMID:17908240): read full text. The "translocations" are eGFP biosensor
  readouts (PKCepsilon recruitment to membrane, MARCKS release from membrane) of DAG/PKC
  signalling after methacholine stimulation; not a physiological protein-transport regulation.
  Marked over-annotated; flagged for expert.
- GO:0007603 phototransduction and GO:0009649 circadian entrainment are ISO from an RGD
  reference (RGD:14227533) that I could not inspect. Phototransduction proper is the opsin
  cascade; M1 does none of its steps -> over-annotation. Circadian entrainment left UNDECIDED.
- Human CHRM1 review (genes/human/CHRM1) used for consistency of actions.

## 2026-10-28 review-fix pass

- Added propagation_review to the two RGD:14227533 ISO rows (phototransduction: TERM_SCOPING_PROBLEM/ROLE_CONFLATION; circadian entrainment: UNRESOLVED). The source reference could not be inspected, which is recorded in the source comment and not as a status.
- The warning that no annotation cites Chrm1-deep-research-manual.md is accepted; every claim rests on primary papers.
