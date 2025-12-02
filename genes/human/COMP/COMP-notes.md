# COMP (Cartilage Oligomeric Matrix Protein) - Gene Review Notes

## Gene Identity
- **UniProt ID**: P49747
- **Gene Symbol**: COMP (should be fixed from P49747 in YAML)
- **Alternative Names**: Thrombospondin-5 (TSP5)
- **Protein Family**: Thrombospondin family
- **Organism**: Homo sapiens

## Core Function Summary

COMP is a pentameric extracellular matrix (ECM) glycoprotein with dual functions:

### 1. Extracellular Structural Role
- **Primary function**: ECM organization and collagen fibril assembly in load-bearing tissues (cartilage, tendon, ligament) [PMID:18285447, deep research]
- **Molecular bridging**: Links multiple ECM components (collagens I/II/IX/XII/XIV, fibronectin, matrilins, aggrecan, proteoglycans) through pentameric structure [deep research]
- **Tissue specificity**: Highly expressed in cartilage, tendon, ligament, synovium - all load-bearing tissues [deep research]

### 2. Intracellular Function
- **Novel discovery**: Facilitates collagen secretion from endoplasmic reticulum (ER) [deep research "COMP-assisted collagen secretion"]
- **Evidence**: COMP-deficient fibroblasts show dilated ER cisternae with accumulated collagen; introducing WT COMP rescues secretion [deep research]
- **Mechanism**: Forms intracellular COMP-collagen complexes that facilitate trafficking through secretory pathway [deep research]

## Molecular Architecture

### Pentameric Structure
- Five identical subunits (~757 AA each, total ~550 kDa) assembled via N-terminal coiled-coil domain [deep research]
- Flower-like appearance with 5 monomers radiating from central stalk [deep research]
- Stabilized by intersubunit disulfide bonds at C-terminal end of coiled-coil heptad repeats [deep research]

### Domain Organization (N→C terminus)
1. **Coiled-coil domain**: Pentamerization, contains Cys36-Cys97 intrasubunit disulfide bond [deep research]
2. **Four EGF-like repeats**: Protein-protein interactions, calcium binding [deep research]
3. **Type 3 calcium-binding repeats** (13 repeats): 21 closed + 5 open Ca²⁺-binding sites; critical for structure [deep research]
4. **C-terminal lectin-like domain**: β-sandwich structure; primary ligand-binding site; contains MIDAS (metal-ion-dependent adhesion site) conserved across all thrombospondins [deep research]

### Post-Translational Modifications
- **N-glycosylation**: Asn101, Asn721 - essential for folding/secretion; loss causes mild MED [deep research]
- **O-glycosylation**: EGF-like repeats (O-glucose, O-fucose, O-GlcNAc) [deep research]
- **Disulfide bonds**: Sequential formation drives proper folding before pentamer assembly [deep research]

## Binding Partners and Interactions

### Collagens (Zn²⁺/Ni²⁺-dependent)
- Binds collagens I, II, IX, XII, XIV via C-terminal domain [deep research]
- **Function**: Organizes fibril networks; bridges collagen I and collagen XII [deep research]
- **Evidence from KO mice**: COMP-null mice show increased fibril diameter, reduced packing, disorganized growth plates [deep research]
- **Direct catalysis**: Promotes collagen fibrillogenesis in vitro [deep research]

### Other ECM Components (Mn²⁺/Ca²⁺-dependent for fibronectin)
- **Fibronectin**: Matrix-matrix interaction [PMID:12225811]
- **Matrilins** (matrilin-1, -3, -4): Mutations in COMP/matrilin-3/collagen IX all cause skeletal dysplasias [PMID:15075323, deep research]
- **Aggrecan**: Direct binding [PMID:17588949, deep research]
- **Proteoglycans**: Binds lubricin [PMID:29030641], chondroitin sulfate, heparin/heparan sulfate [PMID:17588949, deep research]

