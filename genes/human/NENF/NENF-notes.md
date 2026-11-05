# NENF notes

## 2026-11-03 ORGANELLES batch 4 (mitochondrion rows)

- Rows: GO:0005739 IEA (GO_REF:0000120: ARBA, SL-0173, mouse Q9CQ45) and IDA (PMID:31536960); both ACCEPT -> KEEP_AS_NON_CORE.
- PMID:31536960 (full text) fractionates mt, ER and MAM with markers: [PMID:31536960 "showed an accumulation of NENF in the mt, endoplasmic reticulum (ER), and mitochondria-associated membrane (MAM) fractions"]; [PMID:31536960 "mt, ER, and MAM markers (ii) used as internal control"]. So the mitochondrial claim is ER-checked and holds.
- IEA: UniProt location [file:human/NENF/NENF-uniprot.txt "Mitochondrion {ECO:0000269|PubMed:31536960}"]; mouse Nenf mitochondrion rows are ISO from human (QuickGO, 2026-11-03), so a single experimental source.
- Why non-core: secreted neurotrophic factor (signal peptide 1-31); core_functions say extracellular region.
- MAM (GO:0044233) considered and not added: one study, and NENF is a soluble signal-peptide protein with no membrane anchor, so a membrane term does not fit its topology. Candidate if a second line (e.g. protease protection or membrane extraction) appears.
