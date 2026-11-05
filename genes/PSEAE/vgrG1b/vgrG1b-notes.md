# vgrG1b (PA0095, Q9I737) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I737 --alias vgrG1b`; accession matches the
worklist (reviewed entry VGR1B_PSEAE). No deep-research provider key was
available. PMID:21325275 and PMID:24794869 read in full; PMID:30455305 is
abstract only (fetched with `just fetch-pmid`), but its abstract states the
decisive facts.

### Identity and literature

- 741 aa VgrG-family protein, encoded in HSI-I near vgrG1a and closely related
  to it (64% identity, PMID:21325275 Fig. 2).
- Its own release is independent of all three T6SSs
  [PMID:21325275 "Thus, VgrG1b secretion is independent of the three known T6SS clusters."],
  and it is dispensable for the H1-T6SS
  [PMID:21325275 "Overall, these results indicate that although vgrG1b is co-expressed with H1-T6SS genes, VgrG1b neither impacts secretion of components of the H1-T6SS nor requires H1-T6SS components for its own secretion."].
  The authors excluded lysis and periplasmic leakage as the cause of its
  appearance in supernatants.
- It nevertheless carries its own cargo: reintroducing vgrG1b alone into a
  triple vgrG1abc mutant restores activity
  [PMID:24794869 "Finally, VgrG1b-dependent killing is detectable upon complementation of a triple vgrG1abc mutant."],
  with the partner protein encoded in its own cluster
  [PMID:24794869 "We identified three specific VgrG/toxin couples, namely VgrG1a/PA0093, VgrG1b/PA0099, and VgrG1c/RhsP1"].
- The 2018 work establishes the spike role and the H1-T6SS dependence of that
  delivery [PMID:30455305 "Tse7 sits on the tip of the VgrG1b spike"]; the same
  abstract states that the delivery of Tse7 is dependent on the H1-T6SS cluster.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002088178 | GO:0033103 protein secretion by the type VI secretion system | 3 (Q9I737, Q9I741, Q9I0F3) | 13 (3 taxa) | GO:0033103, IMP, PMID:21325275 (PseudoCAP) | WRONG | The cited paper's vgrG1b result is negative on both counts (the mutant secretes Hcp1 and the other VgrGs normally; its own release needs no ClpV). An IMP row cannot rest on that. The term itself is true of vgrG1b on later evidence (PMID:30455305, PMID:24794869), so the fix is the reference, not the term. Full text read, so CONFIRMED. | vgrG1a (Q9I741) and vgrG1c (Q9I0F3), both SOUND (IDA PMID:20114026, IMP PMID:21325275) | Yes — the node rests on the vgrG1a and vgrG1c seeds, so no GO_CENTRAL defect |
| PTN002088178 | GO:0033104 type VI protein secretion system complex | 3 (Q9I737, Q9I0F3, Q9I741) | 13 (3 taxa) | GO:0033104, IMP, PMID:21325275 (PseudoCAP) | WRONG | Same reference problem. Complex membership is defensible for a spike protein whose cargo delivery needs the H1-T6SS cluster, but not core: the Hcp1 apparatus assembles and fires without VgrG1b. | as above | Yes |

One PSEUDOCAP defect (WRONG_REFERENCE, REPOINT PMID:21325275 ->
PMID:30455305, CONFIRMED) is recorded on the GO:0033103 IMP row and covers both
rows. No GO_CENTRAL defect: the node term suits the clade (13 leaves, all VgrG
spike proteins in three taxa) and the IBDs survive without this seed.

## Decisions summary

- ACCEPT: GO:0033103 (IBA, IEA, IMP) — term true, reference wrong on the IMP row.
- KEEP_AS_NON_CORE: GO:0033104 (IBA, IEA, IMP); extracellular region (EXP, IEA).
- Counts: ACCEPT 3, KEEP_AS_NON_CORE 5.
- Defects: PSEUDOCAP 1 (WRONG_REFERENCE, CONFIRMED), GO_CENTRAL 0.
- One BIOLOGY knowledge gap recorded: the export route for VgrG1b itself is
  unidentified.
