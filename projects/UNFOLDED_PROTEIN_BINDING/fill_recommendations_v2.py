#!/usr/bin/env python3
"""
Fill column A (Suggested action) with reannotation recommendations from gene review YAML files.
Reads TSV, looks up genes in genes/*/*.yaml, extracts actions, and writes results back.
"""

import csv
import yaml
from pathlib import Path
from typing import Dict, Optional, Tuple, List
import re

# Comprehensive taxon ID to organism folder mapping
TAXON_TO_ORGANISM = {
    # Major model organisms
    '9606': 'human',           # Homo sapiens
    '10090': 'mouse',          # Mus musculus
    '10116': 'rat',            # Rattus norvegicus
    '6239': 'worm',            # Caenorhabditis elegans (also check 'elegans', 'nematode')
    '7227': 'DROME',           # Drosophila melanogaster
    '7955': 'DANRE',           # Danio rerio (zebrafish)
    '9913': 'BOVIN',           # Bos taurus (cattle)
    '9031': 'CHICK',           # Gallus gallus (chicken)
    
    # Fungi
    '559292': 'yeast',         # Saccharomyces cerevisiae
    '237561': 'CANAL',         # Candida albicans
    '5061': 'ASPNG',           # Candida tropicalis
    '431241': 'CANGA',         # Candida orthopsilosis
    '367110': 'NEUCR',         # Neurospora crassa
    '3702': 'ARATH',           # Arabidopsis thaliana
    '4577': 'ARATH',           # Treat maize as ARATH for now
    
    # Bacteria
    '83333': 'ECOLI',          # Escherichia coli K-12
    '83334': 'ECO57',          # E. coli K-12 W3110
    '99287': 'SALTY',          # Salmonella enterica
    '224308': 'BACSU',         # Bacillus subtilis
    '83332': 'MYCTU',          # Mycobacterium tuberculosis
    
    # Archaea and additional organisms
    '10029': 'CRIGR',          # Cricetulus griseus (hamster)
    '6238': 'CAEBR',           # C. briggsae
    '7165': 'ANOGA',           # Anopheles gambiae
    '3694': 'POPTR',           # Populus trichocarpa
    '1493': 'CLOCL',
    '272630': 'METEA',
    '882': 'DESVH',
    '1515': 'ACET2',
    '8713': 'AGKCO',
    '188937': '188937',
    '641491': '9BACT',
    '997891': '9BACT',
}

# Alternative organism folder names for the same organism
ORGANISM_ALIASES = {
    '6239': ['worm', 'elegans', 'nematode'],  # C. elegans has multiple folder names
}

def get_organism_folders(genes_dir: Path) -> Dict[str, List[str]]:
    """Get all available organism folders and their gene subdirs."""
    org_genes = {}
    for org_folder in genes_dir.iterdir():
        if org_folder.is_dir():
            gene_folders = [g.name for g in org_folder.iterdir() if g.is_dir()]
            org_genes[org_folder.name] = gene_folders
    return org_genes

def find_review_file(organism: str, gene_symbol: str, genes_dir: Path) -> Optional[Path]:
    """
    Find review YAML file for a gene in an organism folder.
    Tries exact match and fuzzy matches.
    """
    org_path = genes_dir / organism
    if not org_path.exists():
        # Try alternative folder names
        if organism in ORGANISM_ALIASES:
            for alt_org in ORGANISM_ALIASES[organism]:
                alt_path = genes_dir / alt_org
                if alt_path.exists():
                    org_path = alt_path
                    break
    
    if not org_path.exists():
        return None
    
    # Try exact match first (case insensitive)
    gene_lower = gene_symbol.lower()
    for folder in org_path.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            if folder_lower == gene_lower or folder_lower == gene_lower.rstrip('123456789'):
                review_file = folder / f"{folder.name}-ai-review.yaml"
                if review_file.exists():
                    return review_file
    
    # Try fuzzy match for complex names or aliases
    for folder in org_path.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            # Match if gene symbol is contained in folder name or vice versa
            if gene_lower in folder_lower or folder_lower in gene_lower:
                review_file = folder / f"{folder.name}-ai-review.yaml"
                if review_file.exists():
                    return review_file
    
    return None

