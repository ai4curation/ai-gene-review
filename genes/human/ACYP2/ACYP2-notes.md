# ACYP2 notes

## GOA and family

- `ACYP2-goa.tsv` has 11 annotation rows, so the QuickGO fetch did not produce a header-only file.
- Human `ACYP1` and `ACYP2` are the only reviewed human members of `PTHR10029`.
- ACYP2 is `PTHR10029:SF20`; ACYP1 is `PTHR10029:SF21`.
- PAINT has one current `PTHR10029` IBD row, placing `GO:0003998` acylphosphatase activity at `PANTHER:PTN000003030`.
- `just paint-losses human ACYP2` found no IRD or IKR loss on the ACYP2 lineage.
- No production GO-CAM in `gocams/index.tsv` references `UniProtKB:P14621`, and the two human acylphosphatases are alternative monomeric enzymes rather than a multi-part biological module.

## Row calls

- The `GO:0003998` rows were accepted. PMID:8268218 synthesized and expressed the human muscle acylphosphatase gene and assayed benzoylphosphate hydrolysis by the recombinant enzymes.
- PMID:1645713 describes acylphosphatase purified from human erythrocytes in the cached abstract, so it was not treated as ACYP2-specific direct evidence from the abstract alone.
- The PMID:25416956 `GO:0005515` rows were removed under the root-protein-binding policy without disputing the high-throughput Y2H interactions with SULT2B1 or CREBZF.
- The two `GO:0042802` rows from PMID:12374855 and PMID:16084386 were marked over-annotated. Those papers deliberately use human muscle acylphosphatase as an amyloid-aggregation model for mutant proteins and do not show native ACYP2 homodimerization as a function.
- The high-throughput `GO:0005739` mitochondrion row from MitoCoP was kept as non-core under the root-organelle policy.
- `GO:0006796` was marked over-annotated. ACYP2 has acylphosphatase activity, but the legacy ProtInc TAS row to broad phosphate-containing compound metabolism does not name a concrete ACYP2 pathway.
