# Neural and Glial Cell Fate Determination Project

## Overview

The development of the nervous system requires the coordinated generation of an astonishing diversity of cell types from a common pool of neural progenitors. Understanding how neural stem cells commit to becoming neurons versus glial cells (astrocytes, oligodendrocytes, Schwann cells), and how neuronal subtypes are specified, represents one of the central questions in developmental neurobiology. This project reviews the GO annotations for key genes involved in neural and glial cell fate decisions.

## Model Species

**Primary: Homo sapiens (human)**
- UniProt species code: HUMAN
- Well-characterized transcription factors and signaling pathways
- Clinical relevance for neurological disorders and regenerative medicine

**Secondary: Mus musculus (mouse)**
- Extensive genetic studies of neural development
- Lineage tracing and knockout studies

## GO Model for Neural/Glial Development: Classic Framework and Modern Challenges

### The Slack/Waddington Framework in GO

The Gene Ontology's cell development branch was designed over two decades ago, following the conceptual framework developed by Jonathan Slack (Slack 2011) and extending Waddington's epigenetic landscape metaphor (Waddington 2014). This classic embryological model posits a series of discrete, temporally ordered stages through which cells progress during development:

1. **Cell fate specification** (GO:0001708) - A reversible state where a cell becomes capable of differentiating autonomously in a neutral environment, but can still be redirected by extrinsic signals
2. **Cell fate determination** (GO:0001709) - An irreversible state where a cell will differentiate autonomously regardless of environment
3. **Cell fate commitment** (GO:0045165) - The final, heritable establishment of cell identity
4. **Differentiation** - Acquisition of specialized structural/functional features
5. **Morphogenesis** - Generation and organization of cell-type-specific structures

This framework envisions cells rolling down valleys in an epigenetic landscape, passing through discrete commitment points before reaching their final differentiated state.

### Challenges with the Classic Model

While the Slack framework has enabled valuable annotation work, several problems have become apparent:

**1. Operational difficulties in distinguishing stages**

Distinguishing 'specification' from 'commitment' from 'determination' requires specific experimental evidence (transplantation assays, neutral environment tests) that is often unavailable for genes being annotated. Curators frequently cannot determine whether a gene acts at the specification versus commitment stage based on the available literature. This has led to inconsistent curation practices across GO consortium members working with different model organisms.

**2. Single-cell studies reveal continuous trajectories**

Modern single-cell transcriptomic studies increasingly reveal that differentiation often proceeds as a continuous or branching trajectory rather than through discrete, temporally ordered commitment stages. For example:

- Hematopoietic stem cell lineage commitment appears continuous, with cells emerging directly from a "cloud" of low-primed progenitors without passing through discrete intermediate stages (Velten et al. 2017)
- Sister cells with near-identical transcriptomes can nonetheless be pre-committed to different fates, suggesting transcriptional state alone does not cleanly map onto classical fate commitment (Weinreb et al. 2020)
- Similar continuous trajectories have been reported in neural development, where single-cell RNA-seq shows gradual transitions rather than sharp boundaries

**3. Inconsistent granularity of cell type-specific terms**

Some GO terms correspond to well-established fate decisions with known molecular programs. For example, **neuron fate commitment** (GO:0048663) and **glial cell fate commitment** (GO:0021781) represent a genuine binary fate choice mediated by Notch-dependent lateral inhibition, with strong experimental support across multiple systems (Morrison et al. 2000).

Other terms are highly specific to particular cell types or anatomical contexts without clear evidence that a discrete "commitment" event occurs. Terms like **proximal convoluted tubule segment 1 cell fate commitment** (GO:0072154) were often added at curator request during annotation of individual genes, without systematic evaluation of whether a commitment stage is biologically meaningful for that cell type.

**4. Divergent annotation practices**

Some curators use highly specific pre-composed terms, while others use general terms like "cell fate commitment" with annotation extensions specifying the cell type via Cell Ontology identifiers. This variation impedes cross-database consistency and complicates computational analyses.

### Project Goal: Fresh Evaluation of Neural Development Annotations

A key goal of this project is to **evaluate neural/glial development annotations in light of both classic embryological understanding and modern single-cell perspectives**. For each gene reviewed, we will assess:

1. **Is the commitment/specification/determination distinction meaningful?** For genes like NOTCH1 and ASCL1 acting at the neuron-glia binary fate decision, the classic framework applies well. For genes involved in continuous maturation processes, simpler "differentiation" terms may be more appropriate.

2. **Is the term granularity appropriate?** Are highly specific terms (e.g., forebrain-specific variants) justified by distinct molecular programs, or would more general terms with annotation extensions better serve consistency?

