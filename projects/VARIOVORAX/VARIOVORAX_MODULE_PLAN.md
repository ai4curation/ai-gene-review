---
title: Variovorax Module & Gene Review Plan
maturity: IN_PROGRESS
tags:
- BIOLOGY_DOMAIN
species:
- VARPS
- VARPD
autolink_gene_symbols: false
---

# *Variovorax* Enzyme Curation & Module Plan

This document defines the batch curation plan and module architecture for *Variovorax* (`NCBITaxon:34072`) enzymes in `ai-gene-review`, with primary focus on **rhizosphere plant–microbe chemical signaling** and **mineral solubilization and heavy-metal homeostasis**.

## 1. Taxonomic & Proteome Strategy

Following UniProt's 2026_02 reference proteome policy ([PROTEOME_REMOVAL](../PROTEOME_REMOVAL.md)), curation is anchored on active UniProtKB reference proteomes and Swiss-Prot reviewed records:

1. ***Variovorax paradoxus* S110 (`VARPS`, `NCBITaxon:543728`, Proteome `UP000001552`):**
   - Multipartite genome (Chromosome 1 `CP001635` and Chromosome 2 `CP001636`, locus tags `Vapar_0001`–`Vapar_6257`; Han et al. 2011, PMID:21183664) with 234 Swiss-Prot reviewed proteins and 6 retained TrEMBL entries in UniProtKB, notably including the four core proteins of the `iad` auxin-catabolism locus (`Vapar_1489` `C5CSP2` `iadR`, `Vapar_1492` `C5CSP5` `iadC`, `Vapar_1493` `C5CSP6` `iadD`, and `Vapar_1494` `C5CSP7` `iadE`).
   - Also provides Swiss-Prot reviewed anchors for rhizosphere amide turnover (`amiE` `C5CWZ4`), organosulfonate desulfonation (`ssuD` `C5CNW9`), cytosolic YggX-family iron trafficking (`fetP` `C5CNX5`), coenzyme PQQ precursor peptide (`pqqA` `C5CPT7`), and nickel-dependent urea hydrolysis (`ureC` `C5CY00`).
2. ***Variovorax paradoxus* (`VARPD`, `NCBITaxon:34073`, Reference Proteome `UP000035170` / `UP000019090`):**
   - Hosts experimentally characterized Swiss-Prot entries including 1-aminocyclopropane-1-carboxylate deaminase (`acdS`, `Q6J256`) and 3-sulfinopropanoyl-CoA desulfinase (`acd`, `B9U6P5`, `VPARA_05440`), alongside active reference-proteome entries for PQQ biosynthesis (`pqqB` `A0A0H2M8Q2`, `pqqC` `A0A0H2MDI9`, `pqqD` `A0A0H2M992`, `pqqE` `A0A0H2MPV4`), periplasmic PQQ-dependent glucose (`gcd` `A0A0H2LUW4`) and alcohol (`VPARA_00790` `A0A0H2MDH4`) dehydrogenases, TonB-dependent ferric-siderophore uptake (`tonB` `A0A0H2M2E3`, `bfrD1` `A0A0H2M677`), polyphosphate kinase (`ppk` `A0A0H2M4T4`), the `czcCBAIR` heavy-metal RND efflux island (`czcA3` `A0A0H2MBF7`), and taurine dioxygenase (`tauD1` `A0A0H2MHV8`).

---

## 2. Tranche 1 Curation Batches (Completed in PR #6000)

### Batch 1A: Auxin (IAA) Catabolism (`iad` Operon) & Root Growth Inhibition Reversal

*Variovorax* is the keystone genus in plant root microbiomes responsible for degrading excess bacterial and plant indole-3-acetic acid (IAA) to prevent ethylene- and auxin-driven root growth inhibition (Finkel et al. 2020, PMID:32999461; Conway et al. 2022, PMID:36266335; Ma et al. 2023, PMID:37459330).

| Role in Module | Gene Symbol | UniProt / Locus (`VARPS`) | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Catalytic $\alpha$ subunit | `iadD` | `C5CSP6` (`Vapar_1493`) | Indole-3-acetic acid Rieske dioxygenase large subunit | `[2Fe-2S]` Rieske cluster + mononuclear non-heme Fe(II) | `GO:0016708`, `GO:0042437` (indoleacetic acid catabolic process) |
| Structural $\beta$ subunit | `iadE` | `C5CSP7` (`Vapar_1494`) | Indole-3-acetic acid dioxygenase small subunit | $\alpha_3\beta_3$ heterohexamer assembly (`contributes_to` holoenzyme activity) | `GO:0016708` (`contributes_to`), `GO:0042437` |
| Electron transfer | `iadC` | `C5CSP5` (`Vapar_1492`) | Class IA FMN/`[2Fe-2S]` ferredoxin-$\text{NAD}^+$ reductase | FMN (`GO:0010181`) + `[2Fe-2S]` cluster (`GO:0051537`) | `GO:0008860` (ferredoxin-NAD+ reductase activity), `GO:0042437` |
| Transcriptional sensor | `iadR` | `C5CSP2` (`Vapar_1489`) | MarR-family IAA-sensing transcriptional repressor | Direct IAA binding pocket (derepresses `iad` transcription) | `GO:0001217`, `GO:0000976`, `GO:0045892` |

