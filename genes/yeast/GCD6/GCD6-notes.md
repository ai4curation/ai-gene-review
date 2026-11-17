# GCD6 (YDR211W, P32501; eIF2B epsilon) review notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- SGD curated description (`GCD6-deep-research-sgd.md`).
- UniProt P32501 FUNCTION, SUBUNIT, SUBCELLULAR LOCATION (by similarity to P56287).
- All 12 GOA-cited publications cached by `just fetch-gene-pmids yeast GCD6` (full text cached for PMID:22842922, 24852487, 26928762, 27023709, 37968396; others abstract-only).
- SGD ids resolved via UniProt REST: S000001734 GCN3 (eIF2B alpha), S000003315 GCD2 (eIF2B delta), S000005786 GCD1 (eIF2B gamma), S000002619 GCD6 itself.
- Context only: integrated stress response module, eif2b_gef annoton, PTHR45887 (module proposed in ai4curation/ai-gene-review#5904).

## Findings

- eIF2B (GCD1, GCD2, GCD6, GCD7, GCN3) is the GEF for eIF2 [PMID:8506384 "In vitro, this complex catalyzes guanine nucleotide exchange on eIF-2"].
- eIF2Bepsilon alone has catalytic activity, stimulated by complex formation [PMID:10805739 "In vitro, eIF2B catalytic function can be provided by the largest (epsilon) subunit alone (eIF2Bepsilon)"].
- Minimal catalytic domain residues 518-712 [PMID:12356745].
- Gcd1-Gcd6 form the catalytic subcomplex, not inhibited by eIF2(alphaP); Gcn3-Gcd7-Gcd2 regulatory subcomplex senses phosphorylation [PMID:9472020].
- Decamer with gamma2-epsilon2 core [PMID:24852487].
- GCD6 originally identified as a repressor of GCN4 translation; deletion lethal [PMID:8441423].
- Cytosolic localization from GFP screens [PMID:22842922; PMID:26928762].
- The ISS row (cytoplasmic translational initiation) cites an S. pombe eIF2B purification paper (PMID:27023709) with WITH human EIF2B5; the claim is correct for yeast GCD6.
