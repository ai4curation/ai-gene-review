# ACER3 (Q9NUN7) review notes

## Identity and core biology

ACER3 = alkaline ceramidase 3 (AlkCDase 3; alkaline phytoceramidase, aPHC; synonyms APHC, PHCA).
Human, 267 aa, single chain PRO_0000212463 [file:human/ACER3/ACER3-uniprot.txt].
EC 3.5.1.23 (ceramidase) / EC 3.5.1.- ; "Belongs to the alkaline ceramidase family"
[file:human/ACER3/ACER3-uniprot.txt].

Core molecular function: hydrolysis of ceramide (an N-acylsphingosine) + H2O -> sphingosine +
free fatty acid, at alkaline pH. This is GO:0017040 N-acylsphingosine amidohydrolase activity
(the ceramidase MF; def = "an N-acylsphing-4-enine + H2O = a fatty acid + sphing-4-enine", OLS).
There is no distinct "alkaline ceramidase" GOMolecularActivity term in the current GO; GO:0017040
is the correct and most specific ceramidase MF (this is what GOA uses).

Substrate preference: unsaturated long-chain (ULC) ceramides. UniProt FUNCTION:
"hydrolysis of unsaturated long-chain C18:1-, C20:1- and C20:4-ceramides, dihydroceramides and
phytoceramides into sphingoid bases like sphingosine and free fatty acids at alkaline pH"
[file:human/ACER3/ACER3-uniprot.txt]. In vitro ACER3 "only hydrolyzed C(18:1)-, C(20:1)-,
C(20:4)-ceramides, dihydroceramides, and phytoceramides" [PMID:20068046 abstract]. It
"specifically controls the hydrolysis of ceramides carrying unsaturated long acyl chains"
and "ACER3 controls the catabolism of ULC ceramides and dihydroceramides" [PMID:20068046].

Original cloning paper described it as an alkaline PHYTOceramidase: "novel human alkaline
ceramidase (aPHC) that hydrolyzes phytoceramide selectively" and "aPHC hydrolyzed phytoceramide
preferentially" [PMID:11356846 abstract]. Later work (PMID:20068046) refined the natural
substrate preference to unsaturated long-chain ceramides; phytoceramide is one of several
substrates (as efficient toward ULC dihydroceramides/phytoceramides as toward the ceramide
counterparts, per PMID:26792856 full text).

Enzyme mechanism / cofactors:
- Catalytic Zn2+: "a catalytic Zn2+ binding site in its core, similar to adiponectin receptors"
  [PMID:30575723 abstract]; UniProt COFACTOR Zn(2+) (ECO:0000269|PubMed:30575723); catalytic Zn2+
  ligands His81, His217, His221 in the crystal structure [file:human/ACER3/ACER3-uniprot.txt].
- Regulatory Ca2+: "we uncover a Ca2+ binding site physically and functionally connected to the
  Zn2+ providing a structural explanation for the known regulatory role of Ca2+ on ACER3 enzymatic
  activity" [PMID:30575723]. UniProt ACTIVITY REGULATION "Activated by 5 mM Ca(2+) and inhibited by
  5 mM Zn(2+)" [file:human/ACER3/ACER3-uniprot.txt]; pH optimum 9.5 [file...]; "activated by Ca(2+),
  but was inhibited by Zn(2+) and sphingosine" [PMID:11356846]. NB the Zn regulation quirk: the
  bound catalytic Zn is required, but excess (5 mM) free Zn2+ inhibits.

Topology / location: seven-transmembrane integral membrane enzyme
("ACER3 is an intramembrane enzyme with a seven transmembrane domain architecture" [PMID:30575723];
UniProt lists 7 TRANSMEM helices, though it names it a multi-pass membrane protein). Localizes to
ER and Golgi membranes: "localized in both the Golgi apparatus and endoplasmic reticulum"
(GFP-tagging) [PMID:11356846]; UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum membrane;
Golgi apparatus membrane; Multi-pass membrane protein [file:human/ACER3/ACER3-uniprot.txt].
Reactome R-HSA-428262 ("ACER3 hydrolyzes phytoceramide") annotates the ER-membrane location.

## Biological processes / physiology

