# Psn (Presenilin; UniProt O02194) notes

Fetched with `just fetch-gene DROME O02194 --alias Psn`. FlyBase FBgn0284421.
PANTHER PTHR10202 (PRESENILIN) / PTHR10202:SF13 (PRESENILIN HOMOLOG).

## Deep research
Falcon deep research completed (`Psn-deep-research-falcon.md`, 39 citations),
although the wrapper reported a timeout (file written after 754 s).

## Key findings
- Psn null abolishes Notch signal transduction and NICD nuclear entry
  [PMID:10206646 "null mutations in the Drosophila Presenilin gene abolish Notch signal transduction and prevent its intracellular domain from entering the nucleus."]
- Required for membrane-tethered activated Notch (N-ECN) [PMID:11134525]
- Substrate choice governed by ectodomain size [PMID:11030342]
- Complex with Nct, Aph-1, Pen-2; Pen-2 needed for endoproteolysis [PMID:12660785]
- In vivo reconstitution; preference for Notch over some APP-family substrates [PMID:20421416]
- Sanpodo binds Psn (aa 100-125) to promote Notch activation in pIIa [PMID:23609534]
- Calcium: loss of Psn associated with elevated cytosolic calcium (deep research citing Kang 2017).
- Possible gamma-secretase-independent role in Debcl-mediated cell death (deep research).

## Review decisions
- Core MF GO:0042500 aspartic endopeptidase activity, intramembrane cleaving; in complex GO:0070765.
- endopeptidase activity (IBA + experimental) MODIFIED to GO:0042500.
- amyloid-beta formation, ectodomain proteolysis, protein processing, calcium homeostasis, apoptotic process kept non-core.
- protein binding (Sanpodo) REMOVED as uninformative (interaction itself not disputed).

## PAINT nodes (GOA WITH/FROM)
- PTN000024429: GO:0004175, GO:0006509, GO:0070765
- PTN000024430: GO:0007219, GO:0055074, GO:0016485, GO:0034205
