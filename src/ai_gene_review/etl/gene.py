"""Gene data ETL module for fetching UniProt and GOA data.

This module provides functionality to fetch gene data from UniProt and GOA APIs
and save them in a structured directory format.

Example:
    >>> from ai_gene_review.etl.gene import fetch_gene_data
    >>> fetch_gene_data(("human", "CFAP300"), uniprot_id="Q9BRQ4")  # doctest: +SKIP

    This creates:
    genes/
      human/
        CFAP300/
          CFAP300-uniprot.txt
          CFAP300-goa.csv
"""

from pathlib import Path
from typing import Tuple, Optional, List, Dict, Any
import requests
import yaml
import re


def _extract_panther_family_id(uniprot_data: str) -> Optional[str]:
    """Extract PANTHER family ID from UniProt data.

    Args:
        uniprot_data: Raw UniProt text data

    Returns:
        PANTHER family ID (e.g., "PTHR11447") or None if not found
    """
    # Look for lines like: DR   PANTHER; PTHR11447; CELLULAR TUMOR ANTIGEN P53; 1.
    # We want the family ID, not the subfamily (PTHR11447:SF6)
    pattern = r'^DR\s+PANTHER;\s+(PTHR\d+);\s+.*$'

    for line in uniprot_data.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            family_id = match.group(1)
            # Skip subfamily IDs (those with colons)
            if ':' not in family_id:
                return family_id

    return None


def _fetch_panther_family_data(family_id: str, base_path: Path) -> bool:
    """Fetch PANTHER family data using the InterPro fetcher.

    Args:
        family_id: PANTHER family ID (e.g., "PTHR11447")
        base_path: Base directory where interpro/ folder should be created

    Returns:
        True if successful, False otherwise
    """
    try:
        # Import the InterPro fetcher class directly
        from ai_gene_review.tools.fetch_interpro_family_simple import InterProFamilyFetcherSimple

        # Create fetcher instance with the correct output directory
        fetcher = InterProFamilyFetcherSimple(output_dir=str(base_path))

        # Fetch and save the family data
        fetcher.fetch_and_save("panther", family_id, include_proteins=True)

        print(f"  ✓ Fetched PANTHER family data for {family_id}")
        return True

    except Exception as e:
        print(f"  ⚠ Error fetching PANTHER family {family_id}: {e}")
        return False


def _compare_file_content(file_path: Path, new_content: str) -> bool:
    """Compare file content with new content.

    Args:
        file_path: Path to existing file
        new_content: New content to compare against

    Returns:
        True if contents differ, False if they are the same
    """
    if not file_path.exists():
        return True  # File doesn't exist, so it's different

    try:
        existing_content = file_path.read_text(encoding='utf-8')
        return existing_content != new_content
    except Exception:
        # If we can't read the file, consider it different
        return True


