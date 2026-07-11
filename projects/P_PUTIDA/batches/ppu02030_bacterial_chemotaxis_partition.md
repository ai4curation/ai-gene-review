---
title: "PSEPK ppu02030 Bacterial chemotaxis partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02030: Bacterial chemotaxis partition

KEGG ppu02030 is a bacterial chemotaxis umbrella. The PSEPK primary
set mixes receptor panels, core Che signal transduction, accessory
adaptation proteins, and periplasmic binding proteins that belong first
to transport modules.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `known_named_mcp_receptor_panel` | 9 | `chemotaxis_receptor_panel_boundary` | NEW_SUBMODULE | `mcpH`, `ctpL`, `mcpU`, `mcpG`, `mcpA`, `pcaY`, `mcpP`, `mcpS` |
| `orphan_mcp_aerotaxis_receptors` | 13 | `orphan_mcp_aerotaxis_receptors_boundary` | NEW_SUBMODULE | `PP_0317`, `PP_0584`, `PP_0779`, `PP_1819`, `PP_1940`, `PP_2111`, `ctpH`, `PP_2257` |
| `periplasmic_binding_transport_spillovers` | 7 | `dipeptide_ribose_binding_transport_boundary` | EXISTING_OR_REUSE | `dppA-I`, `dppA-II`, `dppA-III`, `rbsB`, `PP_2757`, `PP_2758`, `dppA-IV` |
| `chemotaxis_core_che_cluster` | 6 | `bacterial_chemotaxis_core_boundary` | NEW_SUBMODULE | `PP_4332`, `PP_4333`, `cheB1`, `cheA`, `cheZ`, `cheY` |
| `chemotaxis_adaptation_accessory` | 6 | `chemotaxis_adaptation_accessory_boundary` | NEW_SUBMODULE | `PP_0802`, `PP_2128`, `PP_3759`, `cheR3`, `cheR2`, `PP_4393` |

## Working Decisions

- Do not curate all 41 primary genes as one bacterial-chemotaxis PR.
- Keep dipeptide, ribose, and sugar-binding proteins with transport
  modules unless there is direct receptor-level chemotaxis evidence.
- Treat orphan MCP/aerotaxis receptors as a boundary receptor panel:
  ligand specificity remains unresolved, but the bucket is now curated
  and represented by `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml`.
- The strongest new chemotaxis-specific batches are the core Che cluster,
  named receptor panel, and adaptation/accessory group.

## Completed Sub-batches

- `chemotaxis_core_che_cluster`: six genes present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/bacterial_chemotaxis_core_boundary.yaml` created,
  validated, and rendered. Asta retrieval was checked for all six genes, but the
  new PP_4332/PP_4333/cheB1 decisions rely mainly on UniProt, GOA,
  domain, and local cluster evidence because Asta did not return
  curation-changing organism-specific papers for these proteins.
- `chemotaxis_adaptation_accessory`: six genes present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/chemotaxis_adaptation_accessory_boundary.yaml` created,
  validated, and rendered. CheR2 is retained as the receptor
  methyltransferase supported by UniProt and PMID:23677992, CheR3 is
  kept as a broad unresolved methyltransferase candidate, and PP_3759
  is retained as a methylesterase while response-regulator
  over-propagation is removed.
- `known_named_mcp_receptor_panel`: nine genes present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/chemotaxis_receptor_panel_boundary.yaml` created,
  validated, and rendered. The panel captures characterized purine,
  amino-acid, polyamine, GABA, short-chain carboxylate, TCA/citrate,
  and aromatic-acid receptors, while CtpL remains a ligand-unresolved
  named MCP candidate.
- `orphan_mcp_aerotaxis_receptors`: thirteen genes present,
  Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` created,
  validated, and rendered. Ligand specificity remains unresolved for
  the generic orphan MCPs, and PP_2111 SNARE-derived electronic
  annotations were removed.

## Next Steps

- Treat ppu02030 chemotaxis sub-batches as complete for this first
  pass: core Che signaling, adaptation/accessory proteins, named
  receptor panel, and orphan MCP/aerotaxis receptor boundary are all
  curated.
- Keep `periplasmic_binding_transport_spillovers` with transport modules
  unless direct receptor-level chemotaxis evidence is selected.
- Run real Falcon module/pathway commands only after a concrete submodule
  is selected; current Edison Falcon access failure mode is HTTP 402.
