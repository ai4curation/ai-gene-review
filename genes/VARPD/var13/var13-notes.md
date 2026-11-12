# Curation Notes: var13 (A0A0N9M354) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0N9M354` (`A0A0N9M354_VARPD`, 261 aa)
- **Gene symbol / GenBank protein:** `var13` (`ALG65348.1`, `EMBL:KT362218`)
- **Organism:** *Variovorax paradoxus* strain P4B (`NCBITaxon:34073`)
- **Function:** Cytoplasmic FhuF-family `[2Fe-2S]` ferric-siderophore reductase (`PF06276` / `TIGR03951` / `IPR008090`).

## Domain Architecture & Physiological Role
- **Domain organization:** FhuF ferric iron reductase domain (`PF06276` / `TIGR03951` / `IPR008090`) with an IucA/IucC-like core fold (residues 66-206) and a programmatically verified C-terminal `CC-x(10)-C-x(2)-C` `[2Fe-2S]` cluster-binding motif spanning residues 226-250 (`LHRQCCLYYLVPRLGYCGACPLSPE`; exact motif `CCLYYLVPRLGYCGAC` at residues 230-245: `Cys230`, `Cys231`, 10 residues, `Cys242`, 2 residues, `Cys245`; see `var13-bioinformatics/RESULTS.md`). Note that UniProt `FT DOMAIN 66..206` misleadingly labels the `PF06276` match as `"Aerobactin siderophore biosynthesis IucA/IucC-like C-terminal"` (recorded in `source_defects`).
- **Evidence & Comparator Check:** Co-encoded in the *V. paradoxus* P4B `var` cluster (`KT362218`, [PMID:26412281]); catalyzes reductive release of Fe(II) from imported ferric-variobactin hydroxamate complexes in the cytoplasm ([PMID:38590537]; `FT SIGNAL = 0`, `FT TRANSMEM = 0` in `var13-bioinformatics/RESULTS.md`). Comparator check against *E. coli* FhuF (`P39405`) and ontology check of `GO:0033214` (`siderophore-iron import into cell`, restricted to transmembrane transport/endocytosis) and `GO:0033215` (`reductive iron assimilation`, restricted to extracellular reduction via a cell-surface reductase prior to transport) confirm that cytoplasmic FhuF-family reductases act strictly downstream of membrane translocation; therefore `GO:0033214` is not added on `var13`, and a dedicated biological process term for reductive ferric-siderophore iron release under `GO:0006879` (`intracellular iron ion homeostasis`) is proposed in `proposed_new_terms`.
