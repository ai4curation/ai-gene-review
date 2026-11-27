# CDC28 (Cdk1, P00546) - working notes

## Identity and biology

- CDC28/YBR160W is the single essential CDK of *S. cerevisiae*; UniProt calls it
  "Cyclin-dependent kinase 1", EC 2.7.11.22, 298 aa, CMGC/CDC2 subfamily. UniProt
  features: ATP-binding Lys40, active site Asp136, MOD_RES Tyr19 (inhibitory) and
  Thr169 (activating). "Forms a stable but non-covalent complex with the CKS1
  protein and with a cyclin."
- Nine cyclins: Cln1-3 (G1), Clb5/6 (S), Clb3/4 (G2), Clb1/2 (M). Cks1 is required
  for G1 cyclin-Cdc28 activity but not Clb-Cdc28
  [PMID:10913169 "Cdc28 forms stable, active complexes with the B-type cyclins Clb4 and Clb5 regardless of whether Cks1 is present."].
- Start: [PMID:7002718 "Each mutation produces stage-specific arrest of cell division at start, the same point where mating pheromone interrupts division."];
  Cln2-Cdc28 is the G1/S kinase [PMID:2142620 "Cln proteins are an essential component of the active protein kinase complex required for the G1 to S transition"].
- Mitosis: [PMID:2165600 "the Cdc28 protein kinase is also required for mitosis and that this function is executed in the G2 interval of the cell cycle"];
  cdc28-1N/Clb suppression [PMID:1849457 "Its mitotic role, we believe, involves interaction with a family of at least four G2-specific cyclins."];
  Clb1-4 essential at G2/M [PMID:1427070 "the CLB genes perform an essential role at the G2/M-phase transition, and also a role in S phase."].
- Tyr19: dephosphorylation needed for SPB separation
  [PMID:8887667 "dephosphorylation of Tyr-19 is required for the segregation of SPBs"], mechanism = stabilisation
  of Cin8/Kip1/Ase1 against APC-Cdh1 [PMID:16688214 "Tyrosine 19 dephosphorylation of Cdk1 is necessary to specifically prevent proteolysis of these proteins."].
  Swe1 is itself a Cdk1 substrate [PMID:16096060 "Phosphorylation of Swe1 by Cdk1 activates Swe1"].
- Mitotic exit: Cdc28 phosphorylates Hct1/Cdh1 to keep APC off
  [PMID:10074450 "Phosphorylation of Hct1 provides a mechanism by which Cdc28 blocks its own inactivation during S phase and early mitosis."].
- DNA replication: Hartwell 1973 [PMID:4580573 "Mutations in three genes (cdc 4, 7, and 28) appear to block a precondition for DNA synthesis"];
  Dpb2 [PMID:14747467]; meiotic S phase [PMID:12783856 "Early inhibition of analog-sensitive cdc28-as1 blocked DNA replication"].
- Localisation: primarily cytoplasmic by IF in 1987 [PMID:3312233]; Cln3-Cdc28 cytoplasmic in early G1 (Whi3), nuclear
  in late G1 [PMID:14685274]; fraction at ER with Cln3 [PMID:17560371]; SPB -> CM plus ends -> bud neck with Kar9
  [PMID:12554645 "in G(1)/S the yeast Cdk1, Cdc28, associates with SPBs and phosphorylates Kar9"]; meiotic chromosome
  foci [PMID:20825495]; DSB enrichment [PMID:26801641].
- The deep-research file (falcon) is mostly built on theses/reviews (Ubersax 2004, Robertson 2020) and adds the
  docking-motif picture (LP / RxL / NLxxxL / LxF; Cks1 priming) and Whi5 hyperphosphorylation (Xiao 2024); none of
  its citations are in the GOA set, so the review is grounded on the cached GOA papers.

## Grading policy used

