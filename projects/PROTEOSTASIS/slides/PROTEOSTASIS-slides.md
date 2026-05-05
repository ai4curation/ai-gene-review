---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

<!-- _class: lead -->

# Human Proteostasis Network
# GO Mapping Review

Manual PN-to-GO propagation with explicit curation status

Chris Mungall | AI-Assisted Gene Review
2026-05-03

---

## Source And Scope

Current completed pass:

- Human Proteostasis Network Annotation 4.3.11
- Release date: 2026-04-17
- Local schema and mappings are keyed to this release

---

## Why Manual Mapping Is Required

The PN workbook is a role taxonomy, not a GO annotation table.

PN rows can mean:

- direct molecular activity
- cellular component membership
- pathway-stage context
- family or domain metadata
- broad proteostasis systems membership

The mapping cycle separates PN membership from GO assertion.

---

## Coverage Completion

Every 2026 PN source code is now accounted for.

Total nodes: 2029. Leaf nodes: 1348.

| Level | Total | Pending | Mapped | Context | No map | Deferred | Missing |
|-------|------:|--------:|-------:|--------:|-------:|---------:|--------:|
| Branch | 9 | 8 | 0 | 1 | 0 | 0 | 0 |
| Class | 42 | 30 | 9 | 2 | 1 | 0 | 0 |
| Group | 297 | 229 | 60 | 2 | 1 | 5 | 0 |
| Type | 800 | 661 | 119 | 2 | 14 | 4 | 0 |
| Subtype | 881 | 795 | 64 | 1 | 14 | 7 | 0 |

Inventory: 2029 subject curation records, one per PN node.

---

## Curation Status Policy

Every PN node has a curator-facing status.

- pending review: accounted for, not yet manually analyzed in depth
- mapped: reviewed and mapped to GO
- context only: GO relationship recorded, but unsafe to propagate
- no mapping: reviewed, no GO mapping should be made
- deferred: reviewed, but blocked by evidence, taxonomy ambiguity, or a term gap

Current curation inventory:

- 1723 pending review
- 252 mapped
- 8 context only
- 30 no mapping
- 16 deferred

These are tracked directly in the branch mapping YAMLs.

---

## Projection Output

Projection through current propagating mappings produced 2197 unique gene-GO pairs.

GOA source: `~/repos/go-db/db/goa_human.ddb`

| Status | Count |
|--------|------:|
| already in GOA exactly | 703 |
| entailed by GOA closure | 403 |
| more specific than existing GOA | 238 |
| supported by GOA regulation | 77 |
| new to GOA | 760 |
| no local GOA | 16 |

Only the 1075 candidate additions enter manual rereview queues.

---

## Extra Scrutiny Audit

The current mapping set is intentionally conservative, but 180 GO-bearing records are
flagged as requiring gene-level review before changing AIGR YAML.

Top flag types:

- 151 contextual or regulatory source labels
- 73 broad or context-losing GO targets
- 44 domain or family metadata labels
- 12 branch/class-level mappings
- 8 `too_broad_to_propagate` mappings excluded from projections

Report: `reports/pn_mapping_audit/unusual_propagations.tsv`

---

## Propagation Lessons

Projection labels are queue labels, not curation decisions.

Examples from rereview:

- `BCAP31`: accepted ERAD pathway projection
- `EDF1`: accepted RQC/PQC term, rejected broad translation terms
- `TOMM20`: rejected generic protein-import projection as broader than existing mitochondrial import annotation
- `HSPA8`: rejected aggrephagy projection in favor of better-supported CMA
- `RAB7A`: rejected fusion term where evidence better supported post-fusion maturation

---

## Risk Areas

Use extra scrutiny for:

- broad Translation branch/class propagation
- mitochondrial protein import buckets
- ALP docking/fusion and maturation labels
- CMA versus aggrephagy boundaries
- UPS ubiquitin/UBL-binding context buckets
- regulator/modulator labels that point to pathway process terms

These should drive expert review, not automatic gene-review edits.

---

## Current Artifacts

Primary files:

- `projects/PROTEOSTASIS/mappings/*.yaml`
- `projects/PROTEOSTASIS/reports/pn_mapping_coverage/`
- `projects/PROTEOSTASIS/reports/pn_projection/`
- `projects/PROTEOSTASIS/reports/pn_mapping_audit/`
- `projects/PROTEOSTASIS/reports/pn_mappings/pn_mappings.xlsx`
- `projects/PROTEOSTASIS/reports/pn_taxonomy_tree/`

HTML page: `pages/projects/PROTEOSTASIS.html`
Browser: `pages/projects/PROTEOSTASIS-tree.html`

---

## Next Work

1. Work the 1075 candidate additions as manual AIGR rereview tasks.
2. Use unusual-propagation audit as a guardrail.
3. Promote only evidence-backed gene-level decisions to review YAML.
4. Keep broad PN membership as project metadata or triage context.
