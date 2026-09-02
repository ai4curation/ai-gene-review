# PDI1 review notes

## Update 2026-09-02

Audited `PDI1-ai-review.yaml` for factual accuracy. The top-level `description`
field asserted "Orthologous to human PDIA3." This is incorrect and has been
corrected to PDIA1/P4HB.

Evidence:

- The yeast PDI1 UniProt record (`PDI1-uniprot.txt`) gives the recommended
  protein name `Protein disulfide-isomerase` with `EC=5.3.4.1`
  (`DE   RecName: Full=Protein disulfide-isomerase;` / `DE   Short=PDI;` /
  `DE            EC=5.3.4.1;`). This is exactly the recommended name and EC
  number of human P4HB (UniProt P07237, gene symbol alias PDIA1), the
  founding/canonical human PDI. Human PDIA3 (UniProt P30101, ERp57/GRP58) is a
  distinct paralog with a different name and no independent EC entry of its
  own in the same catalytic sense; it acts chiefly on N-glycosylated
  substrates in complex with calnexin/calreticulin, a specialization not
  shared by yeast Pdi1p.
- The yeast PDI1 UniProt record cross-references `eggNOG; KOG0190; Eukaryota.`
  Human P4HB/PDIA1 (UniProt P07237) is cross-referenced to the same eggNOG
  orthologous group, KOG0190, confirming direct orthology between yeast PDI1
  and human PDIA1/P4HB rather than PDIA3.
- The gene's own `PDI1-deep-research-falcon.md` file frames the mammalian
  comparison around PDIA1, not PDIA3: "Although much of this work is framed
  around mammalian PDIA1, the mechanistic concepts apply to canonical yeast
  PDI architecture and redox cycling."

No GO term annotations were affected by this fix (the `existing_annotations`
list does not reference cross-species orthology); only the standalone
biological `description` field was corrected.
