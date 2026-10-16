# PDS1 (securin, P40316) - curation notes

## Identity

- YDR113C, 373 aa, largely disordered (MobiDB regions 1-27, 177-278); N-terminal D-box
  RLPL 85-88; C-terminal separase-interaction segment 258-373 resolved in PDB 5U1S/5U1T.
- No PANTHER family (PTTG1 and Cut2 sit in PTHR10418; Pds1 is unclassified) - so no IBA
  rows and no PAINT node to argue with. Functional equivalence to PTTG1/Cut2 is by
  mechanism, not sequence.
- Not in `gocams/index.tsv`; cited as a securin representative member in
  `modules/metaphase_anaphase_transition_and_mitotic_exit.yaml` with MF GO:0004869.

## Mechanism synthesis

- Founding complex paper: "Pds1p forms a stable complex with a 180 kDa protein called
  Esp1p, which is essential for the dissociation of Scc1p from sister chromatids and for
  their separation" and the APC acts "by liberating the sister-separating Esp1 protein
  from its inhibitor Pds1p" [PMID:9635435].
- Dual mechanism: "securin, while present, directly inhibits the proteolytic activity of
  separase. Securin prevents the binding of separase to its substrates." and "securin is
  required and sufficient to cause accumulation of separase in the nucleus"; "Securin
  also ensures that separase gains full proteolytic activity in anaphase." [PMID:12123570].
- Structure: "residues 258-269 of securin are located in the separase active site,
  illuminating the mechanism of inhibition"; Pro263 replaces the P1 Arg so securin is not
  cleaved; "contacts outside the separase active site are crucial for stabilizing the
  complex"; "securin likely helps to stabilize the overall structure of separase"
  [PMID:28146474].
- Localisation: "As cells progressed through S-phase, Pds1GFP protein accumulated almost
  exclusively in the nucleus."; a fraction "remains at the spindle pole bodies and the
  spindle midzone in anaphase cells"; "Association with Pds1 occurs during S phase and is
  required for efficient nuclear targeting of Esp1." [PMID:11149918].
- Shuttling: Pds1 among proteins "displaying CDK1- and cell cycle-regulated nuclear
  transport"; Msn5 mediates export [PMID:19520826].
- Cdc28 phosphorylation (S277, S292) "is important for efficient binding of Pds1 to Esp1
  and for promoting the nuclear localization of Esp1" [PMID:12050115].
- Late mitosis: "securin still inhibits separase to repress mitotic exit in anaphase";
  APC/C-Cdh1 clears it at telophase [PMID:27418100].
- DNA damage: "the Saccharomyces cerevisiae securin Pds1 blocks anaphase promotion by
  inhibiting ESP1-dependent degradation of cohesins"; pds1 is epistatic with rad51,
  synergistic with rad9, "defective in SSA" [PMID:15533838]; "scc1-15A pds1Δ double
  mutant, however, exhibits marked sensitivity to the DNA-damaging agent phleomycin"
  [PMID:27325700].
- Meiosis: "Pds1p destruction is required for metaphase I-anaphase I transition";
  "Pds1p is required for recombination in both double-strand-break formation and
  synaptonemal complex assembly"; Mcd1 "precociously destroyed" in meiotic pds1 cells
  [PMID:19001291]; "Two waves of securin (Pds1) destruction were detected in anaphase I
  and II" [PMID:38413836].
- Deep research (falcon) agrees: stoichiometric inhibitor plus chaperone-like partner,
  nucleus as functional site; the vacuolar-trafficking claim is preprint-only and was not
  used.

## Supporting-entity ids (SGD)

- SGD:S000003330 = ESP1; SGD:S000002161 = MCD1/SCC1; SGD:S000000897 = RAD51;
  SGD:S000002625 = RAD9 (resolved via yeastgenome.org backend).

## Decisions

- Both bare `protein binding` IPI rows (Esp1) and both `enzyme binding` IPI rows (Esp1)
  -> MODIFY to GO:0004869 cysteine-type endopeptidase inhibitor activity, per repository
  policy for GO:0005515 and because the bound enzyme is a caspase-like cysteine protease
  whose inhibition is shown biochemically [PMID:12123570] and structurally [PMID:28146474].
- GO:0051276 chromosome organization (InterPro2GO) -> MODIFY to GO:2000816, matching the
  PTTG1 and cut2 reviews.
- GO:0008104 intracellular protein localization IMP -> MODIFY to GO:0034504 protein
  localization to nucleus and GO:1902480 protein localization to mitotic spindle (both
  verified in QuickGO); Pds1 does the escorting so the participation test is met.
- GO:0000070 IMP and GO:0051306 IDA -> ACCEPT: Pds1 participates via its activating /
  targeting arm (separase is mislocalised and under-active without it), not only as a
  regulator.
- GO:0006974 IGI -> ACCEPT (Pds1 is the checkpoint effector; it does the inhibiting).
- GO:0000725 recombinational repair (IMP + 2 IGI) -> KEEP_AS_NON_CORE: genuine phenotype,
  curator read full text (cache is abstract-only), but the repair role is indirect via
  separase/cohesin restraint. Did not MODIFY to the SSA descendant because the curator had
  the full text and chose the parent.
- GO:0001100, GO:0007127, GO:0051307 -> KEEP_AS_NON_CORE (real but secondary / NAS).
- Nucleus (3 IDA + IEA), spindle IDA, cytoplasm (IDA + IEA), separase-securin complex IPI
  -> ACCEPT; cytoplasm accepted because the complex assembles there before import
  [PMID:11149918], consistent with PTTG1 review.
- No NEW rows. GO:0140608 cysteine-type endopeptidase activator activity is used in
  core_functions (as in the PTTG1 review) but not proposed as NEW: SGD has not annotated
  it and the activation evidence [PMID:12123570] is captured through the ACCEPTed
  GO:0051306 row. Substrate-side terms (APC/C-dependent catabolic process) are not in
  GOA and were not added - Pds1 is the substrate there, not a participant.
- Not cached and therefore not cited with quotes: PMID:8985178 (Cohen-Fix 1996, D-box
  and APC ubiquitination), PMID:8601617 (Yamamoto 1996, pds1 identification/checkpoint),
  PMID:11553328 (Cdc20 binding). UniProt summarises these.

## Validation

- `just validate yeast PDS1`: valid; remaining warning is the informational
  "GO:0140608 not reflected in existing_annotations" (same situation as PTTG1).
