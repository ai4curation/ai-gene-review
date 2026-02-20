#!/usr/bin/env python3
"""
Fill column A (Suggested action) with reannotation recommendations from gene review YAML files.
Reads TSV, looks up genes in genes/*/*.yaml, extracts actions, and writes results back.
"""

import csv
import yaml
from pathlib import Path
from typing import Dict, Optional, Tuple

# Mapping from common names/IDs to gene symbols and organisms
GENE_MAPPING = {
    # Human
    'HSPA1A': ('human', 'HSPA1A'),
    'HSPA1B': ('human', 'HSPA1B'),
    'HSPA2': ('human', 'HSPA2'),
    'HSPA6': ('human', 'HSPA6'),
    'HSPA8': ('human', 'HSPA8'),
    'HSPA1L': ('human', 'HSPA1L'),
    'DNAJB1': ('human', 'DNAJB1'),
    'DNAJB2': ('human', 'DNAJB2'),
    'DNAJA2': ('human', 'DNAJA2'),
    'DNAJA4': ('human', 'DNAJA4'),
    'DNAJB6': ('human', 'DNAJB6'),
    'DNAJB8': ('human', 'DNAJB8'),
    'CRYAA': ('human', 'CRYAA'),
    'CRYAB': ('human', 'CRYAB'),
    'HSPB6': ('human', 'HSPB6'),
    'PFDN1': ('human', 'PFDN1'),
    'PFDN2': ('human', 'PFDN2'),
    'PFDN4': ('human', 'PFDN4'),
    'PFDN5': ('human', 'PFDN5'),
    'PFDN6': ('human', 'PFDN6'),
    'VBP1': ('human', 'VBP1'),
    'UGGT1': ('human', 'UGGT1'),
    'ERLEC1': ('human', 'ERLEC1'),
    'SYVN1': ('human', 'SYVN1'),
    'NPM1': ('human', 'NPM1'),
    'CLU': ('human', 'CLU'),
    'SCG5': ('human', 'SCG5'),
    'TOMM20': ('human', 'TOMM20'),
    'GRPEL1': ('human', 'GRPEL1'),
    'AIP': ('human', 'AIP'),
    'AHSA1': ('human', 'AHSA1'),
    'PTGES3': ('human', 'PTGES3'),
    'TMEM67': ('human', 'TMEM67'),
    'CALR': ('human', 'CALR'),
    # Yeast
    'SAN1': ('yeast', 'SAN1'),
    'TSA1': ('yeast', 'TSA1'),
    'DnaK': ('ECO57', 'DnaK'),
    'DnaJ': ('ECO57', 'DnaJ'),
    'GroEL': ('ECO57', 'GroEL'),
    'Skp': ('ECO57', 'Skp'),
    'SurA': ('ECO57', 'SurA'),
    'HdeA': ('ECO57', 'HdeA'),
    'HdeB': ('ECO57', 'HdeB'),
    'SecB': ('ECO57', 'SecB'),
    'SlyD': ('ECO57', 'SlyD'),
    'CpxP': ('ECO57', 'CpxP'),
    'Spy': ('ECO57', 'Spy'),
    'CnoX': ('ECO57', 'CnoX'),
    'RidA': ('ECO57', 'RidA'),
    # C. elegans
    'lrx-1': ('worm', 'lrx-1'),
    # Fly
    'HSPH1': ('DROME', 'Hsph1'),
    # Mouse
    'Fbxo2': ('mouse', 'Fbxo2'),
}

def get_organism_from_taxon(taxon_id: str) -> Optional[str]:
    """Map NCBI taxon ID to organism code."""
    taxon_map = {
        '9606': 'human',
        '10090': 'mouse',
        '6239': 'worm',
        '7227': 'DROME',
        '559292': 'yeast',
        '83333': 'ECO57',
        '237561': 'CALBE',
        '5061': 'ANIGE',
        '4577': 'ARATH',
        '10029': 'CRIHA',
    }
    return taxon_map.get(taxon_id)

def get_gene_symbol(bioentity_label: str, taxon_id: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Get organism and gene symbol from bioentity_label and taxon.
    Returns (organism, gene_symbol) or (None, None) if not found.
    """
    # Try direct lookup
    if bioentity_label in GENE_MAPPING:
        return GENE_MAPPING[bioentity_label]
    
    # Try organism mapping
    organism = get_organism_from_taxon(taxon_id)
    if organism:
        return (organism, bioentity_label)
    
    return (None, None)

def get_recommendation(organism: str, gene_symbol: str) -> str:
    """
    Look up gene in YAML review file and extract reannotation recommendation.
    """
    genes_dir = Path('/home/raymond/local/src/git/ai-gene-review/genes')
    
    # Build path to review file
    review_path = genes_dir / organism / gene_symbol / f"{gene_symbol}-ai-review.yaml"
    
    if not review_path.exists():
        return f"No review file found for {organism}/{gene_symbol}"
    
    try:
        with open(review_path, 'r') as f:
            review = yaml.safe_load(f)
        
        # Extract actions from existing_annotations
        actions = []
        if 'existing_annotations' in review:
            for ann in review['existing_annotations']:
                if 'review' in ann and 'action' in ann['review']:
                    action = ann['review']['action']
                    term_label = ann.get('term', {}).get('label', 'Unknown')
                    actions.append(f"{action}: {term_label}")
        
        if actions:
            return '; '.join(actions[:3])  # Limit to first 3 actions
        else:
            return "No action found"
    except Exception as e:
        return f"Error reading {review_path}: {str(e)}"

def main():
    tsv_path = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING')
    tsv_file = list(tsv_path.glob('*.tsv'))[0]
    
    print(f"Reading {tsv_file.name}...")
    
    # Read TSV
    rows = []
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    print(f"Found {len(rows)} rows")
    
    # Process each row
    for i, row in enumerate(rows):
        bioentity_label = row.get('bioentity_label', '')
        taxon_id = row.get('taxon', '').replace('NCBITaxon:', '')
        
        if not bioentity_label:
            continue
        
        organism, gene_symbol = get_gene_symbol(bioentity_label, taxon_id)
        
        if organism and gene_symbol:
            recommendation = get_recommendation(organism, gene_symbol)
            row['Suggested action (by annotation review requester)'] = recommendation
            print(f"[{i+1}] {organism}/{gene_symbol}: {recommendation[:80]}...")
        else:
            print(f"[{i+1}] Could not map {bioentity_label} (taxon: {taxon_id})")
    
    # Write back to TSV
    output_path = tsv_file.parent / f"{tsv_file.stem}_FILLED{tsv_file.suffix}"
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nResults written to: {output_path.name}")

if __name__ == '__main__':
    main()
