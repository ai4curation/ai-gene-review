#!/usr/bin/env python3
"""
Run GO-GPT predictions on an AIGR gene and optionally compare with curated review.

Usage:
    python scripts/gogpt_predict.py <organism> <gene> [--compare] [--output-dir .]
    
Examples:
    python scripts/gogpt_predict.py human TP53
    python scripts/gogpt_predict.py human TP53 --compare
    python scripts/gogpt_predict.py PSEPK rpoS --compare
"""
import argparse
import json
import sys
import os
from pathlib import Path

import torch
import yaml


def get_organism_name(organism_code: str, organism_mapper) -> str:
    """Map AIGR organism code to GO-GPT organism name."""
    # Try exact matches in organism mapper
    code_map = {
        'human': 'Homo sapiens',
        'mouse': 'Mus musculus',
        'rat': 'Rattus norvegicus',
        'yeast': 'Saccharomyces cerevisiae (strain ATCC 204508 / S288c)',
        'worm': 'Caenorhabditis elegans',
        'DROME': 'Drosophila melanogaster',
        'ARATH': 'Arabidopsis thaliana',
        'PSEPK': 'Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)',
        'ECOLI': 'Escherichia coli (strain K12)',
        'PSEAE': 'Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)',
        'BACSU': 'Bacillus subtilis (strain 168)',
    }
    if organism_code in code_map:
        return code_map[organism_code]
    
    # Try to find in organism mapper
    for name in organism_mapper.organism_to_idx:
        if organism_code.lower() in name.lower():
            return name
    
    return organism_code


def extract_sequence(uniprot_file: Path) -> str:
    """Extract protein sequence from UniProt flat file."""
    lines = uniprot_file.read_text().splitlines()
    in_seq = False
    seq = []
    for line in lines:
        if line.startswith('SQ'):
            in_seq = True
            continue
        if in_seq:
            if line.startswith('//'):
                break
            seq.append(line.strip().replace(' ', ''))
    return ''.join(seq)


def load_review_terms(review_file: Path) -> dict:
    """Load GO terms from an AIGR review YAML."""
    with open(review_file) as f:
        review = yaml.safe_load(f)
    
    terms = {'MF': set(), 'BP': set(), 'CC': set()}
    
    # Get from existing_annotations
    for ann in review.get('existing_annotations', []):
        term = ann.get('term', {})
        go_id = term.get('id', '')
        if go_id.startswith('GO:'):
            aspect = ann.get('aspect', '')
            if aspect == 'molecular_function':
                terms['MF'].add(go_id)
            elif aspect == 'biological_process':
                terms['BP'].add(go_id)
            elif aspect == 'cellular_component':
                terms['CC'].add(go_id)
    
    # Get from new_annotations
    for ann in review.get('new_annotations', []):
        term = ann.get('term', {})
        go_id = term.get('id', '')
        if go_id.startswith('GO:'):
            aspect = ann.get('aspect', '')
            if aspect == 'molecular_function':
                terms['MF'].add(go_id)
            elif aspect == 'biological_process':
                terms['BP'].add(go_id)
            elif aspect == 'cellular_component':
                terms['CC'].add(go_id)
    
    # Get from core_functions
    for cf in review.get('core_functions', []):
        mf = cf.get('molecular_function', {})
        if mf and mf.get('id', '').startswith('GO:'):
            terms['MF'].add(mf['id'])
        for bp in cf.get('directly_involved_in', []):
            if bp.get('id', '').startswith('GO:'):
                terms['BP'].add(bp['id'])
        for cc in cf.get('occurs_in', []):
            if cc.get('id', '').startswith('GO:'):
                terms['CC'].add(cc['id'])
    
    return {k: v for k, v in terms.items()}


