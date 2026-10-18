# cul1 (Pcu1, SPAC17G6.12, UniProt O13790) - curation notes

Fission-yeast cullin-1, the scaffold of SCF (Skp1-Cul1-F-box) ubiquitin ligases; orthologue of
budding-yeast Cdc53 and human CUL1. Not to be confused with the other S. pombe cullins Pcu3/Cul3
(stress pathway) and Pcu4/Cul4 (Ddb1-associated; lacks the Skp1-binding N-terminus).

## Sources used

- UniProt O13790 (Swiss-Prot; FUNCTION, SUBUNIT, PTM Lys713 neddylation, K713R mutagenesis).
- PomBase gene page (API): product "cullin 1", deletion viability "inviable"; the GO:0000822 EXP row
  has no annotation extension; the same PMID gives csn2 the same term.
- Deep research: `cul1-deep-research-falcon.md` (Falcon/Edison). Used for orientation; its Wee1
  (Qiu et al. 2018), Zip1 (Harrison et al. 2005) and COP9/Ubp12 (Zhou et al. 2001, 2003) modules cite
  real papers that are not in the local publication cache and were not independently verified.
- Cached publications: PMID:10880460, 11809834, 12167173, 17016471 (abstract + intro only), 25165823
  (full text); PMID:9990507, 15147268, 16823372, 32047038 (abstract only). For PMID:32047038 the
  PMC HTML (PMC7049131) was fetched directly to check the S. pombe experiment.

## Biology (with provenance)

