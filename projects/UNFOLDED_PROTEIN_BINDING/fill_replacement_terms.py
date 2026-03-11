#!/usr/bin/env python3
"""
Fill column A (Suggested action) with recommended replacement GO terms from gene review files.

For each annotation:
1. Find the gene review YAML file
2. Match the annotation by evidence (PMID/reference)
3. Extract proposed_replacement_terms from review.action data
4. Write the new GO term(s) to column A
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
    '6239': 'worm',            # Caenorhabditis elegans
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
    '4577': 'ARATH',           # Zea mays -> ARATH
    
    # Bacteria
    '83333': 'ECOLI',          # Escherichia coli K-12
    '83334': 'ECO57',          # E. coli K-12 W3110
    '99287': 'SALTY',          # Salmonella enterica
    '224308': 'BACSU',         # Bacillus subtilis
    '83332': 'MYCTU',          # Mycobacterium tuberculosis
    
    # Additional organisms
    '10029': 'CRIGR',          # Cricetulus griseus (hamster)
    '6238': 'CAEBR',           # C. briggsae
    '7165': 'ANOGA',           # Anopheles gambiae
    '3694': 'POPTR',           # Populus trichocarpa
    '4896': 'SCHPO',           # Schizosaccharomyces pombe
    '1493': 'CLOCL',
    '272630': 'METEA',
    '882': 'DESVH',
    '1515': 'ACET2',
    '8713': 'AGKCO',
    '188937': '188937',
    '641491': '9BACT',
    '997891': '9BACT',
    '36329': None,  # Viral/uncertain
}

ORGANISM_ALIASES = {
    '6239': ['worm', 'elegans', 'nematode'],
}

def find_review_file(organism: str, gene_symbol: str, genes_dir: Path) -> Optional[Path]:
    """Find review YAML file for a gene in an organism folder."""
    org_path = genes_dir / organism
    if not org_path.exists():
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
    
    # Try fuzzy match
    for folder in org_path.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            if gene_lower in folder_lower or folder_lower in gene_lower:
                review_file = folder / f"{folder.name}-ai-review.yaml"
                if review_file.exists():
                    return review_file
    
    return None

def extract_reference_id(reference_str: str) -> Optional[str]:
    """Extract PMID or reference ID from reference string."""
    # Handle "PMID:12345" or just plain ID
    if not reference_str:
        return None
    
    # Try to extract PMID
    pmid_match = re.search(r'PMID[:\s]+(\d+)', reference_str, re.IGNORECASE)
    if pmid_match:
        return f"PMID:{pmid_match.group(1)}"
    
    # Try other reference formats
    ref_match = re.search(r'(GO_REF:\d+|Reactome:\w+|[\w]+:\w+)', reference_str)
    if ref_match:
        return ref_match.group(1)
    
    return reference_str.strip()

def get_replacement_terms(review_path: Path, reference_id: str, go_term_id: str) -> Tuple[List[str], str]:
    """
    Extract replacement GO terms for a specific annotation by reference ID AND GO term.
    Returns (list of suggested replacement GO terms, action type).
    """
    try:
        with open(review_path, 'r') as f:
            review = yaml.safe_load(f)
        
        if not review or 'existing_annotations' not in review:
            return [], ""
        
        # Find annotation matching this reference AND GO term
        for ann in review['existing_annotations']:
            # Must match BOTH reference AND the GO term being obsoleted
            ann_go_id = ann.get('term', {}).get('id', '')
            ann_ref_id = ann.get('original_reference_id', '')
            
            if ann_ref_id == reference_id and ann_go_id == go_term_id:
                if 'review' not in ann:
                    continue
                
                review_obj = ann['review']
                action = review_obj.get('action', '')
                
                # If MODIFY action, look for proposed replacement terms
                if action == 'MODIFY':
                    replacements = review_obj.get('proposed_replacement_terms', [])
                    if replacements:
                        # Format as "GO:XXXXX (label)"
                        terms = []
                        for rep in replacements:
                            if isinstance(rep, dict):
                                term_id = rep.get('id', '')
                                term_label = rep.get('label', '')
                                if term_id and term_label:
                                    terms.append(f"{term_id} ({term_label})")
                                elif term_id:
                                    terms.append(term_id)
                            elif isinstance(rep, str):
                                terms.append(rep)
                        return terms, action
                    else:
                        # MODIFY but no replacement terms specified
                        return [], action
                
                # ACCEPT should NOT happen for GO:0051082/GO:0031249 - these are being obsoleted!
                # But if it does, it means "keep temporarily until better term available"
                elif action == 'ACCEPT':
                    return ['GO:0051082 (retain temporarily until replacement term created)'], action
                
                # REMOVE: Delete annotation entirely
                elif action == 'REMOVE':
                    return ['DELETE'], action
                
                # MARK_AS_OVER_ANNOTATED: Flag for curator review
                elif action == 'MARK_AS_OVER_ANNOTATED':
                    return ['REVIEW'], action
                
                # KEEP_AS_NON_CORE: Keep but downgrade importance
                # For obsolete terms, this means keep temporarily but mark as non-core
                elif action == 'KEEP_AS_NON_CORE':
                    return ['GO:0051082 (retain temporarily as non-core until replacement created)'], action
                
                # Other actions
                elif action:
                    return [f'{action}'], action
                
                break
        
        return [], ""
    except Exception as e:
        return [], ""

def get_recommendation_for_row(row: Dict, genes_dir: Path) -> str:
    """
    Get replacement GO term(s) for a single row.
    """
    bioentity_label = row.get('bioentity_label', '').strip()
    taxon_id = row.get('taxon', '').replace('NCBITaxon:', '').strip()
    reference = row.get('reference', '').strip()
    go_term_id = row.get('annotation_class', '').strip()  # The GO term being obsoleted
    
    if not bioentity_label or not taxon_id:
        return "(Missing data)"
    
    if not go_term_id:
        return "(Missing GO term)"
    
    # Get organism code from taxon
    organism = TAXON_TO_ORGANISM.get(taxon_id)
    if not organism:
        # Unknown taxon - can't look up
        return "(Unknown organism)"
    
    if organism is None:
        # Viral/uncertain organism
        return "(Organism not in project)"
    
    # Find review file
    review_path = find_review_file(organism, bioentity_label, genes_dir)
    
    if not review_path:
        # Try alternative organisms
        if taxon_id in ORGANISM_ALIASES:
            for alt_org in ORGANISM_ALIASES[taxon_id]:
                review_path = find_review_file(alt_org, bioentity_label, genes_dir)
                if review_path:
                    break
    
    if not review_path:
        return "(No review file)"
    
    # Extract reference ID
    reference_id = extract_reference_id(reference)
    if not reference_id:
        return "(No reference)"
    
    # Get replacement terms and action - must match both PMID and GO term
    replacements, action = get_replacement_terms(review_path, reference_id, go_term_id)
    
    if replacements:
        return '; '.join(replacements)
    elif action == 'MODIFY':
        return "MODIFY (replacement term not specified in review)"
    elif action:
        return f"{action} (unexpected - check review file)"
    else:
        return "(No matching annotation in review)"

def main():
    tsv_dir = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING')
    genes_dir = Path('/home/raymond/local/src/git/ai-gene-review/genes')
    
    # Find TSV file
    tsv_files = list(tsv_dir.glob('*.tsv'))
    tsv_files = [f for f in tsv_files if 'FILLED' not in f.name]
    
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
    
    print(f"Found {len(rows)} rows\n")
    
    # Process each row
    found_count = 0
    for i, row in enumerate(rows, 1):
        recommendation = get_recommendation_for_row(row, genes_dir)
        
        if not recommendation.startswith('('):
            found_count += 1
            gene = row.get('bioentity_label', 'N/A')
            evidence = row.get('reference', 'N/A')
            print(f"[{i}] {gene}: {recommendation}")
        
        row['Suggested action (by annotation review requester)'] = recommendation
    
    # Write back to TSV
    output_path = tsv_file.parent / f"{tsv_file.stem}_FILLED{tsv_file.suffix}"
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nFound {found_count}/{len(rows)} annotations with replacement terms")
    print(f"Results written to: {output_path.name}")

if __name__ == '__main__':
    main()
