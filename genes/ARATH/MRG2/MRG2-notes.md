# MRG2 notes

## 2026-11-24

Automated Falcon/Perplexity Lite deep research failed with the same provider availability problem seen for SDG7 and SDG8, so I summarized the primary evidence manually in `MRG2-deep-research-manual.md`.

The initial `fetch-gene` call produced an empty QuickGO table for MRG2, even though the UniProt record carried TAIR/UniProt GO assertions for nucleus, H3K36me3 reader activity, H3K4me3 reader activity and promoter chromatin binding. A later retry succeeded and seeded 25 QuickGO rows spanning 21 distinct GOA assertions; this review now adjudicates the standing H3K36me3-reader, H3K4me3-reader, promoter-specific chromatin binding, NuA4-complex, nucleus, protein binding, transcription and flowering annotations.

The PAINT NuA4-complex annotation is plausible enough to keep: the node is seeded by Arabidopsis MRG1 as well as fungal, fly and vertebrate MRG/MRG15-family NuA4 subunits, and Arabidopsis MRG2 recruits the HAM1/HAM2 MYST acetyltransferases to methylated H3 chromatin. The row still deserves a composition caveat because Xu et al. did not purify a stable plant NuA4 complex containing MRG2.

GO-CAM consistency notes for the final shared PR:

- The MRG2 H3K36me3-reader activity and chromatin location are supported.
- The model's SCL27/AT2G45160 input on MRG2 is unsupported and should be removed; that entity is a GRAS transcription regulator that shares the HAM1 alias, while the MRG2 paper names MYST acetyltransferase HAM1/AT5G64610 plus redundant HAM2/AT5G09740.
- MRG1/AT4G37280 is a redundant MRG reader in both 2014 MRG papers and could be added beside MRG2.
