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

This document defines the batch curation plan and module architecture for *Variovorax* (`NCBITaxon:34072`) enzymes in `ai-gene-review`, with primary focus on **rhizosphere plant–microbe chemical signaling** and **critical/heavy metal recovery and homeostasis**.

## 1. Taxonomic & Proteome Strategy

Following UniProt's 2026_02 reference proteome policy ([PROTEOME_REMOVAL](../PROTEOME_REMOVAL.md)), curation is anchored on active UniProtKB reference proteomes and Swiss-Prot reviewed records:

1. ***Variovorax paradoxus* S110 (`VARPS`, `NCBITaxon:543728`, Proteome `UP000001552`):**
   - Multipartite genome (Chromosome 1 `CP001635` and Chromosome 2 `CP001636`, locus tags `Vapar_0001`–`Vapar_6257`; Han et al. 2011, PMID:21166890) with 234 Swiss-Prot reviewed proteins and 6 retained TrEMBL entries in UniProtKB, notably including the four core proteins of the `iad` auxin-catabolism locus (`Vapar_1489` `C5CSP2` `iadR`, `Vapar_1492` `C5CSP5` `iadC`, `Vapar_1493` `C5CSP6` `iadD`, and `Vapar_1494` `C5CSP7` `iadE`).
   - Also provides Swiss-Prot reviewed anchors for rhizosphere amide turnover (`amiE` `C5CWZ4`), organosulfonate desulfonation (`ssuD` `C5CNW9`), periplasmic iron/metal trafficking (`fetP` `C5CNX5`), and nickel-dependent urea hydrolysis (`ureC` `C5CY00`).
2. ***Variovorax paradoxus* (`VARPD`, `NCBITaxon:34073`, Reference Proteome `UP000019090`):**
   - Hosts experimentally characterized Swiss-Prot entries including 1-aminocyclopropane-1-carboxylate deaminase (`acdS`, `Q6J256`) and 3-sulfinopropanoyl-CoA desulfinase (`acd`, `B9U6P5`, `VPARA_05440`), alongside active reference-proteome entries for PQQ-dependent glucose dehydrogenase (`gcd`, `A0A0H2LUW4`, `VPARA_65850`), polyphosphate kinase (`ppk`, `A0A0H2M4T4`, `VPARA_28600`), and the `czcCBAIR` heavy-metal RND efflux island (`czcA3`, `A0A0H2MBF7`, `VPARA_44890`).

---

## 2. Prioritized Curation Batches

### Batch 1A: Auxin (IAA) Catabolism (`iad` Operon) & Root Growth Inhibition Reversal

*Variovorax* is the keystone genus in plant root microbiomes responsible for degrading excess bacterial and plant indole-3-acetic acid (IAA) to prevent ethylene- and auxin-driven root growth inhibition (Finkel et al. 2020, PMID:32999461; Conway et al. 2022, PMID:36266335; Ma et al. 2023, PMID:37459330).

| Role in Module | Gene Symbol | UniProt / Locus (`VARPS`) | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Catalytic $\alpha$ subunit | `iadD` | `C5CSP6` (`Vapar_1493`) | Indole-3-acetic acid Rieske dioxygenase large subunit | `[2Fe-2S]` Rieske cluster + mononuclear non-heme Fe(II) | `GO:0016702` (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of two atoms of oxygen into one donor), `GO:0009684` (indoleacetic acid catabolic process) |
| Structural $\beta$ subunit | `iadE` | `C5CSP7` (`Vapar_1494`) | Indole-3-acetic acid dioxygenase small subunit | $\alpha_3\beta_3$ heterohexamer assembly (`contributes_to` holoenzyme activity) | `GO:0016702` (`contributes_to`), `GO:0009684` (indoleacetic acid catabolic process) |
| Electron transfer | `iadC` | `C5CSP5` (`Vapar_1492`) | `[2Fe-2S]` ferredoxin electron carrier | `[2Fe-2S]` iron-sulfur cluster (`GO:0051537`) | `GO:0009055` (electron transfer activity), `GO:0009684` |
| Transcriptional sensor | `iadR` | `C5CSP2` (`Vapar_1489`) | MarR-family IAA-sensing transcriptional repressor | Direct IAA binding pocket (derepresses `iad` transcription) | `GO:0003700` (DNA-binding transcription factor activity), `GO:0045892` (negative regulation of DNA-templated transcription), `GO:0009684` |

- **Target Module:** `modules/bacterial_iad_auxin_catabolism.yaml`

---

