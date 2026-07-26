# BRCA1 (FANCS) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 22 discoveries · self-eval pairwise = **tie** (CAUTION) · faith 100% · gates **not** passed (tie gate tripped).

The Affinage record for BRCA1 is a strong, PMID-dense (22 citations) mechanistic narrative that
correctly centers BRCA1 on error-free homologous recombination as a RING/BARD1 E3-ligase tumor
suppressor, and then fans out into genotoxic-stress signaling, checkpoint, chromatin, centromere/R-loop,
X-inactivation, and transcriptional roles. The AIGR review is curated, GOA-grounded, validated, spans
275 existing annotations, and was already the product of a full manual A→Z pass plus a 2026-07-22 QA
re-review. Because this review was flagged as already high-quality, edits here were deliberately minimal.

## Agreement (brief)

The two sources agree on essentially all core biology. Both make the BRCA1-BARD1 RING heterodimer the
functional E3 ubiquitin ligase (AIGR: GO:0004842 / GO:0061630 ACCEPT across IBA/IEA/IDA/TAS,
GO:0031436 BRCA1-BARD1 complex, GO:0085020 K6-linked ubiquitination, GO:0140863/0140864 H2A K127/K129
ligase, GO:0061649 ubiquitin-modified histone reader; Affinage narrative + PMID:12890688/34321665).
Both make HR the defining function — end resection (counteracting 53BP1) plus PALB2-mediated RAD51
loading (AIGR GO:0000724 ACCEPT across IBA/IEA/IDA, GO:0006282, GO:0110025; Affinage
PMID:30704900/32359443). Both treat the BRCA1-A/B/C and BARD1 complexes, nuclear/nucleoplasm/chromatin
localization, G2/M and G2 checkpoint signaling, IR response, and centrosome regulation as established,
and both demote transcriptional coactivation, X-inactivation, metabolic/ERα, and centrosome/meiotic
roles below the DNA-repair core. Notably, Affinage's narrative even reproduces the careful negative
result that BRCA1/BARD1 ligase activity is *not* essential in vivo for FANCD2 monoubiquitination
(PMID:12887909) — a point in favor of the record's factual discipline.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | `molecular_activity` = `GO:0016874 ligase activity`, `GO:0140096 catalytic activity acting on a protein`, `GO:0140110 transcription regulator activity`, `GO:0003677 DNA binding`, `GO:0140098 catalytic activity acting on RNA` | Precise MF: `GO:0004842`/`GO:0061630` ubiquitin transferase/ligase, `GO:0140863/4` H2A-site ligase, `GO:0061649` reader, `GO:0003684` damaged DNA binding, `GO:0002039` p53 binding | **AIGR right.** Affinage's own header flags this layer as coarse/collapsed-to-parents. `GO:0140098 catalytic activity, acting on RNA` is wrong-branch — BRCA1 binds XIST RNA but has no RNA-acting catalytic activity; `GO:0016874 ligase activity` is the wrong ligase branch (BRCA1's activity is ubiquitin-protein transferase, not an ATP-dependent C–N/C–O ligase); `GO:0003677 DNA binding` is the less-informative parent of the annotated `damaged DNA binding`. Not imported. |
| ~70 `protein binding` (GO:0005515) IPI rows | Narrative leans on dozens of PPIs (BARD1, RAP80/Abraxas/MERIT40, BAP1, PALB2, CtIP, BACH1/BRIP1, topo IIα, MDC1, FANCA…) | ~70 generic IPI `protein binding` rows REMOVE'd as uninformative; each interaction retained via specific complex/MF/BP terms | **AIGR policy-correct; no true conflict.** Affinage never asserts the generic GO:0005515 term. Its cited interactors map to functions AIGR already captures elsewhere (GO:0070531 BRCA1-A, GO:0031436 BARD1, GO:0031625 E2 binding, GO:0019899 topo II). Affinage's evidence therefore does **not** provide grounds to reverse the aggressive blanket-REMOVE — noted, not reversed. |
| Centromere R-loop resolution / CENP-A maintenance | Distinct function (PMID:34599155): BRCA1 counteracts α-satellite R-loops, preserving CENP-A loading | Not annotated | **Affinage surfaces a real, recent function AIGR lacks — left unannotated conservatively.** Single 2021 primary paper, specialized; adding a NEW GO term (e.g. R-loop / centromere maintenance) would over-reach on an already-QA'd high-quality review. Flagged for a possible future non-core BP, not added. |
| ATR-Ser1423 phosphorylation, CRM1/p53 nuclear export | Emphasized as BRCA1 biology (PMID:11114888, 15087457) | Not annotated as BRCA1 function | **AIGR right to exclude.** These describe regulation *of* BRCA1 (BRCA1 as substrate / its localization control), not molecular functions/processes executed by BRCA1. Out of scope. |
| Transcriptional targets (SIRT1, ERα, VDAC3/GPX4 ferroptosis, BRCA1/E2F1/Rb autorepression) | Presented alongside core roles (PMID:18851829, 19887647, 38552003, 20068145) | Transcriptional/metabolic roles already KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED | **AIGR right.** These are peripheral/tissue-specific or indirect (the ferroptosis and atherosclerosis links are downstream); AIGR's non-core/over-annotated treatment is the correct altitude. No change. |

## Was the CAUTION warranted?

**Mildly warranted, but the narrative held up well.** The `pairwise = tie` self-eval almost certainly
reflects that BRCA1's curated UniProt reference is itself exhaustive (BRCA1 is among the most-studied
human genes), so Affinage could not clearly "win" — not that the narrative is weak. Scrutinizing the
record with extra skepticism as instructed, I found **no fabricated claims and no PMID mis-attribution**
in the narrative; the dated-findings table is accurate and even nuanced (the FANCD2 in-vitro-vs-in-vivo
caveat). The genuine weaknesses the caution correctly points at are (1) the coarse `mechanism_profile`
GO layer, which contains at least one clearly wrong-branch term (`GO:0140098` catalytic activity acting
on RNA) and a coarse/mis-branched ligase parent (`GO:0016874`) — exactly the "do not import these GO
ids" failure mode; and (2) the flat presentation of peripheral/indirect roles (ferroptosis,
atherosclerosis, ERα) next to core HR/E3-ligase biology without a core/non-core hierarchy. Both are GO-
grounding/altitude issues, not factual ones. Net: the caution is a reasonable flag to distrust the GO
layer, but the narrative's prose was sound and actually contributed three canonical primary papers the
GOA-grounded review had under-cited.

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:32359443 | HR (GO:0000724) | Nacson et al. 2020 Mol Cell (Brca1CC and Brca1Δ11 separation-of-function alleles). Added verbatim `supported_by` ("BRCA1 counteracts 53BP1-RIF1-Shieldin activity, thereby activating DNA end resection.") to the GO:0000724 IBA annotation, whose only prior support was the 1999 mouse-ES paper; reference + `reference_review` (HIGH/VERIFIED). |
| PMID:30704900 | Regulation of DNA repair (GO:0006282) | Zong et al. 2019 Mol Cell. Added verbatim `supported_by` ("the RNF168-mediated chromatin ubiquitylation pathway acts redundantly with BRCA1 to promote PALB2- and RAD51-dependent HR") to the GO:0006282 annotation (previously falcon-file + an indirect RAP80-DUB quote); reference_review HIGH/VERIFIED. |
| PMID:34321665 | H2AK127 ubiquitin ligase activity (GO:0140863) | Hu et al. 2021 Nature cryo-EM of BRCA1-BARD1 on the nucleosome. Added verbatim `supported_by` ("catalyse ubiquitin conjugation to H2AX at one site (K127) coincidental in H2A") to the GO:0140863 annotation, complementing the existing PMID:35351360 title-only support; reference_review HIGH/VERIFIED. |

