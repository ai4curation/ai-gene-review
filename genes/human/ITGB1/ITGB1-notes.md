# ITGB1 (integrin beta-1, CD29, human, P05556) review notes

Automated deep research was unavailable for this review (no provider keys), so no
`-deep-research-*.md` file exists. These notes are based on the UniProt record, the 349 GOA
rows and the cached publications in `publications/`. Many primary papers behind the GOA rows
are abstract-only in the cache (`full_text_available: false`); decisions on those rows are
limited to what the abstract says, and experimental rows were not removed on that basis.

## Core biology

- Integrins are heterodimeric ECM receptors, old in evolution: "Integrins are cell adhesion
  receptors that are evolutionary old and that play important roles during developmental and
  pathological processes." [PMID:19693543]
- Beta-1 pairs with 12 alpha subunits (alpha1-11, alphaV) (UniProt SUBUNIT). These
  heterodimers are the main receptors for collagens (alpha1, 2, 10, 11), laminins (alpha3, 6,
  7), fibronectin (alpha5, alpha4, alpha8, alphaV) and the cell-surface counter-receptor
  VCAM1 (alpha4, alpha9) (UniProt FUNCTION).
- alpha5beta1 is the prototypic fibronectin receptor: "Integrin α5β1 is a major cellular
  receptor for the extracellular matrix protein fibronectin and plays a fundamental role
  during mammalian development." [PMID:22451694]
- Bidirectional link: "Integrin α5β1 connects to the FN ligand, a major component of the ECM,
  through its extracellular domains and to the actin cytoskeleton through its cytoplasmic tail
  domains in combination with accessory factors" [PMID:33962943]
- Divalent cations: "The integrin βI domain contains three functional metal ion pockets
  exhibiting clear densities, namely, MIDAS, ADMIDAS" [PMID:33962943]; the FN-alpha5beta1
  cryo-EM shows "key interactions centered at R1445 and Y1446 of FN and D137 of ADMIDAS in β1
  βI domain provide an additional anchoring point that triggers the opening of α5β1"
  [PMID:33962943]. The resting buffer is Ca2+/Mg2+, Mn2+ activates.
- Adhesion receptor activity is regulated from inside: "activation of endogenous EphA2 kinase
  induces an inactive conformation of integrins and inhibits cell spreading, migration and
  integrin-mediated adhesion" [PMID:10655584].
- Cytoplasmic tail partners (all with direct-binding evidence in the cited papers):
  - talin: "the interaction between integrin and talin was greatly enhanced by
    PI4,5P(2)-induced talin activation" [PMID:11279249]; NMR of beta1A/beta1D tails with
    talin1/2 [PMID:21134644]; ICAP-1 competes with talin [PMID:12473654].
  - filamin: "the cytoplasmic domain of beta1-integrin specifically interacts with the
    cytoskeletal protein filamin" [PMID:9722563]; FLNa pull-downs [PMID:17690686].
  - ICAP-1 (ITGB1BP1), specific to beta1 and requiring the NPXY motif [PMID:9281591].
  - Rab25 (direct, tail) [PMID:17925226]; Abl2/Arg kinase domain binds the membrane-proximal
    tail [PMID:25694433]; FAK "is directly recruited by integrin β1" [PMID:26763945].
- Extracellular partners beyond ECM: fractalkine chemokine domain (alpha4beta1 coreceptor)
  [PMID:23125415, PMID:24789099]; CD40L (alpha5beta1) [PMID:31331973]; ADAM17 and ADAM9
  disintegrin domains [PMID:14970227, PMID:30455686, PMID:17704059]; seprase/FAP docking at
  invadopodia (alpha3beta1) [PMID:10455171]; viral and fungal ligands (EBV BMRF-2
  [PMID:12592401], Rhizopus CotH7 [PMID:32487760]).

## GO-CAM

`gocams/index.tsv` has ITGB1 in two human models:
- 666b894f00000196 "CD93/Multimerin-2/beta1 integrin complex function in angiogenesis":
  coreceptor activity (GO:0015026), angiogenesis, plasma membrane.
- 689e7a5d00003515 "Ephrin-A1/EPHA2 negative regulation of cell adhesion mediated by
  integrin": cell adhesion receptor activity (GO:0004895), integrin-mediated signaling
  pathway, focal adhesion. This matches the core MF chosen here.

## Decisions by group (349 rows)

