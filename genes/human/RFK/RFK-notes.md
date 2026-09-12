# RFK (human riboflavin kinase) — review notes

UniProt: Q969G6 (RIFK_HUMAN), 155 aa, EC 2.7.1.26. HGNC:30324, chromosome 9. Gene ID 55312.

## Core function

RFK is **riboflavin kinase** (flavokinase, ATP:riboflavin 5'-phosphotransferase),
the first committed and rate-limiting step of flavin-cofactor biosynthesis in
humans. It phosphorylates riboflavin (vitamin B2) using ATP to produce flavin
mononucleotide (FMN); FMN is subsequently adenylylated to FAD by FAD synthase
(FLAD1). The reaction requires a divalent metal (Zn2+ or Mg2+).

- Catalytic activity (UniProt): `riboflavin + ATP = FMN + ADP + H(+)`, EC 2.7.1.26
  [file:human/RFK/RFK-uniprot.txt "Reaction=riboflavin + ATP = FMN + ADP + H(+)"].
- Rate-limiting for FAD synthesis
  [file:human/RFK/RFK-uniprot.txt "form flavin-mononucleotide (FMN), hence rate-limiting enzyme in the"].
- Cofactor: Zn2+ or Mg2+
  [file:human/RFK/RFK-uniprot.txt "Note=Zinc or magnesium."].
- Pathway: "Cofactor biosynthesis; FMN biosynthesis; FMN from riboflavin (ATP route): step 1/1"
  [file:human/RFK/RFK-uniprot.txt "(ATP route): step 1/1."].
- Reactome R-HSA-196964: "Phosphorylation of riboflavin (RIB) results in the
  formation of the first cofactor, flavin mononucleotide (FMN). This reaction is
  catalyzed by riboflavin kinase (RFK), a cytosolic enzyme existing as a monomer.
  It utilizes either zinc or magnesium ions in the reaction."

## Structure (PMID:12623014, PMID:14580199)

Crystal structures of human RFK: six-stranded antiparallel beta barrel core,
similar to the riboflavin synthase / ferredoxin-reductase FAD-binding fold; an
intrinsically bound MgADP defines a novel nucleotide-binding motif; catalysis
proposed through the active-site "arch"
[PMID:12623014 "The structure of human RFK revealed a six-stranded antiparallel beta barrel core"].
PDB: 1NB0, 1NB9, 1P4M, 1Q9S. ACT_SITE Glu79 (nucleophile). Mutagenesis E79Q
abolishes riboflavin kinase activity but not TNFRSF1A/CYBA binding
[file:human/RFK/RFK-uniprot.txt "E->Q: Loss of riboflavin kinase activity."].

PMID:12623014 is a structure paper; GOA also uses it as the NAS source for the
function/localization/pathway statements (author narrative), which is reasonable
but lower-value than the IDA/experimental support.

## Moonlighting: TNFR1 → NADPH oxidase (PMID:19641494)

Yazdanpanah et al. (Nature 2009) identified RFK as a TNFR1 (TNFRSF1A)-binding
protein that physically and functionally couples TNFR1 to NADPH oxidase. RFK
binds the TNFR1 death domain and the NADPH oxidase subunit p22phox (CYBA);
bridging is required for TNF-induced (not TLR-induced) ROS production. RFK's
enzymatic role — providing FAD, an essential prosthetic group of NADPH oxidase —
underlies the ROS phenotype (exogenous FMN/FAD substitutes for TNF stimulation in
RFK-deficient cells).
[PMID:19641494 "riboflavin kinase (RFK, formerly known as flavokinase) as a previously unrecognized TNF-receptor-1 (TNFR1)-binding protein that physically and functionally couples TNFR1 to NADPH oxidase"]
[PMID:19641494 "RFK is rate-limiting in the synthesis of FAD, an essential prosthetic group of NADPH oxidase"]

This is the source of the experimental annotations to `apoptotic process`
(GO:0006915, IMP), `positive regulation of NAD(P)H oxidase activity` (GO:0033864,
IMP), and `protein binding` (GO:0005515, IPI vs TNFRSF1A/P19438). These describe a
context-specific signaling role that is downstream of / built on the core flavokinase
activity — treated as KEEP_AS_NON_CORE (regulatory processes) or
MARK_AS_OVER_ANNOTATED (bare protein binding), not core evolved functions.

## Localization

UniProt SUBCELLULAR LOCATION: **Cytoplasm** (ECO:0000250)
[file:human/RFK/RFK-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]. Reactome
describes RFK as "a cytosolic enzyme." So cytoplasm / cytosol is the core location.

Other localization annotations are lower-confidence high-throughput / IEA calls:
- GO:0005739 mitochondrion — IBA (GO_REF:0000033) and HTP (PMID:34800366, a
  large-scale mitochondrial-proteome dataset). Not the primary site; a flavokinase
  supplies flavin cofactors cytosolically, and MitoCarta-type datasets frequently
  include cytosolic contaminants. Kept as non-core (do not remove HTP experimental-
  type; the IBA can be marked over-annotated).
- GO:0005794 Golgi apparatus — IDA from HPA immunofluorescence (GO_REF:0000052).
  Single antibody-based localization; not corroborated by UniProt or biochemistry.
  Marked as over-annotated (do not REMOVE — IDA experimental type).

## Interactions (protein binding IPI)

- PMID:19641494 IPI vs TNFRSF1A (UniProtKB:P19438 / P19438-1): the TNFR1 death-domain
  interaction — real but a signaling-context binding, bare GO:0005515 uninformative.
- PMID:32296183 IPI vs CNTLN (UniProtKB:Q9NXG0-2): from the HuRI binary interactome
  (Y2H) screen; UniProt records this interaction
  [file:human/RFK/RFK-uniprot.txt "Q969G6; Q9NXG0-2: CNTLN; NbExp=3;"]. High-throughput
  Y2H, no functional characterization — bare protein binding, over-annotated.

All bare `protein binding` (GO:0005515) IPI annotations → MARK_AS_OVER_ANNOTATED
(never REMOVE per policy; uninformative MF for the pathway/core-function view).

## Annotation action summary

Core (ACCEPT): riboflavin kinase activity (IDA, IBA, TAS, and the two IEA/NAS
duplicates for MF); FMN biosynthetic process; riboflavin metabolic process;
cytosol. FAD/FMN biosynthesis is the evolved function.

`riboflavin biosynthetic process` (GO:0009231, IEA InterPro2GO & NAS) is
technically a mislabel for a human context — humans do not synthesize the
riboflavin ring de novo; RFK acts in riboflavin *utilization* (FMN/FAD synthesis),
i.e. riboflavin metabolic process. MODIFY → GO:0006771 riboflavin metabolic
process (the IEA one); the NAS one likewise MODIFY.

Non-core / signaling: apoptotic process, positive regulation of NAD(P)H oxidase
activity (both IMP, KEEP_AS_NON_CORE — real moonlighting downstream of catalytic
function).