def fetch_gene_data(
    gene_info: Tuple[str, str],
    uniprot_id: Optional[str] = None,
    base_path: Optional[Path] = None,
    seed_annotations: bool = True,
    fetch_titles: bool = True,
    alias: Optional[str] = None,
    force: bool = False,
) -> Dict[str, Any]:
    """Fetch gene data from UniProt and GOA APIs and save to files.

    Creates/updates an ai-review.yaml file with GOA annotations if it doesn't exist
    or is missing annotations.

    Args:
        gene_info: Tuple of (organism, gene_name) e.g. ("human", "CFAP300")
        uniprot_id: Optional UniProt accession ID. If not provided, will attempt to resolve.
        base_path: Base directory for output files. Defaults to current directory.
        seed_annotations: If True, creates/seeds ai-review.yaml with GOA annotations.
        fetch_titles: If True, fetch actual titles from PubMed when seeding (default: True).
        alias: Optional alias to use for directory name and file prefixes instead of gene_name.
        force: If True, overwrite existing UniProt and GOA files. If False, report differences.

    Returns:
        Dictionary with status information:
            - yaml_created: bool - True if ai-review.yaml was created
            - yaml_existed: bool - True if ai-review.yaml already existed
            - annotations_added: int - Number of annotations added
            - references_added: int - Number of references added
            - uniprot_updated: bool - True if UniProt file was updated
            - goa_updated: bool - True if GOA file was updated
            - uniprot_differences: bool - True if UniProt content differs from existing
            - goa_differences: bool - True if GOA content differs from existing
            - panther_family_fetched: bool - True if PANTHER family data was fetched
            - panther_family_id: str or None - PANTHER family ID if found

    Raises:
        ValueError: If UniProt ID cannot be resolved or data cannot be fetched.

    Example:
        >>> import tempfile
        >>> from pathlib import Path
        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     base = Path(tmpdir)
        ...     result = fetch_gene_data(("human", "TP53"), uniprot_id="P04637", base_path=base)  # doctest: +SKIP
        ...     assert (base / "genes" / "human" / "TP53").exists()  # doctest: +SKIP
    """
    organism, gene_name = gene_info
    
    # Use alias for directory name and file prefixes if provided
    dir_name = alias if alias else gene_name
    file_prefix = alias if alias else gene_name

    if base_path is None:
        base_path = Path.cwd()

    # Create directory structure
    gene_dir = base_path / "genes" / organism / dir_name
    gene_dir.mkdir(parents=True, exist_ok=True)

    # Resolve UniProt ID if not provided
    if uniprot_id is None:
        uniprot_id = resolve_gene_to_uniprot(gene_name, organism)

    # Determine file paths
    uniprot_file = gene_dir / f"{file_prefix}-uniprot.txt"
    goa_file = gene_dir / f"{file_prefix}-goa.tsv"

    # Fetch UniProt and GOA data
    uniprot_data = fetch_uniprot_data(uniprot_id)
    goa_data = fetch_goa_data(uniprot_id)

    # Check for differences
    uniprot_differs = _compare_file_content(uniprot_file, uniprot_data)
    goa_differs = _compare_file_content(goa_file, goa_data)

    # Initialize result status
    result: Dict[str, Any] = {
        "yaml_created": False,
        "yaml_existed": False,
        "annotations_added": 0,
        "references_added": 0,
        "uniprot_updated": False,
        "goa_updated": False,
        "uniprot_differences": uniprot_differs,
        "goa_differences": goa_differs,
    }

    # Handle UniProt file
    if uniprot_differs:
        if force or not uniprot_file.exists():
            file_existed = uniprot_file.exists()
            uniprot_file.write_text(uniprot_data)
            result["uniprot_updated"] = True
            if not file_existed:
                print(f"  ✓ Created {file_prefix}-uniprot.txt")
            elif force:
                print(f"  ✓ Updated {file_prefix}-uniprot.txt (forced)")
        else:
            print(f"  ⚠ UniProt data differs from existing {file_prefix}-uniprot.txt (use --force to overwrite)")
    else:
        print(f"  - {file_prefix}-uniprot.txt is up to date")

    # Handle GOA file
    if goa_differs:
        if force or not goa_file.exists():
            file_existed = goa_file.exists()
            goa_file.write_text(goa_data)
            result["goa_updated"] = True
            if not file_existed:
                print(f"  ✓ Created {file_prefix}-goa.tsv")
            elif force:
                print(f"  ✓ Updated {file_prefix}-goa.tsv (forced)")
        else:
            print(f"  ⚠ GOA data differs from existing {file_prefix}-goa.tsv (use --force to overwrite)")
    else:
        print(f"  - {file_prefix}-goa.tsv is up to date")

    # Seed ai-review.yaml with GOA annotations if requested
    if seed_annotations:
        yaml_file = gene_dir / f"{file_prefix}-ai-review.yaml"

        # Import here to avoid circular dependency
        from ai_gene_review.validation.goa_validator import GOAValidator

        # Check if file already exists
        yaml_existed = yaml_file.exists()
        result["yaml_existed"] = yaml_existed

        # Get taxon ID and proper label from organism
        organism_to_taxon = {
            "human": ("NCBITaxon:9606", "Homo sapiens"),
            "mouse": ("NCBITaxon:10090", "Mus musculus"),
            "rat": ("NCBITaxon:10116", "Rattus norvegicus"),
            "yeast": ("NCBITaxon:559292", "Saccharomyces cerevisiae"),
            "fly": ("NCBITaxon:7227", "Drosophila melanogaster"),
            "worm": ("NCBITaxon:6239", "Caenorhabditis elegans"),
            "zebrafish": ("NCBITaxon:7955", "Danio rerio"),
        }

        # Check if we have a predefined mapping
        if organism.lower() in organism_to_taxon:
            taxon_info = organism_to_taxon[organism.lower()]
        # Check if it's a UniProt organism code
        elif organism.isupper() and len(organism) <= 5:
            taxon_id = resolve_organism_code_to_taxon(organism)
            if taxon_id:
                # Get organism name from UniProt data if available
                organism_name = get_organism_name_from_uniprot(uniprot_id) or organism
                taxon_info = (f"NCBITaxon:{taxon_id}", organism_name)
            else:
                # Default fallback
                taxon_info = (f"NCBITaxon:{organism}", organism.capitalize())
        else:
            # Default for unknown organisms
            taxon_info = (f"NCBITaxon:{organism}", organism.capitalize())
        taxon_id, taxon_label = taxon_info

        # Create minimal YAML structure if file doesn't exist
        if not yaml_existed:
            yaml_data = {
                "id": uniprot_id,
                "gene_symbol": gene_name,
                "product_type": "PROTEIN",
                "status": "INITIALIZED",
                "taxon": {"id": taxon_id, "label": taxon_label},
                "description": f"TODO: Add description for {gene_name}",
            }

            # Write initial YAML
            with open(yaml_file, "w") as f:
                yaml.dump(
                    yaml_data,
                    f,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                )
            result["yaml_created"] = True

        # Now seed missing GOA annotations
        validator = GOAValidator()
        added_count, _, refs_added = validator.seed_missing_annotations(
            yaml_file, goa_file, fetch_titles=fetch_titles
        )
        result["annotations_added"] = added_count
        result["references_added"] = refs_added

        if added_count > 0:
            print(
                f"  ✓ Seeded {added_count} GOA annotations in {file_prefix}-ai-review.yaml"
            )
        else:
            if yaml_existed:
                print(
                    f"  - {file_prefix}-ai-review.yaml already contains all GOA annotations"
                )

    # Auto-fetch PANTHER family data if found in UniProt data
    panther_family_id = _extract_panther_family_id(uniprot_data)
    if panther_family_id:
        # Check if PANTHER family data already exists
        panther_family_dir = base_path / "interpro" / "panther" / panther_family_id
        panther_metadata_file = panther_family_dir / f"{panther_family_id}-metadata.yaml"
        panther_entries_file = panther_family_dir / f"{panther_family_id}-entries.csv"

        if not (panther_metadata_file.exists() and panther_entries_file.exists()):
            print(f"  🔍 Found PANTHER family {panther_family_id}, fetching family data...")
            family_fetch_success = _fetch_panther_family_data(panther_family_id, base_path)
            result["panther_family_fetched"] = family_fetch_success
            result["panther_family_id"] = panther_family_id
        else:
            print(f"  - PANTHER family {panther_family_id} data already exists")
            result["panther_family_fetched"] = False
            result["panther_family_id"] = panther_family_id
    else:
        print("  - No PANTHER family found in UniProt data")
        result["panther_family_fetched"] = False
        result["panther_family_id"] = None

    return result


