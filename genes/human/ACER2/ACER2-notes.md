# ACER2 (Alkaline ceramidase 2) — review notes

UniProt: Q5QJU3 (ACER2_HUMAN). Synonym ASAH3L. HGNC:23675. Chromosome 9p22.
275 aa, 7-TM multipass Golgi membrane protein.

## Core biology

ACER2 is **alkaline ceramidase 2**, a Golgi-membrane enzyme that hydrolyzes ceramide
(N-acylsphingosine) into **sphingosine + free fatty acid** at alkaline pH, and likewise
hydrolyzes dihydroceramide to dihydrosphingosine. It is one of three human alkaline
ceramidases (ACER1/2/3) plus one acid (ASAH1) and one neutral (ASAH2) ceramidase.

The sphingosine it produces is the precursor that sphingosine kinases (SPHK1/2)
phosphorylate to sphingosine-1-phosphate (S1P). By controlling the ceramide → sphingosine
→ S1P balance, ACER2 governs cell proliferation/survival (S1P-driven) versus growth arrest,
apoptosis and autophagy (sphingosine/ceramide-driven).

- Enzyme / EC / catalytic activity: EC 3.5.1.23 (N-acylsphingosine amidohydrolase =
  ceramidase). "Golgi ceramidase that catalyzes the hydrolysis of ceramides into sphingoid
  bases like sphingosine and free fatty acids at alkaline pH"
  [file:human/ACER2/ACER2-uniprot.txt]. Rhea:RHEA:20856 (an N-acylsphing-4-enine + H2O =
  sphing-4-enine + a fatty acid); Rhea:RHEA:33551 for the sphinganine (dihydro) reaction.
- Broad substrate specificity, prefers unsaturated long-chain ceramides: "Has a better
  catalytic efficiency towards unsaturated long-chain ceramides, including C18:1-, C20:1-
  and C24:1-ceramides" [file:human/ACER2/ACER2-uniprot.txt]. Kinetics (KM/Vmax) measured for
  C6:0–C24:1 ceramides (PMID:20089856).
- Alkaline pH optimum 7.5–9.0; **Ca2+-stimulated** (lumenal, not cytosolic Ca2+),
  Zn2+-dependent catalysis (2 catalytic Zn-binding residues by similarity), inhibited by
  Zn2+/Cu2+ excess and by D-e-MAPP [file:human/ACER2/ACER2-uniprot.txt; PMID:20089856;
  PMID:20207939].

## Localization