3. **What experimental evidence supports the annotation?** We will critically evaluate whether annotations to specification/commitment/determination terms are supported by the requisite experimental assays, or whether they represent inferences from expression data that might be better captured by differentiation terms.

### Assessment Framework for Neural Development Terms

| GO Term | Example Genes | Assessment |
|---------|--------------|------------|
| neuron fate commitment (GO:0048663) | NOTCH1, ASCL1 | **Keep as exemplar** - Canonical binary fate decision with strong experimental support; Notch-mediated lateral inhibition creates genuine discrete commitment |
| glial cell fate commitment (GO:0021781) | SOX9, NFIA | **Keep as exemplar** - Represents the alternative branch of the neuron-glia binary decision |
| glial cell fate specification (GO:0021780) | SOX9 | **Review carefully** - Often inferred from early transcriptional bias rather than experimentally demonstrated plasticity; may be conflated with early differentiation |
| oligodendrocyte cell fate specification (GO:0021778) | OLIG2 | **Evaluate** - Strong experimental support from OLIG2 studies, but need to assess if specification/commitment distinction is consistently applied |
| astrocyte fate commitment (GO:0060018) | NFIA, STAT3 | **Evaluate** - Less discrete than neuron-glia decision; may be part of continuous gliogenic program |
| regulation of neuron differentiation (GO:0045664) | Many | **Keep** - Valuable regulatory process term, but individual annotations need review for over-annotation |

### Key Neural Development Terms (Current GO Structure)

| GO ID | Term | Definition |
|-------|------|------------|
| GO:0048663 | neuron fate commitment | Restriction to develop into a neuron |
| GO:0048664 | neuron fate determination | Irreversible autonomous differentiation into neuron |
| GO:0048665 | neuron fate specification | Reversible capacity to differentiate into neuron |
| GO:0030182 | neuron differentiation | Acquisition of specialized neuron features |
| GO:0048667 | cell morphogenesis involved in neuron differentiation | Generation of neuron structures during differentiation |

### Key Glial Development Terms (Current GO Structure)

| GO ID | Term | Definition |
|-------|------|------------|
| GO:0021781 | glial cell fate commitment | Restriction to develop into a glial cell |
| GO:0007403 | glial cell fate determination | Irreversible commitment to glial fate |
| GO:0010001 | glial cell differentiation | Acquisition of specialized glial features |
| GO:0048708 | astrocyte differentiation | Specialization into astrocytes |
| GO:0060018 | astrocyte fate commitment | Commitment to astrocyte fate |
| GO:0048709 | oligodendrocyte differentiation | Specialization into oligodendrocytes |
| GO:0021779 | oligodendrocyte cell fate commitment | Commitment to oligodendrocyte fate |
| GO:0014037 | Schwann cell differentiation | Specialization into Schwann cells (PNS) |

## Biological Narrative: Neural Cell Fate Decisions

### The Neuron-Glia Decision

The central nervous system arises from neuroepithelial cells that line the neural tube. These early progenitors, and their descendants the radial glial cells, face a fundamental choice: become a neuron or become a glial cell. This decision is controlled by a balance of pro-neural and pro-glial transcription factors, with signaling pathways providing the spatial and temporal context.

#### Proneural Factors Drive Neurogenesis

The basic helix-loop-helix (bHLH) transcription factors ASCL1 (formerly MASH1), NEUROG1, NEUROG2, and NEUROD1 form the core of the proneural gene network. These factors:

1. **Promote neuronal fate** by activating downstream neuronal differentiation genes
2. **Inhibit glial fate** by repressing gliogenic programs
3. **Control cell cycle exit** timing, as neurons are post-mitotic

**ASCL1** (Achaete-scute homolog 1) is particularly important for GABAergic interneurons and some dopaminergic neurons. It acts as a pioneer factor that can open closed chromatin.

**NEUROG1/2** (Neurogenin 1/2) drive glutamatergic neuron fate in the cortex and are required for proper cortical layer formation.

**NEUROD1** acts downstream of the neurogenins and is essential for neuronal survival and maturation.

#### The Neurogenesis-to-Gliogenesis Switch

A key insight is that neurogenesis precedes gliogenesis during development. The same progenitors that first produce neurons later switch to producing glia. This switch involves:

1. **Epigenetic changes** - Methylation of glial genes is removed
2. **JAK-STAT signaling** - Activated by cytokines like CNTF/LIF
3. **NOTCH signaling** - Promotes glial fate via HES/HEY factors
4. **SOX9** - Master regulator of gliogenesis

The **STAT3** pathway is critical: when activated, it drives astrocyte gene expression. The proneural factors actively inhibit STAT3 activity, explaining why neurogenesis must precede gliogenesis.