def expand_organism_name(organism: str) -> str:
    """Expand organism code or common name to full scientific name.

    Args:
        organism: Organism code (e.g., "PSEPK"), common name (e.g., "human"),
                  or taxon ID

    Returns:
        Full scientific name of the organism, or original value if not found

    Examples:
        >>> expand_organism_name("human")
        'Homo sapiens'
        >>> expand_organism_name("PSEPK")  # doctest: +SKIP
        'Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)'
        >>> expand_organism_name("Homo sapiens")
        'Homo sapiens'
    """
    # Common name mappings
    common_to_scientific = {
        "human": "Homo sapiens",
        "mouse": "Mus musculus",
        "rat": "Rattus norvegicus",
        "yeast": "Saccharomyces cerevisiae",
        "fly": "Drosophila melanogaster",
        "worm": "Caenorhabditis elegans",
        "zebrafish": "Danio rerio",
        "chicken": "Gallus gallus",
        "pig": "Sus scrofa",
        "dog": "Canis lupus familiaris",
        "cow": "Bos taurus",
        "ecoli": "Escherichia coli",
        "e.coli": "Escherichia coli",
        "e coli": "Escherichia coli",
    }

    # Check common names first
    if organism.lower() in common_to_scientific:
        return common_to_scientific[organism.lower()]

    # Check if it's a UniProt organism code (uppercase, <= 5 chars)
    if organism.isupper() and len(organism) <= 5:
        try:
            # Query UniProt taxonomy API
            url = "https://rest.uniprot.org/taxonomy/stream"
            params = {"query": f"mnemonic:{organism}", "format": "json", "size": "1"}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            results = response.json().get("results", [])
            if results:
                return results[0].get("scientificName", organism)
        except Exception:
            pass

    # Check if it's a taxon ID (all digits)
    if organism.isdigit():
        try:
            # Query UniProt taxonomy API with taxon ID
            url = "https://rest.uniprot.org/taxonomy/stream"
            params = {"query": f"id:{organism}", "format": "json", "size": "1"}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            results = response.json().get("results", [])
            if results:
                return results[0].get("scientificName", organism)
        except Exception:
            pass

    # Return original if already looks like scientific name or can't expand
    return organism


def get_organism_name_from_uniprot(uniprot_id: str) -> Optional[str]:
    """Get the organism scientific name from a UniProt ID.

    Args:
        uniprot_id: UniProt accession ID

    Returns:
        Scientific name of the organism, or None if not found
    """
    try:
        url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}?format=json&fields=organism_name"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data.get("organism", {}).get("scientificName")
    except Exception:
        return None


def resolve_organism_code_to_taxon(organism_code: str) -> Optional[str]:
    """Resolve a UniProt organism code to an NCBI taxonomy ID.

    Args:
        organism_code: UniProt organism code (e.g., "PSEPK", "ECOLI")

    Returns:
        NCBI taxonomy ID as string, or None if not found

    Example:
        >>> taxon_id = resolve_organism_code_to_taxon("ECOLI")
        >>> taxon_id  # doctest: +SKIP
        '511145'
    """
    try:
        # Query UniProt taxonomy API with the mnemonic
        url = "https://rest.uniprot.org/taxonomy/stream"
        params = {"query": f"mnemonic:{organism_code}", "format": "json", "size": "1"}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        results = response.json().get("results", [])
        if results:
            return str(results[0].get("taxonId"))

    except Exception:
        # Silently fail and return None
        pass

    return None


def swissprot_by_gene_taxon(
    gene_symbol: str, organism: str, limit: int = 10
) -> List[Dict[str, str]]:
    """Look up reviewed (Swiss-Prot) UniProtKB entries by gene symbol and organism.

    Wrapper for backwards compatibility.

    Args:
        gene_symbol: Gene symbol to search for
        organism: Organism name (e.g., "human", "mouse", "yeast") or NCBI taxon ID
        limit: Maximum number of results to return

    Returns:
        List of dictionaries with UniProt entry information

    Raises:
        ValueError: If API request fails
    """
    return uniprot_by_gene_taxon(gene_symbol, organism, limit, reviewed_only=True)


