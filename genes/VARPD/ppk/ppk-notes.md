# Curation Notes for *Variovorax paradoxus* `ppk` (`A0A0H2M4T4`, `VPARA_28600`)

## Overview
- **UniProt Accession:** `A0A0H2M4T4` (`A0A0H2M4T4_VARPD`)
- **Ordered Locus Name:** `VPARA_28600`
- **Gene Symbol:** `ppk`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6; see species genomic context in [PMID:21183664 "Genomic analysis has revealed multiple metabolic features for autotrophic and heterotrophic lifestyles. These metabolic diversities enable independent survival, as well as a symbiotic lifestyle."])
- **Protein Function:** Polyphosphate kinase 1 (`PPK1`, 710 aa, EC 2.7.4.1) that catalyzes the reversible transfer of the terminal $\gamma$-phosphate of ATP to long-chain inorganic polyphosphate (`polyP`).

## Domain Architecture & Biochemical Mechanism (`UniProtKB:A0A0H2M4T4`)
1. **Conserved Four-Domain PPK1 Architecture:**
   - N-terminal domain (`FT DOMAIN 18..119`, `Pfam:PF13089` `PP_kinase_N` / `InterPro:IPR025198` `PPK_N_dom`, `InterPro:IPR036832` `PPK_N_dom_sf`)
   - Middle domain (`FT DOMAIN 128..310`, `Pfam:PF02503` `PP_kinase` / `InterPro:IPR024953` `PP_kinase_middle`, `InterPro:IPR036830` `PP_kinase_middle_dom_sf`)
   - C1 catalytic domain (`FT DOMAIN 338..501`, `Pfam:PF17941` `PP_kinase_C_1` / `InterPro:IPR041108` `PP_kinase_C_1`)
   - C2 C-terminal domain (`FT DOMAIN 511..674`, `Pfam:PF13090` `PP_kinase_C` / `InterPro:IPR025200` `PPK_C_dom2`)
   - Matches full-length `HAMAP:MF_00347` (`Polyphosphate_kinase`), `NCBIfam:TIGR03705` (`poly_P_kin`), and `InterPro:IPR003414` (`PP_kinase`).
2. **Autophosphorylation Active Site (`His441`):**
   - `FT ACT_SITE 441` (`Phosphohistidine intermediate`) within the conserved C1 domain (`UniProtKB:A0A0H2M4T4`).
   - Catalyzes `ATP + (phosphate)n = ADP + (phosphate)n+1` (EC 2.7.4.1), requiring $\text{Mg}^{2+}$ as a cofactor (`FT BINDING 381`, `ligand="Mg(2+)"`).
3. **Prospective Hypothesis on Intracellular Metal & REE Sequestration:**
   - As a prospective hypothesis (not yet experimentally assayed in *V. paradoxus*), polyanionic polyphosphate chains synthesized by `PPK1` (`VPARA_28600`) may form intracellular granules that chelate divalent transition metals ($\text{Cd}^{2+}, \text{Zn}^{2+}, \text{Co}^{2+}, \text{Ni}^{2+}, \text{Cu}^{2+}$) and trivalent lanthanides ($\text{Ln}^{3+}$), complementing the polyphosphate-mobilizing PPK2 phosphotransferases `ppk2` (`VPARA_00520`, `A0A0H2MPR3`) and `VPARA_50220` (`A0A0H2LUF2`).

## Review of Existing GOA Annotations
- `GO:0008976` (`polyphosphate kinase activity`, IEA via UniProtKB-EC / InterPro / ARBA) -> **ACCEPT** (core enzymatic activity, EC 2.7.4.1).
- `GO:0006799` (`polyphosphate biosynthetic process`, IEA via UniProtKB-UniRule / InterPro) -> **ACCEPT** (core biological process).
- `GO:0009358` (`polyphosphate kinase complex`, IEA via InterPro `IPR003414`) -> **ACCEPT** (canonical PPK1 oligomeric kinase complex).

## Proposed New Annotations
- `GO:0005524` (`ATP binding`) — `enables`, supported by `FT BINDING 55` (`ligand="ATP"`) in `UniProtKB:A0A0H2M4T4`.
- `GO:0000287` (`magnesium ion binding`) — `enables`, supported by `FT BINDING 381` (`ligand="Mg(2+)"`) in `UniProtKB:A0A0H2M4T4`.
- `GO:0005829` (`cytosol`) — `located_in`, supported by `CC -!- FUNCTION` in `UniProtKB:A0A0H2M4T4`.
