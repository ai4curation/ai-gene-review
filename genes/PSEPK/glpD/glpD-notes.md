# glpD review notes

## Identity and scope

- Target: `glpD`, PP_1073, UniProt Q88NY0, *Pseudomonas putida* KT2440.
- Reviewed target files: `glpD-ai-review.yaml`, `glpD-goa.tsv`, and `glpD-uniprot.txt`.
- Read-only pathway context: `genes/PSEPK/glpK/glpK-ai-review.yaml`, `glpK-uniprot.txt`, and `glpK-deep-research-asta.md`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/glpD/glpD-uniprot.txt`.

- `"DE   RecName: Full=Glycerol-3-phosphate dehydrogenase"`
- `"DE            EC=1.1.5.3"`
- `"CC       Reaction=a quinone + sn-glycerol 3-phosphate = dihydroxyacetone"`
- `"CC       Name=FAD; Xref=ChEBI:CHEBI:57692;"`
- `"DR   GO; GO:0004368; F:glycerol-3-phosphate dehydrogenase (quinone) activity; IEA:UniProtKB-EC."`
- `"DR   GO; GO:0046168; P:glycerol-3-phosphate catabolic process; IEA:TreeGrafter."`

### Direct KT2440 pathway description

Source: Nikel et al., 2015, PMID:25827416, PMCID:PMC4453509, DOI:10.1128/mBio.00340-15. Full text accessed through PMC/web search.

- `"Glycerol-3-P is then oxidized in an ubiquinone-dependent reaction catalyzed by the membrane-bound GlpD"`
- `"G3P is the substrate for GlpD, a membrane-bound G3P dehydrogenase that yields dihydroxyacetone-P"`
- The abstract states that a transcriptional `glpD-gfp` fusion was used as `"a proxy of the glycerol-3-phosphate [G3P] dehydrogenase activity"` and that GlpR controls the `glpFKRD` cluster.

### Read-only GlpK context

`glpK-ai-review.yaml` identifies GlpK as the ATP-dependent first committed step that produces sn-glycerol-3-phosphate. No glpK file was edited.

### OpenScientist report

Source: `file:PSEPK/glpD/glpD-deep-research-openscientist.md`.

- The report completed with HTML and PDF artifacts even though the wrapper returned a timeout status.
- Its target identity, reaction, and `glpFKRD` pathway placement agree with the UniProt record and PMID:25827416.
- The report also quotes a secondary source as calling GlpD a six-transmembrane enzyme while elsewhere correctly describing the characterized enzyme as monotopic. That contradictory topology claim was not used as evidence.

## Curation conclusions

- Accept GO:0004368 specifically as quinone-dependent activity.
- Do not substitute an NAD-dependent glycerol-3-phosphate dehydrogenase term; that would reverse the physiological chemistry and use the wrong acceptor.
- Accept G3P catabolism and plasma-membrane association; keep the broader G3P metabolic process as non-core.
- Leave the transferred FAD-complex component term UNDECIDED because no
  target-specific oligomerization evidence or distinct GlpB/GlpC partners were
  found. The available evidence establishes a monotopic GlpD enzyme, not the
  composition of a molecular complex.