- Ceramide catabolic process (GO:0046514) and sphingosine biosynthetic process (GO:0046512):
  core downstream of the ceramidase reaction. In erythrocytes ACER3-type alkaline ceramidase
  activity is "instrumental for SPH generation"; "SPH is only generated from the hydrolysis of
  ceramides via ceramidases"; "the generation of SPH and S1P are" increased during erythroid
  differentiation [PMID:20207939 abstract]. This controls the plasma S1P pool.
- Phytosphingosine biosynthetic process (GO:0071602): from phytoceramide hydrolysis
  ("phytoceramidase activity both in vitro and in cells" [PMID:11356846]). Retained but treated as
  a non-core sub-activity of the general ceramidase function (phytoceramide is one substrate class).
- Cell proliferation / programmed cell death (GO:0008284, GO:0043067): "down-regulation inhibits
  both cell proliferation and apoptosis" [PMID:20068046]; ACER3 knockdown up-regulates p21 and
  inhibits proliferation, and inhibits serum-deprivation apoptosis. These are downstream
  consequences of altered ceramide/sphingosine signalling — kept as NON_CORE (context-dependent
  regulatory outputs, not the evolved catalytic function).
- Myelination (GO:0042552): ACER3-E33G loss-of-function causes progressive early-childhood
  leukodystrophy (PLDECO, MIM:617762) [PMID:26792856; PMID:30575723]. IMP annotation from
  PMID:26792856 (patient/human genetics + biochemistry). "complex sphingolipids are the major lipid
  components of myelin" and "most defects of sphingolipid metabolism manifest solely by aberrant
  central myelination"; disease -> "accumulation of various sphingolipids in the blood and probably
  in the brain" [PMID:26792856]. NB: mouse Acer3 KO does NOT impair myelination but causes Purkinje
  degeneration/ataxia (PMID:30575723 intro) — so myelination is a human-disease-context process,
  retained as NON_CORE (a downstream/organism-level phenotype rather than the core molecular role).
- Inflammatory response (GO:0006954): IEA from mouse ortholog (Q9D099) via Ensembl; UniProt notes
  "may modulate the inflammatory response (By similarity)". Weak, orthology-transferred, kept
  NON_CORE (not directly demonstrated for the human gene).

## Disease

Leukodystrophy, progressive, early childhood-onset (PLDECO) [MIM:617762], autosomal recessive;
caused by homozygous p.E33G, which abolishes catalytic activity ("the p.E33G mutation inactivates
the catalytic function of ACER3" [PMID:26792856]). E33 sits in the N-terminal cytoplasmic Ca2+-
binding region; E33G destabilizes the Ca2+ site (PMID:30575723).

## Annotation-review decisions (summary)

Core MF: GO:0017040 N-acylsphingosine amidohydrolase activity (ceramidase). Strong IDA/IMP support
(PMID:11356846, PMID:20068046, PMID:20207939, PMID:26792856, PMID:30575723).
Core catalytic cofactor MF: GO:0008270 zinc ion binding (catalytic Zn2+, IDA PMID:30575723).
Regulatory MF: GO:0005509 calcium ion binding (IDA PMID:30575723) — regulatory, kept but framed as
supporting the ceramidase activity.
Core BP: GO:0046514 ceramide catabolic process; GO:0046512 sphingosine biosynthetic process.
Core CC: GO:0005789 ER membrane; GO:0000139 Golgi membrane.

Over-annotation / generality flags:
- GO:0016020 membrane (IEA InterPro, and IDA PMID:30575723): too general vs ER/Golgi membrane ->
  MARK_AS_OVER_ANNOTATED (do not remove the IDA per policy).
- GO:0006672 ceramide metabolic process (IEA InterPro) and GO:0006665 sphingolipid metabolic
  process (IEA UniPathway): correct but general parents of the specific ceramide catabolic process
  -> KEEP_AS_NON_CORE.
- GO:0071602 phytosphingosine biosynthetic process: real but a sub-branch of the ceramidase
  activity acting on phytoceramide -> KEEP_AS_NON_CORE.
- GO:0006954 inflammatory response (IEA, mouse ortholog) -> KEEP_AS_NON_CORE.
- GO:0008284 positive regulation of cell population proliferation, GO:0043067 regulation of
  programmed cell death -> KEEP_AS_NON_CORE (downstream signalling consequences).
- GO:0042552 myelination (IMP) -> KEEP_AS_NON_CORE (human disease-context phenotype).
No REMOVE actions: no clearly-wrong IEA (all IEAs map to real ceramidase/sphingolipid biology).
