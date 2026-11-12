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

---

## 4. Tranche 3 Curation Batches (Nickel Urease Structural & Maturation Complex, ExbB-ExbD Siderophore-Import Stator, Tripartite CzcCBA & CzcD Heavy-Metal Efflux, and Exopolyphosphatase Ppx)

### Batch 3A: Nickel-Dependent Urease Structural (`ureA`, `ureB`) & Maturation Accessory Complex (`ureD`, `ureE`, `ureF`, `ureG`)

Completes the cytoplasmic bacterial urease holoenzyme (`(UreABC)3`) and `UreD`-`UreF`-`UreG`/`UreE` metallocenter activation machinery around `ureC` (`C5CY00`, `Vapar_4243`):

| Role in Complex | Gene Symbol | UniProt / Locus | Protein / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gamma structural chain | `ureA` | `C5CXZ7` (`VARPS`, `Vapar_4240`) | Urease subunit gamma (100 aa, HAMAP `MF_00739`) | Trimer-interface structural subunit of `(UreABC)3` | `GO:0005198` (structural molecule activity), `GO:0035550`, `GO:0043419`, `GO:0005737` |
| Beta structural chain | `ureB` | `C5CXZ9` (`VARPS`, `Vapar_4242`) | Urease subunit beta (101 aa, HAMAP `MF_01954`) | Non-catalytic beta chain of `(UreABC)3` | `GO:0005198`, `GO:0035550`, `GO:0043419`, `GO:0005737` |
| Apoprotein scaffold | `ureD` | `C5CVT2` (`VARPS`, `Vapar_3971`) | Urease accessory protein UreD (276 aa, HAMAP `MF_01384`) | Binds apo-UreABC and recruits UreF/UreG | `GO:0018237` (urease activator activity), `GO:0044183`, `GO:0043419`, `GO:0005737` |
| Nickel metallochaperone | `ureE` | `A0A0H2LU38` (`VARPD`, `VPARA_50940`) | Urease accessory protein UreE (200 aa, HAMAP `MF_00822`) | Dimeric Ni(2+) donor with 15-His C-terminal tail (residues 148-200) | `GO:0016151` (nickel cation binding), `GO:0051604` (protein maturation), `GO:0043419`, `GO:0005737` |
| GTPase-gating scaffold | `ureF` | `A0A0H2LZ72` (`VARPD`, `VPARA_50930`) | Urease accessory protein UreF (223 aa, HAMAP `MF_01385`) | Docks UreG onto UreD-apourease and gates GTP hydrolysis | `GO:0018237`, `GO:0030695` (GTPase regulator activity), `GO:0043419`, `GO:0005737` |
| SIMIBI G3E GTPase | `ureG` | `C5CY05` (`VARPS`, `Vapar_4248`) | Urease accessory protein UreG (216 aa, HAMAP `MF_01389`) | P-loop (`24-GPVGSGKT-31`) + `Cys72-Pro73-His74` Ni(2+)-binding site | `GO:0003924` (GTPase activity), `GO:0016151`, `GO:0005525`, `GO:0043419`, `GO:0005737` |

- **Linked Module:** [`modules/urease_biogenesis_urea_hydrolysis.yaml`](../../modules/urease_biogenesis_urea_hydrolysis.html) (`MODULE:urease_biogenesis_urea_hydrolysis`)

---

### Batch 3B: ExbB-ExbD Proton-Channel Motor (`exbB4`, `exbD5`), Tripartite CzcCBA & CzcD Heavy-Metal Efflux (`czcB`, `czcC`, `czcD`), and Exopolyphosphatase (`ppx`)

