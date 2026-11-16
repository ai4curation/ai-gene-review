---
title: "Partner-Named and Condition-Dependent Protein Binding Terms"
maturity: SCOPING
tags: [OBSOLETION, PIPELINE]
species: [human, mouse, rat]
collections: [GO_TRACKER_BACKLOG]
index_group: GO_TRACKER_BACKLOG
---

# Partner-Named and Condition-Dependent Protein Binding Terms

**Bottom line:** Three GO tracker issues from 2017-2021 deal with the parts
of the protein binding branch that GO decided to thin out:

- terms naming a single partner gene product (tapasin, haptoglobin,
  dystroglycan, kininogen and others);
- "X-dependent" binding terms (calcium-, ATP-, GTP-, copper-, sterol- and
  modification-dependent);
- family-level binding terms such as protein kinase A binding.

Decisions were made: a 2019 consortium meeting agreed that family binding
terms would go and annotations would move to protein binding with the
partner recorded. Little has been carried out. Three terms are obsolete, the
listed ones are live, and nobody owns the rest. In this repo 172 rows on 109
reviewed genes use the terms examined here. The reviews show where these
terms carry information: calmodulin's calcium-dependent target binding, AKAP
scaffolds' PKA regulatory-subunit binding. The rest restate partner identity.
That distinction is what the remaining obsoletions need. Scoped, not
started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#16186](https://github.com/geneontology/go-ontology/issues/16186) | 2018-08-03 | remove gene-product-specific binding terms when the WITH field can carry the partner | 2021-02-12 |
| [go-ontology#20873](https://github.com/geneontology/go-ontology/issues/20873) | 2021-02-12 | obsolete binding terms "not physiologically relevant" (proline-rich, X-dependent) | body last edited by 2025-10-30 |
| [go-ontology#14601](https://github.com/geneontology/go-ontology/issues/14601) | 2017-11-20 | parentage of protein kinase A / PI3K binding; became the record of the family-binding decision | 2019-04-16 |

Thread summaries are as of 2026-11-16, and term states from a go-ontology
checkout of 2026-11-12. Nothing has been posted to these issues.

## Where the threads stand

- **The decision** (#14601, 2019-01-18): "Decision: protein family binding
  terms will be removed from GO." Annotations would go to protein binding
  with the partner in WITH or has_input. A 2019 meeting also agreed to retire
  precomposed "x complex binding" terms. The parentage fix originally asked
  for was never made: GO:0051018 *protein kinase A binding* and GO:0043548
  *phosphatidylinositol 3-kinase binding* are still direct children of
  GO:0005515, and 67 "complex binding" terms remain.
- **#16186.** PomBase proposed "to get rid of these if the "with" field can
  be applied." MGI marked tapasin, opsonin, haptoglobin and dystroglycan
  binding for obsoletion. UCL curators argued for keeping some, for ISS
  transfer and for partners of unknown species. In 2021 an editor agreed to
  proceed step by step. None of the nine terms is obsolete, and several
  gained PRO-based logical definitions instead.
- **#20873.** This came from an ontology jamboree. Done: GO:0047485 protein
  N-terminus binding, GO:0008022 protein C-terminus binding and GO:0031249
  denatured protein binding are obsolete. Live: proline-rich region binding,
  the five X-dependent terms, modification-dependent protein binding (with a
  subtree, 238 experimental rows in October 2025) and phosphoprotein binding
  (207). The issue says nothing about replacements.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py). Terms with no rows
here (tapasin, opsin, opsonin, nodal, sterol-dependent binding) are omitted.

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0030984 kininogen binding | 2 | 1 | 0 | 0 | 2 | 0 | 0 | 0 |  | 0 |
| GO:0034711 inhibin binding | 2 | 2 | 0 | 1 | 0 | 0 | 0 | 1 |  | 0 |
| GO:0031720 haptoglobin binding | 3 | 3 | 0 | 3 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0002162 dystroglycan binding | 11 | 6 | 3 | 7 | 0 | 0 | 0 | 1 |  | 1 |
| GO:1990405 protein antigen binding | 2 | 2 | 1 | 0 | 0 | 0 | 1 | 0 |  | 0 |
| GO:0070064 proline-rich region binding | 15 | 12 | 12 | 1 | 1 | 0 | 0 | 0 | NEW 1 | 7 |
| GO:0043008 ATP-dependent protein binding | 3 | 3 | 0 | 1 | 1 | 1 | 0 | 0 |  | 0 |
| GO:0048306 calcium-dependent protein binding | 42 | 23 | 19 | 16 | 1 | 1 | 1 | 4 |  | 2 |
| GO:0032767 copper-dependent protein binding | 4 | 2 | 0 | 2 | 0 | 0 | 0 | 2 |  | 0 |
| GO:0030742 GTP-dependent protein binding | 12 | 10 | 8 | 4 | 0 | 0 | 0 | 0 |  | 4 |
| GO:0140030 modification-dependent protein binding | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |  | 0 |
| GO:0051219 phosphoprotein binding | 28 | 23 | 3 | 14 | 7 | 1 | 1 | 2 |  | 1 |
| GO:0051018 protein kinase A binding | 20 | 11 | 2 | 5 | 11 | 1 | 0 | 0 | NEW 1 | 0 |
| GO:0043548 phosphatidylinositol 3-kinase binding | 26 | 16 | 10 | 15 | 0 | 0 | 1 | 0 |  | 4 |

What stands out:

- **Where binding is the mechanism, the reviews keep the specific term.**
  - Calmodulins (CALM1-3, human and mouse), CASQ2 and SYN1 ACCEPT
    calcium-dependent protein binding.
  - The AKAPs (AKAP7, AKAP10, AKAIN1) MODIFY protein kinase A binding to the
    more specific GO:0034237 *protein kinase A regulatory subunit binding*.
  - Rho GTPases and effectors (CDC42, RAC1, PARD6A, ARL13B) ACCEPT
    GTP-dependent protein binding.

  These are adaptors and sensors whose job is the binding. #16186's
  critics did not separate them from the rest.
- **Where the term only names the partner, reviews demote it.**
  - All three haptoglobin binding rows (HBA1, HBA2, HBB) are
    KEEP_AS_NON_CORE.
  - Phosphoprotein binding is mostly non-core or MODIFY (14 + 7 of 28 rows).
    The MODIFY rows on SRC, LYN, GRB2 and YWHAB point to phosphotyrosine or
    phosphoserine residue binding.
- **Proline-rich region binding is ACCEPTed and core** on SH3- and WW-domain
  proteins (ABL1, CSK, BAIAP2, YAP1, NEDD4). #20873 calls it "not
  physiologically relevant". These reviews treat it as the informative MF,
  so obsoleting it without a replacement would lose that.

## What gene review can and cannot settle

- **Can settle, per row:** whether the binding is the gene's mechanism (a
  scaffold, sensor or adaptor, with an informative MF available or needed),
  or a partner identity that WITH or has_input can carry. This is the
  replacement mapping #20873 lacks.
- **Can show:** which live terms have no informative MF to fall back on if
  obsoleted. Proline-rich region binding is the clearest case. SH3 domain
  binding and WW domain binding exist for some partners.
- **Cannot settle:** the consortium's policy, which is decided. The open
  question is implementation, and which terms are exceptions.

## Plan

- [ ] For the 172 rows above, record (a) binding-is-mechanism, with the
      informative MF, or (b) partner identity only. Start with
      calcium-dependent, phosphoprotein and proline-rich region binding, the
      largest groups.
- [ ] Check that each class (a) row has, or proposes, an informative MF
      (adaptor, sensor, residue-specific binding) so the obsoletion would not
      lose it.
- [ ] Align with the repo's protein-binding policy
      (`src/ai_gene_review/validation/protein_binding_policy.py`, bare
      GO:0005515 only) and the
      [MOLECULAR_ADAPTOR_ACTIVITY](MOLECULAR_ADAPTOR_ACTIVITY.md) project.
      Should class (b) rows follow the GO:0005515 rule?
- [ ] Summarise the classification for the issue owners. Posting it is the
      project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No edits started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). All three
  threads read in full.
- #14601's own parentage request is pure ontology structure and needs no
  gene review. It is included here because it records the 2019 decision the
  other two issues implement.
