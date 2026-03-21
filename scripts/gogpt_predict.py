#!/usr/bin/env python3
"""
Run GO-GPT predictions on an AIGR gene and output PredictionReview YAML.

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
from datetime import datetime, timezone
from pathlib import Path

import torch
import yaml


# Root/generic GO terms to filter out
GENERIC_TERMS = {
    'GO:0003674', 'GO:0008150', 'GO:0005575',  # roots
    'GO:0005488', 'GO:0009987', 'GO:0008152',  # very generic
    'GO:0044237', 'GO:0071704', 'GO:0044238',
    'GO:0006807', 'GO:0044260', 'GO:0043170',
    'GO:0097159', 'GO:1901363',
}

ASPECT_MAP = {
    'MF': 'GO_MF',
    'BP': 'GO_BP',
    'CC': 'GO_CC',
}

ASPECT_FULL = {
    'MF': 'molecular_function',
    'BP': 'biological_process',
    'CC': 'cellular_component',
}


def get_organism_name(organism_code: str, organism_mapper) -> str:
    """Map AIGR organism code to GO-GPT organism name."""
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


def extract_accession(uniprot_file: Path) -> str:
    """Extract UniProt accession from flat file."""
    for line in uniprot_file.read_text().splitlines():
        if line.startswith('AC'):
            return line.split()[1].rstrip(';')
    return ''


def load_review_terms(review_file: Path) -> dict:
    """Load GO terms from an AIGR review YAML, organized by aspect."""
    with open(review_file) as f:
        review = yaml.safe_load(f)

    terms = {'MF': set(), 'BP': set(), 'CC': set()}

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

    return terms


def load_go_cache(output_dir: Path) -> dict:
    """Load GO term labels from cache."""
    cache_file = output_dir / 'cache' / 'go' / 'terms.csv'
    labels = {}
    if cache_file.exists():
        for line in cache_file.read_text().splitlines():
            parts = line.split(',', 2)
            if len(parts) >= 2 and parts[0].startswith('GO:'):
                labels[parts[0]] = parts[1]
    return labels


def assess_prediction(go_id: str, aspect: str, curated_terms: dict) -> str:
    """Auto-assess a GO-GPT prediction against curated review terms.
    
    Returns assessment code: CNN, LSP, UNC
    """
    aspect_terms = curated_terms.get(aspect, set())
    
    if go_id in aspect_terms:
        return 'CNN'  # Correct but Not Novel
    
    # Check all aspects for the term (might be mis-classified aspect)
    for a, terms in curated_terms.items():
        if go_id in terms:
            return 'CNN'
    
    # For now, anything not in the review is UNC
    # A proper implementation would check GO hierarchy for ancestor relationships
    return 'UNC'


def build_prediction_review_yaml(
    gene: str,
    organism: str,
    accession: str,
    predictions: dict,
    curated_terms: dict | None,
    go_labels: dict,
    seq_length: int,
) -> dict:
    """Build a PredictionReview YAML document."""
    
    predicted_annotations = []
    
    for aspect in ['MF', 'BP', 'CC']:
        terms = predictions.get(aspect, [])
        for go_id in terms:
            if go_id in GENERIC_TERMS:
                continue
            
            label = go_labels.get(go_id, 'Unknown')
            
            # Auto-assess if we have curated review
            if curated_terms:
                assessment = assess_prediction(go_id, aspect, curated_terms)
            else:
                assessment = 'UNC'
            
            confidence = 2 if assessment == 'CNN' else 1
            
            if assessment == 'CNN':
                summary = f"GO-GPT correctly predicted this term, which is already in the curated review."
            elif assessment == 'LSP':
                summary = f"GO-GPT predicted a less specific ancestor term. The curated review has more precise annotations."
            else:
                summary = f"GO-GPT prediction not found in curated review. Requires manual assessment."
            
            predicted_annotations.append({
                'source_method': 'GO-GPT',
                'source_version': 'wanglab/gogpt',
                'source_reference_id': 'doi:10.64898/2026.03.19.712954',
                'predicted_term': {
                    'id': go_id,
                    'label': label,
                },
                'predicted_term_type': ASPECT_MAP[aspect],
                'review': {
                    'assessment': assessment,
                    'confidence_score': confidence,
                    'summary': summary,
                },
            })
    
    # Count assessments
    assessment_counts = {}
    for pa in predicted_annotations:
        a = pa['review']['assessment']
        assessment_counts[a] = assessment_counts.get(a, 0) + 1
    
    has_review = curated_terms is not None
    total_specific = len(predicted_annotations)
    
    description = (
        f"GO-GPT (BioReason-Pro) predictions for {gene} ({organism}). "
        f"Model predicted {sum(len(v) for v in predictions.values())} total GO terms, "
        f"{total_specific} specific (after filtering root/generic terms). "
    )
    if has_review:
        description += (
            f"Auto-compared against curated AIGR review: "
            f"{assessment_counts.get('CNN', 0)} correct-not-novel, "
            f"{assessment_counts.get('LSP', 0)} less-precise, "
            f"{assessment_counts.get('UNC', 0)} uncertain/novel."
        )
    
    doc = {
        'id': accession,
        'gene_symbol': gene,
        'taxon': {
            'id': f'uniprot:{organism}',
            'label': organism,
        },
        'status': 'DRAFT' if not has_review else 'COMPLETE',
        'description': description,
        'references': [
            {
                'id': 'doi:10.64898/2026.03.19.712954',
                'title': 'BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning (Fallahpour et al. 2026)',
            },
        ],
        'predictions': predicted_annotations,
    }
    
    return doc


def load_predictor(model_dir: Path):
    """Load GO-GPT predictor from local model directory."""
    import sys
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
    
    return predictor


def main():
    parser = argparse.ArgumentParser(description='Run GO-GPT on an AIGR gene')
    parser.add_argument('organism', help='Organism code (human, yeast, PSEPK, etc.)')
    parser.add_argument('gene', help='Gene symbol')
    parser.add_argument('--compare', action='store_true', help='Compare with curated review')
    parser.add_argument('--output-dir', default='.', help='Output directory (default: .)')
    parser.add_argument('--model-dir', default=os.path.expanduser('~/repos/BioReason-Pro/models/gogpt'),
                        help='Path to GO-GPT model directory')
    parser.add_argument('--format', choices=['yaml', 'json', 'both'], default='yaml',
                        help='Output format (default: yaml)')
    args = parser.parse_args()

    gene_dir = Path(args.output_dir) / 'genes' / args.organism / args.gene
    uniprot_file = gene_dir / f'{args.gene}-uniprot.txt'

    if not uniprot_file.exists():
        print(f"❌ No UniProt file: {uniprot_file}")
        sys.exit(1)

    seq = extract_sequence(uniprot_file)
    if not seq:
        print(f"❌ Could not extract sequence from {uniprot_file}")
        sys.exit(1)

    accession = extract_accession(uniprot_file)

    if len(seq) > 2000:
        print(f"⚠️  Truncating sequence from {len(seq)} to 2000 aa (ESM limit)")
        seq = seq[:2000]

    # Load GO-GPT
    model_dir = Path(args.model_dir)
    predictor = load_predictor(model_dir)
    organism_name = get_organism_name(args.organism, predictor.organism_mapper)

    print(f"🧬 GO-GPT prediction for {args.gene} ({args.organism})")
    print(f"   Organism: {organism_name}")
    print(f"   Sequence: {len(seq)} aa")
    print(f"   Device: {predictor.device}")
    print()

    result = predictor.predict(sequence=seq, organism=organism_name)

    # Load GO term labels
    go_labels = load_go_cache(Path(args.output_dir))

    # Print raw predictions
    print("GO-GPT Predictions:")
    for aspect in ['MF', 'BP', 'CC']:
        terms = result.get(aspect, [])
        specific = [t for t in terms if t not in GENERIC_TERMS]
        print(f"  {aspect} ({len(terms)} total, {len(specific)} specific): {', '.join(specific) if specific else '(only generic terms)'}")

    # Load curated review if --compare
    curated_terms = None
    if args.compare:
        review_file = gene_dir / f'{args.gene}-ai-review.yaml'
        if review_file.exists():
            curated_terms = load_review_terms(review_file)
            print(f"\n📊 Comparing against curated review...")
        else:
            print(f"\n⚠️  No review file: {review_file}")

    # Build PredictionReview YAML
    doc = build_prediction_review_yaml(
        gene=args.gene,
        organism=args.organism,
        accession=accession,
        predictions=result,
        curated_terms=curated_terms,
        go_labels=go_labels,
        seq_length=len(seq),
    )

    # Write YAML
    if args.format in ('yaml', 'both'):
        yaml_file = gene_dir / f'{args.gene}-gogpt-predictions.yaml'
        with open(yaml_file, 'w') as f:
            yaml.dump(doc, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=100)
        print(f"\n📄 Saved YAML: {yaml_file}")

    # Write JSON
    if args.format in ('json', 'both'):
        json_file = gene_dir / f'{args.gene}-gogpt-predictions.json'
        json_file.write_text(json.dumps(doc, indent=2))
        print(f"📄 Saved JSON: {json_file}")

    # Print comparison summary
    if curated_terms:
        assessments = [p['review']['assessment'] for p in doc['predictions']]
        print(f"\n📊 Assessment summary:")
        print(f"  CNN (correct, not novel): {assessments.count('CNN')}")
        print(f"  LSP (less precise): {assessments.count('LSP')}")
        print(f"  UNC (uncertain/novel): {assessments.count('UNC')}")


if __name__ == '__main__':
    main()
