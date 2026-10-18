# CDC20 (human, UniProt Q12834) — curation notes

Working journal for the GO annotation review of human CDC20 (p55CDC), the WD40
coactivator of the anaphase-promoting complex/cyclosome (APC/C).

## Identity

- HGNC symbol CDC20; UniProt Q12834; "Cell division cycle protein 20 homolog", alias p55CDC.
- Distinct from the paralogous coactivator FZR1/CDH1 and from CDC20B.
- Domain architecture (UniProt features): N-terminal regulatory region with the C-box,
  KEN box, CRY box, MAD2-binding segment and KILR motif; C-terminal WD40 beta-propeller
  (WD1 starts at residue 173) and the C-terminal IR tail.
- First described as p55CDC, a G-beta-repeat protein of cycling mammalian cells
  [PMID:7513050 "The amino acid sequence of p55CDC contains seven repeats homologous to the beta subunit of G proteins, and the highest degree of homology in these repeats was found with the Saccharomyces cerevisiae Cdc20 and Cdc4 proteins"].

## Core biology (synthesis)

1. **APC/C coactivator and substrate adaptor.** CDC20 is not an enzyme. It binds the
   phosphorylated APC/C through its C-box (to APC8/CDC23) and IR tail (to APC3/CDC27)
   and stimulates the ligase; its WD40 propeller binds D-box, KEN-box and ABBA degrons
   on substrates [PMID:27120157 "Coactivators recognize substrate degrons, and enhance the affinity of the APC/C for its cognate E2"; PMID:27509861 "Cdc20, the APC/C coactivator subunit responsible for substrate interactions"].
   APC/C activation by CDC20 requires mitotic hyperphosphorylation of APC/C, which
   displaces an Apc1 auto-inhibitory segment from the C-box binding site
   [PMID:27120157 "An auto-inhibitory segment of Apc1 acts as a molecular switch that in apo unphosphorylated APC/C interacts with the C-box binding site and obstructs engagement of Cdc20"].
2. **Metaphase-to-anaphase transition.** APC/C-CDC20 ubiquitinates securin and cyclin B1;
   securin loss activates separase, cyclin B1 loss inactivates CDK1. The ternary
   MAD2-CDC20-APC complex is inactive at metaphase and the CDC20-APC binary complex is
   active at anaphase [PMID:9637688 "an inactive hMAD2-CDC20-APC ternary complex present at metaphase, a CDC20-APC binary complex active in degrading specific substrates at anaphase"].
   Additional CDC20-dependent substrates documented in the cited literature: NEK2A and
   KIF18A [PMID:23288039], BUBR1 after acetylation-switch [PMID:19407811 "APC/C-Cdc20 was responsible for BubR1 degradation during mitosis"],
   USP22 [PMID:27030811 "The ubiquitin ligase anaphase-promoting complex (APC/C) targets USP22 for degradation by using the substrate adapter CDC20"],
   FBXO31 [PMID:29343641 "the APC/C coactivators CDH1 and CDC20 bind to a destruction-box (D-box) motif present in FBXO31 to promote its polyubiquitination and degradation"],
   conductin/AXIN2 [PMID:22322943 "Conductin is degraded by the anaphase-promoting complex/cyclosome cofactor CDC20"],
   FBXW5 [PMID:21725316].
3. **Target of the spindle assembly checkpoint (SAC).** Unattached kinetochores catalyse
   incorporation of CDC20 into the mitotic checkpoint complex (MCC = BUBR1-BUB3-CDC20-MAD2)
   [PMID:11535616 "We call this factor the mitotic checkpoint complex (MCC) as it consists of hBUBR1, hBUB3, CDC20, and MAD2 checkpoint proteins in near equal stoichiometry"].
   MAD2 binds a 40-residue segment N-terminal to the WD40 repeats
   [PMID:10700282 "identified the minimal Mad2-binding region of human Cdc20 as a 40-residue segment immediately N-terminal to the WD40 repeats"].
   In the APC/C-MCC structure, BUBR1 degron-like motifs block the degron receptor sites
   on CDC20 and obstruct UbcH10 binding [PMID:27509861 "Degron-like sequences of the MCC subunit BubR1 block degron recognition sites on Cdc20"].
   The MCC also inhibits a second, APC/C-bound CDC20 [PMID:25383541 "the MCC can inhibit a second CDC20 that has already bound and activated the APC/C"].
   Checkpoint silencing involves APC/C-driven ubiquitination of the MCC-intrinsic CDC20
   [PMID:17443186 "Multi-ubiquitination by APC leads to the dissociation of Mad2 and BubR1 from Cdc20"] counteracted by USP44
   [PMID:17443180 "USP44 deubiquitinates the APC coactivator Cdc20 both in vitro and in vivo"],
   an ATP-dependent step [PMID:20212161] promoted by p31comet [PMID:21300909].
   BUB1 phosphorylation of CDC20 inhibits APC/C-CDC20 catalytically [PMID:15525512 "Bub1 directly phosphorylates Cdc20 in vitro and inhibits the ubiquitin ligase activity of APC/C(Cdc20) catalytically"].
