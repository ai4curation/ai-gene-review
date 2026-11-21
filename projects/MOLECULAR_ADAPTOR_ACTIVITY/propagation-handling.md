---
title: "Handling the propagated adaptor bulk"
species: [human]
---

# Handling the propagated adaptor bulk (IBA vs TreeGrafter / ARBA / UniRule)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Almost every annotation under the adaptor subtree is computational. The five
evidence facets recorded for the `GO:0030674` subtree in
[data/propagation-stats.yaml](data/propagation-stats.yaml) — phylogenetic graft
(48.1%), sequence-model rule (21.5%), combined-electronic (13.0%), orthology
projection (12.2%) and reviewed IBA (4.1%) — sum to ~99% of the 446,453 rows,
leaving ~1% for everything else (ISS, ISO, IC, NAS, TAS, ND *and* the
experimental rows; QuickGO's stats facets do not split those out). So a reviewer
who opens an adaptor row is, far more often than not, looking at a **prediction**
— and the predictions are not all of one kind. This page is the rule for telling
them apart. It specialises the general IBA guidance in CLAUDE.md and
[IBA_REVIEW](../IBA_REVIEW.md), and the TreeGrafter evaluation in
[TREEGRAFTER](../TREEGRAFTER.md), to adaptor terms; for those groups it defers to
those projects rather than restating them.

## The sources, by group

Source labels, evidence codes and `GO_REF` ids below were read from real rows in
the `GO:0030674` subtree (QuickGO downloadSearch) and from the GO reference
registry (`go-site/metadata/gorefs.yaml`). The **Share** column is the subtree
**evidence-code** facet (from the data file), which is why it is keyed to the
evidence code rather than exactly to the `assigned_by` source (e.g. a couple of
points of `ECO:0000265` are not from Ensembl).

| Group | Evidence | Source (`assigned_by`) | `GO_REF` | Share | What the row actually rests on |
|---|---|---|---|---|---|
| **A — reviewed phylogenetic** | IBA `ECO:0000318` | GO_Central | `GO_REF:0000033` ("Annotation inferences using phylogenetic trees") | ~4% | A PAINT curator's **IBD** judgment: the function was placed at a tree node after reading the family's experimental annotations. |
| **B — automatic phylogenetic** | IEA `ECO:0007826` | TreeGrafter | `GO_REF:0000118` ("TreeGrafter-generated GO annotations") | ~48% | A query sequence **grafted into a PANTHER reference tree**, inheriting that branch's terms — **no curator inspected the placement or the grafted term**. The single largest slice. |
| **C — rule / signature (sequence)** | IEA `ECO:0000256` | UniProt / InterPro | UniRule `GO_REF:0000104` (curated); ARBA `GO_REF:0000117` (ML); InterPro2GO `GO_REF:0000002` (signature) | ~21% | A sequence rule or domain/family signature mapped to the term. CLAUDE.md treats **UniRule** as good support for *membership*, but **ARBA** as an *unvetted prediction* (a lead, not support). |
| **D — orthology projection** | IEA `ECO:0000265` | Ensembl | `GO_REF:0000107` (Ensembl Compara) | ~12% | A manual annotation **projected to an ortholog** via Compara. Only as strong as the source annotation and the ortholog call. |
| **E — combined / dedup** | IEA `ECO:0000501` | UniProt | `GO_REF:0000120` | ~13% | A redundancy-reduced **merge of several of the above** (its `WITH/FROM` names the contributing methods — e.g. an ARBA rule *and* an Ensembl projection *and* a mouse ortholog on one row). **Not sequence-only, and agreement between independent pipelines is mild corroboration, not weakness.** Read through to the methods. |

## Why adaptor terms are especially fragile under propagation

Propagation transfers a *term*; an adaptor term names a *relation* that the
sequence does not carry. Three consequences:

1. **The two ends never travel.** An adaptor's meaning is "bridges partner A and
   partner B," recorded as its `has input` molecules — and those partners are
   lineage-specific. A TreeGrafter or InterPro2GO row says "this protein has the
   domain architecture of an adaptor family," **not** "this protein bridges A and
   B in this organism." The binding activity is predicted poorly by a signature;
   the specific bridge is not predicted at all.
2. **Adaptor domains are modular and reused.** SH2/SH3, PTB, coiled-coil, F-box,
   DCAF-box, BicD-like and WD40 scaffolds recur across families that bridge
   different partners — or nothing. Domain-architecture propagation therefore has
   a high false-positive rate for the *specific* adaptor child, and often for the
   bridging role at all.
3. **Adjacent functions are sequence-identical.** Adaptor, sequestering and
   carrier proteins — and scaffolds — are not separable by signature.
   Propagation cannot make the distinction decision rule 3 requires, and cannot
   even make the finer one the project page draws (`GO:0140693` molecular
   condensate scaffold is *in-branch*, only `GO:0032947` is the out-of-branch
   scaffold exclusion).

## Decision procedure for a propagated adaptor row

Apply in order; it layers on the project
[decision rules](../MOLECULAR_ADAPTOR_ACTIVITY.md#decision-rules-draft).

1. **Is the *same* term also supported experimentally on this gene?** Then the
   propagation is corroborated — `ACCEPT`. A gene appearing in its own IBA
   `WITH/FROM` is expected here, **not** circular (CLAUDE.md IBA note); do not
   mark it `CIRCULAR_OR_REDUNDANT`. If instead a *more specific child* is the term
   with experimental support, that child stands on its own row and the propagated
   **parent** is judged by decision rule 5 — `TOO_GENERAL` unless it covers a
   distinct bridging event the child does not (as GRB2 and RPTOR keep
   `GO:0030674`, for LAT-microcluster organisation and Rag-GTPase lysosomal
   recruitment respectively, beside their specific adaptor children). Do not
   `ACCEPT` a propagated parent on the strength of an experimental child.
2. **Can you name the two ends?** From literature or the lineage, identify the
   partners this protein would bridge. If yes and the propagated term is as
   precise as the evidence warrants, `ACCEPT` if core / `KEEP_AS_NON_CORE` if
   peripheral, naming the partners in `reason`. If the literature shows a *more
   specific child*, note that **`MODIFY` needs this row's own evidence to reach
   the child** (CLAUDE.md, 2026-11-14 ruling): a signature or graft row whose
   source maps only to the general term is **not** a `MODIFY` — assert the child
   as a separate `NEW` row (with evidence appropriate to its source: the paper,
   when literature names the partners) and send the propagated general row to
   step 3. (A *lateral* correction of a mis-typed branch — the replacement is not
   a descendant — is the separately sanctioned `MODIFY`, as the LDLRAP1 worked
   example did; the depth bar does not apply to it.)
3. **If the ends cannot be named, handle by group — and never REMOVE merely for
   being electronic** (CLAUDE.md): a challenge needs a biological argument.
   - **Group A (IBA):** argue the **node placement**, not a similarity score — is
     the target inside the clade that inherited the adaptor function, and is there
     target-specific evidence of loss or divergence? A sound IBA stays. Use the
     taxonomy and failure patterns in [IBA_REVIEW](../IBA_REVIEW.md).
   - **Group B (TreeGrafter):** here the measured failure is usually **not** the
     placement but the **grafted term's granularity**. The corpus evaluation in
     [TREEGRAFTER](../TREEGRAFTER.md) down-graded 26.4% of TreeGrafter rows (41.5%
     of molecular-function rows), and in roughly three-quarters of those the tree
     placement was sound while the inherited term was too coarse, a sibling, or
     out of context. So **check the term first**: `MODIFY` to the right
     granularity *on the row's own evidence* (else per step 2 the better term is a
     `NEW` row), `MARK_AS_OVER_ANNOTATED` for a too-coarse or out-of-context
     grafted term, or the lateral `MODIFY` of step 2 for a sibling/mis-typed
     adaptor child — each with a stated reason.
   - **Groups C and D (rule / signature / projection):** these are *not* uniform.
     **UniRule** (curated) and **Ensembl** (projected from a manual annotation)
     deserve a reading of what they rest on before any challenge; **ARBA** (ML)
     and **InterPro2GO** (bare signature) are the weakest and the first to
     question. A challenge still needs a biological reason — e.g. the gene is a
     divergent paralog that lost the bridging module, carries the domain but its
     partners are absent in this lineage, or is a stable structural subunit rather
     than a transient bridge.
   - **Group E (combined / dedup):** read through the `WITH/FROM` to the methods
     that actually agree and judge by them; do not treat it as a bare signature.
     Two independent pipelines reproducing the same adaptor call is mild
     corroboration (TREEGRAFTER measured acceptance rising to ~77% for such rows,
     though confounded by reviewers seeing the combined label).

## Which IBA_REVIEW failure patterns bite adaptors most

From the [IBA_REVIEW](../IBA_REVIEW.md) catalogue, the patterns that recur for
adaptor terms specifically:

- **Complex / compartment / pathway membership over-transfer** (pattern 10): a
  non-adaptor **structural subunit** of a complex inherits the adaptor term of a
  genuine adaptor in the same family. This is the adaptor-vs-scaffold confusion of
  decision rule 3, arriving by propagation.
- **Paralog / secondary-activity transfer** (pattern 5) and
  **neo-functionalization** (pattern 4): a paralog that kept the domain but
  bridges different partners, or none, gets the ancestral adaptor child.
- **Mis-grouping revealed by `WITH/FROM`** (pattern 12): the donor list exposes a
  family that was lumped too broadly for a single adaptor assertion.

## What this project does, and does not, do with the bulk

This project is **anchored on experimental evidence**: the phase-1 worklist is the
666 human gene products with an experimental adaptor annotation, not the ~446k
propagated rows. We do **not** sweep the propagated bulk wholesale. This page is
the rule a reviewer applies when a gene already on the worklist *also* carries
propagated adaptor rows (as GRB2, RPTOR and BICD1 all did), so those rows get a
consistent, source-aware call rather than a reflexive accept or a reflexive
remove. A systematic sweep of the propagated population, if it is ever wanted,
belongs in the projects that already evaluate those pipelines —
[TREEGRAFTER](../TREEGRAFTER.md) for the automatic-phylogenetic group and
[IBA_REVIEW](../IBA_REVIEW.md) for the reviewed-phylogenetic group — not here.
