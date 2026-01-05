# C. elegans Mitophagy & Mitochondrial Quality Control Project

## Overview

Mitophagy is the selective autophagy of damaged mitochondria, essential for maintaining a healthy mitochondrial population. *C. elegans* has conserved mitophagy pathways and is particularly valuable for studying the interplay between mitophagy, aging, and neurodegeneration.

The PINK1-Parkin pathway, originally discovered through Parkinson's disease genetics, is well-conserved in worms. Recent work connects mitophagy to ferroptosis regulation, longevity pathways, and stress responses.

## Model Species

**Primary: Caenorhabditis elegans (worm)**
- UniProt species code: CAEEL
- Conserved mitophagy pathways
- Parkinson's disease models
- Aging-mitophagy connections

## Core Pathway Architecture

### 1. PINK1-Parkin Pathway
Canonical mitophagy initiation:
- **pink-1** - PINK1 kinase (accumulates on damaged mito)
- **pdr-1** - Parkin E3 ligase (recruited by PINK1)
- **miro-1** - Miro GTPase (mitochondrial transport, Parkin substrate)

### 2. Mitophagy Receptors
Direct autophagosome recruitment:
- **dct-1** - BNIP3L/NIX ortholog (primary receptor)
- **fundc-1** - FUNDC1 ortholog (hypoxia-induced)

### 3. Mitochondrial Dynamics
Fission/fusion machinery (required for mitophagy):
- **drp-1** - DRP1/Dynamin-related (fission)
- **fzo-1** - Mitofusin (outer membrane fusion)
- **eat-3** - OPA1 ortholog (inner membrane fusion)
- **fis-1** - FIS1 (fission factor)
- **fis-2** - MFF ortholog (fission)
- **mff-1** - MFF ortholog

### 4. Core Autophagy Machinery
Shared with other autophagy pathways:
- **bec-1** - Beclin ortholog
- **lgg-1** - LC3/GABARAP
- **lgg-2** - LC3/GABARAP family
- **atg-18** - WIPI1/2 ortholog
- **epg-5** - Autophagy gene
- **sqst-1** - p62/SQSTM1 receptor

### 5. Mitochondrial UPR Connection
Stress response coordination:
- **atfs-1** - ATFS1 (UPR-mt vs mitophagy decision)
- **hsp-6** - mtHSP70
- **clpp-1** - ClpP protease

### 6. Longevity-Mitophagy Axis
- **daf-2** - Insulin receptor (reduced signaling increases mitophagy)
- **daf-16** - FOXO (promotes mitophagy genes)
- **skn-1** - Nrf2 ortholog
- **hlh-30** - TFEB ortholog (autophagy/lysosome TF)
- **sir-2.1** - SIRT1 (deacetylase)

### 7. Mitochondrial Import/Proteostasis
- **tin-44** - TIM44 (import machinery)
- **tomm-22** - TOM22 (import machinery)
- **spg-7** - SPG7/Paraplegin (m-AAA protease)
- **phb-1/phb-2** - Prohibitins

### 8. ROS and Damage Sensing
- **sod-2** - Mn-SOD (mitochondrial)
- **sod-3** - Fe-SOD
- **clk-1** - COQ7 (ubiquinone synthesis)
- **isp-1** - Rieske iron-sulfur protein

## Genes for Review (Priority Order)

### Priority 1: Core Mitophagy Pathway (~6 genes)
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| pink-1 | Q09298 | PINK1 | Kinase, damage sensor | ✓ REVIEWED |
| pdr-1 | Q9XUS3 | PRKN/Parkin | E3 ligase | ✓ REVIEWED |
| dct-1 | Q09969 | BNIP3L/NIX | Mitophagy receptor | ✓ REVIEWED |
| drp-1 | Q8WQC9 | DNM1L/DRP1 | Mitochondrial fission | ✓ REVIEWED |
| fzo-1 | Q23424 | MFN1/2 | Mitochondrial fusion | ✓ REVIEWED |
| eat-3 | Q18965 | OPA1 | Inner membrane fusion | ✓ REVIEWED |

### Priority 2: Autophagy Machinery (~6 genes)
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| bec-1 | O16351 | BECN1 | Autophagy initiation | ✓ REVIEWED |
| lgg-1 | Q9XYN3 | MAP1LC3 | Autophagosome marker | ✓ REVIEWED |
| lgg-2 | O02053 | GABARAPL2 | Autophagosome | ✓ REVIEWED |
| sqst-1 | G5ECN6 | SQSTM1/p62 | Cargo receptor | ✓ REVIEWED |
| atg-18 | O16466 | WIPI1/2 | PI3P binding | ✓ REVIEWED |
| epg-5 | Q18892 | EPG5 | Autophagosome maturation | ✓ REVIEWED |

