# DER (Gallus gallus, Q8JIS3) review notes

## 2026-10-20 session

### Deep research
`just deep-research-falcon CHICK DER --fallback perplexity-lite` failed: falcon returned
`403 Forbidden` at the Edison auth endpoint, and the perplexity-lite fallback also failed.
No deep-research file exists; this review is built from the cached primary literature and
the UniProt record.

### Experimental evidence in chicken (native enzyme, liver)
- Purified and crystallised from chicken liver; tetramer of ~22 kDa subunits; contains
  bound NADP+ [PMID:7358641 "The enzyme was found to contain up to 3 molecules of NADP+ per enzyme"].
- Activity: [PMID:7358641 "The enzyme was shown to catalyze the reduction of D-erythrulose to D-threitol with the concomitant oxidation of NAD(P)H to NAD(P)+, and was highly specific to D-erythrulose with an apparent Km of 0.38 mM"];
  NADPH preferred over NADH (Km 7.9 uM vs 67 uM).
- Also reduces alpha-diketones such as diacetyl [PMID:9538249 "it can catalyze reduction of not only D-erythrulose but also such diketones as diacetyl"].
  Diacetyl -> acetoin is a ketone -> secondary alcohol reduction, i.e. GO:0004090 carbonyl
  reductase (NADPH) activity (def: "a secondary alcohol + NADP+ = a ketone + H+ + NADPH").
  Acetoin stereochemistry is not stated in the abstract, so the stereo-specific diacetyl
  reductase terms are not proposed.
- Kidney and liver predominant [PMID:9538249 "D-Erythrulose reductase was predominantly located in the kidney and the liver of the chicken"].
- cDNA cloned from liver; 246 aa; identity of cDNA with the purified enzyme anchored by
  peptide sequencing (UniProt RP line: protein sequence of 32-56, 175-193, 211-225)
  [PMID:12200544]. >60% identity to mouse tetrameric lung carbonyl reductase (Cbr2), but
  differing substrate specificity and subcellular localisation; active-site substitutions
  (Asn192, His148) [PMID:12200544].
- Abstracts only cached (full_text_available: false for all three chicken papers).

### What is NOT established in chicken
- L-xylulose reductase activity: UniProt says only "May also catalyze the reduction of
  L-xylulose" and names it "Probable L-xylulose reductase". No chicken paper in the cache
  reports L-xylulose reduction, and the 1980 paper calls the enzyme "highly specific to
  D-erythrulose". L-xylulose reduction for this protein is a phylogenetic inference only.
- Participation in the uronate cycle / glucose metabolism: not studied in chicken.

### Evolutionary grounding
- PANTHER: PTHR44252 (D-ERYTHRULOSE REDUCTASE), subfamily SF3 (D-ERYTHRULOSE
  REDUCTASE-RELATED) [UniProt DR lines; interpro/panther/PTHR44252/PTHR44252-entries.csv].
- SF3 also holds C. elegans dhs-21 (Q21929; recombinant protein reduces L-xylulose with
  NADPH, PMID:21477590) and zebrafish dcxr (Q567K5).
- Mammalian DCXR (human Q7Z4W1, mouse Q91X52, rat Q920P0...) is SF2; mammalian Cbr2
  (mouse P08074, pig Q29529) is SF1. Mammalian DCXRs are NADPH-dependent dicarbonyl and
  L-xylulose reductases (PMID:11882650).
- All IBA rows derive from a single PAINT node, PANTHER:PTN001211870, which sits above the
  SF1/SF2/SF3 split (donors include mouse Cbr2 MGI:107200 = SF1, mammalian DCXR = SF2, and
  dhs-21 WBGene00000984 = SF3). Chicken DER is inside the clade.
- Note the donor composition differs by term: xylulose metabolic process and L-xylulose
  reductase include dhs-21 (SF3) as a donor; glucose metabolic process has mammalian DCXR
  donors only (SF2). So the glucose-metabolism claim rests entirely on the mammalian
  uronate-cycle interpretation.
- The shared SDR chemistry (dicarbonyl/sugar carbonyl reduction with NADPH) is the
  family-wide function; the specific sugar preference varies (D-erythrulose in chicken,
  L-xylulose in mammals and worm), so substrate preference should not be transferred
  across subfamilies without testing.

### Decisions
- GO:0047880 erythrulose reductase (IEA) -> ACCEPT, core; directly established.
- GO:0004090 carbonyl reductase (NADPH) (IBA) -> ACCEPT, core; supported by diacetyl
  reduction in chicken.
- GO:0050038 L-xylulose reductase (IBA, IEA) -> KEEP_AS_NON_CORE; phylogenetically sound
  inference, not shown in chicken.
- GO:0005997 xylulose metabolic process (IBA) -> KEEP_AS_NON_CORE, same reasoning.
- GO:0006006 glucose metabolic process (IBA) -> MARK_AS_OVER_ANNOTATED; indirect,
  mammal-only donors, broad.
- GO:0016616 (IEA ARBA) -> MODIFY to GO:0047880 / GO:0004090.
- GO:0005737 cytoplasm (IEA SubCell) -> ACCEPT (soluble liver enzyme; UniProt SubCell);
  weakly supported, no organelle evidence.
