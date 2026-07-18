---
title: "Affinage Evaluation Project"
maturity: IN_PROGRESS
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
  narrative_vs_go: AFFINAGE_EVALUATION/results/narrative-vs-go.md
---
# Affinage Evaluation Project

Systematic evaluation of **Affinage** (Cheeseman Lab, Whitehead Institute/MIT;
[affinage.wi.mit.edu](https://affinage.wi.mit.edu), [arXiv:2607.02217](https://arxiv.org/abs/2607.02217))
against the agent-adjudicated local AIGR gene reviews — a sibling exercise to the
[BioReason-Pro Comparison Project](BIOREASON_COMPARISON.md), reusing its
methodology (treat the external tool's output as preliminary research, diff it
against GOA and the reviewed core functions).

**Bottom line (n=12 pilot, human):** Affinage *does* ground its literature
findings to GO terms — but the grounding behaves like a **recall-oriented,
frequency-weighted classifier**. It agrees well on **subcellular localization**,
captures **general themes** via its Reactome layer, but **almost never grounds to
the specific curated molecular function** (exact core-MF match: **2/12**), instead
stopping at a general parent (`oxidoreductase activity` for a medium-chain
acyl-CoA dehydrogenase; `molecular transducer activity` for a β2-adrenergic
receptor). It also emits **co-mention / entity-collision groundings** — most
sharply for **ADA**, where the synthesized narrative is about *E. coli* Ada
(an alkyltransferase/transcription factor) while the record is keyed to human
adenosine deaminase P00813.

A second, independent 13-gene cohort (enzymes, kinases, TFs, a channel)
**reproduces the pattern exactly**: **0/13** specific core-MF captured, and it
surfaces a sharper variant — several small-molecule metabolic enzymes are grounded
to the *wrong* catalytic branch (`catalytic activity, acting on a protein/DNA`).
Across the **combined 25 genes**, the specific curated primary function is captured
**0/25** times.

**Crucially, this weakness is specific to the GO layer.** Affinage's free-text
`mechanistic_narrative` — its actual product — is strong and specific, and recovers
exactly the function the GO grounding drops (GPX4's narrative names "selenocysteine
glutathione peroxidase reducing esterified phospholipid hydroperoxides… ferroptosis
defense" with 29 inline PMIDs, where its GO layer says only `oxidoreductase
activity`). See [The mechanism narrative](#the-mechanism-narrative-the-complement-to-go)
below and [`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md).

This is still exploratory, not a finished benchmark: exact-GO-id agreement only,
and the local AIGR references are mixed-maturity, not independently expert-signed
ground truth.

## What Affinage is (and how it differs from BioReason)

Affinage annotates all 19,293 human protein-coding genes by running, once per
gene, a **reading pass** (extract dated, citation-anchored findings from primary
literature) and a **synthesis pass** (reason over those findings into a causal
"current model" + year-by-year history). Unlike BioReason (which reasons *from*
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
direction — using Affinage's "current model" as a **deep-research input** to AIGR — is
weaker than it first appears: on inspection it is **largely redundant** with AIGR's
existing deep-research step (same biology, no independent perspective since both are
Claude-generated, human-only, and its apparent citation advantages are trivial to
replicate). See [The mechanism narrative](#the-mechanism-narrative-the-complement-to-go)
and [`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md).

## Methods

For each gene we (1) fetch the Affinage record from the JSON API
(`https://affinage.wi.mit.edu/api/gene/<SYMBOL>`, cached under
[`affinage-cache/`](AFFINAGE_EVALUATION/affinage-cache/)); (2) extract the
`mechanism_profile` GO sets; (3) load the local review
(`genes/human/<GENE>/<GENE>-ai-review.yaml`) — every GOA annotation (id, evidence,
review action) plus the reviewer-authored `core_functions`; (4) compute exact-id
agreement per aspect and whether Affinage's profile contains the **reviewed core
MF term**. All numbers are recomputed from committed inputs by
[`compare_affinage.py`](AFFINAGE_EVALUATION/compare_affinage.py) — nothing is
hard-coded.

```bash
cd projects/AFFINAGE_EVALUATION
python compare_affinage.py --genes-file pilot-genes.txt   # writes results/
python compare_affinage.py --genes-file batch2-genes.txt --out-dir results/batch2
```

The exact-id metric is deliberately strict and **understates** agreement where
Affinage grounds to a true GO *ancestor* of the curated term; those cases are read
qualitatively below (and are the dominant pattern). Adding an ontology-aware
ancestor/descendant relation is the top follow-up (see [Next steps](#next-steps)).

## Pilot results (n=12)

See the generated [summary](AFFINAGE_EVALUATION/results/summary.md) ·
[CSV](AFFINAGE_EVALUATION/results/summary.csv) ·
[per-gene JSON](AFFINAGE_EVALUATION/results/per-gene.json).

- **Exact core-MF captured: 2/12.** Only AATF and ABL1 had *any* reviewed core
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
pilot pattern generalizes. It does — **0/13** specific core-MF captured. Every
gene's defining activity is grounded only to a top-level parent:

| Gene | AIGR core MF | Affinage top MF |
|------|--------------|-----------------|
| SOD1 | superoxide dismutase activity | oxidoreductase activity |
| CASP3 | cysteine-type endopeptidase activity | catalytic activity, acting on a protein |
| MAPK1 | MAP kinase activity | catalytic activity, acting on a protein |
| HMOX1 | heme oxygenase (decyclizing) activity | oxidoreductase activity |
| LDHA | L-lactate dehydrogenase (NAD+) activity | oxidoreductase activity |
| CFTR | intracellularly ATP-gated chloride channel activity | transporter activity |
| SIRT1 | NAD-dependent protein lysine deacetylase activity | catalytic activity, acting on a protein |

Across the **combined 25-gene set**, the specific curated primary function is
captured **0/25** (the two nominal core matches in the pilot, AATF and ABL1, are
general secondary terms, not the primary activity).

## Failure-mode taxonomy (verified by inspection)

### 1. General-parent / less-precise MF grounding (dominant)

Affinage grounds to a true but **generic ancestor**, missing the specific curated
function. This mirrors the `LSP` ("less precise") and frequency-bias patterns the
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
enzymes are grounded to the **wrong catalytic branch** entirely: SOD1, LDHA and
PKM receive `catalytic activity, acting on a protein` (GO:0140096), and FASN and
GSK3B receive `catalytic activity, acting on DNA` (GO:0140097) — none of which act
on proteins or DNA in the reaction the curated core function describes. This looks
like literature co-mention of protein/nucleic-acid partners leaking into the
substrate-class grounding, and it is worse than mere imprecision: the assigned
parent is not an ancestor of the true term, so even ontology-aware ancestor
scoring would (correctly) count it as wrong.

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

**Implication — but do not over-read it as an integration case.** The narrative is
Affinage's real product, but as an *input source* it is **largely redundant** with
AIGR's existing deep-research: the biology overlaps, the PMID-anchoring advantage is
trivial to replicate (DOI/`[n]`→PMID is a converter call), "more citations" is not
value (GPX4: Affinage 37 vs our review's 10, skewed to material curation prunes), it
adds no independent perspective (both are Claude), and it is human-only. Its residual
value is convenience — a free precomputed first pass for the human backlog — plus a
weak dark-gene prioritization signal. Full argument in
[`narrative-vs-go.md`](AFFINAGE_EVALUATION/results/narrative-vs-go.md).

## Next steps

1. **Ontology-aware scoring.** Replace exact-id match with ancestor/descendant
   distance (using the pinned GO release, as in the BioReason
   [ontology-authority](BIOREASON_COMPARISON/verify_ontology_authority.py)
   approach) to quantify the "general-parent" pattern instead of only counting it.
2. **Scale the cohort.** 25 genes done (pilot + batch 2); extend to a larger
   stratified sample (enzymes, TFs, transporters, receptors, structural,
   uncharacterized) and report per-class capture rates.
3. **Score the narrative, not just the GO layer.** Qualitative sampling done (see
   [narrative-vs-go.md](AFFINAGE_EVALUATION/results/narrative-vs-go.md)); next apply
   the BioReason correctness/completeness rubric on `mechanistic_narrative` across a
   scored cohort, with a blinded second rater, and test whether `evaluation.pairwise`
   predicts the human scores.
4. **Symbol-collision sweep.** Systematically check `prefetch_data.uniprot.accession`
   vs the organism/protein described in `current_model` to size the ADA-type
   failure across the genome.
5. **(Deprioritized) Integration.** A prior idea was to wire Affinage in as a
   `deep-research` provider; the [narrative analysis](AFFINAGE_EVALUATION/results/narrative-vs-go.md)
   argues against it (redundant with existing deep research, no independent
   perspective, human-only). Only worth revisiting as a free first-pass for the human
   backlog, or if a targeted test shows its retrieval recovers primary core-function
   evidence our pipeline systematically misses (raw citation count does not show this).
