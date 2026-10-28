# Source-record defects for OTHER

5 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4V0 enables GO:0018580 nitronate monooxygenase activity (IEA, GO_REF:0000002)
- **Field:** GO_ID
- **Change:** check GO:0018580 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1024/PA1024-ai-review.yaml`

The InterPro2GO mapping IPR004136 (NMO) -> GO:0018580 nitronate monooxygenase activity (resource InterPro / InterPro2GO) puts NMO activity on PA1024 (Q9I4V0). Ball et al. 2016 (PMID:27502282) showed that the purified enzyme lacks NMO activity and is an NADH:quinone reductase. The authors report that this NQR class covers more than 490 sequences in the NMO family. Restrict the mapping, for example by moving it to a subfamily-level entry for true NMOs, or by suppressing it for PA1024-like sequences. A NOT annotation to GO:0018580 on Q9I4V0, citing PMID:27502282, would also be justified.

> which define a new class of NADH:quinone reductases and are present in more than 490 hypothetical proteins in the GenBank
> — PMID:27502282

## 2. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HY69 enables GO:0004467 long-chain fatty acid-CoA ligase activity (IDA, PMID:16797016)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004467
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/alg44/alg44-ai-review.yaml`

The PseudoCAP IDA annotation assigns long-chain fatty acid-CoA ligase activity to Alg44 (Q9HY69) using PMID:16797016. The complete original article, reproduced as Chapter III of Uwe Remminghorst's 2007 thesis (printed pp.58-69; PDF pp.71-82; https://mro.massey.ac.nz/bitstreams/55746141-71a5-48b8-b1b2-8abf9db2eb49/download), reports alginate production, topology, morphology and protein identification, not ATP/CoA-dependent fatty-acid activation. Delete this unsupported activity row; a replacement assay/gene is not established. The unexpected PseudoCAP threonine-deaminase row on AlgL is a separate suspected defect, not proof of a shared mapping cause.

- **Evidence reference:** PMID:16797016

> These studies suggest that Alg44 may act as a co-polymerase in concert with Alg8, the major GT
> — PMID:18524915

## 3. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q06749 enables GO:0004794 threonine deaminase activity (IDA, PMID:8370530)
- **Field:** GO_ID
- **Change:** check GO:0004794 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/algL/algL-ai-review.yaml`

Please check the PseudoCAP IDA threonine deaminase annotation on AlgL (Q06749) against the complete PMID:8370530 paper. Only the abstract was accessible here; it describes alginate lyase sequence/purification, so the unexpected deaminase assertion is suspicious but cannot be rejected from absence in the abstract. Check the original assay and term mapping; retain the row if a target-specific deaminase assay is present, otherwise correct or remove it. No corrected value is asserted because the intended source assertion is unknown.

- **Evidence reference:** PMID:8370530

## 4. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** InterPro:IPR003481
- **Subject:** UniProtKB:Q9K3C5
- **Change:** check GO:0009424 (alternatives in the explanation)
- **Likely cause:** LEGACY_ALIAS
- **Recorded in:** `genes/PSEAE/fliD/fliD-ai-review.yaml`

InterPro2GO (resource: InterPro; GO_REF:0000002) maps IPR003481 (FliD_N, the N-terminal domain of the flagellar cap protein FliD) to GO:0009424 bacterial-type flagellum hook. FliD forms the cap at the distal tip of the filament; the hook-filament junction proteins are FlgK (HAP1) and FlgL (HAP3), and GO:0009424 is defined as the portion of the flagellum connecting filament to basal body. The legacy name "hook-associated protein 2" is the likely source of the mapping, which appears on every FliD entry (for example P24216, P16328, P39738, Q9K3C5). Please review and either retire the mapping or point it at GO:0009421, which IPR040026 already maps to. (FliD has been observed at the distal end of the hook-basal body in filament-less Salmonella mutants, which is why this is raised as a query rather than a straight deletion.)

> A FliD (also called HAP2) oligomer forms the cap protein complex that is located at the tip of the flagellar filament (Yonekura et al.
> — PMID:27664419

## 5. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q03456 involved_in GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325)
- **Change:** GO:0019290 → GO:1900705 (negative regulation of siderophore biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

CACAO annotation of GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325) to P. aeruginosa Fur (Q03456). Fur mutants constitutively produce siderophores, showing that Fur represses the pathway, not that it performs biosynthesis. Repoint to GO:1900705.

> These manganese-resistant Fur mutants constitutively produce siderophores and exotoxin A when grown in concentrations of iron that normally repress their production.
> — PMID:8478325