### Cell Surface Receptors
- **Integrins α5β1 and αvβ3**: RGD-mediated cell attachment [deep research]
- **Calcium-dependent conformation change**: Modulates which integrin is recognized [deep research]
- **CD47**: Reactome pathway annotation [Reactome:R-HSA-2426259]

## Cellular Localization

### Extracellular Compartments
- **ECM (primary)**: Extracellular matrix proper [PMID:18285447, PMID:20551380 (HDA), multiple IBA/IEA]
- **Extracellular space**: Secreted protein [PMID:32747625 (IDA), PMID:20551380 (HDA)]
- **Extracellular region**: General secreted localization [PMID:32747625 (IDA), multiple Reactome TAS]
- **Extracellular exosome**: Found in exosomes [PMID:23533145 (HDA)]
- **Pericellular matrix (PCM)**: Organizes chondrocyte microenvironment; critical for mechanotransduction [deep research]

### Intracellular (ER/Golgi)
- Transiently present during collagen secretion facilitation [deep research]

## Biological Processes

### Skeletal Development (Core Function)
- **Skeletal system development**: Essential for proper bone/cartilage development [PMID:7670472 (TAS), IEA annotations]
- **Cartilage development**: Direct role [GO:0051216]
- **Endochondral bone growth**: Growth plate organization [GO:0003416]
- **Growth plate cartilage development**: COMP-null mice show disorganized growth plates [GO:0003417]
- **Bone morphogenesis**, **bone growth**, **ossification**: Developmental skeletal processes [multiple IEA]
- **Limb development**: Demonstrated experimentally [PMID:16542502 (IDA)]
- **Chondrocyte development/proliferation**: Regulates under BMP-2 influence [GO:0002063, GO:0035988, GO:1902732]

### ECM Organization (Core Function)
- **Collagen fibril organization**: Directly demonstrated [GO:0030199]
- **Cartilage homeostasis**: Maintains cartilage ECM [PMID:32747625 (IDA)]
- **Bone mineralization** and **regulation of bone mineralization**: Structural role in mineralization [GO:0030282, GO:0030500]

### Cell Adhesion and Signaling
- **Cell adhesion**: Integrin-mediated [GO:0007155]
- **BMP signaling pathway**: Functions in BMP signaling context [GO:0030509]
- **Regulation of gene expression**: Through mechanotransduction [GO:0010468]

### Mechanotransduction (Important Context)
- COMP expression upregulated by mechanical loading [deep research "mechano-responsive promoter region"]
- Essential for pericellular matrix organization that transduces biomechanical signals to chondrocytes [deep research]
- β1-integrin-mediated mechanotransduction; lost when integrin blocked [deep research]

### Protein Processing and Secretion
- **Protein secretion**: Facilitates collagen export from ER (intracellular function) [GO:0009306]
- **Protein processing**: Related to collagen secretion facilitation [GO:0016485]

### Other Annotated Processes (Need Review)
- **Apoptotic process** (GO:0006915 IEA) - COMP protects cells against death [PMID:17993464 "elevating IAP family"]
- **Blood coagulation** (GO:0007596 IEA) - May relate to platelet aggregation
- **Platelet aggregation** (GO:0070527 IEA) - Needs evidence review
- **Response to unfolded protein** (GO:0006986 IEA) - Relates to ER retention in disease states
- **Vascular smooth muscle** processes (GO:0014829, GO:0097084) - COMP expressed in vascular SMC, mechanosensitive [deep research]
- **Artery morphogenesis** (GO:0048844 IEA)
- **Skin development** (GO:0043588 IEA) - COMP in skin, role in fibrosis/scar formation [deep research]
- **Tendon development** (GO:0035989 IEA) - COMP highly expressed in tendon [deep research]
- **Muscle processes** (GO:0050881, GO:0050905, GO:0055001) - Likely over-annotations
- **Cellular senescence** (GO:0090398 IEA) - Needs review
- **Negative regulation of hemostasis** (GO:1900047 IEA) - Needs review

