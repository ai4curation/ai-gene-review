# spn-A review notes

- 2026-10-28: Created review. fetch-gene resolved Q27297 (RAD51_DROME, FBgn0003479, GeneID 43577) as expected.
- Core: DNA strand exchange activity (GO:0000150), DNA-dependent ATPase (GO:0008094), ssDNA/dsDNA binding; DSB repair via HR (GO:0000724), strand invasion, SDSA. See spn-A-deep-research-manual.md for quotes.
- Developmental rows (axis polarity, gurken mRNA localization, oocyte fate) are checkpoint-mediated consequences of failed meiotic DSB repair [PMID:14592983 "As detailed in Table II B, females doubly mutant for chk2 and spnA produced progeny with wild-type egg shape (100 versus 6%)"]; marked over-annotated, not removed (sources abstract-only).
- GO:0010569 regulation of DSBR via HR (PMID:24368780) is the wrong relation: spn-A executes HR; recorded as source defect, MODIFY to GO:0000724.
- NEW: site of double-strand break (IDA, PMID:25632158).
- Curation gap: meiotic crossover role in the absence of Dmc1 not directly measured in cached literature.
