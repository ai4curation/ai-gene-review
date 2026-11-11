# C6T1A2 (Glycine max, Glyma17g18110 / GLYMA_17G165600) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used. Earlier text in the review that cited the
ProtNLM2 prediction review as support has been removed. The reference entry is kept,
marked as no longer used.

### Identity
- C6T1A2 is a 210-aa TrEMBL entry (PE 2, transcript level) for GLYMA_17G165600
  (Glyma17g18110.1; NCBI Gene 732609). It is the full-length product, not a fragment: the
  sequence is identical to A0A2K7G974 (gene name ZFP1) and 99.5% identical to Q1H8M0
  (zfp1). [file:SOYBN/C6T1A2/C6T1A2-bioinformatics/RESULTS-rereview.md]
- No reviewed Swiss-Prot entry exists for this gene, so there is no separate canonical
  product to review.
- GOA has no rows for C6T1A2. UniProt carries only GO:0008270 zinc ion binding
  (IEA:UniProtKB-KW), which is not in the GOA export.

### Domain evidence
- One C2H2 zinc finger (PROSITE PS50157, residues 79-106) with the plant Q-type QALGGH
  motif at 92-97. C-terminal LDLRL (206-210) matches the LxLxL EAR-like motif pattern.
  [file:SOYBN/C6T1A2/C6T1A2-bioinformatics/results-rereview.tsv]

### Phylogeny (PANTHER 19)
- C6T1A2 sits in PTHR47593:SF9. SF9 and SF8 are daughter lineages of a Pentapetalae
  duplication node (PTN002935045). The PTHR47593 tree has no Arabidopsis leaves and no
  PAINT nodes.
- The PAINT nodes in `interpro/panther/PTHR47593/PTHR47593-paint.tsv` (PTN008158895,
  GO:0009788 ABA negative regulation, seeded by ZFP7/ZFP4; PTN009184003, nucleus and
  GO:0000976) are nodes of the PTHR45730 tree. C6T1A2 does not descend from them.
- Arabidopsis ZFP7 is 36% identical overall to C6T1A2, and the OpenScientist report's
  claim that ZFP7 is the "direct ortholog" does not hold. ZFP7 is placed in PTHR47593:SF8
  by the UniProt cross-reference (HMM) but in PTHR45730 by the PANTHER tree.
- Conclusion: no ABA-signalling (GO:0009788) transfer. The family-level claim that ZFP1,
  ZFP3, ZFP4, ZFP6 and ZFP7 overexpression confers ABA insensitivity [PMID:24808098
  "regulated overexpression of ZFP3 and the closely related ZFP1, ZFP4, ZFP6, and ZFP7 zinc
  finger factors confers ABA insensitivity to seed germination"] concerns Arabidopsis
  genes, and the Arabidopsis "ZFP1" there is not soybean ZFP1/C6T1A2.

### Decisions
- GO:0003700 NEW (kept): domain-level inference from the Q-type C2H2 finger. The soybean
  TF ORFeome paper classifies C2H2 zinc fingers among its TF families [PMID:26268547].
- GO:0005634 NEW (kept): follows from the TF activity. Earlier support from the ProtNLM2
  file was removed and replaced with the bioinformatics results.
- Description rewritten: the GmZAT10-1 claim was dropped (a two-finger ZAT protein in a
  different family, and PMID:40158630 is not cached), as were the ZFP7 "closest ortholog"
  claim and the unverifiable AlphaFold pLDDT numbers.
- Same-species experimental data: none found. The deep-research file (falcon) also found
  no gene-specific literature.

### Family review disagreement
- `interpro/panther/PTHR47593/PTHR47593-review.yaml` discusses ZFP3 ABA evidence and
  leaves the scope UNRESOLVED. That is consistent with this review, but the family
  directory's PAINT file lists PTHR45730 tree nodes under PTHR47593. This should be
  flagged to whoever maintains the family-level files.
