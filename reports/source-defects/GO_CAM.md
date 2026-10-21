# Source-record defects for GO_CAM

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** gomodel:67e5e74400000148/67e5e74400000172
- **Subject:** AGI_LocusCode:AT2G45160
- **Field:** enabled_by
- **Change:** AGI_LocusCode:AT2G45160 → AGI_LocusCode:AT5G64610 (HAM1, MYST histone acetyltransferase 1 (UniProtKB:Q9FLF7))
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `gocams/67e5e74400000148/67e5e74400000148-review.yaml`

The histone H4K5 acetyltransferase activity (GO:0043995) is enabled_by AT2G45160, which is SCARECROW-LIKE 27 (UniProtKB:Q7XJM8). SCL27 is a GRAS transcription regulator that also carries the alias HAM1 (HAIRY MERISTEM 1). The acetyltransferase in all three cited papers (PMID:17877703, PMID:23273925, PMID:25183522) is the MYST protein HAM1, AT5G64610 (UniProtKB:Q9FLF7; UniProt gene names HAM1 HAG4 At5g64610). The enabler should be AT5G64610. HAM2 (AT5G09740) is redundant and could be added.

> two MYST histone acetyltransferases HAM1 and HAM2 work redundantly to acetylate histone H4 lysine 5 (H4K5ace) in vitro.
> — PMID:23273925

## 2. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** gomodel:67e5e74400000148/67e5e74400000149
- **Subject:** AGI_LocusCode:AT1G02740
- **Field:** has_input
- **Change:** remove AGI_LocusCode:AT2G45160 from has_input
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `gocams/67e5e74400000148/67e5e74400000148-review.yaml`

The MRG2 H3K36me3 reader activity has AT2G45160 (SCL27, a GRAS protein with the alias HAM1) as a has_input. The partner the paper reports is the MYST acetyltransferase HAM1, AT5G64610 (UniProtKB:Q9FLF7). Separately, a recruited effector enzyme is not the input of a reader activity. The MRG2-to-HAM1 relationship is already captured by the causal edge to the acetyltransferase activity, so the has_input should be removed rather than re-pointed.

> interact with the histone H4-specific acetyltransferases (HAM1 and HAM2)
> — PMID:25183522
