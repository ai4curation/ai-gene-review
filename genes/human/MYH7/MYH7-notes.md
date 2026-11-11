# MYH7 (human, P12883) curation notes

## Gene identity

MYH7 encodes myosin-7, the slow/beta-cardiac myosin heavy chain (beta-MHC, MyHC-slow), a
1935-residue class II sarcomeric myosin. Domain layout from UniProt: N-terminal SH3-like
domain (32-81), motor domain (85-778) with the ATP-binding P-loop (178-185) and actin-binding
regions (655-677, 757-771), an IQ motif/lever arm (781-810) that binds the essential and
regulatory light chains, and a coiled-coil rod (839-1935) with four skip residues.

- Expression: main MyHC of ventricles and of slow type 1 skeletal fibres
  [PMID:14520662 "MYH7 encodes the slow/beta-cardiac myosin heavy chain (MyHC), which is the
  main MyHC isoform in slow, oxidative, type 1 muscle fibers of skeletal muscle"; "It is also the
  major MyHC isoform of cardiac ventricles"]; expressed in heart and skeletal muscle
  [PMID:3021460 "we have found by the same technique that it is also expressed in human skeletal
  muscle"]. Ventricles are almost exclusively beta-MHC; atria mix alpha and beta
  [PMID:15621050 "In ventricular tissue, the beta-MHC isoform predominates, whereas in atrial
  tissue a variable mixture of alpha- and beta-MHC is found"].
- Complex: hexamer of 2 heavy chains, 2 essential and 2 regulatory light chains (UniProt SUBUNIT).

## Molecular function: actin-activated ATPase motor

- Recombinant human beta-cardiac S1 has ATPase activity, velocity and intrinsic force
  [PMID:23798412 "The major change in the R453C human β-cardiac subfragment 1 is a 50% increase in
  the intrinsic force of the motor compared with wild type"].
- Patient beta-myosin moves actin in motility assays [PMID:8514894 "Mutant beta-myosin, also shown
  to be present in skeletal muscle by Western blot analysis, translocated actin filaments slower
  than normal controls in an in vitro motility assay"].
- Head = ATPase + actin binding; rod = filament incorporation [PMID:19336582 "Although the head
  region is responsible for myosin's ATPase and actin binding properties, the rod region functions
  to incorporate myosin into bipolar thick filaments through charge based interactions between
  adjacent rods"].
- Beta-MHC is the slow, economical isoform; ATP use and force kinetics track beta/alpha ratio
  [PMID:15621050 "Significant linear correlations were found between MHC isoform composition, ATP
  consumption and rate of force redevelopment"].
- Motor domain structure with omecamtiv mecarbil [PMID:26246073].

## Thick filament assembly (rod)

- Skip residues guide thick filament assembly [PMID:26150528 "The rod of sarcomeric myosins directs
  thick filament assembly and is characterized by the insertion of four skip residues that introduce
  discontinuities in the coiled-coil heptad repeats"].
- LMM paracrystals reproduce native thick filament spacing [PMID:19336582 "corresponds well to the
  14.3 nm axial spacing of full-length β-MyHC found in bipolar thick filaments"].

## Regulation: interacting-heads motif / super-relaxed state

- Purified human beta-cardiac myosin partly occupies an SRX [PMID:30104387 "Here we show that purified
  human β-cardiac myosin exists partly in an SRX and may in part correspond to a folded-back
  conformation of myosin heads observed in muscle fibers around the thick filament backbone"];
  HCM mutations destabilize, mavacamten promotes it [PMID:30104387 "Mutations that cause
  hypertrophic cardiomyopathy destabilize this state, while the small molecule mavacamten promotes
  it"].
- S2- and MyBP-C-dependent sequestration [PMID:28481356 "we show that both S2 and MyBP-C bind to S1
  and that phosphorylation of either S1 or MyBP-C weakens these interactions"].
- HCM mutations at IHM interfaces free heads [PMID:31213605 "lead to a significant increase in the
  number of heads functionally accessible for interaction with actin"].
- Cryo-EM IHM structure [PMID:37258552 "To save energy and precisely regulate cardiac contractility,
  cardiac muscle myosin heads are sequestered in an 'off' state that can be converted to an 'on'
  state when exertion is increased"].
- No GO term exists for this regulated state; raised as a suggested question rather than forced
  onto an ill-fitting term.

## Disease (context only, not GO annotations)

- HCM: ~30% of genotyped cases [PMID:15856146]; head mutations.
- DCM [PMID:11106718 "Cardiac beta-myosin heavy-chain missense mutations (Ser532Pro and Phe764Leu)
  ... caused early-onset ventricular dilatation"].
- LVNC [PMID:18506004 "MYH7 mutations segregated with the disease in 4 autosomal dominant LVNC
  kindreds"].
- Laing distal myopathy, distal rod [PMID:15322983 "All five mutations are predicted, by in silico
  analysis, to locally disrupt the ability of the myosin tail to form the coiled coil, which is its
  normal structure"].
- Myosin storage myopathy, LMM [PMID:14520662; PMID:16684601; PMID:17336526; recessive form
  PMID:25666907; PMID:19336582].

## GOA review decisions (48 rows)

Totals: ACCEPT 14, MODIFY 22, REMOVE 7, MARK_AS_OVER_ANNOTATED 5.

- ACCEPT (14): microfilament motor activity x4, ATP binding, actin filament binding x2, muscle
  myosin complex x2, muscle filament sliding x3, cardiac muscle contraction x2.
- MODIFY (22): general CC terms (cytoplasm, myofibril, sarcomere, supramolecular fiber, myosin filament)
  -> GO:0005863 striated muscle myosin thick filament; myosin complex / myosin II complex ->
  GO:0005859 muscle myosin complex; cytoskeletal motor activity -> microfilament motor activity;
  muscle/striated muscle contraction -> cardiac muscle contraction (and slow-twitch skeletal muscle
  fiber contraction where generic); skeletal muscle contraction and the two "regulation of ... force/
  slow-twitch contraction" rows -> GO:0031444 slow-twitch skeletal muscle fiber contraction (the
  motor executes, it does not regulate, contraction); regulation of the force of heart contraction
  -> cardiac muscle contraction.
- REMOVE: stress fiber (IEA; non-muscle structure), Z disc (IEA; thick filaments are not at the Z
  disc), regulation of heart rate (IDA from PMID:15621050 - the paper measured rate of force
  redevelopment in skinned cells, a cross-bridge rate, not heart rate), and four generic protein
  binding IPI rows (MYBPC3, LRRC39, KXD1, CLVS2).
- MARK_AS_OVER_ANNOTATED: adult heart development (IBA, IMP), ventricular cardiac muscle tissue
  morphogenesis (IMP x2) - disease phenotypes (hypertrophy, non-compaction) turned into process
  terms; necessity, not participation. ATP metabolic process (IDA) - ATP consumption is the motor
  activity itself.
- NEW (1): GO:0008307 structural constituent of muscle (rod builds the thick-filament backbone).
  Comparator check via QuickGO: MYH8, MYH11, Drosophila Mhc, C. elegans unc-54 and myo-1 already
  carry the term, as do MYBPC3 and the myomesins. Considered and rejected: NEW striated muscle
  myosin thick filament assembly (GO:0071688), because QuickGO shows it is annotated to assembly
  factors (unc-45, unc-89, fln) and not to myosin heavy chains; raised as a suggested question.
- PMID:12933792 (TAS for myosin complex) is about alpha-MHC (MYH6) regulation by PUR proteins; noted
  as MISCITED in reference_review, term modified rather than removed since the claim is true.

## Deep research

- Falcon (`just deep-research human MYH7 --provider falcon`) failed: Edison client
  "Exception: Failed to authenticate".
- OpenScientist fallback succeeded (`MYH7-deep-research-openscientist.md`, 28 citations, ~13 min).
  Its picture matches this review: actin-activated ATPase motor plus thick-filament building block,
  ventricular and type 1 slow fibre expression, IHM/SRX regulation, HCM mutations shifting heads ON.
  Additional leads it reports, not independently verified here and not used as annotation evidence:
  DCM variant E525K stabilizing the IHM/SRX (PMID:42395535); alpha:beta MHC ~1:9 in human ventricle
  with beta-S1 slower hydrolysis and ADP release than alpha-S1 (PMID:22349210); miR-208b hosted in a
  MYH7 intron (PMID:19726871). Its caveat that SRX and IHM may not be strictly identical
  (PMID:40118457) is why core_functions describe them as 'corresponding' rather than identical.
