---
title: "Handling the propagated adaptor bulk"
species: [human]
---

# Handling the propagated adaptor bulk (IBA vs TreeGrafter / ARBA / UniRule)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Almost every annotation under the adaptor subtree is computational. Of the
446,453 annotations in the `GO:0030674` subtree
([data/propagation-stats.yaml](data/propagation-stats.yaml)), ~96% are
electronic or phylogenetically propagated and only a small remainder is
experimental. So a reviewer who opens an adaptor row is, far more often than
not, looking at a **prediction** — and the predictions are not all of one kind.
This page is the rule for telling them apart and deciding what each is worth. It
specialises the general IBA guidance in CLAUDE.md and
[IBA_REVIEW](../IBA_REVIEW.md) to adaptor terms; for the IBA tier it defers to
that project rather than restating it.

## The sources, by tier

Source labels, evidence codes and `GO_REF` ids below were read from real rows in
the `GO:0030674` subtree (QuickGO downloadSearch) and from the GO reference
registry (`go-site/metadata/gorefs.yaml`); percentages are the subtree
evidence/assigned-by facets in the data file.

| Tier | Evidence | Source (`assigned_by`) | `GO_REF` | What the row actually rests on |
|---|---|---|---|---|
| **1 — reviewed phylogenetic** | IBA `ECO:0000318` | GO_Central | `GO_REF:0000033` ("Annotation inferences using phylogenetic trees") | A PAINT curator's **IBD** judgment: the function was placed at a tree node after reading the family's experimental annotations. ~4% of the subtree. |
| **2a — automatic phylogenetic** | IEA `ECO:0007826` | TreeGrafter | `GO_REF:0000118` ("TreeGrafter-generated GO annotations") | A query sequence **grafted into a PANTHER reference tree**, inheriting that branch's terms — no curator inspected the placement. The single largest slice (~48%). |
| **2b — curated rule** | IEA `ECO:0000256` | UniProt | `GO_REF:0000104` (UniRule) | A **curated** UniProt rule transferring a manual annotation on shared sequence features. CLAUDE.md treats UniRule as good support for *membership*. |
| **3a — ML rule** | IEA `ECO:0000256` | UniProt | `GO_REF:0000117` ("ARBA machine learning models") | A **machine-learned** association rule. CLAUDE.md classes ARBA as an *unvetted prediction* — a lead, not support. |
| **3b — signature mapping** | IEA `ECO:0000256` | InterPro | `GO_REF:0000002` (InterPro2GO) | A domain/family **signature → GO** mapping: the protein matched a signature whose family is mapped to this term. |
| **2c — orthology projection** | IEA `ECO:0000265` | Ensembl | `GO_REF:0000107` (Ensembl Compara) | A manual annotation **projected to an ortholog** via Compara. Only as strong as the source annotation and the ortholog call. |
| (dedup) | IEA | UniProt | `GO_REF:0000120` | A redundancy-reduced combination of several of the above; read through to the underlying method. |

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
3. **Adjacent functions are sequence-identical.** Adaptor, scaffold
   (`GO:0032947`/`GO:0140693`), sequestering and carrier proteins are not
   separable by signature. Propagation cannot make the distinction the project's
   decision rule 3 requires.

## Decision procedure for a propagated adaptor row

Apply in order; it layers on the project
[decision rules](../MOLECULAR_ADAPTOR_ACTIVITY.md#decision-rules-draft).

1. **Is the same (or a child) term also supported experimentally on this gene?**
   Then the propagation is corroborated — `ACCEPT`. A gene appearing in its own
   IBA `WITH/FROM` is expected here, **not** circular (CLAUDE.md IBA note); do not
   mark it `CIRCULAR_OR_REDUNDANT`.
2. **Can you name the two ends?** From literature or the lineage, identify the
   partners this protein would bridge. If yes, the adaptor claim is real —
   `ACCEPT` if core, `KEEP_AS_NON_CORE` if peripheral, and name the partners in
   `reason`. If the evidence shows a *more specific* child (the named partners fix
   the branch), `MODIFY` to it.
3. **If the ends cannot be named, handle by tier — and never REMOVE merely for
   being electronic** (CLAUDE.md): a challenge needs a biological argument.
   - **Tier 1 (IBA):** argue the **node placement**, not a similarity score — is
     the target inside the clade that inherited the adaptor function, and is there
     target-specific evidence of loss or divergence? A sound IBA stays. Use the
     taxonomy and failure patterns in [IBA_REVIEW](../IBA_REVIEW.md).
   - **Tiers 2–3 (TreeGrafter / UniRule / Ensembl / ARBA / InterPro2GO):** these
     are unreviewed predictions. `MARK_AS_OVER_ANNOTATED`, or `REMOVE` for a
     demonstrably wrong mapping, **only** with a stated reason — e.g. the gene is a
     divergent paralog that lost the bridging module, carries the domain but its
     partners are absent in this lineage, or is a stable structural subunit rather
     than a transient bridge. ARBA-only and InterPro2GO-only rows are the weakest
     and the first to question; UniRule (curated) and Ensembl (projected from a
     manual annotation) deserve a reading of what they rest on before challenge.

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
remove. A systematic sweep of TreeGrafter/ARBA adaptor over-propagation, if it is
ever wanted, belongs in [IBA_REVIEW](../IBA_REVIEW.md)'s homology-propagation
collection, not here.
