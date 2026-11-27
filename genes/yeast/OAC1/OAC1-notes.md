# OAC1 (P32332, YKL120W) notes

- Mitochondrial carrier; reconstituted transport of malonate, oxaloacetate, sulfate, thiosulfate [PMID:10428783 "demonstration that the proteoliposomes transport malonate, oxaloacetate, sulfate, and thiosulfate"]
- Inner membrane [PMID:10428783 "In S. cerevisiae, OAC is in inner mitochondrial membranes"]
- Exports alpha-IPM for leucine biosynthesis [PMID:18682385 "Oac1p is important for leucine biosynthesis on fermentable carbon sources catalyzing the export of alpha-IPM, probably in exchange for oxalacetate"]
- oac1 leu4 synthetic leucine requirement [PMID:18682385 "the double mutant DeltaOAC1DeltaLEU4 did not grow at all on fermentable substrates in the absence of leucine"]

## Decisions
- All IDA rows accepted; root transporter activity IBA marked over-annotated.
- Core: GO:0034658 (alpha-IPM export) + GO:0015131, inner membrane.
- No YeastPathways reaction for OAC1 (transport step absent from LEU pathway frame); module adds it correctly.
