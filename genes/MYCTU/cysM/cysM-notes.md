# cysM: H37Rv enzyme chemistry

CysM is a PLP-dependent cysteine-biosynthetic enzyme of Mycobacterium tuberculosis H37Rv that preferentially uses O-phosphoserine and thiocarboxylated CysO. Sulfur transfer produces a covalent CysO-cysteine adduct, from which Mec+ releases free cysteine. Free sulfide can substitute inefficiently in vitro. Slow O-acetylserine intermediate formation does not establish that the ordinary OAS/free-sulfide reaction is an important native route.

PMID18842002: Full primary transient/single-turnover kinetics distinguish OPS/OAS first-half chemistry and CysO/free-sulfide reaction rates. Slow OAS aminoacrylate formation is not a complete free-cysteine endpoint.

PMID16104727: Full primary reconstitution shows CysO-adduct formation and Mec+-dependent cysteine release using OAS. This demonstrates an alternative carrier route; it does not establish OAS plus free-sulfide chemistry on CysM.

PMID18799456: Cache abstract-only; author-hosted full primary inspected. OAS/Na2S cysteine endpoint ND, whereas OPS/Na2S is active. GSH-prefixed Thr2Ala construct independently verified by 3DKI. Detection threshold not formalized. Exact result excerpt and limits are recorded in the local source analysis.

PMID18771296: Full primary CysM-CysO complex. 3DWG matches H37Rv P9WP53 plus RH. Early OAS-based pathway interpretation must be read alongside subsequent OPS-preference kinetics.

PMID19101553: Abstract reports C-terminal deletion effects on aminoacrylate protection and CysO specificity. Mutant behavior is not attributed to wild-type P9WP53.

Identity evidence is preserved in cysM-source-analysis/. All 12 original annotation payloads and raw source hashes are frozen in pristine-seed.json. No original source was edited. Falcon was genuinely attempted and failed HTTP403; these are manual research notes. PAINT loss query found no IRD/IKR loss record; inherited assertions are assessed against their node and target chemistry, not donor counts. No NEW process annotations were inferred from necessity or stress phenotypes.


## 2026-11-06 PR #6120 round-1 follow-up

Reassessed both GO:0004124 rows against projects/ENZYME_SPECIFICITY.md and changed UNDECIDED to MARK_AS_OVER_ANNOTATED. The decision concerns an unsupported functional assignment, not absence of every residual catalytic event. PMID18842002 measures OAS first-half intermediate formation; it does not establish weak complete OAS/free-sulfide turnover. The full primary PMID18799456 result remains [PMID:18799456, "unable to detect any cysteine as reaction product using OAS as substrate and sodium sulfide as sulfur donor"], with the previously recorded construct and detection-limit boundaries. Its discussion also judges the minor OAS behavior unlikely to matter metabolically. PMID17567578 independently characterizes the dedicated OAS enzyme CysK1. The preferred OPS/CysO reaction, demonstrated OPS/free-sulfide endpoint, and early OAS/CysO/Mec+ route remain distinct. No quantitative complete-reaction cutoff, proven evolutionary loss, or zero native turnover is asserted. Positive E. coli/PAO1 PAINT seed evidence is not invalidated.
