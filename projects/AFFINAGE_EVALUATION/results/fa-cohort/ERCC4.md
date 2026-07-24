# ERCC4 (FANCQ / XPF) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 40 discoveries · 41 citations · self-eval pairwise = **tie** (CAUTION) · gates **not** passed (`gates_passed: False`).

## Agreement (brief)

Affinage and the AIGR review converge tightly on ERCC4/XPF's core biology: it is the
**catalytic subunit of the ERCC1-XPF structure-specific endonuclease**, an obligate
heterodimer that makes the **5' incision** at single-strand/double-strand DNA junctions.
Both place this activity at the center of **nucleotide excision repair** (recruited via
XPA), **interstrand-crosslink unhooking** (coordinated by SLX4/FANCP downstream of FANCD2
ubiquitylation), **single-strand annealing / homology-directed repair** (3'-flap trimming,
RAD52-stimulated), and **telomere overhang processing**. Both correctly identify the
nuclease active site in the XPF N-terminal region, ERCC1 as the catalytically inert
partner bound through the C-terminal (HhH)₂ domain, and the same disease spectrum
(XP-F, XFE progeroid, XPF-CS, Fanconi anemia FA-Q) as reflecting one endonuclease
deficiency with separable NER vs ICL activities. They cite overlapping primary sources
(PMID:22547097, 22483113, 16076955, 14734547, 18812185, 32034146). This is a case where
the narratives substantially agree — the differences are about GO grounding depth and
which specialized roles rise to annotation.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding depth | Coarse `mechanism_profile`: catalytic activity acting on DNA / hydrolase / DNA binding / RNA binding; localization = nucleus + nuclear chromosome; Reactome = DNA Repair, Chromatin organization, Disease | Granular, correctly-branched: GO:0000014 ssDNA endodeoxyribonuclease activity (core MF, NEW), GO:1990599 3'-overhang ssDNA endonuclease, GO:0070522 ERCC4-ERCC1 complex, GO:0000110 NEF1 complex, GO:1901255 NER-in-ICL-repair | **AIGR.** Affinage's own file concedes the profile "collapses to general parents and can contradict the narrative." AIGR re-grounds from the narrative + PMIDs to specific, correctly-branched terms. |
| "RNA binding" (GO:0003723) | Lists **RNA binding** as a molecular_activity in its mechanism_profile | Not annotated as an MF; the RNA:DNA-hybrid/R-loop contact is via the XAB2 complex, not intrinsic XPF RNA binding | **AIGR.** Intrinsic XPF RNA-binding is not established; the R-loop association (PMID:34039990, 36184605) is complex-mediated and context-specific. Importing GO:0003723 would be a wrong-branch over-reach. Affinage flags its own profile as unreliable here. |
| Non-repair transcriptional / chromatin-looping role | Headlines CTCF/cohesin chromatin looping and imprinted-gene silencing (PMID:22771116, 28368372) as a distinct catalytic-activity-requiring function | Not annotated | **AIGR (conservative).** Genuine primary findings, but a specialized, still-consolidating role downstream of the same endonuclease activity; not a distinct core GO function for human XPF. Correctly excluded (valuable context, not a new term). |
| ALT telomere / TERRA R-loops, LINE-1 retrotransposition, Top1-nick, replication-fork cleavage | ~8 discoveries promoted as functions (PMID:36184605, 18396111, 26025908, 30059501, 34039990, 29497062) | Not annotated | **AIGR (conservative).** These are cell-context / disease-model phenotypes downstream of the annotated structure-specific endonuclease activity, not distinct molecular/cellular GO functions. Correctly kept out of the annotation set. |
| Cytoplasmic mislocalization / nuclear import interdependence | Emphasizes XPF stability requires ERCC1 (PMID:20418188), ERCC1 nuclear import requires XPF (PMID:28130555), USP45 deubiquitylation (PMID:25538220) | Not annotated as separate functions; localization captured by nucleus/chromosome/complex terms | **AIGR (defensible).** These are regulatory/stability mechanisms of the heterodimer, already implied by the complex-membership and localization annotations; not additional GO functions. |
| FA-Q disease grounding | Cites PMID:23623386 for biallelic ERCC4 → Fanconi anemia with separable NER/ICL activities | Description named FANCQ but **cited nothing** for it | **Affinage surfaces a real gap.** PMID:23623386 now incorporated (below) onto the ICL-repair annotation. |

## Was the CAUTION warranted?

**Partly — as a prompt for scrutiny, not as a verdict on accuracy.** The `tie` self-eval and
tripped gate correctly flagged that this record should not be trusted wholesale, and two
concrete weaknesses bear it out: (1) the `mechanism_profile` is coarse and internally
inconsistent with the narrative (it lists **RNA binding** and only parent-level catalytic
terms — exactly the wrong-branch/over-general grounding not to import); and (2) the
narrative's breadth is skewed toward **specialized and context-specific roles** (CTCF
looping, ALT/TERRA, LINE-1, fork cleavage, imprinting) that read as headline functions but
are downstream applications of one endonuclease activity — an over-reach profile the
curated review deliberately keeps as non-core or excludes.

That said, the **factual narrative is strong and PMID-dense**: no fabricated or contradicted
claims were found on spot-check, and the core mechanistic account (5' incision, ss/ds
junction specificity, ICL unhooking, SLX4/FANCD2 order, auto-inhibition) is accurate and
well-cited. So the `tie` reflects **coarse GO grounding + breadth-over-focus**, not factual
unreliability. The CAUTION was a reasonable trigger for skeptical reading; the underlying
literature synthesis held up.

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:23623386 | Biallelic ERCC4 mutations cause Fanconi anemia (FA-Q); FA-causing mutations selectively disrupt ICL repair while sparing NER — human genetic evidence for a dedicated ICL-repair function | Fetched/cached (abstract-only). Added to `references` (HIGH, VERIFIED) and attached as a verbatim `supported_by` on GO:1901255 (NER-in-ICL-repair, IBA), which previously rested only on PMID:32034146. The review's `description` named FANCQ but cited nothing for it; this closes that gap. Reason text updated to note the FA-Q genetic evidence. No action changed. |

**1 paper incorporated; 0 NEW annotations added.** The AIGR review was already exceptionally
complete (COMPLETE status, ~90 existing annotations reviewed, core_functions grounded to
GO:0000014 / GO:1990599). Affinage's remaining ~39 discoveries were either already covered
by existing annotations (NER, ICL, SSA, telomere, complex) or were specialized/context-specific
roles the review conservatively and correctly excludes. Validation remains `✓ Valid` (single
benign deep-research-file warning).

## Net assessment

On this gene the two systems largely **agree on the facts**, and the AIGR review is the more
disciplined product: correctly-branched specific GO terms, appropriate ACCEPT / KEEP_AS_NON_CORE /
MARK_AS_OVER_ANNOTATED decisions, and deliberate exclusion of the specialized/therapeutic
phenotypes Affinage foregrounds. Affinage's value here was **breadth of primary citation** — it
surfaced exactly one real gap (the FANCQ disease-defining paper, PMID:23623386), now incorporated.
Its coarse `mechanism_profile` (parent-level catalytic terms + spurious RNA binding) should not be
imported, consistent with the CAUTION. Net: AIGR ahead on grounding and focus; Affinage a useful
citation net that justified one conservative, validated addition.
