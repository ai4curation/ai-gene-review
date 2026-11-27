# NFYA7 review notes

- 2026-10-28: fetch-gene resolved Q84JP1 (TAIR AT1G30500, GeneID 839929) as requested.
  13 GOA rows. Literature on NFYA7 itself is sparse; the only NFYA7-specific experimental
  paper is PMID:23118940 (overexpression, full text cached). See
  NFYA7-deep-research-manual.md for the synthesis with provenance.
- Core MF: NF-YA subunits supply CCAAT specificity but only bind DNA within the
  NF-YA/YB/YC trimer [PMID:23118940 "the complete NF-YA/NF-YB/NF-YC heterotrimer is
  necessary to bind CCAAT-box containing promoters"], so core function uses
  contributes_to GO:0000981; enables rows queried as WRONG_QUALIFIER (SUSPECTED, since
  NF-YA family enables is a widespread convention).
- PMID:19207209 (abstract only) does not name which NF-YA was co-expressed; deferred to
  the TAIR curator (KEEP_AS_NON_CORE: artificial transient assay).
- No NEW process terms: the stress-tolerance and senescence phenotypes are from
  overexpression and are attributed by the authors to growth arrest.
- Protein-binding rows (HT Y2H) removed per policy.
