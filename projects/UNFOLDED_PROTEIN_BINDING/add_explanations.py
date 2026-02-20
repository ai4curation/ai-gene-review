#!/usr/bin/env python3
"""
Add explanations for all recommendations that don't have GO terms.
"""

import csv
import os
import re

FILEPATH = "/home/raymond/local/src/git/ai-gene-review/projects/UNFOLDED_PROTEIN_BINDING/5974 Review annotations to GO_0031249 denatured protein binding GO_0051082 unfolded protein binding - Sheet1_FILLED.tsv"
PUBS_DIR = "/home/raymond/local/src/git/ai-gene-review/publications"

# Read publication
def read_publication(pmid):
    filepath = os.path.join(PUBS_DIR, f"PMID_{pmid}.md")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return None

# Explanation templates and logic
def determine_explanation(gene, evidence_type, source, ref, current_rec):
    """Determine appropriate explanation for non-GO term recommendations."""
    
    # Extract PMID if available
    pmid = None
    if ref.startswith('PMID:'):
        pmid = ref.replace('PMID:', '')
    
    # Known DELETE cases
    if current_rec == 'DELETE':
        if gene == 'slrP':
            return "DELETE (bacterial virulence effector protein that prevents host ubiquitination; not a chaperone)"
        elif gene == 'SYVN1':
            return "DELETE (E3 ubiquitin ligase involved in ERAD; substrate binding is not chaperone function)"
        elif gene == 'ERLEC1':
            return "DELETE (ER lectin involved in ERAD quality control; lectin binding is not chaperone function)"
        elif gene == 'GRPEL1':
            return "DELETE (nucleotide exchange factor for HSP70, not a chaperone itself; catalyzes ADP/ATP exchange)"
        else:
            return "DELETE (not a bona fide chaperone; requires expert review to determine correct function)"
    
    # Known MODIFY case
    if current_rec == 'MODIFY':
        return current_rec  # Already has modifier info
    
    # Known UNDECIDED case
    if current_rec == 'UNDECIDED':
        return "UNDECIDED (requires access to full publication for proper evaluation)"
    
    # REVIEW cases - need to look at specific genes
    if current_rec == 'REVIEW':
        # Assembly chaperones for specific substrates
        if gene in ['COX20', 'PET100', 'SHY1', 'ATP11', 'ATP10', 'VMA22', 'HSP10']:
            return "REVIEW (assembly chaperone for specific substrate; may need more specific GO term than general chaperone)"
        
        # ER quality control proteins
        if gene in ['UGGT1', 'Uggt1', 'EUG1', 'PDI1', 'EPS1']:
            return "REVIEW (ER quality control; folding sensor or oxidoreductase; may need more specific term)"
        
        # Peptidyl-prolyl isomerases
        if gene in ['CPR6', 'CPR7', 'CNE1']:
            return "REVIEW (peptidyl-prolyl cis-trans isomerase; catalytic function may be distinct from holdase activity)"
        
        # Protein translocation
        if gene in ['TOMM20']:
            return "REVIEW (mitochondrial import receptor; transient binding during translocation, not chaperone function)"
        
        # Stress response or regulatory
        if gene in ['IRE1', 'ire1_yeast-1']:
            return "REVIEW (ER stress sensor; may bind unfolded proteins but primary function is signaling, not folding)"
        
        # Co-chaperones or regulatory
        if gene in ['AHSA1', 'CDC37', 'PTGES3']:
            return "REVIEW (HSP90 co-chaperone; assists in substrate loading but may not directly bind unfolded proteins)"
        
        # Protein-specific chaperones
        if gene in ['VPS45']:
            return "REVIEW (SM protein involved in vesicular trafficking; substrate specificity may not qualify as general chaperone)"
        
        # Holdase vs foldase ambiguity
        if gene in ['NSG1', 'NSG2']:
            return "REVIEW (ER membrane protein involved in protein quality control; unclear if holdase or other function)"
        
        # Ciliopathy protein
        if gene in ['TMEM67']:
            return "REVIEW (transmembrane protein; IPI evidence suggests interaction but unclear if chaperone function)"
        
        # E. coli periplasmic
        if gene in ['CpxP']:
            return "REVIEW (E. coli periplasmic protein; inhibitor of CpxA, may bind misfolded proteins but function is regulatory)"
        
        # Metabolic enzyme
        if gene in ['RidA']:
            return "REVIEW (reactive intermediate deaminase; prevents protein damage but not classical chaperone)"
        
        # Drosophila ERAD
        if gene in ['Edem2']:
            return "REVIEW (ERAD enhancer; mannosidase activity, not holdase)"
        
        # Yeast CIA pathway
        if gene in ['cia30']:
            return "REVIEW (cytosolic iron-sulfur assembly; specific substrate, unclear if general chaperone function)"
        
        # Default for REVIEW
        return "REVIEW (requires expert evaluation to determine if true chaperone function or other protein binding activity)"
    
    return current_rec


def main():
    # Read spreadsheet
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    print(f"Total rows: {len(rows)}")
    
    # Update rows that need explanations
    updated_count = 0
    for i, row in enumerate(rows):
        rec = row['Suggested action (by annotation review requester)'].strip()
        
        # Skip if already has GO term or has explanation
        if rec.startswith('GO:') or ('(' in rec and ')' in rec):
            continue
        
        gene = row['bioentity_label']
        evidence_type = row['evidence_type']
        source = row['assigned_by']
        ref = row['reference']
        
        # Get explanation
        new_rec = determine_explanation(gene, evidence_type, source, ref, rec)
        
        if new_rec != rec:
            print(f"\n[{i+1}] {gene} ({evidence_type}/{source})")
            print(f"  Old: {rec}")
            print(f"  New: {new_rec}")
            row['Suggested action (by annotation review requester)'] = new_rec
            updated_count += 1
    
    # Write updated spreadsheet
    with open(FILEPATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n{'='*80}")
    print(f"Updated {updated_count} rows with explanations")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
