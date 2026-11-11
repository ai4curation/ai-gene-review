# Curation Notes: var13 (A0A0N9M354) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0N9M354` (`A0A0N9M354_VARPD`, 261 aa)
- **Gene symbol / GenBank protein:** `var13` (`ALG65348.1`, `EMBL:KT362218`)
- **Organism:** *Variovorax paradoxus* strain P4B (`NCBITaxon:34073`)
- **Function:** Cytoplasmic FhuF-family `[2Fe-2S]` ferric-siderophore reductase (`PF06276` / `TIGR03951` / `IPR008090`).

## Domain Architecture & Physiological Role
- **Domain organization:** FhuF ferric iron reductase domain (`PF06276` / `TIGR03951` / `IPR008090`) with an IucA/IucC-like core fold (residues 66-206) and a verified C-terminal `CC-x(10)-C-x(2)-C` `[2Fe-2S]` cluster-binding motif at residues 222-239 (`LHRQCCLYYLVPRLGYCGACPLSPE`: `Cys222-Cys223`, 10 residues, `Cys234`, 2 residues, `Cys237`). Note that UniProt `FT DOMAIN 66..206` misleadingly labels the `PF06276` match as `"Aerobactin siderophore biosynthesis IucA/IucC-like C-terminal"` (recorded in `source_defects`).
- **Evidence & Comparator Check:** Co-encoded in the *V. paradoxus* P4B `var` cluster (`KT362218`, [PMID:26412281]); catalyzes reductive release of Fe(II) from imported ferric-variobactin hydroxamate complexes in the cytoplasm ([PMID:38590537]). Comparator check against *E. coli* FhuF (`P39405`) confirms that cytoplasmic FhuF-family reductases act strictly downstream of transmembrane siderophore import (`GO:0033214`) and do not mediate membrane translocation; therefore `GO:0033214` is not added as a `NEW` process annotation on `var13`, and a dedicated biological process term for reductive ferric-siderophore iron release is proposed in `proposed_new_terms`.
