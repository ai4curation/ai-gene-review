#!/usr/bin/env python3
"""
Protein interaction network analysis for GATA3
Fetches and analyzes validated protein-protein interactions
"""

import sys
import json
import requests
import pandas as pd
import networkx as nx
from collections import defaultdict

def fetch_string_interactions(protein_name="GATA3", species="9606", score_threshold=400):
    """Fetch protein interactions from STRING database"""
    
    # STRING API endpoint
    url = "https://string-db.org/api/json/network"
    
    params = {
        'identifiers': protein_name,
        'species': species,  # 9606 is human
        'caller_identity': 'gata3_analysis',
        'network_type': 'functional',
        'required_score': score_threshold,
        'add_nodes': 20  # Get top 20 interactors
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"STRING API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching STRING data: {e}")
        return []

def fetch_biogrid_interactions(gene_name="GATA3"):
    """Fetch interactions from BioGRID REST API"""
    
    # BioGRID REST API
    url = "https://webservice.thebiogrid.org/interactions"
    
    # Note: BioGRID requires access key - using limited public access
    params = {
        'searchNames': 'true',
        'geneList': gene_name,
        'organism': '9606',  # Human
        'searchbiogridids': 'false',
        'includeInteractors': 'true',
        'format': 'json',
        'accesskey': 'BIOGRIDKEY'  # Would need actual key for full access
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"BioGRID API not accessible without key")
            return {}
    except Exception as e:
        print(f"Note: BioGRID requires API key for full access")
        return {}

def analyze_interaction_network(interactions):
    """Analyze the protein interaction network"""
    
    if not interactions:
        return {}
    
    # Create network graph
    G = nx.Graph()
    
    interaction_counts = defaultdict(int)
    interaction_details = {}
    
    for interaction in interactions:
        protein1 = interaction.get('preferredName_A', '')
        protein2 = interaction.get('preferredName_B', '')
        score = interaction.get('score', 0)
        
        if protein1 and protein2:
            G.add_edge(protein1, protein2, weight=score)
            interaction_counts[protein2] += 1
            
            if protein2 not in interaction_details:
                interaction_details[protein2] = {
                    'score': score,
                    'evidence_types': []
                }
    
    # Calculate network metrics
    metrics = {}
    if G.number_of_nodes() > 0:
        # Get GATA3 node if present
        if 'GATA3' in G:
            metrics['gata3_degree'] = G.degree('GATA3')
            metrics['gata3_clustering'] = nx.clustering(G, 'GATA3')
            
            # Get direct neighbors
            metrics['direct_interactors'] = list(G.neighbors('GATA3'))
        
        metrics['total_nodes'] = G.number_of_nodes()
        metrics['total_edges'] = G.number_of_edges()
        metrics['network_density'] = nx.density(G)
    
    return {
        'network_metrics': metrics,
        'interaction_counts': dict(interaction_counts),
        'interaction_details': interaction_details
    }

def get_known_gata3_interactors():
    """Return literature-curated GATA3 interactors"""
    
    known_interactors = {
        'TBX21': {
            'name': 'T-bet',
            'function': 'Th1/Th2 cell fate antagonism',
            'evidence': 'Multiple studies show mutual inhibition'
        },
        'ZFPM1': {
            'name': 'FOG1',
            'function': 'Cofactor, modulates GATA3 activity',
            'evidence': 'Direct protein-protein interaction'
        },
        'ZFPM2': {
            'name': 'FOG2',
            'function': 'Cofactor, modulates GATA3 activity',
            'evidence': 'Direct protein-protein interaction'
        },
        'STAT6': {
            'name': 'STAT6',
            'function': 'Th2 differentiation cooperation',
            'evidence': 'Co-regulation of IL-4/IL-13 pathway'
        },
        'RUNX3': {
            'name': 'RUNX3',
            'function': 'T cell development',
            'evidence': 'Physical interaction in T cells'
        },
        'STAT5A': {
            'name': 'STAT5A',
            'function': 'Th2 cell maintenance',
            'evidence': 'Cooperative regulation'
        },
        'EP300': {
            'name': 'p300',
            'function': 'Histone acetyltransferase',
            'evidence': 'Transcriptional coactivator'
        },
        'CREBBP': {
            'name': 'CBP',
            'function': 'Histone acetyltransferase',
            'evidence': 'Transcriptional coactivator'
        }
    }
    
    return known_interactors

