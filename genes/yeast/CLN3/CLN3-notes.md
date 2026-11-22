# CLN3 (P13365, *Saccharomyces cerevisiae*) - curation notes

Working journal for the GO annotation review in `CLN3-ai-review.yaml`. Aliases:
WHI1, DAF1, FUN10, YAL040C. Not to be confused with human CLN3 (battenin), an
unrelated lysosomal protein.

## 1. Biology in brief

Cln3 is the most upstream of the three budding-yeast G1 cyclins and the
functional analogue of metazoan cyclin D. It is a rare, very unstable
cyclin-box protein that binds the sole essential CDK Cdc28 (Cdk1) and confers a
weak but decisive kinase activity on it
[PMID:1316273 "Cln3 associates with Cdc28 to form an active kinase complex that phosphorylates Cln3 itself and a co-precipitated substrate of 45 kDa"]
[PMID:1316273 "We find that Cln3 is a very unstable, low abundance protein"].

The gene was discovered three times as a size-control / pheromone locus before
it was recognised as a cyclin:

- **WHI1** (Nash et al. 1988): the dominant *WHI1-1* truncation lets cells divide
  at abnormally small size and the wild-type gene is dose-dependent
  [PMID:2907481 "WHI1-1 is a dominant mutation that reduces cell volume by allowing cells to commit to division at abnormally small sizes, shortening the G1 phase of the cell cycle"]
  [PMID:2907481 "dosage studies indicated that the normal gene activated commitment to division in a dose-dependent manner"];
  the protein was recognised as a cyclin homolog
  [PMID:2907481 "The WHI1 protein had sequence similarity to clam cyclin A, to sea urchin cyclin and to Schizosaccharomyces pombe cdc13, a cyclin homolog"].
- **DAF1** (Cross 1988): *DAF1-1* gives small size and pheromone resistance; the
  deletion enlarges cells
  [PMID:3062366 "A chromosomal deletion of DAF1 produced by gene transplacement increased cell volume about 1.5-fold; thus, DAF1-1 may be a hyperactive or deregulated allele of a nonessential gene involved in G1 size control"].
- **CLN3** (Richardson et al. 1989): the three Cln proteins share an essential,
  redundant G1 function
  [PMID:2574633 "Mutational elimination of the CLN1, CLN2, and DAF1/WHI1 products leads to cell cycle arrest independent of cell type, while expression of any one of the genes allows cell proliferation"]
  [PMID:2574633 "The data are consistent with the hypothesis that Cln proteins activate the Cdc28 protein kinase, shown to be essential for the G1 to S phase transition in S. cerevisiae"].
  The triple-mutant arrest is a bona fide START arrest, independent of the
  pheromone pathway
  [PMID:2147225 "These results are consistent with a specific CLN requirement for START transit"]
  [PMID:2147225 "cln arrest is distinct from constitutive activation of the mating-factor signalling pathway"].

**Upstream activator model.** Tyers et al. 1993 showed that an early-G1 burst of
CLN3 accelerates Start and induces the other cyclin genes and SWI4, despite Cln3
being rare and weakly active
[PMID:8387915 "An artificial burst of CLN3 expression early in G1 phase accelerates Start and rapidly induces at least five other cyclin genes (CLN1, CLN2, HCS26, ORFD and CLB5) and the cell cycle-specific transcription factor SWI4"]
[PMID:8387915 "we propose that Cln3 may be an upstream activator of the G1 cyclins which directly catalyze Start"].

**Mechanism at promoters.** Cln3-Cdc28 acts on the SBF-bound repressor Whi5
(the yeast Rb analogue): Cln3 promotes Whi5 dissociation from SBF and *whi5*
deletion bypasses the need for Cln3
[PMID:15210110 "Whi5 inactivation bypasses the requirement for Cln3 both for transcriptional activation and cell cycle initiation"]
[PMID:15210111 "Deletion of WHI5 bypasses the requirement for upstream activators of the G1/S transcription factors SBF/MBF and thereby accelerates the G1/S transition"].
Cln3-Cdc28 and Pcl9-Pho85 act in parallel on Whi5 and dislodge the Rpd3/Hos3
HDACs
[PMID:19823668 "We show that a strain deleted for both PHO85 and CLN3 has a slow growth phenotype, a G1 delay, and is severely compromised for SBF-dependent reporter gene expression, yet all of these defects are alleviated by deletion of WHI5"]
[PMID:19823668 "phosphorylation by the early G1 CDKs Cln3-Cdc28 and Pcl9-Pho85 inhibits association of Whi5 with the HDACs"].
Cln3 is physically recruited to SBF at G1/S promoters
[PMID:19823669 "We found that Cln3 co-immunoprecipitates with the Swi6 component of SBF, and that this co-immunoprecipitation depends on Swi4"]
[PMID:19823669 "ChIP showed that Cln3 is found on the CLN2 promoter close to the SBF binding sites"].

