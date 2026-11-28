# ACVR1 manual PTHR23255 review notes

Provider deep-research calls for this batch failed before producing a provider report, so this file records manual source review of cached primary papers, Reactome records, UniProt function text and the PTHR23255 PAINT table. The seeded GOA rows were reviewed one row at a time from `ACVR1-ai-review.yaml`; rows that differ only by PMID, Reactome event, GO_REF, evidence code or WITH/FROM partner were deliberately left as separate entries.

## Mechanistic boundary

PTHR23255 contains BMP, activin/nodal, AMH and TGF-beta receptor branches. The shared family-level assertion is a single-pass serine/threonine receptor kinase that acts in a ligand/type-I/type-II receptor complex at the plasma membrane. Ligand names were adjudicated at subfamily level: ACVR1/ALK2 and BMPR1B/ALK6 were treated as BMP-family receptors; ACVR1C/ALK7 as a nodal/activin type-I receptor; TGFBR1/ALK5 and TGFBR2 as the canonical type-I and type-II TGF-beta receptors.

## Source notes

- PAINT node PTN002758232 supports the broadly conserved plasma-membrane assertion across the family, while PTN000583675 supports broad signaling-receptor complex and receptor serine/threonine kinase assertions.
- The ACVR1C lineage has one PAINT IRD: PTN002758343 blocks GO:0048185 activin binding from PTN000583887 as of 2024-11-20. The current human ACVR1C seed has no GO:0048185 row, so the loss was recorded here and no exception row was needed.
- Bare GO:0005515 rows were removed under the project protein-binding policy. This is a removal of an uninformative generic term, not a rejection of every underlying interaction.
- Mouse ISS/IEA developmental transfers were left UNDECIDED where the exact donor experiment was outside the cached human primary-paper set.

## Primary papers used most heavily

- PMID:9748228 separated ACVR1/ALK2 BMP7-SMAD1/5 signaling from activin-ALK4 signaling.
- PMID:18436533 measured BMP2/4 and BMP6/7 receptor usage in primary human mesenchymal stem cells.
- PMID:15150278, PMID:15531507 and PMID:21356369 support Nodal/ALK7 signaling in human trophoblast or ovarian-cell proliferation, apoptosis and migration contexts.
- PMID:19229295 and PMID:24098149 support GDF5/BMPR1B binding and signaling specificity.
- PMID:1333888, PMID:7852346, PMID:9311995, PMID:12015308, PMID:15761148 and PMID:25893292 support TGFBR1/TGFBR2 complex assembly, ligand binding, SMAD coupling, endoglin association, tight-junction signaling and membrane-raft regulation.

## ACVR1-specific calls

- PMID:9748228 separated ALK2 BMP7-SMAD1/5 signaling from activin-ALK4 signaling; ACVR1 activin/TGF-beta ligand-binding and activin receptor-complex rows were therefore removed or left unresolved rather than carried forward from old activin-receptor nomenclature.
- PMID:18436533 supports ACVR1A as the preferred type-I receptor for BMP6/7 signaling in primary human mesenchymal stem cells, including osteoblastic differentiation outputs.
- The cached PMID:19506109 abstract verifies defective ALK2 L343P kinase/BMP reporter activity and abnormal atrioventricular canal formation, but did not by itself verify the more specific mitral-valve, endocardial-cushion, septum, or dorsal-identity rows; those were left `UNDECIDED`.
