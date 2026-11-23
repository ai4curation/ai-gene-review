"""Rank unreviewed worm genes by how often WormBase texts of reviewed genes name them.

Reads the WormBase-written (``Alliance_Imported``) text in every
``genes/worm/<gene>/<gene>-descriptions.yaml`` sidecar, finds worm-style gene
names in it (``abc-1``, ``abcd-12``, ``abc-1.2``), and counts, for each name that
has no review folder, how many reviewed genes' texts mention it. This is how the
2026-11-16 batch of new worm reviews was chosen.

It is a lexical pointer, not a gene list: the raw ranking also contains human
symbols (``bcl-2``), misspellings (``mkrs-1`` for ``mksr-1``) and synonyms of
genes already reviewed under another name (``lag-3`` is ``sel-8``). Check each candidate's UniProt accession against the existing
reviews before starting one.

Usage:
    uv run python projects/MOD_DESCRIPTIONS/worm_candidates.py --top 40
"""

import argparse
import collections
import re
from pathlib import Path
from typing import Dict, List, Set

import yaml

GENE_NAME = re.compile(r"\b([a-zA-Z]{3,4}-\d{1,3}(?:\.\d+)?)\b")


def reviewed_genes(root: Path) -> Set[str]:
    """Return the lower-cased folder names of worm genes that have a review YAML.

    >>> reviewed_genes(Path("/nonexistent"))
    set()
    """
    if not root.is_dir():
        return set()
    return {
        p.name.lower()
        for p in root.iterdir()
        if (p / f"{p.name}-ai-review.yaml").exists()
    }


def gene_names(text: str) -> Set[str]:
    """Return the worm-style gene names in a text, lower-cased.

    >>> sorted(gene_names("ABI-1 binds MIG-10 and UNC-53/NAV2; see hsp-16.41"))
    ['abi-1', 'hsp-16.41', 'mig-10', 'unc-53']
    """
    return {m.lower() for m in GENE_NAME.findall(text)}


def rank_candidates(root: Path) -> List[Dict[str, object]]:
    """Rank unreviewed gene names by the number of reviewed genes whose text names them."""
    reviewed = reviewed_genes(root)
    mentioners: Dict[str, Set[str]] = collections.defaultdict(set)
    for sidecar in sorted(root.glob("*/*-descriptions.yaml")):
        data = yaml.safe_load(sidecar.read_text(encoding="utf-8")) or {}
        gene = str(data.get("gene_symbol", "")).lower()
        for source in data.get("descriptions") or []:
            if source.get("source") != "Alliance_Imported":
                continue
            for name in gene_names(source.get("text", "")):
                if name != gene and name not in reviewed:
                    mentioners[name].add(gene)
    ranked = sorted(mentioners.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return [
        {"gene": name, "mentions": len(genes), "named_by": sorted(genes)}
        for name, genes in ranked
    ]


def main() -> None:
    """Print the top-ranked candidates as YAML."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--genes-dir", type=Path, default=Path("genes/worm"))
    parser.add_argument("--top", type=int, default=40)
    args = parser.parse_args()
    print(yaml.safe_dump(rank_candidates(args.genes_dir)[: args.top], sort_keys=False))


if __name__ == "__main__":
    main()