- Core (ACCEPT): the kinase activity terms (GO:0004672/4674/4693, GO:0106310, ATP binding), the holoenzyme
  complex, nucleus/cytoplasm, and the transitions the kinase itself gates: G1/S, G2/M, positive regulation of
  nuclear DNA replication, positive regulation of mitotic cell cycle, mitotic SPB separation, spindle assembly,
  positive regulation of meiotic cell cycle, regulation of cell cycle (IBA), mitotic cell cycle.
- Non-core (KEEP_AS_NON_CORE): processes Cdc28 controls through one named substrate (DSB resection/HR/NHEJ
  choice, SC assembly, telomerase recruitment, Eco1/cohesion, Tgl4/Nth1/Gph1 metabolism, Yta7/histone genes,
  Swi6 export, IME1 repression, Iqg1/AMR timing, Nup1/gene positioning, Cac1/CAF-I, Rnr2 relocalisation,
  bud growth, filamentous growth, Ipl1 spindle timing, Fus2), plus generic IBA "signal transduction" and the
  ER and bud-neck pools.
- MODIFY: 
  - 1902806 "regulation of cell cycle G1/S phase transition" (NAS, PMID:2569741) -> GO:0000082; the term is
    defined as a signalling pathway modulating a CDK and Cdc28 is the CDK.
  - 0045930 "negative regulation of mitotic cell cycle" (Hct1 paper) -> GO:0001100 negative regulation of exit
    from mitosis (what the paper shows).
  - 0045893 "positive regulation of DNA-templated transcription" x2 (Swi5 paper, PMID:1652372) -> GO:0042308
    negative regulation of protein import into nucleus; the abstract shows Cdc28 phosphorylation *prevents* Swi5
    nuclear entry [PMID:1652372 "we propose a model in which the CDC28 kinase acts directly to control nuclear entry of SWI5"]. Flagged that the curator may have had full-text data.
  - 0030163 "protein catabolic process" x2 (Sic1, Ash1) -> GO:0032436 positive regulation of proteasomal
    ubiquitin-dependent protein catabolic process (Cdc28 builds the phosphodegron; it is not part of the
    degradation machinery).
  - 0006892 post-Golgi vesicle-mediated transport -> GO:0060627 regulation of vesicle-mediated transport.
  - 0034504 protein localization to nucleus (Fus2) -> GO:1900180 regulation of protein localization to nucleus.
  - 0005515 protein binding with cyclin partners (Cln1/2/3, Clb5/6; 24 rows) -> GO:0030332 cyclin binding.
- REMOVE: protein binding with Cks1 (7 rows; captured by GO:0000307), Cak1 (3 rows; Cdc28 is Cak1's substrate),
  SV40 large T (heterologous), and the Cdc6 row citing PMID:23267104.
- MARK_AS_OVER_ANNOTATED: 0006370 mRNA capping (requirement via CTD-Ser5, not participation) and the stress
  granule HDA (single proteomic detection).

## Reference issues

- PMID:23267104 (Meier, Sit, Quake 2013 PNAS) is a microfluidic screen of *S. pneumoniae* proteins of unknown
  function; the cached title/abstract/full text never mention yeast, Cdc28 or Cdc6. GOA cites it for a Cdc28-Cdc6
  IPI. Recorded as reference_review MISCITED/NONE. The interaction is well documented in PMID:8930895.
- PMID:17460120 (DASH complex protein arms) is cited for Cdc28 Ser/Thr kinase IDA; the cached text has no kinase
  assay. Accepted (the activity is unquestionable) and deferred to SGD.
- PMID:22689984 is cited for RNA polymerase II complex binding (IDA); the cached text shows ChIP-seq occupancy
  and mutual Cdc28/Kin28 recruitment but not a physical-binding assay. Kept as non-core, deferred.

## Open points

- No GO-CAM in `gocams/index.tsv` contains P00546; modules g1_s_transition / g2_m_transition /
  cell_cycle_progression cite CDC28 as the budding-yeast exemplar (consistent with core functions 1 and 3).
- Not proposed as NEW (comparator check not run): spindle pole body (GO:0005816) localisation is documented
  in PMID:12554645 but only as a transient pool; recorded in core_functions locations rather than as a NEW CC row.