def main():
    print("GATA3 Protein Interaction Analysis")
    print("=" * 60)
    
    # Fetch STRING interactions
    print("\n## STRING Database Interactions:")
    print("-" * 40)
    
    string_interactions = fetch_string_interactions("GATA3", score_threshold=400)
    
    if string_interactions:
        print(f"Found {len(string_interactions)} high-confidence interactions")
        
        # Process and display top interactors
        interactor_scores = {}
        for interaction in string_interactions:
            proteinA = interaction.get('preferredName_A', '')
            proteinB = interaction.get('preferredName_B', '')
            score = interaction.get('score', 0)
            
            # Get the non-GATA3 protein
            interactor = proteinB if proteinA == 'GATA3' else proteinA
            if interactor and interactor != 'GATA3':
                interactor_scores[interactor] = score
        
        # Sort by score
        sorted_interactors = sorted(interactor_scores.items(), key=lambda x: x[1], reverse=True)
        
        print("\nTop STRING interactors (by confidence score):")
        for i, (protein, score) in enumerate(sorted_interactors[:15], 1):
            print(f"  {i}. {protein}: score = {score}")
    else:
        print("No STRING interactions found or API unavailable")
    
    # Literature-curated interactions
    print("\n## Literature-Curated Key Interactions:")
    print("-" * 40)
    
    known_interactors = get_known_gata3_interactors()
    
    for protein_id, details in known_interactors.items():
        print(f"\n{protein_id} ({details['name']}):")
        print(f"  Function: {details['function']}")
        print(f"  Evidence: {details['evidence']}")
    
    # Check overlap between STRING and known
    if string_interactions:
        string_proteins = set(interactor_scores.keys())
        known_proteins = set(known_interactors.keys())
        
        overlap = string_proteins.intersection(known_proteins)
        
        print("\n## Validation:")
        print("-" * 40)
        print(f"Known interactors found in STRING: {overlap}")
        print(f"STRING-specific interactors: {len(string_proteins - known_proteins)}")
        print(f"Literature-specific interactors: {len(known_proteins - string_proteins)}")
    
    # Analyze network properties
    if string_interactions:
        network_analysis = analyze_interaction_network(string_interactions)
        
        print("\n## Network Properties:")
        print("-" * 40)
        metrics = network_analysis.get('network_metrics', {})
        for key, value in metrics.items():
            print(f"  {key}: {value}")
    
    # Functional categories of interactors
    print("\n## Functional Categories of Interactors:")
    print("-" * 40)
    
    categories = {
        'Transcription factors': ['TBX21', 'STAT6', 'STAT5A', 'RUNX3', 'MAF', 'RORC'],
        'Cofactors': ['ZFPM1', 'ZFPM2', 'EP300', 'CREBBP'],
        'Chromatin modifiers': ['EP300', 'CREBBP', 'HDAC1', 'HDAC2'],
        'Signaling proteins': ['STAT6', 'STAT5A', 'STAT5B'],
        'Cell cycle/Development': ['CDK1', 'CCNA2', 'PCNA']
    }
    
    for category, proteins in categories.items():
        found = []
        if string_interactions:
            for p in proteins:
                if p in interactor_scores or p in known_interactors:
                    found.append(p)
        else:
            found = [p for p in proteins if p in known_interactors]
        
        if found:
            print(f"\n{category}:")
            print(f"  {', '.join(found)}")
    
    # Save results
    results = {
        'string_interactors': interactor_scores if string_interactions else {},
        'known_interactors': known_interactors,
        'network_analysis': network_analysis if string_interactions else {},
        'functional_categories': categories
    }
    
    with open('interaction_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n## Summary:")
    print("-" * 40)
    print(f"Total unique interactors identified: {len(set(list(interactor_scores.keys()) + list(known_interactors.keys()))) if string_interactions else len(known_interactors)}")
    print(f"High-confidence STRING interactions: {len(interactor_scores) if string_interactions else 0}")
    print(f"Literature-documented interactions: {len(known_interactors)}")
    print("\nResults saved to interaction_analysis_results.json")

if __name__ == "__main__":
    main()