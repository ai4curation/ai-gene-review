# Research Notes: rat Abitram (UniProtKB:D4AE08)

## 1. Nomenclature, Sequence, and Family Context
- **Official RGD Symbol**: `Abitram` (`RGD:1594560`; synonym `Fam206a`).
- **UniProtKB**: `D4AE08` (`D4AE08_RAT`, unreviewed TrEMBL reference-proteome entry; 193 amino acids, 21,510 Da, sequence version 1). Shares ~95% amino acid sequence identity with mouse `Abitram` (`Q80ZQ9`, also 193 aa).
- **PANTHER Family**: `PANTHER:PTHR13651` (`PROTEIN ABITRAM`), subfamily `PANTHER:PTHR13651:SF0` (`PROTEIN ABITRAM`).

## 2. Direct Experimental Evidence in Rat Primary Hippocampal Neurons
Although `D4AE08` is currently unreviewed (`PE=3`) in UniProtKB and all 31 GOA rows on `D4AE08` arehomology/phylogenetic projections (`IBA` from `PANTHER:PTN000342111` / `PTN000342113`, `ISO` from `MGI:MGI:2677850` by RGD, and Ensembl/ARBA `IEA`), three primary publications directly examined **endogenous rat Simiate (`Abitram`)** in dissociated primary hippocampal cultures prepared from E17–E18 Wistar rat embryos:
1. **Derlig et al. 2013 (`PMID:24349419`, *PLoS ONE*)**:
   - Prepared dissociated primary hippocampal cultures from E17–E18 rat brains (`DIV 1–21`) and stained endogenous rat Simiate alongside neuronal (`MAP2`), glial (`GFAP`), nuclear speckle (`SC35`), and synaptic (`SAP97`, `Gephyrin`, `Synaptophysin`) markers.
   - Demonstrated that endogenous rat Simiate is expressed in both neurons and glia, localizes to somata, nuclei (`GO:0005634`), nuclear clusters/speckles (`GO:0016607`), and `MAP2`-positive dendrites (`GO:0030425`), increases markedly in dendrites and nuclei from `DIV 5–7` onward, and is absent from excitatory and inhibitory synapses.
2. **Derlig et al. 2014 (`PMID:24782708`, *Front Cell Neurosci*)**:
   - In E17–E18 rat primary hippocampal neurons (`DIV 7` and `DIV 14`), endogenous rat Simiate strongly colocalizes with both G-actin (`DNaseI` staining) and F-actin (`phalloidin` staining) in axonal/dendritic growth cones (`GO:0030426`), filopodia tips (`GO:0032433`), and proximal and distal dendrites (`GO:0030425`).
   - Elevated expression of Simiate (`GFP-Simiate`) in developing rat hippocampal neurons (`DIV 6–7`) specifically increased branching and total complexity of proximal dendrites (`GO:0048813` `dendrite morphogenesis`).
3. **2022 FAK1–Simiate Study (`PMID:35787638`, *Sci Rep*)**:
   - Tracked endogenous rat Simiate and `FAK1` (`Ptk2`) across `DIV 1–22` in E17–E18 rat primary hippocampal neurons, showing regulated colocalization in nuclear speckles (`GO:0016607`) and dendrites (`GO:0030425`), and demonstrating that overnight NGF stimulation at `DIV 3` triggers robust recruitment and colocalization of endogenous rat Simiate and `FAK1` in G-actin-rich dendritic growth cones (`GO:0030426`).

## 3. Annotation Review Summary
- All 31 GOA rows (`IBA`, `ISO`, `IEA`) on `D4AE08` are strongly supported by both 95% sequence conservation with biochemically characterized mouse `Abitram` (`Q80ZQ9`) and direct endogenous immunofluorescence/functional assays in E17–E18 rat primary hippocampal neurons (`PMID:24349419`, `PMID:24782708`, `PMID:35787638`):
  - `ACCEPT`: `GO:0003785` (`actin monomer binding`), `GO:0051015` (`actin filament binding`), `GO:0030833` (`regulation of actin filament polymerization`), `GO:0005634` (`nucleus`), `GO:0016607` (`nuclear speck`), `GO:0030027` (`lamellipodium`), `GO:0032433` (`filopodium tip`).
  - `KEEP_AS_NON_CORE`: `GO:0051489` (`regulation of filopodium assembly`), `GO:0048813` (`dendrite morphogenesis`), `GO:0030425` (`dendrite`), `GO:0030426` (`growth cone`).
