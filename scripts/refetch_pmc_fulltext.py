#!/usr/bin/env python3
"""Re-fetch full text for PMC publications that don't have it yet.

This script scans the publications folder for articles with PMC IDs but
full_text_available: false, then uses the new HTML fallback to try to
retrieve the full text.
"""

import time
import yaml
from pathlib import Path
from typing import List, Dict, Any

from ai_gene_review.etl.publication import cache_publication


def find_pmc_candidates(
    publications_dir: Path = Path("publications"),
) -> List[Dict[str, Any]]:
    """Find PMC publications without full text."""
    candidates = []

    if not publications_dir.exists():
        print(f"Publications directory {publications_dir} not found!")
        return candidates

    for md_file in publications_dir.glob("PMID_*.md"):
        try:
            content = md_file.read_text()

            # Parse frontmatter
            if not content.startswith("---"):
                continue

            # Extract frontmatter
            parts = content.split("---", 2)
            if len(parts) < 3:
                continue

            frontmatter = yaml.safe_load(parts[1])
            body = parts[2]

            pmid = frontmatter.get("pmid")
            pmcid = frontmatter.get("pmcid")
            full_text_available = frontmatter.get("full_text_available", False)

            # Check if this is a candidate for re-fetch
            has_full_text_section = "## Full Text" in body

            if pmcid and (not full_text_available or not has_full_text_section):
                candidates.append(
                    {
                        "pmid": pmid,
                        "pmcid": pmcid,
                        "file": md_file.name,
                        "full_text_available": full_text_available,
                        "has_full_text_section": has_full_text_section,
                    }
                )

        except Exception as e:
            print(f"Error processing {md_file.name}: {e}")

    return candidates


def refetch_full_text(
    candidates: List[Dict[str, Any]], max_requests: int = None, delay: float = 1.0
) -> Dict[str, int]:
    """Re-fetch full text for candidate publications.

    Args:
        candidates: List of candidate publications
        max_requests: Maximum number of requests to make (None for all)
        delay: Delay between requests in seconds

    Returns:
        Dictionary with success/failure counts
    """
    stats = {"processed": 0, "success": 0, "failed": 0, "already_had_full_text": 0}

    total_to_process = (
        len(candidates) if max_requests is None else min(max_requests, len(candidates))
    )

    print(f"Re-fetching full text for {total_to_process} publications...")
    print()

    for i, candidate in enumerate(candidates):
        if max_requests and i >= max_requests:
            break

        pmid = candidate["pmid"]
        pmcid = candidate["pmcid"]

        print(f"[{i + 1}/{total_to_process}] Processing PMID {pmid} ({pmcid})...")

        try:
            success = cache_publication(pmid, Path("publications"), force=True)

            if success:
                # Check if full text was actually retrieved
                pub_file = Path("publications") / f"PMID_{pmid}.md"
                content = pub_file.read_text()

                if "full_text_available: true" in content and "## Full Text" in content:
                    print("  ✓ Full text retrieved!")
                    stats["success"] += 1
                else:
                    print("  ⚠ Still no full text (may be restricted)")
                    stats["failed"] += 1
            else:
                print("  ✗ Failed to fetch publication")
                stats["failed"] += 1

        except Exception as e:
            print(f"  ✗ Error: {e}")
            stats["failed"] += 1

        stats["processed"] += 1

        # Be polite to servers
        if i < total_to_process - 1:  # Don't delay after the last request
            time.sleep(delay)

        print()

    return stats


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Re-fetch full text for PMC publications with missing content"
    )
    parser.add_argument(
        "--batch-size", type=int, help="Number of publications to process"
    )
    parser.add_argument(
        "--all", action="store_true", help="Process all publications needing refresh"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("PMC Full Text Re-fetch Script")
    print("=" * 60)
    print()

    # Find candidates
    print("Scanning publications folder...")
    candidates = find_pmc_candidates()

    if not candidates:
        print("No candidates found for re-fetch.")
        return

    print(f"Found {len(candidates)} publications with PMC IDs but no full text.")
    print()

    # Determine how many to process
    if args.all:
        max_requests = None
        print("Processing ALL publications...")
    elif args.batch_size:
        max_requests = args.batch_size
        print(f"Processing batch of {max_requests} publications...")
    else:
        # Interactive mode
        try:
            response = input(
                f"How many would you like to re-fetch? (1-{len(candidates)}, or 'all'): "
            ).strip()

            if response.lower() == "all":
                max_requests = None
            else:
                max_requests = int(response)
                if max_requests < 1 or max_requests > len(candidates):
                    print(f"Invalid number. Please enter 1-{len(candidates)} or 'all'.")
                    return
        except (ValueError, KeyboardInterrupt):
            print("Cancelled.")
            return

    # Re-fetch publications
    stats = refetch_full_text(candidates, max_requests=max_requests, delay=args.delay)

    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Processed: {stats['processed']}")
    print(f"Success (full text retrieved): {stats['success']}")
    print(f"Failed (still no full text): {stats['failed']}")

    if stats["processed"] > 0:
        success_rate = stats["success"] / stats["processed"] * 100
        print(f"Success rate: {success_rate:.1f}%")

    print()
    print("Re-fetch complete!")


if __name__ == "__main__":
    main()
