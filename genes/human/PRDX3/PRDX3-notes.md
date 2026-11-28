# PRDX3 notes

## 2026-11-28 PTHR10681 human family review

Automated Falcon deep research was attempted only on the first gene in the family and failed because
the local deep-research client had no non-Claude provider available. No extra sub-workers were allowed
for this campaign, so this review used manual literature triage from the seeded GOA references, the
UniProt record, Reactome records, and the existing PTHR10681 family review.

Key evidence:

- PMID:17707404 reconstituted the mammalian mitochondrial PRDX3 antioxidant pathway from purified
  components and showed that PRDX3 functions as a thioredoxin-dependent peroxidase with Trx2 and
  thioredoxin reductase 2.
- PMID:19462976 assayed human PRDX3 directly, found rapid H2O2 reactivity, and places the enzyme in
  the mitochondrial matrix.
- Reactome:R-HSA-3322995 places the PRDX3/PRDX5 H2O2-reduction event in the mitochondrial matrix.
- PMID:12492477, PMID:15750338, PMID:18205602, and PMID:21850687 support peripheral interactions
  with MAP3K13/LZK, RPS6KC1/RPK118, TNNI3K, and LRRK2, respectively.
- PMID:12011429 and PMID:18262354 establish mitochondrial phenotypes after PRDX3 perturbation, but
  do not make PRDX3 a direct mitochondrial organizing factor or caspase inhibitor.
- PMID:17893648 supports H2O2-specific PRDX3 induction in human lens epithelial cells and rat lenses.

Decisions:

- The core retained function is mitochondrial-matrix thioredoxin-dependent peroxiredoxin activity in
  hydrogen peroxide catabolism and cell redox homeostasis.
- The root mitochondrion rows are retained beside the more specific mitochondrial-matrix Reactome row
  under the organelle policy.
- Cytosolic and early-endosome rows are peripheral and linked to kinase-binding contexts rather than
  the core mitochondrial peroxide-detoxification function.
- Cellular ROS and H2O2 response terms from perturbation or induction studies are kept as non-core
  PRDX3 phenotypes rather than treated as the direct catalytic function.
- Generic `GO:0005515` rows are removed unless the row names a kinase interactor and can be refined
  to `GO:0019901`.