**Localization.** Cln3 is predominantly nuclear with a C-terminal bipartite NLS
that is required for its Cln3-specific functions
[PMID:10611233 "Cln3p localization appears to be primarily nuclear, with the most obvious accumulation of Cln3p to the nuclei of large budded cells"]
[PMID:11509671 "Cln3p localization requires a bipartite nuclear localization signal (NLS) located at the C terminus of the protein"]
[PMID:11509671 "Mislocalized Cln3p, lacking the NLS, is much less active in genetic assays specific for Cln3p, but more active in assays normally specific for Cln2p"]
[PMID:11792824 "The G1 cyclin Cln3 required nuclear localization. An autonomous, nuclear localization sequence was found near the C-terminus of Cln3"].
In early G1, however, Cln3 is held at the ER with Cdc28 and released by the
Hsp40 Ydj1 only in late G1
[PMID:17560371 "We show here that Cln3 is retained bound to the ER in early G1 cells. ER retention requires binding of Cln3 to the cyclin-dependent kinase Cdc28, a fraction of which also associates to the ER"]
[PMID:17560371 "Cln3 contains a chaperone-regulatory Ji domain that counteracts Ydj1, a J chaperone essential for ER release and nuclear accumulation of Cln3 in late G1"].
Ssa1 (Hsp70) phosphorylation at T36 by Pho85 switches Ydj1 for Cln3 and
promotes Cln3 degradation under pheromone or nitrogen starvation
[PMID:23217712 "T36 phosphorylation triggers displacement of Ydj1, allowing Ssa1 to bind the G1 cyclin Cln3 and promote its degradation"]
[PMID:23217712 "The stress CDK Pho85 phosphorylates T36 upon nitrogen starvation or pheromone stimulation, destabilizing Cln3 to delay onset of S phase"].

**Size control.** Whether Cln3 accumulation or Whi5 dilution is the size sensor
is debated; single-cell measurements found Cln3 synthesis scales with size
[PMID:26390151 "although Cln3 concentration does modulate the rate at which cells pass Start, its synthesis increases in proportion to cell size so that its total concentration is nearly constant during pre-Start G1"].

**Pleiotropy.** Loss of Cln3, but not Cln1/Cln2, fragments the vacuole and
impairs its inheritance and cell-free fusion competence
[PMID:14573462 "loss of Cln3p, but not Cln1p or Cln2p, resulted in vacuolar fragmentation"]
[PMID:14573462 "cytosol prepared from cells lacking Cln3p had reduced vacuolar homotypic fusion activity in cell-free assays"].

**Open question (from the Falcon deep-research report).** The direct
physiological substrate of Cln3-Cdc28 is unsettled: Whi5 is the canonical
target, but a 2021 preprint proposes promoter-local phosphorylation of the Rpb1
CTD Ser5. Recorded under `suggested_questions`; not used to change any
annotation because the primary source is a preprint.

## 2. Review decisions

36 GOA rows plus one proposed NEW row. Summary of calls:

### ACCEPT (core)

- **GO:0000082 G1/S transition of mitotic cell cycle** (IBA, IGI x2, IMP) - the
  core process; IBD at node PTN000019791 (G1 cyclins) is sound and Cln3 has its
  own experimental support, so the target appearing in its own WITH/FROM is
  expected, not circular.
- **GO:0007089 traversing start control point** (IGI x2, IMP x2) - the classic
  WHI1/DAF1/CLN genetics; Start passage is exactly what these papers define.
- **GO:0000307 cyclin-dependent protein kinase holoenzyme complex** (IBA, IPI) -
  Cln3-Cdc28 is a directly demonstrated holoenzyme.
- **GO:0005634 nucleus** (IBA, IDA x3, IMP) - two labs, three methods, and the
  NLS mutagenesis all place the site of action in the nucleus.

### MODIFY

- **GO:0016538 CDK regulator activity -> GO:0061575 CDK activator activity**
  (IBA, IEA, IDA, IMP x2). The validator flagged the previous split (IBA/IEA
  ACCEPT vs. IDA/IMP MODIFY). Resolved by making all five rows MODIFY: the
  evidence in every case is that Cln3 association confers kinase activity on
  Cdc28, every member of the PAINT node is an activating cyclin (the family
  contains no CDK inhibitors), and the parent term is merely less informative.
  The IBA `propagation_review` root cause is `TERM_SCOPING_PROBLEM` with
  `SUPPORTS_TRANSFER` on the node - the transfer itself is valid.
