#!/usr/bin/env python3
"""
Domain architecture analyzer for detecting misannotated genes.

Checks if protein domains are consistent with functional GO annotations,
following the approach from PMC8491902.
"""

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set

import requests
import yaml


@dataclass
class DomainAnnotation:
    """Protein domain annotation from InterPro."""
    accession: str
    name: str
    type: str  # Domain, Family, Site, etc.
    start: int
    end: int
    evalue: Optional[float] = None


@dataclass
class DomainAnalysis:
    """Domain analysis results for a gene."""
    uniprot_id: str
    gene_symbol: str
    domains: List[DomainAnnotation]
    go_terms: List[str]
    domain_go_consistency: bool
    missing_expected_domains: List[str]
    unexpected_domains: List[str]
    risk_factors: List[str]


class DomainAnalyzer:
    """Analyze protein domains to detect annotation inconsistencies."""

    def __init__(self, cache_dir: Path = None):
        self.cache_dir = cache_dir or Path("analysis/misannotation/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Domain-GO term mappings (simplified - would need comprehensive database)
        self.domain_go_mappings = {
            # Kinase domains
            "IPR000719": ["GO:0016301", "GO:0004672"],  # Protein kinase domain -> kinase activity
            "IPR008271": ["GO:0016301", "GO:0004672"],  # Serine/threonine protein kinase domain

            # Phosphatase domains
            "IPR000340": ["GO:0016791"],  # Dual specificity phosphatase domain
            "IPR015655": ["GO:0004721"],  # Protein tyrosine phosphatase domain

            # DNA binding domains
            "IPR001356": ["GO:0003677"],  # Homeobox domain -> DNA binding
            "IPR000910": ["GO:0003677"],  # HMG box domain
            "IPR013783": ["GO:0003677"],  # Immunoglobulin-like fold

            # Enzyme domains
            "IPR002347": ["GO:0003824"],  # Glucose/ribitol dehydrogenase domain
            "IPR016040": ["GO:0003824"],  # NAD(P)-binding domain
        }

    def get_interpro_domains(self, uniprot_id: str) -> List[DomainAnnotation]:
        """Fetch domain annotations from InterPro via UniProt API."""
        cache_file = self.cache_dir / f"{uniprot_id}_interpro.json"

        if cache_file.exists():
            with open(cache_file) as f:
                data = json.load(f)
                return [DomainAnnotation(**domain) for domain in data]

        try:
            # Use UniProt API to get InterPro domain information
            url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}?fields=xref_interpro,ft_domain"
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()
            domains = []

            # Parse InterPro cross-references
            if 'uniProtKBCrossReferences' in data:
                for xref in data['uniProtKBCrossReferences']:
                    if xref['database'] == 'InterPro':
                        domains.append(DomainAnnotation(
                            accession=xref['id'],
                            name=xref.get('properties', {}).get('EntryName', ''),
                            type='Unknown',
                            start=0,
                            end=0
                        ))

            # Parse domain features
            if 'features' in data:
                for feature in data['features']:
                    if feature['type'] == 'Domain':
                        domains.append(DomainAnnotation(
                            accession=feature.get('description', 'Unknown'),
                            name=feature.get('description', ''),
                            type='Domain',
                            start=feature['location']['start']['value'],
                            end=feature['location']['end']['value']
                        ))

            # Cache results
            domain_data = [
                {
                    'accession': d.accession,
                    'name': d.name,
                    'type': d.type,
                    'start': d.start,
                    'end': d.end,
                    'evalue': d.evalue
                }
                for d in domains
            ]

            with open(cache_file, 'w') as f:
                json.dump(domain_data, f, indent=2)

            return domains

        except Exception as e:
            self.logger.error(f"Failed to fetch InterPro domains for {uniprot_id}: {e}")
            return []

    def check_domain_go_consistency(self, domains: List[DomainAnnotation], go_terms: List[str]) -> tuple[bool, List[str], List[str]]:
        """Check if domains are consistent with GO functional annotations."""
        missing_domains = []
        unexpected_domains = []

        # Get expected domains based on GO terms
        expected_domain_accessions = set()
        for go_term in go_terms:
            for domain_acc, domain_go_terms in self.domain_go_mappings.items():
                if go_term in domain_go_terms:
                    expected_domain_accessions.add(domain_acc)

        # Get actual domain accessions
        actual_domain_accessions = {d.accession for d in domains}

        # Find missing expected domains
        missing = expected_domain_accessions - actual_domain_accessions
        missing_domains = [acc for acc in missing]

        # Find unexpected domains (domains that don't match GO terms)
        for domain in domains:
            if domain.accession in self.domain_go_mappings:
                domain_go_terms = self.domain_go_mappings[domain.accession]
                if not any(go_term in go_terms for go_term in domain_go_terms):
                    unexpected_domains.append(domain.accession)

        # Consider consistent if no major mismatches
        is_consistent = len(missing_domains) == 0 and len(unexpected_domains) == 0

        return is_consistent, missing_domains, unexpected_domains

    def analyze_gene(self, gene_data: Dict) -> DomainAnalysis:
        """Analyze domain architecture for a gene."""
        uniprot_id = gene_data.get('id', '')
        gene_symbol = gene_data.get('gene_symbol', '')

        # Extract GO terms from existing_annotations
        go_terms = []
        if 'existing_annotations' in gene_data:
            for annotation in gene_data['existing_annotations']:
                if 'term' in annotation and 'id' in annotation['term']:
                    # Focus on molecular function terms (GO:0003xxx, GO:0004xxx, etc.)
                    go_id = annotation['term']['id']
                    if go_id.startswith('GO:0003') or go_id.startswith('GO:0004') or go_id.startswith('GO:0016'):
                        go_terms.append(go_id)

        # Get domain annotations
        domains = self.get_interpro_domains(uniprot_id)

        # Check domain-GO consistency
        is_consistent, missing_domains, unexpected_domains = self.check_domain_go_consistency(domains, go_terms)

        # Identify risk factors
        risk_factors = []
        if missing_domains:
            risk_factors.append(f"Missing expected domains: {', '.join(missing_domains)}")
        if unexpected_domains:
            risk_factors.append(f"Unexpected domains: {', '.join(unexpected_domains)}")
        if len(domains) == 0:
            risk_factors.append("No domain annotations found")
        if len(go_terms) == 0:
            risk_factors.append("No molecular function GO terms found")

        return DomainAnalysis(
            uniprot_id=uniprot_id,
            gene_symbol=gene_symbol,
            domains=domains,
            go_terms=go_terms,
            domain_go_consistency=is_consistent,
            missing_expected_domains=missing_domains,
            unexpected_domains=unexpected_domains,
            risk_factors=risk_factors
        )

    def analyze_gene_directory(self, gene_dir: Path) -> Optional[DomainAnalysis]:
        """Analyze domains for a single gene directory."""
        yaml_files = list(gene_dir.glob("*-ai-review.yaml"))
        if not yaml_files:
            return None

        yaml_file = yaml_files[0]
        try:
            with open(yaml_file) as f:
                gene_data = yaml.safe_load(f)

            return self.analyze_gene(gene_data)

        except Exception as e:
            self.logger.error(f"Failed to analyze {yaml_file}: {e}")
            return None

    def generate_report(self, analyses: List[DomainAnalysis], output_file: Path):
        """Generate domain analysis report."""
        consistent = [a for a in analyses if a.domain_go_consistency]
        inconsistent = [a for a in analyses if not a.domain_go_consistency]

        report = {
            "summary": {
                "total_genes": len(analyses),
                "consistent_domains": len(consistent),
                "inconsistent_domains": len(inconsistent),
                "inconsistency_rate": (len(inconsistent) / len(analyses)) * 100 if analyses else 0
            },
            "inconsistent_genes": [
                {
                    "gene_symbol": a.gene_symbol,
                    "uniprot_id": a.uniprot_id,
                    "domain_count": len(a.domains),
                    "go_term_count": len(a.go_terms),
                    "missing_domains": a.missing_expected_domains,
                    "unexpected_domains": a.unexpected_domains,
                    "risk_factors": a.risk_factors
                }
                for a in inconsistent
            ],
            "detailed_analysis": [
                {
                    "gene_symbol": a.gene_symbol,
                    "uniprot_id": a.uniprot_id,
                    "consistent": a.domain_go_consistency,
                    "domains": [
                        {
                            "accession": d.accession,
                            "name": d.name,
                            "type": d.type,
                            "start": d.start,
                            "end": d.end
                        }
                        for d in a.domains
                    ],
                    "go_terms": a.go_terms,
                    "risk_factors": a.risk_factors
                }
                for a in analyses
            ]
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        # Create TSV summary
        tsv_file = output_file.with_suffix('.tsv')
        with open(tsv_file, 'w') as f:
            f.write("gene_symbol\tuniprot_id\tconsistent\tdomain_count\tgo_term_count\trisk_factors\n")
            for a in analyses:
                f.write(f"{a.gene_symbol}\t{a.uniprot_id}\t{a.domain_go_consistency}\t{len(a.domains)}\t{len(a.go_terms)}\t{'; '.join(a.risk_factors)}\n")


def main():
    parser = argparse.ArgumentParser(description="Analyze protein domains for annotation consistency")
    parser.add_argument("genes_dir", type=Path, help="Path to genes directory")
    parser.add_argument("--organism", help="Analyze specific organism only")
    parser.add_argument("--output", type=Path, default=Path("analysis/misannotation/domain_report.json"),
                       help="Output report file")
    parser.add_argument("--cache-dir", type=Path, help="Cache directory for domain data")

    args = parser.parse_args()

    analyzer = DomainAnalyzer(cache_dir=args.cache_dir)
    analyses = []

    # Find gene directories
    if args.organism:
        gene_dirs = list(args.genes_dir.glob(f"{args.organism}/*"))
    else:
        gene_dirs = list(args.genes_dir.glob("*/*"))

    print(f"Analyzing domains for {len(gene_dirs)} gene directories...")

    for gene_dir in gene_dirs:
        if gene_dir.is_dir():
            analysis = analyzer.analyze_gene_directory(gene_dir)
            if analysis:
                analyses.append(analysis)
                status = "✓" if analysis.domain_go_consistency else "⚠"
                print(f"{status} {analysis.gene_symbol}: {len(analysis.domains)} domains, {len(analysis.go_terms)} GO terms")

    # Generate report
    args.output.parent.mkdir(parents=True, exist_ok=True)
    analyzer.generate_report(analyses, args.output)

    print(f"\nDomain analysis complete!")
    print(f"Report saved to: {args.output}")
    print(f"Consistent genes: {len([a for a in analyses if a.domain_go_consistency])}")
    print(f"Inconsistent genes: {len([a for a in analyses if not a.domain_go_consistency])}")


if __name__ == "__main__":
    main()