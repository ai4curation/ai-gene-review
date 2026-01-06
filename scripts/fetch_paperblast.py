#!/usr/bin/env python3
"""Fetch PaperBlast results for a UniProt ID or sequence."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_gene_review.api.paperblast import fetch_paperblast_results


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_paperblast.py <uniprot_id_or_sequence> [--sequence]")
        print("\nExamples:")
        print("  python fetch_paperblast.py C5B1I4")
        print("  python fetch_paperblast.py MSKGEELFT... --sequence")
        sys.exit(1)

    query = sys.argv[1]
    query_type = "sequence" if "--sequence" in sys.argv else "uniprot"

    print(f"Fetching PaperBlast results for {query_type}: {query[:50]}...")
    print()

    results = fetch_paperblast_results(query, query_type=query_type)

    print(f"Found {len(results)} papers:\n")
    print("=" * 80)

    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result.title}")
        if result.pmid:
            print(f"   PMID: {result.pmid}")
        if result.link:
            print(f"   Link: {result.link}")
        if result.snippet:
            # Truncate long snippets
            snippet = result.snippet
            if len(snippet) > 200:
                snippet = snippet[:197] + "..."
            print(f"   Snippet: {snippet}")
        print()

    print("=" * 80)
    print(f"\nTotal: {len(results)} papers found")


if __name__ == "__main__":
    main()