- **Protein binding (74 rows).** Repository policy: MODIFY where the cited paper supports a
  more informative MF and the partner defines one; otherwise REMOVE as uninformative (removal
  does not mean the interaction is false).
  - talin partners -> `GO:1990147 talin binding` (11279249, 12473654, 21134644, 21947080).
  - filamin partners -> `GO:0031005 filamin binding` (9722563, 17690686, 18177638, 16076904).
  - FN1 -> fibronectin binding (33962943); fibrillin-1 -> `GO:0050840 extracellular matrix
    binding` (12807887, 17158881; GO has no fibrillin-binding term).
  - fractalkine -> `GO:0019960 C-X3-C chemokine binding` (24789099).
  - Rab25 -> `GO:0031267 small GTPase binding` (17925226). Rab21 (16754960) was REMOVED: the
    paper places Rab21 on alpha-chain tails, not beta1.
  - Abl2 -> `GO:1990782 protein tyrosine kinase binding` (25694433).
  - ADAM17/ADAM9 disintegrin ligands -> `GO:0002020 protease binding` (14970227, 22413019,
    30455686, 17704059), matching the existing protease-binding row for seprase.
  - midkine (MDK) rows from 15466886 -> `GO:0038023 signaling receptor activity` ("alpha4beta1-
    and alpha6beta1-integrins are functional receptors for midkine").
  - EBV BMRF-2 -> `GO:0001618 virus receptor activity` (12592401).
  - integrin TM domain heterodimers (14681217) -> `GO:0046982 protein heterodimerization
    activity`.
  - Integrin alpha-subunit partners (ITGA2/4/5/6) REMOVED: subunit pairing is captured by the
    `integrin alphaX-beta1 complex` CC rows.
  - High-throughput Y2H / interactome rows (32814053, 33961781, 35384245, 30021884) REMOVED.
  - PMID:10676904 is a wrong identifier: PubMed (esummary checked) and the cache both give a
    bovine oocyte culture paper, which cannot support an ITGB1-FLNB interaction. REMOVED
    under the protein-binding policy anyway; flagged WRONG_IDENTIFIER in references.
- **Removed process rows.** `homophilic cell-cell adhesion` (TAS 10201960): integrins bind
  heterophilic ligands, and the cited paper only reports eotaxin up-regulating CD29.
  `cellular defense response` (TAS 10201960): same paper, expression change only.
- **Over-annotated.** `B cell differentiation` (IC from 1715889: the abstract only suggests
  adhesion "may be required for normal early B cell development"); `cell development`,
  `regulation of developmental process` (ARBA, too general); `response to muscle activity`,
  `cellular response to low-density lipoprotein particle stimulus` (mouse-derived
  expression/response terms); `melanosome` (proteomics); `cytoplasm` (IDA, platelet paper;
  ITGB1 is a type I membrane protein); `cadherin binding` HDA (E-cadherin proximity
  proteomics); `mesodermal cell differentiation` (IEP and ARBA; the cited paper is on
  endoderm differentiation via ITGA5/ITGAV); ARBA `protein-containing complex binding`;
  `signaling receptor complex` (23382219, SNX17 cargo screen).
- **MODIFY of non-binding rows.** `calcium-independent cell-matrix adhesion` (IGI 19651211)
  -> `cell adhesion mediated by integrin`: the abstract shows RGD-dependent beta1 adhesion but
  says nothing about calcium, and beta1 ligand binding uses Ca2+ sites (ADMIDAS/SyMBS).
  `protein-containing complex binding` IPI (25336636, CDH17 RGD ligand) -> `cadherin binding`.
- **UNDECIDED.** `actin binding` IDA (16803572, platelet dystrophin/utrophin co-IP; abstract
  does not show direct actin binding by beta1); `maintenance of blood-brain barrier` NAS
  (30280653: the cached abstract of the review does not mention integrins).
- **NOT rows** (24036928): beta1 knockdown did not reduce TGF-beta-induced ventral stress
  fibres ("Knockdown of integrin-β1 by siRNA did not reduce TGF-β1-induced VSFs"). Both NOT
  annotations accepted.

## Premetazoan context (ancestral vs animal-specific)

- Integrin beta and alpha are older than animals. Sebé-Pedrós et al. found "four integrin β
  and four integrin α genes in C. owczarzaki", and one of each in the apusozoan
  Amastigomonas [PMID:20479219].
- The ancestral beta subunits already have the key motifs: the cation-binding sites "are well
  conserved in the different nonmetazoan integrin β, except for C. owczarzaki integrin β4",
  and the cytoplasmic alpha-interacting motif and NPXY motif "are well conserved in C.
  owczarzaki integrin β1–β3 and Amastigomonas sp. integrin β" [PMID:20479219].
- Choanoflagellates lost them: "Integrin α and β and several other components of the integrin
  adhesion complex are absent from choanoflagellates and fungi and were presumably lost
  independently in these lineages" [PMID:20479219]. The putative M. brevicollis integrin
  alpha (XP_001749484) failed their criteria and clusters with bacterial FG-GAP proteins.
- Capsaspora integrin beta2 is used for substrate adhesion: Capsaspora "adheres to surfaces
  using actin-dependent filopodia", "integrin β2 and its associated protein vinculin localize
  as distinct patches in the filopodia", and an anti-integrin beta2 antibody inhibited
  adhesion to fibronectin-coated surfaces [PMID:32857975, abstract only].
- Caveat: Capsaspora integrin betas are a lineage-specific expansion ("lineage-specific
  diversifications ... of both integrin α and β have occurred within the C. owczarzaki
  lineage" [PMID:20479219]); they are not orthologs of ITGB1 specifically. The ancestral
  claim is for the integrin beta subunit family, not for ITGB1 as a paralog.
- Talin/vinculin are older still (amoebozoans) and were co-opted to integrins
  [PMID:20479219]; see the TLN1 and VCL reviews.

So, on current evidence:
- **Ancestral (holozoan or older):** alpha/beta heterodimeric receptor; divalent-cation
  (MIDAS/ADMIDAS) dependent ligand binding; cytoplasmic NPXY motif for adaptor (talin) binding;
  cell-substrate adhesion through actin-rich protrusions with vinculin. Capsaspora adhesion is
  enhanced by mammalian fibronectin in assays [PMID:32857975], but the native Capsaspora
  ligand is not identified in the papers read here.
- **Animal-specific (on current evidence; not separately sourced here):** binding to the
  specific animal ECM ligands annotated on ITGB1 (fibronectin, collagens, laminins), cell-cell
  adhesion via counter-receptors (VCAM1, ADAMs), coreceptor roles in chemokine/growth factor
  signalling, angiogenesis, leukocyte trafficking, myogenesis, osteoclast and neural
  functions. These are tissue-level roles of the beta1 paralog in a multicellular body.