### Astrocyte versus Oligodendrocyte Fate

Once committed to a glial fate, progenitors must choose between astrocyte and oligodendrocyte identity (in the CNS) or Schwann cell fate (in the PNS).

#### Oligodendrocyte Specification

**OLIG1/2** are the master regulators of oligodendrocyte fate. These bHLH transcription factors:
- Are induced by Sonic Hedgehog (SHH) signaling from the ventral neural tube
- Specify motor neuron AND oligodendrocyte precursors (which arise from the same domain)
- In combination with NKX2.2, drive oligodendrocyte commitment

**SOX10** is essential for terminal oligodendrocyte differentiation and myelination. It works with MYRF (Myelin Regulatory Factor) to activate myelin gene expression.

**PDGFRA** marks oligodendrocyte precursor cells (OPCs) and is required for their proliferation and migration.

#### Astrocyte Specification

Astrocyte fate is promoted by:
- **SOX9** - Early gliogenic factor
- **NFIA/NFIB** - Nuclear factor I family members critical for astrocyte gene expression
- **STAT3** - Downstream of JAK kinases, activated by cytokines
- **NOTCH signaling** - Via HES1/HES5

Notably, **ID** (Inhibitor of Differentiation) proteins inhibit bHLH factors and promote astrocyte fate by preventing neuronal and oligodendrocyte programs.

### Neuronal Subtype Specification

Once committed to neuronal fate, cells must specify their neurotransmitter phenotype and regional identity.

#### GABAergic versus Glutamatergic Fate

In the cortex:
- **Glutamatergic neurons** arise from dorsal progenitors expressing TBR1/2, NEUROG1/2
- **GABAergic neurons** arise from ventral progenitors expressing DLX1/2/5/6, ASCL1

The **DLX** homeodomain transcription factors are essential for GABAergic interneuron development. DLX1/2 act upstream and regulate DLX5/6.

**LHX6** is induced by DLX genes and specifies parvalbumin and somatostatin interneuron subtypes.

#### Dopaminergic Neuron Specification

Midbrain dopaminergic neurons require:
- **LMX1A/B** - Roof plate transcription factors
- **FOXA1/2** - Pioneer factors
- **NURR1 (NR4A2)** - Essential for dopamine neuron survival
- **PITX3** - Required for substantia nigra dopamine neuron survival

#### Motor Neuron Specification

Spinal motor neurons are specified by:
- **SHH** - Ventralizing morphogen
- **OLIG2** - Initially marks motor neuron progenitors
- **ISL1/2** - LIM homeodomain factors essential for motor neuron identity
- **MNX1 (HB9)** - Motor neuron-specific transcription factor

### Notch Signaling: The Central Regulator

NOTCH signaling plays multiple roles:
1. **Maintains progenitor state** via HES/HEY target genes
2. **Promotes glial over neuronal fate** (lateral inhibition reversal)
3. **Lateral inhibition** - Differentiating neurons inhibit neighbors

Key Notch pathway genes:
- **NOTCH1/2/3** - Receptors
- **DLL1/3/4, JAG1/2** - Ligands
- **RBPJ** - Transcriptional effector
- **HES1/5, HEY1/2** - Target genes

### Wnt and BMP Signaling in Neural Fate

**Wnt signaling**:
- Promotes neuronal differentiation in some contexts
- Specifies dorsal cell types
- CTNNB1 (beta-catenin) is the key effector

**BMP signaling**:
- Inhibits neurogenesis, promotes astrocyte fate
- Specifies dorsal cell types
- Signals through SMAD1/5/8

## Genes for Review (Priority Order)

### Priority 1: Master Regulators (~12 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| ASCL1 | P50553 | Proneural bHLH factor, GABAergic fate |
| NEUROG1 | Q92886 | Proneural factor, glutamatergic fate |
| NEUROG2 | Q9H2A3 | Proneural factor, cortical neurogenesis |
| NEUROD1 | Q13562 | Neuronal differentiation and survival |
| OLIG2 | Q13516 | Oligodendrocyte and motor neuron fate |
| SOX9 | P48436 | Gliogenesis master regulator |
| NFIA | Q12857 | Astrocyte differentiation |
| STAT3 | P40763 | Gliogenic signaling |
| NOTCH1 | P46531 | Progenitor maintenance, glial fate |
| HES1 | Q14469 | Notch target, represses proneural genes |
| PAX6 | P26367 | Cortical progenitor identity |
| SOX2 | P48431 | Neural stem cell maintenance |

