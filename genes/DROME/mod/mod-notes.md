# mod review notes

- fetch-gene resolved P13469 (MODU_DROME, FBgn0002780, GeneID 43764) as requested; 13 GOA rows.
- Literature synthesis in `mod-deep-research-manual.md` (manual, no API).
- Key decisions:
  - RNA binding (IEA) accepted as core; supported by PMID:10037720 (RRM-mediated motif-specific
    RNA binding) and RIP-seq (PMID:39700092).
  - DNA binding IDA accepted as core; sequence-specific DNA binding (PMID:16877538, abstract
    only) kept as non-core because PMID:10037720 found DNA binding by the basic domains to be
    non-specific [PMID:10037720 "two basic terminal domains independently contact DNA without
    sequence specificity"].
  - Splicing regulation and nuclear speck IBA rows come from SR-protein/hnRNP nodes of the
    huge PTHR24012 family. No Modulo evidence for splicing or speckles; Modulo is nucleolar.
    Marked over-annotated.
  - Protein binding (dCBP) modified to transcription coactivator binding (GO:0001223), as dCBP
    is a coactivator and the interaction was mapped (PMID:11854460).
  - NEW heterochromatin location (PMID:9718368 abstract, plus PMID:11854460 full text).
  - No NEW BP terms: centromere assembly, transposon silencing, neuroblast maintenance, growth
    all rest on RNAi/mutant phenotypes; the step Mod performs is unknown.
