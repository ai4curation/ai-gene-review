# SKP2 (human, UniProt Q13309) — curation notes

## Identity and architecture

SKP2 (FBXL1, p45^SKP2, cyclin-A/CDK2-associated protein p45) is a ~45 kDa F-box/leucine-rich-repeat
(FBXL-family) protein. UniProt Q13309 features an F-box domain at 95–137 and ten LRRs (138–385).
The F-box binds SKP1; the LRR solenoid plus accessory factors form the substrate-recognition surface.
The deep research report confirms identity and family placement and stresses that SKP2 is not a kinase
and not the catalytic ubiquitin-transfer subunit
[file:human/SKP2/SKP2-deep-research-falcon.md "SKP2 is the substrate receptor of SCF^SKP2 rather than an autonomous catalytic enzyme."].

## Core molecular function: SCF(SKP2) substrate receptor

UniProt: "Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein
ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target
proteins involved in cell cycle progression, signal transduction and transcription".

The Cul1-Rbx1-Skp1-F box^Skp2 crystal structure establishes the architecture: CUL1 is a rigid scaffold
whose globular domain binds RBX1 (E2 recruitment) and whose stalk tip
[PMID:11961546 "binds the Skp1-F boxSkp2 protein"] substrate-recognition module, holding the two
> 100 Å apart. SKP2 thus provides specificity, not catalysis
[PMID:23911321 "Skp2 is an F-box protein, constituting one of the four subunits of the Skp1-Cullin-1-F-Box (SCF) ubiquitin E3 ligase complex."]
and its SKP1 contact is through the F-box
[PMID:23911321 "Skp2 directly interacts with Skp1 via its F-box domain and indirectly"].

## Canonical substrate: Thr187-phosphorylated p27/CDKN1B, with CKS1B

p27 proteolysis is triggered by CDK-mediated Thr187 phosphorylation, and — uniquely among SCF
substrates — needs the accessory subunit CKS1
[PMID:16209941 "p27(Kip1) ubiquitination also requires the accessory protein Cks1."]. The
Skp1–Skp2–Cks1/phospho-p27 structure shows a composite receptor
[PMID:16209941 "whereas p27(Kip1) binds to both Cks1 and Skp2."]. Mutational work localizes the
CKS1 contact to Skp2 Asp-331
[PMID:12813041 "Mutation of Asp-331 to Ala disrupts the interaction between Skp2 and Cks1."] and shows
the requirement is for p27 turnover
[PMID:12813041 "Ubiquitination of p27 requires the SCFSkp2 ubiquitin ligase and Skp2"].
Independent work restates the model
[PMID:16880511 "is mediated by SCF(Skp2) E3 ligase that captures"] Thr187-phosphorylated p27.

Functional consequence: loss of p45^SKP2 function blocks S-phase entry
[PMID:7553852 "prevented entry into S phase in both normal and transformed cells."], and p27 removal
releases cyclin E/A–CDK2, giving a positive-feedback G1/S switch
[file:human/SKP2/SKP2-deep-research-falcon.md "p27 ubiquitination and proteasomal degradation promote G1/S progression."].

## Additional degradative substrates (graded)

- ORC1: [PMID:11931757 "hOrc1p destruction occurs through the proteasome and is signaled in part by the"] SCF(Skp2) complex.
- CDT1, p21/CDKN1A, p57, p130/RBL2, FOXO1, RAG2, MYC, TOB1, TAL1, KMT2A, CDK9, YTHDF2 (UniProt FUNCTION);
  the deep research report rates these lower-confidence than p27
  [file:human/SKP2/SKP2-deep-research-falcon.md "Proteolytic regulation of p21, p57, p130, FOXO1, BRCA2, CDT1 and other substrates."].
- DUSP1/MKP-1 after ERK-dependent Ser296 phosphorylation
  [PMID:16286470 "active ERK-promoted phospho-Ser(296) MKP-1 bound to SCF(Skp2) ubiquitin ligase"].
- MYC: HBx stabilizes c-Myc by binding the SKP2 F-box
  [PMID:16376880 "through a direct interaction with the F box region of Skp2 and"]; ARF blocks the
  Myc–SKP2 interaction [PMID:23277542 "ARF inhibits the interaction of c-Myc with the E3 ubiquitin ligase Skp2."].
- E-cadherin (cytoplasmic, CKI-dependent), downstream of acetylation-driven cytoplasmic retention
  [PMID:22770219 "ubiquitination and destruction of E-cadherin."].
- HCV NS5A, via the ISG12a/IFI27 adaptor
  [PMID:27194766 "(SKP2) is identified as an ubiquitin E3 ligase for NS5A."],
  [PMID:27194766 "Moreover, the antiviral effect of ISG12a is dependent on the E3 ligase activity"] of SKP2.

## Non-degradative K63 branch: NBN/NBS1 in DSB repair

[PMID:22464731 "Skp2 interacts with NBS1 and triggers K63-linked"] ubiquitination of NBS1 after DSBs,
which is required for NBS1–ATM interaction and ATM recruitment to foci;
[PMID:22464731 "we show that Skp2 deficiency exhibits a defect in homologous"] recombination repair.
The production GO-CAM `gocams/65a1f4f800001029/` models exactly this: SKP2 (Q13309) with
GO:1990756 ubiquitin-like ligase-substrate adaptor activity in GO:0070534 protein K63-linked
ubiquitination, upstream of NBN and ATM at the site of a double-strand break. This is a second,
non-proteolytic core activity, and the repository module `modules/g1_s_transition.yaml` independently
cites SKP2 as the metazoan CKI F-box adaptor.

## Regulation (context for non-core calls)