### Priority 2: Subtype Specification (~10 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| DLX1 | P56177 | GABAergic interneuron development |
| DLX2 | Q07687 | GABAergic interneuron development |
| LHX6 | Q9UPM6 | Cortical interneuron subtype |
| TBR1 | Q16650 | Glutamatergic neuron, cortical layers |
| NR4A2 | P43354 | Dopaminergic neuron survival (NURR1) |
| PITX3 | O75364 | Dopaminergic neuron survival |
| ISL1 | P61371 | Motor neuron identity |
| MNX1 | P50219 | Motor neuron identity (HB9) |
| OLIG1 | Q8TAK6 | Oligodendrocyte differentiation |
| SOX10 | P56693 | Oligodendrocyte/Schwann cell differentiation |

### Priority 3: Signaling and Chromatin (~8 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| SHH | Q15465 | Ventralizing morphogen |
| DLL1 | O00548 | Notch ligand |
| JAG1 | P78504 | Notch ligand |
| RBPJ | Q06330 | Notch transcriptional effector |
| HES5 | Q5TA89 | Notch target |
| ID1 | P41134 | Inhibitor of differentiation |
| ID3 | Q02535 | Inhibitor of differentiation |
| CTNNB1 | P35222 | Wnt effector (beta-catenin) |

### Priority 4: Additional Key Factors (~8 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| PDGFRA | P16234 | OPC marker and proliferation |
| NKX2-2 | O95096 | Oligodendrocyte specification |
| MYRF | Q9Y4C1 | Myelin gene regulation |
| NFIB | O00712 | Astrocyte differentiation |
| FOXA2 | Q9Y261 | Dopaminergic neuron pioneer factor |
| LMX1A | Q8TE12 | Dopaminergic neuron specification |
| GSX2 | Q9BZM3 | Ventral progenitor identity |
| EMX1 | Q04741 | Dorsal telencephalic identity |

## Disease Relevance

- **Glioblastoma**: Dysregulated ASCL1, OLIG2, SOX2 in tumor-initiating cells
- **Parkinson's disease**: Loss of dopaminergic neurons; NR4A2, PITX3 relevant
- **Multiple sclerosis**: Oligodendrocyte death; SOX10, MYRF, OLIG1/2 relevant
- **Autism spectrum disorders**: Interneuron dysfunction; DLX1/2, ASCL1 relevant
- **Aicardi-Goutires syndrome**: Astrocyte dysfunction
- **Developmental epilepsy**: GABAergic interneuron migration defects

## Key References

### Classic Embryology and Cell Fate Framework
- Waddington CH (2014) The Strategy of the Genes - The epigenetic landscape concept
- Slack JMW (2011) Essential Developmental Biology - Framework for specification/determination/commitment
- Morrison SJ et al. (2000) Cell - Regulatory mechanisms in stem cell biology; Notch in neuron-glia fate

### Neural Development Reviews
- Guillemot F (2007) Nat Rev Neurosci - Spatial and temporal specification of neural fates by transcription factor codes
- Rowitch DH, Kriegstein AR (2010) Nat Neurosci - Developmental genetics of vertebrate glial-cell specification
- Kwan KY et al. (2012) Neuron - Transcriptional co-regulation of neuronal migration and laminar identity
- Imayoshi I, Kageyama R (2014) Dev Growth Differ - bHLH factors in self-renewal and multipotency
- Elbaz B, Bhatt DM (2022) Nat Rev Neurosci - Oligodendrocyte development and disease

### Single-Cell Studies Challenging Discrete Fate Models
- Velten L et al. (2017) Nat Cell Biol - Human hematopoiesis shows continuous lineage commitment
- Weinreb C et al. (2020) Science - Lineage tracing reveals clonally unrelated fates despite transcriptional similarity
- La Manno G et al. (2016) Cell - Molecular diversity of midbrain development in mouse and human (scRNA-seq)

## Project Status

- [x] Create gene folders and fetch UniProt/GOA data
- [x] Priority 1 genes review (12/12 genes) - COMPLETE
- [ ] Priority 2 genes review (1/10 genes)
- [ ] Priority 3 genes review (0/8 genes)
- [ ] Priority 4 genes review (0/8 genes)
- [ ] Pathway summary and integration

