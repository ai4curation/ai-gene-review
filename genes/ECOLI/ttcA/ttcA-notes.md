# ttcA (P76055) notes

## Literature search (2026-11-24)

- PubMed query `TtcA 2-thiocytidine tRNA` returned 4 hits: PMID:14729701 (S. enterica
  ttcA genetics), PMID:17592039 (yeast Tuc1p, a TtcA-family U34 thiolase; not about
  E. coli TtcA), PMID:40107730 (E. coli TtcA [4Fe-4S] cluster and tRNA binding),
  PMID:30200616 (Citrobacter ttcA phenotypes; not cached, peripheral).
- GOA references: PMID:14729701, PMID:18304323 (cytosol proteomics), PMID:24914049
  (E. coli TtcA biochemistry, full text cached).
- Cached newly: PMID:40107730.
- No deep-research provider file was generated for this gene; the review rests on the
  primary papers above and the Swiss-Prot record.

## Findings

- TtcA catalyses ATP-dependent 2-thiolation of C32 in tRNA (s2C32). Sulfur comes from
  the IscS persulfide. [PMID:24914049 "TtcA catalyzes the post-transcriptional thiolation
  of cytosine 32 in some tRNAs."]
- Purified E. coli TtcA is a dimer with a [4Fe-4S] cluster bound by three Cys,
  essential for activity; non-redox reaction. [PMID:24914049 "TtcA is unique
  tRNA-thiolating enzyme using an iron-sulfur cluster for catalyzing a non-redox reaction."]
- In vitro activity needs ATP, DTT and reconstituted cluster [PMID:24914049 "No s2C32
  could be detected when reconstituted 6his-TtcA protein, D"] (sentence continues
  "TT, ATP, were omitted individually").
- The cluster does not contribute to tRNA binding; purely catalytic. [PMID:40107730
  "emphasizing the purely catalytic role of the [4Fe-4S] cluster"]
- S. enterica ttcA deletion abolishes s2C in tRNA; central CXXC motif required
  [PMID:14729701 "such a mutant has no detectable s(2)C in its tRNA"]. The GOA IMP row
  for E. coli cites this S. enterica paper; the function is not in doubt.

## Chemistry vs the staged RHEA row

RHEA:57048 (C32 + IscS-SSH + AH2 + ATP -> s2C32 + IscS + A + AMP + PPi) is a sulfur
transfer from a persulfide donor onto a tRNA base, the same reaction shape as
GO:0103016 tRNA-uridine 2-sulfurtransferase activity (MnmA) and GO:0140741
(ThiI). GO:0016783 sulfurtransferase activity is therefore a correct broader term;
no tRNA-cytidine-specific child exists yet. The GOA rows on GO:0016783 (IDA, IBA, IEA)
are accepted, so this review backs the staged broadMatch. A specific term
'tRNA-cytidine(32) 2-sulfurtransferase activity' is proposed.