def uniprot_by_gene_taxon(
    gene_symbol: str, organism: str, limit: int = 10, reviewed_only: bool = True
) -> List[Dict[str, str]]:
    """Look up UniProtKB entries by gene symbol and organism.

    Args:
        gene_symbol: Gene symbol to search for
        organism: Organism name (e.g., "human", "mouse"), UniProt organism code (e.g., "PSEPK"), or NCBI taxon ID
        limit: Maximum number of results to return
        reviewed_only: If True, only return Swiss-Prot (reviewed) entries. If False, include TrEMBL.

    Returns:
        List of dictionaries with UniProt entry information

    Raises:
        ValueError: If API request fails
    """
    # Map common organism names to NCBI taxonomy IDs
    organism_to_taxon = {
        "human": "9606",
        "mouse": "10090",
        "rat": "10116",
        "yeast": "559292",
        "fly": "7227",
        "worm": "6239",
        "zebrafish": "7955",
        "chicken": "9031",
        "pig": "9823",
        "dog": "9615",
        "cow": "9913",
    }

    # Determine if we have a taxon ID or need to look it up
    taxon = organism_to_taxon.get(organism.lower(), organism)

    # Check if it's already a taxon ID (all digits)
    if taxon.isdigit():
        org_field = f"organism_id:{taxon}"
    # Check if it's a UniProt organism code (uppercase letters possibly with digits)
    elif organism.isupper() and len(organism) <= 5:
        # Look up taxon ID from organism code
        taxon_id = resolve_organism_code_to_taxon(organism)
        if taxon_id:
            org_field = f"organism_id:{taxon_id}"
        else:
            # Fall back to organism name search
            org_field = f'organism_name:"{organism}"'
    else:
        # Try as organism name
        org_field = f'organism_name:"{organism}"'

    # Build query
    reviewed_filter = " AND (reviewed:true)" if reviewed_only else ""
    query = f"(gene_exact:{gene_symbol}) AND ({org_field}){reviewed_filter}"

    # API parameters
    params = {
        "query": query,
        "format": "json",
        "fields": "accession,id,gene_primary,organism_name,reviewed",
        "size": str(limit),
        "compressed": "false",
        "download": "true",
    }

    # Make request
    url = "https://rest.uniprot.org/uniprotkb/stream"
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    # Parse results
    hits = []
    for rec in response.json().get("results", []):
        hits.append(
            {
                "accession": rec["primaryAccession"],
                "entry_name": rec.get("uniProtkbId", ""),
                "gene": next(
                    (
                        g.get("geneName", {}).get("value")
                        for g in rec.get("genes", [])
                        if g.get("geneName")
                    ),
                    None,
                ),
                "organism": rec.get("organism", {}).get("scientificName"),
            }
        )

    return hits


def resolve_gene_to_uniprot(gene_name: str, organism: str) -> str:
    """Resolve a gene name to a UniProt accession ID.

    For human genes, only Swiss-Prot (reviewed) entries are accepted.
    For other organisms, falls back to TrEMBL if no Swiss-Prot entry is found.

    Special case: If gene_name looks like a UniProt accession (6+ alphanumeric chars
    starting with letter), verify it exists directly rather than treating as gene name.

    Args:
        gene_name: Name of the gene or UniProt accession
        organism: Organism name (e.g., "human", "mouse", "yeast")

    Returns:
        UniProt accession ID (Swiss-Prot preferred, TrEMBL as fallback)

    Raises:
        ValueError: If gene cannot be resolved to UniProt ID
    """
    # Check if gene_name looks like a UniProt accession
    # UniProt accessions: 6+ chars, start with letter, alphanumeric + optional underscore/dash
    import re
    if re.match(r'^[A-Z][A-Z0-9_-]{5,}$', gene_name.upper()):
        # Looks like an accession, try to validate it exists
        try:
            # Try to fetch the UniProt data to verify it exists
            # This will also work for TrEMBL entries
            fetch_uniprot_data(gene_name)
            return gene_name
        except ValueError:
            # If fetch fails, fall through to treat as gene name
            pass

    # First try Swiss-Prot entries
    hits = uniprot_by_gene_taxon(gene_name, organism, limit=1, reviewed_only=True)

    if hits:
        return hits[0]["accession"]

    # For human, Swiss-Prot is required - no fallback to TrEMBL
    if organism.lower() == "human":
        raise ValueError(
            f"Could not find Swiss-Prot UniProt ID for gene {gene_name} in {organism}. "
            "All human genes should have Swiss-Prot entries."
        )

    # For other organisms, try TrEMBL as fallback
    hits = uniprot_by_gene_taxon(gene_name, organism, limit=1, reviewed_only=False)

    if not hits:
        raise ValueError(
            f"Could not find any UniProt ID (Swiss-Prot or TrEMBL) for gene {gene_name} in {organism}"
        )

    # Return the first hit (could be Swiss-Prot or TrEMBL)
    return hits[0]["accession"]


def fetch_uniprot_data(uniprot_id: str) -> str:
    """Fetch UniProt data in text format.

    Args:
        uniprot_id: UniProt accession ID (e.g., "Q9BRQ4")

    Returns:
        UniProt entry in text format

    Raises:
        ValueError: If UniProt data cannot be fetched
    """
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.txt"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(
            f"Failed to fetch UniProt data for {uniprot_id}: HTTP {response.status_code}"
        )

    return response.text