### Batch 1B: Ethylene Stress Buffering (`acdS`) & Nitrile-to-Auxin/Ammonia Crosstalk (`amiE`)

*Variovorax* coordinates auxin degradation with ethylene precursor cleavage and rhizosphere nitrile/amide turnover:

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACC cleavage | `acdS` | `Q6J256` (`VARPD`) | 1-aminocyclopropane-1-carboxylate deaminase (EC 3.5.99.7) | Pyridoxal 5'-phosphate (`GO:0030170`); cleaves ACC to 2-oxobutanoate + $\text{NH}_3$ | `GO:0042151` (1-aminocyclopropane-1-carboxylate deaminase activity), `GO:0009692` (ethylene metabolic process) |
| Amide hydrolysis | `amiE` | `C5CWZ4` (`VARPS`, `Vapar_0135`) | Aliphatic amidase (EC 3.5.1.4) | Cys-Glu-Lys catalytic triad; hydrolyzes short-chain aliphatic amides to organic acids + $\text{NH}_3$ | `GO:0004040` (amidase activity), `GO:0043605` (cellular amide catabolic process) |

---

### Batch 2A: Metal/Iron Trafficking, PQQ-Dependent Mineral/REE Bioleaching & Polyphosphate Storage

*Variovorax paradoxus* utilizes periplasmic redox metal-trafficking proteins, PQQ-dependent periplasmic glucose dehydrogenase for gluconic acid-driven mineral/REE acidolysis, and intracellular polyphosphate synthesis for metal/lanthanide sequestration (linking to [REE](../REE.md)):

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Periplasmic Fe/Cu trafficking | `fetP` | `C5CNX5` (`VARPS`, `Vapar_2982`) | Probable $\text{Fe}^{2+}$-trafficking protein | Periplasmic metal-binding cupredoxin-like dimer | `GO:0005506` (iron ion binding), `GO:0006826` (iron ion transport) |
| Acidolysis / PQQ oxidation | `gcd` | `A0A0H2LUW4` (`VARPD`, `VPARA_65850`) | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) | PQQ (`GO:0019166`) + $\text{Ca}^{2+}/\text{Mg}^{2+}$ cofactor; oxidizes D-glucose to D-glucono-1,5-lactone | `GO:0008876` (quinoprotein glucose dehydrogenase activity), `GO:0006006` (glucose metabolic process) |
| Intracellular metal/P storage | `ppk` | `A0A0H2M4T4` (`VARPD`, `VPARA_28600`) | Polyphosphate kinase (EC 2.7.4.1) | Polymerizes terminal $\gamma$-phosphate of ATP into long-chain polyP chelator granules | `GO:0008976` (polyphosphate kinase activity), `GO:0006799` (polyphosphate biosynthetic process) |

- **Target Module:** `modules/variovorax_metallophore_metal_homeostasis.yaml`

---

### Batch 2B: Heavy-Metal Efflux (`czcCBA`) & Rhizosphere Organosulfur Mobilization (`ssuD`, `acd`)

*Variovorax* thrives in polymetallic and sulfur-limited soils by coupling tripartite RND metal efflux with organosulfonate and sulfinopropionyl-CoA mineralization:

| Role | Gene Symbol | UniProt / Locus | Enzyme / Function | Key Cofactors / Chemistry | Target GO Terms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RND metal antiporter | `czcA3` | `A0A0H2MBF7` (`VARPD`, `VPARA_44890`) | Cobalt-zinc-cadmium resistance protein CzcA | Proton-motive force driven tripartite RND efflux (`czcCBA`) | `GO:0015297` (antiporter activity), `GO:0006829` (zinc ion transport) / `GO:0046686` (response to cadmium ion) |
| Organosulfur desulfonation | `ssuD` | `C5CNW9` (`VARPS`, `Vapar_2976`) | Alkanesulfonate monooxygenase (EC 1.14.14.5) | $\text{FMNH}_2$-dependent TIM-barrel monooxygenase | `GO:0008726` (alkanesulfonate monooxygenase activity), `GO:0046393` (alkanesulfonate catabolic process) |
| Sulfinopropionyl-CoA cleavage | `acd` | `B9U6P5` (`VARPD`, `VPARA_05440`) | 3-sulfinopropanoyl-CoA desulfinase (EC 4.4.1.29 / 3.13.1.4) | Acyl-CoA dehydrogenase fold adapted for non-oxidative C–S cleavage | `GO:0102131` (3-sulfinopropanoyl-CoA desulfinase activity) |
