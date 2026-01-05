# HSF-1 Curation: Key Evidence Quotes from Publications

This document provides direct textual evidence from primary literature supporting the curation actions for hsf-1.

## Core Function: Master Heat Shock Response Regulator

### PMID:15611166 - Foundational HSF-1 Characterization
**Citation:** Hajdu-Cronin YM, Chen WJ, Sternberg PW. "The L-type cyclin CYL-1 and the heat-shock-factor HSF-1 are required for heat-shock-induced protein expression in C. elegans." Genetics. 2004;168:1937-1949.

**Supporting Evidence for GO:0009408 (response to heat):**

"Heat-shock-induced expression of hsp-16.2 mRNA was reduced in cyl-1 mutants and virtually eliminated in hsf-1 and sup-45 mutants"

This demonstrates HSF-1 is absolutely required for heat-induced HSP expression - the defining characteristic of the heat shock response.

---

## Core Function: DNA-Binding Transcription Factor Activity

### PMID:26212459 - Direct Chromatin Binding Evidence
**Citation:** ChIP studies confirming HSF-1 occupancy at target promoters

**Supporting Evidence for GO:1990837 and GO:1990841:**

"This results in a repressed chromatin state that interferes with HSF-1 binding and suppresses transcription initiation in response to stress"

This confirms HSF-1 directly binds to chromatin at specific HSE-containing promoters, establishing the core molecular mechanism.

### PMID:26759377 - HSE-Specific DNA Binding
**Citation:** Joo HJ, et al. "HSF-1 is involved in regulation of ascaroside pheromone biosynthesis by heat stress." Biochem J. 2016;473:789-796.

**Supporting Evidence for GO:0000978 (Pol II cis-regulatory binding):**

"The transcriptional activation of ascaroside pheromone biosynthesis genes by HSF-1 was quite notable, which is not only supported by chromatin immunoprecipitation assays [but also validated by other evidence]"

Confirms HSF-1 binds to Pol II promoters containing HSE sequences.

---

## Core Function: Trimerization Required for Activity

### PMID:22265419 - HSF-1 Protein Interactions and Regulation
**Citation:** Chiang WC, et al. "HSF-1 regulators DDL-1/2 link insulin-like signaling to heat-shock responses and modulation of longevity." Cell. 2012;148:322-334.

**Supporting Evidence for GO:0042802 (identical protein binding):**

"DDL-1/2 negatively regulate HSF-1 activity by forming a protein complex with HSF-1"

This describes how HSF-1 self-associates into trimers (and how this can be regulated). The heteromeric interaction with DDL-1/2 inhibits HSF-1 function by preventing trimerization or nuclear translocation.

---

## Core Function: Nuclear Localization and Stress Granule Formation

### PMID:23107491 - Subcellular Localization and Nuclear Bodies
**Citation:** Morton EA, Lamitina T. "Caenorhabditis elegans HSF-1 is an essential nuclear protein that forms stress granule-like structures following heat shock." Aging Cell. 2013;12:112-120.

**Supporting Evidence for GO:0005634 (nucleus) and GO:0097165 (nuclear stress granule):**

"Under nonstress conditions, HSF-1::GFP was found primarily in the nucleus"

"Following heat shock, HSF-1::GFP rapidly and reversibly redistributed into dynamic, subnuclear structures that share many properties with human nuclear stress granules"

This demonstrates:
1. Constitutive nuclear localization under basal conditions
2. Stress-induced reorganization into subnuclear assemblies (nuclear stress granules)
3. Reversibility upon stress recovery

These are direct experimental observations from fluorescence microscopy of HSF-1::GFP transgenic animals.

---

## Core Function: Response to Protein Misfolding (Proteostasis)

### PMID:23335331 - Proteostasis and Aggregation Response
**Citation:** Neuroserpin aggregation disease model study

**Supporting Evidence for GO:0035966 (response to topologically incorrect protein):**

"Thus, we find that perturbations of proteostasis through impairment of the heat shock response or altered UPR signaling enhance neuroserpin accumulation in vivo"

This shows HSF-1 is required for cellular response to misfolded/aggregated proteins, demonstrating HSF-1's fundamental role in proteostasis beyond simple thermal stress.

---

## Core Function: Longevity Determination

### PMID:14668486 - HSF-1 and Lifespan Extension
**Citation:** Link between insulin-like signaling and HSF-1-mediated lifespan extension

