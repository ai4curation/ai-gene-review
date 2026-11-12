# Curation Notes: *Variovorax paradoxus* TBEA6 `ppx` (`A0A0H2MBK5`, `VPARA_10490`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2MBK5` (`A0A0H2MBK5_VARPD`, unreviewed TrEMBL, 506 aa)
- **Gene Symbol / Locus Tag:** `ppx` / `VPARA_10490`
- **EC Number:** `3.6.1.11` (`exopolyphosphatase`)
- **Family Classification:** Ppx/GppA phosphatase family (`InterPro:IPR030673` `PyroPPase_GppA_Ppx`, `PIRSF:PIRSF001267`, `PANTHER:PTHR30005:SF14` `EXOPOLYPHOSPHATASE`).

## 2. Sequence & Structural Verification (`UniProtKB:A0A0H2MBK5`)
1. **Two-Domain Ppx/GppA Architecture:**
   - `FT DOMAIN 23..307` (`Pfam:PF02541` `Ppx-GppA`, `CDD:cd24053` `ASKHA_NBD_EcPPX-GppA-like`): N-terminal ASKHA (actin-like ATPase) catalytic domain.
   - Preserves the canonical ASKHA phosphate- and $\text{Mg}^{2+}$-binding loops:
     - **P1 motif:** `11-DLGSNSFR-18` (`Asp11-Leu12-Gly13-Ser14-Asn15-Ser16`)
     - **P2 motif:** `142-DIGGRSTE-149` (`Asp142-Ile143-Gly144-Gly145-Arg146-Ser147-Thr148-Glu149`)
   - `FT DOMAIN 315..480` (`Pfam:PF21447` `Ppx-GppA_III`): C-terminal polyP-recognition and processivity domain.
   - Lacks any signal peptide or transmembrane helices; functions in the cytosol (`GO:0005829`).
2. **Role in the Ppk/Ppx Polyphosphate Cycle:**
   - Together with polyphosphate kinase 1 (`ppk`, `VPARA_28600`, `A0A0H2M4T4`), exopolyphosphatase (`ppx`, `VPARA_10490`) governs intracellular inorganic polyphosphate (`polyP`) turnover by hydrolyzing `polyP` chains to orthophosphate ($\text{P}_i$) [PMID:23687963 Accumulation of inorganic polyphosphate enables stress endurance and catalytic vigour in Pseudomonas putida KT2440., "In addition to Ppk, there is another polyP-modifying enzyme: the so-called exopolyphosphatase (Ppx), that is in charge of polyP hydrolysis to Pi (Figure 1A)."].
   - **Prospective Hypothesis on Metal-Phosphate Remobilization:** Whether Ppx-catalyzed hydrolysis of metal-chelated `polyP` granules remobilizes sequestered divalent transition metals or trivalent lanthanides ($\text{Ln}^{3+}$/REEs) in *Variovorax paradoxus* has not been experimentally tested and is noted as a prospective hypothesis.

## 3. Curation Decisions
- **Accepted:**
  - `GO:0004309` (`exopolyphosphatase activity`)
  - `GO:0006798` (`polyphosphate catabolic process`)
- **Too General:**
  - `GO:0016462` (`pyrophosphatase activity`) — subsumed by `GO:0004309` (`exopolyphosphatase activity`).
- **Added (`NEW`, `IC`):**
  - `GO:0005829` (`cytosol`)
