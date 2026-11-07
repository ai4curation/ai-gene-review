# Source-qualified carnitine reaction capacity

This analysis assesses the exact three reactions in `modules/bacterial_l_carnitine_catabolism.yaml`, independently of review action counts. `evidence-fixture.yaml` is a finite, manually adjudicated source ledger. Its fourteen protein entries specify exact roles, evidence tiers, strain identity and source scope. The executable audit and frozen results are in `analysis/module_audits/bacterial_l_carnitine_catabolism/capacity/`.

The required chemistry is NAD-dependent L-carnitine oxidation, acetyl-CoA-dependent dehydrocarnitine cleavage, and betainyl-CoA hydrolysis. These substrate/product requirements are stricter than the GO acyltransferase or acyl-CoA hydrolase parents. Family membership is an additional compatibility requirement, never sufficient evidence of the substrate reaction. Uptake is a separately evaluated CaiX–CbcWV assembly profile and remains optional for enzyme capacity.

| Panel | Oxidation | Cleavage | Hydrolysis | Evidence boundary |
|---|---|---|---|---|
| PAO1 | Q9HTH8 CdhA | Q9HTH7 CdhC | Q9HTH9 CdhB | Exact primary-linked UniProt reactions plus native genetic context; not all isolated target assay details were available |
| KT2440 | Q88R32 LcdH | Q88R31 PP_0303 | Q88R33 PP_0301 | Conserved sequence/locus and specific ortholog chemistry; PP_0303 additionally has a direct substrate screen |
| S. meliloti 1021 | Q92NF5 BcoEF | Q92NF6 BcoG | Q92NF5 BcoEF | Complete sequence match to biochemically assayed 3D0a2 proteins; strain growth is not transferred |

For KT2440 PP_0303, Dataset2 of PMID24240508 maps Q88R31 to BKACE_511. Dataset4 contains dehydrocarnitine screening values and KAH values. These are target data, but the accepted positive-call cutoff and target-specific kinetic characterization were not recovered. The qualified assignment therefore combines the screen with independent comparative evidence. It neither pretends the target was unassayed nor treats each screen value as definitive specificity. PAO1 CdhC maps to BKACE_529, which is absent from that screen; the assayed Table6 proteins are different members.

PMID30670548 assays the intact BcoEF fusion and BcoG. The independently verified whole-protein matches support the same molecular capacities in the 1021 representatives. The same Q92NF5 witness supplies oxidation and hydrolysis, while Q92NF6 remains necessary for cleavage. No independent domain assay, channeling, or BcoG knockout is inferred. Its upstream carnitinyl-CoA hydrolysis activity lies outside this module boundary. Native 1021 growth on gamma-butyrobetaine can differ despite an identical locus; enzyme capacity does not predict that phenotype.

PMID19919675 supports CaiX-dependent transport with CbcWV. The Table5 reconstitution combines P. syringae B728a CaiX and PAO1 CbcWV in E. coli. The PAO1 import profile consequently contains an explicit ortholog-supported assembly step; KT2440 import remains a qualified inference. Neither is relabeled as an all-native purified complex assay. A CbcWV core without a carnitine-recognition partner cannot satisfy this uptake profile, although other substrate-binding partners can support other transport profiles.

The five family reviews are consulted for scope, and their consumed source closure is hashed. Unresolved family-wide substrate specificity does not invalidate supported exact members, and exact members do not confer the reaction on a whole family. No PAINT loss node, absent experimental activity, or generic fatty-acyl exclusion is inferred from alternative substrate use. The additive CdhB correction receipts explicitly preserve that distinction.

`alternative-route-scope.md` records the CntAB, Cai and hypothetical CJ25 boundary controls. Their failure here means that the available evidence does not establish this exact reaction profile. It is not a biological impossibility claim or a prediction of no carnitine metabolism.
