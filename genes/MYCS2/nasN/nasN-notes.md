# NasN evidence review

## 2026-10-29: identity, chemistry and annotation decisions

The failed Falcon authentication attempt is recorded in the foundation provider log; no provider report was invented. The six original annotation payloads and both raw inputs are preserved.

The corrected DQ866862.1 sequence differs from CP000480.1 MSMEG_4206 by G insertion at nucleotide1850 and translates exactly to the committed A4ZHT3 sequence (1351 aa). Reproducible code and computed proof are in `modules/bacterial_assimilatory_nitrate_reduction-source-analysis/`; `--fetch` obtains missing versioned ENA inputs. [PMID:33471823 "A BLAST search revealed that MSMEI_4108 corresponds to MSMEG_4206"]

The full PMID32111737 article is cached under its normal PMC URL, not in the abstract-only PMID cache. It directly establishes native nitrate loss/rescue and purified enzyme chemistry. [url:https://pmc.ncbi.nlm.nih.gov/articles/PMC7152768/?report=xml "NADPH was preferred over NADH, as shown by a 26-fold greater activity with NADPH relative to NADH"] The two donor-specific reactions refine the generic oxidoreductase row; only NADPH is the main core activity. The electronic sulfite assignment is rejected with an upstream correction record.

The enzyme is oxygen-sensitive despite greater tolerance than the Amycolatopsis comparator. Do not transfer its kinetics or donor preference to the Pseudomonas fusion. Native activity in cytoplasmic fractions supports the cytoplasm correction. [same full article "NasN was shown to be oxygen-sensitive"]

No NEW rows were added. Direct native evidence supports nitrate assimilation in the core summary. A preliminary exact-term comparator query for SYNE7 NarB P39458 and BACSU NasC P42434 returned no GO:0042128 rows; their seeded GOA instead includes a denitrification mapping under review. This absence is not treated as evidence that curators missed a pathway-completeness annotation. The term definition/ancestors were read and no A4ZHT3 match occurs in the cached GO-CAM index. Query results are retained in the ignored resume audit log.
