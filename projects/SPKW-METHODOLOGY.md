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
| Single phage or small viral proteome | Naive | Few annotations overall; closure filtering may hide the practical review queue |
| Virus-wide mixed-clade dataset | Naive + closure-filtered | Naive gives the scope; closure filtering reduced `virus.ddb` candidates by 41% and is useful for prioritization |

## Key Insight

**Use closure-based queries as the default** - they reduce false positives by 70%+ in well-curated organisms. The naive query is only useful when:
1. Exploring poorly-curated organisms
2. Wanting to see the full scope of SPKW coverage
3. Debugging or validating the closure-filtered results

For viruses, use both views when working across many clades. The virus-wide analysis in [SPKW-VIRUS.md](SPKW-VIRUS.md) found 135,117 naive SPKW-unique annotations and 80,218 closure-filtered SPKW-unique annotations.

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

---

## Keyword-Level View: Reverse-Mapping GO Terms to Source Keywords

All SPKW analyses above work at the **GO-term** level, because the GAF stores only the GO
term (`ontology_class_ref`) and `supporting_references='GO_REF:0000043'` — **not** the source
UniProt keyword. To ask the more direct question — *which UniProt keywords drive
over-annotation?* — reverse-map each SPKW-unique GO term to its source keyword(s) using the
public GOA/UniProt **keyword2go** mapping:

```bash
# 744 keyword->GO mappings (version date in the file header)
curl -sL https://current.geneontology.org/ontology/external2go/uniprotkb_kw2go -o kw2go.txt
# Parse "UniProtKB-KW:KW-0067 ATP-binding > GO:ATP binding ; GO:0005524" -> go_id, kw_id, kw_name
grep -vE '^!' kw2go.txt \
  | sed -E 's/^UniProtKB-KW:(KW-[0-9]+) (.+) > GO:.+ ; (GO:[0-9]+)$/\3\t\1\t\2/' > kw2go.tsv
```

Then `LEFT JOIN` `kw2go` on `ontology_class_ref` and aggregate by keyword. One GO term can
map from several keywords (e.g. *defense response* ← `Plant defense` / `Defensin` /
`Antimicrobial`), so pick the keyword whose biology matches the organism set.

### The keyword watch-list (non-Arabidopsis plants, ranked by SPKW-unique gene count)

Tiering follows [SPKW-PLANTS.md](SPKW-PLANTS.md). The over-annotation risk is concentrated in
a small set of **process / pathway / role** keywords; the high-count keywords are otherwise
broad-but-correct binding/enzyme-class terms.

| Tier | UniProt keyword(s) | → GO term | plant genes | Reviewed? |
|------|--------------------|-----------|-------------|-----------|
| **A** | Plant defense (also Defensin, Antimicrobial) | defense response (GO:0006952) | 312 | partial (STS3, PR1B1, MPK4a) |
| **A** | Auxin signaling pathway | auxin-activated signaling pathway (GO:0009734) | 120 | yes (ABP1; ARF19 ARATH) |
| **A** | **Methyltransferase** | methylation (GO:0032259) | 92 | **no — top unreviewed** |
| **A** | Cell division | cell division (GO:0051301) | 81 | yes (AM1; BUB3.1 ARATH) |
| **A** | **Differentiation** | cell differentiation (GO:0030154) | 62 | **no** (MADS-box TFs) |
| **A** | **Flowering** | flower development (GO:0009908) | 46 | partial (ELF4 ARATH) |
| **A** | Defensin / Cytolysis / Hemolysis | killing of cells of another organism (GO:0031640) | 42 | partial (LCR1, PR1B1) |
| **A** | **Nodulation** | nodulation (GO:0009877) | 40 | partial (NFP) |
| A | Abscisic acid / Gibberellin / Brassinosteroid / Cytokinin / Ethylene signaling | respective `*-activated/mediated signaling pathway` | 9–25 each | partial (RHT1=GA) |
| B | Metal-binding, Metal-thiolate cluster | metal ion binding (GO:0046872) | 1149 | low risk (broad, correct) |
| B | Nucleotide-binding / ATP-binding / Zinc-finger | nucleotide / ATP / zinc binding | 286–342 | low risk |
| C | Ribonucleoprotein | ribonucleoprotein complex (GO:1990904) | 235 | correct |
| C | Cell wall biogenesis/degradation | cell wall organization (GO:0071555) | 140 | correct (CASP1) |
| C | Storage protein / Seed storage protein | nutrient reservoir activity (GO:0045735) | 54 | correct (PATB1) |
| D | Photosynthesis / Chlorophyll-binding | photosynthesis, photosystem I/II | 65–110 | context (PPC16, psaC) |

### Two over-annotation mechanisms made explicit at the keyword level

1. **Enzyme-class keyword → bare process term.** `Methyltransferase` (a molecular-function
   keyword) maps to the generic process *methylation* (GO:0032259) — uninformative, and
   sometimes wrong about the substrate (protein vs DNA vs small-molecule methyltransferases
   all collapse to one term). The same shape produced *cell division* from `Cell division`.
2. **Pathway/role keyword → developmental or defense process.** `Differentiation`,
   `Flowering`, `Nodulation`, `Plant defense` attach broad process terms to genes that merely
   act *during* (or are *induced by*) the process — the recurring "expression ≠ function" and
   "responsive ≠ component" patterns.

**Cross-organism reuse.** Because keyword2go is organism-independent, this watch-list of ~30
process/role keywords is the same lever in any taxon — the keywords flagged here (defense,
hormone signaling, differentiation, methylation, cell division/meiosis, killing) are exactly
those that drove over-annotation in the human, *S. pombe*, and Arabidopsis subprojects.
