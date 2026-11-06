# ybbH (MurR, Q45581) notes

## 2026-10-30 — initial review (LBNL hackathon, dashboard gene NZ_CP017763.1_2226)
- Operon (minus strand): ybbI(murQ)–ybbH(murR)–ybbF(murP)–ybbE(amiE)–ybbD(nagZ)–ybbC(namZ). Naming from PMID:20400549 and PMID:27729505 ("murR (formerly ybbH)").
- Only direct B. subtilis evidence: ΔmurR raises PmurQ-lacZ (ectopic, at amyE) while PptsA is unaffected (PMID:30038046, Fig. 8B). The deep-research report missed this paper.
- Operator binding and the MurNAc-6P effector are from E. coli MurR (PMID:18723630).
- MurR vs HexR: pairwise identity is 27.0% to E. coli MurR and 33.0% to E. coli HexR (`ybbH-bioinformatics/RESULTS.md`), so the assignment rests on gene context plus the reporter, not on sequence. A phylogeny would settle the subfamily.

## 2026-10-30 — changes after PR #5754 review
- GO:0003677 row: MODIFY target changed from GO:0001217 (a different branch, not a descendant) to GO:0043565 sequence-specific DNA binding.
- Carbohydrate utilization: one position across both files. The pathway recovers cell wall MurNAc under nutrient limitation (PMID:31296364), which fits GO's "carbohydrate utilization". Added GO:0180068 as NEW (IMP, PMID:30038046); dashboard GO:0043610 stays COR. The NTR for negative regulation of N-acetylmuramic acid catabolic process stays, because no signed-negative or unsigned term exists (checked QuickGO: only GO:0160159 positive).
- GO:0097367: ACCEPT → KEEP_AS_NON_CORE (effector untested in B. subtilis).
