---
title: "Molecular Adaptor Activity Annotation Review"
maturity: SCOPING
tags: [PIPELINE, BIOLOGY_DOMAIN]
species: [human]
sidecars:
  genes: MOLECULAR_ADAPTOR_ACTIVITY/genes.yaml
---

# Molecular Adaptor Activity Annotation Review

**Bottom line (scoping).** `GO:0005515` protein binding records that a protein
sticks to something, not what it does; our curation guidelines tell reviewers
to replace it with an informative molecular function, and for a bridging
protein that replacement is `GO:0060090` molecular adaptor activity (exact
synonym *"binding, bridging"*) or one of its children. This project will work
out the decision rules for making that `protein binding` → adaptor call
consistently: which child term to pick, how to record the two partners being
bridged, how to tell an adaptor from a scaffold / sequestering / carrier
protein, and how much weight to give the large body of phylogenetically
propagated adaptor annotations already in GOA. Nothing has been audited yet —
this page captures the term landscape, the GO guidelines, the propagation
picture, and a seeded phase-1 anchor gene set; no annotations have been
adjudicated yet.

## Scope

In scope: experimental and propagated annotations to `GO:0060090` molecular
adaptor activity and its subtree (chiefly `GO:0030674`
protein-macromolecule adaptor activity and children), and bare `GO:0005515`
protein binding rows that the literature shows to be adaptor/bridging
functions and should be modelled as such.

The **protein-binding policy**
(`src/ai_gene_review/validation/protein_binding_policy.py`) is the governing
machinery here, not merely an out-of-scope exclusion: its
`COMPLIANT_ACTIONS = {MODIFY, REMOVE, UNDECIDED, PENDING}` and its docstring
**prefer MODIFY to an informative MF over REMOVE**, so it is exactly what the
`protein binding` → adaptor `MODIFY` in this project runs through. Genuinely
uninformative `GO:0005515` rows with no bridging role are the REMOVE case of the
same policy.

Out of scope: the distinct but neighbouring molecular functions below, each with
its own GO-CAM guideline — a reviewer should not collapse them into "adaptor":

- `GO:0032947` protein-containing complex scaffold activity — this term is
  **outside** the `GO:0030674` branch and is the genuine scaffold exclusion.
  (Note: `GO:0140693` molecular condensate scaffold activity is **inside** the
  adaptor subtree — it `is_a GO:0030674` — so it is in scope as an adaptor child;
  see [CONDENSATES](CONDENSATES.md) for its tested rules, and decision rule 3.)
- protein sequestering activity (guideline `Protein_sequestering_activity`)
- molecular carrier activity (guideline `Molecular_carrier_activity`)

## Term landscape

Root term: **`GO:0060090` molecular adaptor activity** — *"The binding activity
of a molecule that brings together two or more molecules, permitting those
molecules to function in a coordinated way."* Exact synonym **"binding,
bridging"**. Adaptors are **non-catalytic** by definition — with one standing
exception inside the subtree: the SNARE pair `GO:0005484` (now
*helical-bundle zippering fusogenic activity*) and `GO:0005483` sit under
`GO:0030674` yet describe a fusogenic activity, so they are the case where an
"adaptor" subtree term is not merely a passive bridge. Flag them when they come up.

The protein-adaptor workhorse is **`GO:0030674` protein-macromolecule adaptor
activity**, whose 16 children are where a reviewer usually lands:

| Child term | id |
|---|---|
| signaling adaptor activity | GO:0035591 |
| cytoskeletal adaptor activity | GO:0008093 |
| cargo adaptor activity | GO:0140312 |
| autophagy cargo adaptor activity | GO:0160247 |
| enzyme-substrate adaptor activity | GO:0140767 |
| chromatin-protein adaptor activity | GO:0140463 |
| kinetochore adaptor activity | GO:0140483 |
| protein-membrane adaptor activity | GO:0043495 |
| protein-RNA adaptor activity | GO:0140517 |
| guanyl-nucleotide exchange factor adaptor activity | GO:0005091 |
| receptor clustering activity | GO:0141175 |
| molecular condensate scaffold activity | GO:0140693 |
| ubiquitin-like protein reader activity | GO:0140035 |
| microtubule site clamp | GO:1990644 |
| helical-bundle zippering fusogenic activity (was *SNAP receptor activity*) | GO:0005484 |
| soluble NSF attachment protein activity | GO:0005483 |

