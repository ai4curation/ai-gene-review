# Tardigrade Stress Response Protein Curation Project

**Project Start Date:** 2026-04-09
**Organism:** *Ramazzottius varieornatus* (RAMVA)
**Focus:** Anhydrobiosis and extremotolerance - tardigrade-unique stress response proteins

## Project Overview

This project curates the complete set of reviewed (Swiss-Prot) proteins from the extremotolerant tardigrade *Ramazzottius varieornatus*. These proteins represent a remarkable evolutionary innovation: a suite of tardigrade-unique intrinsically disordered proteins (TDPs) that protect different cellular compartments during anhydrobiosis (near-complete desiccation), plus conventional stress-response enzymes. The same mechanisms that enable desiccation tolerance also confer extraordinary resistance to ionizing radiation, extreme temperatures, vacuum, and high pressure.

The TDP families partition by cellular compartment:
- **Dsup** - nuclear/chromatin protectant (shields DNA from hydroxyl radicals via nucleosome binding)
- **CAHS** - cytosolic-abundant heat-soluble proteins (form protective hydrogels/filaments upon desiccation)
- **SAHS** - secretory-abundant heat-soluble proteins (protect extracellular components; FABP-like fold)
- **MAHS** - mitochondrial-abundant heat-soluble protein (protects mitochondrial function)
- **RvLEAM** - mitochondrial LEA protein (late-embryogenesis abundant; shared with plants/nematodes)
- **RvY_13070 (RvSOD15)** - Cu-Zn superoxide dismutase fold, but likely a **pseudoenzyme** (Val87 replaces catalytic His)

## Gene List and Curation Status

### Nuclear Protectant

| Gene Symbol | UniProt | Status | Deep Research | Review | Notes |
|-------------|---------|--------|---------------|--------|-------|
| Dsup | P0DOW4 | COMPLETE | falcon | COMPLETE | Nucleosome-binding chromatin shield; 2 GOA annots, 3 NEW proposed |

### Cytosolic Protectants (CAHS Family)

| Gene Symbol | UniProt | Status | Deep Research | Review | Notes |
|-------------|---------|--------|---------------|--------|-------|
| CAHS1 | J7M799 | REVIEWED | falcon | REVIEWED | 2 GOA ACCEPT, 1 NEW (response to desiccation) |
| CAHS2 | J7MDG6 | REVIEWED | falcon | REVIEWED | 1 GOA ACCEPT, 2 NEW (response to desiccation, response to osmotic stress) |
| CAHS3 | J7M3T1 | REVIEWED | falcon | REVIEWED | 1 GOA ACCEPT, 2 NEW (response to desiccation, response to osmotic stress) |

### Secretory Protectants (SAHS Family)

| Gene Symbol | UniProt | Status | Deep Research | Review | Notes |
|-------------|---------|--------|---------------|--------|-------|
| SAHS1 | J7MFT5 | REVIEWED | falcon | REVIEWED | 2 GOA ACCEPT, 1 NEW (response to desiccation); FABP-like beta-barrel |
| SAHS2 | J7MAN2 | REVIEWED | falcon | REVIEWED | 1 GOA ACCEPT, 2 NEW (lipid binding, response to desiccation) |

### Mitochondrial Protectants

| Gene Symbol | UniProt | Status | Deep Research | Review | Notes |
|-------------|---------|--------|---------------|--------|-------|
| MAHS | A0A1D1V3Z0 | REVIEWED | falcon | REVIEWED | 1 GOA ACCEPT, 3 NEW (desiccation, osmotic stress, protein stabilization) |
| RvLEAM | A0A0E4AVP3 | REVIEWED | falcon | REVIEWED | 1 GOA MODIFY (mitochondrial matrix), 3 NEW (desiccation, osmotic stress, unfolded protein binding) |

### ROS Scavenging - Cu/Zn Superoxide Dismutase Paralog Family

