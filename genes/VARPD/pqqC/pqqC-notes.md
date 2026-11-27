# Curation Notes for *Variovorax paradoxus* `pqqC` (`A0A0H2MDI9`, `VPARA_00940`)

## Overview
- **UniProt Accession:** `A0A0H2MDI9` (`A0A0H2MDI9_VARPD`)
- **Ordered Locus Name:** `VPARA_00940` (encoded between `pqqB` [`VPARA_00950`] and `pqqD` [`VPARA_00930`] in the `pqqBCDE` cluster)
- **Gene Symbol:** `pqqC`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6)
- **Protein Function:** 254-amino-acid pyrroloquinoline-quinone synthase (`PqqC`, EC 1.3.3.11, `RHEA:10692`; `HAMAP-Rule:MF_00654`, `InterPro:IPR011845`, `NCBIfam:TIGR02111`) that catalyzes the terminal ring cyclization and eight-electron, eight-proton oxidation of AHQQ to mature PQQ (`UniProtKB:A0A0H2MDI9`).

## Biochemical Mechanism & Pathway Context
- PqqC is one of the five obligatory gene products (`PqqA-E`) for bacterial PQQ biosynthesis ([PMID:22324760 Distribution and properties of the genes encoding the biosynthesis of the bacterial cofactor, pyrroloquinoline quinone., "A total of five gene products, PqqA, PqqB, PqqC, PqqD, and PqqE, are identified as being obligatory for PQQ production."]).
- Catalyzes a cofactor-independent 8-electron, 8-proton oxidation of 3a-(2-amino-2-carboxyethyl)-4,5-dioxo-4,5,6,7,8,9-hexahydroquinoline-7,9-dicarboxylic acid (AHQQ) to PQQ, consuming 3 equivalents of $\text{O}_2$ and yielding 2 $\text{H}_2\text{O}_2$ and 2 $\text{H}_2\text{O}$ ([PMID:32731194 Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone., "PqqC catalyzes an overall eight-electron and eight-proton oxidation on AHQQ in the absence of any organic/metal cofactor, consuming three equivalents of O2 in a single turnover manner."]).
- Pathway context is modeled in [`MODULE:pqq_biosynthesis`](../../../modules/pqq_biosynthesis.yaml).

## Review of Existing GOA Annotations
- `GO:0033732` (`pyrroloquinoline-quinone synthase activity`, IEA via `EC:1.3.3.11` / `RHEA:10692`) -> **ACCEPT** (exact core catalytic function).
- `GO:0018189` (`pyrroloquinoline quinone biosynthetic process`, IEA via `UniProtKB-UniRule:UR000098301`) -> **ACCEPT** (core biological process).

## New Annotations Added
- `GO:0005829` (`cytosol`, `IC`, `located_in`) — soluble 254-residue cytoplasmic enzyme lacking signal peptides or transmembrane helices.
