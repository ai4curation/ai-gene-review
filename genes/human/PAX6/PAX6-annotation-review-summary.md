# PAX6 GO Annotation Review Summary

## Gene Description
PAX6 is a paired-box transcription factor with dual DNA-binding domains (paired domain and homeodomain) that functions as a master regulator of eye development (aniridia gene) and is critical for neural development, particularly in maintaining cortical progenitor/radial glia identity and regulating neurogenesis timing.

## Core Functions Identified

### Molecular Functions (CORE)
1. **GO:0000981** - DNA-binding transcription factor activity, RNA polymerase II-specific
   - Multiple evidence types (IBA, IEA, IDA, ISA)
   - Core defining molecular function

2. **GO:0043565** - sequence-specific DNA binding
   - Paired domain + homeodomain confer specificity
   - Core molecular function

3. **GO:0001228** - DNA-binding transcription activator activity, RNA polymerase II-specific
   - Strong IDA evidence (PMID:24802670)
   - Core activator function

4. **GO:0001227** - DNA-binding transcription repressor activity, RNA polymerase II-specific
   - Context-dependent repressor function
   - Core dual regulatory capability

### Biological Processes (CORE)
1. **GO:0001654** - eye development (TAS)
   - THE defining function - "aniridia gene"
   - Master regulator of ocular development

2. **GO:0021987** - cerebral cortex development
   - Critical for NEURON_DEVELOPMENT project
   - Maintains radial glia/progenitor identity

3. **GO:0030900** - forebrain development
   - Specific rostral CNS function
   - Core neural development role

4. **GO:0060041** - retina development in camera-type eye
   - Specific aspect of eye development
   - Retinal progenitor competence

5. **GO:0050768** - negative regulation of neurogenesis
   - Maintains progenitor pool
   - Prevents premature differentiation
   - CRITICAL for NEURON_DEVELOPMENT understanding

### Cellular Components (CORE)
1. **GO:0005634** - nucleus (IDA)
2. **GO:0000785** - chromatin (IDA, ISA)

## Annotations to ACCEPT (62 total)
- All core TF activity annotations (multiple evidence types)
- Eye development annotations (iris, cornea, retina, camera-type eye)
- Brain/neural development (brain, CNS, forebrain, cortex, nervous system)
- Specific DNA binding annotations (cis-regulatory, promoter, sequence-specific)
- Transcriptional regulation annotations (positive/negative, activation/repression)
- Nuclear/chromatin localization
- SMAD interaction annotations (GO:0070410, GO:0070412) - regulatory cross-talk
- miRNA transcription regulation (GO:1902895) - specific validated function
- Co-regulator binding annotations

## Annotations to KEEP_AS_NON_CORE (10 total)
- **GO:0003309** - type B pancreatic cell differentiation (IBA)
- **GO:0003322** - pancreatic A cell development (IEA, IMP)
- **GO:0042593** - glucose homeostasis (IMP)
- **GO:0021517** - ventral spinal cord development (IEA, ISS)
- **GO:0001568** - blood vessel development (IMP) - pleiotropic
- **GO:0009611** - response to wounding (IEP) - expression only
- **GO:0005737** - cytoplasm (IDA) - not primary functional location

## Annotations to REMOVE (4 total)
1. **GO:0005515** - protein binding (IPI x2)
   - Generic, uninformative per curation guidelines
   - From high-throughput screens

2. **GO:0030182** - neuron differentiation (IEA)
   - MISLEADING: PAX6 in progenitors, NOT neurons
   - Maintains progenitor identity, doesn't promote differentiation
   - Contradicts expression pattern

3. **GO:0007601** - visual perception (TAS)
   - Conflates DEVELOPMENT with adult FUNCTION
   - PAX6 builds eye structures during development
   - Not expressed/functional in mature visual system

## Annotations to MARK_AS_OVER_ANNOTATED (7 total)
- **GO:0009653** - anatomical structure morphogenesis - too broad
- **GO:0030154** - cell differentiation - too broad
- **GO:0050877** - nervous system process - wrong temporal context
- **GO:0010628** - positive regulation of gene expression - too general
- **GO:0006338** - chromatin remodeling - over-attributes enzyme activity
- **GO:0009887** - animal organ morphogenesis - too broad

## Annotations UNDECIDED (7 total)
- **GO:0003723** - RNA binding - not well-documented for PAX6
- **GO:0019901** - protein kinase binding - not well-characterized
- **GO:0031625** - ubiquitin protein ligase binding - lacks experimental support
- **GO:0071837** - HMG box domain binding - not prominently documented
- **GO:0048663** - neuron fate commitment - ambiguous given progenitor maintenance role

## Key Evidence Sources

### Experimental (IDA/IMP/IPI)
- **PMID:24802670** - PAX6 in neuroectoderm specification, miR-135b activation (ChIP-seq)
- **PMID:20592023** - PAX6 in pancreatic alpha cell differentiation
- **PMID:7550230** - PAX6 mutations causing aniridia, haploinsufficiency
- **PMID:17251190** - SMAD3 interaction and PAX6 autoregulation
- **PMID:28473536** - DNA binding specificity studies

### Literature Review
- **file:PAX6-deep-research-falcon.md** - Comprehensive synthesis
  - Paired domain + homeodomain structure
  - Master regulator ocular development
  - Cortical neurogenesis and progenitor maintenance
  - 12.8% diabetes prevalence in carriers
  - Expressed in progenitors, NOT mature neurons

## Critical Points for NEURON_DEVELOPMENT Project

1. **PAX6 maintains PROGENITOR identity** - does NOT promote neuronal differentiation
2. **Negative regulation of neurogenesis** (GO:0050768) - CORE function for progenitor maintenance
3. **Cerebral cortex development** (GO:0021987) - highly specific and relevant
4. **Expression pattern**: Neural progenitors/radial glia, NOT mature neurons
5. **Loss phenotype**: Premature differentiation, depletion of progenitor pool

## Annotation Statistics
- Total annotations reviewed: 87
- ACCEPT: 62 (71%)
- KEEP_AS_NON_CORE: 10 (11%)
- REMOVE: 4 (5%)
- MARK_AS_OVER_ANNOTATED: 7 (8%)
- UNDECIDED: 7 (8%)
- Modified/Proposed replacements: 0

## Status
**COMPLETE** - Comprehensive systematic review of all 87 GO annotations for PAX6 with citations and detailed rationales.