## Molecular Functions

### Core MF (Structural)
- **Extracellular matrix structural constituent**: Primary MF [PMID:20551380 (RCA), PMID:7713493 (TAS)]
- This is the most accurate descriptor of COMP's molecular activity

### Binding Functions
- **Calcium ion binding**: Multiple EGF and type 3 repeats; experimentally verified [PMID:10852928, PMID:11084047, PMID:7670472 (all IDA/TAS)]
- **Collagen binding**: Direct binding to collagens I/II/IX [PMID:11084047 (IDA)]
- **Heparin binding**: Direct binding [PMID:17588949 (IDA)]
- **Heparan sulfate proteoglycan binding**: Direct binding [PMID:17588949 (IDA)]
- **Proteoglycan binding**: Lubricin, aggrecan [PMID:29030641 (IDA)]
- **Integrin binding**: α5β1, αvβ3 [IEA]
- **BMP binding**: Facilitates BMP signaling [GO:0036122 IEA]
- **Protease binding**: Binds ADAMTS proteases [PMID:18485748 (IPI)]

### Protein Binding (Non-informative)
- **GO:0005515 protein binding** - Multiple IPIs but this term should be avoided per curation guidelines
- Should be replaced with more specific terms (integrin binding, collagen binding, etc.)

### Oligomerization
- **Protein homooligomerization**: Pentameric assembly [PMID:32747625 (IDA), GO:0051260]

## Disease Associations

### Skeletal Dysplasias (Genetic)
- **Pseudoachondroplasia (PSACH)**: Autosomal dominant; short-limbed dwarfism, joint pain
- **Multiple Epiphyseal Dysplasia (MED)**: Autosomal dominant form
- **Mutations**: >60 mutations, mostly in type III calcium-binding repeats (exons 8-14)
- **Most common mutation**: p.469-473delD (GAC deletion in CLR7) - ~1/3 of PSACH patients
- **Pathomechanism**:
  - Mutations disrupt Ca²⁺ binding → misfolding
  - Mutant COMP retained in ER → ER stress
  - Intracellular matrix accumulation
  - Increased chondrocyte apoptosis
  - Abnormal ECM → early-onset osteoarthritis
  - Dominant negative effect (most pentamers contain ≥1 mutant subunit)

### Osteoarthritis (OA) Biomarker
- **Serum COMP elevation**: Reflects cartilage degradation [deep research]
- **Diagnostic utility**:
  - OA patients: median 1117 ng/ml vs controls: 339 ng/ml
  - Correlates with disease severity (Kellgren-Lawrence grade)
  - Correlates with joint involvement, age, BMI, pain score, IL-1β
  - Highest in first 3 years of disease
- **Gender difference**: 52% higher in males
- **Clinical value**: Early OA detection, progression monitoring

### Other Disease Associations
- **Fibrotic diseases**: Elevated in systemic sclerosis, keloids, scleroderma [deep research]
- **Vascular disease**: Upregulated in atherosclerosis, carotid stenosis [deep research]
- **Carpal tunnel syndrome**: Familial form associated with COMP mutations [PMID:32747625 title]

## Regulation

### Mechanical Loading
- Upregulated by compression, cyclic tensile strain [deep research]
- Mechano-responsive promoter region [deep research]
- Integrin-dependent mechanotransduction (β1-integrin essential) [deep research]

### Growth Factors
- **TGF-β**: COMP facilitates TGF-β signaling; pentameric structure allows multivalent presentation [deep research]
- **BMP-2**: Regulates COMP expression; COMP modulates BMP signaling [deep research]

### Inflammatory Signals
- **NF-κB**: Dynamic tensile strain regulates NF-κB; low magnitude inhibits inflammation, high magnitude promotes [deep research]

## Evolutionary Context
- Member of thrombospondin family (TSP-5)
- Pentameric subgroup (TSP-3, TSP-4, TSP-5/COMP) vs trimeric (TSP-1, TSP-2)
- C-terminal region highly conserved across all thrombospondins
- MIDAS site conserved - ancestral binding mechanism
- Pentameric assembly arose early in metazoan evolution

