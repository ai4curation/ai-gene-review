#!/usr/bin/env python3
from src.ai_gene_review.etl.gene import fetch_goa_data

# Test with some key genes
test_genes = [
    ("P38398", "BRCA1"),
    ("P60484", "PTEN"),
    ("Q9Y4K3", "TRAF6"),
    ("P13569", "CFTR"),
    ("P01106", "MYC"),
    ("P23771", "GATA3"),
    ("P04637", "TP53"),
]

for uniprot_id, name in test_genes:
    print(f"\n=== {name} ({uniprot_id}) ===")
    try:
        data = fetch_goa_data(uniprot_id)
        if data:
            lines = data.strip().split('\n')
            print(f"  Total lines (including header): {len(lines)}")
            print(f"  Total annotations: {len(lines) - 1}")
        else:
            print("  No data returned")
    except Exception as e:
        print(f"  Error: {e}")