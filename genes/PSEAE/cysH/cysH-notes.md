# cysH review notes


## Comparative sulfate-assimilation audit — 2026-10-26

Completed all 14 seeded rows. Read full [PMID:10613872]: native disruption, E. coli complementation, and purified APS-not-PAPS reduction with thioredoxin. [PMID:11940598] adds direct [4Fe-4S] spectroscopic evidence;[PMID:16289027] adds donor adduct/interaction evidence. The broad family label does not override direct substrate specificity. General activity terms refined; catalytic pathway participation retained, without adding redundant NEW terms.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.

Propagation metadata follow-up: recorded the actual PAINT ancestral source as SUPPORTS_TRANSFER; donor-specific refinement does not invalidate the inherited broader activity.

## 2026-10-26 PR #5560 evidence follow-up

Corrected the copied strain name in the iron-sulfur-cluster rationale from KT2440 to PAO1; the biological action is unchanged.

All original annotation payloads and row order are preserved. Focused validation and automatic record-section backfill pass; generated pages and append-only history record this follow-up.

## PseudoCAP IBA-seed assessment (tier 2, 2026-11-05)

Audit only; the existing review was not rewritten. The seed paper PMID:10613872 has
cached full text, which reports both a native knockout and purified-enzyme assays
[PMID:10613872 "Insertional knockout mutation of P. aeruginosa cysH produced cysteine auxotrophy, indicating its role in sulfate assimilation."].

Seeds of PTN008207357 for GO:0000103 (`.cache/paint/IBD.gaf`, column 8): AT1G62180 (APR2,
P92981), AT4G04610 (APR1, P92979), AT4G21990 (APR3, P92980) and O05927 (this gene).
QuickGO (2026-11-05) shows TAIR IDA rows for GO:0000103 on all three APRs (PMID:9653199;
APR1 also PMID:8917600), and IDA rows for GO:0009973 adenylyl-sulfate reductase activity.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008207357 | GO:0000103 sulfate assimilation | 4 | 96 (48 taxa) | GO:0000103 sulfate assimilation, IMP, PMID:10613872 (PseudoCAP) | SOUND | The knockout is a cysteine auxotroph and the purified enzyme reduces APS (not PAPS) with thioredoxin, so CysH performs a step of the pathway. The node term suits an APS-reductase clade spanning bacteria and plants. | Arabidopsis APR1, APR2, APR3 (TAIR IDA) | Yes. No GO_CENTRAL defect. |

No corrections to the existing annotation actions.
