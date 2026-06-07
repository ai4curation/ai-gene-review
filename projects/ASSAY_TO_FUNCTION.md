# ASSAY_TO_FUNCTION

**Which experimental readouts reliably support gene-function annotation, and which drive over-annotation?**

## Motivation

Functional genomics papers infer gene function through a chain:

> perturb gene **G** → readout **R** moves → conclude **G** is "involved in" process **P**

The reliability of that final `R → P` step varies enormously, but GO evidence
codes (IDA, IMP, IGI, …) do not capture it. An IMP read out with a 5×UPRE
reporter and an IMP read out with a reconstituted enzyme assay carry the same
evidence code, yet one is a distal, convergent phenotype and the other is a
direct measurement of molecular activity. This project tries to make that
hidden axis explicit and to measure, against the curated corpus, which readout
classes are associated with annotations that curators later downgrade.

## Conceptual framework

Two independent axes govern `R → P` reliability:

1. **Proximity** — does the readout measure the gene product's *own molecular
   activity* (`molecular`) or a *downstream cellular consequence* (`phenotypic`)?
2. **Convergence** — is the readout a fairly specific signature of process P
   (`low`), or a **hub** that many upstream inputs feed into (`high`)?

Over-annotation risk is highest in the **phenotypic + high-convergence**
quadrant. Classic convergent hubs: ROS, caspase activation, the UPR,
intracellular Ca²⁺, pH, mitochondrial membrane potential. A gene that moves one
of these reporters could be a direct effector *or* anything that perturbs the
process indirectly — so a positive readout licenses, at best, a cautious
`response to` / `regulation of` **BP** term (often non-core), and should never
by itself drive an **MF** or core-function call.

### Example readouts (the seed cases that motivated this)

| Readout | Reports state of | Why it over-annotates |
|---|---|---|
| 5×UPRE | UPR / ER stress | fires for *any* ER perturbation — secretory load, trafficking, metabolic stress |
| CellROX / DCFDA / MitoSOX | oxidative stress | ROS rises under nearly every stress; massively convergent |
| CellEvent / caspase-3/7 | apoptosis | caspase activation is far downstream; many insults trigger it |
| pHrodo / pHluorin | pH / phagocytosis | |
| FeRhoNox | labile Fe²⁺ | |

The full, editable catalog lives in
[`ASSAY_TO_FUNCTION/readout_catalog.yaml`](ASSAY_TO_FUNCTION/readout_catalog.yaml).

## Method (first pass — mining the curated reviews)

`ASSAY_TO_FUNCTION/mine_readouts.py` walks all `genes/**/*-ai-review.yaml`
files. For each annotation it builds an *evidence text* from the curator's
`review.summary`, `review.reason`, and `supported_by[].supporting_text`, then
matches it against the regex patterns in the catalog. Each match becomes a row
joining the readout class to the reviewer's `action`.

Reliability is summarised two ways, over **reviewed annotations only**
(UNREVIEWED / UNDECIDED / PENDING excluded from the denominator):

- `pct_removed_or_overann` — *hard* signal: REMOVE + MARK_AS_OVER_ANNOTATED
- `pct_any_downgrade` — *soft* signal: also includes KEEP_AS_NON_CORE + MODIFY

```bash
uv run python projects/ASSAY_TO_FUNCTION/mine_readouts.py
```

Outputs land in `ASSAY_TO_FUNCTION/reports/`:
`readout_matches.tsv` (one row per match), `readout_action_crosstab.tsv`
(the table below), and `matched_string_counts.tsv` (QC).

## First-pass results

Scanned **1,971 review files / 75,931 annotations**; 1,736 readout matches.

| readout_class | prox | conv | reviewed | rm/OA% | anyDn% |
|---|---|---|--:|--:|--:|
| UPR_ER_STRESS | phenotypic | high | 29 | 0% | 24% |
| APOPTOSIS_CASPASE | phenotypic | high | 41 | 7% | **49%** |
| AUTOPHAGY_FLUX | phenotypic | high | 52 | 6% | 17% |
| MITO_MEMBRANE_POTENTIAL | phenotypic | high | 24 | 8% | **42%** |
| CALCIUM_FLUX | phenotypic | high | 7 | 29% | 57% |
| IRON_PROBE | phenotypic | high | 6 | 0% | 33% |
| TRANSCRIPTIONAL_REPORTER | phenotypic | high | 60 | 3% | 22% |
| VIABILITY_PROLIFERATION | phenotypic | high | 7 | 0% | 43% |
| IN_VITRO_ENZYME | molecular | low | 500 | 9% | 24% |
| DIRECT_BINDING | molecular | low | 988 | 6% | 18% |

