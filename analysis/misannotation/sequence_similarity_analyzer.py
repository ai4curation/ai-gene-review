#!/usr/bin/env python3
"""
Sequence similarity analyzer for detecting potentially misannotated genes.

Inspired by PMC8491902 findings that 78% of enzyme annotations may be incorrect
when proteins share <25% identity with characterized enzymes.
"""

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import requests
import yaml
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML


@dataclass
class AnnotationRisk:
    """Risk assessment for a gene annotation."""
    gene_symbol: str
    uniprot_id: str
    organism: str
    go_terms: List[str]
    max_identity: float
    domain_match: bool
    risk_level: str  # HIGH, MEDIUM, LOW
    issues: List[str]
    blast_hits: Optional[List[Dict]] = None


class SequenceSimilarityAnalyzer:
    """Analyze sequence similarity to detect potential misannotations."""

    def __init__(self, cache_dir: Path = None):
        self.cache_dir = cache_dir or Path("analysis/misannotation/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Thresholds based on PMC8491902 paper
        self.HIGH_RISK_THRESHOLD = 25.0  # <25% identity = high risk
        self.MEDIUM_RISK_THRESHOLD = 50.0  # 25-50% identity = medium risk

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_uniprot_sequence(self, uniprot_id: str) -> Optional[str]:
        """Fetch protein sequence from UniProt."""
        cache_file = self.cache_dir / f"{uniprot_id}_sequence.fasta"

        if cache_file.exists():
            with open(cache_file) as f:
                record = SeqIO.read(f, "fasta")
                return str(record.seq)

        try:
            url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # Cache the sequence
            with open(cache_file, 'w') as f:
                f.write(response.text)

            # Parse and return sequence
            with open(cache_file) as f:
                record = SeqIO.read(f, "fasta")
                return str(record.seq)

        except Exception as e:
            self.logger.error(f"Failed to fetch sequence for {uniprot_id}: {e}")
            return None

    def run_blast_search(self, sequence: str, uniprot_id: str) -> List[Dict]:
        """Run BLAST search against SwissProt for characterized proteins."""
        cache_file = self.cache_dir / f"{uniprot_id}_blast.json"

        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)

        try:
            self.logger.info(f"Running BLAST for {uniprot_id}...")

            # Run BLAST against SwissProt (reviewed proteins only)
            result_handle = NCBIWWW.qblast(
                "blastp",
                "swissprot",
                sequence,
                hitlist_size=50,
                expect=1e-5
            )

            blast_records = NCBIXML.parse(result_handle)
            hits = []

            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if hsp.expect < 1e-5:
                            identity = (hsp.identities / hsp.align_length) * 100
                            hits.append({
                                "accession": alignment.accession,
                                "title": alignment.title,
                                "identity_percent": identity,
                                "coverage": hsp.align_length / len(sequence) * 100,
                                "evalue": hsp.expect,
                                "score": hsp.score
                            })

            # Cache results
            with open(cache_file, 'w') as f:
                json.dump(hits, f, indent=2)

            return hits

        except Exception as e:
            self.logger.error(f"BLAST failed for {uniprot_id}: {e}")
            return []

    def analyze_domain_conservation(self, uniprot_id: str, go_terms: List[str]) -> bool:
        """Check if protein domains are consistent with GO functional annotations."""
        # This is a simplified version - would need InterPro/Pfam integration
        # For now, return True (assuming domains match)
        return True

    def assess_annotation_risk(self, gene_data: Dict) -> AnnotationRisk:
        """Assess risk level for a gene's annotations."""
        uniprot_id = gene_data.get('id', '')
        gene_symbol = gene_data.get('gene_symbol', '')

        # Extract GO terms from existing_annotations
        go_terms = []
        if 'existing_annotations' in gene_data:
            for annotation in gene_data['existing_annotations']:
                if 'term' in annotation and 'id' in annotation['term']:
                    go_terms.append(annotation['term']['id'])

        issues = []

        # Get protein sequence
        sequence = self.get_uniprot_sequence(uniprot_id)
        if not sequence:
            return AnnotationRisk(
                gene_symbol=gene_symbol,
                uniprot_id=uniprot_id,
                organism=gene_data.get('taxon', {}).get('label', 'Unknown'),
                go_terms=go_terms,
                max_identity=0.0,
                domain_match=False,
                risk_level="HIGH",
                issues=["Could not retrieve protein sequence"]
            )

        # Run BLAST analysis
        blast_hits = self.run_blast_search(sequence, uniprot_id)

        # Find maximum sequence identity with characterized proteins
        max_identity = 0.0
        if blast_hits:
            max_identity = max(hit['identity_percent'] for hit in blast_hits)

        # Check domain conservation
        domain_match = self.analyze_domain_conservation(uniprot_id, go_terms)

        # Determine risk level
        if max_identity < self.HIGH_RISK_THRESHOLD:
            risk_level = "HIGH"
            issues.append(f"Low sequence identity ({max_identity:.1f}%) with characterized proteins")
        elif max_identity < self.MEDIUM_RISK_THRESHOLD:
            risk_level = "MEDIUM"
            issues.append(f"Moderate sequence identity ({max_identity:.1f}%) with characterized proteins")
        else:
            risk_level = "LOW"

        if not domain_match:
            issues.append("Domain architecture inconsistent with functional annotations")

        if len(go_terms) == 0:
            issues.append("No GO functional annotations found")

        return AnnotationRisk(
            gene_symbol=gene_symbol,
            uniprot_id=uniprot_id,
            organism=gene_data.get('taxon', {}).get('label', 'Unknown'),
            go_terms=go_terms,
            max_identity=max_identity,
            domain_match=domain_match,
            risk_level=risk_level,
            issues=issues,
            blast_hits=blast_hits[:10] if blast_hits else None  # Top 10 hits
        )

    def analyze_gene_directory(self, gene_dir: Path) -> Optional[AnnotationRisk]:
        """Analyze a single gene directory."""
        yaml_files = list(gene_dir.glob("*-ai-review.yaml"))
        if not yaml_files:
            return None

        yaml_file = yaml_files[0]
        try:
            with open(yaml_file) as f:
                gene_data = yaml.safe_load(f)

            return self.assess_annotation_risk(gene_data)

        except Exception as e:
            self.logger.error(f"Failed to analyze {yaml_file}: {e}")
            return None

    def generate_report(self, risks: List[AnnotationRisk], output_file: Path):
        """Generate misannotation risk report."""
        high_risk = [r for r in risks if r.risk_level == "HIGH"]
        medium_risk = [r for r in risks if r.risk_level == "MEDIUM"]
        low_risk = [r for r in risks if r.risk_level == "LOW"]

        report = {
            "summary": {
                "total_genes": len(risks),
                "high_risk": len(high_risk),
                "medium_risk": len(medium_risk),
                "low_risk": len(low_risk),
                "high_risk_percentage": (len(high_risk) / len(risks)) * 100 if risks else 0
            },
            "high_risk_genes": [
                {
                    "gene_symbol": r.gene_symbol,
                    "uniprot_id": r.uniprot_id,
                    "organism": r.organism,
                    "max_identity": r.max_identity,
                    "go_term_count": len(r.go_terms),
                    "issues": r.issues
                }
                for r in high_risk
            ],
            "detailed_analysis": [
                {
                    "gene_symbol": r.gene_symbol,
                    "uniprot_id": r.uniprot_id,
                    "organism": r.organism,
                    "risk_level": r.risk_level,
                    "max_identity": r.max_identity,
                    "domain_match": r.domain_match,
                    "go_terms": r.go_terms,
                    "issues": r.issues,
                    "top_blast_hits": r.blast_hits[:5] if r.blast_hits else []
                }
                for r in risks
            ]
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        # Also create a TSV summary for easy analysis
        tsv_file = output_file.with_suffix('.tsv')
        with open(tsv_file, 'w') as f:
            f.write("gene_symbol\tuniprot_id\torganism\trisk_level\tmax_identity\tgo_term_count\tissues\n")
            for r in risks:
                f.write(f"{r.gene_symbol}\t{r.uniprot_id}\t{r.organism}\t{r.risk_level}\t{r.max_identity:.1f}\t{len(r.go_terms)}\t{'; '.join(r.issues)}\n")


def main():
    parser = argparse.ArgumentParser(description="Analyze genes for potential misannotations")
    parser.add_argument("genes_dir", type=Path, help="Path to genes directory")
    parser.add_argument("--organism", help="Analyze specific organism only")
    parser.add_argument("--output", type=Path, default=Path("analysis/misannotation/risk_report.json"),
                       help="Output report file")
    parser.add_argument("--cache-dir", type=Path, help="Cache directory for sequences and BLAST results")

    args = parser.parse_args()

    analyzer = SequenceSimilarityAnalyzer(cache_dir=args.cache_dir)
    risks = []

    # Find gene directories
    if args.organism:
        gene_dirs = list(args.genes_dir.glob(f"{args.organism}/*"))
    else:
        gene_dirs = list(args.genes_dir.glob("*/*"))

    print(f"Analyzing {len(gene_dirs)} gene directories...")

    for gene_dir in gene_dirs:
        if gene_dir.is_dir():
            risk = analyzer.analyze_gene_directory(gene_dir)
            if risk:
                risks.append(risk)
                print(f"Analyzed {risk.gene_symbol}: {risk.risk_level} risk")

    # Generate report
    args.output.parent.mkdir(parents=True, exist_ok=True)
    analyzer.generate_report(risks, args.output)

    print("\nAnalysis complete!")
    print(f"Report saved to: {args.output}")
    print(f"High risk genes: {len([r for r in risks if r.risk_level == 'HIGH'])}")
    print(f"Medium risk genes: {len([r for r in risks if r.risk_level == 'MEDIUM'])}")


if __name__ == "__main__":
    main()