# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare the benchmark donkey CADM1 entry with the other products of the same gene.

Input: donkey-CADM1-genecentric-rereview.json (UniProt gene-centric REST response for
A0A9L0IX39, downloaded 2026-10-21). Reports, for every product, its length, the length
of the prefix shared with the gene-centric canonical, and its C-terminal residues.

Run: uv run --script compare_isoforms_rereview.py
"""
import json
from pathlib import Path

BENCHMARK = "A0A9L0IX39"


def shared_prefix(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def main() -> None:
    data = json.loads(Path(__file__).with_name("donkey-CADM1-genecentric-rereview.json").read_text())
    rec = data["results"][0]
    canon = rec["canonicalProtein"]
    cseq = canon["sequence"]["value"]
    print(f"Gene-centric canonical: {canon['id']} ({len(cseq)} aa), C-terminus {cseq[-12:]}")
    prods = [canon] + rec["relatedProteins"]
    for p in prods:
        s = p["sequence"]["value"]
        tag = " <- benchmark" if p["id"] == BENCHMARK else ""
        print(f"{p['id']}\t{len(s)} aa\tprefix shared with canonical: {shared_prefix(s, cseq)}\tC-term: {s[-15:]}{tag}")
    bench = next(p["sequence"]["value"] for p in prods if p["id"] == BENCHMARK)
    # The benchmark shares its whole extracellular/TM region with the stalk-short products;
    # report divergence point against every product that keeps the EYFI tail.
    for p in prods:
        s = p["sequence"]["value"]
        if s.endswith("EYFI"):
            k = shared_prefix(bench, s)
            if k > 340:
                print(f"vs {p['id']}: identical for first {k} residues; benchmark then reads {bench[k:]!r}, "
                      f"{p['id']} reads {s[k:]!r}")


if __name__ == "__main__":
    main()
