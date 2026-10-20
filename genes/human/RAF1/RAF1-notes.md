# RAF1 (CRAF, c-Raf, Raf-1) — curation notes

UniProt P04049, human. HGNC:9829. RAF-family (TKL) Ser/Thr kinase; paralogs BRAF (P15056), ARAF (P10398).

## Identity and architecture

- CR1 = RAS-binding domain (RBD) + cysteine-rich domain (CRD, C1-like); CR2 = Ser/Thr-rich with the inhibitory
  pSer259 14-3-3 site; CR3 = kinase domain followed by the pSer621 14-3-3 site
  [file:human/RAF1/RAF1-deep-research-falcon.md "CR2, a serine/threonine-rich regulatory segment containing the inhibitory"].
- Catalysis: EC 2.7.11.1; UniProt catalytic activity evidence is PMID:17603483
  [file:human/RAF1/RAF1-uniprot.txt "Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +"].

## Core function: MAP3K of the RAS-RAF-MEK-ERK cascade

- UniProt: "Serine/threonine-protein kinase that acts as a regulatory link between the membrane-associated Ras GTPases
  and the MAPK/ERK cascade" [file:human/RAF1/RAF1-uniprot.txt]. RAF1 phosphorylates MAP2K1/MAP2K2, which then
  phosphorylate ERK1/2.
- MEK1/2 are the only broadly accepted physiological substrates; BRAF has higher intrinsic MEK-kinase activity than CRAF
  [file:human/RAF1/RAF1-deep-research-falcon.md "MEK1/MAP2K1 and MEK2/MAP2K2 are the only broadly accepted physiological RAF1 substrates."].
- Reactome: "Although all three RAF kinases can phosphorylate MAP2K1 and MAP2K2, BRAF appears to be the primary
  activator in vivo" [Reactome:R-HSA-5672978].
