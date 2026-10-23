# CO (CONSTANS; At5g15840; UniProtKB:Q39057) notes

## 2026-10-06: review pass (photoperiodic_flowering_co_ft module)

- No PENDING rows remained. Three GO:0005515 rows previously MARK_AS_OVER_ANNOTATED (PHL, PMID:24127609;
  DELLA, PMID:26801684; miP1a/b, PMID:27015278) changed to REMOVE (term only) because the validator's
  protein-binding policy excludes MARK_AS_OVER_ANNOTATED for this term; the interactions are not disputed
  and remain described in the review summaries.
- Two high-throughput protein-binding rows (PMID:21798944 AI-1 interactome; PMID:28650476 CrY2H-seq)
  left UNDECIDED: the specific CO pairs are only in supplementary tables not in the local cache.
- Fixed a folded-scalar hyphen split ("sign-neutral").
- Core function (GO:0001228 with GO:0048578) is used unchanged as the CO annoton in
  modules/photoperiodic_flowering_co_ft.yaml.

## 2026-10-06 follow-up (all UNDECIDED resolved)

- High-throughput protein-binding rows PMID:21798944 (CO-BBX32) and PMID:28650476 (CrY2H-seq) -> REMOVE
  (term only), following the protein-binding policy.
