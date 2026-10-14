# CIMAP3 (Pitchfork, PIFO; C1orf88) — curation notes

## Deep research status

- First attempt `just deep-research-falcon human CIMAP3 --fallback perplexity-lite` was stopped
  (falcon default 600 s timeout; perplexity-lite fallback unavailable in this environment).
- Re-run with `--timeout 2400`: SUCCEEDED (CIMAP3-deep-research-falcon.md). It surfaced two
  additional primary papers, now cached and used: Jung et al. 2016 (PMID:26901434) and Leung et al.
  2025 (PMID:39743588).

## Identity

- UniProt Q8TCI5, "Ciliary microtubule-associated protein 3" / "Protein pitchfork"; HGNC symbol
  CIMAP3 (previous C1orf88, PIFO). Three isoforms.
- Domains: two SHIPPO repeats (PF07004), shared with ODF3/CIMAP1 family (sperm-tail outer dense
  fiber-related proteins). PANTHER PTHR31508 (PROTEIN PITCHFORK).
- The paper notes the Pifo DUF1309 (SHIPPO-repeat) domain "is only found in a few proteins,
  including Outer dense fiber3 (Odf3) and Odf3 like" [PMID:20643351].

## Function (single key paper: Kinzel et al. 2010, Dev Cell)

- Mouse node gene; haploinsufficiency causes node cilia duplication, left-right defects and heart
  failure [PMID:20643351 "Haploinsufficiency causes a unique node cilia duplication phenotype, left-right asymmetry defects, and heart failure."].
- Localization: vesicles budding from Golgi, TGN, along the growing axoneme, basal body
  [PMID:20643351 "In G0-deprived primary ciliated cells, Pifo localizes to the TGN and to the basal body"].
  Accumulates at the basal body during disassembly
  [PMID:20643351 "Restimulation of G0 cells led to rapid accumulation of PIFO-Venus at the basal body/centrosome"].
- Aurora A activation: PIFO binds AurA in pull-downs and overexpression prolongs AurA
  activation; R80K dominant-negatively blocks it
  [PMID:20643351 "This pull-down analysis revealed that both WT and R80K PIFO physically interact with endogenous AurA"];
  [PMID:20643351 "Strikingly, overexpression of SF-TAP-PIFO during the early phase of cilia disassembly leads to a prolonged activation of AurA, whereas total AurA levels were largely unaffected"];
  [PMID:20643351 "these results indicate that mouse and human PIFO accumulate in a cell cycle-dependent manner at the basal body to activate AurA, a process that is specifically abolished by the R80K mutation."].
  Mechanism of activation (direct allosteric vs. scaffolding/delivery) is not established.
- Cilia disassembly phenotype: in Pifo+/- cells "the basal body fails to disconnect from the cilium
  and the cilium is retained during mitosis"; required "specifically to control cilia retraction as
  well as the liberation and duplication of the basal body/centrosome during primary cilia
  disassembly" [PMID:20643351].
- Not required for assembly: "haploinsufficiency for Pifo does not block cilia assembly per se"
  [PMID:20643351].
- Interactions (TAP pull-down of endogenous proteins from HEK293T lysates; direct vs. indirect not
  resolved): Rab6, Rab8, Arl13b, gamma-tubulin, centrin, beta-tubulin, Kif3a
  [PMID:20643351 "the early endosome marker Rab6, the late endosome marker Rab8, the cilium localized small GTPase Arl13b (Caspary et al., 2007), the PCM protein γ-Tubulin, the centriolar protein Centrin, the MT protein β-Tubulin, and the motor protein Kif3a, all physically interact with Pifo/PIFO in cell culture"].
  The authors interpret these as association with ciliary targeting complexes.
- Restricted expression: chordate-specific and expressed in organizer regions; authors explicitly
  say Pifo "cannot be part of a general regulatory mechanism for cilia disassembly" [PMID:20643351].