**SCF composition and scaffold role.** Cullin-1 was identified as the common scaffold of the
Pop1/Pop2 SCF complexes [PMID:9990507 "SCF also contains cullin-1 as a universal scaffold and each
cullin member plays a distinct biological role"]. At endogenous levels, Pip1 (Rbx1), Pop1 and Pop2
antisera co-precipitate all five SCF-Pop subunits, and gel filtration places them in a ~500 kDa
complex [PMID:12167173 "co-elution of Pip1p with Pop1p, Pop2p, Pcu1p, and Psh1p in a high molecular
weight complex of approximately 500 kDa, which we refer to as SCFPop1p-Pop2p"]. The core
Pip1/Pcu1/Psh1 does not vary through the cell cycle [PMID:12167173 "The composition of the core
complex Pip1p/Pcu1p/Psh1p did not undergo major variations during the cell cycle"]. Homo-oligomeric
SCF-Pop1 and SCF-Pop2 also exist [PMID:12167173 "both F-box proteins, in the absence of their
respective heterooligomerization partner, could individually bind to Pip1p in complexes that also
contained Psh1p and Pcu1p"]. Other receptors shown to assemble on Pcu1: Pof3 [PMID:11809834 "Pof3
forms a complex with Skp1 and Pcu1"], Pof14 [PMID:17016471 "Pof14, which forms a canonical, F-box
dependent SCF"], Fbh1 [PMID:25165823 "we separately purified Fbh1-Skp1 and Pcu1 (fission yeast
Cullin1)-Rbx1 complexes, mixed them to form the SpSCFFbh1 complex"]. Skp1-ts mutants keep the
Pcu1 contact while losing F-box contacts [PMID:15147268 "This systematic analysis showed that ts
Skp1 retains binding to Pcu1."].

**Ligase activity of Cul1-based SCFs.** Immunopurified SCF-Pop1/Pop2 polyubiquitylates
CDK-phosphorylated Rum1 in vitro [PMID:12167173 "SCFPop1p-Pop2p complexes immunopurified with
Pip1p antibodies converted a small portion of phosphorylated Rum1p into high molecular weight
species"]. Reconstituted SCF-Fbh1 (Pcu1-Rbx1 + Fbh1-Skp1) ubiquitinates Rad51 with Ubc4 as E2
[PMID:25165823 "Rad51 was ubiquitinated in an Ubc4- and SCFFbh1-dependent manner"], and Rad51 is
cleared in stationary phase in an F-box-dependent way [PMID:25165823 "Fbh1 regulates the level of
Rad51 protein in stationary phase, which is dependent on its F-box motif"].

**Neddylation.** Pcu1 is modified by NEDD8/Ned8 on Lys713; the SCF-assembled pool is essentially
fully modified [PMID:10880460 "Pcu1 assembled on SCF ubiquitin-ligase was completely modified by
NEDD8."; "Pcu1 assembled into the SCF Pop1 complex is modified preferentially by NEDD8"]. K713R
still enters SCF-Pop1 and a ~400 kDa complex but cannot complement deletion [PMID:10880460 "Pcu1
K713R defective for NEDD8 conjugation lost the ability to complement lethality due to pcu1
deletion."], and its overexpression stabilises Rum1 and delays cells in G2 [PMID:10880460 "it was
stabilized greatly by overexpression of Pcu1 K713R"]. Conclusion of that paper: [PMID:10880460
"covalent modification of Pcu1 by NEDD8 is essential for the function of SCF Ub-ligase in fission
yeast"]. Pof3 binds both modified and unmodified Pcu1, whereas Pop1 binds only the modified form
[PMID:11809834 "Pcu1, unmodified and modified by NEDD8, are capable of forming a complex with Pof3"].

**Essentiality.** pcu1 deletion is lethal and stays lethal without rum1 [PMID:10880460 "we found
that pcu1 deletion is still lethal in a rum1 deletion background"]; PomBase: inviable.

**Localisation.** GFP-Pcu1 (low-level expression) is in both cytoplasm and nucleus; Pop1 is
nuclear, Pop2 in both [PMID:12167173 "While Pip1p, Psh1p, Pcu1p, and Pop2p were present in both
the cytoplasm and the nucleus, surprisingly, GFP-Pop1p was largely restricted to the nucleus"].
The ORFeome YFP screen scored Cul1 as cytoplasmic (UniProt SUBCELLULAR LOCATION from
PMID:16823372).

**IP6 and the COP9 signalosome (PMID:32047038).** Abstract: "IP6 binds to a cognate pocket formed
by conserved lysine residues from CSN2 and Rbx1/Roc1". The S. pombe experiment (PMC full text,
Fig. 5G): myc-Cul1 and TAP-Csn2 tagged at their endogenous loci co-immunoprecipitate in wild type
but not in an ipk1 (IP6 synthase) deletion; IP6 also stimulates recombinant CSN2 binding to
Cul1-5 in vitro. So the fission-yeast data show IP6-dependent Cul1-Csn2 engagement, with the
IP6-coordinating residues on Rbx1 and Csn2, not on the cullin.

## Curation decisions

- All 26 GOA rows reviewed; none PENDING.
- **GO:0160072 ubiquitin ligase complex scaffold activity (IBA)** - ACCEPT; the defining MF and the
  first core function.
- **Seven GO:0005515 protein binding IPI rows** (Pof3, Pop2 x2, Skp1 x2, Pof14, Fbh1) - MODIFY to
  GO:0160072, following the repository protein-binding policy and the human CUL1 review. Each
  paper shows SCF assembly on the cullin (Fbh1 paper: reconstitution of an active E3 from
  Pcu1-Rbx1 + Fbh1-Skp1). No process terms were transferred from the Pof14 paper because its
  point is that Pof14's stress function is SCF-independent.
- **GO:0000822 inositol hexakisphosphate binding (EXP, PMID:32047038)** - MARK_AS_OVER_ANNOTATED.
  The abstract places the IP6 pocket on CSN2 and Rbx1; the S. pombe assay is an ipk1-dependent
  Cul1-Csn2 co-IP. Cul1 is a component of an IP6-bridged CRL-CSN complex, but IP6 binding is not
  a molecular function of the cullin. Not REMOVE, because the annotation reflects a real
  IP6-dependent interaction of the Cul1-containing complex and the curator read the full text;
  raised as a suggested question for PomBase.
- **IBA rows** (nucleus, protein ubiquitination, SCF complex, SCF-dependent catabolic process,
  ubiquitin protein ligase binding, scaffold activity) - all ACCEPT; the target's own PomBase
  entry in WITH/FROM is expected, not circular.
- **IEA rows** (ARBA, InterPro, UniPathway, UniProt-SubCell) - ACCEPT as correct
  parent/redundant statements.
- **Localisation** - nucleus (IBA), cytoplasm (IEA), cytosol (HDA) all ACCEPT; both compartments
  are supported by imaging, nucleus is where the characterised substrates are.
- **G1/S transition (GO:0000082)** was considered for core_functions (as in the CDC53 exemplar)
  but not added and not proposed as NEW: the comparator check on QuickGO shows that in S. pombe
  the term sits on Cdc2, the cyclins, Res1/Res2/Cdc10 etc. (mostly IBA), that PomBase gives Pop1
  the regulation term GO:1900087 (IMP), and that Pop2, Skp1 and Cul1 carry no G1/S term - a
  convention, not an oversight. Recorded as a suggested question instead.
- No history record was written because this task was restricted to `genes/SCHPO/cul1/`; one
  should be scaffolded with `just new-history` when the PR is made.
