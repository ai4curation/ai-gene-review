# Curation Notes for *Variovorax paradoxus* S110 `fetP` (`C5CNX5`, `FETP_VARPS`, `Vapar_2982`)

## Overview
- **UniProt Accession:** `C5CNX5` (`FETP_VARPS`)
- **Ordered Locus Name:** `Vapar_2982`
- **Gene Symbol:** `fetP`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Probable cytosolic $\text{Fe}^{2+}$-trafficking protein (`FetP` / `YggX`, 90 aa) predicted via HAMAP rule `MF_00686` (`InterPro:IPR007457`) to mediate intracellular iron transactions between iron acquisition and iron-requiring processes such as synthesis and repair of `[Fe-S]` clusters.
- **Disambiguation Note:** `Vapar_2982` (`C5CNX5`) bears the gene symbol `fetP` in UniProt via the YggX Fe(2+)-trafficking family rule (`HAMAP-Rule:MF_00686`) and is distinct from the uncurated periplasmic FetP-like cupredoxin (`Vapar_3862` / `C5CUI1`) encoded adjacent to the variobactin siderophore locus.

## Literature & Domain Evidence
1. **Genomic Context in *Variovorax paradoxus* S110 (`PMID:21183664`, `UniProtKB:C5CNX5`):**
   - Encoded at locus `Vapar_2982` on Chromosome 1 of *Variovorax paradoxus* S110 (`PMID:21183664`), adjacent to the alkanesulfonate utilization cluster (`Vapar_2976` `ssuD`).
2. **Conserved YggX/FetP Domain Architecture (`UniProtKB:C5CNX5`):**
   - `C5CNX5` (`YGGX_VARPS`) is a Swiss-Prot reviewed entry curated under HAMAP rule `MF_00686` (`InterPro:IPR007457`, `Pfam:PF04362`, Fe(2+)-trafficking protein YggX).
   - Binds one $\text{Fe}^{2+}$ ion per monomer (`CC COFACTOR: Name=Fe(2+); Note=Binds 1 Fe(2+) ion per monomer.`) in the cytosol (`CC SUBCELLULAR LOCATION: Cytosol`) and functions in intracellular $\text{Fe}^{2+}$ trafficking to mitigate oxidative damage to `[Fe-S]` clusters (`CC FUNCTION: Plays a role in the protection of iron-sulfur clusters against oxidative damage; acts as an iron-trafficking protein.`).

## Review of Existing GOA Annotations
- `GO:0005506` (`iron ion binding`, IEA via HAMAP / InterPro / UniProtKB-KW) -> **ACCEPT** (core molecular function: binds 1 $\text{Fe}^{2+}$ ion per monomer for cytosolic iron trafficking).
- `GO:0005829` (`cytosol`, IEA via HAMAP / UniProtKB-SubCell) -> **ACCEPT** (cytosolic localization).
- `GO:0034599` (`cellular response to oxidative stress`, IEA via HAMAP `MF_00686`) -> **KEEP_AS_NON_CORE** (protection against oxidative stress and Fenton damage to `[Fe-S]` clusters is a valid physiological consequence of cytosolic $\text{Fe}^{2+}$ sequestration/trafficking).
