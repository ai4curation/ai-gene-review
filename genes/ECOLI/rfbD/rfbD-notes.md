# rfbD (E. coli K-12) curation notes

## 2026-11-10 review (dTDP-L-rhamnose biosynthesis module)

- Reviewed every GOA row against the cached publications and the UniProt record.
  Deep-research generation was not run (no provider API keys in this session); the
  review rests on UniProt curated text, cached abstracts/full texts and PANTHER/PAINT files.
- Consistent treatment across the four rfb-cluster genes (rfbA/B/C/D):
  core MF and GO:0019305 ACCEPT; cytosol ACCEPT; polymer-level processes
  (GO:0000271, GO:0009103, GO:0009243) MARK_AS_OVER_ANNOTATED, because these enzymes make
  the soluble dTDP-L-rhamnose donor and form no glycosidic bond; the polymer is assembled by
  glycosyltransferases
  [PMID:7517391 "the rhamnose transferase gene is identified by assay of its product"].
  This follows the project decision for the PSEPK RmlC paralogs in
  projects/TREEGRAFTER/rereview-2026-09-24/batch-07.yaml.
- Most K-12 lines are O-antigen negative (rfb-50/rfb-51)
  [PMID:7512872 "the rough phenotype of this strain is due to the presence of one of two independent mutations in the rfb gene cluster"].

## Review follow-up (2026-11-11, PR #6252)

- involved_in polymer-level rows (GO:0000271, GO:0009103, GO:0009243) stay
  MARK_AS_OVER_ANNOTATED: involved_in claims participation, and these enzymes only supply the
  dTDP-L-rhamnose donor.
- The two experimental acts_upstream_of_or_within GO:0009243 rows (PMID:7512872, PMID:7517391)
  are KEEP_AS_NON_CORE: that qualifier states requirement without participation, which is the
  donor-supply relationship. The same-term consistency check ignores qualifiers
  (docs/action_consistency.md, Known limitations), so it reports this deliberate split as a warning.
- The PMID:7512872 abstract does not identify the complementing gene. The rfb-50 IS5 location now
  rests on PMID:7517390 ["the other, located in the downstream end of the cluster next to gnd
  (gluconate-6-phosphate dehydrogenase), had an IS5 insertion"], and the wbbL name rests on the
  curated UniProt caution in the rfbA record ["mutations in dTDP-rhamnose biosynthetic genes or in
  the rhamnosyltransferase gene wbbL"].