- Human genetics: heterozygous R80K in a fetus with situs inversus/cystic liver and kidney and a
  DORV patient; causality not established.
- Nuclear signal: [PMID:20643351 "The ultrastructural analysis revealed that the protein is localized in the nucleus, Golgi apparatus, and in vesicles of the TGN"];
  testis fractionation put the long (coiled-coil) isoform in the nuclear fraction. No nuclear
  function is known.

## Smoothened ciliary targeting (Jung et al. 2016; via deep research, verified in cache)

- [PMID:26901434 "Here we show that Pitchfork (Pifo) and the G protein-coupled receptor associated sorting protein 2 (Gprasp2) are essential components of an Hh induced ciliary targeting complex able to regulate Smo translocation to the PC"].
- Conditional deletion after ciliogenesis abolishes SAG-induced Smo entry; Venus-Pifo rescues
  [PMID:26901434 "PifoFD/FD PLCs with normally formed PC barely responded to SAG induced pathway activation, which can be sufficiently rescued by stable Venus-Pifo expression"].
- PIFO does not bind SMO directly; GPRASP2 bridges them
  [PMID:26901434 "suggesting that a heterotrimeric ciliary targeting complex can be formed in which Gprasp2 bridges between Smo and Pifo"].

## Motile axoneme (Leung et al. 2025)

- [PMID:39743588 "For example, CIMAP3 is present in all mammalian axonemes hitherto studied, yet CIMAP2, which binds the same protofilament cleft, is found only in sperm"].
  CIMAP3 sits at the external surface of doublet microtubules, a structural axonemal MAP role
  consistent with its SHIPPO repeats and current name.

## Curation decisions summary

- Core: AURKA-activating regulator at the basal body promoting primary cilium disassembly
  (cilium retraction and basal body release). MF: protein kinase activator activity (IBA,
  phylogenetically placed; target experimental support from PMID:20643351); AURKA binding.
- NEW: GO:0061523 cilium disassembly (IMP, PMID:20643351). Comparator check: the analogous AURKA
  activator NEDD9 (and AURKA, HDAC6) carry GO:0061523 involved_in in human GOA (IMP,
  PMID:17604723), so a regulator-activator of the AurA-HDAC6 disassembly module legitimately
  carries this term under current practice.
- NEW GO:0061512 protein localization to cilium (ISS from mouse, PMID:26901434) and GO:0097545
  axonemal doublet microtubule (IDA, PMID:39743588). Nucleus row kept as non-core (mouse IDA).
- Binding terms from TAP pull-downs (kinesin, small GTPase, beta-/gamma-tubulin): keep as non-core
  (association, possibly indirect). Generic protein binding: remove (CETN1); ARL13B row modified to
  small GTPase binding to match the RAB6A/RAB8A rows from the same experiment.

## HPA cilium atlas vs module role

- HPA (member_evidence.md): CIMAP3 — no HPA cilia/centrosome call; "not in HPA". The HPA cilium
  atlas (Hansen et al. 2025, PMID:41005307; only metadata cached, no abstract text) therefore
  provides neither support nor contradiction.
- Module role (stage 7, disassembly): "Pitchfork (CIMAP3); AURKA activator". This matches the
  primary literature, and core_functions is written to that role. Caveats for the module: the
  evidence rests on a single study, mostly mouse/overexpression; expression is restricted to
  organizer/embryonic ciliated cells (and testis), so CIMAP3 is a context-specific rather than
  general component of the disassembly machinery. The absence of an HPA call is consistent with
  restricted expression rather than evidence against the role.
- Disagreement/extension: the module assigns only the disassembly role. The literature also
  supports (i) Smoothened ciliary targeting (Hedgehog; mouse) and (ii) a structural CIMAP role on
  motile-cilium doublet microtubules. core_functions lists disassembly first (the module role) and
  Smo targeting second. The axonemal location is recorded as a NEW CC annotation but not as a core
  function, since no activity is known. CIMAP3 could also be cross-listed in the Hedgehog module.
