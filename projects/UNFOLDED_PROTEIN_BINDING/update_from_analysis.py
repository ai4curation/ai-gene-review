#!/usr/bin/env python3
"""
Update spreadsheet with manual curation recommendations from publication analysis.
"""

import csv
from pathlib import Path

# File path
tsv_file = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING/5974 Review annotations to GO_0031249 denatured protein binding GO_0051082 unfolded protein binding - Sheet1_FILLED.tsv')

# Read TSV
rows = []
with open(tsv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    rows = list(reader)

# Recommendations based on PMID analysis
recommendations = {
    'AIPL1_10615133': 'DELETE (false annotation: AIPL1 is AhR-interacting protein, not chaperone)',
    'cct_yeast_16762366': 'GO:0044183 (protein folding chaperone) [ATP-dependent - see PMID:16762366]',
    'HSPA5_14685163': 'GO:0044183 (protein folding chaperone) [ER chaperone - see PMID:14685163]',
    
    # 8 additional recommendations from analysis
    'HSPA1A_16130169': 'GO:0044183 (protein folding chaperone) [ER stress response - see PMID:16130169]',
    'lsc_yeast_16873065': 'GO:0140309 (unfolded protein holdase activity) [ER surveillance complex - see PMID:16873065]',
    'HSPA5_22013210': 'GO:0044183 (protein folding chaperone) [ER chaperone in UPR - see PMID:22013210]',
    'btt1_26618777': 'GO:0044183 (protein folding chaperone) [NAC cotranslational folding - see PMID:26618777]',
    'btt1-egd2_yeast_26618777': 'GO:0044183 (protein folding chaperone) [NAC cotranslational folding - see PMID:26618777]',
    'gimc_yeast_9463374': 'GO:0044183 (protein folding chaperone) [GIM prefoldin tubulin folding - see PMID:9463374]',
    'SSB2_9670014': 'GO:0044183 (protein folding chaperone) [Hsp70 nascent chain binding - see PMID:9670014]',
    'rac_yeast_11274393': 'GO:0044183 (protein folding chaperone) [RAC nascent chain folding - see PMID:11274393]',
    'Hsp90aa1_12855682': 'MODIFY (HSP90 is co-chaperone/client protein binder, not foldase - see PMID:12855682)',
}

# Track updates
updated = {}

# Process rows
for i, row in enumerate(rows):
    gene_symbol = row.get('bioentity_label', '').strip()
    reference = row.get('reference', '').strip()
    current_rec = row.get('Suggested action (by annotation review requester)', '').strip()
    
    # Check for AIPL1
    if gene_symbol == 'AIPL1' and 'PMID:10615133' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['AIPL1_10615133']
        print(f"[{i+1}] AIPL1/PMID:10615133: '{old}' → '{recommendations['AIPL1_10615133']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for cct_yeast
    elif 'cct' in gene_symbol.lower() and 'yeast' in gene_symbol.lower() and 'PMID:16762366' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['cct_yeast_16762366']
        print(f"[{i+1}] {gene_symbol}/PMID:16762366: '{old}' → '{recommendations['cct_yeast_16762366']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for HSPA5 (PMID:14685163)
    elif gene_symbol in ['HSPA5', 'BiP', 'GRP78'] and 'PMID:14685163' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['HSPA5_14685163']
        print(f"[{i+1}] {gene_symbol}/PMID:14685163: '{old}' → '{recommendations['HSPA5_14685163']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for HSPA1A (PMID:16130169)
    elif gene_symbol == 'HSPA1A' and 'PMID:16130169' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['HSPA1A_16130169']
        print(f"[{i+1}] HSPA1A/PMID:16130169: '{old}' → '{recommendations['HSPA1A_16130169']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for lsc_yeast (PMID:16873065)
    elif 'lsc' in gene_symbol.lower() and 'PMID:16873065' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['lsc_yeast_16873065']
        print(f"[{i+1}] {gene_symbol}/PMID:16873065: '{old}' → '{recommendations['lsc_yeast_16873065']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for HSPA5 (PMID:22013210) - UPR paper
    elif gene_symbol in ['HSPA5', 'BiP', 'GRP78'] and 'PMID:22013210' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['HSPA5_22013210']
        print(f"[{i+1}] {gene_symbol}/PMID:22013210: '{old}' → '{recommendations['HSPA5_22013210']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for btt1 or btt1-egd2 (PMID:26618777) - NAC complex
    elif (gene_symbol == 'btt1' or gene_symbol == 'btt1-egd2' or 'btt1' in gene_symbol.lower()) and 'PMID:26618777' in reference and current_rec.startswith('(No'):
        old = current_rec
        # Use the matching key
        key = 'btt1-egd2_yeast_26618777' if 'btt1-egd2' in gene_symbol.lower() else 'btt1_26618777'
        if key not in recommendations:
            key = 'btt1_26618777'
        row['Suggested action (by annotation review requester)'] = recommendations[key]
        print(f"[{i+1}] {gene_symbol}/PMID:26618777: '{old}' → '{recommendations[key]}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for gimc_yeast (PMID:9463374) - GIM complex
    elif 'gimc' in gene_symbol.lower() and 'PMID:9463374' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['gimc_yeast_9463374']
        print(f"[{i+1}] {gene_symbol}/PMID:9463374: '{old}' → '{recommendations['gimc_yeast_9463374']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for SSB2 (PMID:9670014)
    elif 'SSB2' in gene_symbol or gene_symbol == 'SSB' and 'PMID:9670014' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['SSB2_9670014']
        print(f"[{i+1}] {gene_symbol}/PMID:9670014: '{old}' → '{recommendations['SSB2_9670014']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for rac_yeast (PMID:11274393) - RAC complex
    elif 'rac' in gene_symbol.lower() and 'yeast' in gene_symbol.lower() and 'PMID:11274393' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['rac_yeast_11274393']
        print(f"[{i+1}] {gene_symbol}/PMID:11274393: '{old}' → '{recommendations['rac_yeast_11274393']}'")
        updated[f'{gene_symbol}_{reference}'] = True
    
    # Check for Hsp90aa1 (PMID:12855682)
    elif gene_symbol == 'Hsp90aa1' and 'PMID:12855682' in reference and current_rec.startswith('(No'):
        old = current_rec
        row['Suggested action (by annotation review requester)'] = recommendations['Hsp90aa1_12855682']
        print(f"[{i+1}] Hsp90aa1/PMID:12855682: '{old}' → '{recommendations['Hsp90aa1_12855682']}'")
        updated[f'{gene_symbol}_{reference}'] = True

# Write back
if updated:
    with open(tsv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nUpdated {len(updated)} annotations")
else:
    print("No annotations matched for update")
