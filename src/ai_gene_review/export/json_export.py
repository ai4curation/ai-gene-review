"""Backwards compatibility - use annotation_export instead.

This module is deprecated. Please use:
    from ai_gene_review.export import AnnotationExporter

The AnnotationExporter class supports multiple output formats:
- export_to_json()
- export_to_jsonl()
- export_to_duckdb()
- export_to_datajs()
"""

from .annotation_export import AnnotationExporter, JSONExporter

__all__ = ["JSONExporter", "AnnotationExporter"]
