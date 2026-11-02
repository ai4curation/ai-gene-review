# Cdc42 (DROME, P40793) review notes

## Session 2026-10-28

- `just fetch-gene DROME Cdc42` resolved P40793 (CDC42_DROME); 109 GOA rows seeded.
- No deep-research provider keys; literature synthesis written by hand in
  `Cdc42-deep-research-manual.md` from cached publications.
- PMID:21690310 (Tinman/Cdc42 heart function) is cached abstract-only; full text read
  via PubMed Central (PMC3216339). It is not cited by any GOA row.

### Decisions worth flagging

- Bare `protein binding` rows: MODIFY to `protein kinase binding` where the partner is a
  kinase effector (Mbt, PMID:12490550; Gek, PMID:9371783), MODIFY to `GBD domain binding`
  for Frl (PMID:26801180, binding mapped to the Frl GBD-DID region), REMOVE for Par-6, Baz
  and Wash rows (uninformative; interactions themselves are real).
- `rhabdomere` (CC, IMP, PMID:14744998): a mutant phenotype cannot support a location;
  the paper reports rhabdomere morphogenesis defects in cdc42 clones, so MODIFY to
  `rhabdomere development` (GO:0042052).
- `actin filament polymerization` (IMP, PMID:8947551): Cdc42 does not polymerize actin;
  MODIFY to `positive regulation of actin filament polymerization`.
- `neuromuscular synaptic transmission` (IGI, PMID:21228159): Cdc42 dosage modifies
  release in cv-c/Dys mutants; MODIFY to `regulation of neurotransmitter secretion`.
- `maintenance of protein location` (IMP, PMID:12490550): the paper describes recruitment
  of Mbt to adherens junctions; MODIFY to `protein localization to adherens junction`.
- `sensory perception of touch` (PMID:23103192): indirect, via loss of sensory filopodia;
  MARK_AS_OVER_ANNOTATED.
- `synapse` (IEA, GO_REF:0000108): inferred from the synaptic-transmission BP row which is
  itself being modified; no localization data; MARK_AS_OVER_ANNOTATED.
- UNDECIDED where the cited abstract does not mention Cdc42 and full text was not
  available: nucleus (PMID:19498173 supplementary figure), cellularization TAS
  (PMID:12386932), NOT amnioserosa morphology change (PMID:11973353), dorsal appendage
  formation (PMID:11543614), nephrocyte filtration (PMID:23291470).

### NEW terms considered and rejected

- Heart contraction / regulation of heart contraction (PMID:21690310): evidence is
  dominant-negative and compound-heterozygote necessity data plus myofibril disarray.
  Which entity performs the contractile or rhythm step is not established (K+ channels
  dSUR/slo are downstream transcriptional readouts), so no NEW process term. Raised as a
  suggested question instead.
- No NEW MF terms: the informative MFs (G protein activity, GTPase activity, protein kinase
  binding, GBD domain binding) are covered by existing rows or MODIFY replacements.
