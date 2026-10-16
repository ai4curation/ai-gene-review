# ARMS2 review notes

## Sources
- Affinage: trust gates clear.
- Localization is disputed in the literature:
  - PMID:18511946 (abstract): mitochondrial association; photoreceptor ellipsoid.
  - PMID:19255159 (full text): "cytosol, not mitochondria".
  - PMID:19696174 (abstract): secreted, extracellular matrix.
  - PMID:27270414 (abstract): unconventional secretion via lectin chaperones.
- Function: PMID:28086806 (full text): ARMS2 binds dying-cell surfaces and recruits properdin, augmenting C3b opsonization.
- Partners: properdin (CFP, P27918) and hemicentin-1 (HMCN1, Q96RW7).

## Decisions
- Mitochondrion (IDA) → UNDECIDED, recorded as a finding_review DISPUTED on PMID:18511946. It is not removed: it is an experimental annotation, and the full text is not cached.
- KEEP_AS_NON_CORE:
  - Photoreceptor inner segment (same disputed study).
  - Cytoplasm (pre-secretion pool).
  - Retina homeostasis (genetic association only).
- MODIFY: properdin binding → complement binding; HMCN1 binding → extracellular matrix binding.
- NEW: extracellular matrix (IDA, PMID:19696174); positive regulation of complement activation (IDA, PMID:28086806).

## Review round 1 (PR #4202)
- Photoreceptor inner segment → UNDECIDED, matching the mitochondrion row. PMID:19255159 (full text) calls the retinal co-localization image unconvincing and could not replicate mitochondrial targeting; this is now quoted in both rows and in the finding_review.
- Cytoplasm (IEA) → MODIFY to cytosol (PMID:19255159, "cytosol, not mitochondria").
- The NEW process is now GO:0045958 positive regulation of complement activation, alternative pathway. Properdin is recruited from EGTA-treated serum with the alternative pathway intact. The reconstitution caveat is noted.
- The ECM NEW row now quotes the choroid-pillar sentence. A second core function was added for extracellular matrix binding.
- Added PMID:17884985 (the original mitochondrial report) and PMID:23959158 (knockdown lowers C3/C5 in ARPE-19).
