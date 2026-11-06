# Curation Notes: `tauD1` (`A0A0H2MHV8` / `VPARA_23370`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2MHV8` (`A0A0H2MHV8_VARPD`, unreviewed TrEMBL, 302 aa, EC 1.14.11.17)
- **Gene Symbol / Locus Tag:** `tauD1` / `VPARA_23370`
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Sequence & Active-Site Architecture:**
  - Full-length TauD/TfdA-like $\text{Fe(II)}$/$\alpha$-ketoglutarate-dependent dioxygenase domain (`Pfam:PF02668`, residues 23–294; `InterPro:IPR003819`, `PANTHER:PTHR30468:SF1`) [UniProtKB:A0A0H2MHV8, "DE   SubName: Full=Alpha-ketoglutarate-dependent taurine dioxygenase {ECO:0000313|EMBL:KLN56395.1};"].
  - Conserves the canonical mononuclear non-heme $\text{Fe(II)}$ 2-His-1-carboxylate facial triad (`WHTD` motif at residues 105–108: His106 and Asp108, plus distal His262 in `HFTNFH` at residues 257–262) and the 2-oxoglutarate/sulfonate-binding Arg residues.

## 2. Pathway Context & Module Linkage
- **Existing Reusable Module:** [`modules/taurine_uptake_and_desulfonation.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/taurine_uptake_and_desulfonation.yaml) (`MODULE:taurine_uptake_and_desulfonation`).
- **Complementary Rhizosphere Organosulfonate Module:** Complements the $\text{FMNH}_2$-dependent alkanesulfonate monooxygenase `ssuD` (`VPARA_19220`, curated in Tranche 1 and linked to [`modules/bacterial_alkanesulfonate_uptake_desulfonation.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/bacterial_alkanesulfonate_uptake_desulfonation.yaml)). Together, `TauD1` ($\alpha$-ketoglutarate/$\text{Fe(II)}$-dependent dioxygenase) and `SsuD`/`SsuE` ($\text{FMNH}_2$-dependent two-component monooxygenase) equip *Variovorax paradoxus* TBEA6 to mineralize both taurine and diverse aliphatic sulfonates in sulfate-depleted rhizosphere soils [PMID:9287300, "The Escherichia coli tauD gene is required for the utilization of taurine (2-aminoethanesulfonic acid) as a sulfur source and is expressed only under conditions of sulfate starvation."].

## 3. Review of Existing GOA Annotations
- **`GO:0000908` (`taurine dioxygenase activity`, IEA) -> `ACCEPT`:** Core catalytic activity (EC 1.14.11.17).
- **`GO:0016706` (`2-oxoglutarate-dependent dioxygenase activity`, IEA) -> `TOO_GENERAL`:** Direct `is_a` parent of `GO:0000908`.
- **`GO:0016491` (`oxidoreductase activity`, IEA) -> `TOO_GENERAL`:** Broad ancestor of `GO:0000908`.
- **`GO:0005737` (`cytoplasm`, IEA) -> `MODIFY` to `GO:0005829` (`cytosol`) + `NEW` (`IC`):** Soluble cytosolic enzyme.
- **Added `NEW` (`IC`) `GO:0005506` (`iron ion binding`, `enables`) and `GO:0019529` (`taurine catabolic process`, `involved_in`):** Captures the essential non-heme $\text{Fe(II)}$ cofactor and the biological process missing from GOA.
