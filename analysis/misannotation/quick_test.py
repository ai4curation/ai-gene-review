#!/usr/bin/env python3
"""
Quick test of misannotation analysis without BLAST (for development/testing).
"""

import argparse
import json
from pathlib import Path
from sequence_similarity_analyzer import SequenceSimilarityAnalyzer

def quick_test_gene(gene_dir: Path):
    """Quick test of a single gene without BLAST."""
    analyzer = SequenceSimilarityAnalyzer()

    # Find the YAML file
    yaml_files = list(gene_dir.glob("*-ai-review.yaml"))
    if not yaml_files:
        print(f"No YAML file found in {gene_dir}")
        return None

    yaml_file = yaml_files[0]

    try:
        import yaml
        with open(yaml_file) as f:
            gene_data = yaml.safe_load(f)

        uniprot_id = gene_data.get('id', '')
        gene_symbol = gene_data.get('gene_symbol', '')

        # Extract GO terms
        go_terms = []
        if 'existing_annotations' in gene_data:
            for annotation in gene_data['existing_annotations']:
                if 'term' in annotation and 'id' in annotation['term']:
                    go_terms.append(annotation['term']['id'])

        print(f"Gene: {gene_symbol} ({uniprot_id})")
        print(f"GO terms: {len(go_terms)}")
        print(f"GO terms: {go_terms[:5]}..." if len(go_terms) > 5 else f"GO terms: {go_terms}")

        # Get sequence (this should work)
        sequence = analyzer.get_uniprot_sequence(uniprot_id)
        if sequence:
            print(f"Sequence length: {len(sequence)} amino acids")
            print(f"Sequence preview: {sequence[:50]}...")
        else:
            print("Could not retrieve sequence")

        return {
            'gene_symbol': gene_symbol,
            'uniprot_id': uniprot_id,
            'go_term_count': len(go_terms),
            'sequence_length': len(sequence) if sequence else 0,
            'status': 'success' if sequence else 'no_sequence'
        }

    except Exception as e:
        print(f"Error analyzing {yaml_file}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Quick test of misannotation analysis")
    parser.add_argument("gene_dir", type=Path, help="Path to single gene directory")

    args = parser.parse_args()

    if not args.gene_dir.exists():
        print(f"Directory not found: {args.gene_dir}")
        return

    result = quick_test_gene(args.gene_dir)

    if result:
        output_file = Path("quick_test_result.json")
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\nResult saved to: {output_file}")

if __name__ == "__main__":
    main()