# norpA review notes

## Session 1 (create review)

- `just fetch-gene DROME norpA` resolved P13217 (PIPA_DROME); 52 GOA rows.
- No deep-research keys were available. The literature synthesis is in `norpA-deep-research-manual.md`.
- Extra papers cached for this review: PMID:22952921 (lamina axons; full text), PMID:10806481 (GAP
  activity), PMID:2457447 (cloning), PMID:11500369 (INAD PDZ1/NorpA structure), PMID:15140198
  (allele series), PMID:12547945 (Malpighian tubule).
- Most GOA source papers are cached as abstracts only. Full text was available for 15883198,
  16301334, 28489826 and 22952921.

### Decisions

- Core MF: PIP2-PLC activity (GO:0004435) [PMID:7759511, PMID:2457447]. Second MF: GAP activity
  toward Gq-alpha (GO:0005096) [PMID:10806481 "show that PLC functions as a GTPase-activating
  protein (GAP)"; PMID:18184564].
- Core BP: GO:0030265 PLC-activating opsin-mediated signaling pathway. GO:0007602
  (phototransduction) and GO:0071482 (cellular response to light) are refined to it.
- GO:0007200 (PLC-activating GPCR pathway) is kept at that level. NORPA is also the
  effector of Gq-coupled signalling in gut epithelium [PMID:19289084] and Malpighian tubule
  [PMID:12547945], so the parent term fits the gene as a whole.
- Generic lipid rows go to GO:0046488. "Phospholipid biosynthetic process" is a sign error:
  PIP2 hydrolysis breaks a phospholipid down, so it is modified to GO:0046488.
- Bare protein-binding rows: the 9545241 row becomes PDZ domain binding (GO:0030165), from
  direct binding to INAD PDZ1/PDZ5. The 21703451 and 26853938 rows are removed as
  uninformative; their abstracts do not report a NORPA binding mode.
- Calcium-mediated signaling (TAS, review abstract): NORPA acts upstream of the TRP Ca2+ influx
  and is itself Ca2+-regulated, so it is marked over-annotated.
- Adult locomotory behavior (IMP gap-climbing, ARBA IEA): this is a consequence of blindness,
  so both rows are marked over-annotated.
- Negative regulation of retinal PCD: the source paper shows developmental PCD machinery is
  largely dispensable for norpA degeneration, so it is marked over-annotated. Photoreceptor cell
  maintenance is kept as non-core.
- Circadian rhythm (IGI with cry) is refined to GO:0043153 entrainment by photoperiod.
- NEW: axon (GO:0030424). Immunostaining of photoreceptor axons in the lamina [PMID:22952921
  "These results show that PLC, PKC, TRP and TRPL are present in photoreceptor axons."]. No NEW
  process term for neurotransmitter release: the only evidence is a hypomorph phenotype, which
  does not meet the participation bar.

### Open points
- Which isoform (A/B vs C/D) is used outside the eye (gut, tubule, GRNs)?
- The "positive regulation of clathrin-dependent endocytosis" row (PMID:25639794) could not be
  checked in full text. It was kept as non-core, deferring to the curator.
