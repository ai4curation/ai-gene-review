# AMN1 (Q8IY45) review notes

## 2026-10-04: PAINT/affinage review

**Affinage symbol collision (real).** The affinage record for AMN1 describes only budding-yeast Amn1: Tem1/MEN antagonist, Ace2 degradation, the AMEN pathway. A blocking trust gate fired; I quarantined the output with --out and read it. It is not about the human protein, so it was not written to the gene folder and is not used.

Human-specific checks:
- **No human literature.** A Europe PMC search for human AMN1, excluding yeast, returns only expression-list and circRNA hits.
- **No F-box.** See `AMN1-bioinformatics/RESULTS.md`: no F-box is annotated or detected (InterPro, Pfam and SMART find only LRRs), and only the N-terminal 2-28 aligns weakly to the FBXL15 F-box.
- **No membrane features:** neither human AMN1 nor mouse Amn1 has an annotated transmembrane segment or signal peptide in UniProt.
- **Mouse microvillus source:** the IEA rests on an MGI IDA for mouse Amn1 from PMID:14321840, a 1965 study of vitamin B12-binding substances. The paper's other mouse annotations are to Cubn and Cblif, the cubilin-intrinsic factor system whose membrane partner is amnionless (symbol Amn), not Amn1.

Decisions:
- **SCF complex and SCF-dependent catabolism (IBA, node PTN002547163, F-box-containing FBXL donors): MARK_AS_OVER_ANNOTATED**, with propagation_review. These are a sequence inference, not a negative experiment.
- **Microvillus membrane (IEA from mouse): REMOVE.** The source is a homonym mix-up, confirmed in round 1 by MGI's own GO-CAM (see below). This is recorded as propagation_review SOURCE_BAD and raised as a question for MGI.
- **Gene recorded as WHOLLY_DARK.**

## Round 1 (PR #4034 review)

- **GO-CAM confirms the source-side mix-up.** `gocams/index.tsv` lists MGI:MGI:2442933 "Amn1 Mmus" in model 62900b6400002552, "Cobalamin transport, into enterocytes (Mouse)", as cargo receptor activity in the microvillus membrane, citing PMID:14321840 alongside Cubn and Cblif and with no Amn. That cargo-receptor role is amnionless's, the cubilin partner.
- **IBA donors:** all verified as F-box proteins. Per-row donor IDs, UniProt accessions and F-box spans are in `AMN1-bioinformatics/RESULTS.md` (round 2).

## Round 3 (PR #4034 review)

- **The GO-CAM names the right gene outright.** The Amn1 node's enabled_by evidence is ECO:0000266 orthology to UniProtKB:Q9BXJ7, human AMN, from PMID:14576052, the cubilin-amnionless paper. Human AMN carries the same location, cargo-receptor and cobalamin-transport triple by IDA from that paper. So the error is in the gene-product assignment, and is no longer circumstantial. The location row also projects from intrinsic factor (P27352). Cited, and named in the MGI question.
- **PANTHER separates AMN1 from every donor.** AMN1 is in PTHR13318:SF254 (PROTEIN AMN1 HOMOLOG); none of the 14 donors is. The donors are 300-807 aa, against AMN1's 258. fbox_check.py now reports PANTHER subfamily and length per donor.

## Round 4 (PR #4034 review)

- **The structural clause is now cited.** Human AMN carries microvillus membrane, cargo receptor activity and cobalamin transport by IDA from PMID:14576052, including is_active_in GO:0031528 (`genes/human/AMN/AMN-goa.tsv`). These are exactly the terms MGI's GO-CAM hangs on Amn1.
- **fbox_check.py additions:**
  - Per-row donor length ranges: 300-720 for GO:0031146, 300-807 for GO:0019005.
  - Donors now outside PTHR13318: Q8W104 and Q8BH16 are in PTHR13382, and Q06640 is unassigned. This is version drift since the 2023 IBD.
  - All six SF254 members from PTHR13318-entries.csv (human, mouse, rat, cow, orangutan, zebrafish; 249-258 aa) lack an F-box.
- **propagation_review:** failure_modes now include WRONG_ORTHOLOG_OR_PARALOG, and residue_claims_not_applicable explains the absent-domain case.
