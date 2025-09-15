#!/usr/bin/env python3
"""
Structure analysis for GATA3
Analyzes available PDB structures and AlphaFold predictions
"""

import sys
import json
import requests
import pandas as pd
from collections import defaultdict

def fetch_pdb_structures(uniprot_id="P23771"):
    """Fetch PDB structures mapped to UniProt ID"""
    
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{uniprot_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get(uniprot_id, {})
        else:
            print(f"No PDB structures found for {uniprot_id}")
            return {}
    except Exception as e:
        print(f"Error fetching PDB data: {e}")
        return {}

def fetch_alphafold_structure(uniprot_id="P23771"):
    """Check for AlphaFold structure availability"""
    
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else {}
        else:
            print(f"No AlphaFold structure found for {uniprot_id}")
            return {}
    except Exception as e:
        print(f"Error fetching AlphaFold data: {e}")
        return {}

def analyze_pdb_structure(pdb_data):
    """Analyze PDB structure data"""
    
    structures = []
    
    for pdb_id, mappings in pdb_data.items():
        for mapping in mappings:
            struct_info = {
                'pdb_id': pdb_id,
                'chain': mapping.get('chain_id', 'N/A'),
                'start': mapping.get('unp_start', 'N/A'),
                'end': mapping.get('unp_end', 'N/A'),
                'resolution': mapping.get('resolution', 'N/A'),
                'method': mapping.get('experimental_method', 'N/A'),
                'title': mapping.get('title', 'N/A')
            }
            structures.append(struct_info)
    
    return structures

def get_gata3_structural_features():
    """Return known structural features of GATA3"""
    
    features = {
        'zinc_fingers': {
            'ZF1_N-terminal': {
                'residues': '260-284',
                'type': 'C4-type zinc finger',
                'function': 'DNA binding, specificity',
                'structure': 'Four cysteine residues coordinate zinc',
                'dna_binding': 'Minor groove binding'
            },
            'ZF2_C-terminal': {
                'residues': '311-335',
                'type': 'C4-type zinc finger',
                'function': 'DNA binding, stability',
                'structure': 'Four cysteine residues coordinate zinc',
                'dna_binding': 'Major groove binding'
            }
        },
        'functional_regions': {
            'TAD1': {
                'residues': '1-100',
                'function': 'Transactivation domain 1',
                'structure': 'Intrinsically disordered region'
            },
            'TAD2': {
                'residues': '350-443',
                'function': 'Transactivation domain 2',
                'structure': 'Intrinsically disordered region'
            },
            'DNA_binding_domain': {
                'residues': '250-370',
                'function': 'Complete DNA binding domain',
                'structure': 'Two zinc fingers with linker'
            }
        },
        'dna_recognition': {
            'consensus_sequence': 'WGATAR',
            'expanded_motif': '(A/T)GATA(A/G)',
            'binding_mode': 'Both zinc fingers contact DNA',
            'specificity_determinants': [
                'ZF1: Provides specificity',
                'ZF2: Provides stability',
                'Linker region: Allows flexibility'
            ]
        }
    }
    
    return features

def analyze_secondary_structure_prediction(sequence):
    """Predict secondary structure elements (simplified)"""
    
    # This is a simplified prediction based on known patterns
    # Real analysis would use more sophisticated methods
    
    helix_pattern = '[AEHKLMQR]{4,}'
    sheet_pattern = '[VFIYWL]{3,}'
    
    length = len(sequence)
    
    # Known regions from literature
    structure_regions = {
        'disordered_N_terminus': (1, 100),
        'structured_core': (250, 370),
        'disordered_C_terminus': (370, 443)
    }
    
    return structure_regions

def main():
    uniprot_id = sys.argv[1] if len(sys.argv) > 1 else "P23771"
    
    print("GATA3 Structure Analysis")
    print("=" * 60)
    
    # Check for PDB structures
    print("\n## PDB Structures:")
    print("-" * 40)
    
    pdb_data = fetch_pdb_structures(uniprot_id)
    
    if pdb_data:
        structures = analyze_pdb_structure(pdb_data)
        print(f"Found {len(structures)} PDB structure(s)")
        
        for struct in structures:
            print(f"\nPDB ID: {struct['pdb_id']}")
            print(f"  Chain: {struct['chain']}")
            print(f"  Residues: {struct['start']}-{struct['end']}")
            print(f"  Method: {struct['method']}")
            print(f"  Resolution: {struct['resolution']} Å")
    else:
        print("No experimental structures found in PDB")
        print("\nNote: GATA3 zinc finger domains bound to DNA have been crystallized")
        print("Example structures (may need manual lookup):")
        print("  - 3DFX: GATA3 zinc fingers bound to DNA")
        print("  - 4HC9: GATA3 protein-DNA complex")
    
    # Check AlphaFold structure
    print("\n## AlphaFold Structure Prediction:")
    print("-" * 40)
    
    af_data = fetch_alphafold_structure(uniprot_id)
    
    if af_data:
        print(f"AlphaFold structure available")
        print(f"  Version: {af_data.get('modelCreatedDate', 'N/A')}")
        print(f"  Confidence: pLDDT scores available")
        print(f"  URL: https://alphafold.ebi.ac.uk/entry/{uniprot_id}")
        
        # Note about confidence regions
        print("\n  Confidence regions (typical for GATA3):")
        print("    - High confidence: Zinc finger domains (250-370)")
        print("    - Medium confidence: Linker regions")
        print("    - Low confidence: N- and C-terminal regions (disordered)")
    else:
        print("AlphaFold structure lookup failed - may be available online")
    
    # Known structural features
    print("\n## Known Structural Features:")
    print("-" * 40)
    
    features = get_gata3_structural_features()
    
    print("\n### Zinc Finger Domains:")
    for zf_name, zf_data in features['zinc_fingers'].items():
        print(f"\n{zf_name}:")
        for key, value in zf_data.items():
            print(f"  {key}: {value}")
    
    print("\n### Functional Regions:")
    for region_name, region_data in features['functional_regions'].items():
        print(f"\n{region_name}:")
        for key, value in region_data.items():
            print(f"  {key}: {value}")
    
    print("\n### DNA Recognition:")
    dna_rec = features['dna_recognition']
    print(f"  Consensus sequence: {dna_rec['consensus_sequence']}")
    print(f"  Expanded motif: {dna_rec['expanded_motif']}")
    print(f"  Binding mode: {dna_rec['binding_mode']}")
    print("  Specificity determinants:")
    for det in dna_rec['specificity_determinants']:
        print(f"    - {det}")
    
    # Structural insights
    print("\n## Structural Insights:")
    print("-" * 40)
    
    insights = [
        "1. Two C4-type zinc fingers are the key structural elements",
        "2. ZF1 (N-terminal) primarily determines DNA sequence specificity",
        "3. ZF2 (C-terminal) provides binding stability and affinity",
        "4. Both fingers insert into the major groove of DNA",
        "5. The linker between ZFs allows conformational flexibility",
        "6. N- and C-terminal regions are intrinsically disordered",
        "7. Disordered regions likely involved in protein-protein interactions",
        "8. DNA binding induces conformational changes in the protein"
    ]
    
    for i, insight in enumerate(insights, 1):
        print(f"{insight}")
    
    # Save results
    results = {
        'pdb_structures': structures if pdb_data else [],
        'alphafold_available': bool(af_data),
        'structural_features': features,
        'key_insights': insights
    }
    
    with open('structure_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n## Summary:")
    print("-" * 40)
    print(f"PDB structures found: {len(structures) if pdb_data else 0}")
    print(f"AlphaFold structure: {'Available' if af_data else 'Check online'}")
    print("Key structural elements: 2 zinc fingers, 2 TADs, flexible linkers")
    print("\nResults saved to structure_analysis_results.json")

if __name__ == "__main__":
    main()