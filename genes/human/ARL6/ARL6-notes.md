# ARL6 (BBS3) review notes

UniProt: Q9H0F7. ADP-ribosylation factor-like protein 6 / Bardet-Biedl syndrome 3 protein.
186 aa, small GTPase, Arf family (Ras superfamily). Gene on chr 3. HGNC:13210.

## Core identity
- Arf-like small GTPase. Belongs to small GTPase superfamily, Arf family (UniProt SIMILARITY).
- GTP/GDP nucleotide switch. Crystal structure of GTP-bound ARL6 (PDB 2H57) solved
  [PMID:20207729 "we present the crystal structure of ARL6 ... structure of GTP-bound ARL6/BBS3"].
- P-loop / nucleotide binding residues mapped (UniProt BINDING 24-31, 50, 69-73, 130-133, 164;
  Mg2+ at 31, 50). BBS variants T31M/T31R, G169A, L170W abrogate or alter GTP binding and
  increase proteasomal degradation [PMID:19236846; PMID:20207729; PMID:15314642].
- Core MF: GTP binding (GO:0005525) and GTPase activity (GO:0003924). Both are core for this gene.

## Central function: membrane-targeting switch for the BBSome
- ARL6/BBS3 is NOT a structural subunit of the BBSome
  [PMID:20603001 "the small Arf-like GTPase Arl6 which is not part of the BBSome"]
  [PMID:22139371 "BBS3 (ARL6) ... is not part of the BBSome complex"].
- The BBSome is the major effector of GTP-bound Arl6
  [PMID:20603001 "The BBSome is the major effector of the Arf-like GTPase Arl6/BBS3"].
