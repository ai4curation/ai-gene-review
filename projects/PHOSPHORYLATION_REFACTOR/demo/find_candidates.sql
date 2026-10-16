-- Run against a go-db DuckDB snapshot, e.g.:
-- duckdb -readonly ~/repos/go-db/db/mgi.ddb -csv < find_candidates.sql
-- This discovers candidates, not annotation errors. Refresh the rows in QuickGO
-- and check protein identity, literature, and the repository before selection.
WITH positive AS MATERIALIZED (
    SELECT * FROM gaf_association
    WHERE NOT coalesce(is_negation, false)
      AND coalesce(qualifiers, '') NOT LIKE '%NOT%'
), protein_process AS (
    SELECT DISTINCT subject AS id FROM isa_partof_closure
    WHERE object = 'GO:0006468'
    UNION SELECT 'GO:0006468'
), protein_kinase_terms AS (
    SELECT DISTINCT subject AS id FROM isa_partof_closure
    WHERE object = 'GO:0004672'
    UNION SELECT 'GO:0004672'
), all_kinase_terms AS (
    SELECT DISTINCT subject AS id FROM isa_partof_closure
    WHERE object = 'GO:0016301'
    UNION SELECT 'GO:0016301'
), protein_kinases AS MATERIALIZED (
    SELECT DISTINCT db, db_object_id, db_object_symbol, db_object_taxon
    FROM positive WHERE ontology_class_ref IN (SELECT id FROM protein_kinase_terms)
), all_kinases AS MATERIALIZED (
    SELECT DISTINCT db, db_object_id, db_object_symbol, db_object_taxon
    FROM positive WHERE ontology_class_ref IN (SELECT id FROM all_kinase_terms)
)
SELECT DISTINCT a.db, a.db_object_id, a.db_object_symbol, a.db_object_taxon,
    a.db_object_name, a.ontology_class_ref, t.label, a.qualifiers,
    a.evidence_type, a.supporting_references, a.with_or_from,
    a.assigned_by, a.annotation_date_string
FROM positive a JOIN term_label t ON t.id = a.ontology_class_ref
WHERE a.aspect = 'P' AND a.qualifiers = 'involved_in'
  AND t.label NOT ILIKE '%regulation%'
  AND t.label NOT ILIKE '%activation%'
  AND (
    (a.ontology_class_ref IN (SELECT id FROM protein_process)
     AND NOT EXISTS (
       SELECT 1 FROM protein_kinases k
       WHERE k.db_object_taxon = a.db_object_taxon
         AND ((k.db = a.db AND k.db_object_id = a.db_object_id)
              OR k.db_object_symbol = a.db_object_symbol)
     ))
    OR
    (a.ontology_class_ref IN ('GO:0016310', 'GO:0046835')
     AND NOT EXISTS (
       SELECT 1 FROM all_kinases k
       WHERE k.db_object_taxon = a.db_object_taxon
         AND ((k.db = a.db AND k.db_object_id = a.db_object_id)
              OR k.db_object_symbol = a.db_object_symbol)
     ))
  )
ORDER BY a.db_object_symbol, a.ontology_class_ref;
