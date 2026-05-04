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

| Level | Total | Mapped | No map | Deferred | Pending | Uncovered |
|-------|------:|-------:|-------:|---------:|--------:|----------:|
| Branch | 9 | 1 | 0 | 0 | 8 | 0 |
| Class | 42 | 11 | 1 | 0 | 30 | 0 |
| Group | 297 | 62 | 1 | 5 | 229 | 0 |
| Type | 800 | 121 | 14 | 4 | 661 | 0 |
| Subtype | 881 | 65 | 14 | 7 | 795 | 0 |

Inventory: 241 curated mappings, 1769 unmapped subjects.

---

## Unmapped Status Policy

Unmapped does not mean a final non-map.

- no mapping appropriate: reviewed, no GO mapping should be made
- deferred: reviewed, but needs better evidence, a better GO term, or narrower handling
- pending review: tracked for coverage, not yet manually analyzed in depth

Current unmapped inventory:

- 30 no mapping appropriate
- 16 deferred
- 1723 pending review

These are tracked directly in the branch mapping YAMLs.

---

## Projection Output

Projection through current propagating mappings produced 2205 unique gene-GO pairs.

GOA source: `~/repos/go-db/db/goa_human.ddb`

| Status | Count |
|--------|------:|
| already in GOA exactly | 703 |
| entailed by GOA closure | 403 |
| more specific than existing GOA | 239 |
| supported by GOA regulation | 77 |
| new to GOA | 767 |
| no local GOA | 16 |

Only the 1083 candidate additions enter manual rereview queues.

---

## Extra Scrutiny Audit

The current mapping set is intentionally conservative, but 172 mappings are
flagged as requiring gene-level review before changing AIGR YAML.

Top flag types:

- 153 contextual or regulatory source labels
- 37 broad or context-losing GO targets
- 15 domain or family metadata labels
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

1. Work the 1083 candidate additions as manual AIGR rereview tasks.
2. Use unusual-propagation audit as a guardrail.
3. Promote only evidence-backed gene-level decisions to review YAML.
4. Keep broad PN membership as project metadata or triage context.
