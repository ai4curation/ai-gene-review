#!/usr/bin/env python3
"""
Conservation analysis for GATA3 across species
Analyzes conservation of zinc finger domains and overall protein
"""

import sys
import json
import requests
from Bio import SeqIO, AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from io import StringIO
import pandas as pd

def fetch_orthologs_from_uniprot(gene_name="GATA3"):
    """Fetch GATA3 orthologs from different species via UniProt"""
    
    # Key species to check for GATA3 orthologs
    orthologs = {
        'Homo sapiens': 'P23771',
        'Mus musculus': 'P23772',  # Mouse GATA3
        'Rattus norvegicus': 'A0A0G2K079',  # Rat GATA3
        'Gallus gallus': 'Q92002',  # Chicken GATA3
        'Xenopus tropicalis': 'Q28G47',  # Frog GATA3
        'Danio rerio': 'Q90X44',  # Zebrafish GATA3
    }
    
    sequences = {}
    
    for species, uniprot_id in orthologs.items():
        try:
            url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
            response = requests.get(url)
            if response.status_code == 200:
                record = SeqIO.read(StringIO(response.text), "fasta")
                sequences[species] = {
                    'id': uniprot_id,
                    'sequence': str(record.seq),
                    'description': record.description
                }
                print(f"Fetched {species} GATA3 ({uniprot_id})")
            else:
                print(f"Failed to fetch {species} GATA3 ({uniprot_id})")
        except Exception as e:
            print(f"Error fetching {species}: {e}")
    
    return sequences

def calculate_identity(seq1, seq2):
    """Calculate sequence identity between two sequences"""
    if len(seq1) != len(seq2):
        # For different lengths, use the shorter sequence length
        min_len = min(len(seq1), len(seq2))
        seq1 = seq1[:min_len]
        seq2 = seq2[:min_len]
    
    matches = sum(a == b for a, b in zip(seq1, seq2))
    return (matches / len(seq1)) * 100

def analyze_domain_conservation(sequences, domain_regions):
    """Analyze conservation specifically in domain regions"""
    
    human_seq = sequences.get('Homo sapiens', {}).get('sequence', '')
    if not human_seq:
        return {}
    
    conservation_results = {}
    
    for domain_name, region in domain_regions.items():
        start, end = region['start'] - 1, region['end']  # Convert to 0-based
        human_domain = human_seq[start:end]
        
        conservation_results[domain_name] = {
            'human_sequence': human_domain,
            'conservation': {}
        }
        
        for species, data in sequences.items():
            if species == 'Homo sapiens':
                continue
            
            seq = data['sequence']
            if len(seq) > start:
                # Extract corresponding region (may be shorter in some species)
                species_domain = seq[start:min(end, len(seq))]
                identity = calculate_identity(human_domain, species_domain)
                
                conservation_results[domain_name]['conservation'][species] = {
                    'sequence': species_domain,
                    'identity': round(identity, 2)
                }
    
    return conservation_results

def main():
    print("GATA3 Conservation Analysis")
    print("=" * 60)
    
    # Fetch ortholog sequences
    print("\n## Fetching GATA3 orthologs...")
    print("-" * 40)
    sequences = fetch_orthologs_from_uniprot()
    
    if not sequences:
        print("Error: Could not fetch any sequences")
        return
    
    # Calculate overall sequence conservation
    print("\n## Overall Sequence Conservation:")
    print("-" * 40)
    
    human_seq = sequences.get('Homo sapiens', {}).get('sequence', '')
    conservation_matrix = {}
    
    for species, data in sequences.items():
        conservation_matrix[species] = {}
        for species2, data2 in sequences.items():
            identity = calculate_identity(data['sequence'], data2['sequence'])
            conservation_matrix[species][species2] = round(identity, 2)
    
    # Display conservation matrix
    df = pd.DataFrame(conservation_matrix)
    print("\nPairwise sequence identity (%):")
    print(df.to_string())
    
    # Analyze zinc finger domain conservation
    print("\n## Zinc Finger Domain Conservation:")
    print("-" * 40)
    
    # Define domain regions based on literature
    domain_regions = {
        'ZF1_Nterminal': {'start': 260, 'end': 284},
        'ZF2_Cterminal': {'start': 311, 'end': 335},
        'TAD_domain': {'start': 1, 'end': 100},  # Transactivation domain
        'Full_DNAbinding': {'start': 250, 'end': 370}  # Extended DNA binding region
    }
    
    domain_conservation = analyze_domain_conservation(sequences, domain_regions)
    
    for domain_name, results in domain_conservation.items():
        print(f"\n{domain_name}:")
        print(f"  Human sequence: {results['human_sequence']}")
        print("  Conservation across species:")
        
        for species, cons_data in results['conservation'].items():
            print(f"    {species}: {cons_data['identity']}% identity")
            if cons_data['identity'] < 100:
                print(f"      Sequence: {cons_data['sequence']}")
    
    # Identify highly conserved regions
    print("\n## Highly Conserved Motifs:")
    print("-" * 40)
    
    # Check for GATA binding motif conservation
    gata_motif = "CNACG"  # Core GATA zinc finger motif
    wrcnacg = "WRCNACG"  # Extended motif
    
    for species, data in sequences.items():
        seq = data['sequence']
        if gata_motif in seq:
            pos = seq.find(gata_motif)
            print(f"{species}: GATA motif found at position {pos + 1}")
    
    # Save results
    results = {
        'species_analyzed': list(sequences.keys()),
        'conservation_matrix': conservation_matrix,
        'domain_conservation': domain_conservation,
        'sequence_lengths': {sp: len(data['sequence']) for sp, data in sequences.items()}
    }
    
    with open('conservation_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save sequences for further analysis
    with open('gata3_orthologs.fasta', 'w') as f:
        for species, data in sequences.items():
            f.write(f">{data['id']}|{species}\n{data['sequence']}\n")
    
    print("\n## Summary:")
    print("-" * 40)
    print(f"Species analyzed: {len(sequences)}")
    print(f"Average conservation to human: {sum(conservation_matrix['Homo sapiens'].values())/len(conservation_matrix['Homo sapiens']):.2f}%")
    print("\nResults saved to:")
    print("  - conservation_analysis_results.json")
    print("  - gata3_orthologs.fasta")

if __name__ == "__main__":
    main()