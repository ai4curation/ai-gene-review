# Curation Notes for *Variovorax paradoxus* `czcA3` (`A0A0H2MBF7`, `VPARA_44890`)

## Overview
- **UniProt Accession:** `A0A0H2MBF7` (`A0A0H2MBF7_VARPD`)
- **Ordered Locus Name:** `VPARA_44890`
- **Gene Symbol:** `czcA3`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6; see species context in [PMID:21183664 "Variovorax paradoxus is a microorganism of special interest due to its diverse metabolic capabilities, including the biodegradation of both biogenic compounds and anthropogenic contaminants."])
- **Protein Function:** Predicted inner-membrane proton/cation antiporter subunit (`CzcA3`, 1,067 aa) of a heavy-metal efflux resistance-nodulation-division (HME-RND) tripartite efflux pump (`CzcCBA`), which couples the proton-motive force across the cytoplasmic membrane to the active extrusion of monoatomic divalent metal cations.
- **Prospective Hypothesis on Substrate Specificity:** While `NCBIfam:TIGR00914` (`heavy metal efflux pump, CzcA family`) and `InterPro:IPR004763` (`CusA/CzcA subfamily`) strongly support inorganic divalent metal cation efflux ($\text{Co}^{2+}$, $\text{Zn}^{2+}$, $\text{Cd}^{2+}$) by homology to *Cupriavidus metallidurans* CzcA, the exact metal substrate profile of `VPARA_44890` (`czcA3`) among the multiple CzcA paralogs in *V. paradoxus* remains a prospective hypothesis awaiting $\Delta czcA3$ mutant metal-MIC profiling.

## Domain Architecture & Subfamily Classification (`UniProtKB:A0A0H2MBF7`)
1. **12-Transmembrane HME-RND Pump Topology:**
   - Contains 12 transmembrane $\alpha$-helices (`FT TRANSMEM`) and large periplasmic pore/TolC-docking loops (`Pfam:PF00873` `ACR_tran`, `InterPro:IPR001036`, `InterPro:IPR027463`).
2. **Specific Membership in the Heavy-Metal Efflux (HME-RND) CusA/CzcA Subfamily (`InterPro:IPR004763`, `NCBIfam:TIGR00914`):**
   - Crucially, `A0A0H2MBF7` matches `NCBIfam:TIGR00914` (`2A0601: heavy metal efflux pump, CzcA family`) and `InterPro:IPR004763` (`Efflux pump, RND family, CusA/CzcA subfamily`), distinguishing it from hydrophobe/amphiphile (HAE-RND, AcrB/MexB) multidrug/xenobiotic efflux pumps.

## Review of Existing GOA Annotations
- `GO:0005886` (`plasma membrane`, IEA via TreeGrafter `PTN002424683` and UniProtKB-SubCell) -> **ACCEPT** (integral inner-membrane RND transporter with 12 TM helices).
- `GO:0016020` (`membrane`, IEA via InterPro / UniProtKB-KW) -> **MODIFY** to `GO:0005886` (`plasma membrane`).
- `GO:0008324` (`monoatomic cation transmembrane transporter activity`, IEA via InterPro `IPR004763`) -> **ACCEPT** (transports divalent metal cations across the inner membrane).
- `GO:0022857` (`transmembrane transporter activity`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0008324` (`monoatomic cation transmembrane transporter activity`).
- `GO:0098655` (`monoatomic cation transmembrane transport`, IEA via InterPro `IPR004763`) -> **ACCEPT** (core biological process).
- `GO:0006812` (`monoatomic cation transport`, IEA via GOC-owl) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0055085` (`transmembrane transport`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0042910` (`xenobiotic transmembrane transporter activity`, IEA via TreeGrafter `PTN002424683`) -> **REMOVE** (TreeGrafter over-propagation from HAE-RND multidrug efflux paralogs; `CzcA3` belongs to the HME-RND `TIGR00914` / `IPR004763` metal cation efflux subfamily).
- `GO:0042908` (`xenobiotic transport`, IEA via GOC-owl from `GO:0042910`) -> **REMOVE**.
