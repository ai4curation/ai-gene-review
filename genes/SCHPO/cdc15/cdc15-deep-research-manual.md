# Deep Research: S. pombe cdc15 (Q09822)

## Gene Overview

Cdc15 is an essential F-BAR (Fer/CIP4 homology-BAR) domain protein in *Schizosaccharomyces pombe* that serves as the founding member of the PCH (Pombe Cdc15 Homology) protein family. It is a critical scaffold linking the cytokinetic contractile ring (CR) to the plasma membrane during cell division.

## Domain Architecture

- **N-terminal F-BAR domain (aa 20-273)**: Dimerizes to create membrane-binding module; oligomerizes tip-to-tip for high-avidity membrane binding; does NOT tubulate membranes [PMID:33357436, PMID:26702831]. Binds formin Cdc12 on the cytosolic face opposite the membrane-binding surface [PMID:33357436]. Also binds paxillin-like Pxl1 on the same cytosolic face [PMID:33357436].
- **Intrinsically disordered region (IDR, ~aa 321-857)**: Heavily phosphorylated, contains >35 phosphorylation sites. Critical for phosphoregulation, recruits calcineurin. The IDR is essential for viability [PMID:32101481].
- **C-terminal SH3 domain (aa 866-927)**: Interacts with network of protein partners including Fic1, Pxl1 (with IDR), Imp2, and other CR components [PMID:25428987].

## Core Functions

### 1. Cytokinetic contractile ring scaffold and membrane anchor
Cdc15 is one of the earliest and most abundant CR proteins to arrive at the division site [PMID:7634333]. It forms the membrane-proximal layer of the CR (0-80 nm from PM), linking the plasma membrane to internal CR components [PMID:28914606, PMID:33357436]. The F-BAR domain oligomerizes to create a membrane-bound platform, and when oligomerization is disrupted, the CR is unstable and can disassemble [PMID:33357436]. The SH3 domain extends ~150 nm from the PM in the mature CR and interacts with a network of proteins ensuring robust cytokinesis [PMID:33357436].

### 2. Formin Cdc12 recruitment for F-actin nucleation
Cdc15 directly recruits the formin Cdc12 to the cell middle through binding between the Cdc15 F-BAR domain and a conserved N-terminal motif (aa 24-36) in Cdc12, with a dissociation constant of 1.1 nM [PMID:25688133]. Loss of this interaction reduces Cdc12, F-actin, and actin-binding proteins at the CR by ~35%, delays CR formation by ~25%, and is synthetically lethal with mutations in the alternative Cdc12 recruitment pathway (Rng2/Myo2) [PMID:25688133]. Cdc15 also recruits Arp2/3 complex activator Myo1p for the second actin nucleation pathway [PMID:12939254].

### 3. Phosphoregulation controls membrane binding and scaffolding
Cdc15 is hyperphosphorylated in interphase, which generates a closed, inactive conformation that prevents membrane binding, oligomerization, and partner interactions [PMID:32101481]. Dephosphorylation at mitotic onset activates Cdc15, allowing it to oligomerize, bind membranes, and scaffold the CR. Multiple kinases regulate Cdc15:
- **Pom1 (DYRK kinase)**: Phosphorylates 22 sites on Cdc15, preventing membrane binding and Pxl1 interaction; this is key for preventing septum formation at cell tips (tip occlusion) [PMID:32101481]
- **Cdk1**: Phosphoinhibits the Cdc12-Cdc15 interaction, opposing CR formation until the appropriate cell cycle stage [PMID:29343550]
- **Kin1**: Phosphorylates Cdc15 on non-overlapping sites [PMID:32101481]

### 4. Clathrin-dependent endocytosis
Cdc15 localizes to actin cortical patches during interphase and participates in endocytosis. At endocytic sites, Cdc15 assembles stoichiometrically with Myo1p and promotes Arp2/3-dependent actin polymerization. Cells depleted of Cdc15 assemble 3-5 fold less actin in patches and patches move shorter distances from the PM [PMID:21885283].

### 5. Cell polarity and division site positioning
Cdc15 contributes to establishment of bipolar cell polarity [PMID:23093943]. The DYRK kinase Pom1 phosphorylates Cdc15 at cell tips to prevent ectopic septum formation, ensuring medial division [PMID:32101481]. Cdc15 also promotes Cdc42 activation during cytokinesis and cell polarization through regulation of GEF Gef1.

### 6. NOT membrane bending
Unlike some other BAR domain proteins, the Cdc15 F-BAR domain does NOT bend/tubulate membranes. Instead, oligomerization (not membrane bending) underlies its function in cytokinesis [PMID:26702831].

## Key Interaction Partners

| Partner | Interaction domain | Function |
|---------|-------------------|----------|
| Cdc12 (formin) | F-BAR domain (cytosolic face) | Actin nucleation for CR |
| Myo1 (type I myosin) | F-BAR/coiled-coil region | Arp2/3 complex activation |
| Pxl1 (paxillin) | SH3 + IDR | CR integrity, calcineurin recruitment |
| Fic1 | SH3 domain | CR disassembly, septation |
| Imp2 | SH3 domain | CR function |
| Blt1 | Unknown | Node component |
| Rng2 (IQGAP) | Via SH3 network | CR constriction |

## Localization Through Cell Cycle

- **Interphase**: Cytoplasmic puncta at cell tips (endocytic patches), also diffuse cytoplasm. Held inactive by phosphorylation.
- **Early mitosis**: Recruited to medial cortical nodes, one of the first CR components to arrive.
- **Mitosis**: Forms ring structure at division site, most abundant in the membrane-proximal layer.
- **Late mitosis/cytokinesis**: Remains at CR during constriction and septation.
- **Post-division**: Reforms as puncta at old cell ends.

Also localizes to: mating projection tip during conjugation [PMID:25825517], medial membrane band [PMID:15517003, PMID:31276301].

## Key References

- Fankhauser et al. 1995 (PMID:7634333) - Original identification, essential for F-actin reorganization at mitosis
- Carnahan & Gould 2003 (PMID:12939254) - Recruits two F-actin nucleation pathways
- Willet et al. 2015 (PMID:25688133) - F-BAR directly recruits formin Cdc12
- Snider et al. 2020 (PMID:33357436) - F-BAR dual surfaces create membrane platform
- Bhattacharjee et al. 2020 (PMID:32101481) - Pom1 phosphorylation drives Cdc15 from membrane
- McDonald et al. 2015 (PMID:26702831) - Oligomerization, not membrane bending, underlies function
- Arasada & Pollard 2011 (PMID:21885283) - Roles in endocytosis
- McDonald et al. 2017 (PMID:28914606) - Nanoscale architecture of CR
