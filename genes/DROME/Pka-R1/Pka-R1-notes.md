# Pka-R1 notes

Gene: Protein kinase, cAMP-dependent, regulatory subunit type 1 (Pka-R1; DRI), FBgn0259243,
CG42341. UniProt P16905 (KAPR1_DROME, Swiss-Prot, 376 aa, four isoforms; no FUNCTION comment).
PANTHER PTHR11635 (cAMP-dependent protein kinase regulatory chain), subfamily SF152.

## Sources and searches (2026-11-16)

- Cached GOA references: 18 PMIDs, mostly abstract-only. Full text available: PMID:22876196,
  PMID:26092715, PMID:26896675, PMID:37061542.
- FlyBase hand-written description (`Pka-R1-deep-research-flybase.md`).
- Searches run: WebSearch "Baum Li Perrimon 2000 Current Biology cyclase-associated protein CAP oocyte
  polarity PKA regulatory subunit Pka-R1 mutant actin"; "UAS-PKA-R* mutant regulatory subunit cannot bind
  cAMP dominant inhibitor Drosophila Li Ohlmeyer Lane Kalderon 1995"; Europe PMC
  `TITLE_ABS:("Pka-R1" OR "PKA-RI" OR "dPKA-RI") AND drosophila`. Read the Baum et al. 2000 article PDF from
  the Perrimon lab website (not cacheable as a publication) for the Pka-R1 experiment behind the actin and
  microtubule rows.
- Newly cached: PMID:14993189 (Yoshida et al. 2004, Oskar restriction), PMID:10858819 (O'Dell et al. 1999,
  courtship conditioning), PMID:3215511 (Kalderon and Rubin 1988, cloning).

## Molecular function

