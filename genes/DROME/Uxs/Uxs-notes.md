# Uxs (Q9VSE8) notes

- Uxs is the fly UXS1 ortholog (UniProt: UDP-glucuronic acid decarboxylase 1, EC 4.1.1.35, rule-based).
  No direct enzyme assay of fly Uxs is in the cached literature.
- N-terminal hydrophobic signal-anchor (UniProt: "Single-pass type II membrane protein"), so the catalytic
  domain is luminal, as for mammalian UXS1.
- Uxs mutants were used to study the xylose residues of Notch O-glucose glycans
  [PMID:27129198 "O-glucose
trisaccharide (O-glucose-xylose-xylose) are added to many of the Notch EGF-like
repeats"] (abstract-only in cache).
- Decisions: decarboxylase activity and UDP-xylose biosynthesis accepted; IBA cytoplasm modified to Golgi cisterna
  membrane (cytoplasm includes the Golgi, so the term is true but too general; the node's WITH/FROM includes rat Uxs1
  and human UXS1); Golgi membrane modified to Golgi cisterna membrane;
  D-xylose metabolic process modified to GO:0033320; NAD+ binding kept as non-core.

- Falcon deep research (Uxs-deep-research-falcon.md): Uxs/CG7979 is the sole fly UDP-xylose synthase gene; best-supported
  model is ER/Golgi-luminal activity (mammalian UXS seen in ER and Golgi; no direct fly topology data). Supports choosing the
  luminal Golgi cisterna membrane term over cytoplasm; ER-vs-Golgi partitioning remains open.

- PR #4484 review: cytoplasm IBA changed from REMOVE to MODIFY (GO:0032580), matching the treatment of cytoplasm IBA rows in Ugp, Tps1 and Ar1.
