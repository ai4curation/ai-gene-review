# Proteostasis Batch 4 — PN mapping reconciliation

Date: 2026-06-07
Branch: `claude/proteostasis-network-genes-BVKRp`

After reviewing the 30 batch-4 genes (see `batch4_selection_notes.md`), the
independent gene-level decisions were fed back as a QA signal on the PN-to-GO
mappings that had projected onto these genes. The reviews did **not** consume
the PN-projected GO target as evidence (agents worked from UniProt/GOA/
literature), so agreement/disagreement is an independent check on the mappings.

## Corrections (gene-level exclusions added to mapping YAMLs)

These are over-propagations the gene reviews refuted. Each was fixed at the
mapping source via `excluded_subjects`, so the term no longer projects to the
affected genes while remaining valid for the rest of the node's members.

| Mapping node | GO target | Excluded | Evidence |
|---|---|---|---|
| `er_proteostasis.yaml` → `…N-glycosylation system` (group) | GO:0006487 protein N-linked glycosylation | type `…N-glycosylation system\|Lectin chaperone` | CLGN, CALR3 are lectin **chaperones** (calnexin/calreticulin family), not glycosyltransferases; they bind N-glycans but do not catalyze N-linked glycosylation |
| `chaperone_systems.yaml` → `…Peptidyl-prolyl isomerases` (group) and `…\|Cyclophilin type` | GO:0003755 peptidyl-prolyl cis-trans isomerase activity | gene `CWC27` | CWC27 is a catalytically dead cyclophilin pseudo-isomerase; the gene review records GO:0003755 as a `NOT` annotation (PMID:20676357) |

Verified with `report_pn_projected_annotations._mapping_applies` against the
`4.3.11` workbook (DENSE sheet): after the edits, CLGN/CALR3 no longer receive
GO:0006487 and CWC27 no longer receives GO:0003755.

## Confirmations (validating provenance added to mapping YAMLs)

These PN mappings were independently re-derived by the gene reviews; the gene
review files were added as `references` plus a confirmation `notes` on the
node (no behavior change — the mappings still propagate):

| Mapping node | GO target | Confirmed by |
|---|---|---|
| `ubiquitin_proteasome_system.yaml` → Cul4A/Cul4B substrate adaptor | GO:1990756 ubiquitin-like ligase-substrate adaptor activity | COP1 |
| `ubiquitin_proteasome_system.yaml` → Cul4A/Cul4B substrate receptor | GO:1990756 | CRBN, DCAF11 |
| `nuclear_proteostasis.yaml` → Histone chaperone | GO:0140713 histone chaperone activity | CHAF1A, CHAF1B |
| `chaperone_systems.yaml` → HSP90 cochaperone | GO:0051879 Hsp90 protein binding | CDC37L1 |
| `er_proteostasis.yaml` → ER HSP90 cochaperone | GO:0051879 | CNPY3 |

## Notes

- The derived report `reports/pn_projection/pn_projected_candidate_additions.tsv`
  still lists the three now-excluded rows (CLGN/CALR3 GO:0006487, CWC27
  GO:0003755). Regenerating it requires the GOA DuckDB
  (`~/repos/go-db/db/goa_human.ddb`), which is not present in this environment;
  those rows will drop on the next pipeline regeneration. The mapping YAMLs are
  the source of truth and have been corrected.
- All four edited mapping YAMLs pass `linkml-validate` against
  `ext_mapping.yaml`; `test_ext_mapping_schema.py`, `test_pn_mapping_coverage.py`,
  and `test_pn_projection.py` all pass.

## Not changed

- No edits to the PN workbook itself (it is an external resource).
- The V-ATPase `GO:0007042 lysosomal lumen acidification` question is tracked
  separately (follow-up 2).
