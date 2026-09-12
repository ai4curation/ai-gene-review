# FANCC (FANCC) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 34 discoveries · self-eval `win` (faith 100%) · gates passed.

Affinage supplies a strong, PMID-dense mechanistic narrative (34 citation-anchored findings)
plus a coarse `mechanism_profile` GO/Reactome layer. The AIGR review is the curated,
GOA-grounded, validated review (41 GOA annotations reviewed; `status: COMPLETE`).

## Agreement (brief)

- **Core role is identical.** Both place FANCC as a non-catalytic subunit of the nuclear FA
  core complex (with FANCA/E/F/G) required for FANCD2–FANCI monoubiquitination and
  replication-coupled interstrand cross-link (ICL) repair; both flag the L554P patient
  mutation as abolishing FANCA/FANCE binding and complementing activity.
- **Substrate-recognition module.** Affinage's "FANCC–FANCE–FANCF anti-crossover subcomplex"
  and complex-assembly interdependencies match the AIGR `core_functions` adaptor model
  (molecular adaptor activity contributing to the complex's ubiquitin-ligase activity).
- **Dual localization.** Both record a major nuclear form and a minor cytoplasmic pool
  (GRP94/HSP70 associated).
- **Non-core signaling/redox roles are real but separable.** Both acknowledge the cytoplasmic
  anti-apoptotic (PKR/Hsp70), IFN-γ/STAT1, and redox/detoxification roles; AIGR files them as
  non-core, and Affinage's own cited evidence supports that separability (see below).

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| MF grounding | `mechanism_profile`: molecular adaptor activity, molecular function regulator activity, **DNA binding (GO:0003677)** | Molecular adaptor activity (informative MF replacing `protein binding`); no DNA-binding MF | **AIGR.** Affinage's DNA-binding call rests on FANCA/C/G co-purifying on psoralen-crosslinked DNA affinity columns (PMID:11401546) — a complex-level pulldown, not evidence FANCC is a sequence/structure-specific DNA-binding protein. Importing GO:0003677 would over-annotate. |
| Coarse pathway layer | Reactome tags include Programmed Cell Death, Signal Transduction, Autophagy, Reproduction as co-equal to DNA Repair | Core = ICL repair / complex assembly; apoptosis, STAT1 signaling, autophagy, meiotic anti-crossover treated as non-core / out of GOA scope | **AIGR.** The flat Reactome layer loses the core-vs-non-core distinction. The deep-research note itself warns this grounding "collapses to general parents and can contradict the narrative." |
| STAT1/PKR anti-apoptotic role | Emphasized as a major independent function of cytoplasmic FANCC | Kept as **non-core**, structurally separable from ICL repair | **AIGR (and Affinage's own citations confirm it).** PMID:12397061 and PMID:11520787 show FANCC mutants that lose PKR/STAT1 function still complement MMC sensitivity and FANCD2 activation — separable, hence non-core. Affinage's evidence does **not** change the call. |
| NER | Not asserted | GO:0006289 nucleotide-excision repair `MARK_AS_OVER_ANNOTATED` | No conflict; AIGR is more precise (ICL repair, not classical NER). |

## Over-reaches AIGR correctly excludes

- **DNA binding (GO:0003677)** — Affinage `mechanism_profile` only; unsupported at the FANCC
  monomer level (see table).
- Large-scale/network `protein binding` interactions (SMAD4, FBXW7, MEOX2, AKT1) — AIGR marks
  these over-annotated; Affinage does not surface them (correctly ignores).

## Functions AIGR previously under-cited (now strengthened from Affinage papers)

- **Redox/detoxification** basis of the oxidative-stress annotation — Affinage surfaced
  PMID:9787138 (FANCC attenuates NADPH cytochrome P450 reductase), which is the actual redox
  evidence the AIGR reason invoked; it previously cited only a STAT1 study.
- **Interdependent FA complex assembly** — PMID:11063725 (FANCF nuclear complex; loss of any
  FA protein except FANCD disrupts assembly) strengthens the complex-assembly annotation.

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:11063725 | Interdependent FA core complex assembly | Added `supported_by` on GO:0065003 (protein-containing complex assembly) + `reference_review` (MEDIUM/VERIFIED) |
| PMID:9787138 | FANCC redox/detoxification (NADPH cytochrome P450 reductase) | Added `supported_by` on GO:0034599 (cellular response to oxidative stress, non-core) + `reference_review` (MEDIUM/VERIFIED) |
| PMID:12397061 | FANCC–Hsp70–PKR anti-apoptotic function, independent of the FA complex | Added as `reference` with `reference_review` (MEDIUM/VERIFIED); documents non-core PKR role and confirms its structural separability |

No NEW GO annotations were added: the anti-apoptotic/STAT1/redox functions have no matching
GOA annotation and remain correctly scoped as non-core context in the `description`, so adding
new core-level terms was not warranted.

## Net assessment

The AIGR review and Affinage agree on all core biology; the review is more disciplined on GO
grounding (informative adaptor MF instead of coarse regulator/DNA-binding tags; explicit
core-vs-non-core partitioning that Affinage's flat Reactome layer erases). Affinage's chief
value here was surfacing well-cited older primary papers (redox/RED, FANCF interdependence,
PKR separability) that let us attach verbatim support to two existing annotations and
substantiate the non-core signaling roles. Affinage's evidence **reinforces** rather than
overturns the review's non-core calls for the STAT1/PKR/redox functions. No factual conflicts
requiring a change of any existing annotation decision. Validation: **✓ Valid**.
