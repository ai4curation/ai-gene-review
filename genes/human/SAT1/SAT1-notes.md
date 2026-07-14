# SAT1 (Diamine acetyltransferase 1 / SSAT1) — review notes

UniProt: P21673 (SAT1_HUMAN). Gene: SAT1 (HGNC:10540), synonym SAT, SSAT, SSAT-1.
171 aa, ~20 kDa, cytosolic. Chromosome Xp22.1. EC 2.3.1.57.

## Core biology (from UniProt P21673 authoritative record)

SAT1/SSAT1 is the **rate-limiting enzyme of polyamine catabolism / back-conversion**.
It is a cytosolic, acetyl-CoA–dependent GNAT-family (GCN5-related) N-acetyltransferase
that N1-acetylates the polyamines spermine and spermidine (and related diamines),
producing N1-acetylspermine / N1-acetylspermidine + CoA. The N1-acetylated products are
then either exported from the cell or oxidized by acetylpolyamine oxidase (PAOX), driving
back-conversion spermine → spermidine → putrescine.

- FUNCTION [file:human/SAT1/SAT1-uniprot.txt "Enzyme which catalyzes the acetylation of polyamines"].
  Substrate specificity norspermidine = spermidine >> spermine > N(1)-acetylspermine
  (PubMed:17516632). "This highly regulated enzyme allows a fine attenuation of the
  intracellular concentration of polyamines"; "Also involved in the regulation of polyamine
  transport out of cells" (PubMed:16455797). Also acts on 1,3-diaminopropane and
  1,5-diaminopentane.
- CATALYTIC ACTIVITY (three Rhea reactions in UniProt): (1) alkane-alpha,omega-diamine +
  acetyl-CoA = N-acetylalkane-alpha,omega-diamine + CoA + H+ (RHEA:11116; EC 2.3.1.57);
  (2) spermidine + acetyl-CoA = N(1)-acetylspermidine + CoA + H+ (RHEA:28150);
  (3) spermine + acetyl-CoA = N(1)-acetylspermine + CoA + H+ (RHEA:33099).
- KINETICS (UniProt): KM 3.8 uM acetyl-CoA; KM 5.7/3.7 uM spermine; KM 22/58 uM spermidine;
  kcat 8.7 s-1 (spermidine), 5 s-1 (spermine); pH optimum 8.0 (PubMed:15283699, 17516632).
- PATHWAY (UniProt): "Amine and polyamine degradation; putrescine degradation;
  N-acetylputrescine from putrescine: step 1/1." UniPathway UPA00188/UER00363.
- SUBUNIT: Homodimer [file:human/SAT1/SAT1-uniprot.txt "Homodimer"]
  (PubMed:16455797, 16544326, 17516632).
- SUBCELLULAR LOCATION: [file:human/SAT1/SAT1-uniprot.txt "Cytoplasm, cytosol"]
  (PubMed:1985966, 2241897).
- DISEASE: Overexpression of SAT1 and consequent putrescine accumulation might play a role
  in keratosis follicularis spinulosa decalvans (KFSD) [PubMed:12215835; UniProt DISEASE note].
- STRUCTURE: Ten X-ray structures (2B3U, 2B5G, etc.); GNAT/NAT_SF fold (CDD cd04301,
  Pfam PF00583, PROSITE GNAT PS51186); active-site proton donor Tyr140.

## Literature grounding for existing annotations

- **PMID:1985966** (Casero et al. 1991, cDNA cloning of human SSAT1): "Spermidine/spermine
  N1-acetyltransferase (Spd/Spm acetyltransferase) is the rate-limiting enzyme in the
  catabolism of polyamines. This enzyme is highly inducible by several stimuli, including
  the natural polyamines and their structural analogues." This is the original SAT1 cDNA
  characterization and the source of the TAS diamine-N-acetyltransferase annotation. Highly
  relevant, verified. [PMID:1985966 "rate-limiting enzyme in the catabolism of polyamines"]

- **PMID:16455797** (Bewley et al. 2006, PNAS, crystal structures): "Spermidine/spermine
  N1-acetyltransferase (SSAT) is a key enzyme in the control of polyamine levels in human
  cells, as acetylation of spermidine and spermine triggers export or degradation." WT and
  mutant human SSAT structures with CoA/AcCoA/spermine/inhibitor; homodimer; Y140F mutant
  reduces activity ~95%. Also reports self-acetylation of Lys26. Directly establishes the
  catalytic MF and homodimer. Source of the EXP diamine-N-acetyltransferase annotation and
  IPI identical-protein-binding (homodimer). [PMID:16455797 "a key enzyme in the control"];
  [PMID:16455797 "SSAT was found to self-acetylate lysine-26"].

- **PMID:17516632** (Hegde et al. 2007, Biochemistry, mechanism + structure): "The
  N1-acetylation of spermidine and spermine by spermidine/spermine acetyltransferase (SSAT)
  is a crucial step in the regulation of the cellular polyamine levels in eukaryotic cells."
  Random sequential kinetic mechanism; ternary complex; Tyr140 general acid, Glu92 general
  base; pH-activity bell-shaped. Source of the second EXP diamine-N-acetyltransferase
  annotation and the definitive kinetic/mechanistic characterization.
  [PMID:17516632 "The N1-acetylation of spermidine and spermine by spermidine/spermine"];
  [PMID:17516632 "crucial step in the regulation of the cellular"].

