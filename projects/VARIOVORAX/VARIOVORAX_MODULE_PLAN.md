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
   - Also provides Swiss-Prot reviewed anchors for rhizosphere amide turnover (`amiE` `C5CWZ4`), organosulfonate desulfonation (`ssuD` `C5CNW9`), cytosolic YggX-family iron trafficking (`fetP` `C5CNX5`), and nickel-dependent urea hydrolysis (`ureC` `C5CY00`).
2. ***Variovorax paradoxus* (`VARPD`, `NCBITaxon:34073`, Reference Proteome `UP000019090`):**
   - Hosts experimentally characterized Swiss-Prot entries including 1-aminocyclopropane-1-carboxylate deaminase (`acdS`, `Q6J256`) and 3-sulfinopropanoyl-CoA desulfinase (`acd`, `B9U6P5`, `VPARA_05440`), alongside active reference-proteome entries for PQQ-dependent glucose dehydrogenase (`gcd`, `A0A0H2LUW4`, `VPARA_65850`), polyphosphate kinase (`ppk`, `A0A0H2M4T4`, `VPARA_28600`), and the `czcCBAIR` heavy-metal RND efflux island (`czcA3`, `A0A0H2MBF7`, `VPARA_44890`).

---

## 2. Prioritized Curation Batches

### Batch 1A: Auxin (IAA) Catabolism (`iad` Operon) & Root Growth Inhibition Reversal

*Variovorax* is the keystone genus in plant root microbiomes responsible for degrading excess bacterial and plant indole-3-acetic acid (IAA) to prevent ethylene- and auxin-driven root growth inhibition (Finkel et al. 2020, PMID:32999461; Conway et al. 2022, PMID:36266335; Ma et al. 2023, PMID:37459330).

| Role in Module | Gene Symbol | UniProt / Locus (`VARPS`) | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Catalytic $\alpha$ subunit | `iadD` | `C5CSP6` (`Vapar_1493`) | Indole-3-acetic acid Rieske dioxygenase large subunit | `[2Fe-2S]` Rieske cluster + mononuclear non-heme Fe(II) | `GO:0016708` (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of two atoms of oxygen into one donor), `GO:0042437` (indoleacetic acid catabolic process) |
| Structural $\beta$ subunit | `iadE` | `C5CSP7` (`Vapar_1494`) | Indole-3-acetic acid dioxygenase small subunit | $\alpha_3\beta_3$ heterohexamer assembly (`contributes_to` holoenzyme activity) | `GO:0016708` (`contributes_to`), `GO:0042437` (indoleacetic acid catabolic process) |
| Electron transfer | `iadC` | `C5CSP5` (`Vapar_1492`) | Class IA FMN/`[2Fe-2S]` ferredoxin-$\text{NAD}^+$ reductase | FMN (`GO:0010181`) + `[2Fe-2S]` cluster (`GO:0051537`) | `GO:0008860` (ferredoxin-NAD+ reductase activity), `GO:0042437` |
| Transcriptional sensor | `iadR` | `C5CSP2` (`Vapar_1489`) | MarR-family IAA-sensing transcriptional repressor | Direct IAA binding pocket (derepresses `iad` transcription) | `GO:0001217` (DNA-binding transcription repressor activity), `GO:0000976` (transcription cis-regulatory region binding), `GO:0045892` (negative regulation of DNA-templated transcription) |

- **Target Module:** `modules/bacterial_iad_auxin_catabolism.yaml`

---

### Batch 1B: Ethylene Stress Buffering (`acdS`) & Nitrile-to-Auxin/Ammonia Crosstalk (`amiE`)

