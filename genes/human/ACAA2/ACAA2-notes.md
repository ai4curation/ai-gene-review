# ACAA2 (P42765, THIM_HUMAN) — Research Notes

Gene: ACAA2 / 3-ketoacyl-CoA thiolase, mitochondrial / acetyl-CoA acyltransferase 2 / T1
UniProt: P42765 (THIM_HUMAN), 397 aa, EC 2.3.1.16
HGNC:83; GeneID 10449; chromosome 18.

## Core biology

ACAA2 catalyzes the **fourth and last step of each round of the mitochondrial fatty acid
beta-oxidation spiral**: the thiolytic (CoA-dependent) cleavage of a 3-ketoacyl-CoA
(3-oxoacyl-CoA) into acetyl-CoA and a fatty acyl-CoA shortened by two carbon atoms.

From UniProt FUNCTION (P42765):
- [UniProt:P42765 "this is one of the enzymes that catalyzes the last step of the mitochondrial beta-oxidation pathway, an aerobic process breaking down fatty acids into acetyl-CoA"]
- [UniProt:P42765 "Using free coenzyme A/CoA, catalyzes the thiolytic cleavage of medium- to long-chain unbranched 3-oxoacyl-CoAs into acetyl-CoA and a fatty acyl-CoA shortened by two carbon atoms"]
- Reverse/biosynthetic direction: [UniProt:P42765 "Also catalyzes the condensation of two acetyl-CoA molecules into acetoacetyl-CoA and could be involved in the production of ketone bodies"]
- Side hydrolase activity: [UniProt:P42765 "Also displays hydrolase activity on various fatty acyl-CoAs (PubMed:25478839). Thereby, could be responsible for the production of acetate in a side reaction to beta-oxidation"]
- Pathway: [UniProt:P42765 "PATHWAY: Lipid metabolism; fatty acid beta-oxidation."]
- Subunit: [UniProt:P42765 "Homotetramer (PubMed:25478839). Interacts with BNIP3."]
- Location: [UniProt:P42765 "SUBCELLULAR LOCATION: Mitochondrion"]; Reactome places it in mitochondrial matrix (soluble matrix enzyme, distinct from the membrane-bound MTP).
- Family: [UniProt:P42765 "Belongs to the thiolase-like superfamily. Thiolase family."]

EC numbers assigned by UniProt: EC 2.3.1.16 (3-ketoacyl-CoA thiolase / acetyl-CoA
C-acyltransferase), EC 2.3.1.9 (acetyl-CoA C-acetyltransferase, the acetoacetyl-CoA
synthesis/cleavage reaction), and EC 3.1.2.1 / 3.1.2.- (acyl-CoA hydrolase side activity).

## Structure and mechanism (PMID:25478839, Kiema et al. 2014, abstract-only)

The crystal structure (PDB 4C2J/4C2K, 2.0 Å) of human mitochondrial T1 (hT1 = ACAA2):
- [PMID:25478839 "The structures confirm the tetrameric quaternary structure of this degradative thiolase."]
- Active site resembles a biosynthetic tetrameric thiolase rather than the peroxisomal dimeric degradative thiolase: [PMID:25478839 "The active site is surprisingly similar to the active site of the Zoogloea ramigera biosynthetic tetrameric thiolase ... and different from the active site of the peroxisomal dimeric degradative thiolase"]
- Intrinsic thioesterase/hydrolase activity confirmed: [PMID:25478839 "Soaking of the apo hT1 crystals with octanoyl-CoA resulted in a crystal structure in complex with CoA owing to the intrinsic acyl-CoA thioesterase activity of hT1. Solution studies confirm that hT1 has low acyl-CoA thioesterase activity for fatty acyl-CoA substrates. The fastest rate is observed for the hydrolysis of butyryl-CoA."]
- Biosynthetic (acetoacetyl-CoA-forming) activity: [PMID:25478839 "It is also shown that T1 has significant biosynthetic thiolase activity, which is predicted to be of physiological importance."]
- Active-site residues: Cys92 (acyl-thioester intermediate nucleophile) and Cys382 (proton donor/acceptor); mutagenesis of C92 and C382 decreased acyl-CoA hydrolase activity (UniProt FT MUTAGEN).
- Kinetics (UniProt, from PMID:25478839): KM 9.2 uM acetoacetyl-CoA; KM 250 uM acetyl-CoA; KM 35 uM octanoyl-CoA; kcat 14.8 s^-1 for acetoacetyl-CoA degradation, 1.4 s^-1 for acetoacetyl-CoA synthesis, 0.02 s^-1 for octanoyl-CoA hydrolysis (hydrolysis is a very slow side reaction).

This is the EXP/IDA basis for the GOA molecular-function annotations:
GO:0003988 acetyl-CoA C-acyltransferase activity (EC 2.3.1.16, the core thiolase),
GO:0003985 acetyl-CoA C-acetyltransferase activity (EC 2.3.1.9, acetoacetyl-CoA reaction),
GO:0003986 acetyl-CoA hydrolase activity and GO:0047617 fatty acyl-CoA hydrolase activity
(the slow thioesterase side reaction).

## BNIP3 interaction and apoptosis (PMID:18371312, Cao et al. 2008, abstract-only)

