# SPKW Methodology Notes

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This document describes the analytical methods used to identify SPKW-unique annotations for review. The key insight is that **naive queries overestimate the problem** - using ontology closure to filter subsumed annotations reduces false positives by 70%+ in well-curated organisms.

## The Problem: Naive vs True SPKW-Unique

A **naive query** finds all genes with SPKW annotations but no other evidence for the same term:

```
Gene X has:
  - GO:0006915 (apoptotic process) from SPKW
  - No other annotation to GO:0006915
→ Naive query flags as "SPKW-unique"
```

But this misses cases where experimental evidence exists for a **more specific child term**:

```
Gene X has:
  - GO:0006915 (apoptotic process) from SPKW
  - GO:0097300 (programmed necrotic cell death) from IDA  ← child of GO:0006915!
→ The SPKW annotation is REDUNDANT, not unique
```

## Solution: Closure-Filtered Queries

The **TRUE SPKW-unique query** uses the ontology's is_a/part_of closure to exclude annotations that are subsumed by more specific experimental evidence:

> An SPKW annotation to term X is NOT unique if there exists a non-SPKW annotation to term Y where Y is_a X

This dramatically reduces false positives:
- **Human apoptosis**: Naive query returns ~500 genes, closure-filtered returns ~280 (44% reduction)
- **Well-curated organisms**: 70%+ reduction in candidates
- **Poorly-curated organisms**: Minimal reduction (closure filtering has less impact)

## SQL Queries

### Core Query: Find SPKW-Only Annotations (Naive)

```sql
-- Find proteins with annotations ONLY from UniProt Keywords (no corroboration)
-- Database: ~/repos/go-db/db/goa_human.ddb (or organism-specific)

WITH annotations_to_term AS (
    SELECT a.db_object_id, a.db_object_symbol, a.supporting_references
    FROM gaf_association a
    INNER JOIN isa_partof_closure ipc ON a.ontology_class_ref = ipc.subject
    WHERE ipc.object = 'GO:0006915'  -- or other term of interest
      AND a.is_negation = false
),
genes_with_other_evidence AS (
    SELECT DISTINCT db_object_id
    FROM annotations_to_term
    WHERE supporting_references != 'GO_REF:0000043'
),
spkw_only_genes AS (
    SELECT DISTINCT db_object_id, db_object_symbol
    FROM annotations_to_term
    WHERE supporting_references = 'GO_REF:0000043'
      AND db_object_id NOT IN (SELECT db_object_id FROM genes_with_other_evidence)
)
SELECT * FROM spkw_only_genes ORDER BY db_object_symbol;
```

### TRUE SPKW-Unique Query (Closure-Filtered)

For well-curated organisms, filter out SPKW annotations that are subsumed by more specific experimental evidence:

```sql
-- An SPKW annotation to term X is NOT unique if there exists
-- a non-SPKW annotation to term Y where Y is_a X

WITH spkw_annotations AS (
    SELECT a.db_object_id, a.db_object_symbol, a.ontology_class_ref, a.aspect
    FROM gaf_association a
    WHERE a.supporting_references = 'GO_REF:0000043'
),
gene_term_with_other_evidence AS (
    SELECT DISTINCT db_object_id, ontology_class_ref
    FROM gaf_association
    WHERE supporting_references != 'GO_REF:0000043'
),
-- Check if non-SPKW evidence exists for child terms
spkw_subsumed AS (
    SELECT DISTINCT s.db_object_id, s.ontology_class_ref
    FROM spkw_annotations s
    INNER JOIN isa_partof_closure ipc ON ipc.object = s.ontology_class_ref
    INNER JOIN gene_term_with_other_evidence g
        ON g.db_object_id = s.db_object_id
        AND g.ontology_class_ref = ipc.subject
),
true_spkw_unique AS (
    SELECT s.*
    FROM spkw_annotations s
    WHERE NOT EXISTS (
        SELECT 1 FROM gene_term_with_other_evidence o
        WHERE o.db_object_id = s.db_object_id
          AND o.ontology_class_ref = s.ontology_class_ref
    )
    AND NOT EXISTS (
        SELECT 1 FROM spkw_subsumed sub
        WHERE sub.db_object_id = s.db_object_id
          AND sub.ontology_class_ref = s.ontology_class_ref
    )
)
SELECT * FROM true_spkw_unique;
```

