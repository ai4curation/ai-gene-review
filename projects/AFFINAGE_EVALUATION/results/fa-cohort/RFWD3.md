# RFWD3 (FANCW) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 17 discoveries · self-eval `win` (faith 100%) · gates passed.

## Agreement (brief)

Affinage and the AIGR review converge on the core biology, and the AIGR review was
already comprehensive here:

- RFWD3 is a **RING-type E3 ubiquitin ligase** (EC 2.3.2.27, catalytic Cys315) — AIGR core
  molecular function `GO:0061630`.
- Recruited via its **C-terminal WD40 domain to RPA2** on ssDNA at stalled forks / damage
  sites; **polyubiquitinates RPA and RAD51** to drive their VCP/p97-dependent turnover,
  enabling **HR** (`GO:0000724`) and **ICL repair** (`GO:0036297`, RFWD3 = FANCW).
- **ATR/ATM phosphorylation-dependent** activity; promotes ssDNA-protein ubiquitination →
  **PCNA ubiquitination / TLS**.
- Nuclear / site-of-DNA-damage localization; **secondary MDM2-p53 stabilization** role,
  which AIGR correctly demotes to `KEEP_AS_NON_CORE`.

All 8 of Affinage's shared PMIDs (20173098, 21504906, 21558276, 26474068, 28575657,
28575658, 28691929, 33321094) were already cited and adjudicated in the AIGR review.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding of MF | `mechanism_profile` gives only coarse parents: `GO:0016874` ligase activity, `GO:0140096` catalytic activity acting on a protein | Specific `GO:0061630` ubiquitin protein ligase activity | **AIGR right.** Affinage's own note flags the profile as coarse; `GO:0016874` (generic ligase, C–O/C–N/C–S bond formation) is arguably a different branch from thioester-forming Ub transfer. Do not import. |
| Localization grounding | `GO:0005634` nucleus + `GO:0000228` nuclear chromosome | nucleus + `GO:0090734` site of DNA damage / `GO:0035861` etc. | **AIGR right/finer.** `GO:0000228` (nuclear chromosome, the condensed structure) is not where an RPA/ssDNA-recruited fork factor is best placed; AIGR's damage-site/fork terms are more accurate. |
| Pathway layer | Reactome DNA Repair, DNA Replication, Disease, **Metabolism of proteins** | process terms grounded per-annotation | **AIGR right.** "Metabolism of proteins" is a frequency-biased over-general parent (any ubiquitination event); uninformative for this gene. |
| p53 / MDM2 axis | folded into the mechanistic narrative at similar prominence | `KEEP_AS_NON_CORE` (single-group, secondary) | **AIGR right.** Correct scoping; the axis is real (PMID:20173098) but peripheral to the replication-stress core. |
| TREX1 / STING immune role (PMID:41117130) | listed as a 2025 finding | absent | **AIGR defensibly conservative.** Single 2025 paper, distinct pathway; not yet warranting a curated annotation. Noted, not imported. |
| ORC/ORCA stabilization (PMID:33044890) | listed (self-rated **Low** confidence) | absent | **AIGR right to omit.** Affinage itself rates it Low; p53-context-dependent, single group. |
| Drosophila Mus302 (PMID:31900333) | listed | absent | **Correctly excluded** — ortholog/evolution context, not human RFWD3 function; HR role is mammal-specific per that paper. |

No factual conflicts requiring an AIGR reversal; the disagreements are the expected
coarse/over-general GO layer plus a few recent single-group over-reaches AIGR rightly excludes.

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| 30530694 | RFWD3 at unperturbed forks; PCNA/PIP binding stabilizes RFWD3; normal fork progression / DNA replication | Added to `references` (relevance MEDIUM, VERIFIED) + verbatim `supported_by` on the `GO:0031297` replication fork processing annotation |
| 37036693 | RFWD3 recruits ZRANB3 and stimulates fork remodeling/reversal (ZRANB3-epistatic) via PCNA ubiquitination | Added to `references` (relevance MEDIUM, VERIFIED) + verbatim `supported_by` on the same `GO:0031297` annotation |

Both are full-text, RFWD3-focused functional studies that were missing from the review and
that corroborate/extend the (already accepted) replication-fork-processing role. No existing
decisions were weakened. Other Affinage-only PMIDs (32391871, 35905994, 40940676, 41117130,
41372167, 33044890, 31900333) were reviewed and **not** incorporated: they are corroborating
context, single-group recent findings, or non-human, none altering a curation call.

## Net assessment

The AIGR review is stronger than the Affinage record on GO grounding, scoping, and evidence
adjudication — Affinage's `mechanism_profile` collapses to over-general (sometimes wrong-branch)
parents and should not be imported. Affinage's value here is its **dense, dated PMID narrative**,
which surfaced two legitimate RFWD3-focused mechanistic papers (PCNA/fork progression; ZRANB3/fork
remodeling) absent from the review. These were incorporated conservatively as corroborating
evidence on the existing fork-processing annotation. **0 new annotations, 2 papers incorporated,
review remains ✓ Valid.**
