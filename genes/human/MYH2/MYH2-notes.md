# MYH2 (human, Q9UKX2) curation notes

## Gene identity

MYH2 encodes myosin-2, the fast type IIa skeletal muscle myosin heavy chain (MyHC-IIa,
MyHC-2a), a 1941-residue class II sarcomeric myosin in the chromosome 17p13 skeletal MyHC
cluster. UniProt layout: N-terminal SH3-like domain (33-82), motor domain (86-784) with the
ATP-binding P-loop (179-186) and actin-binding regions (661-683, 763-777), an IQ motif/lever
arm (787-816), and a coiled-coil rod (845-1941). It is a skeletal isoform, not cardiac.

- Expression: major MyHC of fast, oxidative type 2A fibres [PMID:22918376 "MyHC IIa (MYH2) is
  expressed in fast, type 2A muscle fibers"]; [PMID:11114175 "since MyHC-IIa is the major
  isoform in type 2A fibers"].
- Complex: hexamer of 2 heavy chains, 2 essential and 2 regulatory light chains
  [file:human/MYH2/MYH2-uniprot.txt "Muscle myosin is a hexameric protein that consists of 2
  heavy chain subunits (MHC), 2 alkali light chain subunits (MLC) and 2 regulatory light chain
  subunits (MLC-2)"].
- Full-length human coding sequence first reported with the rest of the sarcomeric family
  [PMID:10388558 "we present new full-length coding sequences corresponding to four additional
  human genes: MyHC-IIb, MyHC-extraocular, MyHC-IIa and MyHC-IIx/d"].

## Molecular function: actin-activated ATPase motor

- Recombinant human skeletal isoforms, including IIa, expressed in muscle cells and assayed
  [PMID:20080549 "In this study we describe a mammalian muscle cell expression system and the
  functional analysis of all six recombinant human type II skeletal muscle myosin isoforms"];
  IIa is the slowest adult-fast isoform [PMID:20080549 "MyHC-IIb displays the highest maximal
  actin-activated ATPase rate, and the rates for the adult-fast isoforms follow the order from
  fastest to slowest: MyHC-IIb > MyHC-IId > MyHC-IIa"].
- Transient kinetics: ADP affinity of actomyosin distinguishes the fast isoforms
  [PMID:23908353 "The three fast muscle myosins have K(AD) values of 118, 80, and 55"]
  (IId, IIa, IIb respectively).
- E706K (SH1 helix) severely impairs motor function in patient fibres [PMID:17005402 "A dramatic
  impairment in the function of the IIa MyHC isoform was observed at the motor protein level."].
- Single human fibres typed by MHC isoform, including pure IIA fibres, used to relate Vmax to
  isoform [PMID:8145163 "Types I, IIA and IIB MHCs were resolved from single fibre segments"].

## Thick filament (rod) and super-relaxed state

- MyHC forms the thick filament backbone [PMID:22918376 "The myosin heavy chain (MyHC) is the
  molecular motor of muscle and forms the backbone of the sarcomere thick filaments."].
- MYH2 LMM forms filaments; L1870P gives shorter, narrower filaments [PMID:37788100 "The MYH2
  proline mutant (L1870P) did form filaments from homogeneous mixtures, which were shorter and
  narrower than WT"].
- LMM variants reduce the super-relaxed state in patient type IIA fibres [PMID:37788100
  "Similarly, P1 was increased (P2 was decreased) in myofibers expressing type IIA MHC from
  patients with MYH2 mutations compared with controls or patients with MYH7 mutations"], with
  contractility unaffected.
- Truncating MYH2 variants: altered relaxed-state ATP demand, faster kinetics, lower force
  [PMID:36745529 "MYH2 truncating mutations impact myosin presence/functionality in human adult
  mature myofibers by disrupting the ATPase activity and actomyosin complex"].

## Disease (context only, not converted to GO terms)

- Dominant E706K myopathy with contractures, ophthalmoplegia, rimmed vacuoles [PMID:11114175
  "which is located in a highly conserved region of the motor domain, the so-called SH1 helix
  region"]; mutant expression increases with age [PMID:11889243].
- S2 rod variants V970I, L1061V [PMID:15741996].
- Recessive truncating variants abolish IIa protein and type 2A fibres [PMID:20418530 "We have
  identified the first patients lacking fast type 2A muscle fibres, caused by total absence of
  fast myosin heavy chain IIa protein due to truncating mutations of the corresponding gene
  MYH2"]; recessive missense variants too [PMID:24193343]; [PMID:23388406].
- C. elegans unc-54 E710K model: paralysis but thick filaments still form, i.e. functional not
  structural defect [PMID:16130113].
- 20418530 says the isoform is "necessary for normal muscle development and function"; this is
  necessity evidence and was not converted into a developmental process term (consistent with
  MYH7, where cardiomyopathy phenotypes were not turned into heart development terms).

## Annotation review decisions (27 GOA rows + 1 NEW)

- Tally: ACCEPT 8, MODIFY 14, REMOVE 4, TOO_GENERAL 1 (27 GOA rows), plus 1 NEW.
- ACCEPT (8): microfilament motor activity (IBA, TAS), ATP binding (IEA), muscle myosin complex
  (NAS, TAS), muscle filament sliding (NAS), actin filament binding (IBA, IEA).
- MODIFY (14): general location terms (cytoplasm IBA, myofibril IDA/IEA, sarcomere NAS, myosin
  filament IBA, contractile muscle fiber IEA) -> GO:0005863 striated muscle myosin thick
  filament, as for MYH7; myosin complex / myosin II complex -> GO:0005859 muscle myosin complex;
  cytoskeletal motor activity -> GO:0000146; muscle contraction (IBA, IDA, TAS) and system
  process -> GO:0031443 fast-twitch skeletal muscle fiber contraction (counterpart of MYH7's
  slow-twitch choice).
- TOO_GENERAL: protein-containing complex (GO_REF:0000054), entailed by muscle myosin complex.
- REMOVE:
  - cell-cell junction (IMP, PMID:25753039): full text is endothelial HDMEC "myosin IIA", i.e.
    non-muscle myosin IIA (MYH9). Name collision with MyHC-IIa; the reference is on the MYH2
    GOA file but not on MYH9's. [PMID:25753039 "In control HDMEC, β-actin and myosin IIA formed a
    junctional belt"]; [PMID:22918376 "The non-muscle conventional class II MyHC genes MYH9 and
    MYH10 encode the non-muscle myosins IIA (MYHIIA) and IIB (MYHIIB)"].
  - cytosol (TAS, two Reactome phagocytosis events): non-muscle myosin II reactions with every
    class II heavy chain bundled in [Reactome:R-HSA-2029476 "Nonmuscle myosin II, is a motor
    protein known to generate intracellular contractile forces and tension by associating with
    F-actin."].
  - protein binding (IPI, HGAL/GCSAM): uninformative; lymphocyte myosin II is presumably
    non-muscle.
- NEW: GO:0008307 structural constituent of muscle (PMID:37788100). Comparator check via QuickGO
  (2026-10-16): MYH8 (NAS, PMID:2715179) and MYH11 (IMP, PMID:16444274) carry GO:0008307; MYH7
  review proposes it as NEW.

## Deep research

- Provider: openscientist (falcon not used: Edison auth failing on 2026-10-16). The run
  completed (~23 min) and wrote `MYH2-deep-research-openscientist.md` plus artifacts.
- The report agrees with the review: motor head = actin-activated ATPase, rod = thick-filament
  self-assembly domain, location = A-band thick filament of type 2A fibres
  [file:human/MYH2/MYH2-deep-research-openscientist.md "Its long C-terminal coiled-coil tail is a
  structural element that dimerizes and self-assembles into the thick-filament backbone."].
- Leads from the report not used as evidence (not fetched/verified here): F516V relay-loop
  variant and Q1111* tail truncation with filamentous tangles (PMID:33926564); dominant splice
  variant deleting residues 1860-1891 in the assembly region (PMID:36380287). Its claim that
  ophthalmoplegia shows extraocular muscle is especially MYH2-dependent is an inference, kept
  as a suggested question rather than a statement.
