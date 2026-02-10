#!/usr/bin/env python3
"""Query redundancy data from the annotations DuckDB."""

import sys
import duckdb


def spkw_redundant_with_experimental():
    """Show SPKW annotations subsumed by experimental evidence."""
    conn = duckdb.connect('exports/annotations.duckdb')
    print("=== SPKW Annotations Subsumed by Experimental Evidence ===\n")
    result = conn.execute("""
        SELECT r.general_term_label as spkw_term,
               COUNT(DISTINCT r.gene_symbol) as genes,
               r.relationship
        FROM redundant_with r
        JOIN annotations a1 ON r.general_annotation_id = a1.id
        JOIN annotations a2 ON r.specific_annotation_id = a2.id
        WHERE a1.original_reference_id = 'GO_REF:0000043'
          AND a2.original_reference_id != 'GO_REF:0000043'
        GROUP BY r.general_term_label, r.relationship
        ORDER BY genes DESC
        LIMIT 30
    """).fetchdf()
    print(result.to_string())


def spkw_regulatory_conflation():
    """Show regulatory conflation patterns."""
    conn = duckdb.connect('exports/annotations.duckdb')
    print("=== Regulatory Conflation: SPKW 'participates in X' vs Experimental 'regulates X' ===\n")
    result = conn.execute("""
        SELECT r.gene_symbol, r.general_term_label as spkw_term,
               r.specific_term_label as experimental_term
        FROM redundant_with r
        JOIN annotations a1 ON r.general_annotation_id = a1.id
        JOIN annotations a2 ON r.specific_annotation_id = a2.id
        WHERE a1.original_reference_id = 'GO_REF:0000043'
          AND a2.original_reference_id != 'GO_REF:0000043'
          AND r.relationship = 'REGULATES'
        ORDER BY r.gene_symbol
        LIMIT 50
    """).fetchdf()
    print(result.to_string())


