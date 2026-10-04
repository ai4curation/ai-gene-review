# ANKMY2 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKMY2 (Q8IV38) binds membrane adenylyl cyclases (and the guanylyl cyclase GC1) and is required for their maturation and trafficking to primary cilia (PMID:32702291).
  - Knockout mice have Smoothened-independent Hedgehog hyperactivation, open neural tubes, and die mid-gestation.
  - Loss of ANKMY2 suppresses cysts in Pkd1 kidney models.
  - Knockdown in **human** kidney cells lowers ciliary ADCY3 (PMID:41474822; its erratum only fixes an S1 Data upload).
  - The worm ortholog DAF-25 localizes the guanylyl cyclase DAF-11 to cilia (PMID:21124868).
- **Cilium IEA → MODIFY to cytosol.** UniProt's cilium location is ECO:0000250, by similarity to the worm. Mammalian ANKMY2 is "predominantly cytosolic ... not enriched in cilia", and endogenous Ankmy2 fractionates with the cytosol.
- **Enzyme binding IEA** (from mouse Ankmy2-GC1): accepted. Adenylate cyclase binding (GO:0008179, a child term) is used as the core MF rather than a NEW row, to avoid an ancestor-descendant duplicate. The validator warns that the core term is not in existing_annotations; that is intended.
- **NEW GO:0097499** protein localization to non-motile cilium (IMP, PMID:41474822, human cells). Comparator: worm daf-25 carries GO:0097499 by IMP.
- **TINF2 protein-binding IPI:** removed.
- **PAINT finding:** PTHR24150 has **0 PTN nodes** (`just fetch-panther-paint`), yet worm daf-25 has a dozen experimental annotations and mouse Ankmy2 has an IPI. So ANKMY2's missing IBA reflects an uncurated family, not absent donors, which makes this family a candidate for PAINT curation. Family files committed.
