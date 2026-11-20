"""Sample MGI's Alliance gene descriptions for the mouse reviews.

Reproduces the 2026-11-02 check behind "Mouse (MGI): not used" on the project page:
a seeded random sample of mouse review folders, the MGI note the Alliance serves for
each, and whether the note uses mutant-phenotype vocabulary. ``phenotype_vocabulary``
is a regex screen, not a verdict: the page's conclusion that the notes describe allele
phenotypes rests on reading the committed note texts.

Usage:
    uv run python projects/MOD_DESCRIPTIONS/mgi_sample.py --also Cd79a Cd79b \
        -o projects/MOD_DESCRIPTIONS/mouse-mgi-sample.yaml

``--also`` adds named genes (here the pilot pair) outside the random sample.
"""

import argparse
import random
import re
import time
from pathlib import Path
from typing import Any, Dict, List

import yaml

from ai_gene_review.etl.descriptions import ORGANISM_CONFIG, extract_mod_xref, fetch_alliance_description

PHENOTYPE_WORDS = re.compile(
    r"homozyg|heterozyg|null|mutant|knock|allele|mice (?:lacking|deficient)|phenotype", re.IGNORECASE
)


def sample_genes(genes_dir: Path, n: int, seed: int) -> List[str]:
    """Return a seeded random sample of mouse review folder names."""
    genes = sorted(p.name for p in genes_dir.iterdir() if p.is_dir())
    return random.Random(seed).sample(genes, n)


def describe(genes_dir: Path, gene: str) -> Dict[str, Any]:
    """Fetch one gene's MGI note and flag mutant-phenotype vocabulary."""
    uniprot = (genes_dir / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8")
    xref = extract_mod_xref(uniprot, ORGANISM_CONFIG["mouse"])
    row: Dict[str, Any] = {"gene": gene, "mgi_id": f"MGI:{xref}" if xref else None}
    text = fetch_alliance_description(row["mgi_id"]).get("curated_synopsis") if xref else None
    row["mgi_note"] = text
    row["phenotype_vocabulary"] = bool(text and PHENOTYPE_WORDS.search(text))
    return row


def main() -> None:
    """Write the sample and a summary as YAML."""
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--genes-dir", type=Path, default=Path("genes/mouse"))
    p.add_argument("-n", type=int, default=25)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--also", nargs="*", default=[], help="extra genes, reported separately")
    p.add_argument("-o", "--output", type=Path, required=True)
    args = p.parse_args()
    rows = []
    for gene in sample_genes(args.genes_dir, args.n, args.seed):
        rows.append(describe(args.genes_dir, gene))
        time.sleep(0.3)
    extra = []
    for gene in args.also:
        extra.append(describe(args.genes_dir, gene))
        time.sleep(0.3)
    with_text = [r for r in rows if r["mgi_note"]]
    texts = [r["mgi_note"] for r in rows + extra if r["mgi_note"]]
    out = {
        "summary": {
            "mouse_review_folders": sum(1 for p in args.genes_dir.iterdir() if p.is_dir()),
            "sampled": len(rows),
            "seed": args.seed,
            "with_mgi_note": len(with_text),
            "with_phenotype_vocabulary": sum(r["phenotype_vocabulary"] for r in with_text),
            "notes_shared_by_several_genes": sorted({t for t in texts if texts.count(t) > 1}),
        },
        "genes": rows,
        "also": extra,
    }
    args.output.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
    print(yaml.safe_dump(out["summary"], sort_keys=False))


if __name__ == "__main__":
    main()