*Variovorax* coordinates auxin degradation with ethylene precursor cleavage and rhizosphere nitrile/amide turnover:

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACC cleavage | `acdS` | `Q6J256` (`VARPD`) | 1-aminocyclopropane-1-carboxylate deaminase (EC 3.5.99.7) | Pyridoxal 5'-phosphate (`GO:0030170`); cleaves ACC to 2-oxobutanoate + $\text{NH}_3$ | `GO:0008660` (1-aminocyclopropane-1-carboxylate deaminase activity), `GO:0042217` (1-aminocyclopropane-1-carboxylate catabolic process) |
| Amide hydrolysis | `amiE` | `C5CWZ4` (`VARPS`, `Vapar_0135`) | Aliphatic amidase (EC 3.5.1.4) | Glu59-Lys134-Cys166 catalytic triad; hydrolyzes short-chain aliphatic amides to organic acids + $\text{NH}_3$ | `GO:0004040` (amidase activity) |

---

### Batch 2A: Cytosolic Iron Trafficking, PQQ-Dependent Mineral Acidolysis & Polyphosphate Synthesis

*Variovorax paradoxus* utilizes cytosolic YggX-family iron-trafficking proteins, PQQ-dependent periplasmic glucose dehydrogenase for gluconic acid-driven mineral acidolysis, and intracellular polyphosphate synthesis for phosphate/energy storage and divalent cation chelation (with hypothesized applications to [REE](../REE.md)):

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cytosolic Fe(2+) trafficking | `fetP` | `C5CNX5` (`VARPS`, `Vapar_2982`) | Probable $\text{Fe}^{2+}$-trafficking protein | Cytosolic YggX-family iron-binding protein (`HAMAP MF_00686`, `IPR007457`) | `GO:0005506` (iron ion binding), `GO:0006879` (intracellular iron ion homeostasis) |
| Periplasmic PQQ oxidation | `gcd` | `A0A0H2LUW4` (`VARPD`, `VPARA_65850`) | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) | PQQ + divalent cation cofactor; oxidizes D-glucose to D-glucono-1,5-lactone | `GO:0008876` (quinoprotein glucose dehydrogenase activity), `GO:0019521` (D-gluconate metabolic process) |
| Intracellular polyP synthesis | `ppk` | `A0A0H2M4T4` (`VARPD`, `VPARA_28600`) | Polyphosphate kinase (EC 2.7.4.1) | Polymerizes terminal $\gamma$-phosphate of ATP into long-chain polyP polymers | `GO:0008976` (polyphosphate kinase activity), `GO:0006799` (polyphosphate biosynthetic process) |

- **Target Module:** `modules/variovorax_metallophore_metal_homeostasis.yaml`

---

### Batch 2B: Heavy-Metal Efflux (`czcA3`) & Rhizosphere Organosulfur Mobilization (`ssuD`, `acd`)

*Variovorax* thrives in polymetallic and sulfur-limited soils by coupling inner-membrane HME-RND metal cation efflux with organosulfonate and 3-sulfinopropanoyl-CoA mineralization:

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RND metal antiporter | `czcA3` | `A0A0H2MBF7` (`VARPD`, `VPARA_44890`) | Cobalt/zinc/cadmium efflux RND transporter, CzcA family (CzcA3) | Inner-membrane HME-RND proton/cation antiporter subunit (`TIGR00914`, `IPR004763`) | `GO:0008324` (monoatomic cation transmembrane transporter activity), `GO:0098655` (monoatomic cation transmembrane transport) |
| Organosulfur desulfonation | `ssuD` | `C5CNW9` (`VARPS`, `Vapar_2976`) | Alkanesulfonate monooxygenase (EC 1.14.14.5) | $\text{FMNH}_2$-dependent TIM-barrel monooxygenase (standalone Betaproteobacterial comparator to `bacterial_alkanesulfonate_uptake_desulfonation`) | `GO:0008726` (alkanesulfonate monooxygenase activity), `GO:0046306` (alkanesulfonate catabolic process) |
| 3SP-CoA cleavage | `acd` | `B9U6P5` (`VARPD`, `VPARA_05440`) | 3-sulfinopropanoyl-CoA desulfinase (EC 3.13.1.4) | Acyl-CoA dehydrogenase fold adapted for non-oxidative C–S cleavage | Proposed: `3-sulfinopropanoyl-CoA desulfinase activity`, `GO:0006790` (sulfur compound metabolic process) |
