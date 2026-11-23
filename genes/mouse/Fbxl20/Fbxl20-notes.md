# Fbxl20 (mouse, Q9CZV8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Fbxl20 (SCRAPPER) is reviewed here as the experimentally characterised
reference relative for the donkey FBXL20 benchmark gene. ProtNLM2 output was not
consulted.

### Deep research
- `just deep-research-falcon mouse Fbxl20 --fallback perplexity-lite` failed: falcon
  returned "Edison API request failed: Failed to authenticate" (403) and the
  perplexity-lite fallback also failed. No deep-research file exists; this review is
  based on the primary literature cached in `publications/` (searched PubMed for
  Fbxl20/FBXL20/Scrapper and cached the relevant mouse papers).

### Evolutionary grounding
- PANTHER: PTHR13318:SF47 "F-BOX_LRR-REPEAT PROTEIN 20" (UniProt DR line and
  `interpro/panther/PTHR13318/PTHR13318-entries.csv`). Human Q96IG2 and bovine
  Q58DG6 are in the same subfamily. Note: the rat UniProt entry named Fbxl20
  (Q9QZH7, 276 aa fragment) is classified to PTHR13318:SF95, so it should not be
  assumed to be the same subfamily without checking.
- The two IBA rows (SCF ubiquitin ligase complex; SCF-dependent proteasomal
  ubiquitin-dependent protein catabolic process) come from PAINT node PTN002547163,
  a deep node whose donors are other FBXL proteins (human FBXL5/FBXL7/FBXL15 etc.,
  yeast and Arabidopsis F-box/LRR proteins). PAINT propagated only the generic SCF
  terms from this node, not any synapse-specific terms; the synaptic terms on mouse
  Fbxl20 come only from its own experiments (SynGO/MGI).

### Experimental evidence in mouse (PMID:17803915, Yao et al. 2007 Cell; full text)
- Domain architecture: F-box, LRRs, C-terminal CAAX (CIIL) prenylation motif
  [PMID:17803915 "SCRAPPER is a 438 amino acid protein that contains an F box,
  leucine-rich repeats (LRR), and a CAAX domain."]. The cloned 438-aa SCRAPPER is
  UniProt isoform 3 (Q9CZV8-3); the CAAX C-terminus is shared by all isoforms.
- SCF complex: [PMID:17803915 "SCRAPPER formed an SCF complex with Skp1 and Cullin1 in
  mouse brain lysates"].
- Direct substrate binding and ubiquitination of RIM1 (Rims1): [PMID:17803915
  "Purified recombinant SCRAPPER and C2B domain of RIM1 directly interacted in an in
  vitro pull-down assay"]; [PMID:17803915 "Thus, the SCRAPPER complex was sufficient to
  mediate ubiquitination of RIM1 in vitro."].
- In vivo: KO increases RIM1 half-life (0.7 h WT -> 5.0 h KO) and abolishes the MG132
  ubiquitin shift [PMID:17803915 "confirming that SCRAPPER enhances the rate of turnover
  of RIM1"]. beta-catenin half-life unchanged (specificity control).
- Localization: synaptic membrane fractions, punctate colocalization with
  synaptophysin; CAAX mutant C435A diffuse [PMID:17803915 "This indicates that the
  carboxyl-terminal prenylation signal is important for the distinct localization of
  SCRAPPER."]. Prenylation itself was inferred from the motif/mutant, not measured
  biochemically.
- Function at presynapse: KO increases AMPA mEPSC frequency, rescued by SCRAPPER
  re-expression or RIM1 knockdown; mixed-culture experiment places the effect
  presynaptically; KO reduces CA3-CA1 paired-pulse facilitation; proteasome-inhibitor
  effects on mEPSC largely lost in KO.

### Later mouse papers
- PMID:21390313 (Yao et al. 2011): SCR+/- mice impaired in contextual (not cued) fear
  conditioning; transgenic overexpression no effect. Organismal behaviour, downstream.
- PMID:23316391 (Takagi et al. 2012): KO shifts LTP/LTD thresholds at CA3-CA1 synapses.
- PMID:28292828 (Koga et al. 2017): in ACC, KO increases miniature and spontaneous
  glutamate release and blocks presynaptic LTP.
- PMID:32366828 (Eto et al. 2020): region-specific glutamate/GABA abundance changes in KO.
- PMID:18780397: imaging MS of KO brain; neurodegeneration pathology (abstract only).
- PMID:38211741: rat depression model, FBXL20 implicated in VGLUT1/VAMP1 degradation
  (rat, abstract only) - not used for mouse annotation.

### Other species (not transferred as mouse experimental facts)
- Human FBXL20: SCF-mediated degradation of VPS34 (PMID:25593308), PR55alpha
  (PMID:34731788). Same PANTHER subfamily, so the generic SCF substrate-adaptor role is
  shared, but these substrates have not been tested in mouse.

### Decisions
- Bare protein binding (IPI with Rims1) -> MODIFY to GO:1990756
  ubiquitin-like ligase-substrate adaptor activity: the paper shows direct binding of
  the substrate RIM1 plus SCF assembly and RIM1 ubiquitination.
- SynGO synapse terms: accept glutamatergic synapse and Schaffer collateral-CA1 synapse;
  the bare "synapse" rows are MODIFY -> glutamatergic synapse.
- behavioral fear response (acts_upstream_of_or_within, heterozygote behaviour):
  KEEP_AS_NON_CORE; downstream organismal phenotype, not a core function.
