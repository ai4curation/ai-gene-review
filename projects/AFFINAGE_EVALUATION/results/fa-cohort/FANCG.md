# FANCG (FANCG) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 30 discoveries · self-eval pairwise "win" (faith 100%) · gates passed.

## Agreement (brief)

Both sources converge on the central biology: FANCG (= XRCC9) is a TPR-repeat
scaffold subunit of the nuclear Fanconi anemia (FA) core complex, with no intrinsic
catalytic or DNA-binding activity. It binds FANCA directly, is required for complex
assembly/stability/nuclear accumulation, and the assembled core complex drives
damage-induced FANCD2(-FANCI) monoubiquitination and replication-coupled interstrand
crosslink (ICL) repair. Affinage's narrative (FANCA-FANCG mutual stabilization and
nuclear import, cryo-EM contacts, TPR-motif interaction scaffold, requirement for
FANCD2 monoubiquitination, mitochondrial/PRDX3 oxidative-stress pool) is fully
consistent with the AIGR review's `core_functions` (adaptor activity + ICL repair +
DNA damage response, nucleoplasm/chromatin, FA nuclear complex) and its non-core
classification of the mitochondrial role.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| MF grounding | `mechanism_profile`: GO:0060090 molecular adaptor activity **and** GO:0005198 structural molecule activity | Adaptor activity grounded specifically as GO:0030674 protein-macromolecule adaptor activity (NEW); no structural-molecule term | **AIGR.** GO:0030674 is the precise adaptor term for a protein-protein bridging scaffold; GO:0005198 (structural constituent, e.g. cytoskeleton/ribosome) is the wrong sense for a signaling/assembly adaptor. Affinage's layer is coarse and lists both parents. |
| HR-mediated DSB repair | Foregrounds a Ser7-dependent D1-D2-G-X3 (BRCA2/FANCD2/XRCC3) complex and "FANCG required for efficient HR repair of DSBs" (PMID:12861027, PMID:18212739, PMID:16621732) | Originally folded HR only into the `core_functions` prose; no discrete HR annotation | **Affinage flags a real gap.** AIGR now **adds** GO:0000724 (double-strand break repair via HR), NEW/non-core, citing PMID:12861027 (DT40 knockout, ~9-fold HR drop) + PMID:18212739. Direct experimental, correctly branched. |
| DNA-binding MF | Narrative does not claim FANCG binds DNA; grounding lists only adaptor/structural MF | GOA legacy TAS "damaged DNA binding" (GO:0003684) flagged MARK_AS_OVER_ANNOTATED | **Agreement in substance.** Affinage's narrative implicitly agrees FANCG has no DNA-binding activity; AIGR makes the over-annotation call explicit. |
| Localization | `mechanism_profile`: nucleus, cytosol, mitochondrion (flat list, no core/non-core weighting) | Nucleus/nucleoplasm/chromatin = core; cytosol/cytoplasm/mitochondrion/nuclear-speck = non-core | **AIGR.** Same locations, but AIGR correctly weights the nuclear/chromatin pool as functional and demotes the minor cytoplasmic/mito pools. |
| Reactome pathway | Collapses to R-HSA-73894 "DNA Repair" and R-HSA-1643685 "Disease" (very general parents) | Uses specific Reactome ICL-repair reactions for nucleoplasm localization | **AIGR.** Affinage's Reactome grounding is at uninformative top-level nodes. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:12861027 | FANCG required for efficient HR repair of I-SceI-induced DSBs (DT40 knockout, ~9-fold) | New reference (HIGH/VERIFIED) + `supported_by` for the new GO:0000724 annotation |
| PMID:18212739 | Ser7-phospho FANCG promotes D1-D2-G-X3 (BRCA2/FANCD2/XRCC3); FANCG–XRCC3 epistatic for crosslink sensitivity | New reference (HIGH/VERIFIED) + `supported_by` for the new GO:0000724 annotation |

## Net assessment

AIGR was already the stronger, better-grounded record: correct precise MF term
(GO:0030674 vs Affinage's coarse GO:0060090/GO:0005198 pair), correct core/non-core
weighting of localizations, and an explicit over-annotation call on legacy "damaged
DNA binding" that Affinage's coarse GO layer would not surface. Affinage's value here
was the dense, correctly-cited narrative, which surfaced one genuine gap: FANCG's
direct, experimentally demonstrated requirement for HR-mediated DSB repair (via the
Ser7-dependent D1-D2-G-X3 complex). That function is now added as a single NEW,
non-core GO:0000724 annotation backed by two verified primary papers. No Affinage
`mechanism_profile` GO ids were imported, and no existing AIGR decision was weakened.
