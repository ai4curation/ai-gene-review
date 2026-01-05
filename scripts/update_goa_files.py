#!/usr/bin/env python3
"""Update only the GOA files for genes that need re-fetching"""
from pathlib import Path
from src.ai_gene_review.etl.gene import fetch_goa_data

genes_to_update = [
    ("human", "BRCA1", "P38398"),
    ("human", "PTEN", "P60484"),
    ("human", "TRAF6", "Q9Y4K3"),
    ("human", "CFTR", "P13569"),
    ("human", "MYC", "P01106"),
    ("human", "GATA3", "P23771"),
    ("human", "TP53", "P04637"),
    ("human", "EGFR", "P00533"),
    ("human", "JAK1", "P23458"),
    ("mouse", "Syk", "P48025"),
    ("mouse", "Ctnnb1", "Q02248"),
]

for species, gene, uniprot_id in genes_to_update:
    print(f"\nUpdating {species}/{gene} ({uniprot_id})...")

    # Fetch GOA data
    goa_data = fetch_goa_data(uniprot_id)

    if goa_data:
        # Write to file
        goa_path = Path(f"genes/{species}/{gene}/{gene}-goa.tsv")
        goa_path.parent.mkdir(parents=True, exist_ok=True)
        goa_path.write_text(goa_data)

        lines = goa_data.strip().split('\n')
        print(f"  ✓ Updated {gene}-goa.tsv with {len(lines)-1} annotations")
    else:
        print(f"  ✗ Failed to fetch GOA data")