# lptB notes

## 2026-11-02 revision (PR review round, bacterial_lps_transport)

- Every annotation row and core function now carries verbatim support: curated
  HAMAP-rule text or family/domain signatures from this entry's UniProt record
  (ARBA-only statements are not cited), plus experimental quotes from the E. coli
  orthologue (same PANTHER subfamily) reused from the E. coli K-12 Lpt reviews.
- Correct-but-general terms changed from KEEP_AS_NON_CORE/MARK_AS_OVER_ANNOTATED to
  MODIFY with the specific term the gene already carries; transmembrane transport
  refined to lipopolysaccharide transport; transporter complex refined to GO:0062051
  lipopolysaccharide transport system, matching the E. coli reviews.
- No provider deep research was run for this gene.