- Cloned with mammalian probes as the single fly type I regulatory subunit gene [PMID:3215511 "We have used
  mammalian probes to clone genes encoding the catalytic (C) and type I regulatory (RI) components of the
  cAMP-dependent protein kinase in Drosophila."]; 71% identical to mammalian RI. Multiple promoters give a
  full-length and two N-terminally truncated products [PMID:3215511 "A single Drosophila type I regulatory
  subunit gene is the source of at least three distinct transcripts originating from different promoters
  and spliced to a common body that would encode a full-length analog and two amino-terminally truncated
  variants of the mammalian RI protein."]. UniProt lists isoforms 1, 2, 3 and E.
- Domain architecture (UniProt features): N-terminal dimerization/docking region (RIIa/D-D domain, Pfam
  PF02197) with the interchain disulfides (Cys17-Cys38, by similarity), pseudophosphorylation (pseudosubstrate)
  motif 91-95, then two tandem cyclic-nucleotide-binding domains (Pfam PF00027 x2; cAMP-binding positions
  197/206 and 321/330).
- The classical dominant PKA inhibitor transgene UAS-R* (UAS-PKAinh1, "PKA-DN") is a Pka-R1 cDNA with
  mutations in both cAMP-binding sites (G196E, G321D according to the FlyBase UAS-R* records, FBtp0001595 and
  FBal0086779); it keeps the catalytic subunit in an inactive holoenzyme. This is the indirect fly evidence that Pka-R1 binds C subunit
  and cAMP. (FlyBase record seen through web search; not cached.)
- Loss-of-function evidence for the inhibitory activity: [PMID:9348350 "PKA activity in the absence of
  exogenous cAMP also was significantly higher than normal in homogenates from mutant adult heads."] and
  [PMID:14993189 "This phenotype is due to misregulation of PKA catalytic subunit activity and is suppressed
  by reducing catalytic subunit gene dosage."].

## Genuine Pka-R1 loss-of-function phenotypes

- Olfactory learning [PMID:9348350 "Flies homozygous for either of two mutant alleles showed specific defects
  in olfactory learning but not in subsequent memory decay."]; courtship memory [PMID:10858819 "PKA-RI males
  also modify their behavior towards virgin females after prior exposure to a fertilized female, but such an
  effect is short-lived, suggesting a defect in memory rather than learning."].
- Oocyte patterning [PMID:14993189 "Mutations in PKA-R1 cause premature and ectopic accumulation of Oskar
  protein throughout the oocyte."]. Not in GOA.
- FMRFa neuron specification marker changes (HMP, PMID:26092715) and sperm individualization (IMP,
  PMID:31391193, abstract-only).

## Annotations that rest on the R* dominant-negative transgene

The R* transgene is a mutant Pka-R1, so FlyBase attaches its phenotypes to Pka-R1, but the experiments use
it to block PKA catalytic activity; they report what PKA-C (Pka-C1) does, not what endogenous Pka-R1 does.
- Actin filament organization and oocyte microtubule cytoskeleton polarization (PMID:10985383, Baum et al.
  2000). The abstract is about capulet (CAP). The methods section of the article (lab PDF) states that the
  authors phenocopied the pka-C1 null by expressing UAS-pka-R1 from D. Kalderon in the germline with V32-Gal4;
  no Pka-R1 loss-of-function was examined. This is the source of the FlyBase sentence "contributes to actin
  filament and microtubule organization".
- Positive regulation of feeding behavior (PMID:22876196, full text cached): the authors expressed
  [PMID:22876196 "UAS-PKA-DN (a dominant-negative form of PKA)"] in sNPFR1 neurons, which reduced feeding. That
  shows PKA activity promotes feeding; the regulatory subunit that restrains PKA would, if anything, act in
  the opposite direction.
- Molting (PMID:11333238, abstract): [PMID:11333238 "The two pathways act in parallel to affect molting, as
  judged by phenotypes obtained through expression of dominant negative and dominant active forms of protein
  kinase A (PKA) in tissues that normally express the InsP(3) receptor."].
- Neuromuscular synaptic transmission (PMID:15295025, abstract): the paper studies central
  interneuron-to-motoneuron synapses [PMID:15295025 "To test this hypothesis, retrograde signaling between
  postsynaptic motoneurons and their presynaptic interneurons is examined."]; PKA is not mentioned in the
  abstract. Probably the PKA inhibitor transgene, but not verifiable.
- Response to ethanol (IDA, PMID:18675322, abstract): about PKC in NPF neurons [PMID:18675322 "Here we report a
  critical role of the conserved protein kinase C (PKC) pathway in mediating the intoxicating effect of
  ethanol."]; the Pka-R1 experiment is not visible.

## Hedgehog rows

FlyBase has 3 negative and 4 positive regulation of smoothened signaling rows on Pka-R1. PKA-C acts at two
steps: it promotes Ci processing to the repressor and blocks full-length Ci (negative), and it phosphorylates
Smo to activate it (positive). The R subunit acts only by setting PKA-C activity, and which genotype was used
(R* inhibitor, Pka-R1 loss of function) is not visible in the abstracts. Kept as non-core; direction for the
regulatory subunit not adjudicated.

## PANTHER/PAINT (PANTHER 19.0, PAINT 2026-08-28; IBD.gaf and treeinfo fetched 2026-11-16)

Path: PTN000180782 (family root, labelled Eubacteria; IBD GO:0005829 cytosol, GO:0007189
adenylate cyclase-activating GPCR signaling) > PTN004280545 (eukaryotic PKA R-subunit clade, horizontal
transfer event; IBD GO:0005952, GO:0004862, GO:0034236, GO:0030552) > PTN008325982 Eukaryota > Unikonts >
Metazoa-Choanoflagellida > Eumetazoa > PTN000180678 Bilateria (RI clade with PRKAR1A) > Protostomia > ... >
Pka-R1. PTN004280545 holds 291 of the family's leaves, including PRKAR1A/1B, PRKAR2A/2B, fly Pka-R2, worm
kin-2, yeast BCY1 and fission yeast Cgs1; the root's other children are three cyanobacterial/Chloroflexus
proteins. The root-level cytosol and GPCR-pathway IBDs therefore also reach those bacterial proteins, which is
a PAINT placement question outside this gene; fly Pka-R1 is inside the eukaryotic R-subunit clade where both
terms hold. No losses on the Pka-R1 lineage.

Verdicts on IBA rows no other row covers:
- GO:0004862 cAMP-dependent protein kinase inhibitor activity: ACCEPT (core).
- GO:0030552 cAMP binding: ACCEPT (core).
- GO:0034236 protein kinase A catalytic subunit binding: ACCEPT.
- GO:0005829 cytosol: ACCEPT.
- GO:0007189 adenylate cyclase-activating GPCR signaling pathway: ACCEPT (R subunit is the cAMP sensor of
  the pathway).

## FlyBase description verdict

"...encodes a cAMP-dependent protein kinase regulator" is correct. "contributes to actin filament and
microtubule organization" rests on overexpression of the R* PKA inhibitor in Baum et al. 2000: wrong as a
statement about Pka-R1 (PROBABLE, as the methods text is not in the cache). "involved in neuromuscular
synaptic transmission, molting and response to ethanol": molting is a dominant-negative PKA phenotype, the
synaptic paper is about central synapses and the ethanol paper about PKC; none is a Pka-R1 loss-of-function
finding (PROBABLE). The text omits the inhibitory mechanism and the genuine mutant phenotypes (olfactory
learning, Oskar restriction).

UniProt P16905: reviewed but has no FUNCTION comment; recorded as a MISSING_STATEMENT.
