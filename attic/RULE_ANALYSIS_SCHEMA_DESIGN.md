# Rule Analysis Schema Design

## Requirements Analysis

Based on discussion, the data model should include:

### 1. Domain/Family Level Stats (per condition)
- Direct protein count for each InterPro/FunFam domain
- General measure of uniqueness (how specific/unique is this domain)
- Optional: Sample protein IDs (only when count is small, e.g., < 20)

### 2. Condition Set Level Stats (pairwise)
- **Set difference |A - B|**: Proteins in A but not in B (uniqueness of A w.r.t. B)
- **Set difference |B - A|**: Proteins in B but not in A (uniqueness of B w.r.t. A)
- Jaccard similarity (for reference)
- Containment ratios
- Intersection count

### 3. InterPro2GO Redundancy
- Which GO annotations are redundant with existing ipr2go mappings
- Which are novel

## Proposed Schema Extension

```yaml
# Add to RuleCondition
RuleCondition:
  description: A single condition in a rule antecedent
  attributes:
    condition_type:
      range: ConditionTypeEnum
      required: true
    value:
      range: string
      required: true
    curie:
      range: string
      description: Normalized CURIE (e.g., InterPro:IPR005982)
    label:
      range: string
      description: Human-readable label
    negated:
      range: boolean
      description: Whether this is a negative condition

    # NEW: Domain-level statistics
    protein_count:
      range: integer
      description: Number of proteins matching this condition in specified database
      minimum_value: 0
      comments:
        - Only populated for InterPro, FunFam, PANTHER conditions
        - Null for taxon and other condition types

    protein_database:
      range: ProteinDatabaseEnum
      description: Which protein database was queried (e.g., SWISSPROT, TREMBL)
      comments:
        - Defaults to SWISSPROT (reviewed proteins only)
        - Important to specify since counts differ dramatically

    uniqueness_score:
      range: float
      description: >-
        Measure of domain uniqueness (0.0 to 1.0).
        Calculated as 1.0 - (mean containment in other domains in same condition set).
        High score = more unique/specific.
      minimum_value: 0.0
      maximum_value: 1.0

    sample_proteins:
      range: string
      multivalued: true
      description: Sample UniProt IDs (only included when protein_count < 20)
      comments:
        - Avoid storing for large sets
        - Max 10 examples even if count < 20

# Add to RuleConditionSet
RuleConditionSet:
  description: >-
    A set of conditions that must ALL be true (conjunction/AND).
    Multiple condition sets in a rule are OR-ed together (disjunction).
  attributes:
    conditions:
      range: RuleCondition
      multivalued: true
      required: true

    notes:
      range: string
      description: Reviewer notes

    # NEW: Pairwise overlap analysis
    pairwise_overlap:
      range: PairwiseOverlap
      multivalued: true
      inlined_as_list: true
      description: >-
        Pairwise overlap statistics for domain conditions in this set.
        Only computed for InterPro, FunFam, PANTHER conditions.

# NEW: Pairwise overlap class
PairwiseOverlap:
  description: >-
    Overlap statistics between two domain conditions (InterPro, FunFam, etc.)
    in the same condition set.
  attributes:
    condition_a:
      range: string
      required: true
      description: First condition value (e.g., IPR005982)

    condition_b:
      range: string
      required: true
      description: Second condition value (e.g., IPR008255)

    condition_a_label:
      range: string
      description: Human-readable label for condition A

    condition_b_label:
      range: string
      description: Human-readable label for condition B

    protein_database:
      range: ProteinDatabaseEnum
      required: true
      description: Which protein database was queried (SWISSPROT or TREMBL)

    count_a:
      range: integer
      required: true
      minimum_value: 0
      description: Number of proteins matching condition A in specified database

    count_b:
      range: integer
      required: true
      minimum_value: 0
      description: Number of proteins matching condition B in specified database

    intersection_count:
      range: integer
      required: true
      minimum_value: 0
      description: Number of proteins matching BOTH A AND B (|A ∩ B|) in specified database

    # Primary metrics: Set differences (uniqueness)
    a_minus_b_count:
      range: integer
      required: true
      minimum_value: 0
      description: >-
        Number of proteins in A but not in B (|A - B|).
        Represents the uniqueness of A with respect to B.
        High value = A adds unique coverage beyond B.

    b_minus_a_count:
      range: integer
      required: true
      minimum_value: 0
      description: >-
        Number of proteins in B but not in A (|B - A|).
        Represents the uniqueness of B with respect to A.
        High value = B adds unique coverage beyond A.

    # Derived metrics
    jaccard_similarity:
      range: float
      required: true
      minimum_value: 0.0
      maximum_value: 1.0
      description: >-
        Jaccard similarity coefficient: |A ∩ B| / |A ∪ B|
        = intersection / (count_a + count_b - intersection)
        0.0 = no overlap, 1.0 = complete overlap

    containment_a_in_b:
      range: float
      required: true
      minimum_value: 0.0
      maximum_value: 1.0
      description: >-
        Proportion of A contained in B: |A ∩ B| / |A|
        1.0 means A is completely contained in B (A ⊆ B)

    containment_b_in_a:
      range: float
      required: true
      minimum_value: 0.0
      maximum_value: 1.0
      description: >-
        Proportion of B contained in A: |A ∩ B| / |B|
        1.0 means B is completely contained in A (B ⊆ A)

    interpretation:
      range: OverlapInterpretationEnum
      description: Automated interpretation of overlap pattern
      comments:
        - REDUNDANT: Jaccard > 0.9 (very high overlap)
        - HIGH_OVERLAP: Jaccard > 0.5
        - SUBSET: One condition is subset of other (containment > 0.95)
        - MODERATE: 0.2 < Jaccard <= 0.5
        - LOW: Jaccard <= 0.2

# Add to EmbeddedRule
EmbeddedRule:
  attributes:
    rule_id:
      range: string
      required: true

    condition_sets:
      range: RuleConditionSet
      multivalued: true
      required: true

    go_annotations:
      range: RuleGOAnnotation
      multivalued: true

    # NEW: InterPro2GO redundancy analysis
    ipr2go_redundancy:
      range: InterPro2GORedundancy
      inlined: true
      description: Analysis of redundancy with InterPro2GO mappings

# NEW: InterPro2GO redundancy class
InterPro2GORedundancy:
  description: >-
    Analysis of whether rule GO annotations are redundant with
    existing InterPro2GO mappings.
  attributes:
    redundant_annotations:
      range: RedundantAnnotation
      multivalued: true
      inlined_as_list: true
      description: GO annotations already in InterPro2GO

    novel_annotations:
      range: string
      multivalued: true
      description: GO IDs not found in InterPro2GO for any condition

    summary:
      range: string
      description: Human-readable summary

RedundantAnnotation:
  description: A GO annotation that is redundant with InterPro2GO
  attributes:
    go_id:
      range: string
      required: true
      description: GO term ID (e.g., GO:0004791)

    go_label:
      range: string
      description: GO term label

    interpro_source:
      range: string
      required: true
      description: InterPro ID that already maps to this GO term

    interpro_label:
      range: string
      description: InterPro domain label

# NEW: Enums
ProteinDatabaseEnum:
  permissible_values:
    SWISSPROT:
      description: Swiss-Prot (reviewed, manually curated proteins)
    TREMBL:
      description: TrEMBL (unreviewed, automatically annotated proteins)
    UNIPROT:
      description: Full UniProtKB (Swiss-Prot + TrEMBL)

OverlapInterpretationEnum:
  permissible_values:
    REDUNDANT:
      description: Very high overlap (Jaccard > 0.9), conditions are nearly identical
    SUBSET:
      description: One condition is a subset of the other (containment > 0.95)
    HIGH_OVERLAP:
      description: High overlap (Jaccard > 0.5), conditions are similar
    MODERATE:
      description: Moderate overlap (0.2 < Jaccard <= 0.5)
    LOW:
      description: Low overlap (Jaccard <= 0.2), conditions are mostly distinct
    DISJOINT:
      description: No overlap (intersection = 0), conditions are completely distinct
```