### Priority 3: Longevity & Regulation (~5 genes)
| Gene | UniProt | Human Ortholog | Function | Status |
|------|---------|----------------|----------|--------|
| atfs-1 | Q23272 | ATF5 | UPR-mt/mitophagy switch | ✓ REVIEWED |
| hlh-30 | H2KZZ2 | TFEB | Autophagy TF | ✓ REVIEWED |
| skn-1 | P34707 | NFE2L2/Nrf2 | Stress response TF | ✓ REVIEWED |
| miro-1 | Q94263 | RHOT1/2 | Mito transport/Parkin target | ✓ REVIEWED |
| spg-7 | Q9N3T5 | AFG3L2 | m-AAA protease | ✓ REVIEWED |

**Note:** fundc-1 was listed but has no clear C. elegans ortholog in UniProt.

## Key Biological Concepts

### PINK1-Parkin Mechanism
1. PINK1 accumulates on depolarized mitochondria
2. PINK1 phosphorylates ubiquitin and Parkin
3. Parkin ubiquitinates outer membrane proteins
4. Autophagy receptors recognize ubiquitin chains
5. Autophagosome engulfs mitochondrion

### DCT-1/BNIP3L Receptor Pathway
- Direct receptor on mitochondrial outer membrane
- LIR motif binds LC3/LGG-1
- Regulated by phosphorylation
- Important in hypoxia

### Mitophagy vs UPR-mt Decision
- ATFS-1 normally imported into mitochondria and degraded
- Mitochondrial damage prevents import
- ATFS-1 translocates to nucleus
- Activates either repair (UPR-mt) or elimination (mitophagy)

### Heat Shock Induces Mitophagy
- Acute heat shock (37C) causes mitochondrial fragmentation
- DCT-1, PINK-1, PDR-1 dependent process
- Clears damaged mitochondria

## Key Phenotypes

- **Mitophagy reporters** - mito-GFP/mCherry flux
- **Parkinson's model** - Dopaminergic neuron loss
- **Mitochondrial morphology** - Fragmentation/hyperfusion
- **Lifespan** - Often extended by mild mitochondrial stress
- **Rotenone sensitivity** - Complex I inhibitor sensitivity

## Key References

- Palikaras K et al. (2015) Nature - DCT-1 receptor discovery
- Springer & Bharat (2017) eLife - PINK-1/PDR-1 in worms
- Schiavi A et al. (2015) Cell Rep - Mitophagy and longevity
- Luz AL & Bharat T (2020) Redox Biol - Mitophagy in aging
- Bratic I & Trifunovic A (2010) - Mitochondrial aging

## Disease Relevance

- **Parkinson's disease** - PINK1/Parkin mutations
- **Aging** - Mitochondrial dysfunction accumulation
- **Neurodegeneration** - General mitochondrial quality control
- **Cardiomyopathy** - Tissue-specific mitophagy requirements

## Project Status

- [x] Create gene folders and fetch UniProt/GOA data
- [x] Priority 1 genes review (core mitophagy)
- [x] Priority 2 genes review (autophagy machinery)
- [x] Priority 3 genes review (longevity regulation)
- [x] Pathway summary and integration (see CAEEL_MITOPHAGY-pathway.md)

---
# STATUS

## 2025-12-27 - Priority 1 COMPLETE

All 6 core mitophagy genes reviewed:

### Priority 1 Summary:
- **pink-1** (Q09298): PINK1 kinase - 26 annotations reviewed, 21 ACCEPT, 6 KEEP_AS_NON_CORE. Core mitophagy initiator and kinase.
- **pdr-1** (Q9XUS3): Parkin E3 ligase - 37 annotations reviewed, 24 ACCEPT, 6 KEEP_AS_NON_CORE, 3 MODIFY, 2 MARK_AS_OVER_ANNOTATED. Works with PINK-1 in mitophagy pathway.
- **dct-1** (Q09969): BNIP3L/NIX receptor - 26 annotations reviewed, 14 ACCEPT, 8 KEEP_AS_NON_CORE, 1 NEW (GO:0140580 mitochondrion autophagosome adaptor activity). Key mitophagy receptor with LIR-like motif.
- **drp-1** (Q8WQC9): DRP1 fission GTPase - 28 annotations reviewed, 22 ACCEPT, 4 KEEP_AS_NON_CORE, 2 REMOVE (microtubule annotations). Required for isolating damaged mitochondria.
- **fzo-1** (Q23424): Mitofusin - 13 annotations reviewed, all ACCEPT/KEEP. Outer membrane fusion GTPase.
- **eat-3** (Q18965): OPA1 ortholog - 26 annotations reviewed, 14 ACCEPT, 6 KEEP_AS_NON_CORE, 5 REMOVE (peroxisome, microtubule), 1 NEW (GO:1990627 inner membrane fusion). Inner membrane fusion, cristae maintenance.