- Direct kinase assays: carbachol-activated c-Raf phosphorylates MEK in vitro [PMID:8063729 "Carbachol potently induced
  c-Raf activity as judged by its in vitro phosphorylating activity using MEK as a substrate."]; IFN-gamma activates Raf-1
  via JAK1 [PMID:9446616]; IL-8 activates Raf-1 in neutrophils [PMID:8576262].

## Activation cycle (regulatory interactions that map to informative binding MFs)

- **14-3-3** (GO:0071889): 14-3-3 dimer binds pSer259 and pSer621; pS621 is the high-affinity site
  [PMID:14688280 "the 14-3-3 binding domain surrounding pS621 represents the high affinity binding site"];
  S621/14-3-3 binding is required for activity [PMID:19595761 "Mutations that prevent the binding of 14-3-3 proteins to S621 render Raf-1 inactive"];
  Noonan mutations near S259 impair 14-3-3 binding [PMID:20679480]. Many classic papers (PMID:7935795, 7939632, 8085158,
  7882972, 8601312, 7760835).
- **RAS-GTP** (GO:0031267 small GTPase binding): RBD binds GTP-Ras [PMID:8332187 "Raf-1 (1-257) binds GTP-Ras in preference to GDP-Ras"];
  RBD/Rap1A crystal structure [PMID:7791872]; RBD-CRD/KRAS structure [PMID:33608534].
  RAF1 does NOT bind Di-Ras [PMID:12194967 "Di-Ras fails to interact with the Ras-binding domain of Raf"].
- **Dimerization** with BRAF (GO:0046982) and homodimers (GO:0042802/0042803): RAF inhibitors prime wild-type RAF
  dimers [PMID:20130576]; kinase-dead BRAF acts through CRAF [PMID:20141835]; UniProt "Heterodimerizes with BRAF".
- **MEK** (GO:0031434): substrate complex [PMID:24746704 title "Disruption of CRAF-mediated MEK activation ..."];
  RKIP displaces MEK [PMID:17097642 "The Raf kinase inhibitory protein (RKIP) binds to Raf-1 interfering with binding of the MEK substrate"].
- **HSP90/CDC37** chaperone client (GO:0051879, GO:0051087)
  [file:human/RAF1/RAF1-deep-research-falcon.md "RAF1 also depends strongly on the **HSP90–CDC37** chaperone system"].
- **MRAS-SHOC2-PP1C** holophosphatase dephosphorylates pS259 [PMID:25137548 "which tethers RAS, RAF-1 and the catalytic subunit of protein phosphatase 1c (PP1c)"; PMID:36175670].
- **PP2A** B-alpha/delta holoenzymes associate with Raf1 and dephosphorylate S259 [PMID:16239230].
- Negative regulators: RKIP/PEBP1 [PMID:17097642], PAQR3/RKTG Golgi trapping [PMID:17724343 "RKTG changes the localization of Raf-1 from cytoplasm to the Golgi apparatus"],
  HERC2 ubiquitylation [PMID:36241744 "HERC2 regulates C-RAF ubiquitylation"].

## Kinase-independent / non-canonical roles (non-core but real)

- Suppression of apoptosis by binding/inhibiting ASK1 and MST2
  [PMID:21779496 "These include the regulation of apoptosis by suppressing the activity of the proapoptotic kinases, ASK1 and MST2"];
  MST2/Hippo switch [PMID:24929361 "Raf-1 regulates the MST-LATS and MEK-ERK pathways"].
- Mitochondrial pool: Bcl-2 targets Raf-1 to mitochondria, BAD phosphorylation, protection from apoptosis [PMID:8929532];
  RAF phosphorylates BAD S75/S99/S118 [PMID:19667065 "Our results indicate that RAF kinases represent, besides protein kinase A, PAK, and Akt/protein kinase B, in vivo BAD-phosphorylating kinases."].
  Note: GOA row GO:0006915 "acts_upstream_of_or_within_positive_effect" apoptotic process (TAS PMID:8929532) has the sign
  wrong — the paper shows protection from apoptosis.
- Rok-alpha (ROCK2) inhibition, motility, wound healing, differentiation [PMID:21779496, PMID:15943972].
- Adenylyl cyclase phosphorylation/sensitization (AC II, V, VI) [PMID:15385642].
- Nuclear pS621 RAF1 with NFATc3 at CXCR5 promoter in RA-induced differentiation [PMID:24330068].
- Rb binding/phosphorylation [PMID:21139044].

## Disease

- Germline gain-of-function: Noonan syndrome 5 / LEOPARD, hypertrophic cardiomyopathy [PMID:17603483, PMID:20052757].

## Curation decisions (summary)

- Core: MAP3K activity (GO:0004709), protein Ser/Thr kinase activity, MAPK cascade, cytosol, plasma membrane.
- 225 bare GO:0005515 rows mapped by WITH/FROM partner type, matching the BRAF review:
  14-3-3 -> GO:0071889; RAS/RAP -> GO:0031267; MEK1/2 -> GO:0031434; BRAF -> GO:0046982; HSP90 -> GO:0051879;
  CDC37/BAG2/HSPA5/CCT3 -> GO:0051087; STUB1/HERC2 -> GO:0031625; KSR1/JSAP1/PEBP4/SHOC2 -> GO:0097110;
  PAK1/PAK2/AKT1/STK3/EGFR -> GO:0019901; PP2A/PP1/CDC25A -> GO:0019902; NFATC3 -> GO:0140297.
  Partners with no informative MF (PEBP1, PIN1, PAQR3, RB1, RCAN1, FAM83 family, metabolic/mitochondrial Y2H/AP-MS
  hits, viral proteins, APP, CASP8, SMAD4, MLF2, Lox, MFHAS1) -> REMOVE (not asserting interaction is false).
- NOT small GTPase binding (PMID:12194967, Di-Ras): the Di-Ras negative result is correct, but negating the general
  term contradicts the defining RAS-effector function -> REMOVE.
- Several IntAct IPI RAS rows cite papers where the cached text does not mention RAF1 (RBD pulldowns used as a Ras-GTP
  reporter are likely, e.g. PMID:19222999, 19063885, 19696784, 20133694, 21457714, 17229891, 19164755). Mapped to
  GO:0031267 with low confidence, deferring to the curator.
- PMID:9765203 cache has no abstract; PubMed abstract describes constitutive MEK signaling-induced senescence and does
  not mention RAF1 -> UNDECIDED.
- PMID:19593445 (known batch miscitation) does not appear in RAF1 GOA.