def fetch_goa_data(uniprot_id: str) -> str:
    """Fetch Gene Ontology Annotation (GOA) data from QuickGO API.

    Fetches ALL annotations using pagination if necessary.

    Args:
        uniprot_id: UniProt accession ID

    Returns:
        GOA data in TSV format

    Raises:
        ValueError: If GOA data cannot be fetched
    """
    # Use QuickGO search endpoint with JSON format
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

    all_results = []
    page = 1
    limit = 200  # QuickGO's actual max limit per page (not 400!)

    while True:
        # Build URL with properly formatted parameters
        # QuickGO expects multiple includeFields parameters, not an array
        params = [
            ("geneProductId", uniprot_id),
            ("includeFields", "goName"),
            ("includeFields", "taxonName"),
            ("includeFields", "name"),
            ("limit", str(limit)),
        ]

        # Only add page parameter if page > 1 (API doesn't like page=1)
        if page > 1:
            params.append(("page", str(page)))

        # Request JSON format
        headers = {"Accept": "application/json"}

        try:
            response = requests.get(url, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Parse JSON response
            data = response.json()
            results = data.get("results", [])

            if not results:
                # No more results, stop pagination
                break

            all_results.extend(results)

            # Check if we've fetched all results
            # Note: pageInfo.total is unreliable, use numberOfHits instead
            total_annotations = data.get("numberOfHits", 0)

            # Debug output
            print(f"  Page {page}: fetched {len(results)} annotations (total so far: {len(all_results)})")

            # Stop if:
            # 1. We got fewer results than requested (last page)
            # 2. We have fetched all known annotations
            if len(results) < limit or len(all_results) >= total_annotations:
                # We have all results
                print(f"  Total annotations fetched: {len(all_results)} out of {total_annotations}")
                break

            page += 1

        except requests.exceptions.RequestException as e:
            if page == 1:
                # First page failed, return empty result
                return "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\tGENE NAME\tDATE\n"
            else:
                # Subsequent page failed, use what we have
                print(f"Warning: Pagination stopped at page {page} due to error: {e}")
                break

    # Process all collected results
    results = all_results

    if not results:
        # Return header only if no data
        return "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\tGENE NAME\tDATE\n"

    # Sort results: IBA first, then by most recent date (descending), then by GO ID
    sorted_results = sorted(
        results,
        key=lambda x: (
            0 if x.get("goEvidence", "") == "IBA" else 1,  # IBA annotations first
            -(
                int(x.get("date", "0")) if x.get("date", "").isdigit() else 0
            ),  # Negative for descending date
            x.get("goId", ""),  # Then by GO ID
        ),
    )

    # Convert JSON to TSV format
    tsv_lines = [
        "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\tGENE NAME\tDATE"
    ]

    for result in sorted_results:
        # Extract database and ID from geneProductId
        gene_product_id = result.get("geneProductId", "")
        if ":" in gene_product_id:
            db, prod_id = gene_product_id.split(":", 1)
        else:
            db, prod_id = "", gene_product_id

        # Extract WITH/FROM information
        with_from_list = []
        with_from_data = result.get("withFrom")
        if with_from_data:
            for wf in with_from_data:
                for xref in wf.get("connectedXrefs", []):
                    with_from_list.append(
                        f"{xref.get('db', '')}:{xref.get('id', '')}"
                    )
        with_from = "|".join(with_from_list) if with_from_list else ""

        # Build TSV row
        row = [
            db,  # GENE PRODUCT DB
            prod_id,  # GENE PRODUCT ID
            result.get("symbol", ""),  # SYMBOL
            result.get("qualifier", ""),  # QUALIFIER
            result.get("goId", ""),  # GO TERM
            result.get("goName", ""),  # GO NAME
            result.get("goAspect", ""),  # GO ASPECT
            result.get("evidenceCode", ""),  # ECO ID
            result.get("goEvidence", ""),  # GO EVIDENCE CODE
            result.get("reference", ""),  # REFERENCE
            with_from,  # WITH/FROM
            str(result.get("taxonId", "")),  # TAXON ID
            result.get("taxonName", ""),  # TAXON NAME
            result.get("assignedBy", ""),  # ASSIGNED BY
            result.get("name", ""),  # GENE NAME
            result.get("date", ""),  # DATE
        ]

        tsv_lines.append("\t".join(row))

    return "\n".join(tsv_lines) + "\n"


def fetch_rnacentral_data_by_id(rnacentral_id: str) -> str:
    """Fetch RNAcentral data directly by RNAcentral ID.

    This is more reliable than searching by gene name when you already have the ID.
    Also fetches publications for the RNA and removes the sequence field (which can be huge).

    Args:
        rnacentral_id: RNAcentral ID (e.g., "URS0000759CF4_9606" or "URS0000759CF4")

    Returns:
        RNAcentral data in JSON format as text (without sequence, with publications)

    Raises:
        ValueError: If RNAcentral data cannot be fetched

    Example:
        >>> data = fetch_rnacentral_data_by_id("URS0000759CF4_9606")  # doctest: +SKIP
        >>> assert "rnacentral_id" in data  # doctest: +SKIP
    """
    import json

    # Clean up ID - remove species suffix if present for the API call
    clean_id = rnacentral_id.split("_")[0] if "_" in rnacentral_id else rnacentral_id

    url = f"https://rnacentral.org/api/v1/rna/{clean_id}"
    headers = {
        "Accept": "application/json",
        "User-Agent": "ai-gene-review/1.0"
    }

    try:
        # Fetch basic RNA data
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        rna_data = response.json()

        # Remove sequence field (can be huge for long ncRNAs)
        if "sequence" in rna_data:
            del rna_data["sequence"]

        # Fetch publications for this RNA
        publications_url = f"https://rnacentral.org/api/v1/rna/{clean_id}/publications"
        publications_data = []
        try:
            pub_response = requests.get(publications_url, headers=headers, timeout=30)
            pub_response.raise_for_status()
            pub_json = pub_response.json()

            # Collect all publications (handle pagination)
            publications_data = pub_json.get("results", [])
            next_url = pub_json.get("next")

            while next_url:
                pub_response = requests.get(next_url, headers=headers, timeout=30)
                pub_response.raise_for_status()
                pub_json = pub_response.json()
                publications_data.extend(pub_json.get("results", []))
                next_url = pub_json.get("next")

        except requests.exceptions.RequestException:
            # If publications fetch fails, continue without them
            pass

        # Add publications to the RNA data
        rna_data["publications"] = publications_data

        # Wrap single result in the same format as search results for consistency
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [rna_data]
        }

        return json.dumps(data, indent=2, ensure_ascii=False)

    except requests.exceptions.Timeout as e:
        raise ValueError(f"RNAcentral API request timed out after 30 seconds for ID {rnacentral_id}: {e}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch RNAcentral data for ID {rnacentral_id}: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse RNAcentral JSON response: {e}")


