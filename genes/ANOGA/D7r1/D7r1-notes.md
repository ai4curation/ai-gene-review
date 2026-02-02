# D7r1 Review Notes - Anopheles gambiae

## Gene Overview

D7r1 (D7-related 1) is a short-form salivary protein from *Anopheles gambiae* (African malaria mosquito). It belongs to the PBP/GOBP (Pheromone/Odorant-Binding Protein) family.

## Key Literature Findings

### Core Function
D7r1 "modulates blood feeding of female mosquitoes on vertebrate species by binding and sequestering different mediators involved in the host response" [PMID:16301315, UniProt].

Specifically:
- Binds **serotonin** and **histamine** with high affinity [PMID:16301315]
- Increases blood clotting time [PMID:16301315]
- Acts as a "kratagonist" - sequesters host signaling molecules rather than blocking receptors

### Mechanism - Kratagonism
D7 proteins show a unique type of agonist inhibition called "kratagonism" - they bind biogenic amines (serotonin, histamine, norepinephrine, epinephrine) with high affinity, effectively sequestering them and preventing their action on host tissues.

From [PMID:17928288] (D7r4 crystal structure):
> "The D7r proteins bind the biogenic amines serotonin, norepinephrine, and histamine with high affinity"
> "The D7 fold consists of an arrangement of eight alpha-helices stabilized by three disulfide bonds"

### Tissue Expression
- Female salivary gland only [PMID:9990055, PMID:11841502]
- Not detected in male tissues
- Not detected in embryo, larval, or pupal stages

### Stoichiometry
D7 proteins bind ligands in a 1:1 stoichiometric ratio, which explains why they are among the most abundant components of mosquito salivary glands - they need to be at equimolar concentrations with host mediators (1-10 μM for histamine/serotonin).

### D7 Family in A. gambiae
- **Short forms (D7r1-5)**: Bind biogenic amines (serotonin, histamine, norepinephrine)
- **Long forms (D7L1-3)**: More diverse - bind leukotrienes, thromboxane A2, or serotonin
  - D7L1: binds leukotriene C4 and thromboxane A2 [PMID:35460690]
  - D7L2: weakly binds leukotrienes B4 and D4
  - D7L3: binds serotonin (first long-form to bind a biogenic amine)

## GO Annotation Assessment

### Current Annotations

1. **GO:0090729 (toxin activity)** - SPKW via GO_REF:0000043
   - UniProt keywords: "Blood coagulation cascade inhibiting toxin", "Hemostasis impairing toxin"

2. **GO:0005549 (odorant binding)** - InterPro via GO_REF:0000002
   - Based on PBP/GOBP family membership

3. **GO:0005576 (extracellular region)** - UniProt subcellular location via GO_REF:0000044
   - Protein is secreted into saliva

4. **GO:0035821 (modulation of process of another organism)** - GOC via GO_REF:0000108
   - Inferred from toxin activity annotation

### Critical Assessment: Is "toxin activity" appropriate?

**GO:0090729 definition**: "Interacting selectively with one or more biological molecules in another (target) organism, **initiating pathogenesis (leading to an abnormal, generally detrimental state)** in the target organism."

**Assessment**: D7r1 does NOT meet this definition because:
1. It does NOT initiate pathogenesis - it transiently modulates host physiology
2. It does NOT cause disease or tissue damage
3. Its effect is reversible and temporary (duration of feeding)
4. The host returns to normal state after feeding
5. The function evolved to facilitate feeding, not to harm the host

**However**: D7r1 DOES:
- Bind serotonin (GO:0051378)
- Bind histamine (GO:0051381)
- Negatively regulate hemostasis in the host (GO:1900047)
- Modulate processes in another organism (GO:0035821 - already annotated!)

### Recommended Actions

1. **GO:0090729 (toxin activity)**: MARK AS OVER-ANNOTATED
   - The term implies pathogenesis, which doesn't occur
   - More accurate: This is anti-hemostatic activity, not toxin activity

2. **GO:0005549 (odorant binding)**: MODIFY or KEEP_AS_NON_CORE
   - Based on structural family membership, but D7r1 doesn't actually function in olfaction
   - It binds biogenic amines as ligands, not odorants

3. **GO:0005576 (extracellular region)**: ACCEPT
   - Protein is secreted, this is accurate

4. **GO:0035821 (modulation of process of another organism)**: ACCEPT
   - Accurately describes the function

### Proposed New Annotations

1. **GO:0051378 (serotonin binding)** - MF
   - Evidence: PMID:16301315 demonstrates serotonin binding

2. **GO:0051381 (histamine binding)** - MF
   - Evidence: PMID:16301315 demonstrates histamine binding

3. **GO:1900047 (negative regulation of hemostasis)** - BP
   - Evidence: D7r1 increases clotting time [PMID:16301315]

## References

- PMID:16301315 - Function and evolution of mosquito salivary D7 protein family (key functional study)
- PMID:17928288 - Crystal structure of D7r4 with ligand complexes
- PMID:11841502 - D7 gene cluster in A. gambiae salivary glands
- PMID:9990055 - Initial identification of D7 proteins in A. gambiae
- PMID:35460690 - Long-form D7 protein functions in A. gambiae (2022)

## Sources

- [Novel salivary antihemostatic activities of long-form D7 proteins - JBC](https://www.jbc.org/article/S0021-9258(22)00411-2/fulltext)
- [D7r4 crystal structure - PubMed](https://pubmed.ncbi.nlm.nih.gov/17928288/)
- [Function and Evolution of Mosquito Salivary Protein Family - JBC](https://www.jbc.org/article/S0021-9258(20)70742-8/fulltext)