def main():
    parser = argparse.ArgumentParser(description='Run GO-GPT on an AIGR gene')
    parser.add_argument('organism', help='Organism code (human, yeast, PSEPK, etc.)')
    parser.add_argument('gene', help='Gene symbol')
    parser.add_argument('--compare', action='store_true', help='Compare with curated review')
    parser.add_argument('--output-dir', default='.', help='Output directory (default: .)')
    parser.add_argument('--model-dir', default=os.path.expanduser('~/repos/BioReason-Pro/models/gogpt'),
                        help='Path to GO-GPT model directory')
    args = parser.parse_args()
    
    # Find gene files
    gene_dir = Path(args.output_dir) / 'genes' / args.organism / args.gene
    uniprot_file = gene_dir / f'{args.gene}-uniprot.txt'
    
    if not uniprot_file.exists():
        print(f"❌ No UniProt file: {uniprot_file}")
        sys.exit(1)
    
    seq = extract_sequence(uniprot_file)
    if not seq:
        print(f"❌ Could not extract sequence from {uniprot_file}")
        sys.exit(1)
    
    if len(seq) > 2000:
        print(f"⚠️  Truncating sequence from {len(seq)} to 2000 aa (ESM limit)")
        seq = seq[:2000]
    
    # Load GO-GPT
    model_dir = Path(args.model_dir)
    sys.path.insert(0, str(Path.home() / 'repos/BioReason-Pro/gogpt/src'))
    from gogpt.inference import GOGPTPredictor, GOTokenizerJSON, OrganismMapperJSON
    from transformers import AutoTokenizer
    
    predictor = object.__new__(GOGPTPredictor)
    predictor.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    predictor.verbose = False
    predictor.config_path = str(model_dir / 'config.yaml')
    predictor._embed_model_path = 'facebook/esm2_t36_3B_UR50D'
    
    with open(model_dir / 'tokenizer_info.json') as f:
        predictor.tokenizer_info = json.load(f)
    predictor.go_tokenizer = GOTokenizerJSON.from_json(model_dir / 'go_tokenizer.json')
    predictor.organism_mapper = OrganismMapperJSON.from_json(model_dir / 'organism_mapper.json')
    predictor.protein_tokenizer = AutoTokenizer.from_pretrained('facebook/esm2_t36_3B_UR50D')
    predictor._load_model(str(model_dir / 'model.ckpt'))
    
    organism_name = get_organism_name(args.organism, predictor.organism_mapper)
    print(f"🧬 GO-GPT prediction for {args.gene} ({args.organism})")
    print(f"   Organism: {organism_name}")
    print(f"   Sequence: {len(seq)} aa")
    print(f"   Device: {predictor.device}")
    print()
    
    result = predictor.predict(sequence=seq, organism=organism_name)
    
    # Root/generic GO terms to filter
    generic = {
        'GO:0003674', 'GO:0008150', 'GO:0005575',
        'GO:0005488', 'GO:0009987', 'GO:0008152',
        'GO:0044237', 'GO:0071704', 'GO:0044238',
        'GO:0006807', 'GO:0044260', 'GO:0043170',
        'GO:0097159', 'GO:1901363',
    }
    
    print("GO-GPT Predictions:")
    for aspect in ['MF', 'BP', 'CC']:
        terms = result.get(aspect, [])
        specific = [t for t in terms if t not in generic]
        all_str = ', '.join(terms)
        spec_str = ', '.join(specific) if specific else '(only generic terms)'
        print(f"  {aspect} (all {len(terms)}): {all_str}")
        print(f"  {aspect} (specific): {spec_str}")
    
    # Save predictions
    output_file = gene_dir / f'{args.gene}-gogpt-predictions.json'
    output_data = {
        'gene': args.gene,
        'organism': args.organism,
        'organism_full': organism_name,
        'sequence_length': len(seq),
        'predictions': result,
        'model': 'wanglab/gogpt',
    }
    output_file.write_text(json.dumps(output_data, indent=2))
    print(f"\n📄 Saved to {output_file}")
    
    # Compare with curated review
    if args.compare:
        review_file = gene_dir / f'{args.gene}-ai-review.yaml'
        if review_file.exists():
            curated = load_review_terms(review_file)
            print(f"\n📊 Comparison with curated review:")
            for aspect in ['MF', 'BP', 'CC']:
                predicted = set(result.get(aspect, []))
                reviewed = curated.get(aspect, set())
                overlap = predicted & reviewed
                predicted_only = predicted - reviewed - generic
                reviewed_only = reviewed - predicted
                print(f"\n  {aspect}:")
                print(f"    Overlap: {', '.join(overlap) if overlap else 'none'}")
                print(f"    GO-GPT only (specific): {', '.join(predicted_only) if predicted_only else 'none'}")
                print(f"    Review only: {', '.join(reviewed_only) if reviewed_only else 'none'}")
        else:
            print(f"\n⚠️  No review file found: {review_file}")


if __name__ == '__main__':
    main()
