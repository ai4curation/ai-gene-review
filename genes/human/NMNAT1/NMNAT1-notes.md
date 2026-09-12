# NMNAT1 (human) review notes

UniProt: Q9HAN9 (NMNA1_HUMAN). Gene: NMNAT1 (HGNC:17877). 279 aa. Chromosome 1p.

## Identity and core catalytic function

NMNAT1 is the **nuclear isoform** of nicotinamide/nicotinic acid mononucleotide
adenylyltransferase (three human isoforms: NMNAT1 nuclear, NMNAT2 Golgi, NMNAT3
mitochondrial) [PMID:16118205 "Analyses of the subcellular localization confirmed NMNAT1 to be a nuclear protein, whereas NMNAT2 and -3 were localized to the Golgi complex and the mitochondria, respectively."].

It catalyses the central, shared adenylyl-transfer step of NAD+ biosynthesis. UniProt
records two EC numbers and two Rhea reactions:
- EC 2.7.7.1 (NMN adenylyltransferase): beta-nicotinamide D-ribonucleotide (NMN) + ATP + H+ = diphosphate + NAD+ [file:human/NMNAT1/NMNAT1-uniprot.txt "Reaction=beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate"].
- EC 2.7.7.18 (NaMN adenylyltransferase): nicotinate beta-D-ribonucleotide (NaMN) + ATP + H+ = deamido-NAD+ (NaAD) + diphosphate [file:human/NMNAT1/NMNAT1-uniprot.txt "Reaction=nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+)"].

Both EC assignments are experimentally supported by PubMed:17402747
[file:human/NMNAT1/NMNAT1-uniprot.txt "EC=2.7.7.1 {ECO:0000269|PubMed:17402747}"].
NMNAT1 uses NMN and the deamidated NaMN "with the same efficiency"
[file:human/NMNAT1/NMNAT1-uniprot.txt "Can also use the"] and thus sits at the convergence
of the de novo (kynurenine), salvage, and Preiss-Handler (NaMN -> NaAD -> NAD) routes.

FUNCTION comment: "Catalyzes the formation of NAD(+) from nicotinamide mononucleotide
(NMN) and ATP" [file:human/NMNAT1/NMNAT1-uniprot.txt]. It can also run the reverse
(pyrophosphorolysis of NAD+) and use tiazofurin monophosphate (TrMP)
[PMID:17402747 "TrMP is only a substrate with NMNAT1 and NMNAT3"].

Cofactor: divalent metal (Zn2+ gives higher activity than Mg2+)
[file:human/NMNAT1/NMNAT1-uniprot.txt "Zn(2+) confers higher activity as compared"].
Quaternary structure: homohexamer [file:human/NMNAT1/NMNAT1-uniprot.txt "Homohexamer (PubMed:11751893)"];
crystal structures 1KKU/1KQN/1KR2/1GZU/8QE8.

PATHWAY (UniProt): "NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1"
and "deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1"
[file:human/NMNAT1/NMNAT1-uniprot.txt].

## Localisation

Nuclear. NLS motif 123-129 [file:human/NMNAT1/NMNAT1-uniprot.txt "Nuclear localization signal"].
SUBCELLULAR LOCATION: Nucleus (multiple refs PMID:11248244, 12574164, 16118205, 22842230).
Also detected in nucleoplasm and nuclear bodies by HPA (IDA). Interacts with several
karyopherin-alpha importins (KPNA1/2/3/5/6) per IntAct, consistent with active nuclear import.

## Biologically meaningful interactions (focused studies)

- **PARP1 (ADPRT)**: NMNAT1 interacts with and strongly inhibits PARP1 in vitro
  [PMID:11248244 "NMNAT strongly inhibited recombinant human poly(ADP-ribose) polymerase 1"];
  UniProt SUBUNIT "Interacts with ADPRT/PARP1 (PubMed:11248244)". This is the P09874 IPI in GOA.
- **SIRT1**: NMNAT1 is recruited to target-gene promoters by SIRT1 and locally supplies NAD+
  to regulate SIRT1 deacetylase activity / transcription
  [PMID:19478080 "NMNAT-1 interacts with, and is recruited to target gene promoters by SIRT1"].
  This is the Q96EB6 IPI (PMID:19478080) in GOA.

## Nuclear ATP generation / chromatin remodeling