## Example Data

### ARBA00026249 with Extended Schema

```yaml
rule:
  rule_id: ARBA00026249

  condition_sets:
    - conditions:
        # Condition 1: IPR005982
        - condition_type: INTERPRO
          value: IPR005982
          curie: InterPro:IPR005982
          label: Thioredoxin reductase
          negated: false
          protein_count: 65
          uniqueness_score: 0.226  # Mean containment in others = 0.774
          sample_proteins: null  # Not included (count >= 20)

        # Condition 2: IPR008255
        - condition_type: INTERPRO
          value: IPR008255
          curie: InterPro:IPR008255
          label: Pyridine nucleotide-disulphide oxidoreductase, class-II, active site
          negated: false
          protein_count: 84
          uniqueness_score: 0.226  # Mean containment in others = 0.774

        # Condition 3: IPR023753
        - condition_type: INTERPRO
          value: IPR023753
          curie: InterPro:IPR023753
          label: FAD/NAD(P)-binding domain
          negated: false
          protein_count: 869
          uniqueness_score: 0.914  # Low containment in others, very broad

      # Pairwise overlap analysis
      pairwise_overlap:
        # IPR005982 vs IPR008255
        - condition_a: IPR005982
          condition_b: IPR008255
          condition_a_label: Thioredoxin reductase
          condition_b_label: Pyridine nucleotide-disulphide oxidoreductase
          count_a: 65
          count_b: 84
          intersection_count: 65
          a_minus_b_count: 0      # A is subset of B!
          b_minus_a_count: 19     # B has 19 unique proteins
          jaccard_similarity: 0.774
          containment_a_in_b: 1.0
          containment_b_in_a: 0.774
          interpretation: SUBSET

        # IPR005982 vs IPR023753
        - condition_a: IPR005982
          condition_b: IPR023753
          count_a: 65
          count_b: 869
          intersection_count: 65
          a_minus_b_count: 0      # A is subset of B!
          b_minus_a_count: 804    # B has 804 unique proteins (very broad)
          jaccard_similarity: 0.075
          containment_a_in_b: 1.0
          containment_b_in_a: 0.075
          interpretation: SUBSET

        # IPR008255 vs IPR023753
        - condition_a: IPR008255
          condition_b: IPR023753
          count_a: 84
          count_b: 869
          intersection_count: 84
          a_minus_b_count: 0      # A is subset of B!
          b_minus_a_count: 785    # B has 785 unique proteins
          jaccard_similarity: 0.097
          containment_a_in_b: 1.0
          containment_b_in_a: 0.097
          interpretation: SUBSET

    # Condition sets 2 and 3 have no pairwise_overlap (only 1 domain each)
    - conditions: [...]
    - conditions: [...]

  # InterPro2GO redundancy
  ipr2go_redundancy:
    redundant_annotations:
      - go_id: GO:0004791
        go_label: thioredoxin-disulfide reductase (NADPH) activity
        interpro_source: IPR005982
        interpro_label: Thioredoxin reductase

    novel_annotations: []
    summary: "1 redundant annotation(s) (already in ipr2go). All annotations already in ipr2go."
```