### Priority 1 Genes (Master Regulators) - COMPLETED
| Gene | Status | Notes |
|------|--------|-------|
| ASCL1 | ✅ Complete | Proneural bHLH, GABAergic fate. Added GO:0045686 (negative regulation of glial cell differentiation) |
| NEUROG1 | ✅ Complete | Proneural bHLH, glutamatergic fate. Core cranial sensory neuron development (CN V, CN VIII) |
| NEUROG2 | ✅ Complete | Proneural bHLH, cortical neurogenesis. CAT E-box preference |
| NEUROD1 | ✅ Complete | Dual role: neuronal AND pancreatic endocrine differentiation |
| OLIG2 | ✅ Complete | Oligodendrocyte and motor neuron fate. Distinguished specification vs commitment |
| SOX9 | ✅ Complete | Gliogenesis master regulator. Also chondrogenesis |
| NFIA | ✅ Complete | Astrocyte differentiation. Core gliogenic TF |
| STAT3 | ✅ Complete | Gliogenic signaling. JAK-STAT pathway, astrocyte differentiation |
| NOTCH1 | ✅ Complete | Progenitor maintenance, glial fate. Corrected neural annotations to ACCEPT |
| HES1 | ✅ Complete | Notch target, transcriptional REPRESSOR of proneural genes |
| PAX6 | ✅ Complete | Cortical progenitor identity. Maintains progenitor state |
| SOX2 | ✅ Complete | Neural stem cell maintenance. Pluripotency factor |

### Priority 2 Genes (Subtype Specification) - IN PROGRESS
| Gene | Status | Notes |
|------|--------|-------|
| DLX1 | ✅ Complete | GABAergic interneuron development. First P2 gene done |
| DLX2 | Pending | |
| LHX6 | Pending | |
| TBR1 | Pending | |
| NR4A2 | Pending | |
| PITX3 | Pending | |
| ISL1 | Pending | |
| MNX1 | Pending | |
| OLIG1 | Pending | |
| SOX10 | Pending | |

---

# STATUS

**Project created: 2026-01-11**

Initial project setup complete. Ready to begin gene reviews starting with Priority 1 master regulators.

Total genes to review: ~38 genes across 4 priority tiers

# NOTES

## 2026-01-11

**Project Initialization**

Created project file with:
- Extended discussion of GO's cell development ontology structure based on Slack/Waddington framework
- Critical analysis of challenges with classic specification/commitment/determination distinctions
- Assessment framework for evaluating neural development terms in light of single-cell data
- Comprehensive biological narrative covering neuron-glia fate decisions
- Gene lists organized by functional priority:
  - Priority 1: Master regulators (ASCL1, NEUROG1/2, NEUROD1, OLIG2, SOX9, NFIA, STAT3, NOTCH1, HES1, PAX6, SOX2)
  - Priority 2: Subtype specification factors (DLX1/2, LHX6, TBR1, NR4A2, PITX3, ISL1, MNX1, OLIG1, SOX10)
  - Priority 3: Signaling and chromatin factors (SHH, DLL1, JAG1, RBPJ, HES5, ID1, ID3, CTNNB1)
  - Priority 4: Additional key factors (PDGFRA, NKX2-2, MYRF, NFIB, FOXA2, LMX1A, GSX2, EMX1)
- Disease relevance summary
- Key reference list (classic embryology + single-cell studies)

**Key evaluation criteria for this project:**
1. Is the commitment/specification/determination distinction meaningful for each gene?
2. Is the term granularity appropriate (e.g., forebrain-specific terms)?
3. Is experimental evidence sufficient for the annotated developmental stage?
4. Does annotation reflect discrete fate decision vs continuous differentiation?

**Exemplar terms to preserve:**
- neuron fate commitment (GO:0048663) - Canonical binary decision with Notch-mediated lateral inhibition
- glial cell fate commitment (GO:0021781) - Alternative branch of neuron-glia decision

**Terms requiring careful review:**
- glial cell fate specification (GO:0021780) - Often conflated with early differentiation
- astrocyte fate commitment (GO:0060018) - May be part of continuous gliogenic program
- Highly granular anatomical variants (forebrain-specific, etc.)

Key biological concepts in the narrative:
1. The temporal neurogenesis-to-gliogenesis switch
2. Proneural bHLH factors (ASCL1, NEUROG1/2) vs gliogenic factors (SOX9, STAT3)
3. NOTCH signaling as central regulator of progenitor state and fate choice
4. Oligodendrocyte specification via OLIG1/2 and SHH signaling
5. Neuronal subtype specification (GABAergic vs glutamatergic, dopaminergic, motor neurons)

Ready to proceed with deep research and gene annotation reviews.

## 2026-01-11 (cont.) - Review of OLIG2, NOTCH1, ASCL1

### Summary of Review Evaluation

Reviewed existing ai-review.yaml files for ASCL1, OLIG2, and NOTCH1 to assess:
1. Accuracy of existing reviews
2. Missing annotations related to neural/glial fate determination
3. Need for additional literature evidence

### ASCL1 Review Assessment

**File:** `genes/human/ASCL1/ASCL1-ai-review.yaml`
**Overall Assessment:** Well-executed review

