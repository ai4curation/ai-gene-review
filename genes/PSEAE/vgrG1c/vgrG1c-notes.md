# vgrG1c (PA2685, Q9I0F3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I0F3 --alias vgrG1c`; accession matches the
worklist (reviewed entry VGR1C_PSEAE). No deep-research provider key was
available. Same literature as vgrG1a; PMID:20114026 and PMID:21325275 read in
full.

### Identity and literature

- 726 aa VgrG-family spike protein. Its gene is unlinked from HSI-I
  [PMID:20114026 "The PA0091 locus is located within HSI-I, while the PA2685 locus is found at an unlinked site that lacks other apparent T6S elements"],
  but is co-regulated with it through RetS. Originally named vgrG4.
- Among the most abundant proteins of the on-state H1-T6SS secretome, and
  required with vgrG1a for Hcp1 export
  [PMID:20114026 "Western blot analysis revealed that Hcp1 secretion was abolished in both the ΔclpV1 and ΔvgrG1 ΔvgrG4 strains, however it was unaffected by tse deletion"].
- ClpV1-dependent secretion and multimerisation
  [PMID:21325275 "We show that VgrG1a and VgrG1c form multimers, which confirmed the VgrG model predicting trimers similar to the tail spike."];
  redundancy with VgrG1a
  [PMID:21325275 "In conclusion, VgrG1a and VgrG1c are essential for efficient Hcp1 secretion but can function independently."].
- Carries a specific cargo, the Rhs protein RhsP1/Tse5
  [PMID:24794869 "In this respect, VgrG1c is involved in the delivery of an Rhs protein, RhsP1"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002088178 | GO:0033103 protein secretion by the type VI secretion system | 3 (Q9I0F3, Q9I737, Q9I741) | 13 (3 taxa) | GO:0033103, IDA PMID:20114026 and IMP PMID:21325275 (PseudoCAP) | SOUND | Exported by the H1-T6SS and required, with VgrG1a, for Hcp1 export; both papers read in full. | vgrG1a (Q9I741), equally sound; vgrG1b (Q9I737), WRONG reference (genes/PSEAE/vgrG1b) | Yes |
| PTN002088178 | GO:0033104 type VI protein secretion system complex | 3 (Q9I0F3, Q9I737, Q9I741) | 13 (3 taxa) | GO:0033104, IDA PMID:20114026 and IMP PMID:21325275 (PseudoCAP) | SOUND | Multimerises as a tail spike and behaves as an apparatus component, not cargo. | as above | Yes |

Clade and node-term judgement as recorded in genes/PSEAE/vgrG1a: a tight
13-leaf VgrG clade in three taxa, so no GO_CENTRAL defect is warranted.

## Decisions summary

- ACCEPT: GO:0033103 (IBA, IDA, IEA, IMP), GO:0033104 (IBA, IDA, IEA, IMP).
- KEEP_AS_NON_CORE: extracellular region (EXP, IEA).
- Counts: ACCEPT 8, KEEP_AS_NON_CORE 2.
- Defects: none for this gene (PSEUDOCAP 0, GO_CENTRAL 0).
