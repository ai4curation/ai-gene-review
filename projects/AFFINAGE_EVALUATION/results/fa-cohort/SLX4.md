# SLX4 (FANCP) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 57 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for SLX4 is a strong, PMID-dense (57 citations) mechanistic narrative
covering the full scaffold biology: assembly/activation of the three structure-specific
endonucleases (SLX1, XPF-ERCC1, MUS81-EME1), CDK1-driven SLX-MUS holoenzyme formation,
ubiquitin/SUMO-directed recruitment, the SLX4-TRF2 telomere toolkit, ALT processing, and the
FANCP/FA-P disease link. The AIGR review is curated, GOA-grounded and validated.

## Agreement (brief)

The two sources agree on the core biology. Both center SLX4 as a **nuclease-dead multidomain
scaffold/regulatory subunit** that docks and stimulates SLX1, XPF-ERCC1 and MUS81-EME1 to process
branched DNA in interstrand crosslink (ICL) repair, HR-mediated DSB repair and single-strand
annealing (AIGR: GO:0008047 enzyme activator ACCEPT, GO:0060090 molecular adaptor NEW,
GO:0033557 Slx1-Slx4 complex ACCEPT ×many, GO:0036297 ICL repair NEW, GO:0000724 HR ACCEPT,
core_functions; Affinage narrative + PMID:19595721/19596235/19596236). Both treat the SLX1-SLX4
module as a Holliday-junction resolvase, both keep telomere-maintenance / t-circle / D-loop roles
(SLX4-TRF2) as genuine-but-specialized, and both anchor the disease role in FANCP (PMID:21240275/277).
Crucially, both are explicit that **SLX4 itself does not cut DNA** — the catalysis belongs to its
bound partner nucleases.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | molecular_activity list flattens to `GO:0140097 catalytic activity, acting on DNA`, `GO:0016740 transferase activity`, `GO:0003677 DNA binding`, `GO:0060090 adaptor`, `GO:0098772 regulator`; localization to `nucleus`/`nuclear chromosome`/`nucleoplasm` | Uses specific, evidence-matched terms; the informative MF is molecular adaptor + enzyme activator, not "catalytic activity, acting on DNA" | **AIGR right.** Affinage's own note flags this layer as coarse. `GO:0140097 catalytic activity, acting on DNA` wrongly implies SLX4 is itself the nuclease; that activity belongs to SLX1/XPF/MUS81. Do not import. |
| Nuclease catalysis attribution | Narrative is careful ("scaffold that assembles and activates"; SLX1 is "the active subunit"), but the coarse GO layer lists DNA-catalytic/transferase activity on SLX4 | SLX4 is nuclease-dead; catalysis is `contributes_to` crossover-junction endodeoxyribonuclease activity of the SLX1-SLX4 complex, not `enables` on SLX4 | **AIGR right** on the GO layer; **no true narrative conflict** — Affinage prose agrees SLX4 activates partners rather than cutting. |
| `protein binding` (GO:0005515) | Leans on many PPIs (SLX1, XPF, MUS81, TRF2, MSH2, RTEL1, FANCD2, PLK1) | 9 IPI `protein binding` rows MARK_AS_OVER_ANNOTATED; content captured by adaptor/activator MF + core_functions | **AIGR right** per curation policy; Affinage does not assert the generic term, so no real conflict. |
| SUMO E3 ligase activity | Distinct function: SLX4 complex SUMOylates SLX4 and XPF (PMID:25533188) | Previously **not annotated** (review framed SLX4 purely as nuclease scaffold) | **Affinage surfaced a real gap.** Added NEW GO:0061665 (SUMO ligase activity), non-core (SIMs are dispensable for ICL repair). |
| ICL unhooking mechanism | XPF-ERCC1 executes unhooking incisions with SLX4/FANCP; mini-SLX4 stimulates XPF-ERCC1 up to 100-fold (PMID:24726325/24726326) | ICL repair annotated (GO:0036297) but supported only by FA-genetics + binding papers | **Affinage right that stronger mechanistic evidence exists.** Added those two papers as verbatim `supported_by` to the ICL and enzyme-activator functions. |
| DNA replication (GO:0006260) | mechanism_profile implies replication involvement (Reactome Cell Cycle) | MARK_AS_OVER_ANNOTATED (IEA + NAS): SLX4 acts on replication-associated structures, not replication itself | **AIGR right** — broad process parent over-annotates. |
| intra-S checkpoint (GO:0072429, IMP PMID:23361013) | Not directly evidenced; Affinage checkpoint cites are yeast Slx4 (PMID:26490958) and SLX4-XPF/ATR at fork barriers (PMID:33347546) | UNDECIDED (cached PMID:23361013 abstract is about FBH1/MUS81; SLX4-specific support unverifiable) | **AIGR right to hold UNDECIDED** — Affinage adds no SLX4-specific human intra-S checkpoint evidence for this exact term; policy forbids removing an unverifiable experimental IMP. |
| Telomere/ALT & meiotic roles | Rich telomere/ALT narrative (TRF2, t-circles, ALT vs BTR) | KEEP_AS_NON_CORE (telomere set) / meiotic IBA non-core | **AIGR right** — genuine but specialized deployments correctly demoted; not core somatic ICL/HR function. |
| Condensates, MMR suppression, RTEL1, RNF4/USP7 homeostasis | Several specialized functions (PMID:37059091, 35166826, 32398829, 41002028) | Not annotated | **Not incorporated (conservative).** Each is real but single-study/specialized; left out to avoid over-annotation. Flagged here as candidate future non-core additions. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:24726325 | ICL repair unhooking (GO:0036297) | Verbatim `supported_by` on the NEW GO:0036297 annotation and on core_function 1 (adaptor); reference + `reference_review` (HIGH/VERIFIED). Xenopus reconstitution: XPF-ERCC1 cooperates with SLX4/FANCP to carry out unhooking incisions. |
| PMID:24726326 | Enzyme activator activity (GO:0008047) | Verbatim `supported_by` on the GO:0008047 IDA annotation and on core_function 2 (activator); reference + `reference_review` (HIGH/VERIFIED). Quantifies mini-SLX4 stimulation of XPF-ERCC1 up to 100-fold. |
| PMID:25533188 | SUMO ligase activity (GO:0061665) | `original_reference_id` + verbatim `supported_by` for a NEW non-core GO:0061665 annotation; reference + `reference_review` (HIGH/VERIFIED). SLX4 complex SUMOylates SLX4 and XPF. |