- **GO:0005515 protein binding** (IPI x6). Repository policy: bare protein
  binding is uninformative. Five rows with Cdc28 (Uetz 2000, Reynard 2000,
  Hazbun 2003, Breitkreutz 2010, Truman 2012) -> GO:0019901 protein kinase
  binding for the high-throughput / interaction-only rows, and GO:0061575 for
  Reynard 2000, which measured Cln3-Cdc28 kinase activity directly
  [PMID:10913169 "The levels of Cln2-Cdc28 and Cln3-Cdc28 protein kinase activity are severely reduced in cks1-38 cell extracts"].
  One row with Swi6 (Wang 2009) -> GO:0008134 transcription factor binding, the
  interaction that recruits Cln3-Cdc28 to SBF-bound promoters.
- **GO:0006357 regulation of transcription by RNA polymerase II ->
  GO:0045944 positive regulation** (IGI x2, IMP). The sign is unambiguous:
  Cln3-Cdc28 relieves Whi5/HDAC repression of SBF/MBF. The G1/S context is
  carried by the GO:0000082 rows.
- **GO:1902806 regulation of cell cycle G1/S phase transition -> GO:1900087
  positive regulation of G1/S transition** (NAS on Hadwiger 1989, a CLN1/CLN2
  paper). Definition fits, sign is positive; far stronger evidence sits on the
  GO:0000082 / GO:0007089 rows.
- **GO:0044772 mitotic cell cycle phase transition -> GO:0000082** (IEA). ARBA
  generic parent; the specific transition is established.
- **GO:0042144 vacuole fusion, non-autophagic -> GO:0032889 regulation of
  vacuole fusion, non-autophagic** (IDA, IMP). A cyclin does not execute
  membrane fusion; the cell-free assay shows a requirement of cytosol for
  Cln3, i.e. an upstream regulatory role. Non-core.

### KEEP_AS_NON_CORE

- **GO:0007033 vacuole organization** (IMP, Han 2003). Specific to CLN3 and the
  curator read the full text, so retained, but a pleiotropic downstream
  consequence of reduced G1 CDK activity rather than a core function.

### MARK_AS_OVER_ANNOTATED

- **GO:0005737 cytoplasm** (IBA, `is_active_in`). Cln3 is present in the
  cytoplasm (the ER-retained early-G1 pool) but that pool is a sequestered
  pre-activation state; nuclear localization is required for its normal roles
  [PMID:11509671 "Thus, wild-type Cln3p requires nuclear localization to carry out its normal roles"].
  The clade-level cytoplasmic activity reflects Cln1/Cln2-type functions.
  Propagation review: `TERM_SCOPING_PROBLEM`, node
  `SUPPORTS_SOURCE_BUT_NOT_TARGET`. Not wrong as a location; over-stated as an
  activity site.

### NEW

- **GO:0005783 endoplasmic reticulum** (`located_in`, IDA, PMID:17560371).
  Added to close the gap between `core_functions` (which lists the ER as a
  location for the growth-timer function) and `existing_annotations`. The ER
  pool is a regulated, reproducible location (Verges 2007; Whi3-dependent
  retention in later work from the same group; Ydj1/Ssa1 handling in Truman
  2012), so a `located_in` annotation is justified. Deliberately *not*
  `is_active_in`: the ER is where Cln3 is held, not where it acts.

### No REMOVE or UNDECIDED calls

Every experimental row is consistent with the synthesized picture, and no
abstract-only record contradicts its annotation, so nothing was removed. The
abstract-only caches (Tyers 1992/1993, Richardson 1989, Cross 1988/1990, Nash
1988, Costanzo 2004, de Bruin 2004, Verges 2007, Han 2003, Uetz 2000,
Hazbun 2003, Breitkreutz 2010, Reynard 2000, Edgington 2001) all state the
relevant result in the abstract; full text is cached for Miller & Cross
2000/2001, Huang 2009, Wang 2009, Truman 2012 and Schmoller 2015.

## 3. Core functions

1. **Cdc28 activator at Start** - MF GO:0061575; BP GO:0000082, GO:0007089,
   GO:0045944; CC nucleus; complex GO:0000307.
2. **Growth-sensing timer** - the same MF/complex, BP GO:1900087; locations
   nucleus and endoplasmic reticulum (early-G1 retention, Ydj1 release,
   PEST/Ssa1-dependent turnover).

## 4. Validation log

- Initial state: valid with 3 warnings (inconsistent GO:0016538 actions; no
  deep-research citation; core-function ER location not in
  existing_annotations).
- Fixes: GO:0016538 IBA/IEA rows switched to MODIFY -> GO:0061575; the Falcon
  deep-research file cited (verbatim) on the cytoplasm and ER rows; NEW ER
  row added. A Truman 2012 quote was trimmed to avoid a non-breaking space in
  the cached text.
- Target: 0 errors, 0 warnings.
