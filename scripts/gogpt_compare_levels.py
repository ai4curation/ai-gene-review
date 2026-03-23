#!/usr/bin/env python3
"""Compare GO-GPT predictions at three levels against AIGR reviews."""
import json, sys, os, yaml, csv
from pathlib import Path
from collections import defaultdict

REPO = Path(os.path.expanduser('~/repos/ai-gene-review'))

GENERIC_TERMS = {
    'GO:0003674', 'GO:0008150', 'GO:0005575',
    'GO:0005488', 'GO:0009987', 'GO:0008152',
    'GO:0044237', 'GO:0071704', 'GO:0044238',
    'GO:0006807', 'GO:0044260', 'GO:0043170',
    'GO:0097159', 'GO:1901363',
}

def get_goa_terms(goa_file):
    """Level 1: All terms from the original GOA file."""
    terms = set()
    if not goa_file.exists():
        return terms
    with open(goa_file) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) > 4 and parts[4].startswith('GO:'):
                terms.add(parts[4])
    return terms

def get_post_review_terms(review_file):
    """Level 2: All terms after review (accepted + new, excluding removed)."""
    with open(review_file) as f:
        review = yaml.safe_load(f)
    
    terms = set()
    # Existing annotations that were ACCEPTED or kept
    for ann in review.get('existing_annotations', []):
        action = ann.get('review', {}).get('action', '')
        if action in ('ACCEPT', 'KEEP_AS_NON_CORE', 'MODIFY', 'UNDECIDED', ''):
            go_id = ann.get('term', {}).get('id', '')
            if go_id.startswith('GO:'):
                terms.add(go_id)
    
    # New annotations
    for ann in review.get('new_annotations', []):
        go_id = ann.get('term', {}).get('id', '')
        if go_id.startswith('GO:'):
            terms.add(go_id)
    
    # Core functions
    for cf in review.get('core_functions', []):
        mf = cf.get('molecular_function', {})
        if mf and mf.get('id', '').startswith('GO:'):
            terms.add(mf['id'])
        for bp in cf.get('directly_involved_in', []):
            if bp.get('id', '').startswith('GO:'):
                terms.add(bp['id'])
        for cc in cf.get('occurs_in', []):
            if cc.get('id', '').startswith('GO:'):
                terms.add(cc['id'])
    
    return terms

def get_core_terms(review_file):
    """Level 3: Only core_functions terms."""
    with open(review_file) as f:
        review = yaml.safe_load(f)
    
    terms = set()
    for cf in review.get('core_functions', []):
        mf = cf.get('molecular_function', {})
        if mf and mf.get('id', '').startswith('GO:'):
            terms.add(mf['id'])
        for bp in cf.get('directly_involved_in', []):
            if bp.get('id', '').startswith('GO:'):
                terms.add(bp['id'])
        for cc in cf.get('occurs_in', []):
            if cc.get('id', '').startswith('GO:'):
                terms.add(cc['id'])
    
    return terms

def main():
    # Load GO-GPT predictions from batch results
    batch_file = REPO / 'reports' / 'gogpt-comparison.json'
    if not batch_file.exists():
        print("No batch results yet")
        return
    
    batch_data = json.load(open(batch_file))
    
    # Group predictions by gene
    gene_preds = defaultdict(set)
    for r in batch_data:
        key = (r['organism'], r['gene'])
        for t in r.get('pred_only', []):
            gene_preds[key].add(t)
        for t in r.get('overlap_terms', []):
            gene_preds[key].add(t)
    
    stats = {'goa': {'overlap': 0, 'total': 0, 'pred': 0},
             'post_review': {'overlap': 0, 'total': 0, 'pred': 0},
             'core': {'overlap': 0, 'total': 0, 'pred': 0}}
    
    gene_details = []
    
    for (org, gene), preds in sorted(gene_preds.items()):
        specific_preds = preds - GENERIC_TERMS
        if not specific_preds:
            continue
        
        gene_dir = REPO / 'genes' / org / gene
        goa_file = gene_dir / f'{gene}-goa.tsv'
        review_file = gene_dir / f'{gene}-ai-review.yaml'
        
        if not review_file.exists():
            continue
        
        goa_terms = get_goa_terms(goa_file)
        post_review = get_post_review_terms(review_file)
        core_terms = get_core_terms(review_file)
        
        goa_ov = specific_preds & goa_terms
        pr_ov = specific_preds & post_review
        core_ov = specific_preds & core_terms
        
        stats['goa']['overlap'] += len(goa_ov)
        stats['goa']['total'] += len(goa_terms)
        stats['goa']['pred'] += len(specific_preds)
        
        stats['post_review']['overlap'] += len(pr_ov)
        stats['post_review']['total'] += len(post_review)
        stats['post_review']['pred'] += len(specific_preds)
        
        stats['core']['overlap'] += len(core_ov)
        stats['core']['total'] += len(core_terms)
        stats['core']['pred'] += len(specific_preds)
        
        gene_details.append({
            'organism': org, 'gene': gene,
            'preds': len(specific_preds),
            'goa_terms': len(goa_terms), 'goa_overlap': len(goa_ov),
            'post_review_terms': len(post_review), 'post_review_overlap': len(pr_ov),
            'core_terms': len(core_terms), 'core_overlap': len(core_ov),
            'goa_overlap_terms': list(goa_ov),
            'core_overlap_terms': list(core_ov),
        })
    
    print(f"Genes analyzed: {len(gene_details)}")
    print()
    print(f"{'Level':<20} {'Overlap':>8} {'/ Reference':>12} {'Rate':>8} {'/ Predicted':>12} {'Precision':>10}")
    for level in ['goa', 'post_review', 'core']:
        s = stats[level]
        recall = s['overlap']*100/max(s['total'],1)
        precision = s['overlap']*100/max(s['pred'],1)
        label = {'goa': 'vs GOA', 'post_review': 'vs Post-Review', 'core': 'vs Core Functions'}[level]
        print(f"{label:<20} {s['overlap']:>8} {s['total']:>12} {recall:>7.1f}% {s['pred']:>12} {precision:>9.1f}%")
    
    print()
    print("=== TOP GENES BY GOA OVERLAP ===")
    for g in sorted(gene_details, key=lambda x: -x['goa_overlap'])[:10]:
        print(f"  {g['organism']}/{g['gene']}: {g['goa_overlap']}/{g['goa_terms']} GOA overlap, {g['core_overlap']}/{g['core_terms']} core overlap")
    
    # Save detailed results
    out = REPO / 'reports' / 'gogpt-comparison-levels.json'
    json.dump(gene_details, open(out, 'w'), indent=2)
    print(f"\nSaved to {out}")

if __name__ == '__main__':
    main()
