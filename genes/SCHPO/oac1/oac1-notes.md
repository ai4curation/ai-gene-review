# oac1 (SPAC139.02c, UniProt Q9UTN1) notes

- Mitochondrial carrier (SLC25), ortholog of S. cerevisiae OAC1 (P32332). All functional annotations are ISO/ISS from budding yeast; no S. pombe transport data.
- S. cerevisiae evidence (full text): [PMID:18682385 "Recombinant and reconstituted mitochondrial oxalacetate carrier (Oac1p) efficiently transported alpha-IPM in addition to its known substrates oxalacetate, sulfate, and malonate"]; [PMID:18682385 "Oac1p is important for leucine biosynthesis on fermentable carbon sources catalyzing the export of alpha-IPM, probably in exchange for oxalacetate."]
- UniProt (by similarity): [UniProt:Q9UTN1 "Antiporter that exchanges dicarboxylates and sulfur oxoanions across the inner membrane of mitochondria. Exports alpha-isopropylmalate from mitochondrial matrix to the cytosol"].
- Pathway logic in S. pombe: leu3 mitochondrial, leu2/leu1 cytosolic [PMID:35325114 "Leu biosynthesis involves reactions in both the cytosol and the mitochondria"], so an alpha-IPM exporter is needed.
- PomBase GO-CAM: oac1 GO:0034658 in mitochondrial inner membrane, part_of GO:1990556; no causal edges linking leu3 -> oac1 -> leu2.
- Decisions mirror the S. cerevisiae OAC1 review: two core functions (alpha-IPM export; oxaloacetate transport); root transporter IBA marked over-annotated; thiosulfate items kept non-core (S. cerevisiae review has no thiosulfate rows).
