#!/usr/bin/env python3
"""Convert HF protein_catalogue entries to deep-research-bioreason.md files.

Usage:
    python scripts/hf_to_deep_research.py --protein-id P0A9K9 --gene SlyD --species ECOLI
    python scripts/hf_to_deep_research.py --batch scripts/batch_proteins.tsv

The batch TSV should have columns: protein_id, gene_symbol, species_code
"""

import argparse
import re
import textwrap
from datetime import date
from pathlib import Path

import duckdb


DB_PATH = Path("data/bioreason-hf/protein_catalogue.ddb")


def extract_sections(generation: str) -> dict[str, str]:
    """Parse the generation column into structured sections.

    >>> gen = '<think>\\nReasoning here.\\n</think>\\n\\n- Functional Summary: A kinase.\\n- UniProt Summary: Kinase.\\n- InterPro:\\n    - IPR000001: Domain (family) [1-100]\\n- Molecular Function:\\n    - GO:0004672 protein kinase activity\\n- Biological Process:\\n    - GO:0006468 protein phosphorylation\\n- Cellular Component:\\n    - GO:0005737 cytoplasm'
    >>> sections = extract_sections(gen)
    >>> sections['think']
    'Reasoning here.'
    >>> 'kinase' in sections['functional_summary'].lower()
    True
    >>> 'GO:0004672' in sections['go_mf']
    True
    """
    result = {}

    # Extract think block
    think_match = re.search(r"<think>\s*\n?(.*?)\n?\s*</think>", generation, re.DOTALL)
    result["think"] = think_match.group(1).strip() if think_match else ""

    # Extract structured sections after think block
    post_think = generation[think_match.end() :].strip() if think_match else generation

    # Functional Summary
    m = re.search(r"- Functional Summary:\s*(.*?)(?=\n- (?:UniProt|InterPro|Molecular|Biological|Cellular))", post_think, re.DOTALL)
    result["functional_summary"] = m.group(1).strip() if m else ""

    # UniProt Summary
    m = re.search(r"- UniProt Summary:\s*(.*?)(?=\n- (?:InterPro|Molecular|Biological|Cellular))", post_think, re.DOTALL)
    result["uniprot_summary"] = m.group(1).strip() if m else ""

    # InterPro
    m = re.search(r"- InterPro:\s*\n((?:\s+-.*\n)*)", post_think)
    result["interpro"] = m.group(1).rstrip() if m else ""

    # GO terms by aspect
    for aspect, key in [("Molecular Function", "go_mf"), ("Biological Process", "go_bp"), ("Cellular Component", "go_cc")]:
        m = re.search(rf"- {aspect}:\s*\n((?:\s+-.*\n?)*)", post_think)
        result[key] = m.group(1).rstrip() if m else ""

    return result


def format_interpro_table(interpro_text: str) -> str:
    """Convert interpro list to markdown table.

    >>> text = '    - IPR001179: FKBP-type PPIase domain (domain) [4-66]\\n    - IPR046357: PPIase superfamily (homologous_superfamily) [1-110]'
    >>> table = format_interpro_table(text)
    >>> 'IPR001179' in table
    True
    >>> '| Domain |' in table
    True
    """
    lines = []
    for line in interpro_text.split("\n"):
        m = re.match(r"\s+-\s+(IPR\d+):\s+(.+?)\s+\((\w+)\)\s+\[(.+?)\]", line.strip())
        if m:
            lines.append(f"| {m.group(1)} | {m.group(2)} | {m.group(3)} | [{m.group(4)}] |")
    if not lines:
        return interpro_text
    header = "| Domain | Type | Category | Range |\n|--------|------|----------|-------|"
    return header + "\n" + "\n".join(lines)


def format_go_section(go_text: str) -> str:
    """Format GO terms as list items.

    >>> text = '    - GO:0004672 protein kinase activity'
    >>> '- GO:0004672' in format_go_section(text)
    True
    """
    lines = []
    for line in go_text.split("\n"):
        m = re.match(r"\s+-\s+(GO:\d{7})\s+(.*)", line.strip())
        if m:
            lines.append(f"- {m.group(1)} {m.group(2)}")
    return "\n".join(lines)


def generate_md(protein_id: str, gene_symbol: str, species_code: str) -> str:
    """Generate deep-research-bioreason.md content from HF catalogue."""
    con = duckdb.connect(str(DB_PATH), read_only=True)
    row = con.execute(
        "SELECT * FROM protein_catalogue WHERE protein_id = ?", [protein_id]
    ).fetchone()
    con.close()

    if row is None:
        raise ValueError(f"Protein {protein_id} not found in catalogue")

    protein_id_col, generation, model, sequence, organism = row
    sections = extract_sections(generation)

    interpro_table = format_interpro_table(sections["interpro"])
    go_mf = format_go_section(sections["go_mf"])
    go_bp = format_go_section(sections["go_bp"])
    go_cc = format_go_section(sections["go_cc"])

    md = textwrap.dedent(f"""\
    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '{date.today().isoformat()}'
    uniprot_id: {protein_id}
    gene: {gene_symbol}
    organism: {organism}
    ---

    ## Thinking Trace

    {sections['think']}

    ## Functional Summary

    {sections['functional_summary']}

    ## UniProt Summary

    {sections['uniprot_summary']}

    ## InterPro Domains

    {interpro_table}

    ## GO Term Predictions

    ### Molecular Function
    {go_mf}

    ### Biological Process
    {go_bp}

    ### Cellular Component
    {go_cc}
    """)
    return md


def main():
    parser = argparse.ArgumentParser(description="Convert HF catalogue to deep-research markdown")
    parser.add_argument("--protein-id", help="UniProt accession")
    parser.add_argument("--gene", help="Gene symbol")
    parser.add_argument("--species", help="Species code (e.g. ECOLI)")
    parser.add_argument("--batch", help="TSV file with protein_id, gene_symbol, species_code columns")
    parser.add_argument("--output-dir", default="genes", help="Base output directory")
    args = parser.parse_args()

    if args.batch:
        with open(args.batch) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                protein_id, gene_symbol, species_code = parts[0], parts[1], parts[2]
                outdir = Path(args.output_dir) / species_code / gene_symbol
                outpath = outdir / f"{gene_symbol}-deep-research-bioreason.md"
                if outpath.exists():
                    print(f"  SKIP {outpath} (already exists)")
                    continue
                md = generate_md(protein_id, gene_symbol, species_code)
                outdir.mkdir(parents=True, exist_ok=True)
                outpath.write_text(md)
                print(f"  WROTE {outpath}")
    elif args.protein_id and args.gene and args.species:
        outdir = Path(args.output_dir) / args.species / args.gene
        outpath = outdir / f"{args.gene}-deep-research-bioreason.md"
        md = generate_md(args.protein_id, args.gene, args.species)
        outdir.mkdir(parents=True, exist_ok=True)
        outpath.write_text(md)
        print(f"  WROTE {outpath}")
    else:
        parser.error("Provide either --batch or --protein-id/--gene/--species")


if __name__ == "__main__":
    main()