Relations were read from QuickGO on 2026-11-07; the table may mix direct
children with grandchildren (e.g. `GO:0160247` is under `GO:0140312`, not a
direct child of `GO:0030674`), and the sidecar's `branch_terms` list surfaces 22
`core_adaptor` terms where the experimental evidence actually sits (including
`GO:0035615`, `GO:1990756`) — so when picking a term, prefer the specific
**descendant** the evidence supports, not only these headline children.

> `GO:0035591` signaling adaptor activity: *"…brings together two or more
> molecules in a signaling pathway… Adaptor molecules themselves do not have
> catalytic activity."*

Other direct children of `GO:0060090` outside the protein-macromolecule branch:
`GO:0030533` triplet codon-amino acid adaptor activity (tRNA), `GO:0106260`
DNA-DNA tethering activity, `GO:0140369` dbTF DNA-binding stabilizer activity,
`GO:0140177` membrane-membrane adaptor activity.

## GO annotation guidelines (GO-CAM)

GO maintains dedicated guidelines, available through the Noctua guideline set
(`Molecular_adaptor_activity`, `How_to_annotate_molecular_adaptors`). Key
modelling rules:

- The MF unit is `enables` molecular adaptor activity (or a child).
- Record the bridged partners with **`has input`** (the two-or-more molecules
  the adaptor brings together).
- `part of` the biological process; `occurs in` the cellular component.
- Relation to the downstream activity (captured in GO-CAM, not standard
  annotation):
  - **`directly positively regulates`** when the adaptor activates the
    partner's activity (regulatory adaptor; the canonical TYROBP example).
  - **`provides input for`** when the adaptor simply brings an enzyme together
    with its substrate (non-regulatory).
- In standard (Protein2GO / Noctua form) annotation, MF-to-MF relations are not
  captured: record MF + `has input` partners + BP + CC only.
- Adaptors are non-catalytic — if the protein has its own catalytic activity,
  that is a separate, additional MF.

## Propagation / IBA picture

Adaptor activity is **heavily propagated by homology**, so most existing rows
are computational, not experimental. From the QuickGO annotation-statistics API
(retrieved 2026-11-07; exact queries, URLs and facet counts in
[data/propagation-stats.yaml](MOLECULAR_ADAPTOR_ACTIVITY/data/propagation-stats.yaml)).
The two figures below are over **different roots** (`GO:0030674` vs `GO:0060090`)
and so are not a single comparable breakdown:

- The **`GO:0030674` subtree has 446,453 annotations**, dominated by
  TreeGrafter / PANTHER phylogenetic propagation (48.1% by evidence,
  ECO:0007826); a further ~35% is **assigned by** UniProt (22.6%) + InterPro
  (12.3%) — ARBA/UniRule and sequence-model matches — and GO_Central IBD/IBA is
  4.1% by evidence (ECO:0000318). (The two percentages are from different facets,
  evidence-code vs assigned-by; see the data file.)
- The **full `GO:0060090` tree carries 20,948 IBA annotations (ECO:0000318),
  100% assigned by GO_Central** — manually reviewed phylogenetic inferences
  propagated from an experimentally-characterised ancestor down a PANTHER
  family.

Consequences for review (per the IBA guidance in CLAUDE.md and
[IBA_REVIEW](IBA_REVIEW.md)):

- An IBA `molecular adaptor activity` / `signaling adaptor activity` row is a
  considered phylogenetic judgment, not a pairwise transfer. Challenge the node
  placement, not a similarity score.