- **Target Module:** [`modules/bacterial_iad_auxin_catabolism.yaml`](../../modules/bacterial_iad_auxin_catabolism.html)

---

### Batch 1B: Ethylene Stress Buffering (`acdS`), Amide Crosstalk (`amiE`), Mineral Acidolysis (`gcd`), Iron Trafficking (`fetP`), PolyP (`ppk`), RND Efflux (`czcA3`) & Organosulfur (`ssuD`, `acd`)

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACC cleavage | `acdS` | `Q6J256` (`VARPD`) | 1-aminocyclopropane-1-carboxylate deaminase (EC 3.5.99.7) | Pyridoxal 5'-phosphate (`GO:0030170`); cleaves ACC to 2-oxobutanoate + $\text{NH}_3$ | `GO:0008660`, `GO:0042217` |
| Amide hydrolysis | `amiE` | `C5CWZ4` (`VARPS`, `Vapar_0135`) | Aliphatic amidase (EC 3.5.1.4) | Glu59-Lys134-Cys166 catalytic triad | `GO:0004040` (amidase activity) |
| Cytosolic Fe(2+) trafficking | `fetP` | `C5CNX5` (`VARPS`, `Vapar_2982`) | Probable $\text{Fe}^{2+}$-trafficking protein | Cytosolic YggX-family iron-binding protein (`HAMAP MF_00686`) | `GO:0005506`, `GO:0006879` |
| Periplasmic PQQ oxidation | `gcd` | `A0A0H2LUW4` (`VARPD`, `VPARA_65850`) | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) | PQQ + divalent cation cofactor; oxidizes D-glucose to D-glucono-1,5-lactone | `GO:0008876`, `GO:0019521` |
| Intracellular polyP synthesis | `ppk` | `A0A0H2M4T4` (`VARPD`, `VPARA_28600`) | Polyphosphate kinase (EC 2.7.4.1) | Polymerizes terminal $\gamma$-phosphate of ATP into long-chain polyP polymers | `GO:0008976`, `GO:0006799` |
| RND metal antiporter | `czcA3` | `A0A0H2MBF7` (`VARPD`, `VPARA_44890`) | Cobalt/zinc/cadmium efflux RND transporter, CzcA family (CzcA3) | Inner-membrane HME-RND proton/cation antiporter subunit | `GO:0008324`, `GO:0098655` |
| Organosulfur desulfonation | `ssuD` | `C5CNW9` (`VARPS`, `Vapar_2976`) | Alkanesulfonate monooxygenase (EC 1.14.14.5) | $\text{FMNH}_2$-dependent TIM-barrel monooxygenase | `GO:0008726`, `GO:0046306` |
| 3SP-CoA cleavage | `acd` | `B9U6P5` (`VARPD`, `VPARA_05440`) | 3-sulfinopropanoyl-CoA desulfinase (EC 3.13.1.4) | Acyl-CoA dehydrogenase fold adapted for non-oxidative C–S cleavage | `GO:0016846`, `GO:0044273` (sulfur compound catabolic process) |

- **Target Module:** [`modules/variovorax_metallophore_metal_homeostasis.yaml`](../../modules/variovorax_metallophore_metal_homeostasis.html)

---

## 3. Tranche 2 Curation Batches (Coenzyme PQQ Biosynthesis, Periplasmic Alcohol Dehydrogenase, TonB-Dependent Siderophore Import, Nickel Urease & Taurine Dioxygenase)

### Batch 2A: De Novo PQQ Biosynthesis (`pqqABCDE`) & Periplasmic Quinoprotein Dehydrogenase (`VPARA_00790`)

*Variovorax paradoxus* synthesizes coenzyme PQQ via the conserved five-gene `pqqABCDE` pathway to supply periplasmic quinoprotein dehydrogenases (`gcd` and `VPARA_00790`) that drive organic-acid mineral weathering and alcohol/volatile organic compound oxidation in the rhizosphere:

