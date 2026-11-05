# Curation Notes for *Variovorax paradoxus* `czcA3` (`A0A0H2MBF7`, `VPARA_44890`)

## Overview
- **UniProt Accession:** `A0A0H2MBF7` (`A0A0H2MBF7_VARPD`)
- **Ordered Locus Name:** `VPARA_44890`
- **Gene Symbol:** `czcA3`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain B4)
- **Protein Function:** Inner-membrane proton/cation antiporter subunit (`CzcA3`, 1,067 aa) of the heavy-metal efflux resistance-nodulation-division (HME-RND) tripartite efflux pump (`CzcCBA`), which couples the proton-motive force across the cytoplasmic membrane to the active extrusion of toxic divalent transition metal cations ($\text{Co}^{2+}$, $\text{Zn}^{2+}$, $\text{Cd}^{2+}$) from the cytoplasm and periplasm to the extracellular medium.

## Domain Architecture & Subfamily Classification (`UniProtKB:A0A0H2MBF7`)
1. **12-Transmembrane HME-RND Pump Topology:**
   - Contains 12 transmembrane $\alpha$-helices (`FT TRANSMEM` spanning residues 10–30, 341–363, 367–385, 396–418, 441–463, 475–498, 539–559, 875–895, 902–921, 926–947, 976–998, 1007–1029) and large periplasmic pore/TolC-docking loops (`Pfam:PF00873` `ACR_tran`, `InterPro:IPR001036`, `InterPro:IPR027463`).
2. **Specific Membership in the Heavy-Metal Efflux (HME-RND) CusA/CzcA Subfamily (`InterPro:IPR004763`, `NCBIFAM:TIGR00914`):**
   - Crucially, `A0A0H2MBF7` matches `NCBIFAM:TIGR00914` (`2A0601: heavy metal efflux pump, CzcA family`) and `InterPro:IPR004763` (`Efflux pump, RND family, CusA/CzcA subfamily`), distinguishing it from hydrophobe/amphiphile (HAE-RND, AcrB/MexB) multidrug/xenobiotic efflux pumps.
   - Annotated in the *Variovorax paradoxus* B4 genome as `Cobalt-zinc-cadmium resistance protein CzcA; Metal cation efflux system protein` (`gene: czcA3`, `VPARA_44890`).

## Review of Existing GOA Annotations
- `GO:0005886` (`plasma membrane`, IEA via TreeGrafter `PTN000682552` and UniProtKB-SubCell) -> **ACCEPT** (integral inner-membrane RND transporter with 12 TM helices).
- `GO:0016020` (`membrane`, IEA via InterPro / UniProtKB-KW) -> **MODIFY** to `GO:0005886` (`plasma membrane`).
- `GO:0008324` (`monoatomic cation transmembrane transporter activity`, IEA via InterPro `IPR004763`) -> **ACCEPT** (transports divalent metal cations across the inner membrane).
- `GO:0022857` (`transmembrane transporter activity`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0008324` (`monoatomic cation transmembrane transporter activity`).
- `GO:0098655` (`monoatomic cation transmembrane transport`, IEA via InterPro `IPR004763`) -> **ACCEPT** (core biological process).
- `GO:0006812` (`monoatomic cation transport`, IEA via GOC-owl) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0055085` (`transmembrane transport`, IEA via InterPro `IPR001036`) -> **MODIFY** to `GO:0098655` (`monoatomic cation transmembrane transport`).
- `GO:0042910` (`xenobiotic transmembrane transporter activity`, IEA via TreeGrafter `PTN000682552`) -> **REMOVE**!
  - **Rationale:** TreeGrafter over-propagated `xenobiotic transmembrane transporter activity` from multidrug efflux paralogs (such as AcrB/MexB in the broad `PTHR32063` RND superfamily). `CzcA3` specifically belongs to the heavy-metal efflux (HME-RND) CusA/CzcA subfamily (`NCBIFAM:TIGR00914`, `InterPro:IPR004763`), which extrudes inorganic divalent metal cations ($\text{Co}^{2+}, \text{Zn}^{2+}, \text{Cd}^{2+}$) rather than organic xenobiotics.
- `GO:0042908` (`xenobiotic transport`, IEA via GOC-owl from `GO:0042910`) -> **REMOVE**!
  - **Rationale:** Derived from the erroneous `GO:0042910` TreeGrafter annotation; `CzcA3` is an inorganic heavy-metal cation efflux pump (`TIGR00914` / `IPR004763`), not a xenobiotic transporter.
