#!/usr/bin/env python3
"""
Bioinformatic analysis of C. elegans LRX-1 protein (Q22179)
Analyzes protein sequence to validate/refute domain predictions
"""

import re
import json
from typing import List, Dict

def load_sequence() -> str:
    """Load the LRX-1 protein sequence"""
    # Q22179 sequence from UniProt
    sequence = """MAWLTSIFFILLAVQPVLPQDLYGTATQQQPYPYVQPSASSGSGGYVPNPQSSIHTVQQP
YPNIDVVEPDVDSVDIYETEEPQFKVVNPVFPLGGSGIVEEPGTIPPPMPQTQAPEKPDNS
YAINYCDKREFPDDVLAQYGLERIDYFVYNTSCSHVFFQCSIGQTFPLACMSEDQAFDKS
TENCNHKNAIKFCPEYDHVMHCTIKDTCTENEFACCAMPQSCIHVSKRCDGHPDCADGED
ENNCPSCARDDEFACVKSEHCIPANKRCDGVADDCEDGSNLDEIGCSKNTTCIGKFVCGTS
RGGVSCVDLDMHCDGKKDCLNGEDEMNCQEGRQKYLLCENQKQSVTRLQWCNGETDCAD
GSDEKYCY"""
    return sequence.replace("\n", "").replace(" ", "")

def analyze_cysteine_patterns(sequence: str) -> Dict:
    """Analyze cysteine distribution and spacing patterns"""
    
    # Find all cysteine positions
    cys_positions = [i for i, aa in enumerate(sequence) if aa == 'C']
    
    # Calculate spacings between consecutive cysteines
    spacings = []
    for i in range(1, len(cys_positions)):
        spacing = cys_positions[i] - cys_positions[i-1] - 1
        spacings.append(spacing)
    
    # Check for canonical LDL-A domain pattern
    # Pattern: C-x(2,3)-C-x(3,4)-[DE]-x(4,5)-C-x(7,8)-C-x(2,3)-C-x(3,9)-C
    potential_ldla = check_ldla_pattern(sequence, cys_positions, spacings)
    
    return {
        'total_cysteines': len(cys_positions),
        'cysteine_percentage': round((len(cys_positions) / len(sequence)) * 100, 2),
        'positions': cys_positions,
        'spacings': spacings,
        'potential_ldla_domains': potential_ldla,
        'cysteine_clusters': identify_cysteine_clusters(cys_positions, sequence)
    }

def check_ldla_pattern(sequence: str, cys_positions: List[int], spacings: List[int]) -> List[Dict]:
    """Check for LDL-A domain patterns"""
    potential_domains = []
    
    # Need at least 6 cysteines for one LDL-A domain
    if len(cys_positions) < 6:
        return potential_domains
    
    # Check each possible starting position
    for i in range(len(cys_positions) - 5):
        # Get the 6 cysteines that could form a domain
        domain_cysteines = cys_positions[i:i+6]
        domain_spacings = spacings[i:i+5] if i < len(spacings) - 4 else []
        
        if len(domain_spacings) >= 5:
            # Check if spacings match LDL-A pattern
            # C1-x(2,3)-C2-x(3,4)-[DE]-x(4,5)-C3-x(7,8)-C4-x(2,3)-C5-x(3,9)-C6
            spacing_match = (
                2 <= domain_spacings[0] <= 3 and  # C1 to C2
                3 <= domain_spacings[1] <= 4 and  # C2 to C3  
                7 <= domain_spacings[2] <= 8 and  # C3 to C4
                2 <= domain_spacings[3] <= 3 and  # C4 to C5
                3 <= domain_spacings[4] <= 9      # C5 to C6
            )
            
            # Check for acidic residue after C2
            c2_pos = domain_cysteines[1]
            has_acidic = False
            if c2_pos + 4 < len(sequence):
                region = sequence[c2_pos+1:c2_pos+6]
                has_acidic = 'D' in region or 'E' in region
            
            if spacing_match and has_acidic:
                potential_domains.append({
                    'start': domain_cysteines[0],
                    'end': domain_cysteines[5],
                    'cysteines': domain_cysteines,
                    'spacings': domain_spacings,
                    'confidence': 'high'
                })
            elif spacing_match:
                potential_domains.append({
                    'start': domain_cysteines[0],
                    'end': domain_cysteines[5],
                    'cysteines': domain_cysteines,
                    'spacings': domain_spacings,
                    'confidence': 'medium'
                })
    
    return potential_domains

