# Curation Notes for *Variovorax paradoxus* `czcA3` (`A0A0H2MBF7`, `VPARA_44890`)

## Overview
- **UniProt Accession:** `A0A0H2MBF7` (`A0A0H2MBF7_VARPD`)
- **Ordered Locus Name:** `VPARA_44890`
- **Gene Symbol:** `czcA3`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Predicted inner-membrane proton/cation antiporter subunit (`CzcA3`, 1,067 aa) of a heavy-metal efflux resistance-nodulation-division (HME-RND) tripartite efflux pump (`NCBIfam:TIGR00914`, `InterPro:IPR004763`), which couples the proton-motive force across the cytoplasmic membrane to the transmembrane export of monoatomic metal cations (`UniProtKB:A0A0H2MBF7`; species context in [PMID:21183664 Complete genome sequence of the metabolically versatile plant growth-promoting endophyte Variovorax paradoxus S110., "Variovorax paradoxus is a microorganism of special interest due to its diverse metabolic capabilities, including the biodegradation of both biogenic compounds and anthropogenic contaminants."]).

## Domain Architecture & Subfamily Classification (`UniProtKB:A0A0H2MBF7`)
1. **12-Transmembrane HME-RND Pump Topology:**
   - Contains 12 transmembrane $\alpha$-helices (`FT TRANSMEM` spanning residues 10–30, 341–363, 367–385, 396–418, 441–463, 475–498, 539–559, 875–895, 902–921, 926–947, 976–998, 1007–1029) and large periplasmic porter/docking loops (`Pfam:PF00873` `ACR_tran`, `InterPro:IPR001036`, `InterPro:IPR027463`).
2. **Specific Membership in the Heavy-Metal Efflux (HME-RND) CusA/CzcA Subfamily (`InterPro:IPR004763`, `NCBIfam:TIGR00914`):**
   - Crucially, `A0A0H2MBF7` matches `NCBIfam:TIGR00914` (`2A0601: heavy metal efflux pump, CzcA family`) and `InterPro:IPR004763` (`Efflux transporter, RND family, CusA-like`), distinguishing it from hydrophobe/amphiphile (HAE-RND, AcrB/MexB) multidrug/xenobiotic efflux pumps.
   - **Prospective Hypothesis on Substrate Selectivity:** While HME-RND family membership supports monoatomic metal cation export (`GO:0008324`, `GO:0098655`), the specific metal substrate selectivity of `CzcA3` ($\text{Co}^{2+}$, $\text{Zn}^{2+}$, $\text{Cd}^{2+}$, or monovalent $\text{Cu}^{+}/\text{Ag}^{+}$) among the multiple `czcA` paralogs in *V. paradoxus* has not yet been determined experimentally and is captured in `suggested_questions` and `suggested_experiments`.

## Review of Existing GOA Annotations
- `GO:0005886` (`plasma membrane`, IEA via TreeGrafter `PTN002424683` and UniProtKB-SubCell) -> **ACCEPT** (integral inner-membrane RND transporter with 12 TM helices).
- `GO:0016020` (`membrane`, IEA via InterPro / UniProtKB-KW) -> **MODIFY** to `GO:0005886` (`plasma membrane`).
- `GO:0008324` (`monoatomic cation transmembrane transporter activity`, IEA via InterPro `IPR004763`) -> **ACCEPT** (transports monoatomic metal cations across the inner membrane).
- `GO:0022857` (`transmembrane transporter activity`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0008324` (`monoatomic cation transmembrane transporter activity`).
- `GO:0098655` (`monoatomic cation transmembrane transport`, IEA via InterPro `IPR004763`) -> **ACCEPT** (core biological process).
- `GO:0006812` (`monoatomic cation transport`, IEA via GOC-owl) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0055085` (`transmembrane transport`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0042910` (`xenobiotic transmembrane transporter activity`, IEA via TreeGrafter `PTN000682552`) -> **REMOVE** (TreeGrafter over-propagation from multidrug HAE-RND paralogs; `CzcA3` belongs to the inorganic cation HME-RND subfamily `TIGR00914` / `IPR004763`).
- `GO:0042908` (`xenobiotic transport`, IEA via GOC-owl from `GO:0042910`) -> **REMOVE** (derived from the over-propagated `GO:0042910` TreeGrafter annotation).
