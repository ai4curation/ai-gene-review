"""LitScan: deterministic Europe PMC literature-scan jobs for genes and modules.

The scan jobs are high-recall lead generators. Each runs a query against Europe
PMC, deterministically matches results against the curated knowledge base (gene
reviews and pathway/complex modules), and writes a markdown + JSON ``packet``.
The packet is a handoff for downstream triage (e.g. a haiku filter agent); a scan
never edits a review or module file.

See ``docs/superpowers/specs/2026-06-19-litscan-gene-module-jobs-design.md``.
"""

from ai_gene_review.litscan.europepmc import Publication, search

__all__ = ["Publication", "search"]
