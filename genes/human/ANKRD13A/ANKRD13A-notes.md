# ANKRD13A notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKRD13A (Q8IZ07) is a UIM-containing reader of Lys63-linked polyubiquitin. Evidence:
  - It binds ubiquitinated EGFR at the plasma membrane, and overexpression blocks rapid EGFR internalization (PMID:22298428, full text, the source of most GOA rows).
  - With VCP it routes ubiquitinated caveolin-1 to lysosomes (PMID:26797118).
  - It recruits VCP for outer-membrane rupture in PINK1/Parkin mitophagy (PMID:40975168).
- **All 18 GOA rows accepted:** ub-modified protein reader (IBA/IDA/IEA/IPI), receptor-internalization regulation, protein localization to endosome, and plasma membrane, late endosome, perinuclear and cytoplasm locations. The late endosome and perinuclear rows rest on CI-M6PR colocalization in PMID:22298428.
- **Caveat:** the internalization evidence is overexpression; the suggested experiment is a loss-of-function test.
- **Affinage:** trust gate tripped (pairwise tie), so each claim was checked. The used claims match their papers; the Toxoplasma, RIP1 and RNF11 single-study claims are not used. (Round 2: the HLA-I claim was initially missed; see below.)
- **PAINT:** PTHR12447 node PTN000966468, seeded by ANKRD13A/B/D (self-donor expected). Family files committed.
- **No NEW terms:** the VCP-recruitment roles are captured by the reader MF, and mitophagy rests on one 2025 study.

## 2026-10-04 round 2 (reviewer comments on #4091)

- **Seed comment fixed.** The late-endosome IBD (GO:0005770) is seeded only by ANKRD13A and ANKRD13B, per PTHR12447-paint.tsv; the other three IBDs also include ANKRD13D. source_entities comments are now per term.
- **Missed contrary claim.** Affinage's HLA-I finding (PMID:34694569, full text) says upregulated ANKRD13A *promotes* HLA class I internalization in AML cells, the opposite direction to the EGFR result. It is now recorded on the internalization rows and as a cargo-dependence question. The core function keeps the direction-neutral GO:0048259 for this reason.
- **Mitophagy:** no process term is proposed from the single 2025 study; this is now stated in the affinage reference_review.
- The cytoplasm row reason now uses the plasma-membrane anchoring quote.

## Follow-up after merge: direction of regulation

- The reviewer on ANKRD13B (#4092) showed that PMID:22298428 does not support a negative sign. Dominant-negative truncations inhibit like wild type, and the authors write "we propose that Ankrd 13A, 13B, and 13D positively regulate the internalization of ligand-activated EGFR". The ANKRD13A review had ACCEPTed GO:0002091 on the overexpression phenotype.
- Changes: GO:0002091 ×2 → MODIFY to GO:0002090; GO:1905667 (IDA) → MODIFY to GO:1905666. Description, core function and the cargo-dependence question no longer say "restrains". For ANKRD13A, the HLA-I report (PMID:34694569, promotion) points the same way.
