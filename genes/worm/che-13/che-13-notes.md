# che-13 (Q93833, CHE13_CAEEL) research notes

Research journal for the AI GO-annotation review of *C. elegans* **che-13**
(WormBase WBGene00000492; ORF F59C6.7; UniProt Q93833).

## Identity / ortholog assignment (VERIFIED)

- che-13 = "Chemotaxis abnormal protein 13" / "Intraflagellar transport protein che-13".
- **IFT57 ortholog.** UniProt: `SIMILARITY: Belongs to the IFT57 family` (ECO:0000305).
  PANTHER family **PTHR16011 = IFT57/HIPPI** (subfamily PTHR16011:SF0 =
  "INTRAFLAGELLAR TRANSPORT PROTEIN 57 HOMOLOG"); Pfam **PF10498 (IFT57)**; InterPro
  **IPR019530 (Intra-flagellar_transport_57)**. So che-13 is the *C. elegans* ortholog
  of human **IFT57** (a.k.a. HIPPI/ESRRBL1). Confirms the task's stated assignment.
- Member of **IFT complex B (IFT-B)**: ComplexPortal **CPX-1290** "Intraflagellar
  transport complex B"; Reactome R-CEL-5620924 "Intraflagellar transport".
- 412 aa, one predicted C-terminal coiled-coil (302-393), N-terminal + central
  disordered/acidic regions. Two alternatively spliced isoforms (Q93833-1 "a" displayed;
  Q93833-2 "b"). No catalytic motif — a **structural/scaffolding subunit**, not an enzyme.

## What is KNOWN (with provenance)

### Molecular role: structural subunit of the IFT-B particle
- che-13 is a component of IFT complex B, the anterograde IFT particle.
  [PMID:12651157 "loss of che-13 differentially affects the localization of two known IFT complex B proteins, OSM-5 and OSM-6, implying that CHE-13 functions as part of this complex"]