- GTP-bound Arl6 recruits the BBSome to ciliary membrane; Arl6 and BBSome colocalize at ciliary
  punctae interdependently [PMID:20603001 "the BBSome and GTP-bound Arl6 colocalize at ciliary
  punctae in an interdependent manner"]. Arl6 binds the N-terminus of BBS1
  [PMID:20603001 "BBS1 was the BBSome subunit most efficiently captured by Arl6GTP ... mapping the
  interaction domain to the N-terminus of BBS1"].
- Arl6 GTP loading nucleates BBSome polymerization into a coat on membranes
  [PMID:20603001 "Arl6(GTP)-mediated recruitment of the BBSome to synthetic liposomes produces
  distinct patches of polymerized coat apposed onto the lipid bilayer"]. Reconstituted from purified
  components: only GTP-bound Arl6 needed to recruit BBSome to liposomes.
- Arl6 binds membranes via an N-terminal amphipathic helix exposed upon GTP binding (Arf/Sar1-like)
  [PMID:20603001 "Arl6 conforms to the Arf1/Sar1 paradigm and interacts with membranes through its
  N-terminal amphipathic helix when GTP-bound"]; multi-phosphorylated PIPs (e.g. PI(3,4)P2) and acidic
  phospholipids synergize for BBSome recruitment (basis for phospholipid binding annotation).
  Note: in this study Arl6 was reported NOT myristoylated for the recombinant prep, but UniProt LIPID
  feature annotates N-myristoyl glycine at residue 2 (ECO:0000255, by similarity).
- Targeting requires GTP binding but not GTP hydrolysis: T31R (GTP-deficient) absent from cilia;
  Q73L (hydrolysis-deficient) recruits MORE BBSome [PMID:20603001].
- BBSome recognizes ciliary targeting signal (CTS) of cargo e.g. SSTR3; ARL6 depletion removes SSTR3
  from cilia [PMID:20603001].

## Localization
- Cilium / cilium membrane (peripheral membrane protein, cytoplasmic side). Endogenous Arl6 stains
  cilia; lost on siRNA [PMID:20603001]. IDA cilium also from MGI [PMID:22139371] and HPA.
- Ring-like localization at distal end of basal bodies / ciliary gate
  [PMID:20207729 "unique ring-like localization at the distal end of basal bodies, in proximity to the
  so-called ciliary gate"]. Supports basal body / ciliary gate localization.
- Punctae flanking the axoneme (membrane-associated patches) [PMID:20603001]. Basis for axoneme-area
  annotations, though Arl6 is membrane-associated, not a structural axoneme/axonemal-microtubule component.
- NOT cilium (GO:0005929) IDA, PMID:17646400: this is a Rab-GTPase overexpression screen (Yoshimura
  et al.) where only Rab8a was enriched at cilia; ARL6 was tested and not enriched in that particular
  assay. This negative result is in a specific overexpression context and is contradicted by multiple
  direct endogenous-localization studies. Keep the NOT as recorded by the curator (assay-specific) but
  it does not reflect the consensus biology.

## Biological processes
- Protein localization to cilium / BBSome-mediated cargo trafficking to cilia (core downstream role).
  IMP in mouse Bbs3-/- : disrupts ciliary localization of MCHR1 and Smoothened retrograde transport
  [PMID:22139371].
- Cilium assembly / length: GDP- or GTP-locked ARL6 over-expression influences cilium length and
  abundance [PMID:20207729 "Overproduction of GDP- or GTP-locked variants of ARL6/BBS3 in vivo
  influences primary cilium length and abundance"]. ARL6 is a trafficking switch rather than a core
  ciliogenesis/axoneme-assembly factor; cilia still form in its absence (BBSome cargo defects dominate).
- Wnt signaling: ARL6/BBS3 modulates Wnt; signaling function lost in BBS point mutants
  [PMID:20207729 "ARL6/BBS3 also modulates Wnt signaling ... this signaling function is lost in ARL6
  variants containing BBS-associated point mutations"]. IMP-supported but pleiotropic / non-core.
- Hedgehog (Smoothened) trafficking: with BBSome and LZTFL1 controls SMO ciliary trafficking
  [PMID:22072986]; affects SMO retrograde transport [PMID:22139371]. (No SHH GO term currently annotated.)

## IFT27 / BBSome exit
- IFT27/RABL4 binds nucleotide-free ARL6 and prevents its aggregation; promotes ARL6 activation,
  BBSome coat assembly and BBSome+cargo EXIT from cilia
  [PMID:25443296 "IFT27 directly interacts with the nucleotide-free form of ARL6 ... IFT27 prevents
  aggregation of nucleotide-free ARL6 ... promote ARL6 activation, BBSome coat assembly, and
  subsequent ciliary exit"]. Basis for the GOA IPI protein-binding annotation (WITH IFT27, Q9BW83).

## Disease
- Bardet-Biedl syndrome 3 (BBS3, MIM 600151), autosomal recessive [PMID:15258860; PMID:15314642].
- Retinitis pigmentosa 55 (RP55, MIM 613575), variant A89V [PMID:19956407].
- Isoform 2 (BBS3L) is vision-specific / required for proper retinal function (UniProt; PMID:20333246).

## GOA IPI WITH/FROM cross-checks (citation correctness)
- PMID:20603001 IPI WITH BBS1 (Q8NFJ9): correct — Arl6GTP binds BBS1 N-terminus. VERIFIED.
- PMID:22139371 IPI WITH BBS1 (Q8NFJ9): correct — endogenous BBS3-BBSome physical interaction. VERIFIED.
- PMID:25443296 IPI WITH IFT27 (Q9BW83): correct — ARL6 binds nucleotide-free IFT27. VERIFIED.

## Term-by-term reasoning summary
- GTP binding (GO:0005525), GTPase activity (GO:0003924): ACCEPT, core MF.
- protein binding (GO:0005515) IPI x3: uninformative bare term; KEEP_AS_NON_CORE (real interactions,
  but "protein binding" not informative; effector/BBSome-recruitment captured elsewhere).
- protein localization to cilium (GO:0061512): core BP. ACCEPT the experimental IMP (PMID:22139371);
  IBA/IEA duplicates ACCEPT/KEEP_AS_NON_CORE.
- cilium (GO:0005929) IDA x2: ACCEPT. ciliary tip (GO:0097542) IDA: ACCEPT (HPA).
- cilium membrane is the most accurate compartment but not currently in GOA list.
- axoneme (GO:0005930) / axonemal microtubule (GO:0005879): ARL6 is membrane-patch associated near the
  axoneme, not a structural axoneme component. KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- membrane coat (GO:0030117) part_of, ISS: the coat is the BBSome; ARL6 recruits it but is not itself a
  structural coat subunit. MARK_AS_OVER_ANNOTATED.
- protein polymerization (GO:0051258) ISS: ARL6 nucleates BBSome coat polymerization (it does not itself
  polymerize). KEEP_AS_NON_CORE (defensible as "involved_in" the polymerization of the coat).
- phospholipid binding (GO:0005543) ISS: supported — GTP-Arl6 + acidic PIPs synergize. KEEP_AS_NON_CORE.
- protein targeting to membrane (GO:0006612) ISS: GO:0006612 is SRP-dependent targeting to ER membrane;
  WRONG specific term for ARL6's role (it recruits BBSome to ciliary membrane). MARK_AS_OVER_ANNOTATED.
- cilium assembly (GO:0060271): pleiotropic/modulatory, not core ciliogenesis. KEEP_AS_NON_CORE.
- Wnt signaling (GO:0016055) IMP: pleiotropic, KEEP_AS_NON_CORE.
- intracellular protein transport (GO:0006886) IBA, vesicle-mediated transport: general but consistent;
  KEEP_AS_NON_CORE.
- determination of left/right symmetry (GO:0007368) ISS, melanosome transport (GO:0032402) ISS,
  fat cell differentiation (GO:0045444) IEA, protein localization to non-motile cilium (GO:0097499) IEA:
  weak electronic/ISS transfers; KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED (melanosome transport is a
  questionable ortholog transfer; left/right symmetry plausible ciliopathy phenotype but indirect).
- cytoplasm/cytosol/membrane (GO:0005737/0005829/0016020): ACCEPT/KEEP_AS_NON_CORE (ARL6 cycles between
  cytosol and membrane).
- extracellular exosome (GO:0070062) HDA: high-throughput proteomics catch-all; MARK_AS_OVER_ANNOTATED.
- plasma membrane (GO:0005886) TAS Reactome x2: ARL6 acts at ciliary/plasma membrane interface; the
  GTP-bound form is on membranes. KEEP_AS_NON_CORE.
- NOT cilium (GO:0005929) PMID:17646400: keep negated annotation (assay-specific); ACCEPT as recorded.