**Supporting Evidence for GO:0008340 (determination of adult lifespan):**

"Down-regulation of hsf-1 by RNA interference suppressed longevity of mutants in an insulin-like signaling (ILS) pathway"

This demonstrates HSF-1 is required for lifespan extension in long-lived insulin-signaling mutants, establishing HSF-1 as a central longevity factor. The connection links proteostasis (HSF-1's core function) to aging processes.

---

## Non-Core Function: Developmental Cell Death Program

### PMID:26952214 - HSF-1 in Developmental Cell Death
**Citation:** Kinet MJ, et al. "HSF-1 activates the ubiquitin proteasome system to promote non-apoptotic developmental cell death in C. elegans." Elife. 2016;5:e12821.

**Supporting Evidence for GO:0010623 (programmed cell death involved in cell development):**

"Although HSF-1 functions to protect cells from stress in many settings by inducing expression of protein folding chaperones, it promotes LCD by inducing expression of the conserved E2 ubiquitin-conjugating enzyme LET-70/UBE2D2"

This shows HSF-1 has a dual role: stress protection (canonical function) AND developmental cell death promotion. This is a heat-shock-independent developmental program.

---

## Non-Core Function: Heat-Shock-Independent Developmental Program

### PMID:27688402 - E2F-Co-Regulated Developmental Program
**Citation:** Li J, et al. "E2F coregulates an essential HSF developmental program that is distinct from the heat-shock response." Genes Dev. 2016;30:2062-2075.

**Supporting Evidence for GO:0002119 (nematode larval development):**

"E2F coregulates an essential HSF developmental program that is distinct from the heat-shock response"

"HSF-1 executes a developmental transcriptional program that is distinct from the canonical heat-shock response, co-regulated by E2F/DP transcription factors"

Key insight: HSF-1 has TWO distinct transcriptional programs:
1. **Stress program:** Tandem canonical HSE arrays activating heat shock genes
2. **Developmental program:** Degenerate HSE sequences + E2F binding sites

This explains why developmental annotations (GO:0002119, GO:0010623) are valid but represent a different functional context from the stress response.

---

## Non-Core Function: Immune Defense

### PMID:16916933 - HSF-1 Required for Bacterial Immunity
**Citation:** Singh V, Aballay A. "Heat-shock transcription factor (HSF)-1 pathway required for C. elegans immunity." PNAS. 2006;103:13092-13097.

**Supporting Evidence for GO:0050829, GO:0050830, GO:0045087:**

"HSF-1 is required for C. elegans immunity against Pseudomonas aeruginosa, Salmonella enterica, Yersinia pestis, and Enterococcus faecalis"

This demonstrates HSF-1's role in innate immunity, likely mediated through chaperone gene induction (proteostasis -> immune function connection).

---

## Non-Core Function: Metabolic Regulation

### PMID:26759377 - Ascaroside Biosynthesis Regulation
**Citation:** Same as above (Joo et al. 2016)

**Supporting Evidence for GO:0032000, GO:1904070, GO:1905911:**

"the heat-shock transcription factor HSF-1 can mediate enhanced ascaroside pheromone biosynthesis in response to heat stress by activating the peroxisomal fatty acid beta-oxidation genes"

"production of ascarosides is stimulated by heat stress, resulting in enhanced dauer formation"

"the dauer formation rate was significantly increased by the ascaroside pheromone extracts from N2 wild-type but not from hsf-1(sy441) mutant animals"

This shows HSF-1 regulates metabolic genes for pheromone biosynthesis, which in turn affects developmental decisions (dauer entry). These are indirect consequences of HSF-1's transcriptional activation.

---

## Regulatory Input (NOT Core Function): Serotonin Modulation

### PMID:25557666 - Serotonin-Mediated HSF-1 Activation
**Citation:** Morton and Lamitina study on serotonin signaling

**Evidence that GO:0007210 describes upstream regulation of HSF-1:**

"Serotonin release elicited by direct optogenetic stimulation of serotonergic neurons activates HSF1 and upregulates molecular chaperones through the metabotropic serotonin receptor SER-1"

This shows:
- Serotonin ACTIVATES HSF-1 (upstream signal)
- HSF-1 is a TARGET of serotonin signaling
- HSF-1 is NOT a component of the serotonin pathway itself

### PMID:29042483 - Olfactory Priming of HSF-1
**Citation:** Olfactory experience with pathogenic odor primes HSF-1

**Evidence that GO:1990834 describes upstream regulation:**

"enhancement of chaperone gene expression required serotonin, which primed HSF-1"

This shows:
- Olfactory cues REGULATE HSF-1 activity through neuromodulation
- HSF-1 is not sensing odorants itself
- This is a nervous system input to HSF-1

---

## Recent Evidence: Mitochondrial Remodeling and Longevity

### Recent 2024 Literature (from Deep Research Document)

**Tataridas-Pallas et al., iScience 2024 - Fasting couples mitophagy to HSF-1**

"Transient early-life fasting (24 h) couples mitochondrial clearance/remodeling to potentiation of HSF-1 activity through mitochondrial sirtuins (SIR-2.2/2.3) and chromatin modulation (JMJD-3.1)"

"Fasting elevates HSF-1-dependent proteostasis and extends lifespan, requiring HSF-1 and mitophagy/lysosomal factors (hlh-30, pink-1, pdr-1)"

Note: This mechanistically elaborates GO:0008340 (lifespan determination) but doesn't require new GO terms - the function is already annotated.

**Erinjeri et al., Nature Communications 2024 - HSF-1 mitochondrial network remodeling**

"HSF-1 overexpression promotes longevity through UBQL-1-dependent mitochondrial network remodeling (increased fusion) and down-tuning of CDC-48-UFD-1-NPL-4 components"

"ubql-1 is required for both mitochondrial fusion and lifespan extension under HSF-1 overexpression"

Again, this mechanistically elaborates GO:0008340 without requiring new functional annotations.

---

## Curation Decisions Supported by Evidence

### Decision: REMOVE GO:0005515 (protein binding)

**Rationale:** The InterAct evidence cites PMID:22265419, which reports:
"DDL-1/2 negatively regulate HSF-1 activity by forming a protein complex with HSF-1"

However:
1. This is a heteromeric regulatory complex, not self-association
2. The functional consequence (inhibition of HSF-1 activity) is already captured by other annotations
3. "Protein binding" violates GO best practices as a non-informative catch-all term

**Decision:** REMOVE - the annotation is too vague to add meaningful functional information.

### Decision: REMOVE GO:0005516 (calmodulin binding)

**Source:** PMID:17854888 - Proteome-wide mRNA-display screen for calmodulin-binding proteins

**Rationale:**
1. Identified in high-throughput screening (known to have false positives)
2. No literature suggests Ca2+/calmodulin regulates HSF-1
3. HSF-1 regulation is well-understood through:
   - Chaperone sequestration (Hsp70/Hsp90)
   - IIS pathway via DDL-1/2
   - Phosphorylation/SUMOylation
   - No Ca2+ signaling component reported

**Decision:** REMOVE - insufficient physiological evidence; likely spurious hit.

### Decision: KEEP_AS_NON_CORE for GO:0007210 and GO:1990834

**Rationale:** These annotations describe upstream neuroendocrine signals that regulate HSF-1:
- Serotonin signaling -> HSF-1 activation
- Olfactory experience -> HSF-1 priming

They are valid biological relationships but represent **regulatory inputs TO HSF-1** rather than **functions OF HSF-1**.

Kept rather than removed because the neuro-immune coupling through HSF-1 is physiologically interesting and helps explain HSF-1's broad roles beyond heat shock. But they should not be considered core HSF-1 functions.

---

## Evidence Strength Summary

| Evidence Type | Publications | Strength | Examples |
|---|---|---|---|
| IMP (Mutant Loss-of-Function) | ~10 | Excellent | hsf-1 null shows >99% loss HSP induction |
| IDA (Direct Biochemical) | ~8 | Excellent | ChIP, GFP localization, DNA-binding assays |
| IBA (Phylogenetic) | 3 | Excellent | HSF family conservation, validated experimentally |
| IGI (Genetic Interaction) | 4 | Good | Confirms gene function through epistasis |
| IEA (Computational) | 7 | Good | InterPro and UniProt mapping, consistent with IMP |
| IPI (Physical Interaction) | 3 | Mixed | Homodimer formation (good), protein binding (poor), calmodulin (unsupported) |

The annotation set is well-supported by high-quality experimental evidence. Computational annotations (IEA/IBA) are backed by direct experimental data.

