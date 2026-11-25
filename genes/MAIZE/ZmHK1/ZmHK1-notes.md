# ZmHK1 review notes

## 2026-10-28 initial review

- fetch-gene resolved Q9FRY7 (GeneID 541634) as requested; GOA has 16 rows (AgBase IDA/RCA from
  PMID:15064375, UniProt/InterPro IEA). No IBA/ISO rows.
- Read full text of PMID:15064375 (cloning, E. coli rcsC complementation) and PMID:21778179
  (binding constants, ER localisation). PMID:25609827 full text read for pH/plant assay.
  PMID:32205456 (Hsf1) abstract only.
- Ontology checks (OLS / runoak):
  - GO:0009885 ancestors include GO:0004673, GO:0009784, GO:0009884, GO:0038023, GO:0016301,
    GO:0016740, GO:0016772 but NOT GO:0000155 phosphorelay sensor kinase activity. So 0000155
    is kept on its own (true, lateral).
  - GO:0009736 ancestors include GO:0007165, GO:0009735 but NOT GO:0000160.
  - GO:0044373 cytokinin binding is_a GO:0042562 hormone binding.
  - GO:0005789 ER membrane is under GO:0005783, GO:0012505 and GO:0016020.
- GO:0019955 cytokine binding (ARBA) is a cytokine/cytokinin confusion: removed, source defect.
- UniProt ARBA FUNCTION text "transmits the stress signal to a downstream MAPK cascade" is
  carried over from AHK1-type osmosensors; no evidence for ZmHK1. Recorded as source defect.
- Did not add NEW developmental process terms from Hsf1 (gain-of-function phenotype only;
  necessity/sufficiency evidence, not participation).
