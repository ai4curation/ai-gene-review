# ACP5 notes

## 2026-11-28

- Seeded human ACP5 from UniProt/QuickGO; `ACP5-goa.tsv` contains 14 rows, so the review is not a header-only failed fetch.
- ACP5 is the only reviewed human member of PTHR10161 in the InterPro/PANTHER reviewed-member slice (`P13686` in `PTHR10161:SF14`).
- No production GO-CAM activity currently names ACP5 in `gocams/index.tsv`, and this family is a set of single-chain purple acid phosphatases rather than a multi-step biological module.
- `just paint-losses human ACP5` reported no IRD or IKR on the human ACP5 lineage.
- PTN004128707 carries the family acid phosphatase and Fe-binding IBD rows that descend to human ACP5.
- Bone resorption is correct for vertebrate ACP5 but not for the whole PTN000017834 node. The PANTHER 19.0 tree cache resolves `PTN000017834` as a 29-leaf node that includes vertebrate ACP5 leaves plus four `Ciona intestinalis` leaves, `Branchiostoma floridae LOC118405250`, and two `Strongylocentrotus purpuratus` leaves. Its descendant `PTN002563058` is the 22-leaf vertebrate ACP5 node: human, other eutherian and metatherian/monotreme mammals, sauropsids, amphibians, gar, zebrafish, and medaka.
