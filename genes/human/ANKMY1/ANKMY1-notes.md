# ANKMY1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKMY1 (Q9P2S6) has **no GOA annotations**. It is a 941-residue protein with 7 ANK repeats, 3 MORN repeats and a MYND-type zinc finger; HPA classes it as testis-enhanced.
- **Literature:** PubMed (ANKMY1 in title or abstract) returns four papers. The only one with an experiment on the protein is an unvalidated TBXAS1 pulldown hit (PMID:29340222). The others are cancer prognostic signatures, a methylation screen and a lncRNA study.
- **PAINT:** family PTHR15897 (human and mouse ANKMY1 reviewed) has 0 PTN nodes (`just fetch-panther-paint`). Mouse Ankmy1 (Q8C0W1) has only ND rows in a QuickGO query; PAN-GO is 0. Family files committed.
- **Outcome:** `existing_annotations: []` (as for LRP5L), no core function, WHOLLY_DARK. No NEW terms: a MYND-domain zinc-binding inference would be domain-only.

## 2026-10-04 round 2 (reviewer comments on #4075)

- **Overturned finding.** PMID:29340222's 2017 statement that ANKMY1 was "available only at the transcript level" is superseded: UniProt records PE 1 (protein level) and the Proteomics identification keyword, independent of that paper. The finding carries a finding_review (OVERTURNED, superseded_by the UniProt record). The knowledge-gap provenance no longer cites it, and the boundary says ANKMY1 is dark in function, not in existence.
- **PAINT:** the "no PAINT nodes" claim rests on `just fetch-panther-paint PTHR15897` returning 0 annotated nodes. Correspondingly there is no PTHR15897-paint.tsv, since that file is only written for non-empty slices.
- **Testis framing** is now corroborated by UniProt's TSAL1 synonym and the original submission title "Testis specific ankyrin like protein".
