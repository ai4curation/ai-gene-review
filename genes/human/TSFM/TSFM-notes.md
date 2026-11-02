# TSFM (mitochondrial EF-Ts) curation notes

## Deep research
`TSFM-deep-research-claude-code.md` ran for 40 s with 2 web searches (`web_search_requests: 2`) and 4 citations. It states the
search returned thin results and the report rests mainly on the UniProt record and background knowledge. Used as leads only;
all cited disease papers were fetched and read at abstract level (two have full text cached).

## Evidence
- Recombinant bovine EF-Tsmt "forms a complex with E. coli elongation factor Tu. This complex is active in poly(U)-directed polymerization of phenylalanine" [PMID:7615523].
- COXPD3 (Smeitink et al. 2006): "EFTs functions as a guanine nucleotide exchange factor for EFTu"; R333W reduced EF-Ts and EF-Tu by 75% and 60%;
  "These phenotypes and the translation defect were rescued by retroviral expression of either EFTs or EFTu" [PMID:17033963].
- Emperador et al. 2016: cDNA rescue of a childhood-onset ataxia/HCM TSFM mutation [PMID:27677415].
- Ahola et al. 2014: compound heterozygous variants destabilise EF-Ts, with a mitochondrial translation defect [PMID:25037205].
- Adult cardiomyopathy case: EF-Ts "participates in the elongation step of mitochondrial translation by binding and stabilizing" EF-Tu [PMID:30911037].

## Decisions
- Core: guanyl-nucleotide exchange factor activity (GO:0005085) in mitochondrial translational elongation, matrix.
  Translation elongation factor activity (GO:0003746) accepted as the conventional broader term.
- All 10 protein-binding rows (Y2H hits with non-mitochondrial proteins) REMOVE.
- RNA binding (HDA, mRNA-bound proteome) MARK_AS_OVER_ANNOTATED: EF-Ts has no known RNA-binding activity.
- No NEW terms. Binding to EF-Tu (e.g. translation elongation factor binding, GO:0061770) is covered by the GEF activity and was not added.
