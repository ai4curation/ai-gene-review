# col1a1b notes

## 2026-09-28 (claude-opus-5-5, DANRE_DUPLICATION pair review col1a1a/col1a1b)

- **Deep research failed.** Edison returned 402 Payment Required and the OpenAI key is invalid. It was not retried. The literature research was done by hand (Europe PMC REST search plus cached publications).
- Accession Q6PEI9 (1449 aa, TrEMBL, "Collagen, type I, alpha 3", synonym col1a3, RefSeq NP_958886). It holds all 9 GOA rows. There are no GOA rows from PMID:30082390 or PMID:26876635, although both study col1a1b directly.
- Protein: 78% identical to alpha1(I) [PMID:26876635 "Amino acid (AA) sequence alignments revealed that zebrafish proα1(I) and proα3(I) chains share 78% of AA identity"]. The pair script gives 76.3% (global BLOSUM62). One inter-chain C-propeptide Cys is lost [PMID:26876635 "Interestingly, in proα3 this latter domain, crucial for chain association in the trimer, lacks one of the 4 conserved cysteine residues involved in inter-chain bonds (Cys63 of the proα1(I) C-propeptide)"]. Confirmed on the UniProt sequences as col1a1a C1265 vs col1a1b S1267 (col1a1b-bioinformatics/RESULTS.md). Gly-Gly content is higher [PMID:26876635 "In zebrafish α3(I) the number of GG + GGG repeats is about two-fold higher than in zebrafish α1(I)"].
- Protein-level presence: [PMID:26876635 "The identification of α3(I) peptides demonstrated for the first time the translation of the col1a1b gene in zebrafish."]. The chains are roughly 1:1:1 in adult bone, skin and scales, with alpha3/alpha1 higher in skin and scales [PMID:26876635 "SRM and spectral counting mass spectrometry data shows a statistically significant higher α3(I)/α1(I) ratio in external (skin and scales) versus internal (bone) tissues pointing out to a tissue-specific collagen composition."].
- Genetics (PMID:30082390): the sa12931 nonsense null is viable, with no alpha3(I) peptides [PMID:30082390 "Accordingly, in col1a1b−/− mutants, no tryptic peptides of α3(I) could be detected, confirming decay of mutant col1a1b mRNA transcripts."]. This is a PTC/NMD allele, and paralog upregulation (transcriptional adaptation) was not tested. The double heterozygote with col1a1a is fragile. The dominant dmh29 allele is severe.
- Comparative: alpha3 is present in skin collagen of most teleosts but absent from some [PMID:3677606 "The skin collagen seems to exist as an alpha 1 alpha 2 alpha 3 heterotrimer in many teleosts and as an (alpha 1)2 alpha 2 heterotrimer in some teleosts."]. It is reported in sturgeon [PMID:1617936 "The present study, however, has revealed the occurrence of alpha 3(I) in a chondrostean fish, white sturgeon."]; this is my caveat, since sturgeons have their own polyploidy. It is the fastest-evolving chain [PMID:34430038 "with the α3 (I) sequence evolving the fastest, followed by the α2 (I) chain"]. In trout, skin collagen is a heterotrimer and muscle collagen is (alpha1)2alpha2 (PMID:11358497).
- Decisions:
  - skeletal system development IMP (dmh29): ACCEPT.
  - ECM structural constituent conferring tensile strength (IBA), collagen fibril organization (IBA), ECM (IBA), and the IEA rows: ACCEPT.
  - cytoplasm IBA: REMOVE. Its sole source is the col1a1a mRNA-based IDA.
  - skin development and skeletal system morphogenesis (IBA): non-core, the same as col1a1a.
  - NEW GO:0005584 collagen type I trimer (IDA, PMID:26876635), the same as col1a1a.
  - No col1a1b-specific process term. Nothing col1a1b does is absent from col1a1a.
- Pair page: projects/DANRE_DUPLICATION/pairs/col1a1a_col1a1b/col1a1a_col1a1b.md
