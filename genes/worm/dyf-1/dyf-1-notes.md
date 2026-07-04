# dyf-1 (C. elegans) — Research Notes

UniProt: Q8I7G4 (TTC30_CAEEL) · WormBase: WBGene00001117 / F54C1.5 · Gene: dyf-1
("abnormal **dy**e **f**illing protein 1"). Member of the CAEEL_CILIOPATHY / IFT flagship
project (anterograde IFT-B).

## Provenance note: automated deep research unavailable

Automated deep research did not complete for this gene. `just deep-research-falcon worm dyf-1
--fallback perplexity-lite` ran but **both** providers failed: falcon (Edison) **timed out**
after 600 s ("Verbose Edison response has no answer. Status: in progress"), and the
perplexity-lite fallback returned **HTTP 401 – insufficient_quota** ("You exceeded your current
quota"). No `-deep-research-*.md` file was generated, and none was fabricated. This review is
therefore grounded directly in the UniProt entry, the GOA table, and the cached primary
publications (PMID:16049494, PMID:28479320, PMID:22922713, PMID:17761526, PMID:15916950), with
every `supporting_text` verbatim-verified against those cached publications.

## Summary / standalone picture

DYF-1 is a ~656-aa tetratricopeptide-repeat (TPR) protein (9 TPR repeats; TTC30/DYF-1/fleer
family; ortholog of human TTC30A/TTC30B and the algal/ciliate IFT70/FAP259) that is a subunit
of intraflagellar transport (IFT) complex B (IFT-B). It is expressed specifically in ciliated
sensory neurons and localizes to the ciliary base (basal body), the axoneme (axonemal
microtubules), and undergoes IFT along the cilium. Its best-defined role is as an obligatory
activator/adaptor for the homodimeric kinesin-2 motor OSM-3 (KIF17 ortholog): DYF-1 is
specifically required for OSM-3 to dock onto and move IFT particles. In *dyf-1* mutants OSM-3
is inactive, IFT particles are carried by heterotrimeric kinesin-II alone, the distal singlet
segments of the amphid/phasmid cilia are not built, and the animals are dye-filling defective
(Dyf). DYF-1/IFT70 is also required for tubulin polyglutamylation of the ciliary axoneme in
sensory neurons.

## Molecular identity

- 656 aa; 9 TPR repeats (UniProt features REPEAT 1–9); TPR-like all-α solenoid
  (IPR011990/IPR019734; PANTHER PTHR20931 "TETRATRICOPEPTIDE REPEAT PROTEIN 30"; InterPro TT30
  IPR039941). Two alternatively spliced isoforms (a = Q8I7G4-1 displayed; b = Q8I7G4-2 lacks
  residues 1–59) [file:worm/dyf-1/dyf-1-uniprot.txt].
- SIMILARITY: "Belongs to the TTC30/dfy-1/fleer family." [file:worm/dyf-1/dyf-1-uniprot.txt].
- Orthologs: human TTC30A/TTC30B; zebrafish *fleer* (flr); *Chlamydomonas*/*Tetrahymena* IFT70.
  The zebrafish fleer paper cloned "a tetratricopeptide repeat protein homologous to the
  Caenorhabditis elegans protein DYF1" [PMID:17761526 "Positional cloning flr identified a
  tetratricopeptide repeat protein homologous to the Caenorhabditis elegans protein DYF1 that
  was highly expressed in ciliated cells."].

## Core function 1 — OSM-3 kinesin-2 activator within anterograde IFT

The defining C. elegans finding (Ou et al. 2005, Nature): the amphid/phasmid channel cilia are
built by two anterograde IFT motors — heterotrimeric kinesin-II (builds the middle doublet
segment) and homodimeric OSM-3 (extends the distal singlet segment) — which normally move the
same IFT particles cooperatively. DYF-1 is the factor that couples OSM-3 to the IFT train:

- [PMID:16049494 "A conserved ciliary protein, DYF-1, is specifically required for OSM-3 kinesin
  to dock onto and move IFT particles"].
- [PMID:16049494 "OSM-3 kinesin is inactive and intact IFT particles are moved by kinesin-II
  alone in dyf-1 mutants"].
- Consequence: distal singlet segments fail to assemble, dye filling fails
  [PMID:16049494 disruption phenotype: "Sensory neurons are unable to take up a fluorescent dye
  from the media, a phenotype that is often associated with aberrant sensory cilia."].

The same study established DYF-1's ciliary localization and IFT behavior (basis of the
axonemal-microtubule / cilium IDA localization annotations). UniProt FUNCTION synthesizes:
"Specifically required for the kinesin osm-3 to dock onto and move the IFT particles which
contain these precursors." [file:worm/dyf-1/dyf-1-uniprot.txt].

## Core function 2 — IFT-B structural subunit (cilium assembly / cargo transport)

DYF-1 is a bona fide IFT complex B subunit, identified biochemically by mass spectrometry:
- UniProt SUBUNIT: "Component of the IFT complex B composed of at least che-2, che-13, dyf-1,
  dyf-3, dyf-6, dyf-11, dyf-13, ift-20, ift-74, ift-81, ifta-2, osm-1, osm-5 and osm-6."
  [file:worm/dyf-1/dyf-1-uniprot.txt]; ComplexPortal CPX-1290 (IFT complex B).
- Yi et al. 2017 (Curr Biol) identified DYF-1 in IFT-B by mass spectrometry and showed IFT-B is
  required for ciliary entry of the retrograde motor dynein-2:
  [PMID:28479320 "Disruption of the dynein-2 tail domain, light intermediate chain, or
  intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary localization, revealing
  their important roles in ciliary entry of dynein-2."]. This is the NAS source (ComplexPortal)
  for the cilium / IFT particle B / intraciliary transport / cilium-assembly annotations.

As an IFT-B subunit DYF-1 localizes to the ciliary basal body (docking/loading zone) — IDA
localization to GO:0036064 ciliary basal body is from PMID:22922713 (a C. elegans IFT study).

## Core function 3 — required for axonemal tubulin polyglutamylation

The DYF-1/fleer family is required for cilia tubulin polyglutamylation, shown in zebrafish and
confirmed directly in C. elegans dyf-1:
- [PMID:17761526 "flr cilia showed a dramatic reduction in cilia polyglutamylated tubulin,
  indicating that flr encodes a novel modulator of tubulin polyglutamylation."]
- [PMID:17761526 "We also found that the C. elegans flr homologue, dyf-1, is also required for
  tubulin polyglutamylation in sensory neuron cilia."]
- Loss is accompanied by B-tubule ultrastructural defects [PMID:17761526 "flr cilia exhibited
  ultrastructural defects in microtubule B-tubules, similar to axonemes that lack tubulin
  posttranslational modifications (polyglutamylation or polyglycylation)."].

Note: the GOA `protein polyglutamylation` (GO:0018095) IMP annotation is attributed to
PMID:16049494 (Ou 2005), whose abstract is entirely about IFT-motor coordination and does not
itself mention polyglutamylation; the function is definitively established for dyf-1 in
PMID:17761526. Treated as a real but non-core (downstream) role; supporting text drawn from
PMID:17761526.

## Expression / regulation

- Ciliated-sensory-neuron-specific: "Expressed in most amphid, both phasmid and several
  labial-quadrant neurons." [file:worm/dyf-1/dyf-1-uniprot.txt, from PMID:15916950].
- PMID:15916950 (Blacque et al. 2005, "Functional genomics of the cilium") is the SAGE / DAF-19
  X-box ciliary-transcriptome screen that placed dyf-1 among ciliated-cell genes (tissue
  specificity reference).

## What is NOT known (knowledge-gap candidates)

1. **Molecular mechanism of OSM-3 activation (MF-dark / ontology gap).** DYF-1 is genetically
   *required* for OSM-3 to dock onto and move IFT particles, but the biochemical activity is
   undefined: does DYF-1 bind OSM-3 directly, relieve OSM-3 autoinhibition, or bridge OSM-3 to
   the IFT-B core? No GO molecular-function term expresses "kinesin-2 docking/activation factor";
   the only informative MF available is `intraciliary transport particle B binding` (GO:0120170),
   which captures IFT-B membership, not the OSM-3-activation activity.
   Provenance: [PMID:16049494 "DYF-1, is specifically required for OSM-3 kinesin to dock onto and
   move IFT particles, because OSM-3 kinesin is inactive"] — establishes requirement, never a
   biochemical activity/interaction.

2. **Cause vs consequence of the polyglutamylation defect.** Whether DYF-1/IFT70 promotes tubulin
   polyglutamylation directly (e.g. by IFT-dependent delivery of a TTLL glutamylase or its
   substrate) or indirectly (as a downstream consequence of the B-tubule/axoneme structural
   defect) is unresolved. The zebrafish study frames flr as a "novel modulator of tubulin
   polyglutamylation" [PMID:17761526] without a molecular mechanism, and did not distinguish
   these possibilities.

3. **`protein localization to plasma membrane` (GO:0072659) evidence.** The basis of this IMP
   annotation (cited to PMID:16049494, abstract-only in our cache) cannot be verified from the
   available text; the abstract concerns IFT-motor coordination, not membrane-protein
   localization. Which ciliary/plasma-membrane cargo protein (if any) mislocalizes in dyf-1 is
   not established from the accessible evidence.

## Annotation-review disposition (planned)

- IFT-B membership / IFT / cilium / axonemal MT / basal body / IFT-B binding / cilium assembly:
  ACCEPT (well supported by IBA + experimental IDA/NAS; core IFT-B identity).
- intraciliary transport (IMP + IBA + NAS): ACCEPT (core; OSM-3 coupling directly shown).
- protein polyglutamylation (GO:0018095, IMP/PMID:16049494): KEEP_AS_NON_CORE — real but
  downstream; definitive evidence is PMID:17761526.
- protein localization to plasma membrane (GO:0072659, IMP/PMID:16049494): UNDECIDED — cannot
  verify supporting evidence from abstract-only cache; term is imprecise for a ciliary IFT role.
</content>