**Correct Decisions:**
- GO:0048663 (neuron fate commitment) - ACCEPT - Correct, this is core function
- GO:0048665 (neuron fate specification) - ACCEPT - Correct
- GO:0030182 (neuron differentiation) - ACCEPT - Correct
- GO:0003359 (noradrenergic neuron fate commitment) - ACCEPT via IMP - Well-supported
- GO:0045665 (negative regulation of neuron differentiation) - REMOVE - Correct! The PMID:12000752 shows ASCL1 is *downregulated* during differentiation, not that it inhibits differentiation

**Missing Annotations:**
- **GO:0045686 (negative regulation of glial cell differentiation)** - ASCL1 actively suppresses gliogenesis. Literature evidence:
  - "Ascl1-deficient progenitors display a reduced capacity to generate oligodendrocytes (and neurons) and differentiate instead into astrocytes"
  - "In the absence of Ascl1, the SVZ progenitor's fate is predominantly astroglial"
  - Reference: J Neurosci 33(23):9752 (2013) - "Ascl1/Mash1 Promotes Brain Oligodendrogenesis"
  - Reference: Development 141(19):3721 (2014) - "Ascl1 controls the number and distribution of astrocytes and oligodendrocytes"

- **GO:0021779 (oligodendrocyte cell fate commitment)** - While not a primary function, ASCL1 positively regulates oligodendrocyte fate at the expense of astrocyte fate

**Notes:**
- ASCL1 has a dual role: promotes neuronal fate commitment AND promotes oligodendrocyte over astrocyte fate in the glial lineage
- This nuanced role is not fully captured in current annotations
- The review correctly identified the erroneous GO:0045665 annotation but did not add the missing glial suppression annotation

### OLIG2 Review Assessment

**File:** `genes/human/OLIG2/OLIG2-ai-review.yaml`
**Overall Assessment:** Good review with appropriate critical thinking

**Correct Decisions:**
- GO:0007423 (sensory organ development) - REMOVE - Correct! This was an inappropriate IBA propagation from other bHLH family members
- GO:0021778 (oligodendrocyte cell fate specification) - ACCEPT - Core function
- GO:0048709 (oligodendrocyte differentiation) - ACCEPT - Core function
- GO:0030182 (neuron differentiation) - MODIFY to GO:0021522 (spinal cord motor neuron differentiation) - Correct! OLIG2 specifically promotes motor neuron differentiation, not general neuron differentiation
- GO:0005515 (protein binding) - REMOVE - Correct per curation guidelines

**Questions about Current Annotations:**
- GO:0021778 is "oligodendrocyte cell fate specification" - should this be commitment (GO:0021779) instead? Based on the Slack framework discussion, specification is reversible while commitment is irreversible. OLIG2's function may be more accurately described as commitment given the evidence that OLIG2+ cells are restricted to oligodendrocyte fate.

**Missing Annotations:**
- **GO:0021779 (oligodendrocyte cell fate commitment)** - OLIG2 commits precursors to oligodendrocyte lineage; this is arguably more accurate than "specification"
- **Negative regulation terms** - OLIG2 antagonizes V2 and V3 interneuron fates (UniProt states: "Antagonist of V2 interneuron and of NKX2-2-induced V3 interneuron development")
  - Consider: GO:0045665 (negative regulation of neuron differentiation) with appropriate qualifier for V2/V3 interneurons

### NOTCH1 Review Assessment

**File:** `genes/human/NOTCH1/NOTCH1-ai-review.yaml`
**Overall Assessment:** Review has systematic issues with neural development annotations

**CRITICAL ISSUE: Neural development annotations incorrectly marked as non-core**

The reviewer marked ALL neural development annotations as "KEEP_AS_NON_CORE" with reason "tissue-specific function" or "context-dependent function". This is **incorrect** for a gene whose primary developmental role is the neuron-glia binary fate decision via lateral inhibition.

**Annotations that should be CORE, not NON_CORE:**
- GO:0045665 (negative regulation of neuron differentiation) - This is NOTCH1's canonical function in neural development
- GO:0045687 (positive regulation of glial cell differentiation) - Core function via lateral inhibition
- GO:0048711 (positive regulation of astrocyte differentiation) - Core gliogenic function
- GO:0048715 (negative regulation of oligodendrocyte differentiation) - Core function (promotes astrocyte over oligodendrocyte fate)
- GO:0048708 (astrocyte differentiation) - Core
- GO:0048709 (oligodendrocyte differentiation) - Core (regulatory role)

