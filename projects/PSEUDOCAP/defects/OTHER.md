# Source-record defects for OTHER

5 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTH6 enables GO:0015226 carnitine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTH6/Q9HTH6-ai-review.yaml`

CaiX is the periplasmic substrate-binding protein of an ABC importer and cannot translocate carnitine without the CbcW permease and CbcV ATPase; contributes_to is the GO relation for a subunit carrying part of a complex activity.

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

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q06749 enables GO:0004794 threonine deaminase activity (IDA, PMID:8370530)
- **Field:** GO_ID
- **Change:** GO:0004794 → GO:0045135
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/algL/algL-ai-review.yaml`

The PseudoCAP IDA row for AlgL (Q06749) from PMID:8370530 uses GO:0004794 threonine deaminase activity, but the paper's abstract describes only an alginate lyase assay on purified AlgL. The activity measured corresponds to GO:0045135 poly(beta-D-mannuronate) lyase activity. Please repoint the row; the full text was not available to confirm that no separate deaminase assay was performed.

> The purified protein was shown to have alginate lyase activity.
> — PMID:8370530

## 4. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q03456 involved_in GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325)
- **Change:** GO:0019290 → GO:1900705 (negative regulation of siderophore biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

CACAO annotation of GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325) to P. aeruginosa Fur (Q03456). Fur mutants constitutively produce siderophores, showing that Fur represses the pathway, not that it performs biosynthesis. Repoint to GO:1900705.

> These manganese-resistant Fur mutants constitutively produce siderophores and exotoxin A when grown in concentrations of iron that normally repress their production.
> — PMID:8478325

## 5. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR028359
- **Subject:** UniProtKB:G3XD94
- **Change:** GO:0016628 → GO:0016616 (oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

InterPro2GO: IPR028359 (UDP-ManNAc/GlcNAc dehydrogenase) maps to GO:0016628 (CH-CH group of donors). Family members (WbpA EC 1.1.1.136, WecC EC 1.1.1.336) oxidise the C6 hydroxymethyl group of the sugar, a CH-OH donor. The mapping should be GO:0016616.