### Evidence Source Distribution

```sql
-- Count annotations by evidence source
SELECT
    supporting_references,
    COUNT(*) as annotation_count,
    COUNT(DISTINCT db_object_id) as gene_count
FROM gaf_association
GROUP BY supporting_references
ORDER BY annotation_count DESC;
```

## When to Use Each Query

| Organism Type | Recommended Query | Rationale |
|---------------|-------------------|-----------|
| Well-curated (human, mouse, yeast) | Closure-filtered | Many SPKW annotations are redundant with specific experimental evidence |
| Moderately curated (Arabidopsis, Drosophila) | Closure-filtered | Still significant redundancy |
| Poorly curated (most bacteria, parasites) | Naive | Little experimental evidence exists, so closure filtering has minimal effect |
| Phage/Virus | Naive | Very few annotations overall |

## Key Insight

**Use closure-based queries as the default** - they reduce false positives by 70%+ in well-curated organisms. The naive query is only useful when:
1. Exploring poorly-curated organisms
2. Wanting to see the full scope of SPKW coverage
3. Debugging or validating the closure-filtered results

---

## Stratifying by Swiss-Prot vs TrEMBL

### Why This Matters

Keywords are assigned differently based on reviewed status:
- **Swiss-Prot** (reviewed): Keywords are **manually assigned by curators**
- **TrEMBL** (unreviewed): Keywords are **automatically assigned** via RuleBase/Spearmint/ARBA

This distinction affects interpretation: over-annotations in Swiss-Prot entries indicate problems in the **KW→GO mapping**, while TrEMBL over-annotations could be from bad mappings OR bad automatic keyword assignment.

### Distribution Across SPKW Subprojects

| Organism | Swiss-Prot | TrEMBL | SP % | Method |
|----------|-----------|--------|------|--------|
| **Human** | 46,236 (15,172 proteins) | 186 (67) | **99.6%** | swissprot table |
| **T4 Phage** | 459 (128) | 2 (1) | **99.6%** | swissprot table |
| **E. coli O157** | 6,850 (2,419) | 881 (320) | **88.6%** | ID heuristic |
| **P. putida** | 2,345 (677) | 4,945 (2,233) | **32.2%** | swissprot table |
| **Virus (all)** | 23,747 (5,509) | 156,933 (52,452) | 13.1% | swissprot table |
| **A. gambiae** | 668 (250) | 17,119 (6,504) | **3.8%** | swissprot table |
| **Global UniProt** | 35.7M (11.2M) | 202M (77.7M) | **15%** | ID heuristic |
| S. pombe | ? | ? | ? | Uses gene IDs (SPAC...) |
| D. melanogaster | ? | ? | ? | Uses gene IDs (FBgn...) |
| A. thaliana | - | - | - | No SPKW in TAIR database |

### Query: Stratify by Reviewed Status

For databases with `swissprot` table:

```sql
WITH spkw AS (
    SELECT g.db_object_id,
           CASE WHEN sp.uniprot_accession IS NOT NULL
                THEN 'Swiss-Prot' ELSE 'TrEMBL' END as status
    FROM gaf_association g
    LEFT JOIN swissprot sp ON g.db_object_id = sp.uniprot_accession
    WHERE g.supporting_references = 'GO_REF:0000043'
)
SELECT status, COUNT(*) as annotations, COUNT(DISTINCT db_object_id) as proteins
FROM spkw GROUP BY status;
```

For databases without `swissprot` table (use ID length heuristic):

```sql
SELECT
    CASE
        WHEN LENGTH(db_object_id) = 6 THEN 'Swiss-Prot'
        WHEN LENGTH(db_object_id) = 10 THEN 'TrEMBL'
        ELSE 'Other'
    END as status,
    COUNT(*) as annotations
FROM gaf_association
WHERE supporting_references = 'GO_REF:0000043'
GROUP BY status;
```

### Limitations

- **MOD databases** (PomBase, FlyBase, TAIR) use organism-specific IDs, not UniProt accessions
- ID length heuristic is ~95% accurate but not perfect
- Some entries promoted from TrEMBL to Swiss-Prot retain automatic keywords
