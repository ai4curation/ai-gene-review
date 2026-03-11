#!/usr/bin/env python3
"""
Manual curation of final 5 complex entries based on publication analysis.
"""

import csv
from pathlib import Path

# Manual recommendations based on PMID analysis
recommendations = {
    'naca-btf3_human_10982809': 'GO:0044183 (protein folding chaperone) [NAC complex - cotranslational folding, human homolog of yeast NAC]',
    'egd1-egd2_yeast_26618777': 'GO:0044183 (protein folding chaperone) [NAC complex - cotranslational folding, see PMID:26618777]',
    'SSB1_9670014': 'GO:0044183 (protein folding chaperone) [Hsp70 nascent chain binding - ribosome-associated, see PMID:9670014]',
    'HSP17.6A_11576425': 'GO:0140309 (unfolded protein holdase activity) [Small HSP - ATP-independent holdase]',
    'GIP1_16117846': 'UNDECIDED (GIP1 function unclear from reference - requires expert review)',
}

def main():
    tsv_file = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING/5974 Review annotations to GO_0031249 denatured protein binding GO_0051082 unfolded protein binding - Sheet1_FILLED.tsv')
    
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    updated = 0
    for row in rows:
        rec = row.get('Suggested action (by annotation review requester)', '').strip()
        
        if rec.startswith('(No matching'):
            gene = row.get('bioentity_label', '').strip()
            ref = row.get('reference', '').strip()
            
            # Extract PMID
            pmid = ''
            if 'PMID:' in ref:
                pmid = ref.split('PMID:')[1].split('|')[0].split()[0]
            
            # Match to recommendations
            key = None
            if gene == 'naca-btf3_human' and pmid == '10982809':
                key = 'naca-btf3_human_10982809'
            elif gene == 'egd1-egd2_yeast' and pmid == '26618777':
                key = 'egd1-egd2_yeast_26618777'
            elif gene == 'SSB1' and pmid == '9670014':
                key = 'SSB1_9670014'
            elif gene == 'HSP17.6A' and pmid == '11576425':
                key = 'HSP17.6A_11576425'
            elif gene == 'GIP1' and pmid == '16117846':
                key = 'GIP1_16117846'
            
            if key and key in recommendations:
                old = rec
                new = recommendations[key]
                row['Suggested action (by annotation review requester)'] = new
                print(f"{gene} (PMID:{pmid}): {old} → {new}")
                updated += 1
    
    # Write back
    with open(tsv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nUpdated {updated} entries")

if __name__ == '__main__':
    main()
