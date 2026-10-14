# ANAPC15 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC15 (yeast Mnd2) is the APC/C subunit that silences the spindle assembly checkpoint (SAC). It drives CDC20 autoubiquitylation within the APC/C-bound MCC, which turns the MCC over [PMID:21926987, PMID:23007861].
  - It is "dispensable for substrate ubiquitylation by APC/C(CDC20) and APC/C(CDH1)" (PMID:23007861).
  - The role is conserved: yeast Mnd2 is required for SAC-dependent Cdc20 autoubiquitination and for timely release from the arrest (PMID:22940250).
- **GO:0090266 regulation of mitotic SAC (IBA, IEA, IMP):** all three rows MODIFY to GO:0140499 "negative regulation of mitotic spindle assembly checkpoint signaling".
  - Verified with OLS that GO:0140499 is_a GO:0090266.
  - Comparator: MAD2L1BP/p31comet carries GO:0140499 by IMP.
  - Caveat: the OLS definition of GO:0140499 reads "reduces ... negative regulation of mitotic spindle assembly checkpoint signaling". That looks like a GO definition error (a double negative); the label and parentage are correct.
- **Chain-type IDA rows (K11, K48, branched; PMID:29033132):** KEEP_AS_NON_CORE. These are complex-level, and APC15 is dispensable for substrate ubiquitylation.
- **Meiotic NAS:** accepted. APC15 siRNA arrests mouse oocytes at MI with a SAC-silencing defect (PMID:40153087).
- **Protein binding (CEP19, HuRI):** removed.
- **Other rows:** 36 Reactome location rows accepted.
