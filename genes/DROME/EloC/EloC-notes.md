# EloC (Elongin C) review notes

Accession: E2QCI6 (expected accession; `just fetch-gene DROME EloC` resolved to Q7JWD6, which also has GOA rows, so the folder was refetched with `--alias EloC` on E2QCI6). Module: dmel_vcb_ubiquitin_ligase.

## Literature journal

- VCB-Cul2: [PMID:11006129 "Biochemical studies have shown that Drosophila VHL protein binds to Elongins B and C directly, and via this Elongin BC complex, associates with Cul-2 and Rbx1."]; [PMID:11006129 "Like human VHL, Drosophila VHL complex containing Cul-2, Rbx1, Elongins B and C, exhibits E3 ubiquitin ligase activity."]
- Elongin complex and wing veins: [PMID:24204884 "Chromatin immunoprecipitation experiments indicate that Elongin C and Corto bind the vein-promoting gene rhomboid in wing imaginal discs."]
- Socs36E/Cul5 JAK/STAT [PMID:23885117]; Dora TDMD ligase reported as CRL3 with EloB/C [PMID:40328417]; CrPV-1A hijacking [PMID:30308158].

## Decisions

- Core: GO:0160072 scaffold (BC-box adaptor, as for SkpA) contributing to GO:0061630; GO:0030891 VCB complex. Second core function: Elongin complex / Pol II elongation.
- ARBA general complexes -> MODIFY (GO:0140535 -> GO:0030891; GO:1990234 -> GO:0031462); GO:0006511 -> MODIFY GO:0043161.
- Viral process: MARK_AS_OVER_ANNOTATED (host ligase hijacked), same for EloB, Cul2, Roc1a.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `EloC-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.
