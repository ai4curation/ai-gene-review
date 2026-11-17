"""List unreviewed genes whose IBA rows assert terms no other annotation covers.

An IBA (PAINT) row is *non-duplicative* when the gene has no other non-negated
annotation, of any evidence code, to the same GO term or to a more specific one
(``is_a`` / ``part_of`` descendant). Such rows are where a review tests the PAINT
node placement itself, because nothing else on the gene already says the same
thing. Root terms and bare ``GO:0005515`` protein binding are ignored.

Genes that already have a folder under ``genes/<ORG>/`` (case-insensitive symbol
match) are left out. The output ranks genes by the number of non-duplicative IBA
terms, then by the number of PMIDs behind their experimental rows, which is a
rough proxy for how much literature a review can draw on.

Inputs are the GO Consortium GAF for the organism and ``go-basic.obo``, for example:

    curl -sSfLO https://current.geneontology.org/annotations/fb.gaf.gz
    curl -sSfLO https://purl.obolibrary.org/obo/go/go-basic.obo

Usage:
    uv run python projects/MOD_DESCRIPTIONS/iba_novel_candidates.py \
        --gaf fb.gaf.gz --obo go-basic.obo --organism DROME \
        --min-novel 2 --min-exp-pmids 10 --date 2026-11-16 \
        -o projects/MOD_DESCRIPTIONS/fly-iba-novel-candidates.yaml
"""

import argparse
import gzip
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml

ROOTS = {"GO:0003674", "GO:0008150", "GO:0005575", "GO:0005515"}
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def load_obo(path: Path) -> Tuple[Dict[str, Set[str]], Dict[str, str]]:
    """Return (term -> direct is_a/part_of parents, term -> name) for GO terms."""
    parents: Dict[str, Set[str]] = defaultdict(set)
    names: Dict[str, str] = {}
    cur = None
    for raw in path.open(encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("["):
            cur = "" if line == "[Term]" else None
            continue
        if cur is None:
            continue
        if line.startswith("id: GO:"):
            cur = line[4:]
        elif cur and line.startswith("name: "):
            names[cur] = line[6:]
        elif cur and line.startswith("is_a: GO:"):
            parents[cur].add(line[6:16])
        elif cur and line.startswith("relationship: part_of GO:"):
            parents[cur].add(line[22:32])
    return parents, names


def ancestor_closure(parents: Dict[str, Set[str]]):
    cache: Dict[str, Set[str]] = {}

    def ancestors(term: str) -> Set[str]:
        if term not in cache:
            seen: Set[str] = set()
            stack = [term]
            while stack:
                for p in parents.get(stack.pop(), ()):
                    if p not in seen:
                        seen.add(p)
                        stack.append(p)
            cache[term] = seen
        return cache[term]

    return ancestors


def candidates(gaf: Path, obo: Path, genes_dir: Path) -> List[dict]:
    parents, names = load_obo(obo)
    ancestors = ancestor_closure(parents)
    # Folders such as ``CycA__P14785`` review the gene ``CycA``: compare on the symbol part.
    reviewed = (
        {p.name.split("__")[0].lower() for p in genes_dir.iterdir() if p.is_dir()}
        if genes_dir.is_dir() else set()
    )

    symbol: Dict[str, str] = {}
    iba: Dict[str, Set[str]] = defaultdict(set)
    other: Dict[str, Set[str]] = defaultdict(set)
    exp_pmids: Dict[str, Set[str]] = defaultdict(set)
    opener = gzip.open if gaf.suffix == ".gz" else open
    with opener(gaf, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            gene_id, sym, qualifier, term, ref, code = f[1], f[2], f[3], f[4], f[5], f[6]
            symbol[gene_id] = sym
            if "NOT" in qualifier or term in ROOTS:
                continue
            (iba if code == "IBA" else other)[gene_id].add(term)
            if code in EXPERIMENTAL:
                # GAF column 6 can hold several pipe-separated references (FB:... | PMID:...).
                exp_pmids[gene_id].update(r for r in ref.split("|") if r.startswith("PMID:"))

    rows = []
    for gene_id, terms in iba.items():
        if symbol[gene_id].lower() in reviewed:
            continue
        covered: Set[str] = set()
        for t in other[gene_id]:
            covered.add(t)
            covered |= ancestors(t)
        novel = sorted(t for t in terms if t not in covered)
        if novel:
            rows.append({
                "symbol": symbol[gene_id],
                "gene_id": gene_id,
                "iba_terms": len(terms),
                "experimental_pmids": len(exp_pmids[gene_id]),
                "non_duplicative_iba": [f"{t} {names.get(t, '?')}" for t in novel],
            })
    rows.sort(key=lambda r: (-len(r["non_duplicative_iba"]), -r["experimental_pmids"], r["symbol"]))
    return rows


def header_value(path: Path, prefix: str, max_lines: int = 500) -> str:
    """Return the value of the first line starting with ``prefix`` in the file header.

    Records which release of an input was used (the GAF's ``!date-generated:``, the
    ontology's ``data-version:``) so the worklist can be reproduced. Only the first
    ``max_lines`` lines are read; returns "" if the prefix is not found there.
    """
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for _, line in zip(range(max_lines), fh):
            if line.startswith(prefix):
                return line[len(prefix):].strip()
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--gaf", type=Path, required=True)
    ap.add_argument("--obo", type=Path, required=True)
    ap.add_argument("--organism", default="DROME", help="genes/<ORG> folder of existing reviews")
    ap.add_argument("--min-novel", type=int, default=2)
    ap.add_argument("--min-exp-pmids", type=int, default=10)
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args()

    rows = candidates(args.gaf, args.obo, Path("genes") / args.organism)
    kept = [r for r in rows
            if len(r["non_duplicative_iba"]) >= args.min_novel
            and r["experimental_pmids"] >= args.min_exp_pmids]
    doc = {
        "description": __doc__.splitlines()[0],
        "generated": args.date,
        "organism": args.organism,
        "gaf": args.gaf.name,
        "gaf_date_generated": header_value(args.gaf, "!date-generated:"),
        "go_data_version": header_value(args.obo, "data-version:"),
        "filters": {"min_non_duplicative_iba": args.min_novel,
                    "min_experimental_pmids": args.min_exp_pmids},
        "unreviewed_genes_with_any_non_duplicative_iba": len(rows),
        "candidates": kept,
    }
    args.output.write_text(yaml.safe_dump(doc, sort_keys=False, width=100), encoding="utf-8")
    print(f"{len(rows)} unreviewed genes with non-duplicative IBA rows; {len(kept)} written to {args.output}")


if __name__ == "__main__":
    main()
