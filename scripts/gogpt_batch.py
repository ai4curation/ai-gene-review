#!/usr/bin/env python3
"""Batch GO-GPT predictions — loads model once, clears memory between genes."""
import json, sys, os, yaml, gc
from pathlib import Path
from datetime import datetime

import torch

REPO = Path(os.environ.get('AIGR_DIR', os.path.expanduser('~/repos/ai-gene-review')))
MODEL_DIR = Path(os.path.expanduser('~/repos/BioReason-Pro/models/gogpt'))
sys.path.insert(0, str(Path.home() / 'repos/BioReason-Pro/gogpt/src'))

GENERIC_TERMS = {
    'GO:0003674', 'GO:0008150', 'GO:0005575',
    'GO:0005488', 'GO:0009987', 'GO:0008152',
    'GO:0044237', 'GO:0071704', 'GO:0044238',
    'GO:0006807', 'GO:0044260', 'GO:0043170',
    'GO:0097159', 'GO:1901363',
}

ORG_MAP = {
    'human': 'Homo sapiens',
    'mouse': 'Mus musculus',
    'rat': 'Rattus norvegicus',
    'yeast': 'Saccharomyces cerevisiae (strain ATCC 204508 / S288c)',
    'worm': 'Caenorhabditis elegans',
    'DROME': 'Drosophila melanogaster',
    'ARATH': 'Arabidopsis thaliana',
    'PSEPK': 'Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)',
    'ECOLI': 'Escherichia coli (strain K12)',
}

def extract_sequence(uniprot_file):
    lines = uniprot_file.read_text().splitlines()
    in_seq = False; seq = []
    for line in lines:
        if line.startswith('SQ'): in_seq = True; continue
        if in_seq:
            if line.startswith('//'): break
            seq.append(line.strip().replace(' ', ''))
    return ''.join(seq)

def load_review_terms(review_file):
    with open(review_file) as f:
        review = yaml.safe_load(f)
    terms = {'MF': set(), 'BP': set(), 'CC': set()}
    for ann in review.get('existing_annotations', []):
        t = ann.get('term', {})
        go_id = t.get('id', '')
        if go_id.startswith('GO:'):
            a = ann.get('aspect', '')
            if 'molecular' in a: terms['MF'].add(go_id)
            elif 'biological' in a: terms['BP'].add(go_id)
            elif 'cellular' in a: terms['CC'].add(go_id)
    for cf in review.get('core_functions', []):
        mf = cf.get('molecular_function', {})
        if mf and mf.get('id', '').startswith('GO:'): terms['MF'].add(mf['id'])
        for bp in cf.get('directly_involved_in', []):
            if bp.get('id', '').startswith('GO:'): terms['BP'].add(bp['id'])
    return terms

def main():
    from gogpt.inference import GOGPTPredictor, GOTokenizerJSON, OrganismMapperJSON
    from transformers import AutoTokenizer
    
    print(f"Loading GO-GPT model...", flush=True)
    predictor = object.__new__(GOGPTPredictor)
    predictor.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    predictor.verbose = False
    predictor.config_path = str(MODEL_DIR / 'config.yaml')
    predictor._embed_model_path = 'facebook/esm2_t36_3B_UR50D'
    with open(MODEL_DIR / 'tokenizer_info.json') as f:
        predictor.tokenizer_info = json.load(f)
    predictor.go_tokenizer = GOTokenizerJSON.from_json(MODEL_DIR / 'go_tokenizer.json')
    predictor.organism_mapper = OrganismMapperJSON.from_json(MODEL_DIR / 'organism_mapper.json')
    predictor.protein_tokenizer = AutoTokenizer.from_pretrained('facebook/esm2_t36_3B_UR50D')
    predictor._load_model(str(MODEL_DIR / 'model.ckpt'))
    print(f"Model loaded on {predictor.device}", flush=True)
    
    genes = []
    for review_file in sorted(REPO.glob('genes/**/*-ai-review.yaml')):
        gene_dir = review_file.parent
        gene = gene_dir.name
        org = gene_dir.parent.name
        uniprot = gene_dir / f'{gene}-uniprot.txt'
        if uniprot.exists():
            genes.append((org, gene, uniprot, review_file))
    
    print(f"Found {len(genes)} genes to process", flush=True)
    
    results = []
    for i, (org, gene, uniprot, review_file) in enumerate(genes):
        try:
            seq = extract_sequence(uniprot)
            if not seq or len(seq) < 10:
                continue
            if len(seq) > 2000:
                seq = seq[:2000]
            
            org_name = ORG_MAP.get(org, org)
            if org_name == org:
                for name in predictor.organism_mapper.organism_to_idx:
                    if org.lower() in name.lower():
                        org_name = name
                        break
            
            with torch.no_grad():
                preds = predictor.predict(sequence=seq, organism=org_name)
            
            review_terms = load_review_terms(review_file)
            
            for aspect in ['MF', 'BP', 'CC']:
                pred_set = set(preds.get(aspect, [])) - GENERIC_TERMS
                rev_set = review_terms.get(aspect, set())
                overlap = pred_set & rev_set
                results.append({
                    'organism': org, 'gene': gene, 'aspect': aspect,
                    'predicted': len(pred_set), 'reviewed': len(rev_set),
                    'overlap': len(overlap), 'overlap_terms': list(overlap),
                    'pred_only': list(pred_set - rev_set),
                    'rev_only': list(rev_set - pred_set),
                })
            
            # Memory cleanup every gene
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
            gc.collect()
            
            if (i + 1) % 10 == 0:
                print(f"  [{i+1}/{len(genes)}] {org}/{gene} done", flush=True)
                # Save intermediate results every 50
                if (i + 1) % 50 == 0:
                    out = REPO / 'reports' / 'gogpt-comparison.json'
                    out.parent.mkdir(exist_ok=True)
                    with open(out, 'w') as f:
                        json.dump(results, f, indent=2)
        
        except Exception as e:
            print(f"  ERROR {org}/{gene}: {e}", flush=True)
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
            gc.collect()
    
    out = REPO / 'reports' / 'gogpt-comparison.json'
    out.parent.mkdir(exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    
    total_overlap = sum(r['overlap'] for r in results)
    total_pred = sum(r['predicted'] for r in results)
    total_rev = sum(r['reviewed'] for r in results)
    genes_done = len(set((r['organism'], r['gene']) for r in results))
    
    print(f"\n=== SUMMARY ===")
    print(f"Genes processed: {genes_done}")
    print(f"Total predicted (specific): {total_pred}")
    print(f"Total in reviews: {total_rev}")
    print(f"Exact overlap: {total_overlap}")
    print(f"Overlap rate: {total_overlap*100/max(total_rev,1):.1f}% of review terms predicted")
    print(f"Results saved to {out}")

if __name__ == '__main__':
    main()
