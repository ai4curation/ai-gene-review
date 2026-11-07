# Curation Notes for *Variovorax paradoxus* `ppk` (`A0A0H2M4T4`, `VPARA_28600`)

## Overview
- **UniProt Accession:** `A0A0H2M4T4` (`A0A0H2M4T4_VARPD`)
- **Ordered Locus Name:** `VPARA_28600`
- **Gene Symbol:** `ppk`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Polyphosphate kinase 1 (`PPK1`, 710 aa, EC 2.7.4.1) that catalyzes the reversible transfer of the terminal $\gamma$-phosphate of ATP to synthesize long-chain inorganic polyphosphate (`polyP`) in the cytosol (`UniProtKB:A0A0H2M4T4`; species context in [PMID:21183664 Complete genome sequence of the metabolically versatile plant growth-promoting endophyte Variovorax paradoxus S110., "Genomic analysis has revealed multiple metabolic features for autotrophic and heterotrophic lifestyles."]).

## Domain Architecture & Biochemical Mechanism (`UniProtKB:A0A0H2M4T4`)
1. **Conserved Four-Domain PPK1 Architecture:**
   - N-terminal domain (`FT DOMAIN 16..121`, `Pfam:PF02503` / `InterPro:IPR024954`)
   - Head/middle domain (`FT DOMAIN 131..314`, `Pfam:PF13089` / `InterPro:IPR024953`)
   - C1 catalytic domain (`FT DOMAIN 325..503`, `Pfam:PF13090` / `InterPro:IPR003414`)
   - C2 C-terminal domain (`FT DOMAIN 517..683`, `Pfam:PF13090`)
   - Matches full-length `NCBIfam:TIGR03705` / `InterPro:IPR024955` (`polyphosphate kinase 1`) and `HAMAP-Rule:MF_00347`.
2. **Autophosphorylation Active Site (`His441`):**
   - `FT ACT_SITE 441` (`Phosphohistidine intermediate`) and `FT MOD_RES 441` (`Pros-phosphohistidine; by autocatalysis`) within the conserved C1 domain (`UniProtKB:A0A0H2M4T4`).
   - Catalyzes `ATP + (phosphate)n = ADP + (phosphate)n+1` (EC 2.7.4.1), requiring $\text{Mg}^{2+}$ bound at `Glu381` (`FT BINDING 381`) as an essential cofactor.
3. **Prospective Hypothesis on Intracellular Metal & Lanthanide Sequestration:**
   - Whether inorganic polyphosphate granules synthesized by `Ppk` (`VPARA_28600`) sequester divalent transition metals or trivalent lanthanides ($\text{Ln}^{3+}$/REEs) in *Variovorax paradoxus* has not yet been tested experimentally and is recorded as a prospective hypothesis in `suggested_questions` and `suggested_experiments`.

## Review of Existing GOA Annotations
- `GO:0008976` (`polyphosphate kinase activity`, IEA via UniProtKB-EC / InterPro / TreeGrafter) -> **ACCEPT** (core enzymatic activity, EC 2.7.4.1).
- `GO:0006799` (`polyphosphate biosynthetic process`, IEA via UniProtKB-UniRule / InterPro / TreeGrafter) -> **ACCEPT** (core biological process).
- `GO:0009358` (`polyphosphate kinase complex`, IEA via TreeGrafter `PTN000637837`) -> **ACCEPT** (canonical PPK1 kinase complex).

## Proposed New Annotations
- `GO:0005524` (`ATP binding`, `IC`) — `enables`, supported by `FT BINDING 55 /ligand="ATP"` in `UniProtKB:A0A0H2M4T4`.
- `GO:0000287` (`magnesium ion binding`, `IC`) — `enables`, supported by `FT BINDING 381 /ligand="Mg(2+)"` in `UniProtKB:A0A0H2M4T4`.
- `GO:0005829` (`cytosol`, `IC`) — `located_in`, supported by the absence of signal peptides or transmembrane helices in `UniProtKB:A0A0H2M4T4`.