- Treat TreeGrafter / ARBA adaptor rows (unreviewed electronic) as predictions
  to confirm against literature and the two partners actually bridged.
- Good MODIFY target: GOA has bare `protein binding`, literature shows the
  protein bridges two named partners → propose the appropriate adaptor child and
  name the `has input` partners in the rationale.
- Watch for over-propagation: a stable structural subunit of a complex is not
  necessarily an adaptor; distinguish adaptor vs scaffold vs sequestering vs
  carrier.

## Phase 1 anchor set

Seeded from QuickGO (2026-11-07): every **human** gene product carrying at least
one **experimental** annotation (evidence under `ECO:0000269` — IDA, IPI, IMP,
IGI, IEP, EXP) to `GO:0060090` or a descendant. 1,289 annotation rows resolve to
**666 distinct gene products**. This is a worklist, not a set of curation
decisions — the full table, grouped by branch and with per-term evidence and
references, is in [genes.yaml](MOLECULAR_ADAPTOR_ACTIVITY/genes.yaml).

Genes are tagged with one or more *branches* so the sub-domains can be scoped
and worked separately. **The branches are a pragmatic surface-role grouping, not
strict `is_a` cuts, and they deliberately cross the ontology:** the whole
`reader` sub-branch nests under `GO:0140463` (itself a `core_adaptor` term), and
`GO:0005078` MAP kinase scaffold activity `is_a GO:0035591` signaling adaptor
(so it is tagged `core_adaptor`, not `scaffold`, despite its "scaffold" name). A
gene may be in more than one branch, so the counts sum above 666:

| Branch | Genes | What it covers |
|---|---:|---|
| `core_adaptor` | 516 | protein-macromolecule / signaling / cargo / enzyme-substrate / ubiquitin-like ligase-substrate adaptors — the primary `protein binding` → adaptor target |
| `reader` | 114 | histone, RNA and ubiquitin/UFM1 modification "reader" activities (epigenetic/RNA readers; a distinct curation domain) |
| `scaffold` | 45 | `GO:0140693` molecular condensate scaffold activity (in-branch; see [CONDENSATES](CONDENSATES.md)) |
| `tether_anchor` | 17 | organelle membrane tether / anchor / docking and chromatin-loop anchoring activities |

178 of the 666 already have a `genes/human/<symbol>/` folder in the repo
(flagged `existing_folder: true` in the sidecar) — these are the natural
starting points, though a folder does not mean the adaptor row was reviewed.
Three genes in this worklist carry a COMPLETE review (flagged `reviewed: true`):
GRB2 (reviewed independently, before this project), and LDLRAP1 and RPTOR
(reviewed here). The `reviewed` flag — not `existing_folder` — is the filter for
picking un-reviewed genes; its semantics are defined in the sidecar's `source`
block.

**Proposed phase-1 cut:** the `core_adaptor` branch (516 genes). The `reader`
branch is large and mechanistically distinct (recognising a modified residue to
recruit downstream machinery) and overlaps the chromatin/epigenetics work, so it
is a candidate for its own phase. Because the branches cut across the ontology
(above), the cut is a work-planning convenience, not an ontological claim; the
`GO:0032947` scaffold exclusion is the only true out-of-branch boundary.

## Decision rules (draft)

1. Bare `protein binding` that is a bridging function → **`MODIFY` with the
   adaptor term in `proposed_replacement_terms`** (the protein-binding policy's
   preferred action). Only when there is no bridging role does the same policy's
   `REMOVE` apply. Note that a single binary interaction (an IPI hit) evidences
   *binding*, not the bridging *activity* — so refine such a row to a specific
   **binding** term the partner supports (e.g. `protein kinase binding`,
   `AP-2 adaptor complex binding`); assert the adaptor *activity* only where an
   assay shows the bridging, and do not stack a second, unsupported adaptor-activity
   row on top of one already present by IDA.
