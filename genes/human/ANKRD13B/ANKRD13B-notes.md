# ANKRD13B notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKRD13B (Q86YJ7) is the ANKRD13A paralog, characterized in the same paper (PMID:22298428, full text). Its UIMs bind Lys63-linked chains on ubiquitinated EGFR, it sits at the plasma membrane with EGFR, and overexpression blocks rapid EGFR internalization.
- Unlike 13A and 13D, it also colocalizes with EEA1 (early endosome). It colocalizes with CI-M6PR (late endosome) in the perinuclear region.
- **All 19 GOA rows accepted.** IBA source_entities: PTN000966468 plus the self-donor Q86YJ7. Family PTHR12447 files are committed with ANKRD13A (#4091) and again here.
- **Affinage:** trust gate tripped (tie). Its narrative rests only on the RNF11 paper (PMID:31985874) and misses PMID:22298428, so nothing is used. The caveolin-1/VCP family result (PMID:26797118) is cited from the primary paper.
- **No NEW terms.** Same caveat as ANKRD13A: internalization evidence is overexpression-based.

## Round 3 (reviewer, PR #4092): direction of regulation

- The overexpression block of EGFR internalization does not fix the sign. Truncated ANKRD13A mutants "which were expected to act as dominant-negative versions" also inhibit, and the authors write that this leaves open "whether Ankrd 13 proteins have a stimulatory or inhibitory role in the process"; they conclude "we propose that Ankrd 13A, 13B, and 13D positively regulate the internalization of ligand-activated EGFR" [PMID:22298428]. RNAi could not settle it ("failed to deplete the three Ankrd 13 mRNAs/proteins simultaneously").
- So GO:0002091 (negative regulation of receptor internalization; IMP and ARBA IEA) → MODIFY to GO:0002090; GO:1905667 (IDA) → MODIFY to GO:1905666 on the same reasoning. The PAINT node already carries the neutral GO:0048259.
- Added PMID:31985874 (RNF11 binds ANKRD13A/B/D via the UIMs; abstract only) as a direct reference.
- IBA source_entities now list ANKRD13A (Q8IZ07) in all four blocks and ANKRD13D (Q6ZTN6) in the three it seeds (not GO:0005770).
