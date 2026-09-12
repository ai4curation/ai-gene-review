# PCYT1A (CCTα) — curation notes

UniProt: P49585 (PCY1A_HUMAN). Gene: PCYT1A (syn. CTPCT, PCYT1). 367 aa. HGNC:8754.
EC 2.7.7.15. Source of record: `file:human/PCYT1A/PCYT1A-uniprot.txt`.

## Identity and core reaction

PCYT1A is choline-phosphate cytidylyltransferase A (CCTα / CTP:phosphocholine
cytidylyltransferase A). It catalyzes the second, rate-limiting and regulated step of
the CDP-choline (Kennedy) pathway of phosphatidylcholine (PC) biosynthesis:

- Reaction: phosphocholine + CTP + H(+) = CDP-choline + diphosphate
  [file:human/PCYT1A/PCYT1A-uniprot.txt "Reaction=phosphocholine + CTP + H(+) = CDP-choline + diphosphate;"]
- Function: "Catalyzes the key rate-limiting step in the CDP-choline pathway for
  phosphatidylcholine biosynthesis"
  [file:human/PCYT1A/PCYT1A-uniprot.txt "Catalyzes the key rate-limiting step in the CDP-choline"]
- Pathway: "phosphatidylcholine from phosphocholine: step 1/2"
  [file:human/PCYT1A/PCYT1A-uniprot.txt "phosphatidylcholine from phosphocholine: step 1/2."]