def resolve_gene_to_rnacentral_via_hgnc(gene_symbol: str) -> Optional[str]:
    """Resolve a human gene symbol to an RNAcentral ID using HGNC API.

    This is the most reliable method for human genes as HGNC maintains
    authoritative cross-references to RNAcentral.

    Args:
        gene_symbol: Human gene symbol (e.g., "KCNQ1OT1", "XIST")

    Returns:
        RNAcentral ID without species suffix (e.g., "URS0000759CF4") or None if not found

    Raises:
        ValueError: If HGNC API request fails

    Example:
        >>> rna_id = resolve_gene_to_rnacentral_via_hgnc("KCNQ1OT1")  # doctest: +SKIP
        >>> print(rna_id)  # doctest: +SKIP
        URS0000759CF4
    """
    try:
        url = f"https://rest.genenames.org/fetch/symbol/{gene_symbol}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        docs = data.get("response", {}).get("docs", [])

        if not docs:
            return None

        # Get the first RNAcentral ID from the cross-references
        rna_central_ids = docs[0].get("rna_central_id", [])
        if rna_central_ids:
            return rna_central_ids[0]

        return None

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to query HGNC API for gene {gene_symbol}: {e}")


def fetch_rnacentral_data(gene_symbol: str, organism: str) -> str:
    """Fetch ncRNA data from RNAcentral API.

    Args:
        gene_symbol: Gene symbol to search for
        organism: Organism name (e.g., "human", "mouse") or NCBI taxon ID

    Returns:
        RNAcentral data in JSON format as text

    Raises:
        ValueError: If RNAcentral data cannot be fetched

    Example:
        >>> data = fetch_rnacentral_data("SNORD3A", "human")  # doctest: +SKIP
        >>> assert "rnacentral_id" in data  # doctest: +SKIP
    """
    # Map common organism names to NCBI taxonomy IDs
    organism_to_taxon = {
        "human": "9606",
        "mouse": "10090",
        "rat": "10116",
        "yeast": "559292",
        "fly": "7227",
        "worm": "6239",
        "zebrafish": "7955",
        "chicken": "9031",
        "pig": "9823",
        "dog": "9615",
        "cow": "9913",
    }

    # Get taxon ID
    taxon_id = organism_to_taxon.get(organism.lower(), organism)
    if not taxon_id.isdigit():
        # Try to resolve organism code to taxon ID
        resolved_taxon = resolve_organism_code_to_taxon(organism)
        if resolved_taxon:
            taxon_id = resolved_taxon
        else:
            raise ValueError(f"Could not resolve organism '{organism}' to NCBI taxon ID")

    # Search RNAcentral API for the gene symbol
    # Use text search endpoint first to find matching entries
    search_url = "https://rnacentral.org/api/v1/rna"

    # Build query parameters - try different approaches
    params = {
        "description": gene_symbol,
        "format": "json",
        "page_size": 100  # Get up to 100 results
    }

    headers = {
        "Accept": "application/json",
        "User-Agent": "ai-gene-review/1.0"
    }

    try:
        response = requests.get(search_url, params=params, headers=headers, timeout=30)  # type: ignore[arg-type]
        response.raise_for_status()

        data = response.json()

        # If no results found, try alternative search strategies
        if not data.get("results"):
            # Try searching with a broader query using sequence or any field
            alt_params = {
                "length_gte": "20",  # At least 20 nucleotides
                "length_lte": "5000",  # Maximum reasonable RNA length
                "format": "json",
                "page_size": 20  # Smaller page size for broader search
            }

            # Add description filter if gene symbol is provided
            if gene_symbol:
                alt_params["description"] = f"*{gene_symbol}*"

            alt_response = requests.get(search_url, params=alt_params, headers=headers, timeout=30)  # type: ignore[arg-type]
            alt_response.raise_for_status()
            alt_data = alt_response.json()

            # For now, just return the alternative results even if no species filtering
            if alt_data.get("results"):
                data = alt_data

        # Return the JSON data as formatted text
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)

    except requests.exceptions.Timeout as e:
        raise ValueError(f"RNAcentral API request timed out after 30 seconds for gene {gene_symbol}: {e}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch RNAcentral data for gene {gene_symbol} in {organism}: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse RNAcentral JSON response: {e}")


