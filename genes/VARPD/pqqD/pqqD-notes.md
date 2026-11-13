# Curation Notes for *Variovorax paradoxus* `pqqD` (`A0A0H2M992`, `VPARA_00930`)

## Overview
- **UniProt Accession:** `A0A0H2M992` (`A0A0H2M992_VARPD`)
- **Ordered Locus Name:** `VPARA_00930` (encoded between `pqqC` [`VPARA_00940`] and `pqqE` [`VPARA_00920`] in the `pqqBCDE` cluster)
- **Gene Symbol:** `pqqD`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6)
- **Protein Function:** 98-amino-acid cofactor-less PqqA-binding peptide chaperone (`PqqD`, prototype of the RiPP recognition element [RRE] domain; `HAMAP-Rule:MF_00655`, `InterPro:IPR008792`, `InterPro:IPR022479`, `NCBIfam:TIGR03859`, `Pfam:PF05402`) in pyrroloquinoline quinone (PQQ) biosynthesis (`UniProtKB:A0A0H2M992`).

## Removal of False-Positive `GO:0048038` (`quinone binding`) Annotation
- `InterPro:IPR022479` (`PqqD_bac`) maps `A0A0H2M992` to `GO:0048038` (`quinone binding`) via `GO_REF:0000002`.
- This is a well-documented InterPro2GO error (also removed in `PSEPK/pqqD1`): PqqD does **not** bind mature PQQ or any quinone cofactor. As demonstrated by Latham et al. 2015 ([PMID:25817994 PqqD is a novel peptide chaperone that forms a ternary complex with the radical S-adenosylmethionine protein PqqE in the pyrroloquinoline quinone biosynthetic pathway., "Moreover, using SPR and isothermal calorimetry techniques, we establish for the first time that MePqqD binds MePqqA tightly (KD ∼200 nm)."]), Barr et al. 2016 ([PMID:26961875 Demonstration That the Radical S-Adenosylmethionine (SAM) Enzyme PqqE Catalyzes de Novo Carbon-Carbon Cross-linking within a Peptide Substrate PqqA in the Presence of the Peptide Chaperone PqqD., "These results indicate that PqqE, in conjunction with PqqD, carries out the first step in PQQ biosynthesis"]), and Zhu & Klinman 2020 ([PMID:32731194 Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone., "The missing factor has turned out to be PqqD, a small, cofactor-less protein that primarily exists as a free protein (and occasionally as a C-terminal fusion protein of PqqC or an N-terminal fusion of PqqE) (Figure 1D).[12]"]), PqqD is a cofactor-less peptide chaperone that binds the unmodified precursor peptide PqqA (`GO:0042277` `peptide binding`) and presents it to PqqE in a 1:1:1 ternary complex.
- Pathway context is modeled in [`MODULE:pqq_biosynthesis`](../../../modules/pqq_biosynthesis.yaml).

## Review of Existing GOA Annotations
- `GO:0018189` (`pyrroloquinoline quinone biosynthetic process`, IEA via `UniProtKB-UniRule:UR000098302`) -> **ACCEPT** (core biological process).
- `GO:0048038` (`quinone binding`, IEA via `InterPro:IPR022479`) -> **REMOVE** (false-positive InterPro2GO mapping; PqqD is a cofactor-less peptide-binding chaperone for PqqA, not a quinone-binding protein).

## New Annotations Added
- `GO:0042277` (`peptide binding`, `ISS` from `PMID:25817994`) — binds the precursor peptide PqqA (`Kd ~ 200 nM`).
- `GO:0005829` (`cytosol`, `IC`, `located_in`) — soluble 98-residue cytosolic monomer that forms the PqqA-PqqD-PqqE complex.