### Interpretation (preliminary — under-powered)

- **Directional support, not proof.** The two phenotypic-hub classes with
  non-trivial N — apoptosis/caspase (49% any-downgrade) and mitochondrial
  membrane potential (42%) — sit well above the molecular controls
  (in-vitro enzyme 24%, direct binding 18%). But UPR, autophagy, and
  transcriptional reporters are no higher than the molecular baseline, and
  several classes have N < 10. No strong claim is warranted yet.
- **The review prose is the wrong corpus for assay names.** Curators write
  *synthesis* ("phosphorylates ACC", "crystal structure shows…"), not methods.
  Probe brand names are almost absent: CellROX/DCFDA/MitoSOX matched **zero**
  review texts. The molecular classes dominate by volume only because "crystal
  structure", "cryo-EM", and "in vitro" are phrases curators naturally use.
- Implication: to actually measure how assays are interpreted, we must mine the
  **publications** (methods sections), not the review summaries — see next steps.

### Methodology lessons (substring bugs caught in QC)

Keyword mining is treacherous; the QC dump caught three false-positive sources
that would have completely inverted the headline numbers:

- `HyPer` (H₂O₂ biosensor) matched "**hyper**-activation", "**hyper**-expressed"
  → inflated oxidative stress by ~365. Fixed with case-sensitive `(?-i:HyPer)`.
- `ERSE` (ER stress element) matched "div**erse**", "rev**erse**", "adv**erse**"
  → inflated UPR from ~29 to 609. Fixed with a left word boundary.
- `MTS` (viability dye) matched "**MTs**" (microtubules) and the
  mitochondrial-targeting-sequence abbreviation → fixed by requiring
  "MTS assay/reagent/reduction".

**Always inspect `matched_string_counts.tsv` before trusting a class total.**

## Second pass — mining the publications corpus

`ASSAY_TO_FUNCTION/mine_papers.py` does what the first pass showed was needed:
the unit of analysis is now *(annotation, readout-class-used-in-the-source-paper)*.
For each PMID-backed annotation it resolves the cached `publications/PMID_*.md`,
detects which readout classes that paper uses, attaches the GO **aspect**
(MF/BP/CC, from the GOA TSVs), and flags **thematic alignment** — whether the
annotation's GO term is actually *about* the process the readout reports
(GO id in `commonly_overmapped_to`, or label matches `aligned_label_regex`).

```bash
uv run python projects/ASSAY_TO_FUNCTION/mine_papers.py
```

Coverage: **75,931 annotations; 36,660 PMID-backed; 36,449 papers resolved**
(129 PMIDs not cached). 16,682 paper-level readout matches; **722 thematically
aligned** (the high-precision subset where the readout plausibly *drove* the
annotation).

Performance note: detection is a two-stage filter — a cheap literal substring
*screen* (`SCREEN` in the script, a necessary superset per class) gates the
expensive `IGNORECASE` regex, which runs only on the rare screen hits. Screens
were validated to lose zero matches vs. regex-only on a 350-paper sample
(including the 50 largest). Detection is memoized per unique PMID.

### Headline result: the aspect constraint holds

For **thematically aligned** annotations, what GO aspect does each hub readout
license?

| readout_class | aspect distribution (aligned) |
|---|---|
| APOPTOSIS_CASPASE | **BP 68, MF 0** |
| OXIDATIVE_STRESS_ROS | **BP 10, MF 0** |
| VIABILITY_PROLIFERATION | **BP 87**, CC 3 |
| AUTOPHAGY_FLUX | **BP 109**, CC 15 |
| UPR_ER_STRESS | **BP 17**, MF 2 |
| CALCIUM_FLUX | **BP 20**, MF 2 |
| MITO_MEMBRANE_POTENTIAL | **CC 139**, BP 26 |
| TRANSCRIPTIONAL_REPORTER | BP 143, **MF 71**, CC 1 |

