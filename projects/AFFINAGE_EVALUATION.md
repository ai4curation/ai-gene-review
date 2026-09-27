---
title: "Affinage Evaluation Project"
collections: [FUNCTION_PREDICTION]
maturity: MATURE
tags: [PIPELINE, EVALUATION]
species: [human]
sidecars:
  pilot_genes: AFFINAGE_EVALUATION/pilot-genes.txt
  per_gene: AFFINAGE_EVALUATION/results/per-gene.json
  summary_csv: AFFINAGE_EVALUATION/results/summary.csv
  summary_md: AFFINAGE_EVALUATION/results/summary.md
  batch2_genes: AFFINAGE_EVALUATION/batch2-genes.txt
  batch2_per_gene: AFFINAGE_EVALUATION/results/batch2/per-gene.json
  batch2_summary_md: AFFINAGE_EVALUATION/results/batch2/summary.md
  batch3_genes: AFFINAGE_EVALUATION/batch3-genes.txt
  batch3_per_gene: AFFINAGE_EVALUATION/results/batch3/per-gene.json
  batch3_summary_md: AFFINAGE_EVALUATION/results/batch3/summary.md
  batch4_genes: AFFINAGE_EVALUATION/batch4-genes.txt
  batch4_per_gene: AFFINAGE_EVALUATION/results/batch4/per-gene.json
  batch4_summary_md: AFFINAGE_EVALUATION/results/batch4/summary.md
  hard_cases: AFFINAGE_EVALUATION/results/hard-cases.md
  narrative_vs_go: AFFINAGE_EVALUATION/results/narrative-vs-go.md
  fa_cohort_summary: AFFINAGE_EVALUATION/results/fa-cohort.md
  fa_cohort_dir: AFFINAGE_EVALUATION/results/fa-cohort/
  paint_campaign_summary: AFFINAGE_EVALUATION/results/paint-campaign.md
  paint_campaign_per_gene: AFFINAGE_EVALUATION/results/paint-campaign/per-gene.json
  paint_campaign_summary_md: AFFINAGE_EVALUATION/results/paint-campaign/summary.md
  paint_campaign_genes: AFFINAGE_EVALUATION/results/paint-campaign/campaign-genes.txt
  fa_cohort_genes: AFFINAGE_EVALUATION/fa-cohort-genes.txt
  affinage_cache: AFFINAGE_EVALUATION/affinage-cache/
  # Deck images: copied beside the rendered deck so its relative <img> paths resolve.
  slide_images:
    - AFFINAGE_EVALUATION/slides/affinage-pipeline.svg
    - AFFINAGE_EVALUATION/slides/affinage-results.svg
    - AFFINAGE_EVALUATION/slides/go-downcast.svg
manifest:
  slides:
    - href: AFFINAGE_EVALUATION/slides/AFFINAGE_EVALUATION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/5CqTrkg55DQ3bTTeMAFdHm
      title: Project brief
---
# Affinage Evaluation Project

**Bottom line:** Affinage (Cheeseman Lab) writes a literature-grounded mechanism
narrative for every human protein-coding gene and then maps its findings onto GO
and Reactome terms. We compared its output with our agent-adjudicated gene reviews
in four GO-layer cohorts (42 human genes), a forward test on the 22 Fanconi anemia
genes, and a retrieval test on 91 genes from the PAINT campaign. The GO layer
almost never reaches the specific curated function: it captured the primary
molecular function for 1 of 42 genes (KRAS `GTPase activity`), usually stopping at
a generic parent such as `oxidoreductase activity` and sometimes landing on the
wrong catalytic branch. The narrative is much stronger: in the Fanconi cohort it
contributed 59 primary papers and 13 new GO annotations across 10 genes without
reversing any existing curation decision. As a literature search it supplied 52%
of the 718 references the 91 reviews had to find, an upper bound because 56 of
those reviews were written with the Affinage report in hand, and its
`gates_passed` flag checks precision only.

We did this to decide whether Affinage could serve AIGR as a GO-grounding source,
a deep-research input, or a literature search. The answer so far: use the
narrative as a deep-research input, ignore the GO layer, and search partners,
complexes and paralogs independently.

[Function prediction evaluation index](FUNCTION_PREDICTION_EVALUATION.md)


