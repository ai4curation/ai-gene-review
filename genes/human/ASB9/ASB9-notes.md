# ASB9 notes

- Substrates: CKB (PMID:17148442), mitochondrial CK (PMID:20302626), TNP2 in testis [PMID:41915740 "Mechanistically, we found that ASB9 assembles a testis-specific Cullin-RING ligase (CRL) complex-TNP2-ASB9-ELOB/C-CUL5-RBX1-that mediates the ubiquitin-dependent degradation of TNP2 to facilitate the histone-to-protamine transition during spermiogenesis."], and free histones H3/H4 in vitro (PMID:41260500).
- NEW GO:0035092 sperm DNA condensation (IMP; human patient and mouse KO). GO:0035093 (exchange of chromosomal proteins) is obsolete with term_replaced_by GO:0035092 (checked in OLS4, 2026-10-05), so the more specific exchange term is unavailable. Comparators: a QuickGO query of GO:0035093/GO:0035092 annotations (human and mouse, 2026-10-05) returned RNF8 (IMP, mouse) and PSME4 (IMP, mouse) among the chromatin-protein-clearing machinery.
- The 41 protein-binding IPIs are removed. Creatine kinases (CKB, CKM, CKMT1B, HEL-S-29) and ELOC are captured by the adaptor/complex rows.
- PMID:40501794 is the preprint of PMID:41260500; only the latter is cited.
- HIF1AN is the most-replicated ASB9 interactor after CKB. PMID:36683111 (cached) shows co-IP and functional rescue in human SSCs, but not ubiquitination by ASB9. Recorded as a candidate substrate and a question, not as a substrate.
- Nucleus: NEW ISO from mouse spermatid immunostaining (PMID:41915740).

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- GO:0005739 rows: EXP (PMID:20302626) ACCEPT, unchanged; IEA (GO_REF:0000044, SL-0173) ACCEPT, reason rewritten to record the mapping check (UniProt location carries ECO:0000269 from PMID:20302626).
- The study resolves only the organelle: overexpressed ASB9 colocalizing with uMtCK [PMID:20302626 "ASB9 and ASB9DeltaSOCS can interact and colocalise with uMtCK in the mitochondria."], and a crude mitochondrial pellet [PMID:20302626 "the supernatants were then centrifuged at 10,000 g for 20 min at 4°C to separate the mitochondrial (pellets) and the cytosolic fraction (supernatants)."]
- No sub-compartment: no transit peptide or TM; the only hint is the substrate uMtCK, which works between the membranes at contact sites [PMID:20302626 "MtCK proteins form an active octameric complex with an internal channel that stabilises the contact site between the outer membrane and the inner membrane"]. How a cytosolic Cul5 substrate receptor reaches an IMS enzyme is an open question; outer-membrane association would be the obvious guess but has not been shown. Stayed at the root.