## Key Experimental Evidence

### Mouse Models
- **COMP-null mice**:
  - Viable but show altered collagen fibril morphology
  - Increased fibril diameter, reduced packing
  - Disorganized growth plates
  - Altered mechanical properties in skin/tendon
  - ER dilation with accumulated collagen in fibroblasts
  - Abnormal matrilin-3 integration into cartilage

- **COMP-mutant mice** (PSACH model):
  - Recapitulates human disease
  - ER retention of ECM proteins
  - Intracellular matrix formation
  - Increased chondrocyte apoptosis

### In Vitro Studies
- COMP promotes collagen fibrillogenesis (catalytic role)
- COMP-null fibroblasts: Collagen accumulation in ER, rescued by WT COMP introduction
- Integrin-mediated chondrocyte attachment requires COMP
- Mechanical compression upregulates COMP transcription

## References to Check

Publications already in YAML references section that need findings extracted:
- PMID:10852928 - Calcium binding, type 3 repeats, conformational changes
- PMID:11084047 - Mutations affect Ca²⁺ and collagen I/II/IX binding
- PMID:12225811 - COMP-fibronectin interaction
- PMID:15075323 - COMP-matrilin interactions
- PMID:16051604 - Chondrocyte attachment via integrins
- PMID:16542502 - Limb development
- PMID:16611630 - ADAMTS-12 degrades COMP
- PMID:17588949 - Aggrecan interaction, heparin binding
- PMID:17993464 - Anti-apoptotic, elevates IAP family
- PMID:18285447 - ECM retention
- PMID:18485748 - ADAMTS-7/12 degradation, α2-macroglobulin inhibition
- PMID:29030641 - Lubricin binding
- PMID:32747625 - Homooligomerization, cartilage homeostasis, familial carpal tunnel
- PMID:7670472 - PSACH/MED mutations
- PMID:7713493 - Characterization, ECM structural constituent
- Reactome:R-HSA-2424252 - COMP binding partners
- Reactome:R-HSA-2426259 - COMP-integrin/CD47 binding

## Curation Strategy

### ACCEPT as Core Functions
1. Extracellular matrix structural constituent (MF)
2. ECM localization
3. Calcium ion binding
4. Collagen binding
5. Skeletal system development
6. Cartilage development/homeostasis
7. Collagen fibril organization
8. Protein homooligomerization

### MODIFY to More Specific Terms
1. "Protein binding" (GO:0005515) → Should reference more specific binding terms already annotated or suggest removal

### KEEP_AS_NON_CORE (Pleiotropic/Developmental)
1. Limb development (developmental context)
2. Bone mineralization processes (structural context, not enzymatic)
3. Various tissue development processes (tendon, skin, etc.)
4. Chondrocyte proliferation/development (regulatory, not core catalytic activity)

### REMOVE or MARK_AS_OVER_ANNOTATED
1. Generic processes without strong direct evidence (e.g., "multicellular organism growth", "musculoskeletal movement", "neuromuscular process")
2. "Protein binding" annotations (replace with specific binding partners)

### UNDECIDED (Need More Literature Review)
1. Apoptotic process annotations - COMP has anti-apoptotic role but is this core function?
2. Blood coagulation/platelet aggregation - indirect through ECM?
3. Vascular smooth muscle annotations - COMP is expressed there but is it core?
4. Cellular senescence
5. Some regulatory processes

## Questions for Further Investigation

1. Is the anti-apoptotic function (IAP elevation) a core function or a secondary effect of ECM interactions?
2. What is the specific mechanism of COMP in blood coagulation/platelet aggregation?
3. Should the intracellular collagen secretion function be captured with a new annotation?
4. Are the vascular SMC functions significant enough to be core, or are they tissue-specific pleiotropic effects?
