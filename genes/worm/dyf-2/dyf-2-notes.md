# dyf-2 (C. elegans) — research notes

UniProt: G5ECZ4 (DYF2_CAEEL). Gene: dyf-2 / ift-144 / ZK520.3 (WBGene00001118). 1364 aa.
Human ortholog: **WDR19** (= IFT144 in *Chlamydomonas*). Part of the **IFT-A** (intraflagellar
transport complex A) machinery. Flagship project: `projects/CAEEL_CILIOPATHY.md`.

Domain architecture (UniProt/InterPro): N-terminal WD40 β-propeller repeats (WD 1–5) followed by
a long C-terminal TPR (tetratricopeptide) α-solenoid (TPR 1–7). This WD40-propeller + TPR-solenoid
architecture is the signature of the large IFT-A/IFT-B "core" subunits (IFT144/140/122/172/80).
There is **no catalytic domain** — DYF-2 is a scaffolding/structural subunit.

## What is KNOWN (with provenance)

### Identity: DYF-2 is the WDR19/IFT144 ortholog, an IFT-A component
- [PMID:16957054 title: "Caenorhabditis elegans DYF-2, an orthologue of human WDR19, is a component
  of the intraflagellar transport machinery in sensory cilia."]
- [PMID:22922713 "DYF-2 protein (Fig. 1a, b), a known IFT component that is the ortholog of human
  WDR19 (also known as IFT144 in Chlamydomonas)"]
- [PMID:22922713 "In Chlamydomonas, IFT144 (the homolog of DYF-2) is an IFT-A component"]
- UniProt SUBUNIT: "Component of the IFT complex A (IFT-A) composed of at least che-11, daf-10,
  dyf-2, ift-139, ift-43 and ifta-1." ComplexPortal CPX-1289 = Intraflagellar transport complex A.
- Mass-spec identification of DYF-2 in IFT complex A: PMID:28479320 (Yi et al. 2017; UniProt RN[4]:
  "IDENTIFICATION IN IFT COMPLEX A, AND IDENTIFICATION BY MASS SPECTROMETRY").

### Localization: ciliary; expressed in ciliated sensory neurons
- [PMID:16957054 "the mouse orthologue of DYF-2, WDR19, also localizes to cilia, pointing to an
  important evolutionarily conserved role for this WDR protein in cilia development and function"]
- UniProt SUBCELLULAR LOCATION: Cell projection, cilium. TISSUE SPECIFICITY: ciliated sensory
  neurons. *C. elegans* sensory cilia are **non-motile** (GO:0097730).

### Function: retrograde IFT / IFT turnaround; cilium assembly & integrity
- Structural role in the IFT particle: [PMID:22922713 "indicating that G361R mutation is a
  hypomorphic allele that does not affect the major role of DYF-2 as an IFT structural protein"].
- Null allele = loss of cilia + loss of IFT: [PMID:22922713 "the latter show severely truncated
  cilia and completely disrupted IFT transport"] (re dyf-2(m160) null).
- Retrograde transport: the hypomorphic WD40 allele dyf-2(jhu616) selectively loses retrograde IFT:
  [PMID:22922713 "in dyf-2(jhu616), IFT-B component OSM-6 showed characteristic anterograde IFT
  movement, but lost almost all retrograde IFT movements"].
- Mechanistic role at the tip: [PMID:22922713 "our observations reveal a role for the WD40 domain
  of DYF-2 as the key factor in reassembling IFT-B subcomplex into IFT-A-dynein retrograde
  machinery"].
- General IFT-integrity role: [PMID:16957054 "DYF-2, that plays a critical role in maintaining the
  structural and functional integrity of the IFT machinery"] and [PMID:16957054 "Loss of DYF-2
  function selectively affects the assembly and motility of different IFT components and leads to
  defects in cilia structure and chemosensation in the nematode"].

### BBSome coupling
- DYF-2/WD40 is required for BBSome docking onto moving IFT particles: [PMID:22922713 "Our data
  also suggest the WD40 domain of DYF-2 protein is critical for the association between the BBSome
  and IFT particles"].
- Direct WDR19–BBS1 interaction (mammalian): [PMID:22922713 "mouse WDR19 (the homolog of DYF-2) and
  BBS1 (the homolog of BBS-1) show strong interaction"]; BiFC places DYF-2 near BBS-1/7/9:
  [PMID:22922713 "Results from BiFC analyses suggest that DYF-2 locates near BBS-1, BBS-7 and BBS-9
  in the native IFT particles"].

### Disruption phenotype (UniProt, from PMID:16957054)
Shorter phasmid cilia; mislocalization of IFT-A proteins (che-11) and IFT-B (osm-5); impaired
transport/accumulation of IFT-B che-13; strong osmotic-avoidance (Osm) phenotype; impaired
chemotaxis to volatile odorants (pyrazine, iso-amyl alcohol); dye-filling defective (Dyf).

## Curation nuance: IFT-A vs IFT-B complex membership
The 2006 primary paper concluded DYF-2 "can associate with IFT particle complex B"
[PMID:16957054 "we conclude that DYF-2 can associate with IFT particle complex B"] while also noting
"mutations in dyf-2 can interfere with the function of complex A components." This dual/early model
generated the experimental IDA annotation to **GO:0030992 intraciliary transport particle B**.
The modern consensus firmly places WDR19/IFT144/DYF-2 as a **core IFT-A** subunit: direct mass-spec
identification in IFT-A (PMID:28479320 / ComplexPortal CPX-1289), the Chlamydomonas IFT144 = IFT-A
assignment [PMID:22922713 "In Chlamydomonas, IFT144 (the homolog of DYF-2) is an IFT-A component"],
and the IFT-A subunit list in UniProt. The 2006 IFT-B "association" reflects DYF-2 functioning at
the IFT-A/IFT-B interface (it reassembles IFT-B into the IFT-A–dynein machinery at the tip), not
stable IFT-B core membership. => GO:0030992 (IFT-B) is best marked as over-annotation/superseded;
GO:0030991 (IFT-A) is the correct, well-supported complex membership.

## What is NOT known (knowledge gaps)
- **No assigned molecular function / no specific biochemical activity.** DYF-2 has WD40 + TPR
  protein-interaction folds and no catalytic domain; its "function" is to be a structural
  constituent of IFT-A. GO has no "structural constituent of the IFT particle" MF term — an
  ontology gap (structural-subunit pattern), so the gene reads MF-dark despite a well-understood
  cellular role.
- **The IFT-A subunit-level interaction map is undefined in the worm.** Which IFT-A neighbours
  DYF-2 directly contacts (che-11/IFT140, daf-10/IFT122, ift-139, ift-43, ifta-1) and the
  stoichiometry/architecture of worm IFT-A are not experimentally resolved; interactions are
  inferred from cross-species proteomics/structures.
- **Mechanism of tip reassembly.** How the DYF-2 WD40 domain physically "reassembles IFT-B into the
  IFT-A–dynein retrograde machinery" at the ciliary tip is a model, not a solved structure/mechanism.
- **BBSome-docking interface.** The DYF-2/WDR19 surface that docks the BBSome onto moving IFT
  particles is inferred from point mutants (G361R worm / G341R mouse) and BiFC/co-IP, not from a
  structure of the DYF-2–BBSome interface.

## Provisional annotation-review plan (23 GOA annotations)
- Core CC: GO:0030991 (IFT particle A) ACCEPT ×2 (IBA, NAS); GO:0005929 (cilium) ACCEPT ×3;
  GO:0097730 (non-motile cilium, IDA) ACCEPT. GO:0030990 (IFT particle, IEA) = generic parent, keep.
- Core BP: GO:0035721 (retrograde IFT) ACCEPT ×4 (IBA, IEA, NAS, IMP); GO:0042073 (IFT, IDA) ACCEPT;
  GO:0060271 (cilium assembly) ACCEPT ×3; GO:1905515 (non-motile cilium assembly, IMP) ACCEPT;
  GO:0044782 (cilium organization, IEA) = generic parent, keep as non-core.
- GO:0030992 (IFT particle B, IDA PMID:16957054): MARK_AS_OVER_ANNOTATED (superseded; see nuance).
- GO:0008104 (intracellular protein localization) IEA + IMP: MODIFY -> GO:0061512 protein
  localization to cilium (more specific/accurate; DYF-2 loss mislocalizes ciliary IFT proteins).
- Sensory-behaviour phenotypes (downstream of ciliary dysfunction, KEEP_AS_NON_CORE): GO:0006935
  chemotaxis, GO:0007635 chemosensory behavior, GO:0042048 olfactory behavior.

## Deep research provenance
Automated deep research was **unavailable** for this gene: the falcon deep-research run **timed out**
and produced no output file, so there is no `dyf-2-deep-research-falcon.md` (none was fabricated). This
review is instead grounded directly in the UniProt record (G5ECZ4 / DYF2_CAEEL), the QuickGO GOA export
(`dyf-2-goa.tsv`), the PANTHER family data (PTHR14920), and the primary literature — chiefly the founding
ortholog/IFT-component paper [PMID:16957054] and the mechanistic IFT-turnaround/BBSome study
[PMID:22922713] (full text available), with the IFT-A mass-spec composition from [PMID:28479320].
