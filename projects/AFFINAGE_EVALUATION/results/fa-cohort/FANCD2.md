# FANCD2 (FANCD2) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 60 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for FANCD2 is one of its richest: a PMID-dense (60 citations) mechanistic
narrative covering the full FA-pathway life cycle (ATR/ATM priming → FANCL/UBE2T monoubiquitination
of K561 → ID2 sliding-clamp closure → downstream nuclease/HR coordination → USP1-UAF1 reversal)
plus the non-canonical activities (fork protection, R-loop suppression, TAp63/skin-cancer
suppression, mitochondrial homeostasis). The AIGR review is curated, GOA-grounded and validated.

## Agreement (brief)

The two sources agree on the core biology. Both center FANCD2 on replication-coupled interstrand
crosslink (ICL) repair as an obligate FANCI-FANCD2 (ID2) heterodimer that, upon K561
monoubiquitination, closes into a sliding DNA clamp encircling duplex DNA and coordinates
incision/TLS/HR (AIGR: GO:0036297 ACCEPT ×2, GO:1990391 DNA repair complex ACCEPT, core_functions;
Affinage narrative + PMID:32066963/32269332/19965384). Both treat nuclear/chromatin localization,
the intra-S checkpoint, and FAN1 recruitment by Ub-FANCD2 as established. Both recognize a
single-stranded/branched-DNA-binding scaffold activity (AIGR NEW GO:0003697; Affinage
PMID:19609304/21764741).

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | molecular_activity list includes `GO:0031386 protein tag activity`, `GO:0140096 catalytic activity acting on a protein`, `GO:0140110 transcription regulator activity`; localization list flattens to `nucleus`/`nucleoplasm`/`mitochondrion` | Uses specific, evidence-matched terms; FANCD2 is the ubiquitination *substrate*, not a tag/ligase/DUB, and its TAp63 effect is indirect | **AIGR right.** Affinage's own note flags this layer as coarse and self-contradictory. "protein tag" / "catalytic activity acting on protein" mis-assign FA-core-complex (FANCL/UBE2T/USP1) activities to FANCD2. Do not import. |
| `protein binding` (GO:0005515) | Narrative leans on many PPIs (FANCI, BRCA2, MEN1, MRN, FAN1, CEBPD, EGFR) | 11 IPI `protein binding` rows REMOVE'd as uninformative; interactions retained as process/complex/specific-MF or notes | **AIGR right** per curation policy; Affinage does not assert the generic term, so no true conflict. |
| Transcription regulation of TAp63 | Ub-FANCD2 "activates transcription of TAp63" (PMID:23806336); mechanism profile lists transcription regulator activity | Not annotated as a transcription-regulator MF | **AIGR right to exclude** the MF: the effect is a downstream/indirect senescence-tumor-suppression output, not a demonstrated sequence-specific DNA-binding transcription-factor activity of FANCD2. Reasonable to leave unannotated. |
| Replication fork protection/restart | Strongly evidenced as a distinct function (PMID:23993743, 24556218, 25659033, 26797144, 27264184) | Mentioned in description/core prose but **had no GO annotation** | **Affinage surfaced a real gap.** Added NEW GO:0031297 (replication fork processing) + core_functions entry (see below). |
| R-loop suppression | Multiple papers: FANCD2 resolves R-loops via hnRNP U/DDX47 and SRSF1 (PMID:29394375, 30431240, 30650351, 38165804) | Not annotated | **Affinage right that it is real; AIGR was missing it.** Added NEW GO:0062176 (R-loop processing), non-core. |
| Mitochondrial role | FANCD2 localizes to mitochondria, ATAD3/TUFM nucleoid association (PMID:28378742, 28687786) | Not annotated | **Affinage right that a mito pool exists.** Added NEW GO:0005739 (mitochondrion) as a non-canonical, non-core localization. |
| Meiotic pairing / meiotic-recombination DSB repair | Not emphasized (Affinage is somatic-DNA-repair focused) | KEEP_AS_NON_CORE (IBA, germline-restricted) | **AIGR right** — germline specialization correctly demoted; Affinage silence is not a conflict. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:15601828 | HR-mediated DSB repair (GO:0000724) | Added verbatim `supported_by` (FANCD2-null DT40 defective in HR DSB repair / Ig gene conversion) to strengthen a NEW annotation that previously had only UniProt support; reference + `reference_review` (MEDIUM/VERIFIED). |
| PMID:25659033 | Replication fork restart (GO:0031297) | `original_reference_id` for new GO:0031297 annotation; verbatim `supported_by` (BLM-dependent restart of APH-stalled forks, suppresses new origins, core-complex-independent); reference_review HIGH/VERIFIED. |
| PMID:26797144 | Fork protection (GO:0031297) | Second `supported_by` for GO:0031297 (Ub-FANCD2/FAN1 restrains fork progression, prevents chromosome abnormalities without ICLs); reference_review MEDIUM/VERIFIED. |
| PMID:30431240 | R-loop processing (GO:0062176) | `original_reference_id` for new GO:0062176; verbatim `supported_by` (FANCD2 suppresses R-loop levels; recruits hnRNP U/DDX47); reference_review MEDIUM/VERIFIED. |
| PMID:38165804 | R-loop processing (GO:0062176) | Second `supported_by` for GO:0062176 (FA-pathway defects → R-loop accumulation/genomic instability); reference_review MEDIUM/VERIFIED. |
| PMID:28378742 | Mitochondrion (GO:0005739) | `original_reference_id` for new GO:0005739; verbatim `supported_by` (FANCD2 localizes to mitochondrion, associates with ATAD3/TUFM); reference_review LOW/VERIFIED. |

All six PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a whitespace-normalized
verbatim substring of the cached abstract/full text. GO terms verified against QuickGO
(GO:0031297 processing = restore/restart stalled fork; GO:0062176 = R-loop disassembly; both
current, correctly branched BP; GO:0005739 current CC). The obsolete GO:0048478 "replication fork
protection" was deliberately not used.

## Net assessment

The AIGR review and Affinage agree on FANCD2's core ICL-repair/ID2-clamp biology; Affinage's own
GO/Reactome `mechanism_profile` is coarse and in places wrong-branch (protein-tag / catalytic /
transcription-regulator activities that belong to FANCD2's partners, not FANCD2) and was correctly
not imported. Affinage's value here was its dense narrative surfacing three genuine, well-evidenced
functions the GOA-grounded review had described in prose but not annotated: replication fork
protection/restart, R-loop suppression, and a non-canonical mitochondrial pool. These were added
conservatively as validated NEW annotations (plus one strengthened HR annotation), with fork
processing promoted into `core_functions`. No existing AIGR decision was weakened by Affinage's
coarse GO layer. File remains ✓ Valid.
