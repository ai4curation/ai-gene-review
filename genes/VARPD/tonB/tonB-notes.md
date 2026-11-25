# Curation Notes: `tonB` (`A0A0H2M2E3` / `VPARA_25820`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M2E3` (`A0A0H2M2E3_VARPD`, unreviewed TrEMBL, 232 aa)
- **Gene Symbol / Locus Tag:** `tonB` / `VPARA_25820`
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Neighborhood:** Encoded on contig `JZWI01000012` (`KLN56276.1`) immediately upstream of the outer-membrane TonB-dependent ferric-siderophore receptor `bfrD1` (`VPARA_25830`, `KLN56277.1`, `A0A0H2M677`) [UniProtKB:A0A0H2M2E3, "DE   SubName: Full=Gram-negative bacterial tonB protein {ECO:0000313|EMBL:KLN56276.1};"].
- **Domain Architecture:**
  - Residues 18–35: N-terminal inner-membrane transmembrane helix (`SAM:Phobius`)
  - Residues 58–143: Proline-rich periplasmic linker (`COMPBIAS` Pro residues at 59–87 and 95–135)
  - Residues 140–232: C-terminal globular TonB domain (`PROSITE:PS52015`, `Pfam:PF03544`, `InterPro:IPR037682`, `TIGR01352`).

## 2. Pathway Context & Module Linkage
- **Pathway Module:** [`modules/bacterial_tonb_siderophore_import.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/bacterial_tonb_siderophore_import.yaml) (`MODULE:bacterial_tonb_siderophore_import`).
- **Role in Module:** Step 1 inner-membrane proton-motive-force energy transducer (`tonB`) within the TonB–ExbB–ExbD complex (`GO:0098797`), extending across the periplasm (`GO:0030288`) to engage the TonB box of outer-membrane TonB-dependent ferric-siderophore receptors such as `bfrD1` (`VPARA_25830`) [PMID:20420522, "The C-terminal domain of TonB (residues ~150-239 in E. coli) crosses the periplasm to bind the TonB box of ligand-loaded TBDTs, mechanically pulling or partially unfolding the plug domain to open a translocation channel for the ferric-siderophore across the outer membrane."].

## 3. Review of Existing GOA Annotations
- **`GO:0031992` (`energy transducer activity`, IEA) -> `ACCEPT`:** Core molecular function.
- **`GO:0005886` (`plasma membrane`, IEA) -> `ACCEPT`:** Anchored in the bacterial inner membrane via residues 18–35.
- **`GO:0030288` (`outer membrane-bounded periplasmic space`, IEA) -> `ACCEPT`:** Spans the periplasm via its proline-rich linker (58–143) and C-terminal domain (140–232).
- **`GO:0098797` (`plasma membrane protein complex`, IEA) -> `ACCEPT`:** Part of the inner-membrane TonB–ExbB–ExbD complex.
- **`GO:0055085` (`transmembrane transport`, IEA) -> `MODIFY` to `GO:0015891` (`siderophore transport`) + `NEW` (`IC`):** Refined to reflect the specific role of the `VPARA_25820`–`VPARA_25830` (`tonB`–`bfrD1`) locus in energizing outer-membrane ferric-siderophore import.
- **`GO:0015031` (`protein transport`, IEA via `UniRule:UR001806740`) -> `REMOVE`:** Automated UniRule over-mapping resulting from colicin/phage parasitism of enteric TonB; physiologically TonB energizes small-molecule nutrient/siderophore import rather than protein translocation.