**Missing Annotations:**
- **GO:0021781 (glial cell fate commitment)** - NOTCH1 is essential for the binary neuron-glia fate decision. Key literature:
  - PMID:12052917 - "The role of Notch in promoting glial and neural stem cell fates"
  - PMID:11182080 - "Notch1 and Notch3 instructively restrict bFGF-responsive multipotent neural progenitor cells to an astroglial fate"
  - PMID:23307615 - "A critical role for Sox9 in notch-induced astrogliogenesis and stem cell maintenance"

- **Regulation of GO:0048663 (neuron fate commitment)** - NOTCH1 negatively regulates neuron fate commitment

**Rationale:**
NOTCH1 is not just involved in neural development as a "tissue-specific" function - the neuron-glia binary fate decision is mediated by Notch signaling and is **one of the core developmental functions** for which Notch signaling is famous. Marking these as non-core fundamentally misunderstands NOTCH1's biology.

The reviewer may have been confused by the fact that NOTCH1 has MANY functions (cardiac, vascular, immune, etc.) and so no single one seems "core". However, from a developmental biology perspective, the progenitor maintenance and neuron-glia fate decision functions are canonical and well-established.

### Literature to Cache (PMIDs)

Need to run `just target` for:
1. PMID:12052917 - Role of Notch in promoting glial and neural stem cell fates (Gaiano & Bhatt 2002)
2. PMID:11182080 - Notch1/3 restrict progenitors to astroglial fate (Tanigaki et al 2001)
3. PMID:23307615 - Sox9 critical for Notch-induced astrogliogenesis (Scott et al 2010)
4. PMID:11807030 - Notch1 required for neuronal and glial differentiation in cerebellum
5. PMID:17166924 - Ascl1 defines lineage-restricted neuronal and oligodendrocyte precursor cells
6. PMID:23946443 - Ascl1/Mash1 promotes brain oligodendrogenesis (J Neurosci)
7. PMID:25217633 - Ascl1 controls astrocyte and oligodendrocyte distribution (Development)

### Recommendations

1. **NOTCH1 review needs revision** - Neural development annotations should be ACCEPT/CORE, not KEEP_AS_NON_CORE
2. **ASCL1 review should add** - GO:0045686 (negative regulation of glial cell differentiation)
3. **OLIG2 review should consider** - Whether GO:0021779 (commitment) is more appropriate than GO:0021778 (specification)
4. **All reviews** - Ensure annotations capture the reciprocal nature of the neuron-glia binary fate decision

### Cross-Gene Pathway Considerations

The neuron-glia fate decision involves:
- **Proneural factors (ASCL1, NEUROG1/2)**: Promote neuron fate, inhibit glial fate
- **Notch signaling (NOTCH1, HES1/5)**: Maintains progenitor state, promotes glial over neuronal fate
- **Gliogenic factors (SOX9, NFIA)**: Promote glial fate downstream of Notch
- **OLIG2**: Promotes both motor neuron and oligodendrocyte fates (from pMN domain)

GO annotations should reflect this network:
- ASCL1 → positive regulation of neuron fate commitment, negative regulation of glial cell differentiation
- NOTCH1 → negative regulation of neuron fate commitment, positive regulation of glial cell fate commitment
- OLIG2 → oligodendrocyte cell fate commitment, motor neuron differentiation (specific)

### Completed Tasks (2026-01-11)

1. **NOTCH1 review corrections completed:**
   - Changed 6 neural development annotations from KEEP_AS_NON_CORE to ACCEPT
   - GO:0045665 (negative regulation of neuron differentiation)
   - GO:0045687 (positive regulation of glial cell differentiation)
   - GO:0048708 (astrocyte differentiation)
   - GO:0048709 (oligodendrocyte differentiation)
   - GO:0048711 (positive regulation of astrocyte differentiation)
   - GO:0048715 (negative regulation of oligodendrocyte differentiation)
   - Added supporting PMIDs: PMID:12052917, PMID:11182080, PMID:23307615

2. **ASCL1 review - added missing annotation:**
   - Added GO:0045686 (negative regulation of glial cell differentiation) with action: NEW
   - Supported by PMID:17166924: "We find that Ascl1 is present in progenitors to both neurons and oligodendrocytes, but not astrocytes."
   - Added PMID:17166924 to references section

3. **PMIDs already cached (confirmed):**
   - All 7 PMIDs from the literature review were already in publications/

4. **OLIG2 review - clarified specification vs commitment distinction:**
   - Updated GO:0021778 (specification) annotation with expanded explanation of why "specification" is appropriate:
     - Early OLIG2+ cells in pMN domain can become either motor neurons OR oligodendrocytes depending on context
     - This reversibility/context-dependence matches the Slack (2011) definition of specification
   - Added NEW annotation for GO:0021779 (oligodendrocyte cell fate commitment):
     - Captures OLIG2's continued role after specification, when OPCs become irreversibly committed
     - Complements specification term by documenting OLIG2's function throughout oligodendrogenesis

