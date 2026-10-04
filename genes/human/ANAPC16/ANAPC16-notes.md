# ANAPC16 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC16 (C10orf104, CENP-27) is a metazoan-specific, constitutive APC/C subunit needed for activity toward mitotic substrates (PMID:20392738).
- **Structure:** in the Arc Lamp/TPR lobe, one APC16 binds the APC3 dimer and recruits APC7 (PMID:25490258).
- **Worm ortholog:** emb-1 mutants arrest at meiosis I metaphase, like other APC/C subunits (PMID:21775471). This supports accepting the meiotic-regulation NAS.
- **Kinetochore (IDA PMID:20813266, plus IBA):** as CENP-27, APC16 localizes to the outer kinetochore in a chromosome proteomics/GFP screen. Kept as non-core, since this is the mitotic kinetochore pool of the APC/C.
- **Protein binding IPI with HSF2BP (HuRI):** removed.
- **Other rows:** all location, complex, catabolism and chain-type rows are accepted. Unlike APC15, APC16 is needed for substrate ubiquitination, so the complex-level chain-type IDAs are accepted.

## 2026-10-04 round 2 (reviewer comments on #4058)

- **Core MF:** GO:0140378 protein complex scaffold activity ("serves to hold the complex together"), backed by PMID:25490258 (APC16 binds the APC3 dimer and recruits APC7). contributes_to GO:0061630 is kept alongside it.
  - Rejected GO:0160072 ubiquitin ligase complex scaffold activity. Its definition is bridging a ligase and a substrate adaptor; human users are cullins, SKP1 and DDB1.
  - Rejected GO:0030674. Its own comment says complex scaffolds should use GO:0140378.
- **No NEW MF row, after a comparator check.** In QuickGO, human GO:0140378 annotations are scaffold proteins (KSR1, IQGAP1, SKP1, CUL1/2, MAP2K1/2, MAPK8IPs). No small APC/C subunit (CDC26, ANAPC13, ANAPC15) carries it or any adaptor/structural MF. I read that systematic absence as a convention: APC/C subunits get contributes_to ligase activity. So the scaffold MF is stated only in core_functions, not proposed as a GOA addition.
- **Other fixes:**
  - The kinetochore IBA (is_active_in) and IDA (located_in) now have distinct reasons.
  - core_functions now lists cytosol and nucleoplasm.
  - The PMID:29033132 rows note that the quote is a general statement.
  - The seed PMIDs now have reference_review entries.
