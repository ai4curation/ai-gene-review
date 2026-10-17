# DMI1 (Medicago truncatula, Q6RHR6) – curation notes

## Sources
- UniProt Q6RHR6 (Swiss-Prot), GOA (7 rows), falcon deep research
  (`DMI1-deep-research-falcon.md`), cached PMIDs below.
- Full text available: PMID:35972963 (Liu 2022), PMID:39814887 (Cook 2025),
  PMID:31420535 (Kim 2019, Lotus CASTOR). Abstract only: PMID:14963334, 17173544,
  17631529, 21825141, 22706284, 27230377, 39140702.
- PMIDs for Capoen 2011, Liu 2022 and Cook 2025 were resolved from DOI via Europe PMC
  (PubMed MCP was rate-limited).

## Identity and domain architecture
- POLLUX-type member of the CASTOR/POLLUX (TC 1.A.1.23) family; 4 predicted TM helices,
  two cytosolic RCK domains (RCK1 348-489, RCK2 608-757); crystal structure of the
  C-terminal soluble region (PDB 7VM8). [PMID:14963334 "The DMI1 (does not make
  infections) gene encodes a novel protein with low global similarity to a ligand-gated
  cation channel domain of archaea"]
- RCK = MthK-like Ca2+-regulated gating ring [PMID:17631529 "The cytosolic C terminus of
  DMI1 contains a RCK (regulator of the conductance of K(+)) domain that in MthK acts as a
  calcium-regulated gating ring controlling the activity of the channel"].
  NAD(P)-binding Rossmann superfamily hit reflects RCK fold, not enzymatic activity.

## Localization
- Nuclear envelope, functional GFP fusion [PMID:17173544 "a functional DMI1::GFP fusion is
  localized to the nuclear envelope in M. truncatula roots"].
- Preferentially inner nuclear membrane [PMID:21825141 "the cation channel DMI1, which is
  essential for symbiotic calcium oscillations, is preferentially located on the inner
  nuclear membrane"].
- Charpentier 2016 (GOA EXP source) also places the DMI1-CNGC15 complex at the nuclear
  envelope.

## Channel activity / ion selectivity
- Bilayer: ~64 pS in symmetrical KCl, long open state; A-for-S filter substitution made
  DMI1 "solo sufficient" vs Lotus CASTOR+POLLUX pair [PMID:22706284; deep research].
- Charpentier 2016 describes DMI1 as "the postassium-permeable channel, which modulates
  nuclear Ca(2+) release" [PMID:27230377].
- Cook 2025: the native filter (ADAGN) is non-selective cationic; replacing it with a
  strict K+ filter (TVGYG) fully complements dmi1-1 [PMID:39814887 "These results
  demonstrate that substituting a non-selective filter with a potassium-selective filter
  does not impair the function of DMI1."]. So K+ conduction is sufficient for function.
- Dispute: Kim 2019 reports Lotus CASTOR as a Ca2+-regulated Ca2+ channel
  [PMID:31420535]. Homolog evidence only; Cook 2025 TVGYG data argue that DMI1 Ca2+
  permeation is not required.

## Role in the common symbiosis pathway
- dmi1 mutants lack both nodulation and AM symbiosis; no Nod-factor calcium spiking
  [PMID:14963334; UniProt disruption phenotype].
- DMI1 forms a complex with CNGC15a/b/c (the Ca2+-permeable release channels)
  [PMID:27230377 "the cyclic nucleotide-gated channels form a complex with the
  postassium-permeable channel"]; GOA IPI x3 (protein binding) come from this.
- Gain-of-function DMI1 (S760N, spd1) gives spontaneous oscillations and nodules,
  CNGC15-dependent [PMID:35972963].
- Pacemaker: DMI1 is required for CNGC15 activation and sets the oscillation frequency
  [PMID:39814887 "DMI1 is not only essential for activating CNGC15, but it also acts as a
  pacemaker for the frequency of nuclear Ca2+ oscillations"].
- Peiter 2007: DMI1 modulates Ca2+ release from stores in yeast; "DMI1 is not directly
  responsible for Nod factor-induced calcium changes, but does have the capacity to
  regulate calcium channels".

## Curation decisions
- protein binding (IPI x3, CNGC15a/b/c) -> MODIFY to ion channel regulator activity
  (GO:0099106; "modulates the activity of a channel via direct interaction with it").
  Justified by direct interaction (C-terminus of DMI1 with N-terminus of CNGC15) plus
  Cook 2025 showing DMI1 C-terminal Ca2+-binding mobility modulates CNGC15 gating.
- monoatomic ion transport (IEA) -> MODIFY to monoatomic cation transmembrane transport.
- potassium ion transport (IEA) -> ACCEPT (supported by bilayer, Charpentier 2016, TVGYG).
- nuclear membrane (EXP, IEA) -> ACCEPT.
- NEW: monoatomic cation channel activity (GO:0005261, IDA PMID:22706284), kept generic to match Lotus CASTOR review.
- NEW: nodulation (GO:0009877) and arbuscular mycorrhizal association (GO:0036377).
  Comparator check: CNGC15A and CNGC15B (the partner channels in the same oscillator,
  same paper) carry IMP nodulation and IMP AM association; CCAMK and CYCLOPS carry
  nodulation. Participation: DMI1 is a working component of the nuclear Ca2+ oscillator
  (channel + pacemaker), not a substrate. Absence for DMI1 looks like a gap rather than a
  convention.
- Did not add nuclear inner membrane as NEW (descendant of existing nuclear membrane);
  described in text instead.

## Project curation question (symbiosis vs defense)
- DMI1 has no defense/immunity annotations; all roles are symbiotic signalling. Cook 2025
  / Jacott 2024 mention CNGC15/DMI1 roles beyond symbiosis (nitrate signalling) but not
  defense; not annotated.
