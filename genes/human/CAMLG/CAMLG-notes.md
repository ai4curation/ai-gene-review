# CAMLG (P49069) curation notes

## Identity
- HGNC: CAMLG; aka CAML (calcium-modulating cyclophilin ligand), GET2.
- UniProt RecName: "Guided entry of tail-anchored proteins factor CAMLG".
- Multi-pass ER membrane protein: large cytoplasmic N-terminal region (1-189, disordered N-terminus), then three C-terminal TM helices (190-207, 213-231, 270-288). Topology established in PMID:31417168.
- Disease: Congenital disorder of glycosylation 2Z (CDG2Z, MIM:620201), autosomal recessive, neurological phenotype; caused by defective membrane trafficking (PMID:35262690 — not cached).

## Core function: GET/TRC insertase receptor for tail-anchored (TA) proteins
CAML, together with WRB/GET1, forms the mammalian ER membrane receptor for the cytosolic ATPase TRC40/GET3, which delivers newly synthesized tail-anchored membrane proteins for post-translational insertion into the ER membrane. CAML is the mammal-specific subunit (not homologous to yeast Get2); WRB is the Get1 orthologue.

- [PMID:23041287 "We identify calcium-modulating cyclophilin ligand (CAML) as a mammal-specific receptor for TRC40, an ATPase targeting newly synthesized TA proteins, and show that CAML mediates membrane insertion of TA proteins."]
- [PMID:23041287 "We show that CAML binds to WRB, an evolutionarily conserved TRC40 receptor, through the transmembrane domains and that CAML and WRB synergistically insert TA proteins into the membrane."]
- [PMID:27226539 "in mammals of the WRB protein (tryptophan-rich basic protein), homologous to yeast Get1, in combination with CAML (calcium-modulating cyclophilin ligand), which is not homologous to Get2."]
- [PMID:27226539 "in vitro synthesized CAML and WRB together were sufficient to confer insertion competence to liposomes."]
- [PMID:32910895 "The guided entry of tail-anchored proteins (GET) pathway targets and inserts tail-anchored (TA) proteins into the endoplasmic reticulum (ER) membrane with an insertase"] — structural basis: WRB/CAML/TRC40 heterotetramer, PI-stabilized; disulfide bond 208-284 (UniProt FT DISULFID).
- [PMID:32187542 "by using the WRB/CAML complex, an essential insertase for tail-anchored proteins in the endoplasmic reticulum (ER), as a model system."]

Reactome: R-HSA-9609523 "Insertion of tail-anchored proteins into the endoplasmic reticulum membrane".

### GET complex membership and reciprocal stability with WRB
CAML and WRB depend on each other for stability/correct topology.
- [PMID:32187542 "In WRB's absence, CAML folds incorrectly, causing aberrant exposure of a hydrophobic transmembrane domain to the ER lumen. When present, WRB can correct the topology of CAML both in vitro and in cells."]
- [PMID:31417168 "without sufficient levels of WRB, CAML fails to adopt this topology, and is instead incompletely integrated to generate two aberrant topoforms; these congregate in ER-associated clusters and are degraded by the proteasome."]
- GO terms: GET complex (GO:0043529) part_of — well supported (IDA PMID:32910895, IPI PMID:23041287). Protein stabilization (GO:0050821) is supported in the WRB/CAML context (PMID:32187542) but note PMID:20553626 also annotated stabilization in the unrelated RNF122 context.

## Secondary / historical functions
### Calcium signaling (original discovery)
CAML was originally cloned as a cyclophilin-B-binding protein that induces calcium influx in T cells and activates NF-AT/IL-2 transcription. This is the historical basis of the "defense response" (GO:0006952) and "signal transduction" (GO:0007165) TAS annotations from PMID:7522304. Plausible but largely supplanted by the well-established GET insertase role; treat as non-core/contextual.
- [PMID:7522304 "This protein, termed calcium-signal modulating cyclophilin ligand (CAML), acts downstream of the TCR and upstream of calcineurin by causing an influx of calcium."]

### B cell homeostasis
By-similarity/ISS: "Essential for the survival of peripheral follicular B cells" (UniProt). Mouse phenotype; CAML interacts with TACI/TNFRSF13B (PMID:9311921 — not cached). Non-core for the human gene's molecular function.

### EGFR recycling
CAML-deficient cells have defective EGFR recycling; CAML associates with the EGFR kinase domain ligand-dependently (PMID:12919676). This is the basis of Ensembl IEA "receptor recycling" and "epidermal growth factor receptor signaling pathway" terms (not in the current existing_annotations list except via interactome IPI). Context-dependent; potentially confounded by the general role of CAML in membrane protein biogenesis.

### RNF122 / ubiquitin-related annotations (PMID:20553626)
The negative regulation of (protein) ubiquitination / proteasomal catabolism / protein stabilization and ubiquitin-protein-ligase-binding annotations all derive from one yeast-two-hybrid + co-IP study of the RING E3 RNF122, in which CAML stabilizes RNF122 (and is not its substrate). These are narrow, single-study, context-specific findings, not the core GET function.
- [PMID:20553626 "we found that CAML is not a substrate of ubiquitin ligase RNF122, but that, instead, it stabilizes RNF122."]
- [PMID:20553626 "we identified calcium-modulating cyclophilin ligand (CAML) as an RNF122-interacting protein."]

## Over-annotations / non-informative
- GO:0005515 protein binding (IPI) appears ~12 times from interactome/Y2H/MaMTH/coronavirus-host studies (PMID:15451437, 16243292, 22046132, 24658140, 25416956, 28514442, 31980649, 32296183, 33961781, 40205054, 31417168, 32187542). Bare "protein binding" is uninformative; meaningful interactions (WRB, GET3, TACI, RNF122, EGFR) are captured by specific terms or noted in core function.
- GO:0016020 membrane (HDA, PMID:19946888) — generic; subsumed by ER membrane terms.
- GO:0005737 cytoplasm (IDA, PMID:20553626) — CAML has a large cytoplasmic domain, but the protein is an integral ER membrane protein; ER membrane terms are the correct localization.

## Localization
Well supported: ER membrane / ER (multiple EXP/IDA: PMID:23041287, PMID:31417168, PMID:12919676). Core.

## Summary of action plan
- CORE: GET complex (GO:0043529) part_of; tail-anchored membrane protein insertion into ER membrane (GO:0071816); protein insertion into ER membrane (GO:0045048); ER membrane (GO:0005789); endoplasmic reticulum (GO:0005783).
- NON-CORE (real but secondary/contextual): protein stabilization (GO:0050821, WRB/CAML context); B cell homeostasis (GO:0001782); defense response (GO:0006952); signal transduction (GO:0007165).
- NON-CORE single-study (RNF122): negative regulation of protein ubiquitination (GO:0031397), negative regulation of proteasomal ubiquitin-dependent protein catabolic process (GO:0032435), ubiquitin protein ligase binding (GO:0031625).
- OVER-ANNOTATED: bare protein binding (all IPI), generic membrane, cytoplasm.
