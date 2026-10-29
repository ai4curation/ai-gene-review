# ATXN7 notes

## 2026-10-05 review (PAINT, affinage)

- Affinage gate ('yeast') was a false positive: the record cites the yeast ortholog Sgf73. Written with --force.
- SAGA subunit [PMID:15115762 "We show here that ataxin-7 is an integral component of the mammalian SAGA-like complexes, the TATA-binding protein-free TAF-containing complex (TFTC) and the SPT3/TAF9/GCN5 acetyltransferase complex (STAGA)."].
- Nucleosome binding [PMID:20634802 "Instead, it binds to nucleosomes, a property that is conserved in the human ATXN7–SCA7 domain but is lost in the ATXN7L3 domain."]. The H2B IPI was changed to GO:0031491 (core MF).
- Regulation of DNA repair and of RNA splicing (NAS) are over-annotated: they derive from early TFTC/STAGA complex papers that predate ATXN7's identification as a subunit. Visual perception (SCA7 cloning) and nucleus organization (localization study) are also over-annotated.
- The microtubule rows (PMID:22100762) are non-core.
- PMID:11580893 (CRX) has an erratum (a correction, not retrieved).

## 2026-10-05 revision (reviewer round 1)

- PMID:12533095 rows: the cytoplasm EXP row reflects the CNS-enriched ataxin-7b isoform (cytoplasmic, isoform-specific antibody), and the nucleus row the canonical isoform. GOA does not carry isoform IDs on these rows, so no isoform field is set; the summaries state it.
- Visual perception: still over-annotated, now argued on term semantics (sensory perception of light). ATXN7's retinal role is as a CRX cofactor. Affinage cites a zebrafish atxn7 loss-of-function coloboma paper (PMID:30445451, not cached), which bears on eye development, not on perception.
- SORBS1 IPI (PMID:23892081) changed to GO:0017124 SH3 domain binding (NMR-mapped RRTR-SH3C interface). The PMID:11371513 SORBS1 row stays REMOVE.
- core_functions now mentions the conserved zinc-binding domain that mediates TFTC/STAGA incorporation (PMID:15115762). The NAS principle is stated in the over-annotated rows.
