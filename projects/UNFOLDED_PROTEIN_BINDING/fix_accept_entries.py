#!/usr/bin/env python3
"""
Update all "ACCEPT" entries with specific replacement GO terms.
Since GO:0051082 is being obsoleted, every annotation needs a replacement term.
"""

import csv
from pathlib import Path
import re

def determine_replacement_term(gene: str, evidence: str, source: str) -> str:
    """
    Determine the appropriate replacement GO term based on gene/protein characteristics.
    
    GO:0140309 (unfolded protein holdase activity) - ATP-independent, typically small HSPs
    GO:0044183 (protein folding chaperone) - ATP-dependent foldases, most chaperones
    """
    gene_lower = gene.lower()
    
    # Small HSPs are typically ATP-independent holdases
    small_hsp_patterns = [
        r'^hsp\d{1,2}[a-z]?$',  # hsp16, hsp22, hsp90, etc. - but hsp90 is actually ATP-dependent
        r'^hsp\d{1,2}\.\d',      # HSP17.6A, etc.
        r'small.*hsp',
    ]
    
    is_small_hsp = any(re.search(pattern, gene_lower) for pattern in small_hsp_patterns)
    
    # Hsp90 is special - it's ATP-dependent despite the name pattern
    if 'hsp90' in gene_lower or gene.startswith('Hsp90'):
        return 'GO:0044183 (protein folding chaperone) [HSP90 family - ATP-dependent co-chaperone]'
    
    # Small HSPs (hsp16, hsp22, HSP17.6A) are holdases
    if is_small_hsp:
        return 'GO:0140309 (unfolded protein holdase activity) [small HSP - ATP-independent]'
    
    # Specific protein families
    
    # ER chaperones
    if gene in ['CALR', 'CANX', 'CLGN', 'ERO1B', 'LMAN1', 'SIL1']:
        return 'GO:0044183 (protein folding chaperone) [ER chaperone - calcium-binding lectin or oxidoreductase]'
    
    # CCT/TRiC complex subunits - ATP-dependent chaperonin
    if gene.startswith('CCT') or gene == 'TCP1':
        return 'GO:0044183 (protein folding chaperone) [CCT/TRiC chaperonin - ATP-dependent]'
    
    # Hsp70 family
    if 'HSPA' in gene or 'HSP70' in gene:
        return 'GO:0044183 (protein folding chaperone) [HSP70 family - ATP-dependent]'
    
    # Hsp60/chaperonin family
    if gene in ['HSPE1', 'HSP60', 'HSPD1']:
        return 'GO:0044183 (protein folding chaperone) [HSP60/chaperonin - ATP-dependent]'
    
    # Peptidyl-prolyl isomerases
    if gene in ['PPIA', 'PPIB']:
        return 'GO:0044183 (protein folding chaperone) [peptidyl-prolyl cis-trans isomerase]'
    
    # Mitochondrial proteases with chaperone activity
    if gene in ['AFG3L2', 'SPG7']:
        return 'GO:0044183 (protein folding chaperone) [mitochondrial AAA protease with chaperone activity]'
    
    # Tubulin folding cofactors
    if gene in ['TBCE', 'Tbce', 'TTC1']:
        return 'GO:0044183 (protein folding chaperone) [tubulin-specific chaperone cofactor]'
    
    # Other chaperones/cochaperones
    if gene in ['CDC37']:
        return 'GO:0044183 (protein folding chaperone) [HSP90 co-chaperone]'
    
    if gene in ['CHAF1A', 'CHAF1B']:
        return 'GO:0044183 (protein folding chaperone) [chromatin assembly factor - histone chaperone]'
    
    if gene in ['NAP1L4']:
        return 'GO:0044183 (protein folding chaperone) [nucleosome assembly protein - histone chaperone]'
    
    if gene in ['DNAJB4', 'DNAJC4']:
        return 'GO:0044183 (protein folding chaperone) [DnaJ/HSP40 family co-chaperone]'
    
    if gene in ['RUVBL2']:
        return 'GO:0044183 (protein folding chaperone) [AAA+ ATPase with chaperone activity]'
    
    if gene in ['MKKS']:
        return 'GO:0044183 (protein folding chaperone) [chaperonin-like protein]'
    
    if gene in ['APCS']:
        return 'GO:0140309 (unfolded protein holdase activity) [serum amyloid P-component - prevents aggregation]'
    
    if gene in ['TOR1A']:
        return 'GO:0044183 (protein folding chaperone) [AAA+ ATPase]'
    
    if gene in ['RP2']:
        return 'GO:0044183 (protein folding chaperone) [tubulin-binding cofactor]'
    
    if gene in ['TAPBP', 'Tapbp']:
        return 'GO:0044183 (protein folding chaperone) [tapasin - MHC class I chaperone]'
    
    # Yeast genes
    if gene in ['YCF3', 'YCF4']:
        return 'GO:0044183 (protein folding chaperone) [PSI assembly factor - chloroplast]'
    
    # Default for any TAS/IDA with expert curation - most likely ATP-dependent foldase
    if evidence in ['TAS', 'IDA'] and source in ['MGI', 'SGD', 'UniProt', 'PomBase', 'TAIR']:
        return 'GO:0044183 (protein folding chaperone) [ATP-dependent - high confidence evidence]'
    
    # Conservative default
    return 'GO:0044183 (protein folding chaperone) [inferred from TAS evidence]'


def main():
    tsv_file = Path('/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING/5974 Review annotations to GO_0031249 denatured protein binding GO_0051082 unfolded protein binding - Sheet1_FILLED.tsv')
    
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    updated_count = 0
    
    for row in rows:
        rec = row.get('Suggested action (by annotation review requester)', '').strip()
        
        if rec.startswith('ACCEPT'):
            gene = row.get('bioentity_label', '').strip()
            evidence = row.get('evidence_type', '').strip()
            source = row.get('assigned_by', '').strip()
            
            # Determine replacement term
            new_rec = determine_replacement_term(gene, evidence, source)
            
            old = rec
            row['Suggested action (by annotation review requester)'] = new_rec
            print(f"{gene:20s} ({evidence}/{source:12s}): {old} → {new_rec[:80]}")
            updated_count += 1
    
    # Write back
    with open(tsv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nUpdated {updated_count} ACCEPT entries with specific replacement GO terms")

if __name__ == '__main__':
    main()