## Key Design Decisions

### 1. Set Difference as Primary Metric

**Rationale:** |A - B| directly measures uniqueness of A w.r.t. B
- If |A - B| = 0, then A ⊆ B (A is redundant given B)
- If |A - B| is large, then A provides unique coverage
- More intuitive than Jaccard for evaluating condition redundancy

### 2. Sample Proteins Only for Small Sets

**Rationale:** Avoid bloating YAML files with large protein lists
- Include `sample_proteins` only when `protein_count < 20`
- Limit to max 10 examples even then
- For larger sets, use external queries if needed

### 3. Uniqueness Score per Domain

**Rationale:** Single metric to assess domain specificity
- Calculated as `1.0 - mean(containment_in_other_domains)`
- High score = domain is specific/unique
- Low score = domain is broad/commonly co-occurring
- Helps identify which conditions are "pulling weight"

### 4. Overlap Interpretation Enum

**Rationale:** Make common patterns explicit
- SUBSET: One condition makes the other redundant
- REDUNDANT: Both conditions are nearly identical
- LOW: Conditions are complementary (both needed)
- Automated interpretation aids review

## Implementation Notes

These changes are **additive** - they extend the existing schema without breaking changes:
- New fields are optional (can be null)
- Existing reviews continue to validate
- Analysis can be run post-hoc and added incrementally

## Next Steps

1. Add classes to `gene_review.yaml` schema
2. Update `rule_analysis.py` to output this structure
3. Update tests to verify new format
4. Update demo script to display new fields
5. Regenerate pydantic models: `just pydantic`