ACAA2 was identified as a BNIP3-binding partner in a membrane yeast two-hybrid screen:
- [PMID:18371312 "a modified split-ubiquitin membrane yeast two-hybrid system was constructed and used to identify acetyl-Coenzyme A acyltransferase 2 (ACAA2) as a new BNIP3 binding partner."]
- [PMID:18371312 "The interaction between BNIP3 and ACAA2 was confirmed by pull-down and co-immunoprecipitation assays. ACAA2 was also found to co-localize with BNIP3 in mitochondria."]
- [PMID:18371312 "the apoptosis induced by over-expressed BNIP3 via transfection or hypoxia treatment was abolished by ACAA2 in human hepatocellular carcinoma HepG2 cells and osteosarcoma U-2 OS cells."]
- [PMID:18371312 "These results strongly suggest that ACAA2 be a functional BNIP3 binding partner and provide a possible linkage between fatty acid metabolism and apoptosis of cells."]

This is the basis for the BHF-UCL/UniProt process annotations: GO:0005515 protein binding
(IPI with BNIP3 = UniProtKB:Q12983), GO:0071456 cellular response to hypoxia,
GO:1902109 / GO:1901029 negative regulation of mitochondrial membrane permeability /
outer membrane permeabilization in apoptosis, and GO:0005739 mitochondrion (IDA).
Note: this is an overexpression/co-IP study; the apoptosis-modulation role is a
secondary/contextual function (single lab, overexpression-based), not the core
catalytic function. Should be KEPT but as non-core where applicable.

## RNA binding (PMID:22658674, Castello et al. 2012, abstract-only)

High-throughput mRNA-interactome capture in HeLa cells. ACAA2 was among proteins
crosslinked to poly(A) RNA:
- [PMID:22658674 "We identify 860 proteins that qualify as RBPs by biochemical and statistical criteria ... shedding light on ... RNA-binding enzymes of intermediary metabolism"]
This is a proteome-wide HDA "moonlighting"-type detection, no gene-specific functional
follow-up for ACAA2. GO:0003723 RNA binding rests on an orthogonal high-throughput
screen; keep as non-core (not a characterized ACAA2 function).

## Cloning / cholesterol biosynthesis NAS (PMID:8241273, Abe et al. 1993, abstract-only)

Original cDNA cloning paper:
- [PMID:8241273 "The cDNA sequence of human mitochondrial 3-oxoacyl-CoA thiolase was determined ... encodes an amino acid sequence of 397 residues which exhibits 86.6% homology with that of the rat enzyme."]
The abstract describes only cloning/sequencing and Northern expression in liver,
fibroblasts, muscle. It does NOT mention cholesterol biosynthesis. The NAS
GO:0006695 cholesterol biosynthetic process annotation is not supported by this
abstract and is biologically implausible for a mitochondrial beta-oxidation thiolase
(cholesterol synthesis uses the cytosolic acetoacetyl-CoA thiolase ACAT2/cytosolic
HMG-CoA pathway, not mitochondrial ACAA2). Candidate REMOVE.

## Mitochondrial proteome (PMID:34800366, abstract-only / cache exceeds size)

High-confidence human mitochondrial proteome study; HTP localization of ACAA2 to
mitochondrion. Corroborates mitochondrial localization. ACCEPT (localization).

## Paralog distinctions (for term-choice reasoning)

- ACAA2 = soluble mitochondrial MATRIX 3-ketoacyl-CoA thiolase (T1), homotetramer,
  prefers medium/long straight-chain 3-oxoacyl-CoA. Distinct gene/enzyme from:
- HADHB = the long-chain 3-ketoacyl-CoA thiolase that is the beta-subunit of the
  membrane-bound mitochondrial trifunctional protein (MTP) complex (inner membrane).
- ACAT1 (T2) = mitochondrial acetoacetyl-CoA thiolase, ketone-body / isoleucine
  catabolism (EC 2.3.1.9 specialist).
- ACAA1 = peroxisomal 3-ketoacyl-CoA thiolase (dimeric, distinct active site).

## Annotation review summary plan

CORE (ACCEPT, molecular function):
- GO:0003988 acetyl-CoA C-acyltransferase activity (EC 2.3.1.16) — IDA PMID:25478839 = THE core MF.
- GO:0006635 fatty acid beta-oxidation — core BP.
- mitochondrial matrix / mitochondrion — core localization.

ACCEPT non-core / supporting MF:
- GO:0003985 acetyl-CoA C-acetyltransferase activity (EC 2.3.1.9) — demonstrated biosynthetic activity, secondary.
- GO:0003986 acetyl-CoA hydrolase / GO:0047617 fatty acyl-CoA hydrolase — slow in-vitro side activity (kcat 0.02/s); KEEP_AS_NON_CORE.

IEA generic acyltransferase (GO:0016746, GO:0016747): less informative parents of the
specific thiolase MF; MARK_AS_OVER_ANNOTATED / generalize (MODIFY to GO:0003988) — keep as ACCEPT-but-general; use MARK_AS_OVER_ANNOTATED since covered by specific term.

RHEA hydrolase chain-length terms (GO:0052815 medium-chain, GO:0052816 long-chain,
GO:0141126 short-chain fatty acyl-CoA hydrolase): auto from Rhea mapping of the in-vitro
thioesterase side reactions. Physiologically minor (very low kcat). KEEP_AS_NON_CORE.

REMOVE candidates:
- GO:0006695 cholesterol biosynthetic process (NAS PMID:8241273) — unsupported by the
  cited abstract, biologically wrong branch for mito beta-oxidation thiolase.

protein binding GO:0005515 (IPI BNIP3): do not endorse as core; KEEP_AS_NON_CORE
(documents real BNIP3 interaction but uninformative MF term).
</content>
