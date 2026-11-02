# bckd-1A review notes

## 2026-10-28 initial review

- Fetched O45924 (ODBA_CAEEL; Y39E4A.3). 8 GOA rows.
- No deep-research provider available; manual literature summary in
  `bckd-1A-deep-research-manual.md`.
- Key paper PMID:15340492 (full text) shows only RNAi + GC fatty-acid evidence for
  Y39E4A.3 ["RNAi of Y39E4A.3 led to a significant decrease in C15ISO and C17ISO production"];
  there is no enzyme assay. The EXP row for GO:0003863 (UniProt) therefore rests on a
  knockdown phenotype plus homology; the activity is nonetheless clearly correct for a
  BCKDHA ortholog. Accepted, with a PROBABLE WRONG_EVIDENCE_CODE source defect.
- PMID:26683372 confirms E1alpha RNAi reduces mmBCFA and shows BCKDH deficiency causes
  BCAA accumulation and larval arrest suppressible by mmBCFA supplementation.
- GO:0006633 (UniPathway IEA) refined to GO:1902321 methyl-branched fatty acid
  biosynthetic process. Comparator check (QuickGO, GO:1902321): elo-5, elo-6 (IMP,
  PMID:15340492) and Drosophila FASN2 carry it; these are enzymes performing steps. BCKDH
  E1 performs the primer-forming step whose branched acyl group becomes the carbon
  skeleton of the product, so it does work in the process (not just a substrate/
  requirement).
- GO:0016624 IEA refined to GO:0003863 (as in genes/human/BCKDHA).
- Matrix location: transit peptide + function of the complex; no worm assay.
