# glpF review notes

## Identity and scope

- Target: `glpF`, PP_1076, UniProt Q88NX7, *Pseudomonas putida* KT2440.
- Reviewed target files: `glpF-ai-review.yaml`, `glpF-goa.tsv`, and `glpF-uniprot.txt`.
- Read-only pathway context: `genes/PSEPK/glpK/glpK-ai-review.yaml`, `glpK-uniprot.txt`, and `glpK-deep-research-asta.md`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/glpF/glpF-uniprot.txt`.

- `"DE   SubName: Full=Aquaglyceroporin"`
- `"GN   OrderedLocusNames=PP_1076"`
- `"DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter."`
- `"DR   GO; GO:0015254; F:glycerol channel activity; IEA:TreeGrafter."`
- Predicted transmembrane segments are listed at residues 15-35, 42-61, 91-111, 151-170, 182-205, and 233-254.

### Direct KT2440 pathway description

Source: Nikel et al., 2015, PMID:25827416, PMCID:PMC4453509, DOI:10.1128/mBio.00340-15. Full text accessed through PMC/web search.

- `"Uptake of the compound is mediated by the GlpF facilitator, which fosters a diffusion reaction"`
- `"Once inside the cell, glycerol is phosphorylated by an ATP-dependent glycerol kinase (GlpK) to sn-glycerol-3-P (G3P)"`
- `"G3P is the substrate for GlpD, a membrane-bound G3P dehydrogenase that yields dihydroxyacetone-P"`

The paper explicitly places PP_1076/GlpF in the `glpF-glpK-glpR-glpD` locus and describes facilitated glycerol entry rather than active transport.

## Curation conclusions

- Accept glycerol channel activity, glycerol transmembrane transport, and plasma-membrane localization as core.
- Mark generic channel, membrane, and transmembrane-transport parents as over-annotated because specific terms are present.
