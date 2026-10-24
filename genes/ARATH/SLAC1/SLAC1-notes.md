# SLAC1 (At1g12480, UniProt Q9LD83) curation notes

## Session 1 (2026-10-19)

No deep-research provider was available in this environment, so these notes are
built from the cached publications (`publications/PMID_*.md`), the UniProt record
and PubMed/E-utilities look-ups. Full text was available for PMID:18305484,
PMID:19955405, PMID:22730405, PMID:20981093, PMID:35523967, PMID:37963863 and
PMID:30361234; the others are abstract-only.

### Identity and family

- SLAC1 = SLOW ANION CHANNEL-ASSOCIATED 1, At1g12480, 556 aa, 10 TM helices with
  long cytosolic N-terminal (~189 aa) and C-terminal tails. Pfam PF03595 (SLAC1),
  InterPro IPR004695 (SLAC1/Mae1/Ssu1/TehA) and IPR030183 (SLAC/SLAH), PANTHER
  PTHR31269:SF11 (from the UniProt record).
- Distant homologue of bacterial TehA and fungal Mae1/Ssu1 transporters
  [PMID:18305482 "The SLAC1 protein is a distant homologue of bacterial and fungal C4-dicarboxylate transporters, and is localized specifically to the plasma membrane of guard cells."].
- Arabidopsis family: SLAC1 plus SLAH1-SLAH4; SLAH genes can complement slac1 when
  driven in guard cells [PMID:18305482 "Guard-cell-specific expression of SLAC1 or its family members resulted in restoration of the wild-type stomatal responses, including CO2 sensitivity"].

### Expression and localization

- Preferentially expressed in guard cells
  [PMID:18305484 "SLAC1 ( SLOW ANION CHANNEL-ASSOCIATED 1 ) is preferentially expressed in guard cells"].
- Plasma membrane (GFP fusion, onion epidermis, tobacco protoplasts) [PMID:18305484
  "The plasma membrane protein SLAC1 is essential for stomatal closure"]; independently
  [PMID:18305482] (above). BiFC with OST1 in mesophyll protoplasts gives signal only
  at the plasma membrane [PMID:19955405 "YFP-fluorescence complementation was observed at the level of the plasma membrane exclusively"].
- The ISM nucleus prediction (AtSubP) has no support; SLAC1 is a polytopic PM protein.

### Channel activity

- Loss of SLAC1 abolishes guard-cell S-type anion currents (Ca2+- and ABA-activated)
  but not R-type or Ca2+ channel currents [PMID:18305484 "Mutations in SLAC1 impair slow (S-type) anion channel currents that are activated by cytosolic Ca2+ and abscisic acid, but do not affect rapid (R-type) anion channel currents or Ca2+ channel function."].
- Heterologous expression: silent alone; active with OST1 in Xenopus oocytes;
  anion-selective, NO3- > Cl- >> malate, HCO3-, SO4 2-; weakly voltage dependent;
  not proton-coupled [PMID:19955405 "Our studies demonstrate that SLAC1 represents the slow, deactivating, weak voltage-dependent anion channel of guard cells controlled by phosphorylation/dephosphorylation."].
- Structure: trimer, each protomer a 5-helix pore gated by conserved Phe450
  (TehA homologue structure + AtSLAC1 mutagenesis) [PMID:20981093 "SLAC1 is a symmetrical trimer composed from quasi-symmetrical subunits"];
  F450A gives large constitutive currents [PMID:20981093 "removal of the phenyl group in HiTehA F262A or in the homologous AtSLAC1 F450A resulted in very large Cl− currents relative to wild-type levels"].
  GOA's IDA rows cite this paper by DOI:10.1038/nature09487 = PMID:20981093.
- Cryo-EM of AtSLAC1 (2022, 2023): homotrimer, each subunit an independent pore;
  cytosolic N/C-terminal "plug" holds the closed state; phosphorylation releases it
  [PMID:35523967 "each subunit of AtSLAC1 functions as an independent anion pore"]
  [PMID:37963863 "Multiple phosphorylation of an intracellular domain (ICD) causes dissociation of ICD from the transmembrane domain."].
  BdSLAC1 structure + AtSLAC1 electrophysiology: 14 phosphosites, ~330-fold
  activation [PMID:33926963 "We identified 14 phosphorylation sites in AtSLAC1 and showed nearly 330-fold channel-activity enhancement with 4 to 6 of these phosphorylated."].

### Regulation by kinases / phosphatases

- OST1 (SnRK2.6) binds the N-terminus and phosphorylates Ser120; ABI1 prevents
  activation [PMID:19955405 "Integration of ABI1 into the SLAC1/OST1 complex, however, prevented SLAC1 activation."];
  [PMID:19955427 "the OST1 kinase interacts with the SLAC1 anion channel, leading to its activation via phosphorylation"];
  PP2CA binds SLAC1 directly [PMID:19955427 "direct interaction with SLAC1 itself"].