This directly supports the core hypothesis: phenotypic-hub readouts almost
never license **MF** annotations. Caspase, ROS, autophagy, viability, and UPR
readouts produce BP terms (ΔΨm probes produce mostly CC = mitochondrion
localization). **The one exception is transcriptional reporters (MF 71)** — but
inspecting those rows, they are bona fide TF-activity terms (`DNA-binding
transcription factor activity`, `transcription cis-regulatory region binding`)
on genuine transcription factors, mostly `ACCEPT`ed. A luciferase reporter
legitimately supports MF *for a TF*; it is not over-annotation there.

### The real over-annotation mode: correct-but-non-core, not wrong

Action breakdown for aligned annotations (the strong-link subset):

| readout_class | reviewed | ACCEPT | NON_CORE | rm/OA% | anyDn% |
|---|--:|--:|--:|--:|--:|
| VIABILITY_PROLIFERATION | 90 | 21 | **58** | 9% | **74%** |
| APOPTOSIS_CASPASE | 63 | 25 | **34** | 3% | 59% |
| OXIDATIVE_STRESS_ROS | 10 | 3 | 4 | 30% | 70% |
| CALCIUM_FLUX | 22 | 10 | 7 | 18% | 50% |
| MITO_MEMBRANE_POTENTIAL | 165 | 98 | 20 | **21%** | 38% |
| UPR_ER_STRESS | 19 | 9 | 5 | 11% | 37% |
| TRANSCRIPTIONAL_REPORTER | 207 | 146 | 36 | 7% | 28% |
| AUTOPHAGY_FLUX | 124 | 80 | 20 | 5% | 24% |

The key correction to the first-pass intuition: hub readouts are **not removed
more often** than molecular evidence (hard `rm/OA%` is comparable — molecular
controls run ~27% in the weak-link view). Instead their characteristic failure
mode is **demotion to non-core**: viability/proliferation (58/90 → NON_CORE)
and apoptosis (34/63) annotations are rarely *wrong*, but are overwhelmingly
judged peripheral. That is the precise, defensible sense in which these
readouts "over-annotate": they inflate the annotation set with correct-but-
peripheral process terms rather than producing outright errors.

Mitochondrial-membrane-potential readouts are the exception with a genuinely
elevated *hard* downgrade rate (21%), often via `MODIFY` (31/165) — ΔΨm is a
non-specific organelle-health readout that gets refined to more proximal terms.

### Caveats

- **Weak link.** A paper using assay R does not prove the *specific* annotation
  was based on R. Thematic alignment mitigates this (722 high-precision rows)
  but cannot fully establish causation.
- The `any-downgrade` rate is high (40-60%) for *every* class including
  molecular controls, because it is dominated by `KEEP_AS_NON_CORE`/`MODIFY`,
  which are refinements, not errors. The hard `rm/OA%` and the aspect/non-core
  breakdowns are the discriminating signals, not the raw downgrade rate.

## The rubric (deliverable)

The grounded, curator-facing rubric is in [`ASSAY_TO_FUNCTION/RUBRIC.md`](ASSAY_TO_FUNCTION/RUBRIC.md)
(narrative + decision procedure + worked corpus contrasts) with a
machine-readable companion in [`ASSAY_TO_FUNCTION/rubric.yaml`](ASSAY_TO_FUNCTION/rubric.yaml).

Core rule: a convergent phenotypic readout licenses **at most** a BP (or CC)
"response to / regulation of P" term, **never MF**, defaulting to **non-core** —
promote to core only when independent evidence places the gene in P's recognized
machinery. The single MF exception is a transcriptional reporter for a bona fide
DNA-binding TF.

## The flagger (operationalized rubric)

[`ASSAY_TO_FUNCTION/flag_candidates.py`](ASSAY_TO_FUNCTION/flag_candidates.py)
applies the rubric to the mined matches and emits a prioritized re-review
worklist (`reports/flagged_candidates.tsv`). It flags only annotations that are
still *standing* (not already downgraded) and *thematically aligned* to a hub
readout, so precision stays high. Two tiers:

