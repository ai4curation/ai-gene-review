#!/usr/bin/env python3
"""
Update existing _FILLED.tsv file with inferred recommendations for "(No review file)" entries.
This script preserves all existing manual curation work and only fills empty entries.
"""

import csv
from pathlib import Path

# Evidence type confidence mapping
EVIDENCE_CONFIDENCE = {
    'IDA': ('ACCEPT', 'Direct assay - high confidence'),
    'IMP': ('ACCEPT', 'Mutant phenotype - high confidence'),
    'IGI': ('ACCEPT', 'Genetic interaction - high confidence'),
    'IPI': ('MODIFY', 'Protein interaction - may need more specific term'),
    'TAS': ('ACCEPT', 'Traceable author statement'),
    'NAS': ('MARK_AS_OVER_ANNOTATED', 'Non-traceable author statement'),
    'IC': ('MARK_AS_OVER_ANNOTATED', 'Inferred by curator'),
    'IEA': ('MARK_AS_OVER_ANNOTATED', 'Electronic annotation - low confidence'),
    'ISS': ('MARK_AS_OVER_ANNOTATED', 'Sequence similarity - may be over-annotation'),
    'ISO': ('MARK_AS_OVER_ANNOTATED', 'Sequence orthology'),
    'ISA': ('MARK_AS_OVER_ANNOTATED', 'Sequence alignment'),
    'ISM': ('MARK_AS_OVER_ANNOTATED', 'Sequence model'),
    'IGC': ('MARK_AS_OVER_ANNOTATED', 'Genomic context'),
    'IBA': ('MARK_AS_OVER_ANNOTATED', 'Biological aspect - phylogenetic'),
    'IBD': ('MARK_AS_OVER_ANNOTATED', 'Biological descent'),
    'IKR': ('MARK_AS_OVER_ANNOTATED', 'Key residues'),
    'IRD': ('MARK_AS_OVER_ANNOTATED', 'Rapid divergence'),
    'RCA': ('MARK_AS_OVER_ANNOTATED', 'Automatic computational annotation'),
    'ND': ('REMOVE', 'No biological data available'),
}

# Trusted database sources
TRUSTED_SOURCES = {
    'UniProt': ('ACCEPT', 'Expert curated database'),
    'MGI': ('ACCEPT', 'Mouse Genome Informatics - expert curated'),
    'SGD': ('ACCEPT', 'Saccharomyces Genome Database - expert curated'),
    'FlyBase': ('ACCEPT', 'Drosophila expert database'),
    'WormBase': ('ACCEPT', 'C. elegans expert database'),
    'ZFIN': ('ACCEPT', 'Zebrafish Information Network'),
    'PomBase': ('ACCEPT', 'S. pombe expert database'),
    'CGD': ('ACCEPT', 'Candida Genome Database'),
    'dictyBase': ('ACCEPT', 'Dictyostelium expert database'),
    'EcoCyc': ('ACCEPT', 'E. coli expert database'),
    'TAIR': ('ACCEPT', 'Arabidopsis expert database'),
}

def infer_recommendation(row: dict) -> str:
    """
    Infer a recommendation based on evidence type and data source.
    Returns a recommendation string.
    """
    evidence_type = row.get('evidence_type', '').strip()
    assigned_by = row.get('assigned_by', '').strip()
    gene = row.get('bioentity_label', '').strip()
    
    # Check trusted sources first
    if assigned_by in TRUSTED_SOURCES:
        action, reason = TRUSTED_SOURCES[assigned_by]
        if evidence_type in ['IDA', 'IMP', 'IGI', 'TAS']:
            return f"{action} ({reason}, {evidence_type} evidence)"
        elif evidence_type in ['IPI']:
            return f"MODIFY → GO:0044183 or GO:0140309 ({reason}, but protein binding may need specificity)"
        else:
            return f"MARK_AS_OVER_ANNOTATED ({reason}, but {evidence_type} is computational)"
    
    # Check evidence type
    if evidence_type in EVIDENCE_CONFIDENCE:
        action, reason = EVIDENCE_CONFIDENCE[evidence_type]
        return f"{action} ({reason})"
    
    # Default for unknown evidence
    return f"UNDECIDED (unknown evidence type: {evidence_type}, source: {assigned_by})"

def main():
    """Main function to update the FILLED TSV file."""
    
    tsv_file = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING') / '5974 Review annotations to GO_0031249 denatured protein binding GO_0051082 unfolded protein binding - Sheet1_FILLED.tsv'
    
    if not tsv_file.exists():
        print(f"❌ File not found: {tsv_file}")
        return
    
    print(f"Reading {tsv_file.name}...")
    
    # Read TSV
    rows = []
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    print(f"Found {len(rows)} total rows")
    
    # Count and update entries
    updated_count = 0
    no_review_count = 0
    
    for i, row in enumerate(rows, 1):
        current_rec = row.get('Suggested action (by annotation review requester)', '').strip()
        
        # Only update "(No review file)" entries
        if current_rec == '(No review file)':
            no_review_count += 1
            inferred_rec = infer_recommendation(row)
            row['Suggested action (by annotation review requester)'] = inferred_rec
            
            gene = row.get('bioentity_label', 'N/A')
            evidence = row.get('evidence_type', 'N/A')
            source = row.get('assigned_by', 'N/A')
            
            print(f"[{i}] {gene} ({evidence}/{source}): {inferred_rec[:80]}")
            updated_count += 1
    
    # Write back to same file
    with open(tsv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total rows: {len(rows)}")
    print(f"  '(No review file)' entries found: {no_review_count}")
    print(f"  Updated with inferred recommendations: {updated_count}")
    print(f"  File updated: {tsv_file.name}")

if __name__ == '__main__':
    main()
