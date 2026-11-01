# Cdkn1b (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Cdkn1b` resolved UniProt O08769 (unreviewed, RGD:69062, GeneID 83571);
  86 GOA rows, all keyed to O08769. No accession switch.
- No deep-research API keys; literature synthesis written by hand in
  `Cdkn1b-deep-research-manual.md`.
- Only 12 rat GOA papers; all are abstract-only in the cache. PMID:16987298 (n-butylidenephthalide,
  RG2 glioma) was read in full: p27 protein rises in RG2 cells after treatment
  [PMID:16987298 "similar results for p27, Bax and AIF were detected in RG2 cells after treatment with BP"].
  Correlative only, so no annotation proposed from it.
- Most GOA rows are ISO transfers from human CDKN1B (P46527) or mouse Cdkn1b (MGI:104565).
  Decisions follow the human review (genes/human/CDKN1B) where the donor term is the same, so that
  rat and human claims stay consistent:
  - REMOVE ISO for ubiquitin ligase activator activity, positive regulation of protein catabolic
    process, nuclear export: p27 is the substrate/cargo in each donor experiment.
  - MODIFY generic inhibitor/regulator MF rows to GO:0004861; generic cell-cycle regulation rows to
    GO:2000134.
- Mouse donor oddities recorded as source_defects (CHECK):
  - GO:0007096 regulation of exit from mitosis from PMID:9784491, which is about cell-cycle exit into
    terminal differentiation, not the anaphase-to-G1 exit from mitosis
    [PMID:9784491 "function redundantly to control cell cycle exit and differentiation of lens fiber cells and placental trophoblasts"].
  - GO:0071236 cellular response to antibiotic from PMID:19056892: the cached full text does not name an
    antibiotic stimulus applied to p27 (the CRM1-independence test may have used leptomycin B, unverified).
- Hsc73 rows (PMID:10198213, rat FRTL-5): co-IP in both directions; chaperone binding row MODIFY to the
  more specific Hsp70 protein binding, which the gene already carries.
- Rat-specific core evidence: p27 bound to cyclin E-CDK2 in regenerating rat liver when CDK2 activity is low
  [PMID:10952244]; shRNA knockdown in rat cochlea induces proliferation [PMID:23612739]; MENX rats carry a
  Cdkn1b frameshift [PMID:17030811].
