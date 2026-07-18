# PAOX (Peroxisomal N(1)-acetyl-spermine/spermidine oxidase) — review notes

UniProt: Q6QHF9 (PAOX_HUMAN); gene PAOX (synonym PAO); HGNC:20837; EC 1.5.3.13.
511 aa; flavin monoamine oxidase family; FAD-dependent.

## Core biology

PAOX is the mammalian **peroxisomal polyamine oxidase (PAO / APAO)** that carries out the
oxidative arm of **polyamine back-conversion**. Together with spermidine/spermine
N1-acetyltransferase (SAT1/SSAT), it converts higher polyamines back to lower ones:
SAT1 first N1-acetylates spermine/spermidine, then PAOX oxidatively cleaves the
N1-acetylated substrate.

- N(1)-acetylspermine + O2 + H2O → 3-acetamidopropanal + **spermidine** + H2O2
  [file:human/PAOX/PAOX-uniprot.txt "Reaction=N(1)-acetylspermine + O2 + H2O = 3-acetamidopropanal +"; EC=1.5.3.13; Rhea:RHEA:25800]
- N(1)-acetylspermidine + O2 + H2O → 3-acetamidopropanal + **putrescine** + H2O2
  [file:human/PAOX/PAOX-uniprot.txt "Reaction=N(1)-acetylspermidine + O2 + H2O = 3-acetamidopropanal +"; Rhea:RHEA:25812]
- N(1),N(12)-diacetylspermine + O2 + H2O → 3-acetamidopropanal + N(1)-acetylspermidine + H2O2
  [file:human/PAOX/PAOX-uniprot.txt "Reaction=N(1),N(12)-diacetylspermine + O2 + H2O = 3-acetamidopropanal +"; Rhea:RHEA:25868]

**Substrate specificity** ranking: N(1)-acetylspermine = N(1)-acetylspermidine >
N(1),N(12)-diacetylspermine >> spermine; **spermidine is not a substrate**
[PMID:12477380 "a preference ranking of N1-acetylspermine= N1-acetylspermidine> N1,N12-diacetylspermine>>spermine; spermidine was not acted upon"].
This distinguishes PAOX from **spermine oxidase (SMOX/SMO)**, which prefers free
spermine over N1-acetylspermine [PMID:12477380 "distinctly different from the recently identified spermine oxidase (SMO), which prefers spermine over N1-acetylspermine"].
PAOX therefore acts on **acetylated** polyamines (the SAT1 products), whereas SMOX acts
on the free amine. UniProt notes substrate specificity:
[file:human/PAOX/PAOX-uniprot.txt "acetylspermine = N(1)-acetylspermidine > N(1),N(12)-diacylspermine >>"].

## Cofactor

Binds 1 FAD per subunit [file:human/PAOX/PAOX-uniprot.txt "Note=Binds 1 FAD per subunit."]. Multiple
FAD-binding residues annotated (24, 45, 53, 69-70, 247, 472, 481-482) by similarity to
mouse Q8C0L6. FAD/flavoprotein keyword present. GO cofactor term: FAD (ChEBI:CHEBI:57692).

## Localization

Peroxisomal. C-terminal tripeptide 509-511 is a **microbody (PTS1) targeting signal**
[file:human/PAOX/PAOX-uniprot.txt "/note=\"Microbody targeting signal\""]. UniProt
subcellular location: Peroxisome; Cytoplasm [file:human/PAOX/PAOX-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome"].
Reactome places PAOX activity in the peroxisomal matrix (R-HSA-141348, R-HSA-141351) and
also models its peroxisomal import as a PTS1 cargo of PEX5 (R-HSA-9033235/9033236).
The cytoplasm/cytosol annotations most plausibly reflect the newly-synthesized
pre-import pool and the SubCell "Cytoplasm" mapping; peroxisomal matrix is the functional
compartment.

## Function / regulation of polyamine pools

Overexpression of PAOX in HEK-293 lowered spermine ~30% and raised spermidine 2-4 fold
[PMID:12477380 "intracellular spermine pools decreased by approx. 30%, whereas spermidine increased 2-4-fold"],
consistent with its role in the regulation of intracellular polyamine concentration and as
a determinant of sensitivity to antitumor polyamine analogs
[file:human/PAOX/PAOX-uniprot.txt "Plays an important role in the"] /
[file:human/PAOX/PAOX-uniprot.txt "regulation of polyamine intracellular concentration and has the"].

Widely expressed; not detected in spleen; lower in neoplastic tissues; induced by polyamine
analogs [file:human/PAOX/PAOX-uniprot.txt "TISSUE SPECIFICITY: Widely expressed. Not detected in spleen. Expressed"].

## PMID:16354669 (Järvinen et al. 2006, J Biol Chem) — abstract only

Biochemical/enzymology paper on stereospecific degradation of alpha-methylpolyamines by
PAO. Confirms natural substrates: "The natural substrates for the enzyme are
N1-acetylspermidine, N1-acetylspermine, and N1,N12-diacetylspermine"
[PMID:16354669 "The natural substrates for the enzyme are N1-acetylspermidine, N1-acetylspermine, and N1,N12-diacetylspermine"]
and that PAO is "one of the key enzymes in the catabolism of polyamines spermidine and spermine"
[PMID:16354669 "one of the key enzymes in \nthe catabolism of polyamines spermidine and spermine"].
This paper is the GOA source for several human IDA annotations (putrescine biosynthesis,
positive regulation of spermidine biosynthesis, putrescine/spermidine/spermine catabolic
process, polyamine oxidase activity). The cached record is abstract-only
(full_text_available: false); the "biosynthetic"-direction annotations
(GO:0009446 putrescine biosynthesis; GO:1901307 positive regulation of spermidine
biosynthesis) are curator readings of the full text — PAOX generates putrescine and
spermidine as reaction products, so these are downstream product-formation framings of the
catabolic activity rather than PAOX being a biosynthetic enzyme. They are kept as non-core.

## Core function summary

- MF (core): N(1)-acetylpolyamine oxidase activity (GO:0052903); parent polyamine oxidase
  activity (GO:0046592); FAD binding (GO:0050660).
- BP (core): polyamine catabolic process (GO:0006598) via spermidine catabolic (GO:0046203)
  and spermine catabolic (GO:0046208) processes — the back-conversion arm.
- CC (core): peroxisome (GO:0005777) / peroxisomal matrix (GO:0005782).

## Action rationale highlights

- EXP/IDA MF and catabolic-process annotations from PMID:12477380 / PMID:16354669 → ACCEPT
  (core) or KEEP_AS_NON_CORE.
- GO:0016491 oxidoreductase activity (IEA, ARBA/InterPro) → too general → MODIFY toward
  GO:0052903.
- GO:0009446 putrescine biosynthetic process & GO:1901307 positive regulation of spermidine
  biosynthetic process (IDA) → experimental; KEEP_AS_NON_CORE (product-formation framing of
  the catabolic activity; not a biosynthetic function of PAOX).
- GO:0010509 intracellular polyamine homeostasis (IEA ortholog transfer) → KEEP_AS_NON_CORE
  (true but a high-level outcome, not the molecular/pathway core).
- GO:0008215 spermine metabolic process (IEA UniPathway) → general parent; KEEP_AS_NON_CORE.
- cytoplasm/cytosol CC → KEEP_AS_NON_CORE (pre-import / SubCell mapping); peroxisome is core.
</content>
