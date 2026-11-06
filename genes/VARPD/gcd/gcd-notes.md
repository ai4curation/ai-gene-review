# Curation Notes for *Variovorax paradoxus* `gcd` (`A0A0H2LUW4`, `VPARA_65850`)

## Overview
- **UniProt Accession:** `A0A0H2LUW4` (`A0A0H2LUW4_VARPD`)
- **Ordered Locus Name:** `VPARA_65850`
- **Gene Symbol:** `gcd`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Membrane-bound pyrroloquinoline quinone (PQQ)-dependent glucose dehydrogenase (`mGDH` / `Gcd`, 818 aa, EC 1.1.5.2) that catalyzes the direct oxidation of D-glucose to D-glucono-1,5-lactone at the periplasmic face of the inner membrane, coupling electron transfer to ubiquinone in the respiratory chain (`UniProtKB:A0A0H2LUW4`; genomic context in *V. paradoxus* S110, [PMID:21183664 Complete genome sequence of the metabolically versatile plant growth-promoting endophyte Variovorax paradoxus S110., "Genomic analysis has revealed multiple metabolic features for autotrophic and heterotrophic lifestyles."]).

## Domain Architecture & Biochemical Mechanism (`UniProtKB:A0A0H2LUW4`)
1. **N-Terminal Transmembrane Anchor (residues 14–169):**
   - Contains 5 predicted transmembrane $\alpha$-helices (`FT TRANSMEM 14..38`, `45..63`, `75..98`, `109..133`, `145..169`) corresponding to the conserved membrane-bound PQQ-dependent glucose dehydrogenase N-terminal ubiquinone-binding anchor (`InterPro:IPR017511` `PQQ_mDH`, `NCBIfam:TIGR03074` `PQQ_membr_DH`).
2. **C-Terminal Periplasmic PQQ-Dependent Catalytic Beta-Propeller Domain:**
   - Matches `InterPro:IPR011047` (Quinoprotein alcohol/glucose dehydrogenase beta-propeller fold) and `PANTHER:PTHR32303:SF4` (`QUINOPROTEIN GLUCOSE DEHYDROGENASE`).
   - Catalyzes the reaction: `D-glucose + a quinone = D-glucono-1,5-lactone + a quinol` (EC 1.1.5.2).
   - **Prospective Hypothesis (Not Yet Established in *V. paradoxus*):** Periplasmic/extracellular hydrolysis of D-glucono-1,5-lactone yields D-gluconic acid, a candidate organic-acid lixiviant whose potential contribution to mineral phosphate or rare earth element (REE / lanthanide) solubilization in *V. paradoxus* remains an open experimental question (see `suggested_questions` and `suggested_experiments` in `gcd-ai-review.yaml`).

## Review of Existing GOA Annotations
- `GO:0008876` (`quinoprotein glucose dehydrogenase activity`, IEA via EC 1.1.5.2 and PANTHER `PTN002427004`) -> **ACCEPT** (core catalytic activity of `Gcd`).
- `GO:0048038` (`quinone binding`, IEA via InterPro `IPR017511`) -> **ACCEPT** (binds membrane ubiquinone via the N-terminal 5-TM domain as physiological electron acceptor and PQQ in the periplasmic domain).
- `GO:0016020` (`membrane`, IEA via InterPro `IPR017511`) -> **MODIFY** to `GO:0005886` (`plasma membrane`) (as Gram-negative `Gcd` is an integral inner-membrane protein with 5 N-terminal transmembrane helices).
- `GO:0016491` (`oxidoreductase activity`, IEA via ARBA) -> **TOO_GENERAL** (subsumed by the accepted child term `GO:0008876` `quinoprotein glucose dehydrogenase activity`).
- `GO:0016614` (`oxidoreductase activity, acting on CH-OH group of donors`, IEA via InterPro) -> **TOO_GENERAL** (subsumed by the accepted child term `GO:0008876` `quinoprotein glucose dehydrogenase activity`).

## Proposed New Annotations
- `GO:0019521` (`D-gluconate metabolic process`, `IC`) — `involved_in`, supported by `InterPro:IPR017511` and `NCBIfam:TIGR03074` in `UniProtKB:A0A0H2LUW4` (while `GO:0016020` `membrane` is refined via `MODIFY` to `GO:0005886` `plasma membrane`).