R. varieornatus has an expanded family of ~10 Cu/Zn SOD paralogs in UniProt
(plus 1 Mn/Fe-SOD, RvY_01767). Sim & Inoue (2023) identified RvSOD15 as a
likely pseudoenzyme and noted that "some other RvSODs" may also have lost
function. We applied bioinformatic analysis (sequence conservation + PROSITE
motif matching + Pfam membership) to all 10 paralogs to assess catalytic
capability. Details: `genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md`

| Gene Symbol | UniProt | Status | Verdict | Notes |
|-------------|---------|--------|---------|-------|
| **RvY_13070 (RvSOD15)** | A0A1D1VU85 | REVIEWED (Swiss-Prot) | **PSEUDOENZYME** | Val87 replaces catalytic His48; confirmed structurally (PMID:37358501); 4 SOD activity annots OVER-ANNOTATED |
| RvY_00650 | A0A1D1UDY8 | REVIEWED | **IMPAIRED** | All Cu His present but PROSITE PS00087 fails (loop context divergent); 292 aa with N-terminal extension |
| RvY_03757 | A0A1D1UP59 | REVIEWED | **IMPAIRED** | Same: residues OK, PROSITE PS00087 fails |
| RvY_17310 | A0A1D1W3Y1 | REVIEWED | **IMPAIRED** | 475 aa (3x normal), residues OK, PROSITE PS00087 fails |
| RvY_15948 | A0A1D1VWP9 | REVIEWED | **CCS chaperone** | NOT a SOD; copper chaperone homolog; H46→A, H48→C; correctly lacks SOD activity in GOA |
| RvY_00651 | A0A1D1UKR0 | REVIEWED | Likely functional | 66% identity to human SOD1 (highest); all sequence + PROSITE checks pass |
| RvY_03754 | A0A1D1UP68 | REVIEWED | Likely functional | 63% identity; all checks pass |
| RvY_09480 | A0A1D1VEY6 | REVIEWED | Likely functional | All checks pass |
| RvY_10893 | A0A1D1VE88 | REVIEWED | Likely functional | All checks pass |

### Mn/Fe Superoxide Dismutase

| Gene Symbol | UniProt | Status | Notes |
|-------------|---------|--------|-------|
| RvY_01767 | A0A1D1USM4 | REVIEWED | Mitochondrial Mn-SOD (different family from Cu/Zn-SODs); 6 ACCEPT, 1 REMOVE (incorrect respiratory chain complex annotation from ARBA rule) |

## Scientific Background

### Anhydrobiosis as the Central Selective Pressure

Tardigrades can survive near-complete desiccation by entering a dormant tun state. During desiccation, massive ROS accumulation causes oxidative damage across all cellular compartments. The TDP protein families represent a coordinated evolutionary response: each family protects a different compartment (nucleus, cytosol, mitochondria, extracellular space) during the desiccation-rehydration cycle.

The extraordinary radiation tolerance of tardigrades is likely a byproduct of desiccation tolerance, since both stresses generate hydroxyl radicals that damage biomolecules. This is supported by the observation that Dsup protects against both X-ray and H2O2-induced damage through the same nucleosome-shielding mechanism.

### Intrinsic Disorder as a Common Theme

Most TDPs are intrinsically disordered proteins (IDPs). This is functionally important: disorder allows flexible, multivalent interactions with target substrates (chromatin for Dsup, cytoskeletal elements for CAHS) and enables reversible phase transitions (hydrogel formation for CAHS) that may physically stabilize cellular structures during water loss.

### Evolutionary Uniqueness

The TDP families (CAHS, SAHS, MAHS, Dsup) are tardigrade-specific with no homologs outside the phylum. RvLEAM is the exception - LEA proteins are found in plants, nematodes, and other anhydrobiotic organisms, representing convergent evolution of desiccation tolerance. RvSOD15 is a conventional Cu-Zn superoxide dismutase.

## Key Findings from Curation

