# OCA6 (Q12454) GO decision table

All rows are leads requiring curator verification.

| GO ID | Label | Aspect | Current state on Q12454 | Lead action | Basis | Strength |
|---|---|---|---|---|---|---|
| GO:0016791 | phosphatase activity | MF | IBA, GO_REF:0000033, GO_Central, with/from AT1G05000, AT2G32960, AT3G02800, AT5G16480, SIW14 (S000005043), I6WXK4, Q4QBX1, Q6K461, Q9HXC7 | **Remove or mark as over-annotated (NOT qualifier)** | Invariant arginine absent (Ile120 at the Siw14 Arg220 column), 0/64 Oca6-clade orthologues retain it, no CX5R anywhere in the sequence, no cation within 7.54 A of Cys114 SG, no assay ever performed on Oca6 | Strong |
| GO:0004725 | protein tyrosine phosphatase activity | MF | IEA, GO_REF:0000120 (UniProt family rule, EC 3.1.3.48) | **Remove**; flag the UniProt rule for review | Same evidence, and this term is more specific than GO:0016791 so it is less defensible | Strong |
| GO:0003674 | molecular_function | MF | ND, SGD, GO_REF:0000015 | Retain ND until a direct assay exists, or replace with a non-catalytic MF term if one is supported | SGD already declines to assign an MF | Lead |
| GO:0005737 | cytoplasm | CC | IEA (GO_REF:0000044) and HDA (PMID:14562095) | **Retain** | GFP-fusion localization collection | Strong |
| GO:0032991 | protein-containing complex | CC | absent | **Candidate addition**, IPI evidence from PMID:37968396 and PMID:16429126 | Oca6 co-purifies with Oca1, Oca2, Oca4, Oca5 and Siw14; OCA4 MI score 0.70 across five methods | Lead, needs curator verification |
| GO:0019903 | protein phosphatase binding | MF | absent | **Candidate addition**, IPI with SIW14 (PMID:37968396) | Anti-tag coIP with Siw14, the one catalytically active member of the group. More informative than bare protein binding | Lead, weaker. One high-throughput method; a targeted coIP or reconstitution would be needed |
| GO:0071474 / GO:0006950 | cellular hyperosmotic response / response to stress | BP | absent (BP is ND) | **Candidate lead only** | PMID:21409566 reports oca6 deletion strains sensitive to caffeine and rapamycin, suppressed by SIW14 overexpression. No GO term matches caffeine or rapamycin response cleanly and the phenotype is a loss-of-function readout | Weak lead |

## Terms deliberately not recommended

- GO:0005515 protein binding as a terminal recommendation. The interaction data supports a more informative term (GO:0032991, and possibly GO:0019903), so bare protein binding would lose information.
- GO:0052745 / inositol phosphate phosphatase terms. Siw14 is a 5-InsP7 beta-phosphatase, but no inositol pyrophosphate measurement has been made in an oca6 deletion strain, so there is nothing to transfer.
- A pseudophosphatase-specific MF term. GO has no term for catalytically dead phosphatase scaffolds, which is why the practical action here is removal plus a CC and interaction-based addition.
