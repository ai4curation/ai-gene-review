# Curation Notes: Variovorax paradoxus `iadA` (`A0A0H2MF87`, `VPARA_32210`)

## Summary
- **Gene symbol & strain attribution**: `iadA` (also designated `iotA`; locus tag `VPARA_32210`, 734 aa in *Variovorax paradoxus* strain **TBEA6**, `NCBITaxon:34073`, `Proteomes:UP000035170`; syntenic ortholog of the experimentally characterized *V. paradoxus* strain **CL14** gene 72 / IMG `2643613672`).
- **Operon & regulatory context (`PMID:36266335`)**:
  - First structural gene of the primary `iad` operon, located immediately downstream of the DNA operator site bound by the MarR-family IAA-sensing repressor `IadR` (`MarR_73`) [PMID:36266335, "These data (Fig. 2) demonstrate that MarR_73 functions as a repressor of this locus: in the absence of IAA, MarR_73 binds to a DNA site between MarR_73 (iadR) and iadA to repress expression of the IAA degradation genes. When IAA is present, it binds to MarR_73, releasing MarR_73 from the DNA site to allow expression of the IAA degradation genes downstream."].
  - Phylogenomic profiling across ~180,000 bacterial genomes identifies `iotA/iadA` and `iorB/iadB` as exclusive marker genes of `iad`-like auxin-degrading operons (which degrade IAA through dioxindole-3-acetic acid, isatin, and isatinic acid to anthranilic acid) as opposed to `iac`-like operons [PMID:36266335, "Specifically, for each potential operon, we determined the prevalence of COGs that a priori (Extended Data Fig. 4) showed differential prevalence across the two degrading operons (for example, iacA, iacB and iacI are markers of the iac operon, while iorB/iadB and iotA/iadA are exclusive markers of the iad-like operon)."].
  - The specific oxidized indole intermediate acted upon by the heterodimeric `IadA/IadB` complex in vivo has not yet been biochemically established.
- **Domain architecture (`UniProtKB:A0A0H2MF87`)**:
  - Contains the pyruvate/ferredoxin oxidoreductase N-terminal domain (`IPR002880`), TPP-binding domain (`PF02775` / `IPR011766`, `CDD:cd02008` `TPP_IOR_alpha`), and a C-terminal `[4Fe-4S]` ferredoxin-type cluster-binding domain at residues 630–661 (`PROSITE:PS51379`).
- **Annotation review**:
  - `MODIFY` `GO:0003824` (`catalytic activity`) and `GO:0016491` (`oxidoreductase activity`) to `GO:0016903` (`oxidoreductase activity, acting on the aldehyde or oxo group of donors`), and `ACCEPT` `GO:0030976` (`thiamine pyrophosphate binding`).
  - `NEW` `GO:0051539` (`4 iron, 4 sulfur cluster binding`, `IC`), `GO:0042437` (`indoleacetic acid catabolic process`, `ISS` from `PMID:36266335` and `UniProtKB:A0A0H2MF87`), and `GO:0005829` (`cytosol`, `IC`).
