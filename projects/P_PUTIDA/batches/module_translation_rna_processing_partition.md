---
title: "PSEPK translation/RNA processing functional bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK translation/RNA processing functional bucket partition

Source bucket: `module:translation_rna_processing`

The UniProt keyword/name bucket is heterogeneous. This partition separates true rRNA/tRNA processing, ribosome maturation, translation-factor, RNA decay, aminoacyl-tRNA quality-control, transcription spillover, NRPS spillover, and low-information side contexts before gene-level curation.

| Split | Genes | Module target | Action | Review files | Curated | Asta |
|---|---:|---|---|---:|---:|---:|
| `rrna_modification_methyltransferase_pseudouridine` | 29 | `rrna_modification_ribosome_maturation_boundary` | NEW_SUBMODULE | 29 | 29 | 29 |
| `ribosome_assembly_maturation_hibernation` | 24 | `bacterial_ribosome_maturation_regulation_boundary` | NEW_SUBMODULE | 24 | 24 | 24 |
| `trna_modification_processing` | 30 | `trna_modification_processing_boundary` | NEW_SUBMODULE | 30 | 30 | 30 |
| `ribonuclease_rna_decay_processing_helicases` | 12 | `rna_decay_processing_boundary` | NEW_SUBMODULE | 12 | 12 | 12 |
| `aminoacyl_trna_charging_editing_quality_control` | 11 | `aminoacyl_trna_quality_control_boundary` | NEW_SUBMODULE | 11 | 11 | 11 |
| `translation_factors_ribosome_rescue` | 10 | `translation_factor_ribosome_rescue_boundary` | NEW_SUBMODULE | 10 | 10 | 10 |
| `transcription_rna_polymerase_spillovers` | 6 | `transcription_rna_polymerase_spillover_boundary` | ROUTE_OUT_OF_TRANSLATION | 6 | 6 | 6 |
| `nonribosomal_peptide_synthetase_spillovers` | 4 | `siderophore_biosynthesis_boundary` | REUSE_OR_EXTEND_EXISTING | 4 | 4 | 4 |
| `low_information_rna_binding_or_enzyme_spillovers` | 2 | `translation_rna_processing_spillover_boundary` | DEFER_LOW_EVIDENCE | 2 | 2 | 2 |

## Split details

### rRNA modification methyltransferase and pseudouridine enzymes

- Split id: `rrna_modification_methyltransferase_pseudouridine`
- Proposed module: `rrna_modification_ribosome_maturation_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 29}
- Genes: `rsmG`, `rsmB`, `rsmA`, `rluD`, `rsmC`, `rlmN`, `rlmF`, `PP_1191`, `rsmI`, `rsmH`, `rsuA`, `rsmJ`, `rlmAA`, `rlmD`, `rluC`, `rlmL`, `PP_2110`, `rlmM`, `PP_4306`, `rluB`, `rlmG`, `rlmE`, `rlmH`, `rlmB`, `rlmJ`, `rsmE`, `PP_5019`, `PP_5114`, `rlmI`
- Notes: Rsm/Rlm/Rlu/Rsu-family rRNA methyltransferase and pseudouridine synthase entries, including dual rRNA/tRNA enzymes where the rRNA role is the dominant product-name signal. Curate site-specific RNA modification terms where GOA/domain support is strong, and keep broad RNA binding non-core.

### Ribosome assembly, maturation, hibernation, and ribosomal-protein modification

- Split id: `ribosome_assembly_maturation_hibernation`
- Proposed module: `bacterial_ribosome_maturation_regulation_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 24}
- Genes: `yigZ`, `rimI`, `der`, `darP`, `hpf`, `rimO`, `era`, `rimM`, `prmB`, `PP_1910`, `PP_2956`, `ycaO`, `PP_3810`, `rbfA`, `rimP`, `ybeY`, `rsfS`, `prmA`, `PP_4885`, `PP_4996`, `typA`, `rmf`, `PP_5700`, `PP_5726`
- Notes: Ribosome biogenesis GTPases, maturation factors, hibernation/silencing factors, ribosomal-protein modifiers, and low-information ribosomal subunit interface/S2p fragments. Keep these separate from the already completed 30S/50S structural ribosome modules.

### tRNA modification and processing enzymes