- Golgi apparatus / Golgi membrane, multipass (7-TM). "haCER2 is localized to the Golgi
  complex" [PMID:16940153]; UniProt "Golgi apparatus membrane ... Multi-pass membrane
  protein" [file:human/ACER2/ACER2-uniprot.txt]. N-terminal region (aa 1–13/1–16) required
  for Golgi targeting; deleting it mislocalizes to ER without abolishing intrinsic
  ceramidase activity (PMID:20089856 mutagenesis; MUTAGEN 1..16 "Loss of localization to the
  Golgi. No effect on the ceramidase activity" [file:human/ACER2/ACER2-uniprot.txt]).

## Physiological roles (from primary literature)

1. **Sphingosine/S1P homeostasis, proliferation & survival** — PMID:16940153 (FASEB J 2006,
   abstract-only cache). Identifies haCER2, Golgi-localized, placenta-enriched. Low ectopic
   expression raises S1P and promotes proliferation in serum-free medium (via S1P1/S1PR1);
   high ectopic expression accumulates sphingosine, fragments Golgi, causes growth arrest.
   "haCER2 is important for the generation of S1P and S1P-mediated cell proliferation and
   survival, but ... its overexpression may cause cell growth arrest due to an accumulation
   of sphingosine" [PMID:16940153].

2. **β1-integrin maturation / cell adhesion** — PMID:18945876 (FASEB J 2009, abstract-only).
   ACER2/sphingosine pathway regulates N-glycosylation-dependent maturation of the integrin
   β1 subunit; overexpression inhibits β1 maturation, lowers surface β1 integrins, and
   inhibits adhesion to fibronectin/collagen; knockdown has opposite effects. ATRA induces
   ACER2 and inhibits β1 maturation. "ACER2 overexpression decreased the cell surface levels
   of beta1 integrins, thus inhibiting cell adhesion to fibronectin or collagen" [PMID:18945876].

3. **Substrate specificity, topology, activity regulation** — PMID:20089856 (JBC 2010,
   abstract-only). 7-TM, luminal N-terminus / cytosolic C-terminus; requires Ca2+; N-terminal
   tail needed for activity and Golgi localization; mistargeting abolishes ability to regulate
   protein glycosylation (β1 integrin, Lamp1). "overexpression of ACER2 but not ACER2DeltaN13
   or ACER2DeltaN36 inhibited the glycosylation of integrin beta1 subunit and Lamp1"
   [PMID:20089856].

4. **Erythrocyte SPH/S1P generation** — PMID:20207939 (FASEB J 2010, abstract-only). Alkaline
   ceramidase activity (ACER-type) is the ceramidase active in erythrocytes for generating the
   S1P precursor sphingosine; D-e-MAPP inhibits. Supports ceramide catabolism / sphingosine
   biosynthesis role. "alkaline ceramidase activity is important for the generation of SPH,
   the S1P precursor in erythrocytes" [PMID:20207939].

5. **4-HPR (fenretinide) cytotoxicity via dihydrosphingosine** — PMID:20628055 (JBC 2010,
   abstract-only). 4-HPR upregulates ACER2 (retinoic-acid-receptor-independent, caspase-
   dependent); ACER2 hydrolyzes dihydroceramides to dihydrosphingosine (DHS); ACER2/DHS
   mediates 4-HPR cytotoxicity in tumor cells. "4-HPR increases the expression of ACER2,
   which catalyzes the hydrolysis of dihydroceramides to generate DHS" [PMID:20628055]. This
   is the "cellular response to xenobiotic stimulus" (IEP) and "response to retinoic acid"
   basis.

6. **DNA damage response via sphingosine/ROS** — PMID:26943039 (Oncotarget 2016, full text).
   DNA-damaging agents (doxorubicin, 5-FU) upregulate ACER2 (protein + activity), raising
   sphingosine and S1P; ACER2 knockdown blunts this and inhibits programmed cell death; SPH
   (not S1P) is the death mediator, acting through ROS. "DNA damage increases sphingosine
   levels in tumor cells by upregulating alkaline ceramidase 2 (ACER2) and ... the ACER2/
   sphingosine pathway induces PCD in response to DNA damage by increasing the production of
   reactive oxygen species (ROS)" [PMID:26943039].

7. **Direct p53 target; autophagy + apoptosis via ROS** — PMID:28294157 (Sci Rep 2017, full
   text). ACER2 is a direct transcriptional target of p53 (p53RE in first intron, ChIP-
   confirmed); ACER2 promotes autophagy (LC3-II, mTOR/Akt inhibition) and apoptosis; ATG5
   knockdown shows autophagy facilitates apoptosis; both depend on ROS (NAC blocks, H2O2
   enhances). "human ACER2 transcription is directly regulated by p53 and ACER2 is implicated
   in the induction of autophagy as well as apoptosis" [PMID:28294157].

8. **p53 links ceramide metabolism to DDR through ACER2** — PMID:29229990 (Cell Death Differ
   2018, full text). Confirms ACER2 is a direct p53 target (two p53REs in first intron, ChIP);
   p53/IR upregulate ACER2, raising SPH and S1P, lowering ceramides. Moderate ACER2 → S1P →
   inhibits cell-cycle arrest/senescence; robust ACER2 → sphingosine accumulation → PCD.
   ACER2 frequently inactivated in cancers (deletion/mutation); restoring it inhibits tumor
   xenograft growth → tumor-suppressor role. "human alkaline ceramidase 2 (ACER2) is a novel
   transcriptional target of p53 and ... its transactivation by p53 mediates the DDR"
   [PMID:29229990].

## Regulation

Induced by serum deprivation (PMID:16940153), 4-HPR/fenretinide (PMID:20628055), and DNA
damage in a p53-dependent manner (PMID:26943039, PMID:28294157, PMID:29229990). Tissue: highly
expressed in placenta [file:human/ACER2/ACER2-uniprot.txt].

## GO review reasoning summary

- **Core MF**: GO:0017040 N-acylsphingosine amidohydrolase activity (= ceramidase / EC
  3.5.1.23). Strongly supported by direct enzymology (IDA in PMID:16940153, PMID:20089856,
  PMID:20628055; IMP PMID:20207939) plus IBA/IEA/Reactome. Verified current label via OLS.
- **Core BP**: GO:0046514 ceramide catabolic process and GO:0046512 sphingosine biosynthetic
  process — the two sides of the same hydrolysis reaction; both have IDA/IMP experimental
  support. Sphingolipid metabolism (GO:0006665/GO:0006672/GO:0030149) are broader parents,
  kept as non-core.
- **Core CC**: GO:0000139 Golgi membrane (IDA PMID:20089856; multipass). GO:0005794 Golgi
  apparatus (IDA PMID:16940153) is the correct-but-less-precise parent → keep as non-core.
- **Downstream/pleiotropic BP** (proliferation, apoptosis, autophagy, DDR, p53 signaling,
  integrin adhesion, glycoprotein biosynthesis, xenobiotic/retinoic-acid responses): all are
  genuine experimental annotations reflecting the *consequences* of altering the sphingosine/
  S1P balance, not the enzyme's direct molecular action. Keep experimental ones as
  KEEP_AS_NON_CORE (do not REMOVE experimental annotations).
- **IEA duplicates / broad terms**: GO:0016020 membrane (IEA InterPro) is uninformative given
  the specific Golgi-membrane annotation → MARK_AS_OVER_ANNOTATED. GO:0046872 metal ion
  binding (KW-derived) is not in the seeded GOA TSV (dropped) so not reviewed here; Zn2+/Ca2+
  binding is real but a housekeeping/keyword annotation.
- No REMOVE actions used: all IEA terms present are biologically consistent (ceramidase MF,
  sphingolipid metabolism, Golgi/membrane location).
