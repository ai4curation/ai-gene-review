# Curation Notes for *Variovorax paradoxus* `gcd` (`A0A0H2LUW4`, `VPARA_65850`)

## Overview
- **UniProt Accession:** `A0A0H2LUW4` (`A0A0H2LUW4_VARPD`)
- **Ordered Locus Name:** `VPARA_65850`
- **Gene Symbol:** `gcd`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Membrane-bound pyrroloquinoline quinone (PQQ)-dependent glucose dehydrogenase (`mGDH` / `Gcd`, 818 aa, EC 1.1.5.2) that catalyzes the direct oxidation of D-glucose to D-glucono-1,5-lactone at the periplasmic face of the inner membrane, coupling electron transfer to ubiquinone in the respiratory chain and generating extracellular/periplasmic gluconic acid for mineral phosphate solubilization and rare earth element (REE / lanthanide) and metal bioleaching.

## Domain Architecture & Biochemical Mechanism (`UniProtKB:A0A0H2LUW4`)
1. **N-Terminal Transmembrane Anchor (residues 1–150):**
   - Contains 5 predicted transmembrane $\alpha$-helices (`FT TRANSMEM 14..34`, `36..58`, `73..94`, `101..123`, `127..147`) corresponding to the conserved membrane-bound PQQ-dependent glucose dehydrogenase N-terminal ubiquinone-binding anchor (`InterPro:IPR017510`, `TIGRFAMs:TIGR03074`).
2. **C-Terminal Periplasmic PQQ-Dependent Catalytic Beta-Propeller Domain (residues 181–792):**
   - Matches `InterPro:IPR011047` (Quinoprotein alcohol/glucose dehydrogenase beta-propeller fold) and `PANTHER:PTHR43560` (`QUINOPROTEIN GLUCOSE DEHYDROGENASE`).
   - Catalyzes the reaction: `D-glucose + a quinone = D-glucono-1,5-lactone + a quinol` (EC 1.1.5.2).
   - Spontaneous or lactonase-mediated hydrolysis of D-glucono-1,5-lactone yields D-gluconic acid ($pK_a \approx 3.86$), the primary organic acid lixiviant secreted by rhizosphere and mineral-weathering bacteria to solubilize poorly soluble mineral phosphates and mobilize rare earth elements (lanthanides) and transition metals from silicate and phosphate ores.

## Review of Existing GOA Annotations
- `GO:0008876` (`glucose dehydrogenase (PQQ, quinone) activity` / `quinoprotein glucose dehydrogenase activity`, IEA via InterPro `IPR017510` and TreeGrafter `PTN002697387`) -> **ACCEPT** (core catalytic activity of `Gcd`).
- `GO:0048038` (`quinone binding`, IEA via TreeGrafter `PTN002697387`) -> **ACCEPT** (binds membrane ubiquinone via the N-terminal 5-TM domain as physiological electron acceptor).
- `GO:0016020` (`membrane`, IEA via UniProtKB-KW `KW-0472`) -> **MODIFY** to `GO:0005886` (`plasma membrane`) (as Gram-negative `Gcd` is an integral inner-membrane protein with 5 N-terminal transmembrane helices).
- `GO:0016491` (`oxidoreductase activity`, IEA via UniProtKB-KW) -> **MODIFY** to `GO:0008876` (`quinoprotein glucose dehydrogenase activity`).
- `GO:0016614` (`oxidoreductase activity, acting on CH-OH group of donors`, IEA via InterPro `IPR011047`) -> **MODIFY** to `GO:0008876` (`quinoprotein glucose dehydrogenase activity`).

## Proposed New Annotations
- `GO:0005886` (`plasma membrane`) — `located_in`, supported by the 5 transmembrane helices (`FT_TRANSMEM`) and `InterPro:IPR017510` in `UniProtKB:A0A0H2LUW4`.
- `GO:0019595` (`non-phosphorylated glucose catabolic process`) — `involved_in`, supported by `InterPro:IPR017510` and `PANTHER:PTHR43560` in `UniProtKB:A0A0H2LUW4`.
