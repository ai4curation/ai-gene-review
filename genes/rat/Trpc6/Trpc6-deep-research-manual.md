# Trpc6 (rat) - manual literature synthesis

No deep-research provider was available for this session; this summary was written by the
reviewer from the cached publications in `publications/` and PubMed metadata.

## Identity

- UniProtKB A0ABK0M635 (TrEMBL, unreviewed), RGD:619788, NCBI GeneID 89823, 930 aa.
- Domain architecture: N-terminal ankyrin repeats, six predicted transmembrane helices
  (Phobius, residues ~403-723), TRP domain; InterPro IPR002153 (TRPC channel) and
  IPR005462 (TRPC6 channel); PANTHER PTHR10117:SF7 "SHORT TRANSIENT RECEPTOR POTENTIAL
  CHANNEL 6".
- The 930-residue length matches the rat TRP6A isoform cloned by Zhang and Saffen
  [PMID:11278449 "The longest isoform, rTRP6A, contains 930 amino acid residues"].

## Channel function

- Rat TRP6A/B expressed in COS cells increase Ca2+ influx and produce Ba2+ influx after
  M5 muscarinic receptor activation, but not after thapsigargin store depletion
  [PMID:11278449 "passive depletion of intracellular Ca(2+) stores with thapsigargin did not induce Ba(2+) influx in cells expressing rTRP6 isoforms"].
  The DAG analogue OAG activates rTRP6A (N-terminus 3-56 required)
  [PMID:11278449 "the N terminus (3-56 amino acids) is crucial for the activation of rTRP6A by diacylglycerol"].
- In A7r5 aortic smooth muscle cells, vasopressin activates a nonselective, OAG-activated,
  store-independent cation current with TRPC6-like properties
  [PMID:11788346 "TRPC6 is a molecular component of receptor-stimulated Ca(2+)-permeable cation channels in A7r5 smooth muscle cells"].
- Graham et al. (rat TRPC6A cDNA in HEK293T; endogenous TRPC6 in A7r5): H2O2 increases
  TRPC6 Ca2+ entry, open probability and whole-cell current; TRPC6 siRNA nearly abolishes
  the H2O2 current in A7r5 cells; oxidation also sensitizes the channel to DAG and promotes
  surface trafficking [PMID:20501650 "H(2)O(2) significantly increased TRPC6 channel open probability and whole-cell currents"].

## Localization

- Plasma membrane: TRPC6 colocalizes with the Na+/K+-ATPase at the plasmalemma and is
  surface-biotinylated in HEK cells [PMID:16025302]; H2O2 increases surface TRPC6
  [PMID:20501650].
- Podocyte slit diaphragm (mouse/human; Reiser et al. 2005, PMID:15924139, not cached;
  basis of the RGD ISO row from MGI).

## Interactions

- Immunoprecipitation-mass spectrometry from rat brain identified cytoskeletal (actin,
  spectrin, drebrin, myosin), endocytic (clathrin, dynamin, AP-2) proteins and the
  Na+/K+-ATPase; TRPC6-NKA co-IP confirmed in kidney, HEK and Sf9 cells
  [PMID:16025302 "TRPC6 coimmunoprecipitated with the NKA pump when the proteins were coexpressed in Spodoptera frugiperda insect cells"].
  Abstract only; co-IP does not establish direct binding to actin, actinin or clathrin.

## Physiology / phenotypes (context, not core)

- Chronic hypoxia upregulates TRPC6 in rat PASMCs; TRPC6 siRNA attenuates hypoxic
  increases in SOCE and basal [Ca2+]i [PMID:19889962].
- Neural progenitors: TRPC6 is upregulated in differentiated neurons; abstract states TRPC6
  siRNA had no significant effect on differentiation, while one results sentence reports that
  knockdown of either TRPC5 or TRPC6 suppressed differentiation [PMID:20479868].
- Hippocampal neurons: NT-4-induced Ca2+ influx through TRPC6 promoted dendritic growth,
  opposite to TRPC5/NT-3 [PMID:22764246 "the Ca(2+) influx through TRPC6 induced by NT-4 promoted the dendritic growth"].