Systematic evaluation of **Affinage** (Cheeseman Lab, Whitehead Institute/MIT;
[affinage.wi.mit.edu](https://affinage.wi.mit.edu), [arXiv:2607.02217](https://arxiv.org/abs/2607.02217))
against the agent-adjudicated local AIGR gene reviews.

See for example, the [Affinage page for SOD1](https://affinage.wi.mit.edu/gene/SOD1). This
has:

- a PMID-grounded chronological mechanistic *narrative*
- open questions (what we call "knowledge gaps" in this repo)
- mechanistic "profile" (summarizes of function and pathway grounded in GO/Reactome)

## GO term evaluation

**Bottom line (42 human genes: pilot n=12 + batches 2–4):** Affinage's GO layer is
a **slim classifier**. Every one of the 43 distinct GO ids it emits across the 42 genes
is a `goslim_generic` term (43/43; the agr, pir and drosophila slims cover 16, 19 and 24
of them), so it never emits a leaf term and an exact match to a specific curated
function is near-impossible **by construction**. The earlier "exact core-MF capture"
counts (2/12 pilot, 1/42 specific overall) therefore measure the vocabulary, not the
grounding, and are kept below only as history. Scored at the level the tool actually
works at — each curated core term mapped up to its `goslim_generic` bins over the
pinned GO release — Affinage emits a bin of at least one curated core MF for **38/42**
genes, its **single most-supported** MF is such a bin for **32/40** (two genes have no
MF at all), and it emits a bin of a curated core location for **34/38**. So the GO
layer is mostly *right but coarse*: `oxidoreductase activity` for a medium-chain
acyl-CoA dehydrogenase, `molecular transducer activity` for a β2-adrenergic receptor. It also emits **co-mention / entity-collision groundings** — most
sharply for **ADA**, where the synthesized narrative is about *E. coli* Ada
(an alkyltransferase/transcription factor) while the record is keyed to human
adenosine deaminase P00813.

The cohorts are the pilot, batch 2 (13 well-characterized genes), a batch-3 stress test
(5 leaf/hormone cases), and a **batch-4 hard-case set** (12 pseudoenzymes /
disputed-function / reclassified genes drawn from our own curation docs). The one
exact hit on a *primary* function, KRAS `GTPase activity`, is the case where the curated
term happens to be a `goslim_generic` term itself. The real errors are at bin level:
the MF bin misses (ADA, NDUFA4; INS and CASP12 have no MF grounded at all), and
enzymes that also get a catalytic bin that is not a bin of any curated core MF
(`acting on a protein` for SOD1 and LDHA, `acting on DNA` for FASN and GSK3B,
`ligase` for the transferase OTC).

**Crucially, this weakness is specific to the GO layer.** Affinage's free-text
`mechanistic_narrative` — its actual product — is strong and specific, and recovers
exactly the function the GO grounding drops (GPX4's narrative names "selenocysteine
glutathione peroxidase reducing esterified phospholipid hydroperoxides… ferroptosis
defense" with 29 inline PMIDs, where its GO layer says only `oxidoreductase
activity`). See [The mechanism narrative](#the-mechanism-narrative-the-complement-to-go)
below and [`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md).

This is still exploratory, not a finished benchmark. The slim-level metric is lenient
for genes with several core MFs (any one bin counts), and the local AIGR references are
agent-made reviews, not expert-signed ground truth (see
[Reference independence](#reference-independence)).

## Retrieval evaluation

Separately from the GO layer, [**Retrieval recall at scale**](#retrieval-recall-at-scale-paint-campaign-n91)
measures what Affinage *finds* rather than what it says. On the 69 PAINT-backlog genes whose
reviews were not built around Affinage it supplied **48%** of the references a review had to go
locate (an upper bound; the reviewers had read the report). The 22-gene Fanconi-anemia cohort,
whose reviews folded Affinage's papers in by design, scores 85% and must not be pooled with
them. Whether recall varies with how well-studied a gene is cannot be settled on this sample.
Its `gates_passed` flag certifies precision only — there is no recall gate, and six reports
returned zero citations without being flagged.

## What Affinage is (and how it differs from BioReason)

Affinage annotates all 19,293 human protein-coding genes by running, once per
gene, a **reading pass** (extract dated, citation-anchored findings from primary
literature) and a **synthesis pass** (reason over those findings into a causal
"current model" + year-by-year history). Unlike [BioReason](BIOREASON_COMPARISON.md) (which reasons *from*
InterPro/GO-GPT domain inputs), Affinage reasons **bottom-up from the literature**
and then, as a *summary* layer, maps its findings onto controlled-vocabulary
terms in `narrative.mechanism_profile`:

| Field | Content |
|-------|---------|
| `molecular_activity` | GO **MF** terms, each with `supporting_discovery_ids` (which literature findings back it) |
| `localization` | GO **CC** terms + supporting discoveries |
| `pathway` | **Reactome** (`R-HSA-…`) pathway terms |
| `partners` / `complexes` | free-text partner names / complex memberships |

Two features prove these GO terms are **Affinage-generated grounding, not a GOA
import**: every term links back to Affinage's own discovery ids, and each carries
a support **count** (an aggregation over *its* findings). The genuine imports live
separately under `prefetch_data` (`uniprot`, `hpa`, `alphafold`, `depmap`, …).

## Relationship to AIGR

The two projects sit on opposite sides of the *structured ↔ narrative* divide and
are complementary:

- **Affinage:** literature → free-text findings → *maps up to* GO/Reactome terms.
  No GO **evidence codes**, no per-annotation **ACCEPT/MODIFY/REMOVE** verdict, no
  validation against GOA.
- **AIGR (us):** *starts from* GOA's evidence-coded GO annotations → reviews each
  one → keeps/modifies/removes, and authors validated, specific `core_functions`.

So AIGR can act as the **GO-grounding + curation layer** Affinage lacks. The reverse
direction — using Affinage's "current model" as a **deep-research input** to AIGR — was
first judged largely redundant with AIGR's existing deep-research step (same biology,
no independent perspective since both are Claude-generated, human-only; see
[`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md)). **Practice has
since overtaken that judgment:** Affinage is in routine use as a deep-research provider —
139 human gene folders carry a committed `-deep-research-affinage.md` at the time of
writing — and the two later cohorts measure what that use delivers:
the [FA cohort](#forward-test-affinage-as-a-deep-research-input-fa-cohort-n22) found real
net value from the narrative, and the [PAINT campaign](#retrieval-recall-at-scale-paint-campaign-n91)
found it supplies about half of the literature a review needs but cannot be the only
search. The position this page now takes is: **use the narrative as one input, never
import its GO layer, and always search partners/paralogues independently.**

## Methods

For each gene we (1) fetch the Affinage record from the JSON API
(`https://affinage.wi.mit.edu/api/gene/<SYMBOL>`) and cache it **trimmed** under
[`affinage-cache/`](AFFINAGE_EVALUATION/affinage-cache/) — all 42 records are now
committed (run dates 2026-06-09/10), so the comparison re-runs offline; (2) extract the
`mechanism_profile` GO sets; (3) load the local review
(`genes/human/<GENE>/<GENE>-ai-review.yaml`) — every GOA annotation (id, evidence,
review action) plus the reviewer-authored `core_functions`; (4) compute exact-id
agreement per aspect and whether Affinage's profile contains the **reviewed core
MF term**; (5) map each core MF and core location to its `goslim_generic` bins
(reflexive `is_a` + `part_of` closure over the pinned GO release
`go-basic-2026-03-25.obo`, the one the BioReason audit uses) and score whether Affinage
emitted the bin, and whether its most-supported MF is one; (6) report shared exact ids
both in full and excluding GOA terms every one of whose annotations the review
REMOVEd or MARK_AS_OVER_ANNOTATED. All numbers are recomputed from committed inputs by
[`compare_affinage.py`](AFFINAGE_EVALUATION/compare_affinage.py) — nothing is
hard-coded.

```bash
cd projects/AFFINAGE_EVALUATION
uv run python compare_affinage.py --offline --genes-file pilot-genes.txt   # writes results/
uv run python compare_affinage.py --offline --genes-file batch2-genes.txt --out-dir results/batch2
uv run python compare_affinage.py --offline --genes-file batch3-genes.txt --out-dir results/batch3
uv run python compare_affinage.py --offline --genes-file batch4-genes.txt --out-dir results/batch4
```

Re-fetching the 42 records on 2026-09-27 reproduced every committed Affinage GO set
exactly; the only differences from the earlier results were three `core_mf` sets
(ACADM, ADA, ACSL4) that changed because the reviews were revised since, none of
which changed a capture call. **Shared exact ids:** 99 across the 42 genes, 93 after
excluding wholly-rejected GOA terms. Most of the six are generic parents a curator
marked over-annotated because a specific child exists (FASN oxidoreductase and
transferase, GAPDH oxidoreductase), plus AGO2 RNA binding, MAPK1 mitochondrion, and
CPT1C transferase (REMOVEd).

## Pilot results (n=12)

See the generated [summary](AFFINAGE_EVALUATION/results/summary.md) ·
[CSV](AFFINAGE_EVALUATION/results/summary.csv) ·
[per-gene JSON](AFFINAGE_EVALUATION/results/per-gene.json).

- **Slim level:** core-MF bin emitted **11/12** (miss: ADA); top-supported MF is a core
  bin **10/12** (TP53, ADA not); core-location bin **11/12**.
- **Exact core-MF captured: 2/12** (historical metric; see the vocabulary finding above).
  Only AATF and ABL1 had *any* reviewed core
  molecular-function term appear verbatim in Affinage's `molecular_activity` — and
  in both cases the match is a **general secondary** core term (RNA binding for
  AATF; DNA binding for ABL1), **not** the specific primary activity (transcription
  coactivator; non-membrane-spanning tyrosine kinase), which Affinage grounds only
  to the parent (`catalytic activity, acting on a protein`). So the true
  specific-function capture rate is effectively **0/12** in this pilot.
- **Localization agrees well.** Cytosol / mitochondrion / nucleus / plasma
  membrane matches are common; localization is Affinage's strongest aspect.
- **MF grounding is systematically less precise** — see taxonomy below.

## Extended cohort (batch 2, n=13)

A second cohort ([`batch2-genes.txt`](AFFINAGE_EVALUATION/batch2-genes.txt);
[results](AFFINAGE_EVALUATION/results/batch2/summary.md)) of well-characterized
enzymes, kinases, transcription factors and a channel was run to test whether the
pilot pattern generalizes. It does — **0/13** exact core-MF, **13/13** core-MF slim bin,
and the top-supported MF is a core bin for **12/13**. Every gene's defining activity is
grounded only to a slim-level parent (support counts in brackets):

| Gene | AIGR core MF | Affinage top MF |
|------|--------------|-----------------|
| SOD1 | superoxide dismutase activity | oxidoreductase activity |
| CASP3 | cysteine-type endopeptidase activity | catalytic activity, acting on a protein |
| MAPK1 | MAP kinase activity | catalytic activity, acting on a protein |
| HMOX1 | heme oxygenase (decyclizing) activity | molecular adaptor activity (3); oxidoreductase activity is second (2) — the one batch-2 gene whose top bin is wrong |
| LDHA | L-lactate dehydrogenase (NAD+) activity | oxidoreductase activity |
| CFTR | intracellularly ATP-gated chloride channel activity | transporter activity |
| SIRT1 | NAD-dependent protein lysine deacetylase activity | catalytic activity, acting on a protein |

## Stress-test cohort (batch 3, n=5) — *when* does capture happen?

A third cohort ([`batch3-genes.txt`](AFFINAGE_EVALUATION/batch3-genes.txt);
[results](AFFINAGE_EVALUATION/results/batch3/summary.md)) deliberately picked cases
that *might* break the pattern — very specific/leaf enzyme functions plus a small
GTPase and a hormone. Result: **1/5** exact (4/5 at slim level; INS has no MF), and the
one exact hit is the tell.

| Gene | AIGR core MF | Affinage top MF | captured |
|------|--------------|-----------------|:--------:|
| KRAS | **GTPase activity** (GO:0003924) | **GTPase activity** | ✅ |
| CALM1 | calcium ion binding | molecular function regulator / sensor activity | ❌ |
| OTC | ornithine carbamoyltransferase activity | transferase activity + `ligase activity` (wrong branch) | ❌ |
| G6PD | glucose-6-phosphate dehydrogenase activity | oxidoreductase activity + `hydrolase activity` (wrong branch) | ❌ |
| INS | insulin receptor binding | *(empty — no MF grounded at all)* | ❌ |

**The rule this sharpens:** Affinage captures the specific function *only when that
function's GO term is itself a slim term* — `GTPase activity` (GO:0003924) is both the
specific KRAS function and a `goslim_generic` bin, so the slim-level grounding lands
on it. Deep-leaf enzyme terms (ornithine carbamoyltransferase,
glucose-6-phosphate dehydrogenase) are collapsed to their parent. And for a peptide
**hormone** (INS, function = receptor binding) Affinage grounds *no* molecular activity
at all — the MF layer has nothing to say about non-enzymatic function.

## Hard cases (batch 4, n=12) — pseudoenzymes & disputed functions

Full analysis: [`results/hard-cases.md`](AFFINAGE_EVALUATION/results/hard-cases.md).
A cohort of human genes our own docs flag as hard to curate — pseudoenzymes (ILK,
ROR1, CPT1C, CASP12), contested activities (PARK7, UCHL1), reclassifications (HDAC6,
NDUFA4, PLD3), a GAP mis-typed as a GTPase (RASA1), a moonlighter (GAPDH), and a
family-label misdirection (KEAP1). Exact GO capture is **1/12** (GAPDH, on its secondary
core term `RNA binding`; **0/12** on a primary function); at slim level the core-MF bin is
emitted for **10/12**, but the top-supported MF is a core bin for only **6/11** — the worst
cohort. The two layers split sharply:

- **The narrative is genuinely pseudoenzyme-/reclassification-aware** (literature-grounded,
  not domain-grounded): it calls ILK a *"bona fide pseudokinase… no detectable activity,"*
  ROR1 a *"pseudokinase devoid of intrinsic catalytic activity,"* CPT1C's transferase
  *"weak… 20–300× lower,"* HDAC6 a *non-histone/tubulin* deacetylase, and it *adjudicates*
  the PARK7 glyoxalase-vs-deglycase dispute. On **KEAP1** its GO layer avoids the
  actin-binding error a domain-based tool (BioReason/InterPro2GO) made, but its most-supported
  terms are `molecular sensor activity` (4) and `catalytic activity, acting on a protein` (3),
  with `ligase` and `molecular adaptor` (2 each) behind — the catalytic and ligase bins are
  wrong for a non-catalytic substrate adaptor.
- **The GO layer is a lossy down-cast that can contradict its own narrative.** For **ROR1**
  the narrative says *"devoid of intrinsic catalytic activity"* while `mechanism_profile`
  grounds **`catalytic activity, acting on a protein`**; for **CPT1C** the narrative says
  *"weak"* while the GO layer includes `transferase activity`, the activity our review
  REMOVEd (its curated core, palmitoyl-protein hydrolase, falls in the `acting on a
  protein` bin, which Affinage also emits; its top term is `molecular sensor activity`).
  Judged by the **top-supported** term, only ILK (adaptor, 4) and CASP12 (no MF) cleanly
  avoid the ancestral-activity trap. RASA1's top term is `catalytic activity, acting on a
  protein` (5), with the correct `molecular function regulator activity` (3) second;
  PLD3's are `acting on RNA` and `hydrolase` (5 each) ahead of `acting on DNA` (3).
- **Controversy handling is mixed:** PARK7's narrative engages and resolves the dispute; UCHL1's
  omits the contested ubiquitin-ligase activity entirely (the "current model" has no slot for a
  positive-vs-NOT pair).

Across the **combined 42-gene set** the exact curated primary function is captured
**1/42** (KRAS). Three other nominal matches (AATF, ABL1, GAPDH) are general/secondary
terms, not the primary activity. Given the slim vocabulary, the informative numbers are
the slim-level ones: 38/42 core-MF bin, 32/40 top-supported MF in a core bin.

## Forward test: Affinage as a deep-research *input* (FA cohort, n=22)

Full analysis: [`results/fa-cohort.md`](AFFINAGE_EVALUATION/results/fa-cohort.md) · per-gene
writeups in [`results/fa-cohort/`](AFFINAGE_EVALUATION/results/fa-cohort/).

The cohorts above judge Affinage's **GO layer** against finished reviews. This cohort runs the
*forward* experiment the [Relationship to AIGR](#relationship-to-aigr) section flagged as
"weaker than it first appears": take the whole **Fanconi-anemia complementation group (A–W, 22
genes)**, review each de-novo, then feed the Affinage narrative back in as a deep-research source
and measure **net curation value** — not exact-GO overlap.

- **The narrative earned its keep:** **59** Affinage-surfaced primary papers were folded into the
  reviews and **13 new GO annotations** added across **10** genes (including one genuine
  biochemistry gap — FANCA's intrinsic RAD52-like single-strand-annealing activity — and prose-only
  functions like FANCD2 fork protection, FANCM ATR-checkpoint, RAD51C/XRCC2 ICL-repair, MAD2L2
  fork-resection control). **No** existing curation decision was reversed.
- **The GO layer stayed unusable (0/22 imported), and its FA failure mode is sharper than
  "general parent":** on this adaptor/scaffold-heavy pathway it lands on the **wrong catalytic
  branch** — typing the non-catalytic subunits FANCB/E/I as `catalytic activity, acting on a
  protein`, FANCA/PALB2/SLX4 as acting-on-DNA, the RING-E3s FANCL/RFWD3/BRCA1 as generic
  `ligase`, and — inverting the error — the *catalytic* helicase BRIP1/FANCJ as `molecular
  adaptor activity`.
- Several times Affinage's own cited evidence **reinforced** an AIGR non-core/over-annotation
  call (FANCC redox mutants; RAD51C is-not-an-endonuclease; XRCC2 is-not-a-damage-sensor; SLX4
  nuclease-dead), the opposite of redundancy.
- The two `pairwise = tie` records (ERCC4, BRCA1) carry the flag in the report's
  `self_evaluation_pairwise` frontmatter and in the per-gene writeups
  ([ERCC4](AFFINAGE_EVALUATION/results/fa-cohort/ERCC4.md),
  [BRCA1](AFFINAGE_EVALUATION/results/fa-cohort/BRCA1.md)). **It is not recorded in any of
  the 22 reviews' `reference_review`** (0/22; no FA review mentions `tie` or `pairwise`).
  More broadly, none of the 22 FA reviews lists its `-deep-research-affinage.md` as a
  reference, and only 4 (BRCA1, FANCA, FANCC, RAD51) mention Affinage at all, so the
  Affinage provenance of the folded-in papers is recorded in the project writeups rather
  than in the reviews. The weakness the `tie` tracked was in the **GO layer** (a spurious
  RNA-catalytic term on BRCA1), not the prose, which was factually sound.

**Takeaway:** used as this project endorses — narrative-as-input, GO-layer-ignored — Affinage
delivered measurable, conservative value on the very pathway where it should have been most
redundant with AIGR's own deep-research step.

## Retrieval recall at scale (PAINT campaign, n=91)

Full analysis: [`results/paint-campaign.md`](AFFINAGE_EVALUATION/results/paint-campaign.md) ·
generated tables in [`results/paint-campaign/`](AFFINAGE_EVALUATION/results/paint-campaign/).
The 91-gene cohort is pinned in
[`campaign-genes.txt`](AFFINAGE_EVALUATION/results/paint-campaign/campaign-genes.txt)
(reconstructed from the committed `per-gene.json`); `--all` now scores every committed report
(139 genes on 2026-09-27, recall 47%) and is not this cohort. Regenerate with:

```bash
cd projects/AFFINAGE_EVALUATION
uv run python retrieval_recall.py --genes-file results/paint-campaign/campaign-genes.txt \
    --split-file fa-cohort-genes.txt --split-name FA
```

Every cohort above asks what Affinage *says*. This one asks what it *finds*, over the 91 human
genes that had a committed Affinage report when it was first run. **Those 91 are not one
cohort:** 69 are PAINT-backlog genes, and 22 are the FA cohort above, whose reviews were revised
specifically to fold Affinage's papers in. Pooling them inflates recall, so the two are reported
separately (numbers regenerated at commit `fff7793a`):

| cohort | genes | novel refs | supplied by Affinage | recall |
|--------|------:|-----------:|---------------------:|-------:|
| **PAINT backlog (non-FA)** | 69 | 650 | 309 | **48%** |
| FA cohort (Affinage input by design) | 22 | 73 | 62 | 85% |
| all 91 (previously reported as 52%) | 91 | 723 | 371 | 51% |

**On the non-FA genes Affinage supplies about half the references a review has to go find, and
its trust gates cannot tell you which half is missing.** Across all 91, 908 of the 1631 cited
PMIDs arrive prepackaged in the GOA file and need no search at all; recall is scored only
against the 723 the reviewer had to locate. (Scoring against all 1631 understates it at 32%.)
Of what Affinage returned for the non-FA genes, 59% was cited.

- **`gates_passed` measures precision, and there is no recall gate.** The gates correctly certify
  that returned citations are real and correctly quoted. Two verified misses on
  otherwise-clean reports: **ADAMTSL1**'s `PMID:22242013`, which holds the only molecular-function
  experiment ever done on the human protein (a measured SPR negative) and is cited seven times in
  the review; and **ACTG2**'s `PMID:38820162`, a 2024 cryo-EM study supplying four of five proposed
  new annotations and cited 29 times. Both absent from the report **and** from GOA.
- **Whether recall depends on how well-studied the gene is is not established.** The earlier
  claim that it does not (52% / 50% / 56% across dark, medium and well-studied bands) came from
  the pooled 91, and the well-studied band was 17 FA genes out of 24. Without FA the bands read
  51% (25 genes) / 49% (36) / **27%** (7 genes, 62 references). Seven genes cannot carry a trend
  either way, and one of them (ACTR8, 15 novel references) is an empty report. Most genes at the
  100% end of the sorted table (17 of 27) are FA genes, and the remaining ten have one to seven
  novel references each. What does change with curation depth is the *consequence* of a miss: on
  a dark gene, half the literature can be the difference between one functional experiment and
  none.
- **Six reports returned zero PMIDs** (AADACL2/3/4, ACP7, ACTL10, ACTR8) — including a whole
  paralogue family — and are not flagged as failures. ACTL10's empty report carries
  `gates_passed: True`, which is vacuously true and reads as success.

**Takeaway:** consistent with the FA-cohort result — the narrative is the product and it earns its
keep — but it cannot be the literature search. 48% is an upper bound (see
[Reference independence](#reference-independence)). The decisive paper for a sparsely-annotated gene is
usually titled for a partner, complex, or paralogue, so search those independently.

## Reference independence

None of the reference sets on this page is independent of the thing being scored, and each
result should be read with the matching caveat:

- **The AIGR reviews are agent-made.** `core_functions` and review actions were written by
  the same class of model (Claude) that Affinage uses, not signed off by expert curators. They
  are a consistent reference, not ground truth; a disagreement is a prompt to look, not a
  verdict on Affinage.
- **The FA reviews had Affinage input by design.** Their reference lists were revised to fold
  in Affinage-surfaced papers, so their 85% recall measures that editing step, not Affinage's
  retrieval. They are excluded from every recall headline above.
- **Recall is an upper bound even without FA.** 57 of the 69 non-FA reviews cite the Affinage
  report as a source, so the reviewers read it before choosing references. A paper Affinage
  surfaced is more likely to end up cited than an equally relevant one it missed. A clean
  estimate needs reviews written blind to the report.
- **The GO-layer cohorts (42 genes) are the least affected.** None of the 42 gene folders
  holds an Affinage report and none of the reviews mentions Affinage. The comparison also uses
  `core_functions`, not reference lists. The
  agent-made caveat still applies.

## Failure-mode taxonomy (verified by inspection)

### 1. Slim-level MF grounding (dominant, by design)

Affinage grounds to a true but **generic ancestor**, missing the specific curated
function. Because every term it emits is a `goslim_generic` bin, this is how the tool
is built, not an occasional error. This mirrors the `LSP` ("less precise") and frequency-bias patterns the
[BioReason project](BIOREASON_COMPARISON.md) found.

| Gene | AIGR core MF | Affinage MF (top) |
|------|--------------|-------------------|
| GPX4 | phospholipid-hydroperoxide glutathione peroxidase activity (GO:0047066) | oxidoreductase activity (GO:0016491) |
| ACADM | medium-chain fatty acyl-CoA dehydrogenase activity (GO:0070991) | oxidoreductase activity (GO:0016491) |
| ADRB2 | β2-adrenergic receptor activity (GO:0004941) | molecular transducer activity (GO:0060089) |
| AGO2 | RNA endonuclease activity (GO:0004521) | catalytic activity, acting on RNA (GO:0140098) |

### 2. Co-mention / spurious MF grounding

Terms grounded from literature co-mention that are **wrong for the protein's
actual activity**: GPX4 gets `DNA binding` (GO:0003677) and `catalytic activity,
acting on RNA` (GO:0140098); AGO2 gets `transcription regulator activity`
(GO:0140110). Our reviews handle such biology as `KEEP_AS_NON_CORE` or `REMOVE`
(e.g. GPX4 `protein binding` → REMOVE), which Affinage's summary layer cannot do.

### 3. Entity / gene-symbol collision in retrieval (ADA)

The sharpest failure. Affinage's record for **ADA** is keyed to human adenosine
deaminase (`prefetch_data.uniprot.accession = P00813`), but the synthesized
`current_model` is a **chimera of three different "ADA/Ada" entities**:

> "The *E. coli* Ada protein is a bifunctional enzyme and transcriptional
> regulator of the adaptive response to alkylating agents… in eukaryotes, the
> orthologous ADA complex subunits (Ada2, Ada3) scaffold the GCN5 histone
> acetyltransferase within the ADA and SAGA co-activator complexes… in humans,
> ADA enzymatic activity (deamination of adenosine and deoxyadenosine) is
> essential for lymphocyte survival…"

Three unrelated proteins — *E. coli* Ada (DNA alkyltransferase/TF), the
eukaryotic **ADA2/ADA3** transcriptional-adaptor subunits of SAGA/ATAC, and human
**ADA** (adenosine deaminase) — are conflated by the shared symbol. The GO
grounding latched onto the first two: every MF term (`DNA binding`, `transcription
regulator activity`, `catalytic activity, acting on DNA/protein`, `transferase
activity`) and the partners/complexes (`GCN5`, `ADA2`, `ADA3`, `SAGA`, `ATAC`)
belong to those entities, while the actual **`adenosine deaminase activity`
(GO:0004000)** — mentioned only in the narrative's trailing clause — is **dropped
from the profile entirely** (0 shared GO ids with GOA; 0 localization terms).
Tellingly, Affinage's *own* head-to-head `evaluation.pairwise` scores ADA a
`"loss"` versus UniProt. This is a literature-retrieval symbol-ambiguity failure,
analogous to the BioReason `csr-1` wrong-input case, and precisely what an
accession-anchored GOA review catches.

### 4. Wrong parent *branch* (metabolic enzymes → acting-on-protein/DNA)

Beyond generic-ancestor grounding (mode 1), several small-molecule metabolic
enzymes **also** receive a catalytic bin that is not a slim ancestor of any of their
curated core MFs: SOD1 and LDHA get `catalytic activity, acting on a protein`
(GO:0140096), FASN and GSK3B get `catalytic activity, acting on DNA` (GO:0140097),
and OTC, a transferase, gets `ligase activity` (GO:0016874). The slim scoring counts
these as off-bin, so they are real errors and not imprecision. In each case the
correct bin is also present and is the most-supported term. Across the 42 genes, 22 carry at least one catalytic-bin MF
outside every core bin (listed per gene as `aff_mf_off_core_bins` in the
per-gene JSON). Some of these are defensible non-core biology, not errors.

An earlier version of this list included PKM. That was wrong. PKM's curated core
includes protein tyrosine and protein serine/threonine kinase activity, both under
`acting on a protein`. The same applies to CPT1C (core: palmitoyl-(protein) hydrolase
activity) and GAPDH (core includes peptidyl-cysteine S-nitrosylase activity). For all
three, `acting on a protein` is a correct bin.

## The mechanism narrative (the complement to GO)

Full analysis: [`results/narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md).

The GO `mechanism_profile` is Affinage's **weakest** output; its actual product is
the citation-anchored `narrative.mechanistic_narrative` plus the structured
`timeline.discoveries` (each a typed object: `year`, `finding`, `method`, `journal`,
`confidence` + rationale, `pmids[]`, `is_preprint`), and a `teleology` track of what
each advance *explained*. On the sampled genes the narrative **recovers the specific
mechanism the GO layer drops** — the GO grounding is a lossy down-cast, not a measure
of what Affinage knows:

| Gene | GO layer (lossy) | Narrative (specific; distinct inline PMIDs) |
|------|------------------|---------------------------------------------|
| GPX4 | oxidoreductase activity | selenocysteine glutathione peroxidase reducing membrane phospholipid hydroperoxides; ferroptosis defense (29) |
| CASP3 | catalytic activity, acting on a protein | executioner cysteine protease; zymogen→p20/p11; DEVD specificity; cleaves PARP (25) |
| MAPK1 | catalytic activity, acting on a protein | ERK2 Ser/Thr kinase; MEK1 dual phosphorylation (25) |
| ADRB2 | molecular transducer activity | β2-adrenergic GPCR, catecholamine-responsive (18) |

**But the narrative has two failure modes.** (1) *Recency/novelty bias on canonical
genes:* the ADRB2 narrative surveys recent specialized papers (HCC drug resistance,
amyloid-β, CAR-T checkpoint, osteoclastogenesis) but omits the textbook core — no
cAMP, adenylyl cyclase, Gs, or β-arrestin desensitization. (2) *Symbol collisions
break the prose too:* ADA's narrative is the three-entity chimera (§3). Usefully,
Affinage's own `evaluation.pairwise` tracks these tiers — GPX4/CASP3/MAPK1 = `win`,
ADRB2 = `tie`, ADA = `loss` — a built-in triage flag for which narratives to trust.

**Implication, as first argued on this sample.** The narrative is Affinage's real
product. On these 42 genes it looked **largely redundant** with AIGR's existing deep
research as an *input source*. The biology overlaps, and the PMID-anchoring advantage is
trivial to replicate (DOI/`[n]`→PMID is a converter call). "More citations" is not value
either: GPX4 has 37 in Affinage against 10 in our review, skewed to material curation
prunes. It adds no independent perspective (both are Claude), and it is human-only. Full
argument in [`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md). The
later [FA cohort](#forward-test-affinage-as-a-deep-research-input-fa-cohort-n22) tested
this directly and found measurable net value. Affinage has since become a routine
provider (see [Relationship to AIGR](#relationship-to-aigr)). The redundancy argument
still holds for the GO layer and for citation counts, but not for the narrative as a
first pass.

## Next steps

1. **Ontology-aware scoring — done at slim level (2026-09-27).** `compare_affinage.py`
   now maps core terms to `goslim_generic` bins over the pinned GO release. Still open:
   a per-term precision score (what fraction of emitted bins are bins of *any* accepted
   GOA or core term, not only core), and a stricter variant restricted to each gene's
   primary core MF.
2. **Scale the cohort.** 42 genes done (pilot + batches 2–4, incl. a hard-case set).
   Since exact capture is fixed by the slim vocabulary, the next cohort should report
   slim-level capture and top-bin accuracy per class (enzymes, TFs, transporters,
   receptors, structural, uncharacterized). The KRAS rule is now explained: exact capture
   happens only when the curated term is itself a slim term.
3. **Score the narrative, not just the GO layer.** Qualitative sampling done (see
   [narrative-vs-go.md](AFFINAGE_EVALUATION/results/narrative-vs-go.md)); next apply
   the BioReason correctness/completeness rubric on `mechanistic_narrative` across a
   scored cohort, with a blinded second rater, and test whether `evaluation.pairwise`
   predicts the human scores.
4. **Symbol-collision sweep.** Systematically check `prefetch_data.uniprot.accession`
   vs the organism/protein described in `current_model` to size the ADA-type
   failure across the genome.
5. **Integration is in use; measure it properly.** Affinage is already a routine
   deep-research provider (139 human reports committed). What is missing is a clean
   recall estimate. That needs reviews written blind to the report (see
   [Reference independence](#reference-independence)), enough non-FA well-studied genes
   to test whether recall falls with curation depth (7 today), and provenance recorded
   in the review itself (a `file:` reference plus `reference_review` noting the
   `pairwise` flag), which the FA reviews currently lack.

## Notes

### 2026-09-27 — response to the [2026-09-26 review](FUNCTION_PREDICTION_EVALUATION/REVIEW-2026-09-26.md)

- **Vocabulary is `goslim_generic`.** All 43 distinct GO ids Affinage emits across the 42
  GO-layer genes are `goslim_generic` terms (43/43, in both the current 2026-07-26 slim file and
  the pinned 2026-03-25 release). Other slims cover fewer: agr 16, pir 19, drosophila 24.
  `compare_affinage.py` now scores at slim level. Core-MF bin emitted: 38/42. Top-supported MF
  is a core bin: 32/40. Core-location bin emitted: 34/38. The exact 1/42 and 2/12 figures stay
  as history only.
- **Cache committed.** All 42 records were fetched from the live API and committed trimmed.
  The re-fetch reproduced the committed GO sets exactly. `--offline` re-runs byte-identically.
- **Shared ids:** 99 in total, 93 excluding GOA terms the reviews wholly rejected.
  `NEG_ACTIONS` is now used.
- **PAINT recall split.** The pinned 91-gene list is committed. The FA cohort (22 genes,
  Affinage input by design) scores 85% and the other 69 score 48%, against 51% pooled at
  current HEAD (52% originally). The "recall is flat across curation depth" claim is withdrawn:
  without FA the well-studied band is 27% on 7 genes, which is too few to support a trend either
  way. `--all` now scores 139 genes (47%) and is no longer this cohort.
- **Examples corrected.** PKM was removed from the wrong-branch list. `acting on a protein` is a
  correct bin for PKM, CPT1C and GAPDH, given their core functions. RASA1 and KEAP1 are now
  described by their top-supported terms. HMOX1's top MF is adaptor (3), not oxidoreductase (2).
  hard-cases.md now reads 1/12 exact, 0/12 specific.
- **FA provenance.** The `tie` flag is in the `reference_review` of 0/22 FA reviews, not "each".
  None of the 22 cites its Affinage report as a `file:` source, and 4/22 mention Affinage at all.
- **Integration stance reconciled.** Affinage is in routine use (139 reports), and next step 5
  now asks for a blind recall test, not integration.
- Added the [Reference independence](#reference-independence) section.