2. Pick the most specific **descendant** of `GO:0030674` the evidence supports
   (the sidecar surfaces 22 `core_adaptor` terms where the experimental evidence
   sits — e.g. `GO:0035615`, `GO:1990756` — beyond the 16 headline children);
   fall back to `GO:0060090` only when nothing more specific fits.
3. Distinguish adaptor from sequestering and carrier activities, and from the
   one true out-of-branch scaffold term `GO:0032947`. `GO:0140693` molecular
   condensate scaffold activity is *inside* the adaptor subtree — defer to
   [CONDENSATES](CONDENSATES.md)'s rules for it rather than excluding it.
4. Name the bridged partners (`has input`) in the review rationale. This is the
   adaptor's inputs, a separate thing from the MF-to-MF relation (`provides input
   for` / `directly positively regulates`) that only a GO-CAM captures; do not
   conflate the two.
5. A general adaptor term (`GO:0030674`) may be kept **beside** a more specific
   child **only** when it covers a *distinct* bridging event the child does not
   (e.g. GRB2 keeps `GO:0030674` for LAT-microcluster organisation separate from
   its RTK/GEF adaptor children; RPTOR keeps it for Rag-GTPase lysosomal
   recruitment separate from its enzyme-substrate adaptor activity). Otherwise a
   parent beside its own descendant is `TOO_GENERAL` — state the distinct event
   or drop the parent.
6. Treat IBA/TreeGrafter adaptor rows as inference: verify the family is
   coherent and the target is not a divergent paralog before `ACCEPT`.

## Plan / open items

- [x] Seed the phase-1 anchor set from QuickGO: 666 human gene products with an
  experimental annotation under the `GO:0060090` subtree, grouped by branch
  ([genes.yaml](MOLECULAR_ADAPTOR_ACTIVITY/genes.yaml)).
- [ ] Add the complementary set: human genes whose GOA carries a bare
  `protein binding` row plus literature evidence of a bridging role (needs
  manual literature triage; not deterministically queryable).
- [ ] Confirm the phase-1 cut (core_adaptor 516 vs. splitting the reader
  branch) and prioritise the 178 genes that already have a review folder.
- [x] Worked example on a reviewed gene: [GRB2](MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md)
  (signaling / RTK / GEF adaptor; 567 `protein binding` rows vs. the adaptor
  function, read through the decision rules).
- [x] Worked example driving a *new* review of a previously unreviewed gene:
  [LDLRAP1 / ARH](MOLECULAR_ADAPTOR_ACTIVITY/worked-example-LDLRAP1.md)
  (clathrin-cargo adaptor; full 90-annotation review now COMPLETE, incl.
  lateral `MODIFY` of two mis-typed signaling-branch adaptor terms).
- [x] Enzyme-substrate adaptor child, new review:
  [RPTOR / Raptor](MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md)
  (mTORC1 substrate-presenting subunit; 170-annotation review now COMPLETE;
  61 `protein binding` rows split by partner into the MTOR kinase vs. TOS-motif
  substrates — the `provides input for` / enzyme-substrate case).
- [ ] Add worked examples for the remaining common children (cytoskeletal,
  ubiquitin-like ligase-substrate).
- [ ] Decide handling of the propagated bulk (IBA vs TreeGrafter/ARBA) for
  adaptor terms; cross-reference [IBA_REVIEW](IBA_REVIEW.md).
- [ ] Add the project card to `pages/projects/index.html` when the project
  leaves SCOPING (the index is manually maintained).

## Sources

- GO-CAM guidelines (Noctua): `Molecular_adaptor_activity`,
  `How_to_annotate_molecular_adaptors` (reviewed 2023-07-20).
- QuickGO terms [GO:0060090](https://www.ebi.ac.uk/QuickGO/term/GO:0060090),
  [GO:0030674](https://www.ebi.ac.uk/QuickGO/term/GO:0030674),
  [GO:0035591](https://www.ebi.ac.uk/QuickGO/term/GO:0035591).
- QuickGO annotation statistics API (evidence-code and assigned-by facets over
  descendant usage).
