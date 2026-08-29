# arl5a (F6WPT1) notes

## Re-review 2026-08-29

Re-checked the completed review against the GOA tsv, UniProt entry, and the
falcon deep-research file.

- All 9 GOA rows have matching `existing_annotations` entries (term id +
  evidence code + reference); no PMIDs are cited in GOA (all IBA/IEA), so no
  publication caching issues arise.
- All actions retained: the six IBA annotations are phylogenetically sound and
  well supported by mammalian ARL5A/ARL5B experimental literature summarized in
  the deep research (GARP recruitment, ARFRP1-SYS1-dependent TGN localization,
  ARMH3-PI4KB axis, Ragulator interaction). GO:0005737 cytoplasm remains
  KEEP_AS_NON_CORE (real but uninformative for a TGN-acting GTPase); broad BP
  terms (GO:0016192, GO:0006886) remain ACCEPT since the IBA level is
  defensible and the specific retrograde-trafficking biology is captured in
  `core_functions` and annotation summaries.
- Added `supported_by` evidence citing
  file:XENTR/F6WPT1/F6WPT1-deep-research-falcon.md (verbatim quotes) to all 9
  annotations, plus a uniprot.txt quote for GTP binding; added both files to
  the top-level references with findings. This resolves the validation warning
  that no annotations referenced the available deep-research file.
- Trimmed curation-flavored wording ("functional annotation rests on...",
  "annotation is based on...") from `description` and `core_functions` in
  favor of biological phrasing (function inferred from orthology).
- `just validate XENTR F6WPT1` passes with no warnings.