def resolve_gene_to_rnacentral(gene_symbol: str, organism: str) -> Optional[str]:
    """Resolve a gene symbol to an RNAcentral ID.

    For human genes, uses HGNC API for reliable cross-reference mapping.
    For other organisms, attempts to use RNAcentral API directly.

    Args:
        gene_symbol: Gene symbol to search for
        organism: Organism name or NCBI taxon ID

    Returns:
        RNAcentral ID (e.g., "URS0000000001_9606") or None if not found

    Raises:
        ValueError: If gene cannot be resolved to RNAcentral ID

    Example:
        >>> rna_id = resolve_gene_to_rnacentral("KCNQ1OT1", "human")  # doctest: +SKIP
        >>> print(rna_id)  # doctest: +SKIP
        URS0000759CF4_9606
    """
    # Map organism names to taxon IDs
    organism_to_taxon = {
        "human": "9606",
        "mouse": "10090",
        "rat": "10116",
        "yeast": "559292",
        "fly": "7227",
        "worm": "6239",
        "zebrafish": "7955",
    }

    # Get taxon ID
    taxon_id = organism_to_taxon.get(organism.lower(), organism)

    # For human genes, use HGNC API (most reliable)
    if organism.lower() == "human":
        rna_id = resolve_gene_to_rnacentral_via_hgnc(gene_symbol)
        if rna_id:
            # Add species suffix if not present
            if "_" not in rna_id:
                return f"{rna_id}_{taxon_id}"
            return rna_id
        else:
            raise ValueError(
                f"Could not find RNAcentral ID for human gene {gene_symbol} in HGNC. "
                "The gene may not be an ncRNA or may not have RNAcentral cross-references."
            )

    # For non-human organisms, try RNAcentral API
    # (Note: This approach is less reliable and may need improvement for specific organisms)
    try:
        data_text = fetch_rnacentral_data(gene_symbol, organism)
        import json
        data = json.loads(data_text)

        results = data.get("results", [])
        if results:
            # Return the first result's RNAcentral ID
            first_result = results[0]
            rna_id = first_result.get("rnacentral_id")
            # Add species suffix if not present
            if rna_id and "_" not in rna_id:
                if taxon_id.isdigit():
                    rna_id = f"{rna_id}_{taxon_id}"
            return rna_id

        raise ValueError(
            f"Could not find RNAcentral ID for gene {gene_symbol} in {organism}. "
            "No matching entries found in RNAcentral database."
        )
    except ValueError:
        # Re-raise ValueError with context
        raise


