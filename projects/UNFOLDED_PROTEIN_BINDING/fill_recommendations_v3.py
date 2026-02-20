#!/usr/bin/env python3
"""
Fill column A (Suggested action) with reannotation recommendations from gene review YAML files
and statistical inference for genes without reviews.

Strategy:
1. For genes with review files, extract actions directly
2. For genes without reviews, infer based on:
   - Data source (CAFA, DisProt, expert databases suggest ACCEPT/MARK_AS_OVER_ANNOTATED)
   - Evidence type (IDA=high confidence ACCEPT, IPI=MODIFY, computational=MARK_AS_OVER_ANNOTATED)
   - Similarity to reviewed genes
"""

import csv
import yaml
from pathlib import Path
from typing import Dict, Optional, Tuple, List
import re
from collections import defaultdict

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
    '4896': 'SCHPO',           # Schizosaccharomyces pombe (fission yeast)
    '1493': 'CLOCL',
    '272630': 'METEA',
    '882': 'DESVH',
    '1515': 'ACET2',
    '8713': 'AGKCO',
    '188937': '188937',
    '641491': '9BACT',
    '997891': '9BACT',
    '36329': None,  # Viral/uncertain organism - use inference instead
}

# Alternative organism folder names for the same organism
ORGANISM_ALIASES = {
    '6239': ['worm', 'elegans', 'nematode'],  # C. elegans has multiple folder names
}

# Evidence type confidence scoring (higher = more confident in the annotation)
EVIDENCE_TYPE_CONFIDENCE = {
    'IDA': 0.95,  # Inferred from Direct Assay
    'IEP': 0.90,  # Inferred from Expression Pattern
    'IPI': 0.85,  # Inferred from Protein Interaction
    'IGI': 0.80,  # Inferred from Genetic Interaction
    'IMP': 0.75,  # Inferred from Mutant Phenotype
    'IEA': 0.30,  # Inferred from Electronic Annotation
    'RCA': 0.50,  # Reviewed Computational Analysis
    'TAS': 0.85,  # Traceable Author Statement
    'NAS': 0.70,  # Non-traceable Author Statement
    'ISS': 0.60,  # Inferred from Sequence Similarity
    'ISO': 0.60,  # Inferred from Sequence Orthology
    'ISA': 0.60,  # Inferred from Sequence Alignment
    'ISM': 0.60,  # Inferred from Sequence Model
    'IGC': 0.60,  # Inferred from Genomic Context
}

# Data source scoring (whether we trust the source to have made a careful annotation)
DATA_SOURCE_EVIDENCE = {
    'CAFA': 0.40,      # Computational; tends to over-annotate
    'DisProt': 0.75,   # Intrinsic disorder specialists; usually careful
    'FlyBase': 0.80,   # Expert curated
    'MGI': 0.80,       # Expert curated (mouse)
    'ComplexPortal': 0.70,  # Protein complex database; mixed quality
    'AgBase': 0.75,    # Livestock Gene databases
    'AspGD': 0.75,     # Aspergillus database
    'BHF-UCL': 0.70,  # Cardiovascular research curated
    'CGD': 0.75,       # Candida genomics database
    'EcoCyc': 0.75,    # E. coli database; usually good
    'UniProt': 0.80,   # Expert curated
    'Reactome': 0.70,  # Pathway database
}

def infer_action_from_evidence(evidence_type: str, assigned_by: str) -> str:
    """
    Infer recommendation based on evidence type and source for genes without reviews.
    """
    confidence = EVIDENCE_TYPE_CONFIDENCE.get(evidence_type, 0.50)
    source_score = DATA_SOURCE_EVIDENCE.get(assigned_by, 0.50)
    combined_score = (confidence * 0.6) + (source_score * 0.4)  # Weight evidence more
    
    # Decision logic based on combined score
    if combined_score >= 0.80:
        return "ACCEPT: (inferred from evidence)"
    elif combined_score >= 0.60:
        return "MODIFY: unfolded protein binding (requires expert review)"
    elif combined_score >= 0.45:
        return "MARK_AS_OVER_ANNOTATED: (low confidence source)"
    else:
        return "MARK_AS_OVER_ANNOTATED: (computational prediction)"

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

def get_recommendation_for_row(row: Dict, genes_dir: Path) -> str:
    """
    Get reannotation recommendation for a single row.
    Returns either the actions found from reviews or inferred recommendation.
    """
    bioentity_label = row.get('bioentity_label', '').strip()
    taxon_id = row.get('taxon', '').replace('NCBITaxon:', '').strip()
    evidence_type = row.get('evidence_type', '').strip()
    assigned_by = row.get('assigned_by', '').strip()
    
    if not bioentity_label or not taxon_id:
        return "Missing data"
    
    # Get organism code from taxon
    organism = TAXON_TO_ORGANISM.get(taxon_id)
    if not organism:
        # Unknown taxon - use inference
        return infer_action_from_evidence(evidence_type, assigned_by)
    
    if organism is None:
        # Organism explicitly set to None (e.g., viral) - use inference
        return infer_action_from_evidence(evidence_type, assigned_by)
    
    # Find review file
    review_path = find_review_file(organism, bioentity_label, genes_dir)
    
    if not review_path:
        # Try alternative organisms for this taxon
        if taxon_id in ORGANISM_ALIASES:
            for alt_org in ORGANISM_ALIASES[taxon_id]:
                review_path = find_review_file(alt_org, bioentity_label, genes_dir)
                if review_path:
                    break
    
    if review_path:
        # Extract actions from existing review
        actions = extract_actions(review_path)
        if actions:
            return '; '.join(actions[:5])
        else:
            return "No actions in review"
    else:
        # Infer recommendation based on evidence
        inferred = infer_action_from_evidence(evidence_type, assigned_by)
        return inferred

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
    matched_reviews = 0
    inferred = 0
    for i, row in enumerate(rows, 1):
        recommendation = get_recommendation_for_row(row, genes_dir)
        
        if not recommendation.startswith('Unknown') and not recommendation.startswith('Missing'):
            if 'inferred' in recommendation.lower():
                inferred += 1
                print(f"[{i}] {row.get('bioentity_label', 'N/A')} (inferred): {recommendation[:80]}")
            else:
                matched_reviews += 1
                if not recommendation.startswith('No actions') and not recommendation.startswith('No review'):
                    print(f"[{i}] {row.get('bioentity_label', 'N/A')}: {recommendation[:80]}")
        else:
            print(f"[{i}] {row.get('bioentity_label', 'N/A')}: {recommendation}")
        
        row['Suggested action (by annotation review requester)'] = recommendation
    
    # Write back to TSV
    output_path = tsv_file.parent / f"{tsv_file.stem}_FILLED{tsv_file.suffix}"
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nMatched {matched_reviews} from reviews + {inferred} inferred = {matched_reviews + inferred}/{ len(rows)}")
    print(f"Results written to: {output_path.name}")

if __name__ == '__main__':
    main()
