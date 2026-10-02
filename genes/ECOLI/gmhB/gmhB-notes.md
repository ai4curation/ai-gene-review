# gmhB notes

## 2026-10-02 ADP-heptose module review

GmhB is the HAD-family phosphatase step between the two HldE reactions in E. coli ADP-heptose synthesis. Kneidinger et al. showed that purified E. coli GmhB converts the beta heptose 1,7-bisphosphate intermediate to beta heptose 1-phosphate and that deleting gmhB produces an altered LPS core [PMID:11751812].

The exact `GO:0034200` activity is well supported by several later biochemical and structural studies. Wang et al. showed that E. coli GmhB has a narrow substrate range, high catalytic efficiency for beta-HBP, and selective C-7 phosphate removal by NMR [PMID:20050615]. Nguyen et al. solved Mg/substrate-bound and apo E. coli GmhB structures and established the structural Zn-binding loop as a substrate-recognition feature rather than the catalytic metal site [PMID:20050614]. The abstract-only structural paper cited in GOA/UniProt also supports Mg and Zn binding [PMID:20050699].

Review decisions:

- Accept all exact `GO:0034200` rows and both specific pathway rows.
- Mark the broad IBA `GO:0009103 lipopolysaccharide biosynthetic process` row as over-annotated because the more precise `GO:0009244 lipopolysaccharide core region biosynthetic process` row already exists.
- Keep Mg/Zn binding and cytosol/cytoplasm as real but non-core.
- Mark generic carbohydrate metabolism and phosphatase activity as over-annotated.
