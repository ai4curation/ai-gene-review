#!/usr/bin/env python3
"""
Domain architecture analysis for GATA3
Analyzes zinc finger domains and other functional regions
"""

import sys
import json
import requests
from Bio import SeqIO
from Bio.Seq import Seq
from io import StringIO
import re

def fetch_uniprot_sequence(uniprot_id):
    """Fetch protein sequence from UniProt"""
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch sequence for {uniprot_id}")

def fetch_uniprot_features(uniprot_id):
    """Fetch feature annotations from UniProt"""
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch features for {uniprot_id}")

def analyze_zinc_fingers(sequence):
    """Identify zinc finger domains using pattern matching"""
    # Classic C2H2 zinc finger pattern
    c2h2_pattern = r'C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H'
    # GATA-type zinc finger pattern (C4 type)
    gata_pattern = r'C.{2}C.{17,20}C.{2}C'
    
    results = {
        'c2h2_matches': [],
        'gata_matches': []
    }
    
    # Search for C2H2 patterns
    for match in re.finditer(c2h2_pattern, str(sequence)):
        results['c2h2_matches'].append({
            'start': match.start() + 1,  # 1-based
            'end': match.end(),
            'sequence': match.group()
        })
    
    # Search for GATA patterns
    for match in re.finditer(gata_pattern, str(sequence)):
        results['gata_matches'].append({
            'start': match.start() + 1,  # 1-based
            'end': match.end(),
            'sequence': match.group()
        })
    
    return results

def main():
    uniprot_id = sys.argv[1] if len(sys.argv) > 1 else "P23771"
    
    print(f"Analyzing GATA3 (UniProt: {uniprot_id})")
    print("=" * 60)
    
    # Fetch sequence
    fasta_text = fetch_uniprot_sequence(uniprot_id)
    record = SeqIO.read(StringIO(fasta_text), "fasta")
    sequence = record.seq
    
    print(f"\nProtein length: {len(sequence)} amino acids")
    
    # Fetch UniProt features
    uniprot_data = fetch_uniprot_features(uniprot_id)
    
    # Extract domain information from UniProt
    print("\n## UniProt Annotated Domains:")
    print("-" * 40)
    
    domains = []
    if 'features' in uniprot_data:
        for feature in uniprot_data['features']:
            if feature['type'] in ['Domain', 'Zinc finger', 'Region', 'DNA binding']:
                location = feature.get('location', {})
                start = location.get('start', {}).get('value', 'N/A')
                end = location.get('end', {}).get('value', 'N/A')
                description = feature.get('description', 'No description')
                
                domains.append({
                    'type': feature['type'],
                    'description': description,
                    'start': start,
                    'end': end
                })
                
                print(f"{feature['type']}: {description}")
                print(f"  Position: {start}-{end}")
                if start != 'N/A' and end != 'N/A':
                    domain_seq = sequence[start-1:end]
                    print(f"  Sequence: {domain_seq}")
                print()
    
    # Pattern-based zinc finger detection
    print("\n## Pattern-based Zinc Finger Detection:")
    print("-" * 40)
    
    zf_patterns = analyze_zinc_fingers(sequence)
    
    if zf_patterns['gata_matches']:
        print("\nGATA-type zinc fingers (C4 pattern):")
        for i, match in enumerate(zf_patterns['gata_matches'], 1):
            print(f"  ZF{i}: positions {match['start']}-{match['end']}")
            print(f"    Sequence: {match['sequence']}")
    
    if zf_patterns['c2h2_matches']:
        print("\nC2H2-type zinc fingers:")
        for i, match in enumerate(zf_patterns['c2h2_matches'], 1):
            print(f"  ZF{i}: positions {match['start']}-{match['end']}")
            print(f"    Sequence: {match['sequence']}")
    
    # Known GATA3 zinc fingers (from literature)
    print("\n## Literature-documented GATA3 Zinc Fingers:")
    print("-" * 40)
    print("N-terminal zinc finger (ZF1): ~260-284")
    print("C-terminal zinc finger (ZF2): ~311-335")
    
    # Extract and display the known zinc finger sequences
    zf1_seq = sequence[259:284]  # 0-based indexing
    zf2_seq = sequence[310:335]
    
    print(f"\nZF1 sequence: {zf1_seq}")
    print(f"ZF2 sequence: {zf2_seq}")
    
    # Check for conserved cysteines
    print("\n## Cysteine positions (important for zinc coordination):")
    print("-" * 40)
    cys_positions = [i+1 for i, aa in enumerate(sequence) if aa == 'C']
    print(f"Cysteine positions: {cys_positions}")
    
    # Save results to JSON
    results = {
        'protein_length': len(sequence),
        'uniprot_domains': domains,
        'pattern_matches': zf_patterns,
        'known_zinc_fingers': {
            'ZF1': {'start': 260, 'end': 284, 'sequence': str(zf1_seq)},
            'ZF2': {'start': 311, 'end': 335, 'sequence': str(zf2_seq)}
        },
        'cysteine_positions': cys_positions
    }
    
    with open('domain_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n## Summary:")
    print("-" * 40)
    print(f"Total domains identified: {len(domains)}")
    print(f"Zinc fingers detected by pattern: {len(zf_patterns['gata_matches']) + len(zf_patterns['c2h2_matches'])}")
    print("\nResults saved to domain_analysis_results.json")

if __name__ == "__main__":
    main()