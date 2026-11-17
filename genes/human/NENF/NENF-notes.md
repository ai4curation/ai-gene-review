# NENF notes

## 2026-11-03 ORGANELLES batch 4 (mitochondrion rows)

- Rows: GO:0005739 IEA (GO_REF:0000120: ARBA, SL-0173, mouse Q9CQ45) and IDA (PMID:31536960); both ACCEPT -> KEEP_AS_NON_CORE.
- PMID:31536960 (full text) fractionates mt, ER and MAM with markers: [PMID:31536960 "showed an accumulation of NENF in the mt, endoplasmic reticulum (ER), and mitochondria-associated membrane (MAM) fractions"]; [PMID:31536960 "mt, ER, and MAM markers (ii) used as internal control"]. So the mitochondrial claim is ER-checked and holds.
- IEA: UniProt location [file:human/NENF/NENF-uniprot.txt "Mitochondrion {ECO:0000269|PubMed:31536960}"]; mouse Nenf mitochondrion rows are ISO from human (QuickGO, 2026-11-03), so a single experimental source.
- Why non-core: secreted neurotrophic factor (signal peptide 1-31); core_functions say extracellular region.
- MAM (GO:0044233) considered and not added: one study, and NENF is a soluble signal-peptide protein with no membrane anchor, so a membrane term does not fit its topology. Candidate if a second line (e.g. protease protection or membrane extraction) appears.

## 2026-11-05 ORGANELLES ER batch 3 (endoplasmic reticulum rows)

- Rows: GO:0005783 IBA (GO_REF:0000033), IEA (GO_REF:0000120), IDA (PMID:31536960); all ACCEPT -> KEEP_AS_NON_CORE, consistent with the mitochondrion rows (batch 4).
- IBA: PAINT node PTN000031653 (interpro/panther/PTHR10281/PTHR10281-paint.tsv) seeded by NENF itself (Q9UMX5), PGRMC2 (O15173) and MAPR members from mouse, rat, Arabidopsis, Aspergillus. NENF among its own seeds is expected.
- IEA: UniProt line [file:human/NENF/NENF-uniprot.txt "Endoplasmic reticulum {ECO:0000269|PubMed:31536960}"]; same single paper as the IDA.
- Evidence (full text): [PMID:31536960 "showed an accumulation of NENF in the mt, endoplasmic reticulum (ER), and mitochondria-associated membrane (MAM) fractions"]; [PMID:31536960 "mt, ER, and MAM markers (ii) used as internal control"]. Endogenous protein, marker-checked fraction.
- Why non-core: secreted neurotrophic factor, signal peptide 1-31 (ECO:0000255), no TM, C-terminus ...FDIKDEF has no KDEL-type retrieval motif. The ER pool is the biosynthetic route plus the proposed DJ-1/PINK1 heme-loading association; ADIPOQ precedent (endogenous protein in native cells) -> KEEP_AS_NON_CORE, not MARK_AS_OVER_ANNOTATED.
- No sub-compartment row: no evidence of lumenal residence or retention; one fractionation study cannot separate lumen from MAM.
- Not edited (outside brief scope, flag): the GO:0012505 endomembrane system IBA row's reason contains the 2026-11-03 mitochondrion ORGANELLES text (about GO_REF:0000120 and SL-0173), which belongs to the mitochondrion IEA row, not to an IBA endomembrane row.
  - Correction (2026-11-05): this flag was a false alarm. Checked on origin/main and on the batch 3 branch, the GO:0012505 IBA row's reason holds only its original endomembrane text; the GO_REF:0000120/SL-0173 text is on the GO:0005739 IEA row, where it belongs.
