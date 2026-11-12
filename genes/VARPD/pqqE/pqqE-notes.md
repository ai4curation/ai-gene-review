# Curation Notes for *Variovorax paradoxus* `pqqE` (`A0A0H2MPV4`, `VPARA_00920`)

## Overview
- **UniProt Accession:** `A0A0H2MPV4` (`A0A0H2MPV4_VARPD`)
- **Ordered Locus Name:** `VPARA_00920` (submitted as `moaA1`, synonym `pqqE` via `HAMAP-Rule:MF_00660`; located immediately downstream of `pqqD` [`VPARA_00930`] in the `pqqBCDE` cluster `VPARA_00950`–`VPARA_00920`)
- **Gene Symbol:** `pqqE`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6)
- **Protein Function:** 383-amino-acid radical $S$-adenosyl-L-methionine (SAM) SPASM-domain PqqA peptide cyclase (`PqqE`, EC 1.21.98.4, `RHEA:56836`; `HAMAP-Rule:MF_00660`, `InterPro:IPR011843`, `NCBIfam:TIGR02109`, `PANTHER:PTHR11228:SF7`) that catalyzes the initiating intramolecular $\text{C}_\gamma(\text{Glu})\text{–C}_3(\text{Tyr})$ cross-linking of PqqA in the presence of PqqD (`UniProtKB:A0A0H2MPV4`).

## Domain Architecture & Radical SAM Treatment Rule (`projects/RADICAL_SAM.md`)
1. **Radical SAM Core & C-Terminal SPASM Domain:**
   - N-terminal radical SAM core domain (`FT DOMAIN 8..223`, `PROSITE:PS51918`, `Pfam:PF04055`) containing the canonical `CxxxCxxC` motif at `Cys22`, `Cys26`, and `Cys29` (`FT BINDING 22/26/29 /ligand="[4Fe-4S] cluster" /ligand_note="4Fe-4S-S-AdoMet"`), demonstrated by Wecksler et al. 2009 ([PMID:19746930 Pyrroloquinoline quinone biogenesis: demonstration that PqqE from Klebsiella pneumoniae is a radical S-adenosyl-L-methionine enzyme., "Herein we present evidence that PqqE from Klebsiella pneumoniae is a functional member of the radical S-adenosyl-L-methionine (SAM) superfamily, capable of cleaving SAM to methionine and 5'-deoxyadenosine in an uncoupled reaction."]).
   - C-terminal SPASM domain (`Pfam:PF13186`, `InterPro:IPR023885`, `NCBIfam:TIGR04085`) housing two auxiliary iron-sulfur clusters (`AuxI` and `AuxII`) required for radical-mediated Glu-Tyr cross-linking in the ternary PqqA-PqqD-PqqE complex ([PMID:26961875 Demonstration That the Radical S-Adenosylmethionine (SAM) Enzyme PqqE Catalyzes de Novo Carbon-Carbon Cross-linking within a Peptide Substrate PqqA in the Presence of the Peptide Chaperone PqqD., "These results indicate that PqqE, in conjunction with PqqD, carries out the first step in PQQ biosynthesis: a radical-mediated formation of a new carbon-carbon bond between two amino acid side chains on PqqA."]; [PMID:32731194 Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone., "In the presence of reducing reagent and SAM, the [4Fe-4S] cluster in PqqE promotes the cleavage of SAM to 5’-deoxyadenosyl radical to initiate a series of steps culminating in a Glu-Tyr crosslink within PqqA."]).
2. **Alignment with `projects/RADICAL_SAM.md` and `PSEPK/pqqE`:**
   - `GO:0003824` (`catalytic activity`) -> **MODIFY** to `GO:0009975` (`cyclase activity`).
   - `GO:0005506` (`iron ion binding`) -> **MODIFY** to `GO:0051539` (`4 iron, 4 sulfur cluster binding`).
   - `GO:0046872` (`metal ion binding`) -> **MODIFY** to `GO:0051539` (`4 iron, 4 sulfur cluster binding`).
   - `GO:0051536` (`iron-sulfur cluster binding`) -> **MODIFY** to `GO:0051539` (`4 iron, 4 sulfur cluster binding`).
   - `GO:0009975` (`cyclase activity`) -> **ACCEPT** (core MF, with `PqqA peptide cyclase activity` in `proposed_new_terms`).
   - `GO:0051539` (`4 iron, 4 sulfur cluster binding`) -> **ACCEPT** (core cofactor MF).
   - `GO:1904047` (`S-adenosyl-L-methionine binding`) -> **ACCEPT** (core cosubstrate MF).
   - `GO:0018189` (`pyrroloquinoline quinone biosynthetic process`) -> **ACCEPT** (core BP).
   - `GO:0005829` (`cytosol`, `IC`, `located_in`) -> **NEW**.
   - Pathway context is modeled in [`MODULE:pqq_biosynthesis`](../../../modules/pqq_biosynthesis.yaml).
