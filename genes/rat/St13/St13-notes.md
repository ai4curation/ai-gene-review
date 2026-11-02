# St13 (Hip) notes

## Re-review 2026-10-10

GOA changes since the original review:
- New row: GO:0044183 protein folding chaperone (IDA, PMID:9183013), replacing the
  retired GO:0051082 unfolded protein binding IDA row from the same paper. QuickGO
  confirms GO:0051082 is obsolete ("should be replaced by an activity term such as
  protein folding chaperone (GO:0044183) or unfolded protein holdase activity
  (GO:0140309)"). Resolved as ACCEPT, matching the earlier MODIFY recommendation
  [PMID:9183013 "The role of Hip as a molecular chaperone has been confirmed by its
  ability to strongly bind to the reduced, carboxymethylated form of alpha-lactalbumin"].
- Retired: GO:0051082 IDA (PMID:9183013); review kept, note added.

Action changes:
- GO:0005515 IPI PMID:21808025 (with rat ERalpha P06211): MARK_AS_OVER_ANNOTATED -> REMOVE
  (protein-binding policy). Abstract-only; the abstract is about CHIP-mediated ERalpha
  degradation and does not support a specific MF such as nuclear receptor binding.
- GO:0046983 protein dimerization activity (IEA, InterPro Hip_N): MARK_AS_OVER_ANNOTATED
  -> KEEP_AS_NON_CORE; the claim is accurate [PMID:23812373 "Here we present crystal
  structures of the dimerization domain"].
- GO:0032991 protein-containing complex (IDA x2): MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE;
  generic but not overreaching.
- GO:0032564 dATP binding (IDA): ACCEPT -> KEEP_AS_NON_CORE (real in vitro observation,
  not core function).
- GO:0009617 response to bacterium (ISO from mouse St13): UNDECIDED -> MARK_AS_OVER_ANNOTATED.
  QuickGO shows the mouse source (Q99L47) is IEP from PMID:23012479, a transcriptomic
  study of listeriosis; expression change is not participation.
- Added supported_by quotes to two PMID:7585962 rows that lacked them.
- Description: oligomeric state now reflects both the SEC tetramer [PMID:9183013 "the
  chaperone forms a tetramer"] and the structural dimerization-domain data.

Open questions:
- Whether GO:0140309 unfolded protein holdase activity would describe the isolated,
  refolding-inhibiting behaviour of Hip better than GO:0044183.

Review follow-up 2026-10-19: the merge-queue integration run for PR #4624 failed in the
repository test suite (not in gene validation). The BioReason-Pro SFT prediction review for
GO:0032991 protein-containing complex (St13-sft-predictions.yaml, added on main after this
branch was cut) had been audited to NPI on the basis of the earlier MARK_AS_OVER_ANNOTATED
actions; this re-review keeps both GO:0032991 rows as KEEP_AS_NON_CORE, so the deterministic
cross-check flagged the prediction as NPI against a positive AIGR action. Re-ran
scripts/auto_review_sft_predictions.py --apply on the branch merged with main; it reclassified
that one prediction NPI -> CNN (confidence 0 -> 2) with the audit note updated. Changes the
script proposed to other genes outside this PR were not taken.

Review follow-up 2026-10-19 (second pass, PR #4624): the GOA refresh retired every GO:0051082
unfolded protein binding row for St13 (replaced by GO:0044183 protein folding chaperone), so the
BioReason-Pro SFT prediction rationale "Term is in GOA" for GO:0051082 was no longer true; the CNN
assessment stands (the concept is a known curated annotation via GO:0044183) and the rationale now
says so. Also replaced the title-only quote on GO:0009617 response to bacterium with the abstract
sentence that establishes PMID:23012479 as a transcriptomic expression screen.