All three PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a whitespace-normalized
verbatim substring of the cached full text/abstract. GO terms verified against QuickGO
(GO:0061665 SUMO ligase activity — current MF; GO:0036297 and GO:0008047 already in the review).

## Net assessment

AIGR and Affinage agree closely on SLX4's core biology — a nuclease-dead scaffold that assembles and
activates the SLX1 / XPF-ERCC1 / MUS81-EME1 toolkit for ICL repair and HR — and, importantly,
Affinage's narrative does **not** mis-attribute nuclease catalysis to SLX4 (only its coarse,
self-flagged `mechanism_profile` GO layer does, and that was correctly not imported). Affinage's value
was (i) surfacing one genuine molecular function the GOA-grounded review had entirely omitted — the
SLX4-complex **SUMO E3 ligase activity** (added as a validated non-core NEW annotation) — and (ii)
supplying stronger mechanistic primary evidence for the already-annotated ICL-unhooking and
enzyme-activator functions (two papers added as verbatim `supported_by`). All prior AIGR decisions
(telomere/meiotic non-core demotions, DNA-replication over-annotation, the UNDECIDED intra-S
checkpoint IMP, protein-binding over-annotation) were left intact; nothing was weakened over
Affinage's coarse GO. File remains ✓ Valid (single benign deep-research-file warning).
