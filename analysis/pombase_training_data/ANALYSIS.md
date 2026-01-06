# PomBase AI/ML Training Datasets Analysis

## Overview
PomBase provides curated training datasets for ML/AI models focused on biological curation tasks. These datasets are from the October 2025 release.

## Available Datasets

### 1. Alleles Dataset (alleles.tsv)
- **Size**: 16,401 alleles
- **Format**: Tab-separated values
- **Fields**:
  - Gene systematic ID
  - Gene name
  - Allele internal ID
  - Allele name
  - Allele type (deletion, point mutation, etc.)
  - Allele description
  - Allele synonyms
- **Use Cases**:
  - Training models for variant effect prediction
  - Learning patterns in gene-allele relationships
  - Validation of mutation impact predictions

### 2. Publication Classification (canto_pub_classification.tsv)
- **Size**: 14,700 publications
- **Format**: Tab-separated (PMID, Classification)
- **Classification Categories**:
  - Curatable: 6,989 (47.5%)
  - Wrong organism: 3,251 (22.1%)
  - Review or comment: 1,385 (9.4%)
  - Method or reagent: 1,038 (7.1%)
  - Other categories: ~2,000 papers across 30+ categories
- **Use Cases**:
  - Training publication triage models
  - Learning what makes a paper "curatable" for gene annotation
  - Filtering relevant literature for gene reviews

### 3. Publications with Annotations (publications_with_annotations.txt)
- **Size**: 5,714 PubMed IDs
- **Format**: Simple text list of PMIDs
- **Use Cases**:
  - Identifying high-value papers for gene annotation
  - Creating a gold standard corpus of annotated publications
  - Cross-referencing with gene review citations

## Potential Applications for Gene Review Project

### 1. Literature Triage Model
- Train a classifier using `canto_pub_classification.tsv` to identify "Curatable" papers
- Features could include: title, abstract, journal, keywords
- Could help prioritize which papers to review for each gene

### 2. Allele-Function Relationships
- Use `alleles.tsv` to understand gene-phenotype relationships
- Particularly valuable for genes with many characterized alleles
- Could inform "suggested_experiments" section of reviews

### 3. Cross-Species Validation
- Many pombe genes have human orthologs
- PomBase's curated annotations can validate human gene function predictions
- Useful for evolutionary conservation analysis

### 4. Quality Metrics
- Compare our reviewed PMIDs against PomBase's annotated publications
- Higher overlap suggests more comprehensive literature coverage
- Can identify potentially missed important papers

## Integration Strategy

1. **Immediate Use**:
   - Download and cache these datasets for validation
   - Cross-reference PMIDs in gene reviews with annotated publications

2. **Future Development**:
   - Build publication classifier for automatic literature triage
   - Create allele effect prediction models
   - Develop cross-species annotation transfer pipelines

### 4. GO Annotations with Curator Comments (canto_go_annotations_with_comments.tsv)
- **Size**: 4,111 GO annotations for 1,309 genes
- **Format**: Tab-separated with 9 fields
- **Fields**:
  - Gene systematic ID & name
  - GO aspect (molecular_function, biological_process, cellular_component)
  - Term ID and name
  - Reference (PMID)
  - Evidence code (IDA, EXP, IMP, IPI, IGI)
  - Extensions (e.g., occurs_in, part_of)
  - Curator comments (72% have comments!)
- **Evidence Distribution**:
  - IDA (Inferred from Direct Assay): 1,970
  - EXP (Inferred from Experiment): 917
  - IMP (Inferred from Mutant Phenotype): 762
  - IPI (Inferred from Physical Interaction): 385
  - IGI (Inferred from Genetic Interaction): 76
- **Use Cases**:
  - **Gold standard for annotation quality** - Expert-curated annotations with detailed comments
  - **Training annotation review models** - Learn what makes a good annotation
  - **Evidence extraction** - Comments often cite specific figures/results
  - **Annotation extension patterns** - Learn proper use of GO-CAM extensions

### Example High-Quality Annotation (epe1 gene):
```
Gene: epe1
GO Term: GO:0032454 (histone H3K9 demethylase activity)
Evidence: IDA
Extension: part_of(GO:0033696)
Comment: "The analyses presented here are consistent with Epe1 normally acting
as an H3K9 demethylase that removes H3K9 methylation from ectopic sites of
heterochromatin formation."
```

## Key Insights for Gene Review Project

1. **Curator Comments as Training Data**:
   - 2,965 annotations have detailed curator comments
   - Comments often cite specific figures and experimental results
   - Excellent for training models to extract evidence from papers

2. **Evidence Code Distribution**:
   - Heavy emphasis on direct experimental evidence (IDA/EXP/IMP = 88%)
   - Minimal computational predictions
   - Sets a high bar for annotation quality

3. **Annotation Extensions**:
   - Many annotations use GO-CAM style extensions
   - Examples: occurs_in(), part_of(), coincident_with()
   - Valuable for learning proper annotation context

## Citation
Kim Rutherford et al., "PomBase: a Global Core Biodata Resource—growth, collaboration, and sustainability", Genetics, February 2024
DOI: https://doi.org/10.1093/genetics/iyae007