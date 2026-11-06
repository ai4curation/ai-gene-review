# Curation Notes for *Variovorax paradoxus* `VPARA_00790` (`A0A0H2MDH4`)

## Overview
- **UniProt Accession:** `A0A0H2MDH4` (`A0A0H2MDH4_VARPD`)
- **Ordered Locus Name:** `VPARA_00790` (located on the same contig `JZWI01000001` ~15 genes upstream of the `pqqBCDE` cluster `VPARA_00950`–`VPARA_00920`)
- **Gene Symbol:** `VPARA_00790`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6)
- **Protein Function:** 608-amino-acid periplasmic pyrroloquinoline quinone (PQQ)-dependent methanol/alcohol dehydrogenase [cytochrome c] subunit (`EC 1.1.2.7`; `NCBIfam:TIGR03075`, `InterPro:IPR017512`, `CDD:cd10278`, `Pfam:PF01011`) (`UniProtKB:A0A0H2MDH4`).

## Structural Features & Active-Site Metal Motif Analysis
1. **Periplasmic Eight-Bladed $\beta$-Propeller Quinoprotein (`FT SIGNAL 1..28`, `FT CHAIN 29..608`):**
   - `A0A0H2MDH4` contains a cleavable 28-residue Sec signal peptide (`FT SIGNAL 1..28`) and zero transmembrane helices. The `GO:0016020` (`membrane`) IEA annotation from `InterPro:IPR017512` is a well-known false positive on soluble periplasmic PQQ methanol/alcohol dehydrogenases (also removed in `METEA/xoxF1`) and is **REMOVED** in favor of `GO:0042597` (`periplasmic space`, `IC`).
   - Retains the conserved active-site vicinal disulfide bond (`FT DISULFID 130..131`, `Cys130-Cys131`), PQQ-binding pocket (`FT BINDING 83, 136, 180, 266`), and catalytic proton-acceptor base `Asp328` (`FT ACT_SITE 328`).
2. **Active-Site `Asp328-Phe329-Asp330` (`DFD`) Motif (`PMID:24816778`):**
   - Inspection of the active-site loop in `A0A0H2MDH4` (`321-MTPYDEWDFDGINEM-335`) reveals `Asp328-Phe329-Asp330` (`DFD`), containing the second aspartate (`Asp330`) two residues C-terminal to the catalytic base `Asp328`.
   - As established by Keltjens et al. 2014 ([PMID:24816778 PQQ-dependent methanol dehydrogenases: rare-earth elements make a difference., "While structures of MxaFI- and XoxF-MDH are conserved, also regarding the binding of PQQ, the accommodation of a REE requires the presence of a specific aspartate residue near the catalytic site."]), $\text{Ca}^{2+}$-dependent MxaF dehydrogenases have an alanine at this position (`Asp-X-Ala`), whereas lanthanide/rare-earth-element ($\text{Ln}^{3+}$/REE)-dependent XoxF/ExaF dehydrogenases have a second aspartate (`Asp-X-Asp`) that coordinates the trivalent lanthanide ion.
   - Because automated PIRSR (`PIRSR617512-3`) and InterPro (`IPR017512`) rules transfer `GO:0005509` (`calcium ion binding`) indiscriminately across both $\text{Ca}^{2+}$- and $\text{Ln}^{3+}$-dependent members, and because the metal cofactor of `VPARA_00790` has not yet been assayed experimentally in *V. paradoxus*, `GO:0005509` (`calcium ion binding`) is **MODIFIED** to the parent term `GO:0046872` (`metal ion binding`), and the $\text{Ln}^{3+}$ vs $\text{Ca}^{2+}$ selectivity hypothesis is recorded in `suggested_questions` and `suggested_experiments`.

## Review of Existing GOA Annotations
- `GO:0052933` (`alcohol dehydrogenase (cytochrome c(L)) activity`, IEA via `EC:1.1.2.7`) -> **ACCEPT** (core catalytic activity).
- `GO:0016491` (`oxidoreductase activity`, IEA via ARBA) -> **TOO_GENERAL** (subsumed by `GO:0052933`).
- `GO:0016614` (`oxidoreductase activity, acting on CH-OH group of donors`, IEA via `InterPro:IPR017512`) -> **TOO_GENERAL** (subsumed by `GO:0052933`).
- `GO:0005509` (`calcium ion binding`, IEA via `InterPro:IPR017512`) -> **MODIFY** to `GO:0046872` (`metal ion binding`).
- `GO:0016020` (`membrane`, IEA via `InterPro:IPR017512`) -> **REMOVE** (soluble periplasmic protein with `FT SIGNAL 1..28` and 0 TM helices).

## New Annotations Added
- `GO:0070968` (`pyrroloquinoline quinone binding`, `IC`, `enables`) — supported by `CC COFACTOR` and `FT BINDING 83, 136, 180, 266` in `UniProtKB:A0A0H2MDH4`.
- `GO:0006066` (`alcohol metabolic process`, `IC`, `involved_in`) — supported by `NCBIfam:TIGR03075` (`PQQ_enz_alc_DH`).
- `GO:0042597` (`periplasmic space`, `IC`, `located_in`) — supported by `FT SIGNAL 1..28` and absence of transmembrane helices.
