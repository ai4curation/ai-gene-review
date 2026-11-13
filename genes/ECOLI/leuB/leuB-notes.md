# E. coli leuB (P30125) curation notes

Provider deep research was not run for this gene. These notes record the
literature read for the review (cached abstracts under `publications/`).

- Purified E. coli IPMDH: cation-dependent, Mn2+ preferred
  [PMID:9003442 "the activity of E. coli IPMDH was dependent on the divalent cations, Mg2+ or Mn2+, with Mn2+ being the preferred cation"];
  kinetics [PMID:9003442 "the K(m) of E. coli IPMDH was 105 microM for IPM and 321 microM for NAD, the kcat was 69 s-1"].
- Crystal structure of the E. coli enzyme at 2.1 A [PMID:9086278 "The structure of the E. coli enzyme was refined at a resolution of 2.1 A"].
- Promiscuous D-malate activity [PMID:32412093 "the turnover constant (kcat ) of IPMDH for d-malate is about 30-fold lower than the kcat for 3-isopropylmalate"]. Not proposed as a GO annotation: weak secondary activity of uncertain physiological relevance.
- leuB mutants lack IPMDH activity [PMID:4570778 "with a mutation in gene B lacked beta-isopropylmalate dehydrogenase activity"].
- The two `cellular response to amino acid starvation` IMP rows (PMID:10220423, PMID:15133107) use a leuB- allele as a reversion reporter; the abstracts say so explicitly, so both rows were removed.
- Actions aligned with PSEPK leuB, yeast LEU2 and S. pombe leu1 (metal and NAD binding non-core; GO:0016616 TOO_GENERAL).
