# mcrA (MTH_1164, O27232) — Methanothermobacter thermautotrophicus Delta H

Notes for the ARCHAEA project review. Automated deep research providers (falcon,
openai) were unavailable for this session (API authentication failures), so no
`-deep-research-*.md` file exists. Literature was researched manually via NCBI
E-utilities and the cached UniProt record; all PMIDs below were verified against
PubMed esummary and cached in `publications/`.

## Identity

- UniProt O27232 (MCRA_METTH), 550 aa, gene mcrA, locus MTH_1164; EC 2.8.4.1.
- Alpha subunit of methyl-coenzyme M reductase **isoenzyme I** (MCR I). The
  organism also encodes MCR II (mrtBDGA operon), a distinct isoenzyme.
- Operon: mcrBDCGA, immediately upstream of the mtr operon
  [PMID:7929010 "The MRI-encoding mcr operon (mcrBDCGA) has been located immediately upstream from the mtr operon (mtrEDCBA)"].
- Expression: mrt (MCR II) transcribed early in batch culture, then replaced by mcr (MCR I)
  [PMID:7929010 "Transcription of the mrt operon was found to occur only at early times in batch cultures and was then replaced by transcription of the mcr operon."].
  At the protein level, MCR I predominates under gas limitation
  [PMID:2269306 "When growth was limited by the gas supply, MCR I predominated."].

## Activity

- MCR catalyses CH3-S-CoM + HS-CoB -> CH4 + CoM-S-S-CoB, the terminal, methane-forming
  step of all methanogenic pathways.
- Delta H cell extracts: [PMID:3122735 "CH4 and CoM-S-S-HTP were produced stoichiometrically in a ratio of 1:1."]
  (cell extract; does not discriminate MCR I from MCR II).
- Purified enzyme (strain Marburg, now M. marburgensis): [PMID:3350018 "The enzyme was found to catalyze the reduction of methylcoenzyme M (CH3-S-CoM) with N-7-mercaptoheptanoylthreonine phosphate (H-S-HTP = component B) to CH4."]
- Two isoenzymes purified from both Marburg and Delta H strains, each with three subunits
  [PMID:2269306 "MCR II is similar to MCR I in that it is also composed of three different subunits alpha, beta, and gamma"].
  The cached record for PMID:2269306 is abstract-only; the curators' EXP annotation
  presumably reflects activity measurements on the purified MCR I in the full text.
- Mechanism: methyl radical / Ni(II)-thiolate intermediate, no methyl-Ni(III)
  [PMID:27199421 "magnetic circular dichroism spectroscopy identified the Ni(II)-thiolate intermediate"].

## Structure and the shared active site

- Crystal structure of M. thermoautotrophicum MCR (strain Marburg enzyme per UniProt P11558):
  [PMID:9367957 "two molecules of the nickel porphinoid coenzyme F430 are embedded between the subunits alpha, alpha', beta, and gamma and alpha', alpha, beta', and gamma', forming two identical active sites."]
- So the active site is built at the interface of two alpha subunits plus beta and gamma; the
  alpha subunit supplies the F430 axial Gln ligand and most CoM/CoB contacts (UniProt
  FT BINDING lines, by similarity to P11558; CoB site "ligand shared between two alpha subunits").
- The alpha subunit carries the active-site post-translational modifications (thioglycine,
  methylated His/Arg/Gln/Cys, didehydroaspartate) (UniProt PTM by similarity); modifications
  vary among methanogens [PMID:17725644 "MCRs from all methanogens investigated contain the thioxo peptide bond, but that the enzymes differ in their post-translational methylations."].
- MCR types I/II/III share virtually identical active-site architecture
  [PMID:28559298 "virtually identical active site architectures reflecting the chemically challenging mechanism of methane formation"].

## Localization

- Cytoplasmic, very abundant; some studies suggest association with/proximity to the
  cytoplasmic membrane, but no MCR subunit has a membrane anchor
  [PMID:30951290 "However, none of the genes associated with MCR synthesis"] (review, full text).
  Cytoplasm is retained as the location.

## Physiology

- M. thermautotrophicus Delta H is an obligate hydrogenotroph
  [PMID:30951290 "an archaeon that grows with H2 and CO2 as sole carbon and energy sources, forming methane."],
  so the only methanogenic route MCR I serves in this organism is CO2 reduction
  (GO:0019386 methanogenesis, from carbon dioxide).

## GO reasoning summary

- GO:0050524 (EXP x2, IEA): ACCEPT. Catalytic alpha subunit; GO convention annotates the
  catalytic subunit with `enables`. Complex context captured by NEW GO:0044674
  (verified in OLS: "methyl coenzyme M reductase complex", alpha2beta2gamma2 hexamer, is_a
  transferase complex). No MCR-subunit-specific activity term exists; `contributes_to`
  would understate the alpha subunit, which carries F430 ligand and most substrate contacts.
- GO:0015948 methanogenesis (IEA InterPro2GO): MODIFY -> GO:0019386 (organism only grows on H2/CO2).
- GO:0005737 cytoplasm (IEA, ISS from P11558): ACCEPT.
- No NEW cofactor-binding term proposed: GO has no F430-binding term, and nickel cation
  binding (used in METAC review) mis-describes binding of a nickel tetrapyrrole cofactor.

## Comparison with genes/METAC/mcrA review (not edited)

Issues noted there: REMOVE of GO:0016740 transferase activity (true-but-broad term; should
be TOO_GENERAL/MODIFY per CLAUDE.md); cytoplasm ACCEPT supported only by a non-verbatim
"See deep research file" quote; GO:0050524 supported by PMID:29743535 (about a radical SAM
methyltransferase, not the MCR activity — miscited); NEW GO:0051291 protein
heterooligomerization (assembly, not a physiological process the subunit performs);
nickel cation binding for an F430 (nickel-tetrapyrrole) cofactor; status DRAFT.