Catalytic activity of the human enzyme is directly supported experimentally:
[PMID:7918629 "The specific activity of the HCT in COS cell homogenates was the same as
that of analogously expressed rat liver CT"] (TAS/EXP in GOA), and
[PMID:30559292 "CTP:phosphocholine cytidylyltransferase (CCT) is the key regulatory
enzyme in phosphatidylcholine (PC) synthesis and is activated by binding to
PC-deficient membranes"] (EXP, PMID:30559292). CCTα enzymatic activity, subcellular
localization and tissue specificity were characterized in [PMID:10480912] (IDA).

## Amphitropic regulation (membrane sensing)

CCT is an amphitropic enzyme that interconverts between an inactive soluble form and an
active membrane-bound form. Activation requires membrane binding of an amphipathic
α-helical domain and disruption of an autoinhibitory (AI) segment that otherwise
constrains the active site. In UniProt:
- "Interconverts between an inactive cytosolic form and an active membrane-bound form"
  and "Activation involves disruption of an inhibitory interaction between helices at the
  base of the active site and the autoinhibitory (AI) region"
  [file:human/PCYT1A/PCYT1A-uniprot.txt "Activated by anionic lipid vesicles and by oleic acid or"]
- FT REGION 228..287 "Amphipathic"; REGION 272..293 "Autoinhibitory (AI)".
- Human enzyme is lipid-activated: [PMID:7918629 "The soluble form was
  activated 3 to 4-fold by anionic phospholipids and by oleic acid or
  diacylglycerol-containing PC vesicles"].

This membrane sensing underlies the two IEA "regulatory" molecular functions in GOA:
- molecular function inhibitor activity (GO:0140678) — the AI helix autoinhibits the
  active site (intramolecular; a plausible mechanistic annotation, Ensembl-projected).
- lipid binding (GO:0008289) / phosphatidylcholine binding (GO:0031210) — the
  amphipathic helix binds membrane lipid and senses PC-deficient membranes. The
  PC-binding term GO:0031210 is the specific membrane-sensing readout (IBA from
  GO_Central plus Ensembl IEA).

## Structural / interchain disulfide

CCT is an obligate homodimer (SUBUNIT: Homodimer). Cys37 can form an in vitro interchain
disulfide that reports on the membrane-binding-coupled quaternary state
([PMID:15069071], MUTAGEN C37S; not in publications cache — abstract not read here).
Homodimerization (GO:0042803) and identical protein binding (GO:0042802) both reflect
this. GO:0042802 has direct IntAct support (P49585–P49585, self-interaction).

## Subcellular location

CCTα (unlike CCTβ isoforms) resides in the nucleus in addition to associating with the ER:
[PMID:10480912 "CCTalpha which resided in the nucleus in addition to associating with the
endoplasmic reticulum"]. GOA has IDA nucleus (GO:0005634), IDA ER (GO:0005783), and
IDA/is_active_in ER membrane (GO:0005789) all from PMID:10480912. UniProt subcellular
location: Cytoplasm/cytosol; Membrane (peripheral); ER membrane (peripheral); Nucleus.
Nuclear envelope (GO:0005635) is an Ensembl-projected refinement consistent with the
nuclear + ER localization. Cytosol (GO:0005829) = the inactive soluble pool.

glycogen granule (GO:0042587, ISS from mouse P49586) is an isolated, weakly supported
localization for the alpha isoform; kept as non-core.

## Isoform note

PMID:10480912 is primarily about identifying a new CCTβ2 splice variant; it explicitly
contrasts CCTα (nucleus + ER, ubiquitous) with CCTβ1/β2 (ER only). The IDA annotations
attributed to PCYT1A (CCTα) — catalytic activity, nucleus, ER, ER membrane, PC
biosynthesis, CDP-choline pathway — are the CCTα-specific findings and are correct for
this gene. Do not read the paper title's β2 focus as a mis-attribution.

## Disease

- Spondylometaphyseal dysplasia with cone-rod dystrophy (SMDCRD, MIM:608940), autosomal
  recessive; also isolated retinal dystrophy. Variants A99T, A99V, E129K, P150A, F191L,
  R223S ([PMID:24387990], [PMID:24387991]; biochemically characterized in
  [PMID:30559292]). Not in publications cache; from UniProt DISEASE/VARIANT blocks.
- Congenital generalized lipodystrophy 5 (CGL5, MIM:620680), autosomal recessive.
  Variants V142M, E280del ([PMID:24889630]). E280del removes a residue of the
  autoinhibitory helix and ~4-fold increases constitutive (lipid-independent) activity
  [PMID:30559292 "E280del, a single amino acid deletion in the autoinhibitory helix
  increased the"].

All disease variants converge on reduced fold stability / solubility and/or altered
catalysis of the one enzyme — i.e. loss (or dysregulation) of PC-synthesis flux
[PMID:30559292 "Disease-linked mutations in the phosphatidylcholine regulatory enzyme
CCTα impair enzymatic activity and fold stability"].

## Protein-binding IPIs (GO:0005515)

All four GO:0005515 IPI annotations come from high-throughput interactome screens with no
gene-specific functional claim:
- PMID:28514442 (BioPlex 2.0, AP-MS), PMID:33961781 (BioPlex 3.0, AP-MS),
  PMID:32296183 (HuRI, Y2H), PMID:40205054 (multimodal U2OS cell map, AP-MS + IF).
The UniProt INTERACTION block partners (AGTRAP, FKBP7, GYS1, MAGEA3, MOB1A, MOB3C,
NMNAT1, PCYT1B, RNF8, SCAMP1, SDCBP, SNAPIN, TNFRSF10D, VKORC1L1) are typical
HT-screen hits and none establish a specific biological function for CCTα. Per policy,
bare "protein binding" IPIs are marked as over-annotated (not removed).

## Non-core / over-projected process annotations

- B cell proliferation (GO:0042100) and isotype switching (GO:0045190): ISS/IEA from the
  mouse Pcyt1b (P49586, CCTβ) ortholog, reflecting the B-cell phenotype of CCTβ, not a
  demonstrated CCTα role. Over-annotation via ortholog transfer; kept as non-core.
- calmodulin binding (GO:0005516): Ensembl IEA projected from rat P19836; no primary
  human evidence in these files. Over-annotated.
- catalytic activity (GO:0003824): InterPro IEA, correct but uninformative parent of the
  specific MF (GO:0004105) → MODIFY to the specific activity.
- phosphatidylcholine metabolic process (GO:0046470): ARBA IEA parent of the specific PC
  biosynthetic process (GO:0006656) → MODIFY / redundant with the specific IDA term.

## Core function summary

- MF: choline-phosphate cytidylyltransferase activity (GO:0004105).
- MF (membrane-sensing): lipid binding (GO:0008289) / phosphatidylcholine binding
  (GO:0031210) via the amphipathic helix.
- BP: phosphatidylcholine biosynthetic process (GO:0006656) via the CDP-choline pathway
  (GO:0006657).
- Location: nucleus (GO:0005634), endoplasmic reticulum / ER membrane (GO:0005783 /
  GO:0005789), nuclear envelope (GO:0005635).
</content>
</invoke>
