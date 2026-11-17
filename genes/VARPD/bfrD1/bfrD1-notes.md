# Curation Notes: `bfrD1` (`A0A0H2M677` / `VPARA_25830`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M677` (`A0A0H2M677_VARPD`, unreviewed TrEMBL, 739 aa)
- **Gene Symbol / Locus Tag:** `bfrD1` / `VPARA_25830`
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Neighborhood:** Encoded immediately adjacent to `tonB` (`VPARA_25820`, `A0A0H2M2E3`) on contig `JZWI01000012` (`KLN56277.1` and `KLN56276.1`), forming a linked TonB–TBDT iron-uptake locus [UniProtKB:A0A0H2M677, "DE   SubName: Full=Putative TonB-dependent receptor BfrD {ECO:0000313|EMBL:KLN56277.1};"].
- **Domain Architecture:**
  - Residues 1–17: Sec signal peptide (`SAM:SignalP`)
  - Residues 60–159: N-terminal TonB-dependent receptor plug (cork) domain (`Pfam:PF07715`, `InterPro:IPR012910`)
  - Residues 265–709: C-terminal 22-stranded outer-membrane beta-barrel domain (`Pfam:PF00593`, `InterPro:IPR000531`)
  - Family classification: `InterPro:IPR010105` (`TonB_sidphr_rcpt`), `TIGR01783` (`TonB-siderophor`), `PANTHER:PTHR32552` (`FERRICHROME IRON RECEPTOR-RELATED`).

## 2. Pathway Context & Module Linkage
- **Pathway Module:** [`modules/bacterial_tonb_siderophore_import.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/bacterial_tonb_siderophore_import.yaml) (`MODULE:bacterial_tonb_siderophore_import`).
- **Role in Module:** Step 2 outer-membrane receptor (`bfrD1`), energized by inner-membrane `tonB` (`VPARA_25820`), importing extracellular ferric-siderophore complexes across the outer membrane into the periplasm [PMID:20420522, "TBDTs are large β-barrel proteins (22-stranded) with an N-terminal globular plug domain that occludes the barrel pore. Binding of an iron-siderophore complex on the extracellular face triggers conformational changes that expose a conserved N-terminal segment (the TonB box) in the periplasm."].
- **Cross-Module Link:** Connects downstream of endogenous variobactin lipopeptide siderophore biosynthesis and secretion modeled in [`modules/variovorax_metallophore_metal_homeostasis.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/variovorax_metallophore_metal_homeostasis.yaml) [PMID:26412281, "Variovorax paradoxus S110 and P4B produce variobactin, a photoreactive lipopeptide siderophore containing both catecholate and hydroxamate iron-chelating groups."].

## 3. Review of Existing GOA Annotations
- **`GO:0009279` (`cell outer membrane`, IEA) -> `ACCEPT`:** Supported by the N-terminal signal peptide (1–17) and 22-stranded outer-membrane beta-barrel domain (265–709).
- **`GO:0015344` (`siderophore uptake transmembrane transporter activity`, IEA) -> `ACCEPT`:** Core molecular function capturing inward TonB-dependent ferric-siderophore transport across the outer membrane.
- **`GO:0015343` (`siderophore-iron transmembrane transporter activity`, IEA) -> `TOO_GENERAL`:** Direct `is_a` parent of `GO:0015344`, which is already accepted on this protein.
- **`GO:0033214` (`siderophore-iron import into cell`, IEA) -> `ACCEPT`:** Core biological process.
- **`GO:0015891` (`siderophore transport`, IEA) -> `TOO_GENERAL`:** Ancestor of `GO:0033214`.
- **`GO:0038023` (`signaling receptor activity`, IEA via `InterPro:IPR010105`) -> `REMOVE`:** BfrD1 is 739 aa with its signal peptide at residues 1–17 and plug domain starting at residue 60 (`PF07715`, 60–159). It lacks the N-terminal ~80–100 aa periplasmic FecR-binding anti-sigma signaling extension (`Pfam:PF07660`) required for cell-surface signaling transduction (`GO:0038023`).
