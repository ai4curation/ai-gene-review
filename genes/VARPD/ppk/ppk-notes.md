# Curation Notes for *Variovorax paradoxus* `ppk` (`A0A0H2M4T4`, `VPARA_28600`)

## Overview
- **UniProt Accession:** `A0A0H2M4T4` (`A0A0H2M4T4_VARPD`)
- **Ordered Locus Name:** `VPARA_28600`
- **Gene Symbol:** `ppk`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Polyphosphate kinase 1 (`PPK1`, 710 aa, EC 2.7.4.1) that catalyzes the reversible transfer of the terminal $\gamma$-phosphate of ATP to long-chain inorganic polyphosphate (`polyP`), forming intracellular polyphosphate granules that serve as high-capacity chelators for heavy metals and lanthanides/rare earth elements (REEs) as well as a high-energy phosphate reservoir.

## Domain Architecture & Biochemical Mechanism (`UniProtKB:A0A0H2M4T4`)
1. **Conserved Four-Domain PPK1 Architecture:**
   - N-terminal domain (`FT DOMAIN 16..121`, `Pfam:PF02503` / `InterPro:IPR024954`)
   - Head/middle domain (`FT DOMAIN 131..314`, `Pfam:PF13089` / `InterPro:IPR024953`)
   - C1 catalytic domain (`FT DOMAIN 325..503`, `Pfam:PF13090` / `InterPro:IPR003414`)
   - C2 C-terminal domain (`FT DOMAIN 517..683`, `Pfam:PF13090`)
   - Matches full-length `NCBIFAM:TIGR03705` / `InterPro:IPR024955` (`polyphosphate kinase 1`).
2. **Autophosphorylation Active Site (`His441`):**
   - `FT ACT_SITE 441` (`Tele-phosphohistidine intermediate`) and `FT MOD_RES 441` (`Phosphohistidine; by autocatalysis`) within the conserved C1 domain (`UniProtKB:A0A0H2M4T4`).
   - Catalyzes `ATP + (phosphate)n = ADP + (phosphate)n+1` (EC 2.7.4.1), requiring $\text{Mg}^{2+}$ as a cofactor (`CC COFACTOR: Name=Mg(2+)`).
3. **Role in Intracellular Metal & REE Sequestration:**
   - In soil and mine-tailing *Variovorax*, polyphosphate chains synthesized by `PPK1` form polyanionic acidocalcisome/volutin-like granules that sequester divalent transition metals ($\text{Cd}^{2+}, \text{Zn}^{2+}, \text{Co}^{2+}, \text{Ni}^{2+}, \text{Cu}^{2+}$) and trivalent lanthanides ($\text{Ln}^{3+}$), protecting cytoplasmic enzymes from metal toxicity while enabling bioaccumulation.

## Review of Existing GOA Annotations
- `GO:0008976` (`polyphosphate kinase activity`, IEA via UniProtKB-EC / InterPro / TreeGrafter) -> **ACCEPT** (core enzymatic activity, EC 2.7.4.1).
- `GO:0006799` (`polyphosphate biosynthetic process`, IEA via UniProtKB-UniRule / InterPro / TreeGrafter) -> **ACCEPT** (core biological process).
- `GO:0009358` (`polyphosphate kinase complex`, IEA via TreeGrafter `PTN000637837`) -> **ACCEPT** (canonical PPK1 homotetrameric/homodimeric kinase complex).

## Proposed New Annotations
- `GO:0005524` (`ATP binding`) — `enables`, supported by `CC_CATALYTIC_ACTIVITY` and `FT_ACT_SITE` in `UniProtKB:A0A0H2M4T4`.
- `GO:0000287` (`magnesium ion binding`) — `enables`, supported by `CC_COFACTOR` (`Name=Mg(2+)`) in `UniProtKB:A0A0H2M4T4`.