### Next Steps

1. Continue with reviews of other Priority 1 genes (NEUROG1/2, NEUROD1, SOX9, NFIA, STAT3, HES1, PAX6, SOX2)

## 2026-01-12

**Completed Priority 1 Reviews (10 genes)**

Selected and reviewed 10 genes to complete Priority 1:
- NEUROG1, NEUROG2, NEUROD1, SOX9, NFIA, STAT3, HES1, PAX6, SOX2, DLX1

### Key Biological Insights from Reviews

**Proneural bHLH Factors (NEUROG1, NEUROG2, NEUROD1)**
- All bind E-box motifs (CANNTG) as heterodimers with E-proteins
- NEUROG1/2 are proneural - initiate neuronal differentiation programs
- NEUROD1 is downstream - essential for neuronal survival and maturation
- NEUROD1 has dual role in both neural AND pancreatic endocrine differentiation (MODY6 diabetes gene)

**Gliogenic Factors (SOX9, NFIA, STAT3, HES1)**
- SOX9: HMG-box TF, master regulator of gliogenesis AND chondrogenesis
- NFIA: CTF/NF-I family, promotes astrocyte differentiation
- STAT3: JAK-STAT pathway, LIF/CNTF signaling drives astrocyte genes (GFAP)
- HES1: bHLH REPRESSOR - directly represses proneural genes (ASCL1, NEUROG1/2)
  - Critical note: HES1 is NOT an activator - it maintains progenitor state by repression

**Progenitor Maintenance (PAX6, SOX2)**
- PAX6: Paired box + homeodomain TF, maintains cortical progenitor/radial glia identity
- SOX2: SOXB1 factor, essential for neural stem cell self-renewal
  - Pioneer factor - maintains chromatin accessibility
  - Part of Yamanaka factors (Oct4, Sox2, Klf4, Myc)

**GABAergic Specification (DLX1)**
- Distal-less homeobox TF for GABAergic interneurons
- OPPOSITE function to NEUROG1/2 (which drive glutamatergic fate)
- Part of ventral telencephalon patterning (ganglionic eminences)

### Annotation Review Statistics

| Gene | Total Annotations | ACCEPT | KEEP_AS_NON_CORE | REMOVE | MODIFY |
|------|-------------------|--------|------------------|--------|--------|
| NEUROG1 | 57 | ~45 | ~8 | 3 | 1 |
| NEUROG2 | 18 | 11 | 3 | 1 | 3 |
| NEUROD1 | 82 | ~60 | ~15 | 5 | 2 |
| SOX9 | 185 | ~140 | ~35 | 10 | - |
| NFIA | 28 | 20 | 7 | 0 | 0 |
| STAT3 | 493 | ~300 | ~80 | ~110 | ~3 |
| HES1 | ~100 | ~62 | ~20 | ~10 | ~8 |
| PAX6 | 87 | 62 | 10 | 4 | 7 |
| SOX2 | 100 | 75 | 13 | 11 | 1 |
| DLX1 | 35 | 26 | 10 | 1 | 2 |

### Common Issues Identified

1. **Generic "protein binding" (GO:0005515)** - Removed from all genes per curation guidelines
2. **Over-broad developmental terms** - Modified to more specific terms (e.g., "cell differentiation" → "neuron differentiation")
3. **Incorrect activator/repressor annotations** - HES1 was annotated with "positive regulation" terms but is a REPRESSOR
4. **IBA propagation issues** - Some annotations from phylogenetic inference were inappropriate for specific gene functions

### Files Validated
All 10 genes passed validation (some with warnings about supporting_text coverage):
- NEUROG1 ✓
- NEUROG2 ✓
- NEUROD1 ✓
- SOX9 ✓
- NFIA ✓ (clean validation)
- STAT3 ✓
- HES1 ✓
- PAX6 ✓
- SOX2 ✓
- DLX1 ✓

### Summary

**Priority 1 is now COMPLETE (12/12 genes)**

Key themes across neuron-glia fate decision genes:
1. Binary fate decision mediated by Notch signaling → HES1 repression of proneural genes
2. Proneural factors (ASCL1, NEUROG1/2) promote neuronal fate AND inhibit glial fate
3. Gliogenic factors (SOX9, NFIA, STAT3) activated after neurogenesis-to-gliogenesis switch
4. Progenitor maintenance (PAX6, SOX2) prevents premature differentiation
5. Subtype specification (DLX1 for GABAergic) operates downstream of initial neuron fate commitment

Ready to proceed with Priority 2 genes (subtype specification).