- **PMID:15283699** (Coleman et al. 2004, Biochem J). IMPORTANT: the paper's *primary*
  subject is **SSAT2 (SAT2, a paralog)**, and it concludes SSAT2 is NOT a polyamine catabolic
  enzyme. SSAT1 (this gene, P21673) is used throughout as the well-characterized comparator:
  "Spermidine/spermine-N1-acetyltransferase (SSAT1) is a short-lived polyamine catabolic
  enzyme inducible by polyamines and polyamine analogues"; "Induction of SSAT1 plays an
  important role in polyamine homoeostasis, since the N1-acetylated polyamines can be
  excreted or oxidized by acetylpolyamine oxidase." UniProt cites this PMID as EXP evidence
  for SAT1 catalytic activity (KM/kcat for spermine/spermidine measured on SSAT1). The GOA
  IDA annotations from this paper to SAT1 are therefore defensible for MF (diamine/
  N-acetyltransferase activity) — the full text characterizes SSAT1 activity as the reference
  standard. However the IDA to **GO:0006596 polyamine BIOSYNTHETIC process is wrong-direction**
  (SSAT1 is catabolic, not biosynthetic) — MODIFY to polyamine catabolic process.
  [PMID:15283699 "short-lived polyamine"]; [PMID:15283699 "inducible by polyamines and
  polyamine analogues"]; [PMID:15283699 "plays an important role in polyamine homoeostasis"].

- **PMID:11866539** (Aitkenhead et al. 2002, Microvasc Res): in-vitro angiogenesis model
  (EC tube formation in 3D collagen); representational difference analysis identified genes
  upregulated in tube-forming cells. SAT1 appears among the ~2- to 10-fold upregulated genes.
  This is an IEP expression-correlation annotation to GO:0001525 angiogenesis. The abstract
  foregrounds ESM-1/βig-h3/NrCAM; SAT1 is a co-identified upregulated transcript, not shown
  to have a causal angiogenic function. Keep as non-core (expression association, not the
  enzyme's evolved role). [PMID:11866539 "2- to 10-fold upregulation"].

- **Reactome R-HSA-351200 "Interconversion of polyamines"**, **R-HSA-351207 "Spermine =>
  N-acetylated spermine"**, **R-HSA-351208 "Spermidine => N-acetylated spermidine"**: model
  SAT1 as the cytosolic SSAT catalyzing the rate-limiting N1-acetylation step of polyamine
  back-conversion; the acetylated intermediates are oxidized by PAOX/SMOX. These support the
  TAS diamine-N-acetyltransferase MF and cytosol location. NOTE: GOA maps R-HSA-351200 to
  GO:0006596 polyamine *biosynthetic* process, which mislabels the interconversion pathway;
  the pathway is back-conversion (catabolic). MODIFY the BP to polyamine catabolic process.

## Protein–protein interaction annotations (IPI, GO:0005515 / GO:0042802)

The many GO:0005515 "protein binding" IPI annotations (PMID:16169070, 16189514, 19060904,
21516116, 25416956, 29892012, 31515488, 32296183, 32814053, 33961781) derive from
high-throughput yeast-two-hybrid / interactome and AP-MS proteome-scale screens (IntAct).
The partner lists are large, promiscuous, and non-overlapping across screens (APP, CASP7,
KCNA4, HOXB9, TCF25, PSMA1, etc.), with no coherent biological complex. These are
uninformative "protein binding" annotations — mark as over-annotated (not core), but per
policy do NOT remove experimental IPI. Bare "protein binding" is not used in core_functions.

The GO:0042802 "identical protein binding" IPI annotations (PMID:16189514 Y2H self-hit;
PMID:16455797 crystallographic homodimer; PMID:25416956 interactome self-hit) are supported
by the biologically real homodimer (UniProt SUBUNIT "Homodimer"; PubMed:16455797, 16544326,
17516632). These are ACCEPT — homodimerization is a genuine, structurally validated property.

## Curation decisions summary

- Core MF: **GO:0004145 diamine N-acetyltransferase activity** (EC 2.3.1.57).
- Core BP: **GO:0006598 polyamine catabolic process** (with spermidine/spermine catabolic
  as more specific), realized via N1-acetylation (GO:0032918 spermidine acetylation).
- Core CC: **GO:0005829 cytosol**.
- Homodimer (GO:0042802) accepted as a real structural property.
- polyamine *biosynthetic* process (GO:0006596) annotations MODIFY → polyamine catabolic
  process (wrong pathway direction; SSAT1 drives back-conversion/degradation).
- angiogenesis (IEP), polyamine metabolic process (IEA/ARBA, correct but general),
  acyltransferase activity (IEA/InterPro, general) → keep as non-core / over-annotated.
- Bare protein binding (GO:0005515) IPI → MARK_AS_OVER_ANNOTATED (do not remove; experimental).
