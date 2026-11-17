# Research Notes: zebrafish abitram (UniProtKB:Q1LU93)

## 1. Nomenclature, Sequence, and Family Context
- **Official ZFIN Symbol**: `abitram` (`ZFIN:ZDB-GENE-060503-602`; synonym `fam206a`, ORF names `si:ch211-254e15.2`, `zgc:153072`).
- **UniProtKB**: `Q1LU93` (`ABITM_DANRE`, reviewed Swiss-Prot entry; 177 amino acids, 20,504 Da, sequence version 1).
- **PANTHER Family**: `PANTHER:PTHR13651` (`PROTEIN ABITRAM`), subfamily `PANTHER:PTHR13651:SF0` (`PROTEIN ABITRAM`).
- **Sequence Conservation**: Zebrafish `abitram` (`Q1LU93`) is a 1:1 vertebrate ortholog sharing **68.0%** global Needleman–Wunsch sequence identity (123/181; 69.5% [123/177] ungapped) with human `ABITRAM` (`Q9NX38`), **65.8%** global identity (127/193; 71.8% [127/177] ungapped) with mouse `Abitram` (`Q80ZQ9`), and **66.3%** global identity (128/193; 72.3% [128/177] ungapped) with rat `Abitram` (`D4AE08`) across the `IPR039169` (`Abitram` / `PF01597` `GCV_H`) single-hybrid-motif fold (`genes/human/ABITRAM/ABITRAM-bioinformatics/RESULTS.md`).

## 2. Literature Search & Expression Context
Queries across PubMed and EuropePMC (`"abitram" AND ("zebrafish" OR "Danio")`, `"fam206a" AND ("zebrafish" OR "Danio")`, `"zgc:153072"`, `"si:ch211-254e15.2"`, `"Q1LU93"`) found no gene-specific experimental characterization of zebrafish `abitram` beyond the zebrafish reference genome (`PMID:23594743`) and NIH Zebrafish Gene Collection cDNA sequencing from olfactory epithelium (`BC125852`, `Q1LU93` UniProt `RN [2]`), plus broad embryonic/neural expression (`Bgee:ENSDARG00000070407`, expressed in gastrula and 21 other cell types/tissues including central nervous system). Per `projects/MOD_DESCRIPTIONS.md`, ZFIN does not maintain hand-written curated gene descriptions.

## 3. Annotation Review Summary
All 22 GOA rows on `Q1LU93` derive from PAINT phylogenetic propagation (`IBA` from `PANTHER:PTN000342111` and `PANTHER:PTN000342113`), UniProt sequence-similarity projection (`ISS` from mouse `UniProtKB:Q80ZQ9`), and UniProt SubCell `IEA` mappings. Given conservation of the single-domain `GCV_H/Abitram` fold across jawed vertebrates (65.8%–68.0% global identity [69.5%–72.3% ungapped] to mammalian orthologs; `genes/human/ABITRAM/ABITRAM-bioinformatics/RESULTS.md`) and shared jawed-vertebrate central nervous system neuronal architecture (multipolar arborized dendrites, growth cones, lamellipodia, filopodia, and nuclear speckles):
- **`ACCEPT` (core biochemical & subcellular functions)**:
  - `GO:0003785` (`actin monomer binding`, IBA)
  - `GO:0051015` (`actin filament binding`, IBA)
  - `GO:0030833` (`regulation of actin filament polymerization`, IBA, ISS)
  - `GO:0005634` (`nucleus`, IBA, ISS, IEA)
  - `GO:0016607` (`nuclear speck`, ISS, IEA)
  - `GO:0030027` (`lamellipodium`, IBA, ISS, IEA)
  - `GO:0032433` (`filopodium tip`, IBA, ISS)
- **`KEEP_AS_NON_CORE` (specialized protrusion & neuronal arborization contexts)**:
  - `GO:0051489` (`regulation of filopodium assembly`, IBA, ISS)
  - `GO:0048813` (`dendrite morphogenesis`, IBA, ISS)
  - `GO:0030425` (`dendrite`, IBA, IEA)
  - `GO:0030426` (`growth cone`, ISS, IEA)
- **Nuclear Speckle Mechanism & `GO:0035063` (`nuclear speck organization`) Evaluation**: Existing BP `GO:0035063` (`nuclear speck organization`) and a `GO:0005198` (`structural molecule activity`) proposed child were evaluated and withheld because mammalian STED core-domain enrichment (`PMID:41617053`) and acute speckle compaction upon anti-Simiate antibody blockade (`PMID:24349419`, `PMID:27167171`) do not yet distinguish structural scaffolding from factor recruitment or regulatory maintenance, and zebrafish `abitram` itself lacks direct functional characterization.
