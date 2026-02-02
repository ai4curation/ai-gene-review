#!/usr/bin/env python3
"""Analyze reference coverage across all gene reviews."""

import yaml
from pathlib import Path

def analyze_gene_references():
    """Analyze reference counts for all genes."""
    genes_dir = Path("/Users/cjm/repos/ai-gene-review/genes")
    results = []

    for yaml_file in genes_dir.rglob("*-ai-review.yaml"):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)

            species = yaml_file.parent.parent.name
            gene = yaml_file.parent.name

            # Count different reference types
            references = data.get('references', [])
            total_refs = len(references)

            pmid_count = sum(1 for ref in references if ref.get('id', '').startswith('PMID:'))
            pmc_count = sum(1 for ref in references if ref.get('id', '').startswith('PMC:'))
            uniprot_count = sum(1 for ref in references if ref.get('id', '').startswith('UniProtKB:'))
            pdb_count = sum(1 for ref in references if ref.get('id', '').startswith('PDB:'))
            go_ref_count = sum(1 for ref in references if ref.get('id', '').startswith('GO_REF:'))
            other_count = total_refs - (pmid_count + pmc_count + uniprot_count + pdb_count + go_ref_count)

            # Count findings
            total_findings = sum(len(ref.get('findings', [])) for ref in references)

            results.append({
                'species': species,
                'gene': gene,
                'total_refs': total_refs,
                'pmid_count': pmid_count,
                'pmc_count': pmc_count,
                'uniprot_count': uniprot_count,
                'pdb_count': pdb_count,
                'go_ref_count': go_ref_count,
                'other_count': other_count,
                'total_findings': total_findings,
                'path': str(yaml_file)
            })

        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")
            continue

    return results

def print_analysis(results):
    """Print analysis results."""
    print("=== Gene Reference Analysis ===\n")

    # Sort by total references (ascending to find genes needing attention)
    results_sorted = sorted(results, key=lambda x: x['total_refs'])

    print("Top 20 genes with FEWEST references (need attention):")
    print("Species/Gene | Total | PMID | PMC | PDB | Other | Findings")
    print("-" * 65)
    for r in results_sorted[:20]:
        print(f"{r['species']}/{r['gene']:<15} | {r['total_refs']:5} | {r['pmid_count']:4} | {r['pmc_count']:3} | {r['pdb_count']:3} | {r['other_count']:5} | {r['total_findings']:8}")

    print("\n=== Summary Statistics ===")
    print(f"Total genes analyzed: {len(results)}")
    print(f"Average references per gene: {sum(r['total_refs'] for r in results) / len(results):.1f}")
    print(f"Genes with 0 PDB structures: {sum(1 for r in results if r['pdb_count'] == 0)}")
    print(f"Genes with <5 literature refs (PMID/PMC): {sum(1 for r in results if r['pmid_count'] + r['pmc_count'] < 5)}")
    print(f"Genes with no findings: {sum(1 for r in results if r['total_findings'] == 0)}")

    print("\n=== Genes needing immediate attention (very low refs) ===")
    priority_genes = [r for r in results_sorted if r['total_refs'] < 5 or (r['pmid_count'] + r['pmc_count']) < 3]
    for r in priority_genes:
        print(f"- {r['species']}/{r['gene']}: {r['total_refs']} refs, {r['pmid_count']+r['pmc_count']} literature")

if __name__ == "__main__":
    results = analyze_gene_references()
    print_analysis(results)