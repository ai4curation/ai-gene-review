# C. elegans Unfolded Protein Response & Stress Integration Project

## Overview

The unfolded protein response (UPR) comprises three organelle-specific stress response pathways: UPR-ER (endoplasmic reticulum), UPR-mt (mitochondrial), and UPR-cyt (cytosolic/heat shock response). *C. elegans* has been instrumental in discovering non-cell autonomous regulation of these pathways and unexpected crosstalk with DNA damage response.

Recent discoveries (2024) reveal that UPR-ER protects against DNA damage from stalled replication forks, and that germline-soma signaling regulates mitochondrial UPR. These findings expand our understanding of how stress responses are integrated at the organismal level.

## Model Species

**Primary: Caenorhabditis elegans (worm)**
- UniProt species code: CAEEL
- UPR pathways well-characterized
- Non-cell autonomous signaling discovered here
- DNA damage-UPR crosstalk (2024 discovery)

## Core Pathway Architecture

### 1. UPR-ER: IRE-1 Branch
Conserved splicing-based activation:
- **ire-1** - IRE1 kinase/RNase (sensor)
- **xbp-1** - XBP1 transcription factor (spliced by IRE-1)
- **hsp-4** - BiP/GRP78 (HSP70 chaperone, readout gene)
- **hsp-3** - BiP family

### 2. UPR-ER: PEK-1/PERK Branch
Translation attenuation:
- **pek-1** - PERK kinase (sensor)
- **eif-2alpha** - Translation initiation factor (phosphorylated)
- **atf-4** - ATF4 transcription factor
- **atf-5** - ATF5 (downstream effector)

### 3. UPR-ER: ATF-6 Branch
Regulated proteolysis activation:
- **atf-6** - ATF6 transcription factor
- Site-1 and Site-2 proteases

### 4. Alternative UPR (abu genes)
Discovered in *C. elegans* when canonical UPR is blocked:
- **abu-1** - Activated in blocked UPR
- **abu-8** - ABU family member
- **abu-11** - ABU family member
- **pqn-* family** - Prion-like Q/N-rich proteins

### 5. UPR-mt (Mitochondrial UPR)
Mitochondrial proteostasis:
- **atfs-1** - ATFS1 TF (shuttles between mito and nucleus)
- **ubl-5** - UBL5 (transcription regulator)
- **dve-1** - DVE-1 TF
- **hsp-6** - mtHSP70 (readout gene)
- **hsp-60** - HSP60 chaperonin (readout gene)
- **clpp-1** - ClpP protease (stress signal generator)

### 6. UPR-mt Regulators
- **lin-65** - Chromatin regulator
- **met-2** - Histone methyltransferase
- **jmjd-1.2** - Histone demethylase
- **jmjd-3.1** - Histone demethylase

### 7. Non-Cell Autonomous Signaling
Neuronal control of peripheral UPR:
- **ocr-2** - TRPV channel (sensory neurons)
- Serotonin signaling
- Neuronal-intestinal axis

### 8. DNA Damage Response Crosstalk (2024)
Newly discovered connections:
- Replication stress activates UPR-ER
- IRE-1 and PEK-1 both respond to DNA damage
- Germline-specific activation patterns

### 9. Integrated Stress Response (ISR)
Convergent signaling:
- **gcn-2** - GCN2 kinase (amino acid sensing)
- Multiple kinases phosphorylate eIF2alpha
- ATF-4/5 as common downstream effectors

## Genes for Review (Priority Order)

### Priority 1: Core UPR-ER Sensors (~6 genes) ✅ COMPLETE
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| ire-1 | Q9XWR5 | ERN1 | IRE1 sensor/RNase | ✅ |
| xbp-1 | Q9BLS7 | XBP1 | bZIP TF (spliced) | ✅ |
| pek-1 | Q9N519 | EIF2AK3/PERK | PERK kinase | ✅ |
| atf-6 | Q17827 | ATF6 | Membrane-bound TF | ✅ |
| hsp-4 | Q966C6 | HSPA5/BiP | ER chaperone | ✅ |
| atf-4 | O44705 | ATF4 | ISR effector TF | ✅ |

### Priority 2: UPR-mt Pathway (~6 genes) ✅ COMPLETE
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| atfs-1 | G5ED34 | ATF5 | mt-nuclear TF | ✅ (reviewed in MITOPHAGY) |
| dve-1 | Q9N3Z4 | SATB1 | Chromatin regulator | ✅ |
| ubl-5 | Q20209 | UBL5 | UPR-mt regulator | ✅ |
| hsp-6 | P11141 | HSPA9/mtHSP70 | Mito chaperone | ✅ |
| hsp-60 | P50140 | HSPD1 | Mito chaperonin | ✅ |
| clpp-1 | Q21898 | CLPP | Mito protease | ✅ |

### Priority 3: Regulators and Integration (~6 genes) ✅ COMPLETE
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| gcn-2 | Q9XWF4 | EIF2AK4/GCN2 | AA sensing kinase | ✅ |
| abu-1 | Q20747 | - | Alternative UPR | ✅ |
| lin-65 | G5ED51 | - | UPR-mt chromatin | ✅ |
| met-2 | G5EBN4 | SETDB1 | H3K9 methyltransferase | ✅ |
| jmjd-3.1 | Q9N585 | KDM6B | H3K27 demethylase | ✅ |
| ocr-2 | Q9Y0D2 | TRPV4 | Sensory neuron UPR | ✅ |

