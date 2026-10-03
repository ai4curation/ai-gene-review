# KIF2A — curation notes

## Deep research status

- First run (`--fallback perplexity-lite`) stopped (falcon 600 s default timeout; perplexity-lite
  unavailable). The 2400 s rerun was killed (exit 137); a second rerun SUCCEEDED
  (KIF2A-deep-research-falcon.md). It added Trofimova 2018 (PMID:29980677) and Vysloužil 2025
  (PMID:39930500), both cached and used, and noted cell-line variability of the spindle phenotype
  (largely normal bipolar spindles in RPE1).

## Identity

- UniProt O00139, kinesin-like protein KIF2A (HK2); kinesin-13 family (central motor domain), with
  paralogs KIF2B and KIF2C/MCAK. Several isoforms.
- Disease: cortical dysplasia, complex, with other brain malformations 3 (CDCBM3).

## Core biochemistry: ATP-dependent microtubule depolymerase

- [PMID:15302853 "Kif2a has been shown to catalyze microtubule depolymerization in the absence of motile function (Desai et al., 1999)."]
- Purified KIF2A depolymerizes GMPCPP microtubules; TTBK2 phosphorylation inhibits it
  [PMID:26323690 "Phosphorylation by TTBK2 decreased the MT-depolymerizing activity of KIF2A."];
  [PMID:26323690 "Collectively, these data show that TTBK2 inhibits the MT-depolymerizing activity of KIF2A by reducing the interaction between KIF2A and MTs."].
- Historical motility: mouse KIF2 was reported as a plus-end-directed anterograde axonal motor in a
  gliding assay [PMID:7535303 "Recombinant KIF2 exists as a dimer with a bigger head and plus-end directionally moves microtubules at a velocity of 0.47 +/- 0.11 microns/s"].
  This contrasts with the kinesin-13 consensus (depolymerization without motile function). The
  motor/transport annotations are therefore kept but treated as non-core.
- GO has no "microtubule depolymerase" MF term (OLS search for "depolymerase" in GO returned only
  polyester depolymerases; MCAK itself is annotated only with motor activity / MT binding). I
  propose an NTR "ATP-dependent microtubule depolymerase activity".

- Structure: [PMID:29980677 "Kinesin-13 proteins are major microtubule (MT) regulatory factors that catalyze removal of tubulin subunits from MT ends"];
  [PMID:29980677 "AMPPNP-bound Kif2A can form stable complexes with tubulin in solution and trigger MT depolymerization."].

## Mitosis

- Required for bipolar spindle assembly; localizes to centrosomes/spindle poles
  [PMID:15302853 "RNAi-induced knockdown of Kif2a expression inhibited cell cycle progression because cells assembled monopolar spindles."].
- DDA3/PSRC1 recruits KIF2A to spindle and poles and controls spindle dynamics
  [PMID:18411309 "Biochemically, DDA3 directly interacted with the MT depolymerase Kif2a in an MT-dependent manner and increased the efficiency of targeting Kif2a to spindle poles."].
- esiRNA screen: Kif2A crucial for spindle formation [PMID:15843429].
- Distinct from KIF2B/MCAK [PMID:17538014 "the microtubule depolymerase activities of Kif2a, Kif2b, and MCAK fulfill distinct functions during mitosis in human cells."].

## Neurons and migration

- Kif2a-/- mice: overextended collateral branches; decreased MT depolymerization in growth cones
  [PMID:12887924 "we propose that KIF2A regulates microtubule dynamics at the growth cone edge by depolymerizing microtubules and that it plays an important role in the suppression of collateral branch extension."].
- TTBK2-EB1/3 removes KIF2A from MT ends to regulate MT dynamics in migrating cells [PMID:26323690].

## Cilium disassembly (module role)

- [PMID:25660017 "we report that kinesin superfamily protein 2A (KIF2A), phosphorylated at T554 by PLK1, exhibits microtubule-depolymerizing activity at the mother centriole to disassemble the primary cilium in a growth-signal-dependent manner."]
- [PMID:25660017 "KIF2A-deficient hTERT-RPE1 cells showed the impairment of primary cilia disassembly following growth stimulation."]
- TTBK2 restrains KIF2A at the mother centriole during cilium growth
  [PMID:39930500 "we link the defects in cilia growth to aberrant turnover of a microtubule-depolymerizing kinesin KIF2A, which we find restrained by TTBK2 phosphorylation"].
  KIF2A is therefore a negative regulator of cilium length/maintenance as well as the disassembly enzyme.
- PCS syndrome: constitutively active PLK1-KIF2A pathway impairs ciliogenesis [PMID:25660017].
- Localization consistent with mother centriole: GOA has centriole and centriolar subdistal
  appendage IDA (PMID:23213374, 3D-SIM). KIF2A is not named in the cached text (probably supplementary
  data), so I defer to the curator.
- Comparator check for NEW/MODIFY to GO:0061523 cilium disassembly: human GOA annotates AURKA,
  NEDD9 and HDAC6 to GO:0061523 (IMP, PMID:17604723). KIF2A carries it in neither human nor mouse.
  KIF2A passes the participation test more directly than those regulators. It is the enzyme that
  depolymerizes the (axonemal/centriolar) microtubules, so it performs the step. I therefore
  re-point the cilium assembly IBA (MODIFY) to cilium disassembly with PMID:25660017 support.

## Curation decisions summary

- ACCEPT: MT binding, ATP binding, ATP hydrolysis, MT depolymerization, spindle/spindle pole/
  centrosome/centriole/subdistal appendage, mitotic spindle assembly/organization, MT cytoskeleton
  organization, cytoplasm/cytosol.
- KEEP_AS_NON_CORE: motor activity, MT-based movement, transport (historical motility),
  dendrite/dendritic transport/GABA-ergic synapse/sperm principal piece (electronic, from mouse),
  cell migration regulation, nucleoplasm (HPA), mitotic sister chromatid segregation (ARBA).
- REMOVE: generic protein binding (PSRC1/DDA3 interaction is real but GO:0005515 is uninformative;
  HT screen hits).
- MARK_AS_OVER_ANNOTATED: membrane (HDA, NK-cell membrane proteome). KIF2A has no TM segment and is
  at most peripherally associated.
- MODIFY: cilium assembly (IBA) -> cilium disassembly.

## HPA cilium atlas vs module role

- HPA v25: Basal body (Uncertain); Centrosome (Enhanced); main locations Annulus; Basal body;
  Centrosome; Nucleoli; Nucleoplasm. The HPA-sourced GOA rows (GO_REF:0000052) are centrosome,
  cytosol and nucleoplasm; there is no basal body row, consistent with the Uncertain grade. The HPA
  atlas paper (PMID:41005307) is cached as metadata only.
- Module role (stage 7: "MT depolymerase at basal body"): agrees with Miyamoto et al. 2015 (activity
  at the mother centriole), and the HPA centrosome (E) / basal body (U) calls are compatible with it.
  core_functions includes cilium disassembly. KIF2A is pleiotropic: its best-supported roles are
  mitotic spindle bipolarity and neuronal MT dynamics, and cilium disassembly rests on one primary
  study (abstract-only in cache). The module's assignment is reasonable, but KIF2A is not
  cilium-specific. Its common denominator is ATP-dependent MT depolymerization, used at the spindle
  pole, growth cone and mother centriole.