| Role in Pathway | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Precursor peptide | `pqqA` | `C5CPT7` (`VARPS`, `Vapar_3057`) | Coenzyme PQQ synthesis protein A (24 aa) | Ribosomally synthesized precursor supplying Glu15 and Tyr19 (`ETSY`) | `GO:0018189` (pyrroloquinoline quinone biosynthetic process), `GO:0005829` (cytosol) |
| Oxygenase / hydroxylase | `pqqB` | `A0A0H2M8Q2` (`VARPD`, `VPARA_00950`) | Coenzyme PQQ synthesis protein B (307 aa) | Non-heme Fe(II)-dependent $\text{O}_2$ hydroxylase + structural $\text{Zn}^{2+}$ site | `GO:0016705`, `GO:0005506`, `GO:0008270`, `GO:0018189` |
| Ring-closing oxidase | `pqqC` | `A0A0H2MDI9` (`VARPD`, `VPARA_00940`) | Pyrroloquinoline-quinone synthase (EC 1.3.3.11, 254 aa) | Cofactorless 8-electron oxidation and ring cyclization of AHQQ to PQQ | `GO:0008986` (pyrroloquinoline-quinone synthase activity), `GO:0018189` |
| Peptide chaperone | `pqqD` | `A0A0H2M992` (`VARPD`, `VPARA_00930`) | PQQ biosynthesis peptide chaperone PqqD (98 aa) | Binds PqqA leader peptide (`GO:0042277`) and presents it to PqqE | `GO:0042277` (peptide binding), `GO:0018189` |
| Radical SAM cyclase | `pqqE` | `A0A0H2MPV4` (`VARPD`, `VPARA_00920`) | PqqA peptide cyclase (EC 1.21.98.4, 383 aa) | Catalytic + auxiliary `[4Fe-4S]` clusters (`GO:0051539`) + SAM (`GO:1904047`) | `GO:0009975` (cyclase activity), `GO:0051539`, `GO:1904047`, `GO:0018189` |
| Periplasmic quinoprotein | `VPARA_00790` | `A0A0H2MDH4` (`VARPD`, `VPARA_00790`) | PQQ-dependent alcohol/methanol dehydrogenase (EC 1.1.2.7, 608 aa) | Periplasmic 8-bladed $\beta$-propeller binding PQQ + active-site $\text{Ca}^{2+}$/$\text{Ln}^{3+}$ | `GO:0052882` (methanol dehydrogenase (cytochrome c) activity), `GO:0070968`, `GO:0046872`, `GO:0042597` |

- **Linked Module:** [`modules/pqq_biosynthesis.yaml`](../../modules/pqq_biosynthesis.html) (`MODULE:pqq_biosynthesis`)

---

### Batch 2B: TonB-Dependent Ferric-Siderophore Import (`tonB`, `bfrD1`), Nickel Urease (`ureC`) & Taurine Dioxygenase (`tauD1`)

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Outer-membrane TBDT | `bfrD1` | `A0A0H2M677` (`VARPD`, `VPARA_25830`) | Outer-membrane TonB-dependent ferric-siderophore receptor BfrD1 (739 aa) | 22-stranded $\beta$-barrel (`PF00593`) + N-terminal plug domain (`PF07715`) | `GO:0015344` (siderophore uptake transmembrane transporter activity), `GO:0033214`, `GO:0009279` |
| Inner-membrane energy transducer | `tonB` | `A0A0H2M2E3` (`VARPD`, `VPARA_25820`) | Inner-membrane proton-motive-force energy transducer TonB (232 aa) | N-terminal TM helix + proline-rich periplasmic linker + C-terminal TonB domain (`PF03544`) | `GO:0031992` (energy transducer activity), `GO:0015891` (siderophore transport), `GO:0005886`, `GO:0030288`, `GO:0098797` |
| Nickel urease $\alpha$ subunit | `ureC` | `C5CY00` (`VARPS`, `Vapar_4243`) | Urease catalytic subunit alpha (EC 3.5.1.5, 572 aa) | Dinuclear $\text{Ni}^{2+}$ center bridged by N6-carboxylysine (Lys222) in $(\text{UreABC})_3$ complex | `GO:0009039` (urease activity), `GO:0016151` (nickel cation binding), `GO:0043419`, `GO:0035550`, `GO:0005829` |
| Taurine dioxygenase | `tauD1` | `A0A0H2MHV8` (`VARPD`, `VPARA_23370`) | Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17, 302 aa) | Mononuclear non-heme Fe(II) (`GO:0005506`) + 2-oxoglutarate + $\text{O}_2$ | `GO:0000908` (taurine dioxygenase activity), `GO:0005506`, `GO:0019529` (taurine catabolic process), `GO:0005829` |

- **Target & Linked Modules:**
  - [`modules/bacterial_tonb_siderophore_import.yaml`](../../modules/bacterial_tonb_siderophore_import.html) (`MODULE:bacterial_tonb_siderophore_import` — new module anchored on `tonB` and `bfrD1`)
  - [`modules/urease_biogenesis_urea_hydrolysis.yaml`](../../modules/urease_biogenesis_urea_hydrolysis.html) (`MODULE:urease_biogenesis_urea_hydrolysis` — linked to `ureC`)
  - [`modules/taurine_uptake_and_desulfonation.yaml`](../../modules/taurine_uptake_and_desulfonation.html) (`MODULE:taurine_uptake_and_desulfonation` — linked to `tauD1`)
