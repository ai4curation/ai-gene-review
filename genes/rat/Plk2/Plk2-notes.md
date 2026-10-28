# Plk2 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Plk2` resolved Q9R012 (PLK2_RAT, Swiss-Prot; RGD:620760; GeneID 83722). 83 GOA rows.
- Full text read: PMID:18723513, PMID:20802490, PMID:21382555, PMID:23983262, PMID:27908889.
  Abstract only: PMID:10523297, PMID:14576440, PMID:18498738, and the human/mouse donor papers.
- See `Plk2-deep-research-manual.md` for the literature summary with provenance.

### Key decisions

- Core: Ser/Thr kinase acting at the postsynapse in homeostatic synaptic downscaling (phosphorylates
  SPAR, RasGRF1, SynGAP, PDZGEF1) [PMID:21382555 "CA Plk2, but not KD Plk2, robustly phosphorylated each of
  these Ras/Rap regulators in this defined system"], plus a kinase-independent NSF-binding function that
  removes surface GluA2 [PMID:20802490 "Plk2 engagement of NSF, but not Plk2 kinase activity, was required
  for this mechanism"]. Centriole duplication (human evidence) kept as a non-neuronal core function.
- `regulation of synaptic plasticity` rows MODIFIED to `regulation of synaptic scaling` (GO:0150092, is_a
  GO:0048167, checked with OAK).
- RGD IPI rows from PMID:20802490: RGD ids resolved via RGD REST: 2064=Ap1b1, 71015=Ap2a2, 2364=Cltc,
  2513=Dnm2, 620416=Dnm1l, 727949=Dnm3, 621594=Nsf, 708497=Sipa1l1.
  - `protein kinase binding` with adaptins: adaptins are not kinases -> wrong term (source defect).
  - `GTPase binding` with dynamins: the paper reports dynamin bound GST and GST-Plk2c equally -> REMOVE.
  - `clathrin heavy chain binding`: only in supplementary mass-spec table, not inspected -> UNDECIDED.
- LTP/LTD IDA rows from PMID:21382555: the paper mentions LTP/LTD only as background on Ras/Rap -> over-annotation.
- Postsynapse IEP/IMP rows: wrong evidence code for a location; kept with the IDA row, WRONG_EVIDENCE_CODE CHECK.
- Kinetochore, spindle pole, nucleus IBA rows rest on PLK1/Polo-type donors; no Plk2 evidence -> MARK_AS_OVER_ANNOTATED.
- Mouse miRNA-target and knockdown phenotype rows (angiogenesis, senescence, bone marrow apoptosis) -> over-annotated.
