# XRCC2 (FANCU) — AIGR vs Affinage

**Affinage record:** run 2026-06-11 · 29 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for XRCC2 is a tight, PMID-dense (29 citations) mechanistic narrative that
correctly frames XRCC2 as a RecA/RAD51-family HR protein acting as a stable subunit of the RAD51
paralog complexes (BCDX2 and the XRCC3-containing complex), essential for HR but not NHEJ, and
required for damage-induced RAD51 focus formation without needing its own ATP binding. It layers on
the FA (FANCU), meiotic, replication-fork and centrosome/mitotic strands. The AIGR review is
curated, GOA-grounded and validated.

## Agreement (brief)

Both sources center XRCC2 on the same core biology: an obligate subunit of the BCDX2 complex
(GO:0033063) acting as an HR **mediator** that promotes RAD51 nucleoprotein-filament nucleation and
extension on ssDNA/branched-DNA intermediates, required for DSBR-HR (GO:0000724) and strand
invasion (GO:0042148), acting downstream of BRCA2 and upstream of RAD51 recruitment. Both treat
XRCC2 as *not* a classic recombinase/strand-exchange enzyme in its own right, and both note that the
ATP hydrolysis powering the complex is contributed by RAD51B/RAD51C while XRCC2 only binds ATP
(the 2023/2026 cryo-EM structures, PMID:37344587, PMID:41196948). Both keep centrosome/mitotic and
meiotic roles as peripheral/context-specific rather than the core molecular function.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| `mechanism_profile` GO layer | molecular_activity list = `GO:0003677 DNA binding`, `GO:0140657 ATP-dependent activity`, `GO:0098772 molecular function regulator activity`, `GO:0140096 catalytic activity acting on a protein`; localization flattens to `nucleus`/`chromosome` | Uses specific evidence-matched MF (`GO:0000400 four-way junction DNA binding`) and locations (replication fork, nucleoplasm, centrosome) | **AIGR right.** Affinage's own note flags this layer as coarse (collapses to general parents) and self-contradictory. `catalytic activity acting on a protein` and a bare `ATP-dependent activity` mis-cast a structural mediator subunit as an enzyme; do not import. |
| ATP-dependent DNA damage sensor MF (GO:0140664) | Not asserted; narrative explicitly says XRCC2 acts "without itself requiring ATP binding" (PMID:11301337, 11834724, 19470754) | MARK_AS_OVER_ANNOTATED (InterPro over-propagation of RecA/RAD51 ATPase) | **AIGR right, and Affinage corroborates it.** Used Affinage's PMID:11301337 to strengthen the over-annotation call (see below). |
| Fanconi anemia / interstrand-crosslink repair (FANCU) | Emphasized: XRCC2 acts late in the FA pathway downstream of FANCD2 monoubiquitination (PMID:27208205) | Described in prose (`description`) as FANCU/ICL repair but **had no ICL-repair GO annotation** — only general DNA repair + DSBR-HR | **Affinage surfaced a real annotation gap.** Added NEW GO:0036297 (interstrand cross-link repair), IMP, PMID:27208205 (see below). |
| Meiotic role | Strong human/mouse evidence: p.Leu14Pro → meiotic arrest, azoospermia, POF, infertility (PMID:30042186) | KEEP_AS_NON_CORE, supported only by the weak 1998 testis-expression inference (PMID:9628903) | **Both agree it is real & non-core; AIGR's evidence was thin.** Strengthened the existing meiotic annotation with PMID:30042186. |
| Replication-fork restraint | Distinct XRCC2-specific function: restrains fork progression during dNTP imbalance via ATR-Ser247 phosphorylation (PMID:30566856) | Replication-fork localization/function annotated, but cited via paralog-general papers (PMID:32669601, 20207730) | **Complementary.** Added PMID:30566856 as XRCC2-specific corroboration; no decision changed. |
| Centrosome / mitotic role | Mentioned (PMID:11025669 centrosome fragmentation) | KEEP_AS_NON_CORE (GO:0005813, GO:0007098, GO:0000278) | **AIGR right to demote.** Likely an indirect consequence of genome instability; Affinage does not contest non-core status. |
| Transcriptional / proliferation roles (ZNF281, c-Myc, NSCLC/FOS) | Includes PMID:26300006, 39153434 as XRCC2-regulation / cancer-proliferation findings | Not annotated | **AIGR right to exclude.** These describe *regulation of XRCC2 expression* and downstream oncogenic phenotypes, not a molecular function of the XRCC2 protein. Correctly left unannotated. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:10517641 | DSBR-HR (GO:0000724) | Added verbatim `supported_by` to the IEA HR annotation that previously lacked supporting_text (>100-fold HR decrease, NHEJ normal); reference + reference_review HIGH/VERIFIED. |
| PMID:11301337 | over-annotation of ATP-dependent DNA damage sensor (GO:0140664) | Added second verbatim `supported_by` ("it does not make use of ATP binding to promote this function") strengthening the MARK_AS_OVER_ANNOTATED call; reference_review HIGH/VERIFIED. |
| PMID:27208205 | interstrand cross-link repair (GO:0036297) | `original_reference_id` for the NEW ICL-repair annotation; verbatim `supported_by`; reference_review HIGH/VERIFIED (FANCU; corrects MMC/ICL phenotypes). |
| PMID:30042186 | meiotic cell cycle (GO:0051321) | Added verbatim `supported_by` (p.Leu14Pro meiotic arrest/infertility in human & knockin mouse) strengthening the non-core meiotic annotation; reference_review HIGH/VERIFIED. |
| PMID:30566856 | replication fork (GO:0005657) | Added XRCC2-specific `supported_by` to the NAS replication-fork annotation (restrains active DNA synthesis; ATR-Ser247); reference_review MEDIUM/VERIFIED. |

All five PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a whitespace-normalized
verbatim substring of the cached abstract/full text. GO:0036297 verified against QuickGO
(non-obsolete biological_process, "interstrand cross-link repair", is_a child of DNA repair).

## Net assessment

AIGR and Affinage agree on XRCC2's core BCDX2-mediator / RAD51-filament-assembly biology, and
Affinage's narrative actually reinforces two AIGR judgment calls (XRCC2 is not an ATP-dependent
damage sensor; meiotic and centrosome roles are peripheral). Affinage's own `mechanism_profile` GO
layer is coarse and in places wrong-branch ("catalytic activity acting on a protein", bare
"ATP-dependent activity") and was correctly not imported. Affinage's value here was surfacing one
genuine annotation gap — the FANCU / interstrand-crosslink-repair role that AIGR had only in prose —
now added as a validated NEW annotation (GO:0036297), plus four strengthened citations
(HR, meiosis, replication fork, and the over-annotation rebuttal). No existing AIGR decision was
weakened by Affinage's coarse GO. File remains ✓ Valid (single benign deep-research warning).
