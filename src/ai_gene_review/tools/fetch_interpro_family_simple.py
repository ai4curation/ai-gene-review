#!/usr/bin/env python3
"""
Fetch protein family metadata using InterPro API - simple faithful conversion.

This tool fetches the raw InterPro API response and converts it to YAML,
optionally adding protein member lists.

Usage:
    python fetch_interpro_family_simple.py panther PTHR11447
    python fetch_interpro_family_simple.py panther PTHR11447 --include-proteins
"""

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import requests
import yaml


class InterProFamilyFetcherSimple:
    """Fetches protein family data via InterPro API with minimal processing."""

    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.base_url = "https://www.ebi.ac.uk/interpro/api"

    def fetch_family_data(self, database: str, family_id: str, include_proteins: bool = False) -> Dict[str, Any]:
        """
        Fetch family data from InterPro API with minimal processing.

        Args:
            database: Source database (e.g., 'panther', 'pfam')
            family_id: Family ID (e.g., 'PTHR11447', 'PF00001')
            include_proteins: Whether to include protein member lists

        Returns:
            Dictionary containing raw API response + optional protein data
        """
        print(f"🌐 Fetching {database} family {family_id} from InterPro API...")

        # Fetch basic family metadata
        family_url = f"{self.base_url}/entry/{database}/{family_id}/"

        try:
            response = requests.get(family_url, timeout=30)
            response.raise_for_status()
            family_data = response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch family metadata: {e}")

        # Start with the raw API response
        result = family_data.copy()

        # Add fetch metadata
        result["_fetch_info"] = {
            "fetched_date": datetime.now().isoformat(),
            "api_endpoint": family_url,
            "database": database,
            "family_id": family_id
        }

        # Optionally add protein members
        if include_proteins:
            print("🧬 Fetching reviewed protein members...")
            proteins = self._fetch_protein_members(database, family_id)
            result["reviewed_proteins"] = proteins

        return result

    def _fetch_protein_members(self, database: str, family_id: str) -> List[Dict[str, Any]]:
        """Fetch reviewed protein members from InterPro API."""

        protein_endpoint = f"{self.base_url}/protein/reviewed/entry/{database}/{family_id}/"
        proteins = []
        page_count = 0
        next_url = protein_endpoint

        try:
            while next_url and page_count < 50:  # Limit to prevent runaway requests
                page_count += 1
                print(f"   Fetching page {page_count}...")

                response = requests.get(next_url, timeout=30)
                response.raise_for_status()
                data = response.json()

                # Add proteins from this page
                proteins.extend(data.get("results", []))

                # Check for next page
                next_url = data.get("next")
                if not next_url:
                    break

        except requests.exceptions.RequestException as e:
            print(f"⚠️  Warning: Could not fetch all protein members: {e}")

        print(f"✅ Retrieved {len(proteins)} reviewed protein members")
        return proteins

    def create_family_directory(self, database: str, family_id: str) -> Path:
        """Create interpro/database/family_id directory structure."""
        family_dir = self.output_dir / "interpro" / database / family_id
        family_dir.mkdir(parents=True, exist_ok=True)
        return family_dir

    def save_family_data(self, database: str, family_id: str, data: Dict[str, Any]) -> tuple[Path, Optional[Path]]:
        """Save family data as separate metadata YAML and entries CSV files."""
        family_dir = self.create_family_directory(database, family_id)

        # Extract proteins for CSV and remove from metadata
        proteins = data.pop("reviewed_proteins", None)

        # Save metadata YAML (without proteins)
        yaml_file = family_dir / f"{family_id}-metadata.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        # Save entries CSV if proteins exist
        csv_file = None
        if proteins:
            csv_file = family_dir / f"{family_id}-entries.csv"
            self._save_entries_csv(csv_file, proteins)

        return yaml_file, csv_file

    def _save_entries_csv(self, csv_file: Path, proteins: List[Dict[str, Any]]) -> None:
        """Save protein entries as CSV with flattened structure."""
        if not proteins:
            return

        # Extract flattened protein data
        entries = []
        for protein in proteins:
            metadata = protein.get("metadata", {})
            organism = metadata.get("source_organism", {})

            entry = {
                "id": metadata.get("accession"),
                "name": metadata.get("name"),
                "entry_type": "protein",  # All are proteins from the protein endpoint
                "source_tax_id": organism.get("taxId"),
                "source_tax_name": organism.get("scientificName"),
                "full_tax_name": organism.get("fullName"),
                "gene": metadata.get("gene"),
                "length": metadata.get("length"),
                "in_alphafold": metadata.get("in_alphafold", False),
                "subfamily": None  # Will be populated from entries if available
            }

            # Extract subfamily information from entries
            entries_list = protein.get("entries", [])
            if entries_list:
                for entry_info in entries_list:
                    locations = entry_info.get("entry_protein_locations", [])
                    for location in locations:
                        subfamily_info = location.get("subfamily")
                        if subfamily_info:
                            entry["subfamily"] = subfamily_info.get("accession")
                            entry["subfamily_name"] = subfamily_info.get("name")
                            break
                    if entry["subfamily"]:
                        break

            entries.append(entry)

        # Write CSV
        if entries:
            fieldnames = ["id", "name", "entry_type", "source_tax_id", "source_tax_name",
                         "full_tax_name", "gene", "length", "subfamily", "subfamily_name",
                         "in_alphafold"]

            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(entries)

    def fetch_and_save(self, database: str, family_id: str, include_proteins: bool = False) -> None:
        """Main method to fetch and save family data via InterPro API."""
        print(f"Fetching {database} family {family_id} via InterPro API...")

        # Fetch data
        data = self.fetch_family_data(database, family_id, include_proteins)

        # Save to files
        yaml_file, csv_file = self.save_family_data(database, family_id, data)

        print(f"✅ Family metadata saved to: {yaml_file}")
        if csv_file:
            print(f"✅ Protein entries saved to: {csv_file}")
        print(f"📁 Family directory: {yaml_file.parent}")

        # Display summary
        self._print_summary(data, csv_file)

    def _print_summary(self, data: Dict[str, Any], csv_file: Optional[Path] = None) -> None:
        """Print a summary of the fetched data."""
        metadata = data.get("metadata", {})

        print("\n📊 Family Summary:")
        print(f"   Family ID: {metadata.get('accession')}")
        print(f"   Database: {metadata.get('source_database', '').upper()}")
        name_info = metadata.get("name", {})
        if name_info:
            print(f"   Family Name: {name_info.get('name')}")
            if name_info.get('short'):
                print(f"   Short Name: {name_info.get('short')}")

        counters = metadata.get("counters", {})
        if counters:
            print(f"   Subfamilies: {counters.get('subfamilies', 0)}")
            print(f"   Total Proteins: {counters.get('proteins', 0)}")
            print(f"   Structures: {counters.get('structures', 0)}")
            print(f"   Taxa: {counters.get('taxa', 0)}")

        if csv_file and csv_file.exists():
            # Count entries in CSV file
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                entry_count = sum(1 for row in reader)
            print(f"   Reviewed Proteins (CSV): {entry_count}")

        fetch_info = data.get("_fetch_info", {})
        if fetch_info.get("fetched_date"):
            print(f"   Fetched: {fetch_info['fetched_date'][:19]}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch protein family metadata via InterPro API (simple)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python fetch_interpro_family_simple.py panther PTHR11447
    python fetch_interpro_family_simple.py panther PTHR11447 --include-proteins
    python fetch_interpro_family_simple.py pfam PF00001
        """
    )

    parser.add_argument(
        "database",
        help="Source database (e.g., panther, pfam, smart, etc.)"
    )

    parser.add_argument(
        "family_id",
        help="Family ID (e.g., PTHR11447, PF00001)"
    )

    parser.add_argument(
        "--include-proteins",
        action="store_true",
        help="Include reviewed protein member lists"
    )

    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory (default: current directory)"
    )

    args = parser.parse_args()

    try:
        fetcher = InterProFamilyFetcherSimple(args.output_dir)
        fetcher.fetch_and_save(args.database, args.family_id, args.include_proteins)

    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()