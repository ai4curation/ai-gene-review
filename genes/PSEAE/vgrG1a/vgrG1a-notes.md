# vgrG1a (PA0091, Q9I741) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I741 --alias vgrG1a`; accession matches the
worklist (reviewed entry VGR1A_PSEAE). No deep-research provider key was
available. Cached full texts: PMID:20114026, PMID:21325275, PMID:24794869,
PMID:30177742. Abstract only: PMID:16763151, PMID:26894531, PMID:30455305
(the last three fetched with `just fetch-pmid`).

### Identity and literature

- 643 aa VgrG-family spike protein, encoded in HSI-I (the H1-T6SS cluster).
- Trimeric needle structure solved at 2.0 A
  [PMID:26894531 "Valine-glycine repeat protein G1 (VgrG1) forms the spike at the tip of the elongating tube formed by haemolysin co-regulated protein 1 (Hcp1)"].
- Secreted in a ClpV1-dependent manner, unlike VgrG1b
  [PMID:21325275 "Whereas VgrG1a and VgrG1c were secreted in a ClpV1-dependent manner, secretion of VgrG1b was ClpV1-independent."].
- Required, redundantly with VgrG1c, for Hcp1 export
  [PMID:21325275 "In conclusion, VgrG1a and VgrG1c are essential for efficient Hcp1 secretion but can function independently."];
  the double deletion abolishes Hcp1 secretion while deletion of the Tse cargo
  proteins does not
  [PMID:20114026 "Western blot analysis revealed that Hcp1 secretion was abolished in both the ΔclpV1 and ΔvgrG1 ΔvgrG4 strains, however it was unaffected by tse deletion"].
  Note the older nomenclature: vgrG1 = vgrG1a (PA0091), vgrG4 = vgrG1c (PA2685).
- VgrGs are also needed for export of other substrates
  [PMID:21325275 "Our results demonstrate that VgrG proteins are not only secreted components but are essential for secretion of other T6SS substrates."],
  and each VgrG pairs with its own cargo
  [PMID:24794869 "We identified three specific VgrG/toxin couples, namely VgrG1a/PA0093, VgrG1b/PA0099, and VgrG1c/RhsP1"].
- Cargo loading onto VgrG1a needs the chaperone EagT6 (UniProt SUBUNIT, from
  PMID:30177742).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002088178 | GO:0033103 protein secretion by the type VI secretion system | 3 (Q9I741, Q9I0F3, Q9I737) | 13 (3 taxa) | GO:0033103, IDA PMID:20114026 and IMP PMID:21325275 (PseudoCAP) | SOUND | The protein is exported by the H1-T6SS and is required, with VgrG1c, for Hcp1 export; both papers read in full. | vgrG1c (Q9I0F3), equally sound; vgrG1b (Q9I737), WRONG reference (see genes/PSEAE/vgrG1b) | Yes |
| PTN002088178 | GO:0033104 type VI protein secretion system complex | 3 (Q9I741, Q9I0F3, Q9I737) | 13 (3 taxa) | GO:0033104, IDA PMID:20114026 and IMP PMID:21325275 (PseudoCAP) | SOUND | VgrG1a is the spike at the tip of the Hcp1 tube (crystal structure), and behaves as an apparatus component rather than cargo. | as above | Yes |

The node is small and tight: the 13 leaves are P. aeruginosa VgrGs (vgrG1a,
vgrG1b, vgrG1c, vgrG4b, vgrG5, PA2373, PA3294, PA5266) plus Yersinia pestis and
Salmonella homologues, so the node terms suit the clade. No GO_CENTRAL defect
is warranted: the IBDs stand on the vgrG1a and vgrG1c seeds even after the
vgrG1b reference problem is set aside.

## Decisions summary

- ACCEPT: GO:0033103 (IBA, IDA, IEA, IGC, IMP), GO:0033104 (IBA, IDA, IEA, IGC,
  IMP).
- KEEP_AS_NON_CORE: extracellular region (EXP, IEA) — a consequence of firing.
- Counts: ACCEPT 10, KEEP_AS_NON_CORE 2.
- Defects: none for this gene (PSEUDOCAP 0, GO_CENTRAL 0).