- APC/C-CDH1 degrades SKP2 in G1 [PMID:18239684 "regulated by the APC(Cdh1), which targets Skp2 for degradation."];
  CDK2 phosphorylation of Ser64/Ser72 protects it, Cdc14B dephosphorylation re-exposes it.
- p300 acetylates K68/K71 in the NLS; SIRT3 reverses this
  [PMID:22770219 "acetylation of Skp2 in the nuclear localization signal (NLS) promotes its"] cytoplasmic
  retention, and also promotes dimerization
  [PMID:22770219 "We found that p300-mediated Skp2 acetylation promotes Skp2 dimerization"].
- SCF assembly is gated by CUL1 neddylation and CAND1
  [PMID:12504026 "Both in vivo and in vitro, CAND1 prevents the binding of SKP1 and SKP2 to CUL1"];
  TIP120A/CAND1-family proteins act similarly
  [PMID:12609982 "but interfered with the binding of Skp1 and F-box proteins"];
  DCUN1D3 promotes CUL1 neddylation
  [PMID:27542266 "DCUN1D3 can inhibit the formation of SCFSKP2 complex by reducing Cullin-1"] (on knockdown).
- TRIM21/Ro52 can substitute for RBX1 in a Cul1-based core that also contains SKP2
  [PMID:16880511 "Here we identify Skp2 as a component"] of such a complex.

## Curation decisions taken in this review

1. **Bare `GO:0005515` protein binding (50 IPI rows).** Per repository policy, these were either
   MODIFYed to an informative MF where the cited study establishes one, or REMOVEd as uninformative
   (never asserting the interaction is false):
   - MODIFY → `GO:1990756` ubiquitin-like ligase-substrate adaptor activity for rows whose partner is a
     recognised SKP2 substrate (CDKN1B, CDKN1A, DUSP1, MYC, ORC1, CDT1, CDH1, HCV NS5A) or a component
     of the recognition bridge itself (SKP1, CKS1B) in a focused mechanistic/structural study.
   - MODIFY → `GO:0097602` cullin family protein binding for the CUL1 rows from focused SCF-assembly
     studies (11961546, 12504026, 12609982, 18239684, 27542266).
   - REMOVE for proteome-scale screens (BioPlex 2.0/3.0, LuTHy, in-situ PLA network, ISG interactome,
     Polycomb complexome, neoPPI, AI-pipeline, multimodal cell maps, CRL AQUA proteomics), for partners
     that act *on* SKP2 rather than being acted on by it (FZR1/Cdh1, EP300, SIRT3, TRIM21, ASB2, HBx,
     SGT1/Hsp90), and for rows whose paper attributes the mechanism to a different F-box protein
     (SMAD4 via β-TrCP1 in PMID:16865698; RRM2 via cyclin F in PMID:22632967). The physical
     interactions remain recorded in IntAct; only the uninformative GO annotation is removed.
   - Note on PMID:18239684: the supporting entity `UniProtKB:A5D8W4` (cadherin-1) sits in a paper about
     APC/C **Cdh1** (FZR1). Whatever the intended partner, the row is a bare protein-binding record and
     is removed as uninformative; no claim of curator error is made.
2. **`GO:0042802` identical protein binding** (IPI, PMID:22770219) is supported by direct dimerization
   data but is an acetylation-gated regulatory property, so KEEP_AS_NON_CORE.
3. **IBA rows** (GO:0019005, GO:0031146, GO:1990756, GO:1905168) are accepted. For GO:1990756 and
   GO:1905168 the `WITH/FROM` includes `UniProtKB:Q13309` itself — expected, since SKP2's own
   experimental annotations are among the descendant evidences the PAINT curator used to place the IBD;
   this is not circularity.
4. **Localisation.** Nucleus/nucleoplasm = core (canonical p27 turnover is nuclear
   [file:human/SKP2/SKP2-deep-research-falcon.md "Canonical activity is predominantly nuclear and oscillates with the cell cycle."]).
   Cytoplasm/cytosol (real, acetylation- and AKT-gated; Reactome places CRL neddylation/CAND1 handling
   in cytosol) and nucleolus (HPA immunofluorescence only) are kept as non-core.
5. **Phenotype-adjacent process terms.** `GO:0042981 regulation of apoptotic process` (IDA,
   PMID:23277542) is a downstream consequence of Myc-TD ubiquitination and SKP2 overexpression, so
   non-core. `GO:0045087 innate immune response` and `GO:0051607 defense response to virus` (IMP,
   PMID:27194766) rest on a single HCV/ISG12a study and are kept non-core.
6. **`GO:0070936 protein K48-linked ubiquitination`** (IMP, PMID:27194766): the cached record is
   abstract-only and does not state the linkage, but K48 chains are the canonical degradative output of
   SCF(SKP2) and the curator read the full text — ACCEPT rather than second-guess.
7. **`core_functions` holds two entries**, both with `GO:1990756` as the molecular function: the
   proteolytic SCF(SKP2) branch (GO:0031146 + GO:0000082, nucleus/nucleoplasm) and the K63/NBN branch
   (GO:0070534 + GO:1905168, nucleus), each `in_complex: GO:0019005`. A third, cytoplasmic
   E-cadherin-degradation entry was drafted and then dropped: listing cytoplasm/cytosol as core
   locations would contradict the KEEP_AS_NON_CORE calls on those very annotations (validation flagged
   exactly this). The cytoplasmic branch is therefore described in `description` and raised in
   `suggested_experiments` instead.
8. **No `proposed_new_terms`.** Every distinct activity SKP2 performs (adaptor activity, SCF
   membership, SCF-dependent proteasomal catabolism, K63 ubiquitination, positive regulation of HR
   repair, G1/S transition) already has an annotation; substrate relationships belong on `has input` of
   the ligase activity in GO-CAM, not as new terms on SKP2.