### Key Findings:
1. PINK-1/PDR-1/DCT-1 form the core mitophagy signaling axis
2. DRP-1 fission is required to isolate damaged mitochondria
3. FZO-1/EAT-3 fusion opposes fission for mitochondrial morphology balance
4. Several incorrect annotations inherited from other dynamins (microtubule-related) were removed from drp-1 and eat-3
5. DCT-1 acts as the primary mitophagy receptor via its LIR-like WXXL motif

# NOTES

## 2025-12-27
- Project initiated
- Fetched data for all 6 Priority 1 genes
- Ran deep research (falcon provider) for all genes
- Completed systematic annotation review for all Priority 1 genes
- Key pathway connections established between genes

## 2025-12-28 - Priority 2 COMPLETE

All 6 autophagy machinery genes reviewed:

### Priority 2 Summary:
- **bec-1** (O16351): Beclin ortholog - VPS34 complex subunit for PI3P generation at phagophores. Required for autophagy, endocytic sorting, and apoptotic cell clearance.
- **lgg-1** (Q9XYN3): GABARAP family - Ubiquitin-like modifier conjugated to phagophore membrane. Operates upstream of LGG-2 in autophagosome formation.
- **lgg-2** (O02053): LC3 family - Autophagosome membrane protein. Acts downstream of LGG-1, directly binds VPS-39/HOPS for lysosome tethering.
- **sqst-1** (G5ECN6): p62/SQSTM1 ortholog - Selective autophagy receptor with UBA and LIR domains. Links ubiquitinated cargo to LGG-1.
- **atg-18** (O16466): WIPI1/2 ortholog - PROPPIN family PI3P effector with FRRG motif. Distinct from EPG-6 in autophagosome formation. Functions in apoptotic cell clearance, xenophagy.
- **epg-5** (Q18892): Metazoan-specific autophagy factor - RAB-7 effector that promotes autophagosome-lysosome fusion. SNARE binding coordinates trans-SNARE complex assembly.

### Key Findings:
1. LGG-1 (GABARAP) acts upstream of LGG-2 (LC3) in C. elegans - opposite order to some mammalian models
2. LGG-2 directly binds VPS-39/HOPS for lysosome tethering, specialized maturation role
3. ATG-18 and EPG-5 both function in LAP (LC3-associated phagocytosis) for apoptotic cell clearance
4. EPG-5 is a RAB-7 effector that coordinates SNAREs for autophagosome-lysosome fusion specificity
5. SQST-1 is the primary selective autophagy receptor, potentially targets paternal mitochondria

## 2025-12-28 - Priority 3 COMPLETE

All 5 longevity & regulation genes reviewed (fundc-1 omitted - no clear C. elegans ortholog):

### Priority 3 Summary:
- **atfs-1** (Q23272): ATFS1 transcription factor - Master regulator of UPR-mt. Dual targeting (MTS+NLS) allows import-efficiency sensing. Under stress, accumulates in nucleus to activate mitochondrial chaperones, proteases, and immune genes. Degraded by LONP-1 in healthy mitochondria.
- **hlh-30** (H2KZZ2): TFEB ortholog - bHLH transcription factor for autophagy/lysosome biogenesis and longevity. Required for lifespan extension in 6 distinct paradigms. Activated by starvation, infection (S. aureus), heat stress. Drives ~80% of host defense response.
- **skn-1** (P34707): Nrf1/Nrf2 ortholog - CNC/bZIP transcription factor for oxidative stress and xenobiotic responses. Activates phase II detoxification genes. Nuclear localization regulated by phosphorylation; GSK-3 and IIS pathway suppress activity.
- **miro-1** (Q94263): Miro GTPase - Outer mitochondrial membrane adaptor linking mitochondria to kinesin/dynein motors. Contains 2 GTPase domains and 2 calcium-sensing EF-hands. Parkin substrate; degradation arrests mitochondrial transport to quarantine damaged organelles.
- **spg-7** (Q9N3T5): m-AAA protease subunit - Actually ortholog of AFG3L2 (not human SPG7/paraplegin). Inner membrane metalloprotease for respiratory chain assembly and protein quality control. RNAi triggers UPR-mt via ATFS-1 activation.

### Key Findings:
1. ATFS-1 import-efficiency model: mitochondrial damage reduces import → nuclear accumulation → UPR-mt activation
2. HLH-30 integrates longevity, autophagy, lysosome biogenesis, and innate immunity in a unified transcriptional program
3. SKN-1 is the hub for oxidative stress response; overlaps with DAF-16/FOXO and HIF-1 networks
4. MIRO-1 serves as both mitochondrial transport adaptor AND mitophagy switch (degraded by Parkin to halt transport)
5. SPG-7 nomenclature is misleading - it's AFG3L2, not SPG7 ortholog; true SPG7 ortholog is ppgn-1

### Project Complete!
All 17 genes (6 + 6 + 5) across 3 priority levels have been reviewed. Only pathway summary integration remains.