| Role | Gene Symbol | UniProt / Locus | Protein / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ExbB pentameric stator | `exbB4` | `A0A0H2MHH3` (`VARPD`, `VPARA_25810`) | Biopolymer transport protein ExbB4 (238 aa, Pfam `PF01618`) | 3-TM inner-membrane proton-channel pore (`exbD5-exbB4-tonB-bfrD1` operon) | `GO:0015078` (proton transmembrane transporter activity), `GO:1902600`, `GO:0015891`, `GO:0005886`, `GO:0098797` |
| ExbD proton-coupling rotor | `exbD5` | `A0A0H2M1F3` (`VARPD`, `VPARA_25800`) | Biopolymer transport protein ExbD5 (137 aa, Pfam `PF02472`) | Single-pass type II inner-membrane dimer with conserved TM `Asp23` | `GO:0015078`, `GO:1902600`, `GO:0015891`, `GO:0005886`, `GO:0030288`, `GO:0098797` |
| RND periplasmic adaptor | `czcB` | `A0A0H2LX82` (`VARPD`, `VPARA_44900`) | Cobalt-zinc-cadmium resistance protein CzcB (455 aa, `TIGR01730`) | N-terminal 10-His region (41-121) + 4 CzcB/CusB adaptor domains | `GO:0005198` (structural molecule activity), `GO:0015562` (`contributes_to`), `GO:0098655`, `GO:0030288`, `GO:0005886` |
| Outer-membrane efflux duct | `czcC` | `A0A0H2M0U4` (`VARPD`, `VPARA_44910`) | Outer membrane protein CzcC (445 aa, Pfam `PF02321`, `PTHR30203`) | Sec signal peptide (1-20) + two OEP repeats forming trimeric outer-membrane tunnel | `GO:0015562`, `GO:0008324`, `GO:0098655`, `GO:0009279` (cell outer membrane) |
| Inner-membrane CDF pump | `czcD` | `A0A0H2M558` (`VARPD`, `VPARA_15480`) | Cadmium, cobalt and zinc/H(+)-K(+) antiporter CzcD (320 aa, `TIGR01297`) | 6-TM CDF antiporter with Site A (`His59, His62, His188, Asp192`) + 15-His loop (152-179) | `GO:0005385` (zinc ion transmembrane transporter activity), `GO:0071577`, `GO:0006882`, `GO:0005886` |
| PolyP depolymerization | `ppx` | `A0A0H2MBK5` (`VARPD`, `VPARA_10490`) | Exopolyphosphatase Ppx (EC 3.6.1.11, 506 aa, `PTHR30005:SF14`) | ASKHA catalytic domain (`PF02541`, P1 `11-DLGSNSFR-18`, P2 `142-DIGGRSTE-149`) + C-terminal polyP-binding domain (`PF21447`) | `GO:0004309` (exopolyphosphatase activity), `GO:0006798` (polyphosphate catabolic process), `GO:0005829` |

- **Updated Modules:**
  - [`modules/bacterial_tonb_siderophore_import.yaml`](../../modules/bacterial_tonb_siderophore_import.html) (`MODULE:bacterial_tonb_siderophore_import` — expanded with `exbB4` and `exbD5` proton-channel motor step)
  - [`modules/variovorax_metallophore_metal_homeostasis.yaml`](../../modules/variovorax_metallophore_metal_homeostasis.html) (`MODULE:variovorax_metallophore_metal_homeostasis` — expanded with `ppx` polyP turnover and `czcB`, `czcC`, `czcD` heavy-metal efflux)

---

## 5. Tranche 4 Curation Batches (SsuABC-SsuE Alkanesulfonate Import & Reductase, TauABC Taurine Import, CzcI/CzcR/CusS/CadA2 Heavy-Metal Island Completion, and Fur1 Iron Regulation)

### Batch 4A: Alkanesulfonate ABC Importer & FMN Reductase (`ssuA2`, `ssuB2`, `ssuC5`, `ssuE`) and Taurine ABC Importer (`tauA`, `tauB1`, `tauC`)

Completes the organosulfonate and taurine assimilation pathways around `ssuD` (`C5CNW9`) and `tauD1` (`A0A0H2MHV8`):

| Role in Complex / Pathway | Gene Symbol | UniProt / Locus (`VARPD`) | Protein / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Periplasmic sulfonate SBP | `ssuA2` | `A0A0H2M784` (`VPARA_09270`) | Aliphatic sulfonate-binding protein SsuA2 (319 aa, `TIGR01728`, `IPR010067`) | Tat signal peptide (1-29, `PS51318`) + periplasmic SsuA fold (`PTHR30024:SF42`) | `GO:0042918` (alkanesulfonate transmembrane transport), `GO:0042959` (`contributes_to`), `GO:0030288`, `GO:0055052` |
| Sulfonate import ATPase | `ssuB2` | `A0A0H2MBB8` (`VPARA_09230`) | Aliphatic sulfonates import ATP-binding protein SsuB2 (276 aa, `PTHR42788:SF17`) | ABC ATPase (`PS50893`) with Walker A (`51-GRSGCGKS-58`) | `GO:0042959` (`contributes_to`), `GO:0005524`, `GO:0016887`, `GO:0042918`, `GO:0005886`, `GO:0055052` |
| Sulfonate permease | `ssuC5` | `A0A0H2M6G6` (`VPARA_09240`) | Aliphatic sulfonates transport permease protein SsuC5 (284 aa, `NF008470`, `PTHR30151:SF38`) | 5-TM ABC transmembrane type-1 domain (`PS50928`, residues 80-264) | `GO:0042918`, `GO:0042959` (`contributes_to`), `GO:0005886`, `GO:0055052` |
| NAD(P)H-FMN reductase | `ssuE` | `A0A0H2M6H0` (`VPARA_09290`) | FMN reductase SsuE (EC 1.5.1.38, 194 aa, `TIGR03567`, `PTHR43408:SF1`) | Flavodoxin-like fold (`PF03358`, residues 1-142) supplying $\text{FMNH}_2$ to SsuD | `GO:0008752` (FMN reductase [NAD(P)H] activity), `GO:0046306`, `GO:0005829` |
| Periplasmic taurine SBP | `tauA` | `A0A0H2M727` (`VPARA_03650`) | Taurine-binding periplasmic protein TauA (340 aa, `TIGR01729`) | Sec signal peptide (1-30) + periplasmic TauA fold (`PTHR30024:SF47`) | `GO:0030977` (taurine binding), `GO:0015734`, `GO:0015411` (`contributes_to`), `GO:0030288`, `GO:0055052` |
| Taurine import ATPase | `tauB1` | `A0A0H2MNF8` (`VPARA_03660`) | Taurine import ATP-binding protein TauB1 (262 aa, `PTHR42788:SF18`) | ABC ATPase (`PS50893`) with Walker A (`40-GASGCGKT-47`) | `GO:0015411` (`contributes_to`), `GO:0005524`, `GO:0016887`, `GO:0015734`, `GO:0005886`, `GO:0055052` |
| Taurine permease | `tauC` | `A0A0H2M7Y1` (`VPARA_03670`) | Taurine transport system permease protein TauC (294 aa, `PTHR30151:SF25`) | 6-TM ABC transmembrane type-1 domain (`PS50928`, residues 100-280) | `GO:0015734`, `GO:0015411` (`contributes_to`), `GO:0005886`, `GO:0055052` |

