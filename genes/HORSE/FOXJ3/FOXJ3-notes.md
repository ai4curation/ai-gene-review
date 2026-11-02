# FOXJ3 (horse, F6SCJ5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior file). ProtNLM2 output was not consulted.

### Deep research
`just deep-research-falcon HORSE FOXJ3 --fallback perplexity-lite` failed: Edison API login returned
`403 Forbidden`, and the perplexity-lite fallback also failed. No deep-research file was produced; the
review uses the cached primary literature below and the reviewed UniProt records.

### Identity
- F6SCJ5 (TrEMBL, PE 4) is 623 aa; human Q9UPW0 is 622 aa, mouse Q8BUR3 623 aa.
- Global alignment (FOXJ3-bioinformatics/compare_sequences.py): 98.1% identity to human, 95.3% to mouse;
  fork-head domain (78-173) 95/96 identical with no gaps. Full-length canonical-like product, not a
  fragment or alternative gene model.
- PANTHER PTHR46078:SF3 (FORKHEAD BOX PROTEIN J3), same subfamily as human and mouse FOXJ3; FOXJ2 is SF1.

### Literature
- [PMID:19914232 "Foxj3 transcriptionally activates the Mef2c gene in a dose dependent fashion and binds to the conserved FBS"]
  mouse; also fewer type I fibres and impaired regeneration in mutants.
- [PMID:27739607 "survival of spermatogonia and participates in spermatocyte meiosis"] mouse conditional KOs
  (Mvh-Cre, Stra8-Cre); reduced meiotic gene transcripts. Abstract only.
- PMID:22740631 human U2OS siRNA screen: FOXJ3 knockdown disrupts cell-cycle reporter oscillation; source of the
  human IDA activator row but the evidence is indirect.

### Decisions
- Core: GO:0001228 activator activity (Pol II), GO:0000978 cis-regulatory DNA binding, GO:0045944, nucleus.
- General ancestors (GO:0000981, 0003700, 0003677, 0043565, 1990837, 0006355, 0006357) TOO_GENERAL.
- Spermatogenesis KEEP_AS_NON_CORE; male meiosis I MARK_AS_OVER_ANNOTATED (TF upstream of meiotic genes;
  PAINT node PTN002918318 propagated DNA-binding/TF terms but not the germline process terms).
- No NEW terms; the mouse muscle fibre-type phenotype is not added as process participation.

### Relative
Mouse Foxj3 (Q8BUR3), same SF3 subfamily, carries the experimental data (PMID:19914232, PMID:27739607). No
review exists in the repo for mouse Foxj3 or human FOXJ3. Donkey FOXJ3 (genes/EQUAS/FOXJ3) is the campaign partner.
No FamilyReview for PTHR46078 under interpro/panther/ (only metadata/entries); no module mentions FOXJ3.