- Split id: `trna_modification_processing`
- Proposed module: `trna_modification_processing_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 30}
- Genes: `mnmG`, `mnmE`, `tsaC`, `tsaD`, `cca`, `cmoM`, `selU`, `trmJ`, `tadA`, `cmoB`, `trmD`, `tsaB`, `tilS`, `truD`, `yfiP`, `ttcA`, `rluA`, `mnmC`, `trhO`, `dusC`, `truA`, `dusA`, `trmK`, `PP_4520`, `trmA`, `truB`, `dusB`, `miaA`, `tsaE`, `trmL`
- Notes: Mnm/Cmo/Tsa/Trm/Dus/Tru/Mia/Ttc/Til/Cca tRNA-modification and tRNA processing enzymes. Curate explicit tRNA modification reactions where supported; avoid generic transferase or RNA-binding terms as core calls.

### Ribonucleases, RNA decay/processing, and RNA helicases

- Split id: `ribonuclease_rna_decay_processing_helicases`
- Proposed module: `rna_decay_processing_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 12}
- Genes: `rnpA`, `rng`, `rnt`, `PP_1840`, `PP_2084`, `rnz`, `PP_4462`, `srmB`, `rnd`, `PP_4720`, `dbpA`, `rph`
- Notes: RNase P/G/T/Z/D/PH, YbeY, DEAD-box RNA helicases, and RraA-like ribonuclease-regulator spillovers. Separate catalytic nuclease/helicase roles from rRNA/tRNA/ribosome-assembly process context.

### Aminoacyl-tRNA charging, editing, amidotransferase, and quality-control enzymes

- Split id: `aminoacyl_trna_charging_editing_quality_control`
- Proposed module: `aminoacyl_trna_quality_control_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 11}
- Genes: `PP_0201`, `PP_0782`, `PP_0784`, `ybaK`, `PP_1091`, `ycfH`, `aat`, `PP_4228`, `gluQ`, `dtd`, `PP_5664`
- Notes: Aminoacyl-tRNA synthetase fragments or specialized synthetases, GatCAB-like amidotransferase subunits, YbaK/Dtd/YcfH deacylases, and Aat tRNA-protein transferase context. Curate aminoacylation/editing functions precisely.

### Translation factors, ribosome rescue, and translational regulation

- Split id: `translation_factors_ribosome_rescue`
- Proposed module: `translation_factor_ribosome_rescue_boundary`
- Recommended action: `NEW_SUBMODULE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 10}
- Genes: `hslR`, `selB`, `ettA`, `ychF`, `pth`, `lepA`, `frr`, `arfB`, `infA`, `smpB`
- Notes: Initiation/elongation/recycling factors, ribosome rescue proteins, translation throttles, and ribosome-associated stress factors. Keep translation regulation/rescue distinct from structural ribosome modules.

### Transcription and RNA-polymerase spillovers

- Split id: `transcription_rna_polymerase_spillovers`
- Proposed module: `transcription_rna_polymerase_spillover_boundary`
- Recommended action: `ROUTE_OUT_OF_TRANSLATION`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 6}
- Genes: `nusB`, `rapA`, `PP_2266`, `PP_4553`, `dksA`, `nusA`
- Notes: Nus antitermination factors, RapA, DksA, an ECF sigma factor, and an RNA-polymerase subunit fragment/candidate. Route these to transcription or regulatory modules rather than translation/RNA-processing modules.

### Non-ribosomal peptide synthetase spillovers

- Split id: `nonribosomal_peptide_synthetase_spillovers`
- Proposed module: `siderophore_biosynthesis_boundary`
- Recommended action: `REUSE_OR_EXTEND_EXISTING`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 4}
- Genes: `pvdD`, `pvdJ`, `pvdI`, `pvdL`
- Notes: Pyoverdine/ferribactin NRPS genes entered this bucket by the string 'non-ribosomal'. They should be routed to siderophore/pyoverdine biosynthesis context, not translation.

### Low-information RNA-binding or enzyme spillovers

- Split id: `low_information_rna_binding_or_enzyme_spillovers`
- Proposed module: `translation_rna_processing_spillover_boundary`
- Recommended action: `DEFER_LOW_EVIDENCE`
- Status: `COMPLETE`
- Curation status counts: {'CURATED': 2}
- Genes: `PP_2182`, `PP_2953`
- Notes: ProQ/FinO and zinc-alcohol-dehydrogenase-like RNA-binding or regulatory spillovers with weak pathway specificity. Keep core functions narrow and do not force them into rRNA/tRNA processing without stronger evidence.
