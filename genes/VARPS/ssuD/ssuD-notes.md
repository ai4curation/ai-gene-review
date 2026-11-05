# Curation Notes for *Variovorax paradoxus* S110 `ssuD` (`C5CNW9`, `Vapar_2976`)

## Overview
- **UniProt Accession:** `C5CNW9` (`C5CNW9_VARPS`)
- **Ordered Locus Name:** `Vapar_2976`
- **Gene Symbol:** `ssuD`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** $\text{FMNH}_2$-dependent alkanesulfonate monooxygenase (`SsuD`, 389 aa, EC 1.14.14.5) that catalyzes the oxidative C–S bond cleavage of aliphatic sulfonates into the corresponding aldehyde and bioavailable sulfite (`SO3(2-)`) during inorganic sulfate limitation in the rhizosphere.

## Literature & Domain Evidence
1. **Genomic Context & Rhizosphere Sulfur Mobilization (`PMID:21183664`, `UniProtKB:C5CNW9`):**
   - In agricultural soils, >95% of total sulfur is bound in organic forms (primarily sulfonates and sulfate esters) that plant roots cannot directly assimilate. *Variovorax paradoxus* S110 encodes an expansive suite of alkanesulfonate and taurine desulfonation systems (`PMID:21183664`), including `ssuD` (`Vapar_2976`), enabling mineralization of soil organosulfonates into plant-available inorganic sulfur.
2. **Conserved Alkanesulfonate Monooxygenase (`SsuD`) Domain Architecture (`UniProtKB:C5CNW9`):**
   - `C5CNW9` matches `NCBIFAM:TIGR01436` / `InterPro:IPR017511` (`alkanesulfonate monooxygenase SsuD`), `PIRSF:PIRSF000908` (`FMNH2-dependent alkanesulfonate monooxygenase`), `PANTHER:PTHR42718` (`ALKANESULFONATE MONOOXYGENASE`), and `Pfam:PF00296` (`Bac_luciferase` TIM-barrel fold, residues 5–318).
   - Catalyzes the two-component monooxygenase reaction (paired with an NADPH-dependent FMN reductase such as `SsuE`):
     `an alkanesulfonate + FMNH2 + O2 = an aldehyde + FMN + H+ + H2O + sulfite` (EC 1.14.14.5).

## Review of Existing GOA Annotations
- `GO:0008726` (`alkanesulfonate monooxygenase activity`, IEA via UniProtKB-EC / InterPro / TreeGrafter) -> **ACCEPT** (core catalytic activity, EC 1.14.14.5).
- `GO:0046306` (`alkanesulfonate catabolic process`, IEA via InterPro `IPR017511` / TreeGrafter `PTN001389533`) -> **ACCEPT** (core biological process).
- `GO:0016705` (`oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen`, IEA via InterPro `IPR011251`) -> **MODIFY** to `GO:0008726` (`alkanesulfonate monooxygenase activity`).

## Proposed New Annotations
- `GO:0010181` (`FMN binding`) — `enables`, supported by `PIRSF:PIRSF000908` (`FMNH2-dependent alkanesulfonate monooxygenase`) and `CC_CATALYTIC_ACTIVITY` in `UniProtKB:C5CNW9`.
- `GO:0005737` (`cytoplasm`) — `located_in`, as `SsuD` is a soluble cytoplasmic TIM-barrel monooxygenase.
