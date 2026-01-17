"""Build and maintain ontology term cache.

This script scans all YAML files and GOA files for ontology term IDs,
fetches their labels from OLS or OAK, and writes a cached TSV file.
This allows for fast, offline validation and prevents breakage when
ontology labels change upstream.
"""

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Set

import pandas as pd
import yaml
from oaklib import get_adapter  # type: ignore[import-untyped]


@dataclass
class OntologyCacheMetadata:
    """Metadata about the ontology cache."""

    ontology_id: str
    version: Optional[str]
    cache_date: str
    source: str
    term_count: int
    notes: str


class OntologyCacheBuilder:
    """Build and update ontology term caches."""

    def __init__(self, repo_root: Path):
        """Initialize the cache builder.

        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = Path(repo_root)
        self.cache_dir = self.repo_root / "cache" / "ontologies"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.genes_dir = self.repo_root / "genes"

    def collect_term_ids(self, ontology_prefix: str) -> Set[str]:
        """Collect all term IDs for an ontology from YAML and GOA files.

        Args:
            ontology_prefix: Ontology prefix (e.g., 'GO', 'CHEBI')

        Returns:
            Set of term IDs found
        """
        term_ids: Set[str] = set()
        prefix_pattern = f"{ontology_prefix}:"

        # Scan YAML files
        for yaml_file in self.genes_dir.rglob("*-ai-review.yaml"):
            try:
                with open(yaml_file) as f:
                    data = yaml.safe_load(f)
                    self._extract_term_ids(data, prefix_pattern, term_ids)
            except Exception as e:
                print(f"Warning: Could not read {yaml_file}: {e}")

        # Scan GOA files
        for goa_file in self.genes_dir.rglob("*-goa.tsv"):
            try:
                df = pd.read_csv(goa_file, sep="\t", comment="!")
                if "GO_ID" in df.columns:
                    go_ids = df["GO_ID"].dropna().unique()
                    term_ids.update(
                        [gid for gid in go_ids if gid.startswith(prefix_pattern)]
                    )
            except Exception as e:
                print(f"Warning: Could not read {goa_file}: {e}")

        return term_ids

    def _extract_term_ids(self, data, prefix_pattern: str, term_ids: Set[str]):
        """Recursively extract term IDs from data structure."""
        if isinstance(data, dict):
            if "id" in data and isinstance(data["id"], str):
                term_id = data["id"]
                if term_id.startswith(prefix_pattern):
                    term_ids.add(term_id)
            for value in data.values():
                self._extract_term_ids(value, prefix_pattern, term_ids)
        elif isinstance(data, list):
            for item in data:
                self._extract_term_ids(item, prefix_pattern, term_ids)

    def fetch_term_labels(
        self, term_ids: Set[str], ontology_id: str
    ) -> Dict[str, Dict]:
        """Fetch labels and metadata for terms.

        Args:
            term_ids: Set of term IDs to fetch
            ontology_id: Ontology identifier for OAK (e.g., 'go', 'chebi')

        Returns:
            Dictionary mapping term_id to {label, is_obsolete, fetched_date}
        """
        results: Dict[str, Dict[str, Any]] = {}

        try:
            print(f"Loading {ontology_id} ontology via OAK...")
            adapter = get_adapter(f"sqlite:obo:{ontology_id}")
        except Exception as e:
            print(f"Could not load adapter for {ontology_id}: {e}")
            return results

        for term_id in sorted(term_ids):
            try:
                label = adapter.label(term_id)

                # Check if term is obsolete by seeing if label starts with "obsolete"
                is_obsolete = False
                if label and label.lower().startswith("obsolete"):
                    is_obsolete = True

                if label:
                    results[term_id] = {
                        "label": label,
                        "is_obsolete": is_obsolete,
                        "fetched_date": datetime.now().isoformat(),
                    }
                    if is_obsolete:
                        print(f"  {term_id} -> {label} [OBSOLETE]")
                    else:
                        print(f"  {term_id} -> {label}")
                else:
                    print(f"  {term_id} -> NOT FOUND")
            except Exception as e:
                print(f"  {term_id} -> ERROR: {e}")

        return results

    def write_cache(
        self,
        ontology_id: str,
        term_data: Dict[str, Dict],
        notes: str = "",
    ):
        """Write cache TSV and metadata.

        Args:
            ontology_id: Ontology identifier (e.g., 'go')
            term_data: Dictionary of term data
            notes: Optional notes for metadata
        """
        # Write TSV
        tsv_path = self.cache_dir / f"{ontology_id}.tsv"
        rows = []
        for term_id, data in sorted(term_data.items()):
            rows.append(
                {
                    "term_id": term_id,
                    "label": data["label"],
                    "is_obsolete": str(data["is_obsolete"]).lower(),
                    "fetched_date": data["fetched_date"],
                }
            )

        df = pd.DataFrame(rows)
        df.to_csv(tsv_path, sep="\t", index=False)
        print(f"\nWrote {len(rows)} terms to {tsv_path}")

        # Write metadata
        metadata = OntologyCacheMetadata(
            ontology_id=ontology_id,
            version=None,  # Could fetch from ontology if available
            cache_date=datetime.now().isoformat(),
            source="OAK (sqlite:obo)",
            term_count=len(rows),
            notes=notes,
        )

        meta_path = self.cache_dir / f"{ontology_id}.meta.json"
        with open(meta_path, "w") as f:
            json.dump(metadata.__dict__, f, indent=2)
        print(f"Wrote metadata to {meta_path}")

    def update_ontology_cache(self, ontology_prefix: str, ontology_id: str):
        """Update cache for a specific ontology.

        Args:
            ontology_prefix: CURIE prefix (e.g., 'GO')
            ontology_id: OAK ontology identifier (e.g., 'go')
        """
        print(f"\n{'='*60}")
        print(f"Updating cache for {ontology_prefix} ({ontology_id})")
        print(f"{'='*60}\n")

        # Collect term IDs
        print("Step 1: Collecting term IDs from YAML and GOA files...")
        term_ids = self.collect_term_ids(ontology_prefix)
        print(f"Found {len(term_ids)} unique {ontology_prefix} terms\n")

        if not term_ids:
            print(f"No {ontology_prefix} terms found, skipping cache update")
            return

        # Fetch labels
        print("Step 2: Fetching labels from ontology...")
        term_data = self.fetch_term_labels(term_ids, ontology_id)
        print(f"Successfully fetched {len(term_data)} term labels\n")

        # Write cache
        print("Step 3: Writing cache files...")
        self.write_cache(
            ontology_id,
            term_data,
            notes=f"Only terms used in annotations (from {len(term_ids)} scanned)",
        )

        print(f"\n✓ Cache update complete for {ontology_prefix}")


def main():
    """Main entry point for cache building."""
    import argparse

    parser = argparse.ArgumentParser(description="Build ontology term cache")
    parser.add_argument(
        "--ontology",
        choices=["go", "chebi", "uberon", "all"],
        default="go",
        help="Ontology to update (default: go)",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory",
    )

    args = parser.parse_args()

    builder = OntologyCacheBuilder(args.repo_root)

    ontology_map = {
        "go": ("GO", "go"),
        "chebi": ("CHEBI", "chebi"),
        "uberon": ("UBERON", "uberon"),
    }

    if args.ontology == "all":
        for prefix, ontology_id in ontology_map.values():
            try:
                builder.update_ontology_cache(prefix, ontology_id)
            except Exception as e:
                print(f"Error updating {prefix}: {e}")
    else:
        prefix, ontology_id = ontology_map[args.ontology]
        builder.update_ontology_cache(prefix, ontology_id)


if __name__ == "__main__":
    main()