- **Linked Module:** [`modules/taurine_uptake_and_desulfonation.yaml`](../../modules/taurine_uptake_and_desulfonation.html) (`MODULE:taurine_uptake_and_desulfonation` — expanded with `tauA`, `tauB1`, and `tauC`)

---

### Batch 4B: Heavy-Metal Resistance Island Completion (`czcI`, `czcR`, `cusS`, `cadA2`) and Ferric Uptake Regulator (`fur1`)

| Role | Gene Symbol | UniProt / Locus (`VARPD`) | Protein / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Periplasmic Czc modulator | `czcI` | `A0A0H2LVR9` (`VPARA_44920`) | Cobalt-zinc-cadmium resistance protein CzcI (123 aa, `NF045614`) | Histidine-rich cluster (`36-HWGHHEHE-43`) + `71-CAVCH-75` motif | `GO:0046686` (response to cadmium ion), `GO:0010043` (response to zinc ion), `GO:0030288` (outer membrane-bounded periplasmic space) |
| Heavy-metal response regulator | `czcR` | `A0A0H2LVW5` (`VPARA_44930`) | Two-component response regulator CzcR (225 aa, `TIGR01387`) | Receiver domain (`Asp51`) + OmpR/PhoB winged-helix DNA-binding domain (`PS51755`) | `GO:0000156`, `GO:0003700`, `GO:0000976`, `GO:0000160`, `GO:0006355`, `GO:0010043`, `GO:0005829` |
| Heavy-metal sensor kinase | `cusS` | `A0A0H2MBG2` (`VPARA_44940`) | Sensor protein CusS/CzcS (EC 2.7.13.3, 443 aa, `TIGR01386`) | 2 TM helices + HAMP (`PS50885`) + HisKA/HATPase_c (`PS50109`, `His233`) | `GO:0000155` (phosphorelay sensor kinase activity), `GO:0005524`, `GO:0000160`, `GO:0046777`, `GO:0010043`, `GO:0005886` |
| P1B-2-type heavy-metal ATPase | `cadA2` | `A0A0H2LVW9` (`VPARA_44980`) | P-type Zn(2+)/Cd(2+) transporter CadA2 (EC 7.2.2.12, 759 aa, `TIGR01512`) | N-terminal HMA domain (`IPR006121`) + intramembrane `410-CPC-412` + `Asp454` phosphorylation site | `GO:0016463` (P-type zinc transporter activity), `GO:0015086` (cadmium ion transmembrane transporter activity), `GO:0005524`, `GO:0008270`, `GO:0046870`, `GO:0071577`, `GO:0070574`, `GO:0005886` |
| Ferric uptake repressor | `fur1` | `A0A0H2M8T9` (`VPARA_18200`) | Ferric uptake regulation protein Fur1 (139 aa, `NF006999`) | Structural $\text{Zn}^{2+}$ site (`Cys92, Cys95, Cys132, Cys135`) + regulatory $\text{Fe}^{2+}$ site (`His86, Asp88, Glu107, His124`) | `GO:0001217` (DNA-binding transcription repressor activity), `GO:0000976`, `GO:0008198` (ferrous iron binding), `GO:0045892`, `GO:0006879`, `GO:0005829` |

- **Updated Modules:**
  - [`modules/variovorax_metallophore_metal_homeostasis.yaml`](../../modules/variovorax_metallophore_metal_homeostasis.html) (`MODULE:variovorax_metallophore_metal_homeostasis` — expanded with `fur1`, `cadA2`, `czcI`, `czcR`, and `cusS`)
  - [`modules/bacterial_tonb_siderophore_import.yaml`](../../modules/bacterial_tonb_siderophore_import.html) (`MODULE:bacterial_tonb_siderophore_import` — evidence updated with `fur1`)