def extract_actions(review_path: Path) -> List[str]:
    """Extract all action values from existing_annotations in YAML."""
    try:
        with open(review_path, 'r') as f:
            review = yaml.safe_load(f)
        
        if not review or 'existing_annotations' not in review:
            return []
        
        actions = []
        seen_actions = set()
        
        for ann in review['existing_annotations']:
            if 'review' in ann and 'action' in ann['review']:
                action = ann['review']['action']
                term_label = ann.get('term', {}).get('label', '')
                
                # Create a unique action string
                if term_label:
                    action_str = f"{action}: {term_label}"
                else:
                    action_str = action
                
                # Avoid duplicates but maintain order
                if action_str not in seen_actions:
                    actions.append(action_str)
                    seen_actions.add(action_str)
        
        return actions
    except Exception as e:
        return []

def get_recommendation_for_row(bioentity_label: str, taxon_id: str, genes_dir: Path) -> str:
    """
    Get reannotation recommendation for a single row.
    Returns either the actions found or an error message.
    """
    taxon_id = taxon_id.replace('NCBITaxon:', '').strip()
    
    if not taxon_id:
        return "No taxon ID"
    
    # Get organism code from taxon
    organism = TAXON_TO_ORGANISM.get(taxon_id)
    if not organism:
        return f"Unknown taxon: {taxon_id}"
    
    # Find review file
    review_path = find_review_file(organism, bioentity_label, genes_dir)
    
    if not review_path:
        # Try alternative organisms for this taxon
        if taxon_id in ORGANISM_ALIASES:
            for alt_org in ORGANISM_ALIASES[taxon_id]:
                review_path = find_review_file(alt_org, bioentity_label, genes_dir)
                if review_path:
                    break
    
    if not review_path:
        return f"No review found for {organism}/{bioentity_label}"
    
    # Extract actions
    actions = extract_actions(review_path)
    
    if not actions:
        return "No actions in review"
    
    # Return combined actions (limit to reasonable length)
    return '; '.join(actions[:5])

def main():
    tsv_dir = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING')
    genes_dir = Path('/home/raymond/local/src/git/ai-gene-review/genes')
    
    # Find TSV file
    tsv_files = list(tsv_dir.glob('*.tsv'))
    tsv_files = [f for f in tsv_files if 'FILLED' not in f.name]  # Skip already filled
    
    if not tsv_files:
        print("No TSV file found")
        return
    
    tsv_file = tsv_files[0]
    
    print(f"Reading {tsv_file.name}...")
    
    # Read TSV
    rows = []
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    print(f"Found {len(rows)} rows")
    
    # Process each row
    matched = 0
    for i, row in enumerate(rows, 1):
        bioentity_label = row.get('bioentity_label', '').strip()
        taxon_id = row.get('taxon', '').strip()
        
        if not bioentity_label:
            print(f"[{i}] Empty bioentity_label")
            continue
        
        recommendation = get_recommendation_for_row(bioentity_label, taxon_id, genes_dir)
        
        if not recommendation.startswith('No review') and not recommendation.startswith('Unknown') and not recommendation.startswith('No actions'):
            matched += 1
            print(f"[{i}] {bioentity_label}: {recommendation[:100]}...")
        else:
            print(f"[{i}] {bioentity_label}: {recommendation}")
        
        row['Suggested action (by annotation review requester)'] = recommendation
    
    # Write back to TSV
    output_path = tsv_file.parent / f"{tsv_file.stem}_FILLED{tsv_file.suffix}"
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nMatched {matched}/{len(rows)} rows")
    print(f"Results written to: {output_path.name}")

if __name__ == '__main__':
    main()