All three PMIDs were fetched/cached via `fetch-pmid` (full text from PMC); every `supporting_text` is a
verbatim substring of the cached text. Each addition strengthens an already-present, correctly-branched
annotation — **no new GO terms were minted and no existing curation decision (action/summary/reason) was
changed.** Zero NEW annotations were added: the review already comprehensively covered HR, checkpoint,
E3-ligase, complexes and localization, and the only functions Affinage surfaced beyond it (centromere
R-loop resolution, ATR/CRM1 regulation, transcriptional targets, ferroptosis) are either specialized
single-paper findings, regulation of BRCA1 rather than by BRCA1, or peripheral/indirect — all below a
conservative bar for a high-quality already-QA'd review.

## Net assessment

AIGR and Affinage agree on BRCA1's core RING/BARD1 E3-ligase and homologous-recombination biology, and
Affinage's narrative was factually clean under extra scrutiny. Its coarse `mechanism_profile` GO layer
is, as the CAUTION implies, the untrustworthy part — one wrong-branch RNA-catalytic term and a mis-
branched ligase parent that were correctly not imported. Affinage's real value was its dense, well-
anchored narrative supplying three canonical primary papers — Nacson 2020 (separation-of-function HR
alleles), Zong 2019 (RNF168-redundant PALB2 loading), and Hu 2021 (cryo-EM H2A-K127 ubiquitylation
opposing 53BP1) — that the review had under-cited. These were incorporated conservatively as added
references + verbatim `supported_by` on existing annotations, with no change to any curation decision,
no reversal of the aggressive protein-binding REMOVEs, and no new terms. The **CAUTION was warranted as
a flag against the GO layer but not against the prose.** File remains ✓ Valid.
