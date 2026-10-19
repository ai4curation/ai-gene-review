# PWL2 (Pyricularia oryzae, UniProt G5EI71) research notes

## Identity

- Secreted effector PWL2 = "Pathogenicity/Prevents pathogenicity toward Weeping Lovegrass 2"; 145 aa precursor
  with a 21-aa signal peptide; ORFs MGG_04301 / MGG_13863 (two copies in strain 70-15).
- Originally defined genetically as a host-species-specificity gene: [PMID:7549480 "Genetic analysis of host
  specificity in the rice blast fungus (Magnaporthe grisea) identified a single gene, PWL2 (for Pathogenicity
  toward Weeping Lovegrass), that exerts a major effect on the ability of this fungus to infect weeping
  lovegrass (Eragrostis curvula)"] and [PMID:7549480 "The PWL2 gene encodes a glycine-rich, hydrophilic protein
  (16 kD) with a putative secretion signal sequence."]
- Deep research report: `PWL2-deep-research-falcon.md` (Edison/Falcon) — flags that Were et al. was a preprint
  at the time; it is now published as PMID:40341381.

## Secretion and localization

- Secreted by invasive hyphae into the biotrophic interfacial complex (BIC), then translocated into the rice
  cytoplasm and moves cell-to-cell: [PMID:20435900 "were translocated into the rice cytoplasm"],
  [PMID:20435900 "continued to accumulate in BICs after IH were growing elsewhere"]. BAS4, an apoplastic
  effector, is not translocated.
- Non-conventional secretion route, distinct from the ER-Golgi route used by apoplastic effectors:
  [PMID:34236677 "secretion of Pwl2 is BFA insensitive and follows a nonconventional secretion pathway that is
  Snare and Exocyst dependent"], [PMID:23774898 "fluorescent cytoplasmic effectors accumulate at BICs following
  photobleaching, and this process is BFA insensitive"].
- Punctate accumulation at the BIC: [PMID:26472068 "These observations also reveal that Pwl2:mCherry is
  localized in BICs as puncta."]; used as the standard symplastic-effector marker [PMID:26472068 "BICs were
  visualized using a fluorescently labeled symplastic effector, Pwl2:mCherry"].
- Host-cell entry confirmed with an NLS-tagged reporter against a rice nuclear marker line: [PMID:31749824
  "oryzae effector PWL2 into host cells."] — the nuclear signal is an artefact of the engineered NLS, so no
  native nuclear location should be annotated.
- Uptake appears to be clathrin-mediated: [PMID:38653755 "demonstrating that PWL2 is also internalized by CME"];
  clathrin inhibitors distort BIC localization [PMID:38722963 "Treatment with CLATHRIN HEAVY CHAIN inhibitor
  ES9–17 results in swollen, irregular localization of Pwl2:mRFP in BICs lacking obvious MEC puncta."]
- Methods chapter devoted to imaging PWL2 translocation: [PMID:30182232 "We describe three complementary assays
  for visualizing M. oryzae effector translocation into the rice cytoplasm and cell-to-cell movement during
  infection."]

## Molecular activity: binding host HMA (HIPP43) proteins

- Crystal structure (1.8 A) of Pwl2 with the rice OsHIPP43 HMA domain; Pwl2 is a MAX effector with an extra
  C-terminal helix/loop: [PMID:38968126 "The crystal structure of Pwl2 bound to OsHIPP43 reveals Pwl2 to be a
  MAX effector, with a C-terminal helical extension and extended loop region."], [PMID:38968126 "Both the MAX
  fold and C-terminal extension are involved in OsHIPP43 binding."]
- Nanomolar affinity by ITC: [PMID:38968126 "OsHIPP43 interacted with Pwl2 with a calculated dissociation
  equilibrium constant (Kd) of 191 nM"]; paralogues Pwl1/Pwl4 bind similarly [PMID:38968126 "Pwl1 and Pwl4
  interacted with OsHIPP43 with similar affinities as Pwl2, with Kd values of 147 and 124 nM, respectively"].
- In planta the barley orthologue HvHIPP43 is bound by Pwl2 (IP-MS, Y2H, co-IP) and displaced from
  plasmodesmata: [PMID:40341381 "Pwl2 binds to the barley heavy metal-binding isoprenylated protein HIPP43,
  which results in HIPP43 displacement from plasmodesmata"].
- Direction of effect on the target is unresolved: Pwl2 may stabilise/accumulate HIPP43 rather than simply
  inactivate it — [PMID:40341381 "It is therefore possible that Pwl2 is able to stabilize HvHIPP43 or increases
  its accumulation, because the mCherry-HvHIPP43 signal is barely detectable in the absence of Pwl2 (Fig."]
  — and HIPP43 overexpression alone suppresses immunity [PMID:40341381 "Strikingly, we observed that both the
  chitin and flg22-induced ROS burst was abolished or reduced in plants expressing HvHIPP43, compared with wild
  type (Fig."]. So "protein sequestering activity" (GO:0140311, "Binding to a protein to prevent it from
  interacting with other partners or to inhibit its localization to the area of the cell or complex where it is
  active") is plausible but not established; I do not assert an MF term.

## Biological process: suppression of host PTI; virulence vs avirulence

- Transgenic plants expressing signal-peptide-less Pwl2 have attenuated PTI: [PMID:40341381 "Furthermore,
  because Pwl2 attenuates the ROS burst in barley transgenic lines"], [PMID:40341381 "attenuated immune
  responses and increased disease susceptibility."]
- Binding is required for both target relocalisation and the virulence contribution: [PMID:40341381 "Finally,
  we show that a Pwl2SNDEYWY mutant unable to interact with HIPP43 fails to displace it from PDs and cannot
  complement the reduced virulence of Δpwl2 mutants."]
- Overall conclusion: [PMID:40341381 "Pwl2 is a virulence factor that suppresses host immunity by perturbing the
  plasmodesmatal deployment of HIPP43"]. PWL2 expression is Pmk1-dependent and occurs at plasmodesmata-containing
  pit fields [PMID:40341381 "the Pmk1 MAP kinase regulates PWL2 expression during the cell-to-cell movement of M.
  oryzae at plasmodesmata-containing pit fields"].
- Deletion of all three Guy11 copies: [PMID:40341381 "Targeted deletion of 3 PWL2 copies in M. oryzae resulted in
  a Δpwl2 mutant showing gain of virulence toward weeping lovegrass and barley Mla3 lines, but reduced blast
  disease severity on susceptible host plants."] — i.e. one molecule, two opposite outcomes depending on host
  recognition.
- Recognition by a barley NLR: [PMID:37820736 "the recognized effector from M. oryzae is Pathogenicity toward
  Weeping Lovegrass 2 (Pwl2), a host range determinant factor that prevents M. oryzae from infecting weeping
  lovegrass (Eragrostis curvula)"].
- Host-range role also demonstrated in finger-millet blast isolates from eastern Africa: [PMID:37245238
  "Resulting transformants harboring either gene gained varying degrees of avirulence on"] (PubMed abstract text
  is mangled by lost italic gene names; the point is that PWL1/PWL2 transformants of a Ugandan isolate gained
  avirulence on weeping lovegrass while remaining virulent on finger millet).
- Biotechnological consequence: an engineered rice NLR with the OsHIPP43 HMA domain replacing Pik-1's integrated
  HMA recognises Pwl2 and other PWL alleles [PMID:38968126 "(A and B) Cell death assays showing Pwl2, Pwl2-2,
  and Pwl2-3, but not AVR-PikD, are recognized by the chimeric Pikm-1OsHIPP43/Pikp-2 receptor."]

## Curation decisions

- All 15 GOA rows are cellular-component rows (extracellular region, host cell cytoplasm), each well supported
  for the secreted and host-translocated pools respectively; all accepted. Several of the cited papers are
  methods chapters or resource papers that use PWL2 as a reporter rather than studying it; these are weaker
  sources but not wrong, so ACCEPT with a note rather than REMOVE (CLAUDE.md: do not overrule curators).
- GOA has **no** process or function annotation. One NEW process annotation is proposed,
  `GO:0052034 effector-mediated suppression of host pattern-triggered immunity` (symbiont-side, as the project
  requires). Participation test: Pwl2 itself binds and relocalises the host target, and a binding-dead variant
  loses the virulence contribution — the effector does the work. Comparator check: other PTI-suppressing
  secreted effectors carry this branch (M. oryzae Slp1 and C. fulvum Ecp6 reviews use GO:0140423, a child of
  GO:0052034). The parent, not the "signaling" child GO:0140423, is used because whether HIPP43 acts in the
  signalling chain is explicitly left open by the authors.
- No MF term is asserted: binding to host HIPP43 is firmly established, but "protein binding" is uninformative
  per CLAUDE.md and the mechanistic interpretation (sequestration vs stabilisation/co-option) is unresolved.
  Raised in `suggested_questions` instead.
- Avirulence/host-range activity is the host's recognition of Pwl2; no symbiont-side GO term describes "being
  recognised", so nothing is annotated for it. Noted as a question.