## Key Biological Concepts

### Synthetic Lethality in UPR
- ire-1 or xbp-1 deletion is synthetic lethal with atf-6 or pek-1
- Reveals parallel pathway requirements
- Important for therapeutic targeting

### Non-Cell Autonomous UPR
- Neurons sense ER stress
- Signal to peripheral tissues (intestine, muscle)
- Serotonin and other neurotransmitters involved

### UPR-DNA Damage Crosstalk
- 2024 discovery of UPR-ER in genome integrity
- Replication fork stalling activates IRE-1 and PEK-1
- Differential activation in soma vs germline

### Transgenerational UPR Inheritance
- Mitochondrial stress can be inherited
- Epigenetic mechanisms (histone modifications)
- Longevity effects

## Key Phenotypes

- **hsp-4::GFP** - UPR-ER reporter
- **hsp-6::GFP** - UPR-mt reporter
- **Developmental arrest** - L2 arrest in double mutants
- **Tunicamycin sensitivity** - ER stress sensitivity
- **Lifespan effects** - Mild stress can extend lifespan

## Key References

- Calfon M et al. (2002) Nature - XBP-1 splicing in worms
- Nargund AM et al. (2012) Science - ATFS-1 mechanism
- Taylor RC & Bharat T (2014) Cell - Cell non-autonomous UPR
- Xu D et al. (2024) G3 - UPR-ER protects against DNA damage
- Shpilka T & Bharat T (2024) Cell Reports - Germline UPR-mt regulation

## Disease Relevance

- **Diabetes** - ER stress in beta cells
- **Neurodegeneration** - Chronic UPR activation
- **Cancer** - UPR supports tumor growth
- **Aging** - Decline in UPR capacity

## Project Status

- [x] Create gene folders and fetch UniProt/GOA data
- [x] Priority 1 genes review (UPR-ER) - 6/6 genes COMPLETE
- [x] Priority 2 genes review (UPR-mt) - 5/5 genes COMPLETE (atfs-1 shared with MITOPHAGY)
- [x] Priority 3 genes review (regulators) - 6/6 genes COMPLETE
- [x] Pathway summary and integration

## Session Notes

### 2025-12-28: Project Completion

**Priority 1 - UPR-ER (6 genes):**
- ire-1: 40 annotations reviewed (33 ACCEPT, 6 KEEP_AS_NON_CORE, 1 MARK_AS_OVER_ANNOTATED)
- xbp-1: Complete review with core functions documented
- pek-1: 30 annotations reviewed (27 ACCEPT, 3 KEEP_AS_NON_CORE)
- atf-6: 20 annotations reviewed; **KEY FINDING**: ATF-6 deletion extends lifespan 43-57% via ER-mitochondrial calcium signaling
- hsp-4: 25 annotations reviewed; BiP/GRP78 ER chaperone, major UPR marker (hsp-4::GFP)
- atf-4: 17 annotations reviewed (13 ACCEPT, 2 MODIFY, 2 NEW); ISR effector, regulates H2S biosynthesis

**Priority 2 - UPR-mt (5 genes + atfs-1 from MITOPHAGY):**
- dve-1: 31 annotations reviewed; works with UBL-5 for chromatin remodeling
- ubl-5: 11 annotations reviewed; **CRITICAL FIX**: Removed protein tag activity (GO:0031386) - UBL-5 lacks C-terminal di-Gly motif required for covalent conjugation; functions via non-covalent interactions
- hsp-6: 19 annotations reviewed; mtHSP70, standard UPR-mt marker
- hsp-60: 21 annotations reviewed; **ERROR CORRECTED**: Removed GO:0061629 (TF binding) - paper described DVE-1 binding hsp-60 PROMOTER, not HSP-60 protein
- clpp-1: 16 annotations (ALL ACCEPT); ClpXP protease generates UPR-mt signaling peptides

**Priority 3 - Regulators (6 genes):**
- gcn-2: 26 annotations reviewed; GCN2 kinase for amino acid sensing and ISR
- met-2: 32 annotations reviewed; SETDB1 H3K9 methyltransferase for transgenerational inheritance
- jmjd-3.1: Multiple annotations; **FIXED**: Removed GO:0000978 (DNA binding) - no intrinsic DNA-binding domains; added stress response functions
- ocr-2: 21 annotations reviewed; TRPV channel in sensory neurons for non-cell autonomous signaling
- abu-1: 6 annotations (ALL ACCEPT); Alternative UPR when canonical IRE-1/XBP-1 blocked
- lin-65: 6 annotations + 1 NEW; nuclear co-factor working with MET-2 for chromatin

**Key Biological Insights:**
1. UBL-5/Hub1 is NOT a true ubiquitin modifier - functions via non-covalent protein interactions
2. ATF-6 links ER-mitochondrial calcium homeostasis to longevity (43-57% lifespan extension)
3. JMJD-3.1 acts locus-specifically in stress response (unlike UTX-1 global developmental regulator)
4. OCR-2 requires OSM-9 heteromerization for polymodal sensory function
5. MET-2/LIN-65 complex establishes H3K9me2 marks for transgenerational UPR-mt inheritance
