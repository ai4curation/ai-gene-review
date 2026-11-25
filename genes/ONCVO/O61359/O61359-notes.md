# O61359 notes

## 2026-11-24

- Started the `ONCVO/O61359` review from current `origin/main` in a fresh
  registered worktree for the nematode beta-tubulin/benzimidazole lane.
- Resolved the target from live UniProt before fetching: *Onchocerca volvulus*
  uses the `ONCVO` mnemonic and taxon 6282; O61359 is a 448 aa unreviewed
  beta-tubulin fragment in PANTHER family PTHR11588 with gene name `tub` and
  EMBL genomic DNA record `AF019886` / protein `AAC13549.1`.
- O61359 is the Geary et al.-linked companion of the merged O61358 review.
  UniProt imports O61358 from `AF019885` / `AAC13548.1`, a full-length cDNA
  record, and O61359 from `AF019886` / `AAC13549.1`, a genomic-DNA record
  flagged as a fragment with a C-terminal non-terminal marker.
- `just fetch-gene-pmids ONCVO O61359` found no PMID rows in the GOA-derived
  review; this review reuses cached `PMID:9576511`, `PMID:2592410`,
  `PMID:24780738`, and `PMID:6087508` from the merged `ONCVO/O61358` review.
- `just paint-losses ONCVO O61359` reported no IRD or IKR loss on the gene's
  lineage, noting that O61359 is not a leaf of the cached PTHR11588 tree.
- `just deep-research-falcon ONCVO O61359 --fallback perplexity-lite` could
  not generate a provider report because only the `claude_code` provider was
  available. This review uses the seeded GOA rows, the matching UniProt
  flatfile, the Geary et al. filarial beta-tubulin paper PMID:9576511, the
  C. elegans BEN-1 genetic anchor PMID:2592410, the Lacroix et al. TBB-5
  egg-laying apparatus paper PMID:24780738, the Engelbrecht and Schulz-Key
  O. volvulus microfilaria-release paper PMID:6087508, and the neighboring
  nematode beta-tubulin reviews.
- I kept this review accession-scoped and did not infer a one-to-one
  relationship between O61359, O61358, or a current O. volvulus genome model.
  O61359 has the seven standard beta-tubulin rows plus the two C. elegans
  BEN-1 behavior transfers. As with O61358, the behavior transfers are kept as
  over-propagated or removed because the direct evidence supports a conserved
  microtubule structural subunit, not the transferred worm behaviors.
- The PR review caught that Geary et al.'s abstract explicitly states that the
  study cloned the genomic locus for the O. volvulus beta-tubulin cDNA. I kept
  the review scoped to O61359 because AF019886 is still only an accession-level
  genomic DNA fragment in this UniProt record, but added the author statement as
  evidence for a candidate O61359/O61358 genomic-locus/cDNA pairing to resolve
  against the current O. volvulus gene models.
- A formal re-review of the InterPro2GO `GO:0003924` qualifier defect asked for
  explicit support on the polymer- and alpha-subunit-coupled GTPase premise.
  I added the RuleBase-supported UniProt `CC:FUNCTION` sentence to the GTPase
  row and to the source-defect evidence so the `enables` to `contributes_to`
  query no longer rests on the Tubulin/FtsZ domain boundaries alone.