def identify_cysteine_clusters(cys_positions: List[int], sequence: str) -> List[Dict]:
    """Identify regions with clustered cysteines"""
    clusters = []
    if not cys_positions:
        return clusters
    
    current_cluster = [cys_positions[0]]
    
    for i in range(1, len(cys_positions)):
        if cys_positions[i] - cys_positions[i-1] <= 25:  # Within 25 residues
            current_cluster.append(cys_positions[i])
        else:
            if len(current_cluster) >= 2:
                clusters.append({
                    'start': current_cluster[0],
                    'end': current_cluster[-1],
                    'n_cysteines': len(current_cluster),
                    'span': current_cluster[-1] - current_cluster[0] + 1,
                    'region': sequence[current_cluster[0]:current_cluster[-1]+1]
                })
            current_cluster = [cys_positions[i]]
    
    # Add last cluster
    if len(current_cluster) >= 2:
        clusters.append({
            'start': current_cluster[0],
            'end': current_cluster[-1],
            'n_cysteines': len(current_cluster),
            'span': current_cluster[-1] - current_cluster[0] + 1,
            'region': sequence[current_cluster[0]:current_cluster[-1]+1]
        })
    
    return clusters

def analyze_hydrophobicity(sequence: str) -> Dict:
    """Analyze hydrophobicity for membrane topology prediction"""
    
    hydrophobic_aa = set('AILMFWV')
    
    # Check signal peptide (first 30 aa)
    signal_region = sequence[:30] if len(sequence) >= 30 else sequence
    signal_hydro_count = sum(1 for aa in signal_region if aa in hydrophobic_aa)
    
    # Scan for transmembrane helices (windows of 20 aa)
    tm_candidates = []
    window_size = 20
    threshold = 0.65  # 65% hydrophobic
    
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        hydro_count = sum(1 for aa in window if aa in hydrophobic_aa)
        hydro_ratio = hydro_count / window_size
        
        if hydro_ratio >= threshold:
            tm_candidates.append({
                'start': i,
                'end': i + window_size,
                'hydrophobicity': round(hydro_ratio, 3),
                'sequence': window
            })
    
    # Merge overlapping TM candidates
    tm_regions = merge_overlapping_regions(tm_candidates)
    
    return {
        'signal_peptide': {
            'length': len(signal_region),
            'hydrophobic_count': signal_hydro_count,
            'hydrophobicity': round(signal_hydro_count / len(signal_region), 3)
        },
        'tm_regions': tm_regions,
        'topology_prediction': predict_topology(tm_regions, signal_hydro_count / len(signal_region))
    }

def merge_overlapping_regions(regions: List[Dict]) -> List[Dict]:
    """Merge overlapping hydrophobic regions"""
    if not regions:
        return []
    
    sorted_regions = sorted(regions, key=lambda x: x['start'])
    merged = [sorted_regions[0]]
    
    for region in sorted_regions[1:]:
        if region['start'] <= merged[-1]['end']:
            # Merge overlapping regions
            merged[-1]['end'] = max(merged[-1]['end'], region['end'])
        else:
            merged.append(region)
    
    return merged

def predict_topology(tm_regions: List[Dict], signal_hydrophobicity: float) -> str:
    """Predict protein topology based on hydrophobic regions"""
    
    if len(tm_regions) == 0:
        if signal_hydrophobicity > 0.4:
            return "likely_secreted"
        else:
            return "cytoplasmic"
    elif len(tm_regions) == 1:
        return "single_pass_membrane"
    else:
        return "multi_pass_membrane"

def check_domain_patterns(sequence: str) -> Dict:
    """Check for various domain patterns"""
    
    results = {}
    
    # EGF-like domain pattern: C-x(3,4)-C-x(3)-C-x(5)-C-x-C-x(2)-C
    egf_pattern = re.compile(r'C.{3,4}C.{3}C.{5}C.C.{2}C')
    egf_matches = egf_pattern.finditer(sequence)
    results['egf_domains'] = [{'start': m.start(), 'end': m.end(), 'sequence': m.group()} 
                              for m in egf_matches]
    
    # Check for other patterns could be added here
    
    return results

def compare_protein_sizes() -> Dict:
    """Compare LRX-1 size to typical LRP proteins"""
    
    return {
        'lrx1_length': None,  # Will be filled from sequence
        'typical_lrp_length': {'min': 4000, 'max': 6000, 'average': 4500},
        'typical_ldlr_length': {'min': 800, 'max': 900, 'average': 860},
        'size_compatible_with_lrp': None  # Will be calculated
    }

def main():
    """Run complete analysis and output results as JSON"""
    
    sequence = load_sequence()
    
    results = {
        'protein_info': {
            'uniprot_id': 'Q22179',
            'gene_name': 'lrx-1',
            'organism': 'Caenorhabditis elegans',
            'sequence_length': len(sequence)
        },
        'cysteine_analysis': analyze_cysteine_patterns(sequence),
        'hydrophobicity_analysis': analyze_hydrophobicity(sequence),
        'domain_patterns': check_domain_patterns(sequence),
        'size_comparison': compare_protein_sizes()
    }
    
    # Update size comparison with actual length
    results['size_comparison']['lrx1_length'] = len(sequence)
    results['size_comparison']['size_compatible_with_lrp'] = (
        len(sequence) >= results['size_comparison']['typical_lrp_length']['min']
    )
    
    # Output results as JSON
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()