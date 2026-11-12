# Curation Notes: Variovorax paradoxus `iadB` (`A0A0H2LZ92`, `VPARA_32200`)

## Summary
- **Gene symbol & strain attribution**: `iadB` (also designated `iorB`; locus tag `VPARA_32200`, 498 aa in *Variovorax paradoxus* strain **TBEA6**, `NCBITaxon:34073`, `Proteomes:UP000035170`; syntenic ortholog of the experimentally characterized *V. paradoxus* strain **CL14** `iadB` / `iorB` encoded immediately downstream of `gene 72 (iadA)` and upstream of `gene 70 (iadC)` and `gene 69 (iadD)`—inferred by synteny and the Fig. 1a `26436136##` convention as CL14 `gene 71`, IMG `2643613671`—in `PMID:36266335`).
- **Operon & functional context (`PMID:36266335`)**:
  - Encoded immediately downstream of `iadA` (`VPARA_32210`) in the conserved *Variovorax* `iad` operon and forms the beta subunit of the heterodimeric `IadA/IadB` 2-oxoacid/indolepyruvate ferredoxin oxidoreductase complex.
  - Together with `iotA/iadA`, `iorB/iadB` is an exclusive phylogenomic marker distinguishing `iad`-type auxin catabolism operons from `iac`-type operons [PMID:36266335, "Specifically, for each potential operon, we determined the prevalence of COGs that a priori (Extended Data Fig. 4) showed differential prevalence across the two degrading operons (for example, iacA, iacB and iacI are markers of the iac operon, while iorB/iadB and iotA/iadA are exclusive markers of the iad-like operon)."].
  - The specific oxidized indole intermediate processed by `IadA/IadB` in vivo has not yet been biochemically determined.
- **Domain architecture (`UniProtKB:A0A0H2LZ92`)**:
  - Contains an N-terminal pyruvate/ketoisovalerate oxidoreductase catalytic domain (residues 6–186, `PF01558` / `IPR019752`) and a C-terminal `DUF6537` domain (residues 248–458, `PF20169` / `IPR046667`) characteristic of `IorB` (`PTHR43854:SF1` / `IPR052198`).
- **Annotation review**:
  - `MODIFY` `GO:0016491` (`oxidoreductase activity`) to `GO:0016903` (`oxidoreductase activity, acting on the aldehyde or oxo group of donors`), and `ACCEPT` `GO:0016903`.
  - `NEW` `GO:0042437` (`indoleacetic acid catabolic process`, `ISS` from `PMID:36266335` and `UniProtKB:A0A0H2LZ92`) and `GO:0005829` (`cytosol`, `IC`).