- In planta S120 is the OST1 site needed for ozone-induced rapid closure
  [PMID:20128877 "only S120 was a specific phosphorylation site for OST1"].
- CPK21/CPK23 (and CPK6) interact with and activate SLAC1 [PMID:20385816
  "Split YFP-based protein-protein interaction assays, using SLAC1 as the bait, identified guard cell expressed CPK21 and 23 as major interacting partners."].
- GHR1 [PMID:22730405] interacts with/activates SLAC1 in oocytes, but later shown
  to be a pseudokinase [PMID:30361234 "suggesting that GHR1 is an inactive pseudokinase"].
- SIF2 (At1g51850) phosphorylates S65 [PMID:32327536 "SIF2-mediated activation of SLAC1 depends on specific phosphorylation of Ser 65."].
- CO2 relay RHC1 -> HT1 -| OST1 -> SLAC1 [PMID:25599916].

### Physiology (all upstream of the channel; SLAC1 is the effector)

- slac1: stomata insensitive to CO2, ABA, O3, humidity, light/dark, Ca2+, H2O2, NO
  [PMID:18305484 "The plasma membrane protein SLAC1 is essential for stomatal closure in response to CO2, abscisic acid, ozone, light/dark transitions, humidity change, calcium ions, hydrogen peroxide and nitric oxide."].
- Anion over-accumulation in guard cells of the mutant [PMID:18305482 "The loss-of-function mutation in SLAC1 was accompanied by an over-accumulation of the osmoregulatory anions in guard cell protoplasts."].
- 8-nitro-cGMP closure requires SLAC1 [PMID:23396828]; systemic light-stress
  stomatal closure requires SLAC1 [PMID:29463779].
- Negative regulation of stomatal opening: SLAC1 inhibits KAT1 (not KAT2) via
  protein interaction [PMID:27002025 "Voltage-clamp results demonstrated that SLAC1 inhibited KAT1 dramatically, but did not inhibit KAT2."]
  (single study, abstract only). Laanemets et al. [PMID:23766366] describe slac1
  stomatal opening defects as compensatory feedback (abstract is a single sentence).

### Curation decisions (summary)

- Core MF: GO:0008308 voltage-gated monoatomic anion channel activity (matches
  modules/abscisic_acid_signaling.yaml). Parent GO:0008509 rows -> MODIFY.
- Core BP: GO:0090332 stomatal closure; transport: GO:0098656, plus Cl- and NO3-
  transmembrane transport as refinements of "inorganic anion transport".
- Core CC: plasma membrane; generic "membrane" -> MODIFY; nucleus (ISM) -> REMOVE.
- Bare protein binding: MODIFY to protein kinase binding (OST1, CPK21, CPK23, SIF2)
  or potassium channel inhibitor activity (KAT1, AKT2, per UniProt curated text);
  REMOVE for GHR1 (pseudokinase), KAT2 (not inhibited) and KC1.
- "Response to X" phenotypes (ABA, CO2, ozone, humidity, light) kept as non-core.

### Possible upstream reports

- GO:0005634 nucleus (ISM, GO_REF:0000122, AtSubP) is a false prediction for a
  10-TM plasma-membrane channel.
- GO:0090333 regulation of stomatal closure (IMP, PMID:29463779): SLAC1 executes
  closure (the anion efflux step) rather than regulating it; GO:0090332 fits.

## 2026-10-24: OpenScientist run on KAT1/AKT2 inhibition

Report: `SLAC1-hypotheses/slac1-kat1-inhibition/openscientist.md` (3 iterations, ~25 min).
Hypothesis: SLAC1 directly inhibits KAT1 and AKT2, but not KAT2, and this has been replicated.

- Verdict from the run: partially supported (weak to moderate), not independently replicated.
  The report supports keeping GO:0019870 as a non-core activity with caveats.
- Checked here: the Zhang 2016 oocyte result is verbatim in the cached paper
  [PMID:27002025 "SLAC1 inhibited KAT1 dramatically, but did not inhibit KAT2"]. The
  Laanemets 2013 abstract confirms that slac1 lowers inward K+ channel activity through
  raised cytosolic Ca2+ [PMID:23126621 "this is caused by the severely reduced activity of inward K(+) (K(+)(in)) channels in slac1 guard cells"].
  The report calls this "later work"; it is from 2013, three years before Zhang 2016.
- No action changes. The KAT1 and AKT2 rows stay MODIFY to GO:0019870 with a caveat added to
  their reasons. GO:0019870 was already absent from core_functions.
