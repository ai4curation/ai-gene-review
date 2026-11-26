# elnb notes

## 2026-09-27 (claude-opus-5-5, DANRE_DUPLICATION pair review elna/elnb)

- Accession: A0A8M1NAS7 (2020 aa, RefSeq NP_001041529, unreviewed; one of ~8 elnb isoform entries, 2020-2104 aa).
  Germline-mutant paper cites a 2,041-aa full-length protein [PMID:41712646 "compared to the full-length 2,041-amino acid protein in wild-type fish"],
  so this entry is a slightly shorter isoform; PANTHER uses A0A8M6Z3N0 (2104 aa, XP-backed). Not a problem for GO review.
- GOA: only 2 InterPro2GO IEA + 2 root ND rows; no GOA-cited PMIDs.
- Expression restricted to the bulbus arteriosus (BA) in zebrafish, medaka, stickleback
  [PMID:26783159 "We found that elnb expression patterns were restricted to the BA, while elna was observed in various tissues in both medaka"].
- Function: morphant BA hypoplasia with less elastin and ectopic cardiomyocytes; rescued by elnb but not elna or Polypterus eln mRNA
  [PMID:26783159 "both of these Polypterus eln mRNAs did not rescue the elnb morphant phenotype"].
  Germline PTC mutant (2026, exon 2, 81-aa truncation) more severe than morphant
  [PMID:41712646 "Homozygous elnb mutants exhibited a more severe hypoplastic BA than elnb morphants and developed ectopic cardiomyocytes in the BA"];
  loss of BA low stiffness; artificial stiffening phenocopies.
- Decisions: ND x2 REMOVE; GO:0005201 MODIFY -> GO:0030023; GO:0031012 ACCEPT; NEW GO:0071953 elastic fiber (IDA, PMID:17112714);
  NEW GO:0048251 elastic fiber assembly (IMP, PMID:26783159); NEW GO:0003232 bulbus arteriosus development (IMP, PMID:41712646).
  BA development comparator: human ELN has GO:0003151 outflow tract morphogenesis (IMP); existing GO:0003232 annotations are zebrafish IMP (pak1, dhfr, pbx4).
  Not added: smooth muscle differentiation / cell fate terms (effect is indirect, via matrix stiffness).
- Deep research: elnb-deep-research-falcon.md appeared during the session and was used as a pointer; it does not cover PMID:41712646.
  It cites Boezio 2020 (Alk5-Fbln5, Eln2 coverage) and Nahia 2024 (scRNA-seq), not fetched/used here.
- Pair page: projects/DANRE_DUPLICATION/pairs/elna_elnb/elna_elnb.md
