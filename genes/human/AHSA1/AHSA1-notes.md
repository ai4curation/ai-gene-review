# AHSA1 notes

## 2026-11-04 ORGANELLES ER batch 1 (endoplasmic reticulum rows)

- Row: GO:0005783 IEA (GO_REF:0000044, SL-0095), no qualifier; kept KEEP_AS_NON_CORE.
- Check: UniProt "Endoplasmic reticulum {ECO:0000269|PubMed:11554768}. Note=May transiently interact with the endoplasmic reticulum." [file:human/AHSA1/AHSA1-uniprot.txt]. The source is Sevier and Machamer 2001 (abstract-only cache): "Preliminary evidence suggests that p38 may interact transiently with endoplasmic reticulum (ER) membranes" [PMID:11554768].
- No signal peptide or TM segment; cytosolic HSP90 co-chaperone recruited to the ER surface at most, so root only, no NEW sub-compartment row.
- Added PMID:11554768 to references (it was cited in prose but absent) and as supported_by on the ER row.
- Judgement call: the source is explicitly preliminary; MARK_AS_OVER_ANNOTATED would also be defensible. Kept the existing KEEP_AS_NON_CORE because the curated UniProt location is experimental and no paper refutes it.
