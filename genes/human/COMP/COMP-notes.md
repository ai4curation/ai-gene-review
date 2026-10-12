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


---

## 2026-10-12: source-based reassessment

The preceding journal is retained verbatim as historical research notes. The current assessment below supersedes its provisional curation strategy and any conflicting biological shorthand. In particular, the older references to generic “deep research” do not independently establish the numerical domain/modification claims, universal normal-cartilage indispensability, or mouse-null growth-plate and ER-rescue phenotypes. Mutant toxicity must not be relabeled as a null phenotype. The limb-development paper establishes localization with a speculative functional interpretation; it does not demonstrate the developmental step. Free heparan sulfate is distinct from an intact heparan-sulfate proteoglycan. The integrin experiment's reducing conditions matter. PMID32747625 is a correction notice, and its biological original is PMID32686688. A Reactome event mentioning CD47 does not itself establish a COMP–CD47 contact. These qualifications and the source-specific decisions below govern the current review; the historical lists are not additional evidence.

### Matrix assembly, ligand specificity and source limits

COMP is a secreted thrombospondin-family glycoprotein whose N-terminal assembly region produces a multivalent pentamer. Its collagen and other matrix interactions support one integrated extracellular-matrix structural function. In the original bovine fibrillogenesis experiment, native pentamer and an N-terminally truncated recombinant monomer have different effects on early collagen assembly. This is performed organization, rather than merely the presence of COMP in a tissue. It supports the existing collagen-fibril-organization process without creating a separate enzyme or generic scaffold assertion. Human matrix detection and full-length assembly corroborate the tissue role. [PMID:17716974](https://pubmed.ncbi.nlm.nih.gov/17716974/), [PMID:20551380](https://pubmed.ncbi.nlm.nih.gov/20551380/), [PMID:32686688](https://pubmed.ncbi.nlm.nih.gov/32686688/).

The two official products are not experimentally interchangeable. Displayed P49747-1 contains 757 residues; P49747-2 contains 704 after deletion of canonical 129–181. That removes most of EGF-like domain 2 and a small adjacent segment. The signal sequence, N-terminal oligomer region and C-terminal domain remain, but equal folding, secretion, calcium occupancy and ligand activity have not been demonstrated. The human signature-domain crystal uses A225–A757; its packing trimer is explicitly nonbiological and does not replace evidence for full-length pentamers. [PMID:19276170](https://pmc.ncbi.nlm.nih.gov/articles/PMC2717772/).

Ligand assays require specific reagent descriptions. The original glycosaminoglycan study tested free bovine-kidney heparan sulfate, supporting heparan-sulfate binding; it did not thereby demonstrate an intact heparan-sulfate proteoglycan. The separately tested whole aggrecan carries chondroitin/keratan sulfate and supports the chondroitin-sulfate-proteoglycan class. Its two database accessions do not establish separately documented human and bovine preparations. In the attachment study, calcium-replete COMP acts through alpha5beta1, while the alphavbeta3 result uses calcium-depleted **and DTT-reduced** COMP. Surface-receptor immunoprecipitation is not a purified COMP–integrin binding measurement. [PMID:17588949](https://pmc.ncbi.nlm.nih.gov/articles/PMC2905148/), [PMID:16051604](https://pmc.ncbi.nlm.nih.gov/articles/PMC2896261/).

The positive interaction screens are preserved with exact product and assay scope. OTX1 and MEOX2 support a DNA-binding transcription-factor partner class; the tested MEOX2 accession Q6FHY5 is 303 residues and differs from curated P50222 only by a pre-homeobox glutamine. ATOX1's corresponding class is inferred from mouse evidence. AQP1 is a transmembrane transporter. These refinements do not make COMP a transcription factor, channel regulator or physiological nuclear partner. The Fragoza record contains a COMP residue 386 variant marked as having no effect on the tested OTX1 interaction. CYSRT1, NUFIP2 and SGTB remain positive generic interactions where the saved evidence does not resolve a more informative class; SGTB binding/regulation of Hsp70 does not itself prove unfolded-client chaperone function. [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), [PMID:31515488](https://pubmed.ncbi.nlm.nih.gov/31515488/).

Contextual survival and developmental roles remain separate from the structural core. Human culture experiments support an anti-apoptotic effect with IAP changes and XIAP/survivin knockdown dependence. They do not establish direct COMP–IAP binding, direct caspase inhibition or a particular integrin receptor. In contrast, controlled human embryonic localization supplies no performed limb-development assay, and the source itself leaves the functional inference open. Mouse mutant growth plates and tendons show real matrix, proliferation and stress phenotypes, but normal structural participation and toxic-mutant effects must be separated for each transferred process. [PMID:17993464](https://pubmed.ncbi.nlm.nih.gov/17993464/), [PMID:16542502](https://pubmed.ncbi.nlm.nih.gov/16542502/), [PMID:17588960](https://pubmed.ncbi.nlm.nih.gov/17588960/), [PMID:19808781](https://pubmed.ncbi.nlm.nih.gov/19808781/).

PMID32747625 is an affiliation correction. Its original source identifier is preserved, while biological support is attributed to the explicitly linked original PMID32686688. Human full-length COMP and a separate rat coiled-coil construct are distinguished. Affected cartilage or tendon phenotypes do not establish universal normal cartilage indispensability. Other access limits are equally source-specific: some genuine caches omit Methods despite a full-text flag; the aorta target tables were actually read, while the exact COMP exosome and vein supplements remain unverified. Positive experimental annotations are not rejected solely because those target supplements were unavailable.

The source record contains 104 assertions: 63 current and 41 retired historical records. Retirement marks 36 absent historical assertions and five collapsed interaction groups; it is not a biological REMOVE decision. All 79 historical source objects retain their original fields, including omitted support lists. Exact current source objects remain separately represented, so one aggregate is not silently equated with several individual partners. Current ARBA branches match the official target; the historical PAINT node placement could not be independently recovered. Target matrix evidence supports the accepted structural inference without counting donors or treating a self-source as circular.

[The source-evidence index](COMP-source-evidence.json) provides exact reconciliation, official definitions, product/interaction identities, current donor records, the two distinct Reactome participant paths, original aorta table cells and source-access locators. New primary excerpts are kept in the YAML without duplication in this appendix or the evidence index.
