# AMACR (human, Q9UHK6) — review notes

Deep research provider note: falcon deep-research is OUT OF CREDITS (HTTP 402) for this run,
so no `AMACR-deep-research-falcon.md` was generated. This review is grounded in the cached
UniProt record (`AMACR-uniprot.txt`), the seeded GOA (`AMACR-goa.tsv`), and the cached
`publications/PMID_*.md` (7 cited PMIDs, all present).

## Function (verified)

AMACR = alpha-methylacyl-CoA racemase (EC 5.1.99.4). Interconverts (R)- and (S)-epimers of
2-methyl-branched acyl-CoA esters.

- Acts only on CoA thioesters, not free fatty acids; wide substrate range including
  pristanoyl-CoA and trihydroxycoprostanoyl-CoA; not 3-methyl-branched or linear-chain acyl-CoAs.
  [PMID:7649182 "It acts only on coenzyme A thioesters, not on free fatty acids, and accepts as substrates a wide range of alpha-methylacyl-CoAs, including pristanoyl-CoA and trihydroxycoprostanoyl-CoA (an intermediate in bile acid synthesis), but neither 3-methyl-branched nor linear-chain acyl-CoAs."]
- Biological role: converts (2R)-methyl-branched acyl-CoAs to their (S)-stereoisomers, the only
  ones degradable by peroxisomal beta-oxidation. Required for peroxisomal breakdown of
  (2R)-pristanic acid and the (25R)-isomer of C27 bile-acid intermediates.
  [PMID:11060344 "2-Methylacyl-CoA racemase is an auxiliary enzyme required for the peroxisomal beta-oxidative breakdown of (2R)-pristanic acid and the (25R)-isomer of C(27) bile acid intermediates."]
  [PMID:10655068 "This enzyme is responsible for the conversion of pristanoyl-CoA and C27-bile acyl-CoAs to their (S)-stereoisomers, which are the only stereoisomers that can be degraded via peroxisomal beta-oxidation."]
- Also has a mitochondrial role: converts (2R,6)-dimethylheptanoyl-CoA to its (S)-isomer in
  mitochondrial beta-oxidation of pristanic acid breakdown products.
  [PMID:11060359 "the mitochondrial enzyme plays a crucial role in the mitochondrial beta-oxidation of the breakdown products of pristanic acid byconverting (2R,6)-dimethylheptanoyl-CoA to its (S)-stereoisomer."]

## Localization (verified)

Dual peroxisomal + mitochondrial. Single transcript, two topogenic signals.
- Bulk activity peroxisomal, 10–30% mitochondrial in human cells; peroxisomal form absent in
  Zellweger (peroxisome assembly deficiency) cells. [PMID:7649182]
- C-terminal KASL = novel PTS1 variant (ASL); mitochondrial targeting info between aa 22–85; a
  single transcript gives a protein with two topogenic signals → dual localization.
  [PMID:11060344 "our data show that a single transcript gives rise to a racemase protein containing two topogenic signals, explaining the dual cellular localization of the activity."]
- Bimodal peroxisome/mitochondrion from the same gene. [PMID:11060359 "alpha-methylacyl-CoA racemase is bimodally distributed to both the peroxisome and the mitochondrion."]
- UniProt SUBCELLULAR LOCATION: Peroxisome; Mitochondrion. C-terminal MOTIF 380..382 "Microbody targeting signal".
- Cytosol/cytoplasm annotations: cytosol TAS is from Reactome peroxisomal-import steps (protein
  transits cytosol en route to peroxisome, not a functional cytosolic pool). Cytoplasm IDA
  (PMID:15941950) is a breast-cancer IHC study reporting "cytoplasmic granules consistent with a
  mitochondrial and peroxisomal localization" — parent term, over-annotation vs the specific
  organelles.

## Disease (verified, UniProt)

- AMACR deficiency (AMACRD, MIM:614307): adult-onset sensorimotor neuropathy / relapsing
  encephalopathy; elevated pristanic acid and C27 bile-acid intermediates. [PMID:10655068]
- Congenital bile acid synthesis defect 4 (CBAS4, MIM:214950). [PMID:10655068, PMID:12512044]
- Inactivating variants S52P (AMACRD+CBAS4) and L107P (CBAS4) — enzyme inactive. (UniProt FT VARIANT)

## Family / structure

CoA-transferase III family (Pfam PF02515; InterPro IPR003673). ACT_SITE His122 (proton acceptor),
Asp152 (proton donor) by similarity to UniProtKB:O06543. Monomer [PMID:7649182 "It is a monomer of 47 kDa"].

## Annotation review decisions (summary)

- MF GO:0008111 racemase activity: multiple EXP/IDA/IMP/IBA/TAS/IEA — ACCEPT (core). EXP/IDA/IMP
  from human liver purification (7649182), subcellular study (11060359), disease IMP (10655068).
- CC peroxisome GO:0005777 (IDA/EXP/IBA/IEA) and peroxisomal matrix GO:0005782 (Reactome TAS):
  ACCEPT peroxisome (core location); matrix is the more precise soluble-matrix location — ACCEPT.
- CC mitochondrion GO:0005739 (IDA/EXP/IBA/IEA): ACCEPT — genuine second localization with a
  demonstrated mitochondrial catalytic role (11060359). HTP (34800366) mito hit: HTP large-scale,
  AMACR not named in cached text → UNDECIDED (evidence in supp tables, unverifiable here).
- CC cytosol GO:0005829 (Reactome TAS): part of peroxisomal-import machinery steps — transient,
  MARK_AS_OVER_ANNOTATED (not a functional cytosolic localization).
- CC cytoplasm GO:0005737 (IDA PMID:15941950): parent-of-organelle IHC over-annotation →
  MARK_AS_OVER_ANNOTATED (the specific peroxisome/mitochondrion terms are what should be used).
- BP bile acid biosynthetic GO:0006699 / bile acid metabolic GO:0008206: ACCEPT (core; racemase
  step in C27 bile-acid side-chain shortening).
- BP fatty acid beta-oxidation using acyl-CoA oxidase GO:0033540 (Reactome pristanoyl-CoA): ACCEPT
  (core; branched-chain FA degradation).
- BP fatty acid metabolic process GO:0006631 (IEA UniPathway): broad but correct — ACCEPT.
- MF catalytic activity GO:0003824 (IEA InterPro): correct but uninformative root-ish MF; the
  specific GO:0008111 supersedes it → MARK_AS_OVER_ANNOTATED.
</content>
</invoke>