def full_analysis():
    """Run full SPKW redundancy analysis with all summary tables."""
    import pandas as pd
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.width', 200)

    conn = duckdb.connect('exports/annotations.duckdb', read_only=True)

    print('=' * 80)
    print('DATABASE OVERVIEW')
    print('=' * 80)
    print(f"Total annotations: {conn.execute('SELECT COUNT(*) FROM annotations').fetchone()[0]:,}")
    print(f"Total redundancy relationships: {conn.execute('SELECT COUNT(*) FROM redundant_with').fetchone()[0]:,}")
    print()

    print('=' * 80)
    print('ANNOTATIONS BY SPECIES AND SOURCE')
    print('=' * 80)
    species_spkw = conn.execute("""
        SELECT
            taxon_label,
            CASE WHEN original_reference_id = 'GO_REF:0000043' THEN 'SPKW' ELSE 'Other' END as source,
            COUNT(*) as count
        FROM annotations
        GROUP BY taxon_label, source
        ORDER BY taxon_label, source
    """).fetchdf()
    species_pivot = species_spkw.pivot(index='taxon_label', columns='source', values='count').fillna(0).astype(int)
    species_pivot['Total'] = species_pivot.sum(axis=1)
    species_pivot['SPKW_pct'] = (species_pivot['SPKW'] / species_pivot['Total'] * 100).round(1)
    species_pivot = species_pivot.sort_values('Total', ascending=False)
    print(species_pivot.to_string())
    print()

    print('=' * 80)
    print('SPKW REDUNDANCY BY SPECIES AND RELATIONSHIP TYPE')
    print('=' * 80)
    redundancy_summary = conn.execute("""
        WITH spkw_annotations AS (
            SELECT id, gene_symbol, term_id, term_label, taxon_label
            FROM annotations
            WHERE original_reference_id = 'GO_REF:0000043'
        ),
        spkw_with_redundancy AS (
            SELECT DISTINCT s.id, s.gene_symbol, s.term_label, s.taxon_label, r.relationship
            FROM spkw_annotations s
            JOIN redundant_with r ON s.id = r.general_annotation_id
            JOIN annotations a2 ON r.specific_annotation_id = a2.id
            WHERE a2.original_reference_id != 'GO_REF:0000043'
        )
        SELECT
            taxon_label,
            relationship,
            COUNT(DISTINCT id) as redundant_annotations
        FROM spkw_with_redundancy
        GROUP BY taxon_label, relationship
        ORDER BY taxon_label, relationship
    """).fetchdf()

    if not redundancy_summary.empty:
        redundancy_pivot = redundancy_summary.pivot(
            index='taxon_label',
            columns='relationship',
            values='redundant_annotations'
        ).fillna(0).astype(int)
        redundancy_pivot['Total_Redundant'] = redundancy_pivot.sum(axis=1)
        redundancy_pivot = redundancy_pivot.sort_values('Total_Redundant', ascending=False).head(25)
        print(redundancy_pivot.to_string())
    print()

    print('=' * 80)
    print('REVIEW ACTION DISTRIBUTION (SPKW vs Other)')
    print('=' * 80)
    action_dist = conn.execute("""
        SELECT
            CASE WHEN original_reference_id = 'GO_REF:0000043' THEN 'SPKW' ELSE 'Other' END as source,
            "review.action" as review_action,
            COUNT(*) as count
        FROM annotations
        WHERE "review.action" IS NOT NULL
        GROUP BY source, "review.action"
        ORDER BY source, count DESC
    """).fetchdf()
    action_pivot = action_dist.pivot(index='review_action', columns='source', values='count').fillna(0).astype(int)
    action_pivot['Total'] = action_pivot.sum(axis=1)
    action_pivot = action_pivot.sort_values('Total', ascending=False)
    print(action_pivot.to_string())
    print()

    print('=' * 80)
    print('SWISS-PROT vs TrEMBL BREAKDOWN')
    print('=' * 80)
    swissprot = conn.execute("""
        SELECT
            CASE WHEN is_swissprot IS TRUE THEN 'Swiss-Prot'
                 WHEN is_swissprot IS FALSE THEN 'TrEMBL'
                 ELSE 'Unknown' END as db,
            CASE WHEN original_reference_id = 'GO_REF:0000043' THEN 'SPKW' ELSE 'Other' END as source,
            COUNT(*) as annotations,
            COUNT(DISTINCT gene_symbol) as genes
        FROM annotations
        GROUP BY db, source
        ORDER BY db, source
    """).fetchdf()
    print(swissprot.to_string())
    print()

    print('=' * 80)
    print('SPKW OVER-ANNOTATION RATES BY SPECIES (min 10 SPKW annotations)')
    print('=' * 80)
    overannotation = conn.execute("""
        SELECT
            taxon_label,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043') as spkw_total,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                             AND "review.action" = 'MARK_AS_OVER_ANNOTATED') as spkw_overannotated,
            ROUND(100.0 * COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                                            AND "review.action" = 'MARK_AS_OVER_ANNOTATED') /
                  NULLIF(COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'), 0), 1) as overannotation_rate_pct
        FROM annotations
        GROUP BY taxon_label
        HAVING COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043') > 10
        ORDER BY overannotation_rate_pct DESC NULLS LAST
    """).fetchdf()
    print(overannotation.to_string())
    print()

    print('=' * 80)
    print('OVER-ANNOTATION RATES BY SWISS-PROT STATUS')
    print('=' * 80)
    sp_overannotation = conn.execute("""
        SELECT
            CASE WHEN is_swissprot IS TRUE THEN 'Swiss-Prot'
                 WHEN is_swissprot IS FALSE THEN 'TrEMBL'
                 ELSE 'Unknown' END as db,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043') as spkw_total,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                             AND "review.action" = 'MARK_AS_OVER_ANNOTATED') as spkw_overannotated,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                             AND "review.action" = 'ACCEPT') as spkw_accepted,
            COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                             AND "review.action" = 'MODIFY') as spkw_modified,
            ROUND(100.0 * COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'
                                            AND "review.action" = 'MARK_AS_OVER_ANNOTATED') /
                  NULLIF(COUNT(*) FILTER (WHERE original_reference_id = 'GO_REF:0000043'), 0), 1) as overannotation_pct
        FROM annotations
        GROUP BY db
        ORDER BY db
    """).fetchdf()
    print(sp_overannotation.to_string())

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: query_redundancy.py <command>")
        print("Commands: spkw-redundant, spkw-regulatory, all")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "spkw-redundant":
        spkw_redundant_with_experimental()
    elif cmd == "spkw-regulatory":
        spkw_regulatory_conflation()
    elif cmd == "all":
        full_analysis()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