- IFT-B membership confirmed biochemically / by mass-spec identification in the IFT-B
  complex. [PMID:28479320 abstract establishes IFT-B complex; UniProt SUBUNIT: "Component of the
  IFT complex B composed of at least che-2, che-13, dyf-1, dyf-3, dyf-6, dyf-11, dyf-13,
  ift-20, ift-74, ift-81, ifta-2, osm-1, osm-5 and osm-6" ECO:0000269|PubMed:28479320]
- Modular assignment placed che-13 in the IFT-B subcomplex module (Ou et al. 2007).
  [PMID:17314406 "the C. elegans IFT machinery has a modular design, consisting of modules IFT-subcomplex A, IFT-subcomplex B, and a BBS protein complex"]

### Behaves as an IFT protein (moves along the axoneme)
- CHE-13::GFP concentrates at the ciliary base and moves along the axoneme, i.e. it is a
  moving IFT-B particle component carried bidirectionally (anterograde + retrograde).
  [PMID:12651157 "Fluorescent-tagged CHE-13 protein concentrates at the base of cilia and moves along the axoneme as expected for an IFT protein"]
- IEP annotations to intraciliary anterograde (GO:0035720) and retrograde (GO:0035721)
  transport derive from this movement (PMID:12651157).

### Required for building the ciliary axoneme (ciliogenesis)
- che-13(e1805) mutants: **normal transition zones but severely shortened axonemes**, with
  ectopic doublet microtubules — a cilium-assembly (not transition-zone) defect.
  [PMID:2428682 "The cilia in che-13 (e1805), osm-1 (p808), osm-5 (p813), and osm-6 (p811) mutants have normal transition zones and severely shortened axonemes. Doublet-microtubules, attached to the membrane by Y links, assemble ectopically proximal to the cilia in these mutants"]
- che-13 is "required for cilia assembly and whose function is disrupted in che-13
  ciliogenic mutants". [PMID:12651157 "a novel C. elegans gene, F59C6.7/9, that is required for cilia assembly and whose function is disrupted in che-13 ciliogenic mutants"]
- IGI cilium-assembly annotation from the dauer-pathway genetics: che-13 is one of the
  cilium-structure genes whose mutation gives structurally defective chemosensory cilia.
  [PMID:1732156 "Dauer-defective mutations in nine genes cause structurally defective chemosensory cilia, thereby blocking chemosensation"]
- *C. elegans* sensory cilia are **non-motile** — hence "non-motile cilium assembly"
  (GO:1905515) is the appropriately specific cilium-assembly term.

### Localization (CC)
- Base of cilia / basal body, transition zone, along the axoneme.
  [PMID:12651157 "concentrates at the base of cilia and moves along the axoneme"] and
  UniProt SUBCELLULAR LOCATION: "Cytoplasm, cytoskeleton, cilium axoneme ... Moves along the axoneme".
- IDA localizations in GOA: axoneme (GO:0005930, PMID:12651157/18337471), ciliary
  transition zone (GO:0035869, PMID:12651157), ciliary basal body (GO:0036064,
  PMID:22922713/ISS). ComplexPortal NAS cilium (GO:0005929).

### Required for localizing other IFT proteins into cilia
- Loss of che-13 mislocalizes IFT-B proteins OSM-5 and OSM-6 → basis of the "protein
  localization" IMP (GO:0008104). More precisely this is protein localization *to cilium*.
  [PMID:12651157 "loss of che-13 differentially affects the localization of two known IFT complex B proteins, OSM-5 and OSM-6"]

### Regulation / expression
- Expressed in ciliated sensory neurons; transcription controlled by the RFX factor
  **DAF-19** (X-box), like other IFT-B genes.
  [PMID:12651157 "expression of che-13 (F59C6.7/9) is regulated by the RFX-type transcription factor DAF-19, suggesting a conserved transcriptional pathway in ciliogenesis"]

### Downstream (non-core) phenotypes
- che-13 mutants are **dye-filling / chemosensory defective** and fail osmotic avoidance;
  these are *downstream consequences* of defective sensory cilia, not a direct signalling
  activity of CHE-13. [PMID:2428682 "Mutations in 14 genes prevent dye uptake and disrupt chemosensory behaviors"]
- UniProt DISRUPTION PHENOTYPE: "defects in ciliary structure resulting in defects in ...
  osmotic avoidance behavior ... affects the localization of IFT complex B proteins,
  osm-5 and osm-6 ... Shortened axonemes of all classes of sensory cilia in the head.
  Required for mating." (ECO:0000269|PubMed:12651157, PubMed:2428682).

## What is NOT known (candidate knowledge gaps)

1. **Intra-complex contacts of CHE-13/IFT57 in the worm are not mapped.** In vertebrates
   IFT57 sits in the IFT-B1 peripheral region and helps bridge IFT-B to the IFT-A/dynein-2
   handoff (and IFT57 loss destabilizes IFT-B), but which IFT-B subunits CHE-13 directly
   contacts in *C. elegans*, and via which region (the coiled-coil vs the disordered N/central
   segments), is undetermined. GOA carries only the generic root MF (GO:0003674, ND) —
   no subunit-level MF term exists.
2. **No independent biochemical/enzymatic activity** is known or expected for CHE-13;
   whether the che-3/motility-cargo "entrance" role suggested by UniProt reflects a
   direct CHE-13 cargo-selection activity vs a general IFT-B requirement is unresolved.
   [UniProt FUNCTION "May be required for ciliary entrance and transport of specific
   ciliary cargo proteins such as che-3 which are related to motility (PubMed:28479320)"]
3. **Isoform-specific function.** Two splice isoforms (a/b differ in the first ~119 aa);
   whether the two isoforms have distinct roles/expression is unstudied.

## Annotation-review plan (summary)

- Keep as **core**: IFT-B membership (GO:0030992, part_of), intraciliary transport
  (GO:0042073), cilium assembly (GO:0060271) + non-motile cilium assembly (GO:1905515),
  anterograde/retrograde intraciliary transport (GO:0035720/0035721), and the ciliary
  localizations (axoneme, transition zone, basal body, cilium).
- **MODIFY** GO:0008104 intracellular protein localization → GO:0061512 protein
  localization to cilium (more specific; supported by OSM-5/OSM-6 mislocalization).
- **KEEP_AS_NON_CORE**: microtubule organizing center (GO:0005815, IBA; generic parent of
  the experimentally supported ciliary basal body), chemosensory behavior (GO:0007635,
  downstream sensory phenotype), ND root MF (GO:0003674).
- **MARK_AS_OVER_ANNOTATED**: Golgi apparatus (GO:0005794, IBA) — no experimental support
  in worm; over-propagated from the IFT57/HIPPI family; CHE-13 is a ciliary/basal-body
  protein.
- Add a **NEW** structural-molecule-activity MF (GO:0005198) as the subunit-level MF, per
  the osm-6 precedent, and propose a dedicated "structural constituent of IFT particle" term.

## Provenance / cache status
- All 8 cited PMIDs cached in `publications/`. Only PMID:22922713 has full text; the rest
  are abstract-only (verified `full_text_available:` flags). Experimental IDA/IMP/IGI/IEP
  annotations citing abstract-only papers are NOT overruled on cached-text grounds
  (curator read full text), per repo guidance.
</content>
</invoke>
