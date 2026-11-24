# ACYP1 notes

## GOA and family

- `ACYP1-goa.tsv` has 4 annotation rows, so the QuickGO fetch did not produce a header-only file.
- Human `ACYP1` and `ACYP2` are the only reviewed human members of `PTHR10029`.
- ACYP1 is `PTHR10029:SF21`; ACYP2 is `PTHR10029:SF20`.
- PAINT has one current `PTHR10029` IBD row, placing `GO:0003998` acylphosphatase activity at `PANTHER:PTN000003030`.
- `just paint-losses human ACYP1` found no IRD or IKR loss on the ACYP1 lineage.
- No production GO-CAM in `gocams/index.tsv` references `UniProtKB:P07311`, and the two human acylphosphatases are alternative monomeric enzymes rather than a multi-part biological module.

## Row calls

- The `GO:0003998` IBA, IEA and TAS rows were accepted. PMID:3026468 purified the human erythrocyte isozyme and reported hydrolysis of acyl phosphates; PMID:7796909 cloned the erythrocyte cDNA and expressed an active recombinant enzyme.
- `GO:0006796` was marked over-annotated. ACYP1 has acylphosphatase activity, but the legacy ProtInc TAS row to broad phosphate-containing compound metabolism does not name a concrete ACYP1 pathway.