- **Tier 1 — MF from a hub readout** (a state readout cannot license molecular
  function). The legitimate transcriptional-reporter→TF-activity case is
  excluded.
- **Tier 2 — a core (`ACCEPT`) hub-aligned BP/CC call**, where the rubric
  default is non-core; verify the gene is in the recognized machinery.

```bash
uv run python projects/ASSAY_TO_FUNCTION/flag_candidates.py
```

Current run: **296 candidates (5 Tier 1, 291 Tier 2)** (post Tier-1 binding-MF calibration — see [Tier-1 re-review outcome](#tier-1-re-review-outcome-loop-closed) below for the 7→5 reduction). The Tier-1 set is
precisely the reporter-driven over-annotation pattern the rubric predicts —
`transcription coactivator/corepressor activity` claimed from luciferase
reporters for coregulators that are **not** sequence-specific TFs (CTNNB1/
β-catenin, NOTCH1, SIRT1, HMGB1), plus Ca²⁺-binding MF terms (Calm2, HRC) that
should rest on EF-hand/structural evidence rather than Ca²⁺ imaging. Tier 2 is a
larger triage queue dominated by `MITO_MEMBRANE_POTENTIAL` (85, mostly generic
`mitochondrion`), `TRANSCRIPTIONAL_REPORTER` (72), and `AUTOPHAGY_FLUX` (70).

These are re-review *candidates*, not asserted errors.

### Tier-1 re-review outcome (loop closed)

All 7 original Tier-1 candidates were re-reviewed against their actual evidence
(see [`ASSAY_TO_FUNCTION/REREVIEW_TIER1.md`](ASSAY_TO_FUNCTION/REREVIEW_TIER1.md)).
Outcome: **none is a clean readout-driven over-annotation** — six KEEP, one
(SIRT1 corepressor activity) a soft non-core suggestion. Three calibration
findings fed back:

1. **Binding MF is a direct activity, not a readout consequence** — Calm2/HRC
   ("calcium … binding") were false positives. The flagger now excludes
   `*binding` MF from Tier 1 (7 → 5), and the rubric's "never MF" rule is scoped
   to *regulatory/process-like* MF, not binding/catalytic MF.
2. **Coregulator MF is legitimate for genuine coregulators** (β-catenin, NICD);
   the discriminator vs. the corpus's true over-annotation (`AIP → coactivator`)
   is machinery membership, not aspect.
3. **The standing-only filter works**: the real over-annotation (AIP) was
   already `MARK_AS_OVER_ANNOTATED`, so was correctly not re-flagged. The
   flagger's marginal value is therefore highest on *unreviewed* annotations and
   the Tier-2 queue, not on re-litigating accepted MF calls.

### Tier-2 triage + the machinery discriminator

The Tier-2 queue (core `ACCEPT` on a hub-aligned BP/CC term) is large and, on
its own, low precision: re-reviewing the top `VIABILITY_PROLIFERATION` class
showed the queue mixes genuine machinery (CDK1, MYC, RB1, TP53 — correctly core)
with indirect cases (IL21, PDGFB, VEGFA). See
[`ASSAY_TO_FUNCTION/REREVIEW_TIER2.md`](ASSAY_TO_FUNCTION/REREVIEW_TIER2.md).

The flagger now (a) ranks Tier 2 by each readout class's empirical any-downgrade
rate, and (b) adds a **machinery discriminator**: a candidate is tagged
`indirect_ligand` when the gene's own MF is a *secreted signaling ligand*
(cytokine/growth factor/hormone/chemokine), because then any cellular process it
drives is downstream of receptor signaling — the strongest computable non-core
signal. This cleanly isolates 6 high-precision non-core candidates (IL21, PDGFB,
VEGFA×2, HMGB1×2) at the top of the queue while the cell-cycle machinery sinks.

```bash
uv run python projects/ASSAY_TO_FUNCTION/flag_candidates.py --target accepted
```

## Annotation edits made (curation output)

The analysis was carried through to actual YAML edits — see
[`ASSAY_TO_FUNCTION/EDITS.md`](ASSAY_TO_FUNCTION/EDITS.md) for the full table
with gene descriptions and rationale. Summary: **4 genes / 6 annotation records
downgraded `ACCEPT` → `KEEP_AS_NON_CORE`** where a process is genuinely
downstream of the gene's core MF:

- **PDGFB** — glomerular mesangial cell proliferation (GO:0072126) — downstream of PDGFR signaling
- **HMGB1** — cytosolic calcium (GO:0007204) — downstream CXCR4 signaling
- **Sirt2** — positive regulation of cell division (GO:0051781) — downstream of deacetylase activity
- **VEGFA** — negative regulation of apoptotic process (GO:0043066) — downstream Akt survival signaling

Deliberately **kept as-is** (flag was a false positive): VEGFA endothelial-cell
proliferation (defining function), SIRT1 corepressor activity, the
binding/coactivator MF terms from the Tier-1 re-review, and PDGFB mesangial
proliferation (a reversal was considered but rejected — knockout necessity is
not mechanistic evidence of direct proliferation regulation). All edited files
re-validate cleanly.

**Deferred to expert review (`UNDECIDED`):** IL21 `positive regulation of T cell
proliferation` (GO:0042102) is genuinely borderline — a real but weak,
context-dependent effect versus IL21's signature B-cell/Tfh axis. Rather than
guess, the two IDA annotations were set to `UNDECIDED` (paper-backed) and the
term removed from `core_functions` pending
[issue #1418](https://github.com/ai4curation/ai-gene-review/issues/1418).
This exposed a needed **rubric refinement**: the "signaling-ligand ⇒ indirect"
discriminator over-fires on *dedicated* cytokines/growth factors, whose
regulated processes can be core. The better axis is **signature vs incidental**
(see `RUBRIC.md`).

## Catalog extension — 12 new readout classes

The catalog was extended beyond the seed hubs to cover more phenotypic assay
families: **cell migration/invasion** (scratch, Transwell, Boyden, Matrigel),
**cell adhesion/spreading**, **membrane trafficking/endocytosis** (transferrin/
FM4-64/dextran uptake), **secretion/degranulation** (LDH release, CD107a,
β-hexosaminidase), **metabolic flux** (Seahorse/OCR/ECAR, 2-NBDG glucose uptake),
**DNA-damage foci** (γH2AX, comet, 53BP1/RAD51 foci), **senescence** (SA-β-gal,
SASP), and pathway-specific transcriptional reporters for **Wnt** (TOPFlash),
**NF-κB**, **hypoxia** (HRE/HIF), **Notch** (RBP-J/CSL), and **Hippo** (TEAD/GTIIC).
Each class got an `aligned_label_regex`, `commonly_overmapped_to` GO IDs, regex
patterns, and a necessary-superset literal `SCREEN` entry.

`mine_papers.py` now also emits **`reports/paper_matched_string_counts.tsv`** — a
corpus-level matched-substring QC (counted once per paper), the publications
analogue of the prose miner's QC and the place substring bugs actually surface.

### QC caught one substring bug
`\bOCR\b` (oxygen consumption rate) matched the *C. elegans* **ocr-2** TRPV-channel
gene (19 false hits). Dropped bare `OCR`; the class now relies on the spelled-out
"oxygen consumption rate" / Seahorse / ECAR. After the fix
`paper_matched_string_counts.tsv` is clean across all 12 new classes.

### The aspect constraint generalizes

Aligned annotations per new class (publications corpus):

| readout_class | aligned N | aspect | non-core demotion |
|---|--:|---|---|
| CELL_MIGRATION_INVASION | 35 | **BP 37, MF 0** | 16/35 NON_CORE |
| DNA_DAMAGE_FOCI | 36 | **BP 32, CC 4, MF 0** | (mostly machinery) |
| WNT_REPORTER | 17 | **BP 15**, MF 1, CC 1 | 8/17 NON_CORE |
| MEMBRANE_TRAFFICKING_ENDOCYTOSIS | 14 | **BP 12, CC 2, MF 0** | 7/14 NON_CORE |
| SENESCENCE | 9 | **BP 9, MF 0** | 6/9 NON_CORE |
| NFKB_REPORTER | 6 | **BP 7, MF 0** | 4/6 NON_CORE |
| CELL_ADHESION_SPREADING | 4 | BP 4 | under-powered |
| METABOLIC_FLUX | 3 | BP 3 | under-powered |
| HYPOXIA_HIF | 2 | BP 2 | under-powered |
| SECRETION_DEGRANULATION | 1 | BP 2 | under-powered |
| NOTCH_REPORTER / HIPPO_TEAD | ~0 | — | under-powered |

Every new class is BP/CC-dominant with ~zero MF (the sole MF, LRRK2 *β-catenin
destruction complex binding*, is a binding MF already non-core), and the
well-powered ones show the predicted elevated non-core demotion. The same
BP-not-MF, default-non-core regime holds.

### Re-review: machinery vs signature, again

The standing-`ACCEPT` candidates in the new classes are, on re-review, almost all
correctly curated — the flagger's precision on accepted calls remains low:

- **Machinery → core (KEEP):** BRCA1/2, CHD1, RAD18 (DNA-damage); CLTC, TFRC
  (endocytosis); CTNNB1, AXIN1, FZD7 (Wnt); TRAF6 (NF-κB); ARNT/HIF-1β (hypoxia);
  TP53 (senescence) — the "core only if in the machinery" discriminator.
- **Signature ligand outputs → core (DECLINE):** the `CELL_MIGRATION_INVASION`
  `indirect_ligand` cluster (CCL11, PDGFA/B, VEGFA, HMGB1) is exactly the
  signature-vs-incidental over-firing the rubric's caveat predicts — chemotaxis
  *is* a chemokine's job; PDGF migration is already in `core_functions`.
- **Genuine non-core/borderline → defer:** **STAT3 → positive regulation of cell
  migration (GO:0030335, ×2 IMP)** — a transcription factor whose migration role
  is a downstream transcriptional consequence, not motility machinery. High-profile
  and contested (oncogenic EMT driver vs downstream), so set `ACCEPT → UNDECIDED`,
  opened [issue #1422](https://github.com/ai4curation/ai-gene-review/issues/1422),
  and staged + submitted a cited OpenScientist hypothesis job (see below) rather
  than unilaterally demoting. See [`ASSAY_TO_FUNCTION/EDITS.md`](ASSAY_TO_FUNCTION/EDITS.md).

### A molecular positive-control class: rubidium (⁸⁶Rb⁺) flux

To probe the *other* end of the proximity axis, a `RUBIDIUM_FLUX` class was added
as **molecular / low-convergence** — the classic ⁸⁶Rb⁺ K⁺-channel/transporter
assay (Rb⁺ as a K⁺ congener). Unlike the Ca²⁺ imaging hub, Rb⁺ flux is a near-direct
measure of the channel's own activity and should *license* an MF channel-activity
term — the mirror image of the phenotypic hubs. QC is clean (the ⁸⁶Rb notation
matched 33 papers with no RB1-gene/rubidium-salt false positives — bare `Rb` is
deliberately excluded from the screen).

**Honest result: under-powered to null (robust).** Of the 33 ⁸⁶Rb papers, only one
is cited by any reviewed annotation (mTOR *transmembrane transporter binding*, not
a K⁺ channel — correctly not aligned), so there are **zero aligned Rb-flux
annotations** — and this holds even under the broader supported_by join below.
The 33 ⁸⁶Rb papers are essentially disconnected from the curated annotation
references. The class is kept as a correctly-implemented control that future
ion-channel-gene coverage would populate; the null re-confirms the first-pass
lesson that MF annotations cite structural/biochemical references rather than
functional-flux assays. Caveat for when it does populate: Rb⁺ flux is direct only
for the pore-forming channel — flux moved by perturbing a regulator/subunit is the
same indirect inference as the hubs.

### Broader join: supported_by references (not just the primary)

`mine_papers.py --include-supporting` joins each annotation to readout usage
across *all* its cited papers (`supported_by` / `additional_reference_ids`), not
only `original_reference_id`, recording a `ref_role` (primary/supporting) per row.
Written to `reports/with_supporting/` so the canonical strong-link analysis stays
intact.

Effect: PMID-backed annotations 37.6k → **47.2k**, paper-readout matches 18.9k →
**28.1k**, thematically aligned **863 → 1,200** (+39%; 337 of the 1,200 from
supporting refs). Crucially the **headline pattern strengthens** — the phenotypic
hubs remain BP/CC-dominant with ~zero MF on the larger sample (apoptosis BP93/MF0,
autophagy BP186/CC30/MF0, DNA-damage BP58/CC7/MF0; TRANSCRIPTIONAL_REPORTER's MF
is the legitimate-TF exception). QC of the broader run is clean. The broader join
did **not** rescue RUBIDIUM_FLUX, making that null robust rather than an artifact
of the primary-only join.

## The proximity axis, demonstrated both ways (molecular vs phenotypic)

The first extension showed phenotypic hubs license BP/CC and ~never MF. A second
batch of 10 classes was added to test the *other* prediction directly — that
**molecular** assays of the gene product's own activity license **MF** — by
including common, well-cited molecular readouts (not just the niche Rb⁺ flux):
electrophysiology, in-vitro kinase assays, GTPase/GAP/GEF assays, in-vitro
ubiquitination/E3-ligase assays, and ChIP/EMSA; plus five more phenotypic hubs
(differentiation, angiogenesis/tube-formation, phagocytosis, cell-cycle/flow,
barrier/TEER).

The aspect of thematically-aligned annotations splits exactly on the axis
(canonical join; QC clean — e.g. ChIP required `ChIP`+suffix so no potato/
microarray "chip" leaked, and the broad `kinase` screen still gated a precise
`kinase assay` regex):

| molecular / MF-licensing | aligned aspect | | phenotypic hub | aligned aspect |
|---|---|---|---|---|
| CHROMATIN_CHIP (ChIP/EMSA) | **MF 136** | | CELL_DIFFERENTIATION | BP 19 |
| KINASE_ACTIVITY_ASSAY | **MF 106**, BP 10, CC 4 | | ANGIOGENESIS_TUBE | BP 22 |
| GTPASE_ACTIVITY | **MF 55**, BP 8 | | CELL_CYCLE_FLOW | BP 16 |
| UBIQUITINATION_ASSAY | **MF 39**, CC 24, BP 1 | | PHAGOCYTOSIS | BP 6 |
| ELECTROPHYSIOLOGY | **MF 18**, BP 9, CC 1 | | BARRIER_PERMEABILITY | CC 5 |

This is the framework's central claim shown as a single within-corpus contrast:
a readout of the gene product's **own activity** (DNA binding, phosphotransfer,
GTP hydrolysis, ubiquitin transfer, ion conduction) licenses an **MF** term,
whereas a **downstream phenotype** (differentiation, a tube, an engulfed
particle, a cell-cycle profile, a resistance drop) licenses **BP/CC and ~never
MF**. Electrophysiology (MF 18) supplies the channel-activity positive control
that the niche RUBIDIUM_FLUX class could not. The split is even sharper under the
broader `--include-supporting` join (ChIP MF 212, kinase MF 153, GTPase MF 93,
ubiquitination MF 51, electrophysiology MF 35).

**Curation:** the new phenotypic-hub flags were all **machinery or signature**
on re-review — VEGFA→angiogenesis (signature), GATA3/SOX9 (master differentiation
TFs), RB1/BRCA1 (cell-cycle machinery) — so **no edits** were warranted (the
"core only if in the machinery / signature output" discriminators at work again).

### Further coverage: proteostasis, lipid, redox, nucleic-acid handling

A fourth batch (8 classes, catalog now **43** readout classes total) extended into
proteostasis, lipid, redox, and nucleic-acid assays and reproduced the axis once
more. Molecular catalytic readouts license **MF** — NUCLEASE_ACTIVITY MF 20,
PROTEASE_ACTIVITY MF 15, LIPID_TRANSFER_FLIPPASE MF 5 (canonical; NUCLEASE MF 42 /
PROTEASE MF 33 with supporting refs). Phenotypic state readouts license **BP** —
PROTEIN_TURNOVER (CHX chase/half-life) BP 29, TRANSLATION_ASSAY BP 13,
LIPID_PEROXIDATION BP 12, REDOX_BALANCE BP 1 (under-powered). PROTEASOME_ACTIVITY
aligns BP/CC (BP 30, CC 12) — its label regex maps to the catabolic-process and
complex terms, i.e. it reads proteostasis *function/location* rather than a bare
endopeptidase MF.

QC clean, with three substring traps deliberately dodged: bare `MDA` (collides
with the MDA-MB cell-line series) → `malondialdehyde`; bare `puromycin` (a
selection antibiotic) → `puromycin incorporation`/SUnSET; cyclic-nucleotide
deferred to avoid `cAMP`→"hippocampus"/"campaign". The 27 new phenotypic-hub
flags are again all **machinery** (PSMA1/PSMB5 proteasome subunits, CUL3 cullin
E3, CDC37/PEX19 chaperones) — correctly core, **no edits**.

### Fifth batch: epigenetic enzymes, immune readouts, second messengers

A fifth batch (9 classes; catalog now **52** readout classes) added epigenetic
writers/erasers, immune assays, and the second-messenger class — done safely —
and reproduced the axis a fifth time. Molecular catalytic readouts → **MF**:
ACETYLTRANSFERASE_DEACETYLASE MF 59, POLYMERASE_ACTIVITY MF 15, PHOSPHATASE MF 8,
METHYLTRANSFERASE MF 7, HELICASE MF 7 (with supporting refs: acetyl MF 76,
polymerase MF 26). Phenotypic state readouts → **BP**: HISTONE_MARK (H3K4me3 etc.)
BP 13, CYCLIC_NUCLEOTIDE_SIGNALING BP 10, CYTOKINE_PRODUCTION BP 7,
CYTOTOXICITY_KILLING BP 3.

The histone-mark vs methyltransferase/acetyltransferase pair is a nice epigenetic
echo of the reporter-vs-ChIP one: the **enzyme assay** (HAT/HDAC/HMT) licenses an
MF, while the **mark state** (H3K4me3, H4K16ac) is a downstream BP chromatin
readout. The cyclic-nucleotide class was added without the `cAMP`→"hippocampus"
substring trap by requiring an explicit assay/level/sensor context.

QC clean. The 11 new phenotypic-hub flags are again machinery or signature —
chromatin enzymes (RTT109 HAT, SET1 methyltransferase, CHD1 remodeler, ASF1
chaperone) and GPCRs whose cyclase-activating signaling *is* their signature
(ADRB2, Drd1) — correctly core, **no edits**.

The proximity axis has now held across **five independent batches** spanning ~30
molecular-vs-phenotypic assay families (43→52 classes).

## Cited-adjudication complement: staged OpenScientist jobs

For borderline / signature-vs-incidental disputes, the project stages
openscientist.io hypothesis jobs as a *cited literature complement* (the pattern
from the IL21 #1418 run). A human-gated generator turns selected
`flagged_candidates.tsv` rows into committed, frontmatter-free `prompt.md` files:

```bash
# stage prompts (writes prompt.md, prints submit commands, NEVER submits)
uv run python projects/ASSAY_TO_FUNCTION/stage_hypotheses.py --discriminator indirect_ligand --max 5
uv run python projects/ASSAY_TO_FUNCTION/stage_hypotheses.py --gene STAT3 --go-id GO:0030335
# or: just assay-stage-hypotheses --gene STAT3 --go-id GO:0030335
```

It reuses `scripts/gene_hypothesis_deep_research.py` so staged prompts are
identical to what that tool submits, specialized to the "core function vs
downstream/context-dependent consequence?" question. A human reviews the staged
prompts and submits only the few worth a paid (~15–30 min) job. The STAT3 job was
run as the worked example; its verdict is posted to #1422 and treated as
hypothesis-generating synthesis to verify against the cited PMIDs — the annotation
stays `UNDECIDED` until an expert decides.

## Next steps

1. **Curator triage** of the ranked `flagged_candidates.tsv`, starting with the
   `indirect_ligand` subset (highest-precision non-core candidates).
2. **Expand the catalog** with more probe vocabularies and the convergent
   *process-term* GO IDs each readout gets over-mapped to.
3. **Generalize the discriminator** beyond signaling ligands (e.g. transporters,
   structural proteins) — currently those indirect cases still need human
   judgement via the ranked queue.

## Relationship to existing projects

- `OVER_ANNOTATION_PATTERNS.md` — pattern #4 ("indirect downstream process
  annotations") is the conceptual cousin; this project quantifies the
  assay-specific version of it.
- `BIOSENSORS.md` — unrelated (plant synthetic-biology biosensors).