def fetch_gene_data_ncRNA(
    gene_info: Tuple[str, str],
    rnacentral_id: Optional[str] = None,
    base_path: Optional[Path] = None,
    seed_annotations: bool = True,
    alias: Optional[str] = None,
    force: bool = False,
) -> Dict[str, Any]:
    """Fetch ncRNA gene data from RNAcentral API and save to files.

    This is the ncRNA equivalent of fetch_gene_data() for protein-coding genes.

    Args:
        gene_info: Tuple of (organism, gene_name) e.g. ("human", "SNORD3A")
        rnacentral_id: Optional RNAcentral ID. If not provided, will attempt to resolve.
        base_path: Base directory for output files. Defaults to current directory.
        seed_annotations: If True, creates/seeds ai-review.yaml with basic structure.
        alias: Optional alias to use for directory name and file prefixes.
        force: If True, overwrite existing files. If False, report differences.

    Returns:
        Dictionary with status information similar to fetch_gene_data()

    Example:
        >>> result = fetch_gene_data_ncRNA(("human", "SNORD3A"))  # doctest: +SKIP
        >>> print(result["rnacentral_updated"])  # doctest: +SKIP
        True
    """
    organism, gene_name = gene_info

    # Use alias for directory name and file prefixes if provided
    dir_name = alias if alias else gene_name
    file_prefix = alias if alias else gene_name

    if base_path is None:
        base_path = Path.cwd()

    # Create directory structure
    gene_dir = base_path / "genes" / organism / dir_name
    gene_dir.mkdir(parents=True, exist_ok=True)

    # Resolve RNAcentral ID if not provided
    if rnacentral_id is None:
        rnacentral_id = resolve_gene_to_rnacentral(gene_name, organism)
        if rnacentral_id is None:
            raise ValueError(f"Could not resolve gene {gene_name} to RNAcentral ID in {organism}")

    # Determine file paths
    rnacentral_file = gene_dir / f"{file_prefix}-rnacentral.json"
    goa_file = gene_dir / f"{file_prefix}-goa.tsv"

    # Fetch RNAcentral data
    # If we have the RNAcentral ID, fetch directly by ID (more reliable)
    # Otherwise fall back to searching by gene name
    if rnacentral_id:
        rnacentral_data = fetch_rnacentral_data_by_id(rnacentral_id)
    else:
        rnacentral_data = fetch_rnacentral_data(gene_name, organism)

    # Download publications from RNAcentral to publications folder
    import json
    try:
        rnacentral_json = json.loads(rnacentral_data)
        results = rnacentral_json.get("results", [])
        if results and "publications" in results[0]:
            publications = results[0]["publications"]
            pmids_to_fetch = []

            for pub in publications:
                pmid = pub.get("pubmed_id")
                if pmid:
                    pmids_to_fetch.append(pmid)

            if pmids_to_fetch:
                print(f"  Fetching {len(pmids_to_fetch)} publications from RNAcentral...")

                # Import publication fetcher
                from ai_gene_review.etl.publication import cache_publications

                # Create publications directory
                pubs_dir = base_path / "publications"
                pubs_dir.mkdir(exist_ok=True)

                # Fetch publications (prefix with PMID: if needed)
                pmid_ids = [f"PMID:{pmid}" if not pmid.startswith("PMID:") else pmid for pmid in pmids_to_fetch]
                fetched_count = cache_publications(pmid_ids, pubs_dir, force=False, delay=0.5)

                if fetched_count > 0:
                    print(f"  ✓ Downloaded {fetched_count} publications to publications/")
    except (json.JSONDecodeError, Exception):
        # Continue if publication download fails
        pass

    # Fetch GOA data using the RNAcentral ID
    # QuickGO API accepts RNAcentral IDs just like UniProt IDs
    goa_data = fetch_goa_data(rnacentral_id)

    # Check for differences
    rnacentral_differs = _compare_file_content(rnacentral_file, rnacentral_data)
    goa_differs = _compare_file_content(goa_file, goa_data)

    # Initialize result status
    result = {
        "yaml_created": False,
        "yaml_existed": False,
        "annotations_added": 0,
        "references_added": 0,
        "rnacentral_updated": False,
        "goa_updated": False,
        "rnacentral_differences": rnacentral_differs,
        "goa_differences": goa_differs,
    }

    # Handle RNAcentral file
    if rnacentral_differs:
        if force or not rnacentral_file.exists():
            file_existed = rnacentral_file.exists()
            rnacentral_file.write_text(rnacentral_data, encoding='utf-8')
            result["rnacentral_updated"] = True
            if not file_existed:
                print(f"  ✓ Created {file_prefix}-rnacentral.json")
            elif force:
                print(f"  ✓ Updated {file_prefix}-rnacentral.json (forced)")
        else:
            print(f"  ⚠ RNAcentral data differs from existing {file_prefix}-rnacentral.json (use --force to overwrite)")
    else:
        print(f"  - {file_prefix}-rnacentral.json is up to date")

    # Handle GOA file
    if goa_differs:
        if force or not goa_file.exists():
            file_existed = goa_file.exists()
            goa_file.write_text(goa_data)
            result["goa_updated"] = True
            if not file_existed:
                print(f"  ✓ Created {file_prefix}-goa.tsv")
            elif force:
                print(f"  ✓ Updated {file_prefix}-goa.tsv (forced)")
        else:
            print(f"  ⚠ GOA data differs from existing {file_prefix}-goa.tsv (use --force to overwrite)")
    else:
        print(f"  - {file_prefix}-goa.tsv is up to date")

    # Seed ai-review.yaml with basic ncRNA structure if requested
    if seed_annotations:
        yaml_file = gene_dir / f"{file_prefix}-ai-review.yaml"

        # Check if file already exists
        yaml_existed = yaml_file.exists()
        result["yaml_existed"] = yaml_existed

        # Get taxon information
        organism_to_taxon = {
            "human": ("NCBITaxon:9606", "Homo sapiens"),
            "mouse": ("NCBITaxon:10090", "Mus musculus"),
            "rat": ("NCBITaxon:10116", "Rattus norvegicus"),
            "yeast": ("NCBITaxon:559292", "Saccharomyces cerevisiae"),
            "fly": ("NCBITaxon:7227", "Drosophila melanogaster"),
            "worm": ("NCBITaxon:6239", "Caenorhabditis elegans"),
            "zebrafish": ("NCBITaxon:7955", "Danio rerio"),
        }

        if organism.lower() in organism_to_taxon:
            taxon_info = organism_to_taxon[organism.lower()]
        else:
            # Try to resolve organism code to taxon
            taxon_id = resolve_organism_code_to_taxon(organism)
            if taxon_id:
                organism_name = organism  # Use organism code as name for now
                taxon_info = (f"NCBITaxon:{taxon_id}", organism_name)
            else:
                taxon_info = (f"NCBITaxon:{organism}", organism.capitalize())

        taxon_id, taxon_label = taxon_info

        # Create minimal YAML structure for ncRNA if file doesn't exist
        if not yaml_existed:
            yaml_data = {
                "id": rnacentral_id,
                "gene_symbol": gene_name,
                "product_type": "OTHER_NCRNA",  # Default, should be updated based on RNA type
                "status": "INITIALIZED",
                "taxon": {"id": taxon_id, "label": taxon_label},
                "description": f"TODO: Add description for {gene_name}",
                "references": [],
                "existing_annotations": [],
                "core_functions": [],
            }

            # Write initial YAML
            with open(yaml_file, "w") as f:
                yaml.dump(
                    yaml_data,
                    f,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                )
            result["yaml_created"] = True

        # Now seed missing GOA annotations (same as for protein-coding genes)
        from ai_gene_review.validation.goa_validator import GOAValidator
        validator = GOAValidator()
        added_count, _, refs_added = validator.seed_missing_annotations(
            yaml_file, goa_file, fetch_titles=True
        )
        result["annotations_added"] = added_count
        result["references_added"] = refs_added

        if added_count > 0:
            print(
                f"  ✓ Seeded {added_count} GOA annotations in {file_prefix}-ai-review.yaml"
            )
        else:
            if yaml_existed:
                print(
                    f"  - {file_prefix}-ai-review.yaml already contains all GOA annotations"
                )

    return result