### Annotation gaps across all TDPs
The most consistent gap is the absence of **GO:0009269 (response to desiccation)** from all TDP annotations. This is the core biological process for the entire family and was proposed as NEW for every gene. Similarly, **response to osmotic stress** was proposed for several genes where experimental gain-of-function data exists (MAHS, RvLEAM in human cells).

### RvSOD15 is a confirmed pseudoenzyme - and it's not alone
The crystal structure (PMID:37358501) revealed that Val87 replaces a critical
histidine copper ligand in RvSOD15. We extended this analysis to all 10
Cu/Zn-SOD paralogs in *R. varieornatus* using sequence + PROSITE motif analysis
(see `genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md`):

- **1 confirmed pseudoenzyme** (RvSOD15/RvY_13070): structural data + sequence
- **3 additional probably-impaired paralogs** (RvY_00650, RvY_03757, RvY_17310):
  All four catalytic Cu histidines preserved at the residue level, BUT all three
  fail PROSITE PS00087 (the N-terminal Cu coordination signature), indicating
  divergence in flanking residues that maintain the structural geometry of the
  Cu site. By analogy with the V87H rescue failure in RvSOD15 (where restoring
  the missing histidine did NOT restore activity due to loop dynamics), these
  paralogs likely have impaired catalytic function.
- **1 copper chaperone** (RvY_15948, CCS homolog): correctly lacks SOD activity
  annotation in GOA - automated pipelines got this one right
- **4 likely-functional canonical SODs**: RvY_00651, RvY_03754, RvY_09480,
  RvY_10893

This validates Sim & Inoue's claim that "some other RvSODs are also unusual
SODs" and provides a more precise count: at least 4 of 9 Cu/Zn-SOD-family
paralogs (excluding the chaperone) appear to have lost or impaired canonical
SOD activity. The picture of "gene duplication = more antioxidant capacity"
is only partially correct - roughly half the expanded SOD repertoire may be
non-catalytic.

The bioinformatic analysis pipeline (sequence conservation + PROSITE PS00087/
PS00332 + Pfam membership) is reusable: `analyze_sods.py` and `check_prosite.py`
in the bioinformatics folder.

### Annotation propagation errors are systematic
Standard automated pipelines (InterPro2GO, EC2GO, UniRule, ARBA) assigned
GO:0004784 (SOD activity) to ALL Cu/Zn-SOD-family proteins based on Pfam
membership, without checking catalytic residue conservation or motif integrity.
This is the canonical "annotation propagation by family membership" failure
mode, and it is now clearly documented for at least 4 out of 9 Cu/Zn-SOD
paralogs in this organism. RvY_01767 (Mn-SOD) also received an incorrect
"respiratory chain complex" annotation from an ARBA rule, since mitochondrial
Mn-SOD is a soluble matrix protein, not a respiratory chain component.

### Dsup DNA binding vs nucleosome binding
The original GO:0003677 (DNA binding) annotation was initially proposed for MODIFY to nucleosome binding, but was corrected to ACCEPT after recognizing that GO:0031491 (nucleosome binding) is NOT a child of DNA binding in GO (it's under chromatin binding). Both are valid independent MF annotations for Dsup.

### SAHS proteins have FABP-like folds
SAHS1 and SAHS2 adopt beta-barrel folds homologous to fatty acid-binding proteins, with crystal structures available. Lipid binding was annotated for SAHS1 but not SAHS2 - proposed to add for SAHS2.

## Key References

- Hashimoto et al. 2016 (PMID:27649274) - Genome sequencing, discovery of Dsup
- Chavez et al. 2019 (PMID:31571581) - Dsup nucleosome binding mechanism
- Tanaka et al. 2015 (PMID:25581620) - MAHS improves osmotic tolerance
- Yamaguchi et al. 2012 (PMID:22554515) - CAHS/SAHS protein families identified
- Fukuda et al. 2017 (PMID:28703282) - SAHS1 crystal structure (FABP-like)
- Tanaka et al. 2022 (PMID:34675210) - CAHS1 fibrous condensation/hydrogel
