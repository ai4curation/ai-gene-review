# CLDN18 notes

Deep research providers unavailable in this environment; research from UniProt P56856 and the two
cached publications (both large-scale interaction screens). Human-specific experimental literature is
sparse: almost all GOA process terms are ISS/IEA from mouse P56857.

## Topology / localization
- Tetraspan claudin: TOPO_DOM 1-6 cytoplasmic, TM 7-27, extracellular 28-80, TM 81-101, cytoplasmic
  102-122, TM 123-143, extracellular 144-174, TM 175-195, cytoplasmic tail 196-261 ending in a
  PDZ-binding motif.
- UniProt: "SUBCELLULAR LOCATION: Cell junction, tight junction ... Cell membrane; Multi-pass membrane
  protein ... Localizes to tight junctions in epithelial cells"; isoform A2 also "Lateral cell membrane".
- Conclusion: plasma membrane, concentrated at bicellular tight junctions; only two short extracellular
  loops are exposed (relevant for antibody accessibility — zolbetuximab targets the CLDN18.2 first loop).

## Isoforms
- A1 = CLDN18.1 (lung-restricted), A2 = CLDN18.2 (gastric; aberrantly expressed in gastric/pancreatic
  adenocarcinoma). They differ in TM1 and extracellular loop 1.

## Functions (mostly By similarity from mouse)
- Tight-junction strand component controlling alveolar and gastric paracellular barrier
  [UniProt "Involved in alveolar fluid homeostasis via regulation of alveolar epithelial tight junction
  composition", "Required for the formation of the gastric paracellular barrier"].
- Scaffold: binds ZO-1/ZO-2 and phosphorylated YAP1, sequestering YAP1 from the nucleus.

## Curation decisions
- 16 protein-binding rows from PDZ fragmentomics (PMID:36115835) modified to GO:0030165 PDZ domain
  binding (all partners are PDZ-domain proteins binding the claudin C-terminal motif); two HuRI rows
  removed.
- cell-cell junction and membrane rows modified to bicellular tight junction / plasma membrane.