NMNAT1 participates (with PARP1, PARG, NUDT5/NUDIX5) in nuclear ATP synthesis from
poly-ADP-ribose, required for energy-consuming chromatin remodeling
[file:human/NMNAT1/NMNAT1-uniprot.txt "Involved in the synthesis of"];
the NUDIX5 paper establishes the pathway [PMID:27257257 "ADP-ribose is used by the pyrophosphatase NUDIX5 to generate nuclear ATP. The nuclear source of ATP is essential for hormone-induced chromatin remodeling"].
Underpins GO:1990966 ATP generation from poly-ADP-D-ribose (IDA, PMID:27257257).

## ISS/By-similarity roles transferred from mouse (Nmnat1, MGI:1913704)

UniProt (By similarity, from mouse ortholog Q9EPA7): "acts as a cofactor for glutamate and
aspartate ADP-ribosylation by directing PARP1 catalytic activity to glutamate and aspartate
residues on histones" [file:human/NMNAT1/NMNAT1-uniprot.txt] — basis for GO:0140768 (protein
ADP-ribosyltransferase-substrate adaptor activity, ISS) and GO:0045892 (negative regulation
of DNA-templated transcription, ISS). Also "Protects against axonal degeneration"
[file:human/NMNAT1/NMNAT1-uniprot.txt "Protects against axonal degeneration following"] — the
Wallerian-degeneration (Wld^S) connection; note NMNAT1 is the human homolog of the gene in the
Wld^S mouse (PMID:11891043, cited in UniProt refs). Neuroprotection "does not correlate with
cellular NAD(+) levels but may still require enzyme activity" (By similarity).

## Disease

- **Leber congenital amaurosis 9 (LCA9)**, MIM:608553 — many missense variants; several
  (e.g. E257K, R207W, N273D, V9M, R66W) reduce enzymatic activity; E257K mislocalizes to
  cytoplasm [file:human/NMNAT1/NMNAT1-uniprot.txt "the mutant localizes to the cytoplasm"].
  Refs PMID:22842227/22842229/22842230/22842231.
- **SHILCA** (spondyloepiphyseal dysplasia, sensorineural hearing loss, intellectual
  disability, LCA), MIM:619260, recessive; Alu-mediated duplication [PMID:32533184, UniProt].

## Annotation-review decisions (summary)

Core catalytic MF terms (author-supplied core_functions):
- GO:0000309 nicotinamide-nucleotide adenylyltransferase activity (EC 2.7.7.1) — ACCEPT (EXP/IDA).
- GO:0004515 nicotinate-nucleotide adenylyltransferase activity (EC 2.7.7.18) — ACCEPT (EXP/IDA).
Core BP: GO:0009435 NAD+ biosynthetic process; salvage-specific GO:0034355 is IBA and true but
narrower than the whole NMN->NAD role (NMNAT1 also serves de novo/Preiss-Handler), kept.
Core CC: nucleus (GO:0005634) / nucleoplasm (GO:0005654).

Over-annotations / generic terms:
- GO:0005515 protein binding (IPI) x9 — all from high-throughput interactome/proteomics screens
  (PMID:21516116, 24722188, 25416956, 25502805, 26871637, 28514442, 31515488, 32296183, 33961781);
  MARK_AS_OVER_ANNOTATED (uninformative bare term; keep, do not remove). PMID:11248244 (PARP1) and
  PMID:19478080 (SIRT1) are the two functionally informative binding annotations but the GO term is
  still bare "protein binding" -> KEEP_AS_NON_CORE with functional note.
- GO:0042802 identical protein binding (IPI) — reflects the real homohexamer; KEEP_AS_NON_CORE.
- GO:0003824 catalytic activity (IEA) and GO:0016779 nucleotidyltransferase activity (IEA) —
  parents of the specific MF; MARK_AS_OVER_ANNOTATED (subsumed by GO:0000309/GO:0004515).
- GO:0006163 purine nucleotide metabolic process (IEA, ARBA) — over-broad/tangential; MARK_AS_OVER_ANNOTATED.
- GO:0009165 nucleotide biosynthetic process (IEA + IC) — true but generic parent of NAD biosynthesis;
  KEEP_AS_NON_CORE.
- GO:1990966 ATP generation from poly-ADP-D-ribose (IDA, PMID:27257257) — real but non-core niche
  nuclear role; KEEP_AS_NON_CORE.
- GO:0045892 negative regulation of DNA-templated transcription (ISS) — via SIRT1/PARP1 chromatin
  role, By similarity from mouse; KEEP_AS_NON_CORE.
- GO:0140768 protein ADP-ribosyltransferase-substrate adaptor activity (ISS) — By similarity
  (directs PARP1 to Glu/Asp on histones); KEEP_AS_NON_CORE.
- GO:0016604 nuclear body (IDA, HPA) — KEEP_AS_NON_CORE.
