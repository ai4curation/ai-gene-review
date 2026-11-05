# pmrB (PA4777, Q9HV31) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HV31 --alias pmrB`; accession matches the worklist. No
deep-research provider used. PMID:14507375 is abstract-only (no PMC record).

### Literature

- [PMID:14507375 "We have identified a second two-component regulatory system, PmrA-PmrB, that regulates resistance to polymyxin B and cationic antimicrobial peptides."]
- [PMID:14507375 "Inactivation of the pmrB sensor kinase and pmrA response regulator greatly decreased the expression of the operon encoding pmrA-pmrB"]
- UniProt: two TM helices, HAMP, HisKA (His249 phosphohistidine), HATPase. No receiver or HPt domain.
  pmrB carries no GO:0009927 histidine phosphotransfer kinase row, so the HPt problem recorded on
  PA1611 and pfeS does not arise here.

### Annotation decisions

- ACCEPT: GO:0000155 (IEA), GO:0000160 (IBA, IDA seed, IEA), GO:0005886 (IBA).
- TOO_GENERAL: GO:0004673 (IEA, ISS), GO:0016772, GO:0007165, GO:0016020.
- PSEUDOCAP WRONG_EVIDENCE_CODE (CHECK, SUSPECTED) on the IDA GO:0000160 row, as for pfeS.
- Action counts: ACCEPT 5, TOO_GENERAL 5.

## PseudoCAP IBA-seed assessment

PTN001976770 is not shared with the reviewed sensor kinases (parS, PA5484, pprA, fleS, cbrA, PA1611,
PA3271, pfeS); no node term in it is GO:0009927.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001976770 | GO:0000160 phosphorelay signal transduction system | 3 | 71 (24 taxa) | GO:0000160, IDA, PMID:14507375 (PseudoCAP) | UNVERIFIABLE | Abstract only; it reports mutants and reporter fusions, no PmrB assay. The term is true of PmrB, but whether IDA-type evidence exists could not be checked. | E. coli PhoQ P23837, O69729 | Yes; the term suits a sensor-kinase clade |
