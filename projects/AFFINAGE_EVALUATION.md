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

This is a **pilot**, not a finished benchmark: n=12, exact-GO-id agreement only,
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

So AIGR can act as the **GO-grounding + curation layer** Affinage lacks; and
Affinage's citation-anchored "current model" is a strong candidate **deep-research
input** for AIGR reviews (feeding `description` / `proposed_new_terms`), provided
its free-text claims are re-grounded to GO by our pipeline before they touch
`existing_annotations` or `core_functions`.

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

## Failure-mode taxonomy (pilot, verified by inspection)

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

## Next steps

1. **Ontology-aware scoring.** Replace exact-id match with ancestor/descendant
   distance (using the pinned GO release, as in the BioReason
   [ontology-authority](BIOREASON_COMPARISON/verify_ontology_authority.py)
   approach) to quantify the "general-parent" pattern instead of only counting it.
2. **Scale the cohort.** Extend from 12 to a stratified sample (enzymes, TFs,
   transporters, receptors, structural, uncharacterized) and report per-class.
3. **Score the narrative, not just the GO layer.** Adopt the BioReason
   correctness/completeness rubric on Affinage's `current_model` text, with a
   blinded second rater.
4. **Symbol-collision sweep.** Systematically check `prefetch_data.uniprot.accession`
   vs the organism/protein described in `current_model` to size the ADA-type
   failure across the genome.
5. **Integration spike.** Prototype Affinage's `current_model` as a `deep-research`
   provider input for AIGR reviews.
