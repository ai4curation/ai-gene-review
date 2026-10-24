# Computed provenance: GO:0035615 family carry-over across AP mu subunits

QuickGO annotation API queried this run for GO:0035615 (clathrin-cargo adaptor activity)
on each human AP-complex medium (mu) subunit. Result:

| Subunit | UniProt | # annotations to GO:0035615 | Evidence codes |
|---------|---------|-----------------------------|----------------|
| AP1M1 | Q9BXS5 | 1 | IBA (ECO:0000318) |
| AP2M1 | Q96CW1 | 3 | **IDA (ECO:0000314) + TAS (ECO:0000304)** + IBA |
| AP3M1 | Q9Y2T2 | 1 | IBA (ECO:0000318) |
| **AP3M2** | **P53677** | 1 | **IBA only** (ECO:0000318) |
| AP4M1 | O00189 | 1 | IBA (ECO:0000318) |

## Interpretation
- The ONLY experimentally supported assignment of GO:0035615 is to **AP2M1**, the genuine
  clathrin-mediated-endocytosis adaptor.
- AP1M1, AP3M1, **AP3M2**, and AP4M1 carry the term **by IBA (phylogenetic) inference only**.
- **AP-4 is an established clathrin-INDEPENDENT complex** (PMID 22022230; PMID 15377281), yet AP4M1
  still carries GO:0035615 by IBA. This proves the term is propagated across PANTHER family PTHR10529
  regardless of actual clathrin dependence.
- Conclusion: the AP3M2 GO:0035615 annotation is family carry-over anchored in AP-2, not AP-3-specific
  evidence — supporting a curation lead to generalize/replace it with a cargo/sorting-signal-recognition MF.
