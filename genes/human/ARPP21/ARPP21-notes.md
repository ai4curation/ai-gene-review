# ARPP21 review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:29581509 (full text): iCLIP shows ARPP21 binds U-rich 3' UTR sequences. It opposes miR-128 via eIF4F and promotes dendritic branching in mouse cortical neurons. Tagged mouse proteins were expressed in HEK-293T cells.
  - PMID:38467629 (full text): direct R3H-domain RNA binding in mouse thymocytes.
- Mouse Arpp21 (Q9DCB4) donor rows (QuickGO) include IDA cytoplasm (PMID:29581509) and IDA mRNA 3'-UTR binding (PMID:38467629).

## Decisions
- ACCEPT: cytoplasm (IBA, IEA).
- MODIFY: nucleic acid binding (InterPro R3H IEA) → mRNA 3'-UTR binding.
- NEW: positive regulation of dendrite morphogenesis (ISO from mouse, PMID:29581509).

## 2026-10-04 review round (PR #4206)

- QuickGO (2026-10-04): mouse Arpp21 (Q9DCB4) has no GO:0050775 row from MGI. Its MGI rows are 3-UTR binding, cytoplasm and thymocyte processes (PMID:38467629). The dendrite ISO rests directly on the PMID:29581509 mouse IUE experiments.
- Added GO:0045727 [PMID:29581509 "ARPP21 activity in the tethering assay is reduced after eIF4G knockdown."].
