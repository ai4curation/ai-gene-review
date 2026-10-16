# ORMDL3 curation notes

## 2026-09-04 — finishing pass (PAINT no-IBA project)

Performed the finishing quality pass over `ORMDL3-ai-review.yaml` (drafted with all
actions assigned) and completed the companion family review for PANTHER:PTHR12665.

What was checked / changed:

- Re-verified all `existing_annotations` entries against the GOA table and cached
  publications; all actions were found justified and no action changes were made.
  All `supported_by` quotes pass the verbatim-substring validator.
- Cleared the remaining validation warning ("No annotations reference available
  deep research files") by adding a verbatim `supported_by` quote from
  `file:human/ORMDL3/ORMDL3-deep-research-falcon.md` to the GO:0090156
  (intracellular sphingolipid homeostasis) IBA entry, where the deep-research
  synthesis of the ceramide feedback loop genuinely informed the ACCEPT call
  (the file was already listed in `references` and in `additional_reference_ids`).
- Verified the author-supplied term ids: core_functions MF terms (GO:0004857
  enzyme inhibitor activity, GO:0097001 ceramide binding) pass the hard
  branch/label validation, and the NEW-annotation term GO:0090155 was confirmed
  against OLS as "negative regulation of sphingolipid biosynthetic process"
  (non-obsolete).
- Set `status: COMPLETE` (no PENDING actions, zero validation warnings).

Action distribution: 14 ACCEPT, 3 MODIFY (the SPTLC1-interaction protein-binding
IPIs from PMID:20182505/33558761/33558762, proposed replacement GO:0004857 —
the structures show the ORMDL3 N-terminus physically occluding the SPT substrate
tunnel [PMID:33558761 "ORMDL3 blocks the tunnel and competes with substrate binding through its amino terminus"]),
1 MARK_AS_OVER_ANNOTATED (the HuRI HT screen protein-binding IPI),
4 KEEP_AS_NON_CORE (the PMID:28747345 B-cell/autophagy/ATF6 annotations —
downstream immune phenotypes of the sphingolipid/ER-stress axis, not core
molecular functions), 4 REMOVE (the four Reactome TAS localizations to plasma
membrane / secretory granule membrane / specific granule membrane, contradicted
by the primary localization literature [PMID:12093374 "these data show that the ORMDL proteins locate at the ER membrane"]),
and 3 NEW (GO:0004857, GO:0097001, GO:0090155).

Notable curation findings:

- **The "human no-IBA" flag for this gene is stale.** The current GOA slice has
  four IBA rows from PAINT node PTN000292374 (GO:0030148, GO:0090156,
  GO:0017059, GO:0006672), all reviewed ACCEPT. The cached
  `PTHR12665-paint.tsv` carries IBD rows for three of these (GO:0017059,
  GO:0006672, GO:0090156) but not GO:0030148 — a snapshot discrepancy noted in
  the family review.
- ORMDL3 appearing in its own WITH/FROM for the SPT-complex and ceramide IBAs is
  expected (its own experimental annotations seeded the IBDs), not circular.
- The ceramide-sensing mechanism is now structurally settled
  [PMID:37308477 "Structure-guided mutational analyses reveal the essential function of this ceramide binding site for the suppression of SPT activity."].
