# dyf-3 (C. elegans) research notes

UniProt: Q6I6D4 (CLUA1_CAEEL). WormBase: WBGene00001119 / C04C3.5. Gene: dyf-3.
Human ortholog: CLUAP1 (clusterin-associated protein 1); also known as IFT38 / qilin.
PANTHER family: PTHR21547 "CLUSTERIN ASSOCIATED PROTEIN 1". Pfam: PF10234 (Cluap1).
InterPro: IPR019366 (Clusterin-associated protein-1).

Note: the flagship project doc `projects/CAEEL_CILIOPATHY.md` lists dyf-3 as an
"IFT54 ortholog" — this is incorrect. dyf-3 is the CLUAP1/IFT38 ortholog (PANTHER
PTHR21547, Pfam Cluap1). dyf-11 is the true IFT54/TRAF3IP1 ortholog.

## Identity / orthology

- UniProt names the protein "Clusterin-associated protein 1 homolog" and states it
  "Belongs to the CLUAP1 family." 404 aa (isoform 1), 3 alternatively spliced isoforms
  (dyf-3a/b/c differing at the N-terminus).
- Structural features (UniProt): a long coiled-coil region (residues 176-306) and a
  C-terminal disordered, acidic region (328-382). No catalytic domain; no enzyme
  classification.