4. **Meiosis I.** Biallelic CDC20 mutations cause oocyte maturation arrest (MI arrest),
   fertilization failure and early embryonic arrest (OZEMA14)
   [PMID:32666501 "we identified biallelic CDC20 mutations in five infertile individuals with oocyte maturation arrest, fertilization failure, and early embryonic arrest"; "In oocytes, the activation of APC/C by CDC20 is a key step in homologue disjunction and in transition from meiosis I to meiosis II"].
5. **Localization.** Kinetochores (GFP-Cdc20 turns over rapidly at unattached kinetochores
   [PMID:15182668]; human CDC20 localizes to kinetochores in mouse oocytes and truncating
   mutants fail to [PMID:32666501 "CDC20 showed normal kinetochore localization as the wild-type"]),
   centrosome/spindle pole (UniProt, PubMed:20034488, not cached), and the mitotic cytosol
   where APC/C-CDC20 and MCC act (Reactome). Nucleoplasm rows come from Reactome
   reactions involving EMI1/FBXO5 and USP44.
6. **Regulation.** SIRT2 deacetylates CDC20 (K66), enhancing CDC27 binding
   [PMID:22014574 "SIRT2 regulates the anaphase-promoting complex/cyclosome activity through deacetylation of its coactivators, APC(CDH1) and CDC20"].
   Inhibitors: EMI1/FBXO5 [PMID:11988738], RASSF1A [PMID:14743218 "RASSF1A interacts with Cdc20, an activator of the anaphase-promoting complex (APC), resulting in the inhibition of APC activity"],
   MAD2B/MAD2L2 [PMID:11459826 "MAD2B inhibits both CDH1-APC and CDC20-APC"].
7. **Neuronal roles (rodent, by similarity).** A centrosomal Cdc20-APC pathway regulates
   dendrite morphogenesis and presynaptic differentiation in rodent neurons (UniProt "By
   similarity" statements; GOA rows are ISS/IEA from mouse/rat). Not demonstrated in human;
   graded non-core.

## Curation decisions (rationale summary)

- **Protein binding (67 IPI rows).** Following the repository policy, none kept as bare
  GO:0005515. Partner classes:
  - CDC27/ANAPC3 and ANAPC4 partners from mechanistic papers -> MODIFY to GO:0010997
    anaphase-promoting complex binding (the IR tail/C-box contacts with APC3/APC8 are the
    structural basis of coactivator binding).
  - MAD2L1 partners from papers on the MAD2-CDC20 interaction -> MODIFY to GO:1990333
    mitotic checkpoint complex, CDC20-MAD2 subcomplex (consistent with the MAD2L1 review).
  - MAD2L1/BUB1B partners from whole-MCC papers -> MODIFY to GO:0033597 mitotic
    checkpoint complex.
  - Partners that are APC/C-CDC20 substrates (BUBR1 after acetylation, AXIN2, FBXW5) ->
    MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity.
  - SIRT2 -> MODIFY to GO:0042826 histone deacetylase binding (anchors the rat-derived IEA).
  - High-throughput interactome rows (MitoCheck, BioPlex, OpenCell, Clone-seq, kinase
    network, cell maps, PLA screen, TRAIL kinase study), inhibitor-binding rows (EMI1,
    RASSF1A, MAD2L2, IpaB study), regulator rows (USP44, HSF1, CDK5RAP2, CCNF) and the
    stPEPC drug study -> REMOVE as uninformative; removal does not dispute the interaction.
- **GO:0005819 spindle TAS (PMID:7513050)** kept non-core: the 1994 source only infers a
  spindle role from yeast homology; later work supports spindle-pole/kinetochore
  association.
- **GO:0044784 (generic metaphase/anaphase transition)** -> MODIFY to the mitotic child
  GO:0007091; the meiotic child GO:1990949 already carries IMP.
- **GO:0007346 regulation of mitotic cell cycle (NAS, review)** -> MODIFY to
  GO:0045842, the specific IDA-supported process.
- **GO:0051445 regulation of meiotic cell cycle (NAS, review)** -> MODIFY to GO:1990949.
- **GO:0008284 positive regulation of cell population proliferation (IEA from rat)** ->
  MARK_AS_OVER_ANNOTATED (downstream consequence of being required for mitosis).
- **Neuronal terms (GO:0031915, GO:0090129, GO:0050773)** -> non-core / over-annotated;
  rodent-only, "By similarity".
- **GO:0032991 protein-containing complex (IEA)** -> MODIFY to the specific complexes.
- No `NEW` terms proposed: GO-CAMs 6348a65d00002236 and 657ba49f00001888 and the module
  metaphase_anaphase_transition_and_mitotic_exit already place CDC20 under GO:0010997 /
  GO:1990756 / GO:1990757, GO:0045842 and GO:0007094, which the existing GOA covers.
