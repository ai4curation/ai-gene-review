---
title: "Molecular Adaptor Activity Annotation Review"
maturity: SCOPING
tags: [PIPELINE, BIOLOGY_DOMAIN]
species: [human]
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
this page is a stub capturing the term landscape, the GO guidelines, and the
propagation picture so the audit can be scoped.

## Scope

In scope: experimental and propagated annotations to `GO:0060090` molecular
adaptor activity and its subtree (chiefly `GO:0030674`
protein-macromolecule adaptor activity and children), and bare `GO:0005515`
protein binding rows that the literature shows to be adaptor/bridging
functions and should be modelled as such.

Out of scope: `GO:0005515` rows that are genuinely uninformative with no known
bridging role (those are handled by the protein-binding removal policy,
`src/ai_gene_review/validation/protein_binding_policy.py`), and the distinct
but neighbouring molecular functions below, each of which has its own GO-CAM
guideline — a reviewer should not collapse them into "adaptor":

- scaffold / condensate scaffold (`GO:0140693` molecular condensate scaffold
  activity; `GO:0032947` protein-containing complex scaffold activity)
- protein sequestering activity (guideline `Protein_sequestering_activity`)
- molecular carrier activity (guideline `Molecular_carrier_activity`)

## Term landscape

Root term: **`GO:0060090` molecular adaptor activity** — *"The binding activity
of a molecule that brings together two or more molecules, permitting those
molecules to function in a coordinated way."* Exact synonym **"binding,
bridging"**. Adaptors are **non-catalytic** by definition.

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
| SNAP receptor activity | GO:0005484 |
| soluble NSF attachment protein activity | GO:0005483 |

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
are computational, not experimental. From QuickGO annotation statistics
(descendant usage over `is_a`/`part_of`/`occurs_in`):

- The **`GO:0030674` subtree has ~446,000 annotations**, dominated by
  TreeGrafter / PANTHER phylogenetic propagation (~48%, ECO:0007826) and
  UniProt/InterPro sequence-model matches (~34% combined, ARBA/UniRule etc.);
  GO_Central IBD/IBA is a small slice.
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

## Decision rules (draft)

1. Bare `protein binding` → replace with an adaptor term **only when the
   function is bridging two or more partners**; otherwise apply the
   protein-binding policy / find a different informative MF.
2. Pick the most specific child of `GO:0030674` the evidence supports; fall
   back to `GO:0060090` only when no child fits.
3. Distinguish adaptor from scaffold (`GO:0140693`/`GO:0032947`), sequestering,
   and carrier activities — do not collapse them.
4. Name the bridged partners (`has input`) in the review rationale, even though
   standard annotation does not store the MF-to-MF relation.
5. Treat IBA/TreeGrafter adaptor rows as inference: verify the family is
   coherent and the target is not a divergent paralog before `ACCEPT`.

## Plan / open items

- [ ] Assemble the phase-1 gene set: human proteins whose GOA carries a bare
  `protein binding` row plus literature evidence of a bridging role, and
  human experimental annotations already under `GO:0060090` / `GO:0030674`.
- [ ] Draft worked examples for the common children (signaling, cargo,
  cytoskeletal, enzyme-substrate) tying each to a reviewed gene.
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