- Named "qilin" in some IFT literature: [PMID:25443296 "all IFT-B subunits, including
  the suspected subunit CLUAP1/DYF-3/qilin (Ou et al., 2005b), co-purified with
  IFT27[K68A] and with IFT27"].

## KNOWN (well supported)

### 1. Required for sensory cilium formation / ciliogenesis (C. elegans, experimental)
- dyf-3 mutants are Dyf (dye-filling defective) and have structurally abnormal cilia.
  [PMID:15713455 "we analyzed dyf-3 mutants that are defective in uptake of a fluorescent
  dye and abnormal in sensory cilium structure"].
- Loss of dyf-3 stunts cilia and causes ectopic posterior neuronal projections.
  [PMID:15713455 "the mutant has stunted cilia and abnormal posterior projections in
  some sensory neurons"].
- UniProt DISRUPTION PHENOTYPE: "Cilia of at least eight pairs of amphid neurons from
  mutant dyf(m185) animals are truncated at a middle segment, and empty amphidial
  sockets were seen indicating cilium structural abnormalities."
- GOA: cilium assembly (GO:0060271) IDA from PMID:15713455.

### 2. Component of the intraflagellar transport (IFT) complex B
- The dyf-3 gene product was predicted early on to act in IFT: [PMID:15713455 "DYF-3 may
  be involved in the intraflagellar transport system"].
- UniProt FUNCTION/SUBUNIT (from PMID:28479320): "Component of the intraflagellar
  transport (IFT) complex B ... IFT complex B composed of at least che-2, che-13,
  dyf-1, dyf-3, dyf-6, dyf-11, dyf-13, ift-20, ift-74, ift-81, ifta-2, osm-1, osm-5
  and osm-6."
- Vertebrate ortholog IFT38/CLUAP1 is an integral component of the IFT-B *peripheral*
  subcomplex: [PMID:26980730 "we identified TTC26/IFT56 and Cluap1/IFT38, neither of
  which was included with certainty in previous models of the IFT-B complex, as
  integral components of the core and peripheral subcomplexes, respectively"].
- Function depends on binding to other IFT-B subunits: [PMID:26980730 "a ciliogenesis
  defect of Cluap1-deficient mouse embryonic fibroblasts was rescued by exogenous
  expression of wild-type Cluap1 but not by mutant Cluap1 lacking the binding ability
  to other IFT-B components"].
- Co-purifies with the IFT-B complex: [PMID:25443296 "all IFT-B subunits, including the
  suspected subunit CLUAP1/DYF-3/qilin ... co-purified with IFT27"].
- GOA: intraciliary transport particle B (GO:0030992), intraciliary transport
  (GO:0042073), cilium (GO:0005929) — IBA and NAS/ComplexPortal.

### 3. Role in ciliary entry/retrograde transport of dynein-2 cargo (che-3)
- PMID:28479320 (Yi et al 2017) shows IFT-B is required for ciliary entry of dynein-2:
  [PMID:28479320 "Disruption of the dynein-2 tail domain, light intermediate chain, or
  intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary localization,
  revealing their important roles in ciliary entry of dynein-2"].
- UniProt FUNCTION (from PMID:28479320): "May be required for ciliary entrance and
  transport of specific ciliary cargo proteins such as che-3 which are related to
  motility." (che-3 = cytoplasmic dynein heavy chain / dynein-2). Note UniProt says
  "motile cilium" in the generic family sentence; C. elegans cilia are non-motile
  sensory cilia — the "motile" wording is generic CLUAP1-family text.

### 4. Localization: ciliated sensory neurons (dendrite, cell body, axon, cilium)
- Expressed in a defined set of ciliated chemosensory neurons: [PMID:15713455
  "Expression of a functional dyf-3...gfp fusion gene is detected in 26 chemosensory
  neurons, including six IL2 neurons, eight pairs of amphid neurons (ASE, ADF, ASG,
  ASH, ASI, ASJ, ASK and ADL) and two pairs of phasmid neurons (PHA and PHB)"].
- UniProt SUBCELLULAR LOCATION: axon, cilium, dendrite (all IDA from PMID:15713455).
- GOA IDA (PMID:15713455): axon (GO:0030424), dendrite (GO:0030425), cell projection
  (GO:0042995), neuronal cell body (GO:0043025). These reflect the pan-neuronal
  distribution of an IFT protein en route to/along the cilium; the cilium/ciliary base
  is the site of function.

### 5. Cell-autonomous, DAF-19/RFX–regulated ciliary gene
- [PMID:15713455 "dyf-3 acts cell-autonomously for fluorescent dye uptake"].
- [PMID:15713455 "Reduction of dyf-3...gfp expression in a daf-19 mutant suggests that
  dyf-3 expression is regulated by DAF-19 transcription factor"]. (X-box/RFX ciliary
  gene battery — consistent with a dedicated ciliary component.)

### 6. Required for cilia-dependent sensory behaviors (downstream/indirect)
- GOA IMP (PMID:23664973): chemotaxis (GO:0006935), chemosensory behavior (GO:0007635),
  response to alkaline pH (GO:0010446). PMID:23664973's abstract is about the guanylyl
  cyclase GCY-14 and does not name dyf-3; dyf-3 was assayed in the full text (as a
  Dyf/cilium-defective strain) — dye-filling/ciliary integrity is required for these
  amphid-mediated behaviors. These behaviors are downstream consequences of the loss
  of functional cilia, not a distinct molecular activity of DYF-3. Treat as NON-CORE.

## NOT known / knowledge gaps

- **Molecular/biochemical activity is undefined.** DYF-3/CLUAP1 has no catalytic
  activity and no assigned GO molecular function (GOA carries GO:0003674 ND). It is a
  structural/scaffold subunit of IFT-B; the exact interaction partners within IFT-B in
  C. elegans, and which specific cargo it adapts, are not established. The mouse work
  shows it must bind other IFT-B components to function but does not define a discrete
  molecular activity (PMID:26980730).
- **Which ciliary cargoes DYF-3 specifically adapts is uncertain.** UniProt hedges "May
  be required for ciliary entrance and transport of specific ciliary cargo proteins
  such as che-3" (PMID:28479320) — the "May" and single-cargo example show the cargo
  spectrum is not defined.
- **Core vs peripheral placement / stoichiometry in the worm** IFT-B is inferred from
  vertebrate biochemistry (PMID:26980730), not directly measured in C. elegans.
- **No GO MF term exists for "IFT-B structural subunit"** — an ontology gap; the gene
  reads MF-dark despite a well-defined cellular role (mirrors CFAP300 exemplar).

## Existing-annotation review plan (20 GOA annotations)

- cilium assembly (GO:0060271) IDA/IBA/NAS → ACCEPT (core). IDA is the strongest.
- intraciliary transport particle B (GO:0030992) IBA/NAS → ACCEPT (core CC / complex).
- intraciliary transport (GO:0042073) NAS → ACCEPT (core BP).
- cilium (GO:0005929) IBA/IEA/NAS → ACCEPT (site of function; is_active_in/located_in).
- microtubule organizing center (GO:0005815) IBA → KEEP_AS_NON_CORE or MODIFY. IFT
  proteins concentrate at the ciliary base (basal body region). The MTOC IBA is a
  broad phylogenetic call; basal body is the more specific/appropriate location.
- axon (GO:0030424) IDA/IEA, dendrite (GO:0030425) IDA/IEA, cell projection
  (GO:0042995) IDA, neuronal cell body (GO:0043025) IDA → KEEP_AS_NON_CORE. These
  reflect the neuronal distribution of the protein in transit; not the functional site.
- chemotaxis (GO:0006935), chemosensory behavior (GO:0007635), response to alkaline pH
  (GO:0010446) IMP → KEEP_AS_NON_CORE. Downstream cilia-dependent behaviors; do not
  REMOVE (experimental IMP, full text not in cache).
- molecular_function (GO:0003674) ND → ACCEPT as a genuine MF knowledge gap (do not
  invent an MF).

## Provenance policy
All supporting_text quotes above are verbatim substrings of the cached abstracts/
full-text in `publications/`. PMID:15713455, 23664973, 28479320 are abstract-only
(full_text_available: false); PMID:26980730 abstract-only; PMID:25443296 full text.
