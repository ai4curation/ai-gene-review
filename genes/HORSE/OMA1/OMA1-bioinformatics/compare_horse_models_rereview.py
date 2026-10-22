"""Compare every horse OMA1 UniProt gene-model product with human Q96E52 (re-review).

Fetches (live) all horse (taxon 9796) UniProt entries with gene name OMA1
(plus the target A0A9L0R9P8, which lacks a gene name),
human Q96E52 and mouse Q9D8H7, whose products all come from horse gene
ENSECAG00000009131 (taken from the UniProt Ensembl cross-references;
the Ensembl REST service returned HTTP 500 on 2026-10-20). For each horse product it reports:

* global alignment identity/coverage against human Q96E52-1;
* the residue aligned to each human catalytic/zinc position (H327, E328,
  H331, E392), the disulfide cysteines (C407, C465) and the C-terminal
  autocatalytic processing region (447-456);
* identity over the human C-terminal segment 405-524 separately from the
  N-terminal 1-404 segment, so that a divergent C-terminal exon is visible.

Writes RESULTS-rereview.md and results-rereview.json next to this script.
Run from the repository root:
    uv run python genes/HORSE/OMA1/OMA1-bioinformatics/compare_horse_models_rereview.py
"""

import json
from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
HUMAN = "Q96E52"
MOUSE = "Q9D8H7"
TARGET = "A0A9L0R9P8"
SITES = {327: "H", 328: "E", 331: "H", 392: "E", 407: "C", 465: "C"}
SPLIT = 404  # human residues 1..404 vs 405..524


def get(url: str, accept: str = "text/plain") -> str:
    req = Request(url, headers={"Accept": accept, "User-Agent": "ai-gene-review"})
    with urlopen(req, timeout=60) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(txt.splitlines()[1:])


def horse_entries() -> list[dict]:
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query=gene:OMA1+AND+organism_id:9796"
        "&fields=accession,length,xref_ensembl,sequence&format=tsv"
    )
    rows = get(url).strip().splitlines()[1:]
    out = []
    for row in rows:
        acc, length, ens, seq = row.split("\t")
        out.append({"accession": acc, "length": int(length), "ensembl": ens, "sequence": seq})
    return out


def align(a: str, b: str):
    aligner = Align.PairwiseAligner(
        mode="global", match_score=2, mismatch_score=-1, open_gap_score=-10, extend_gap_score=-0.5
    )
    al = aligner.align(a, b)[0]
    m = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            m[int(i)] = int(j)
    return al, m


def seg_identity(a: str, b: str, m: dict, lo: int, hi: int) -> dict:
    pos = [i for i in range(lo - 1, hi) if i in m]
    ident = sum(a[i] == b[m[i]] for i in pos)
    n = hi - lo + 1
    return {
        "human_range": [lo, hi],
        "paired": len(pos),
        "identical": ident,
        "identity_over_human_segment_percent": round(100 * ident / n, 1),
    }


def main() -> None:
    human = fasta_seq(HUMAN)
    mouse = fasta_seq(MOUSE)
    entries = horse_entries()
    # The target entry has no GN line, so the gene-name search misses it.
    if TARGET not in {e["accession"] for e in entries}:
        t = fasta_seq(TARGET)
        entries.insert(0, {"accession": TARGET, "length": len(t), "ensembl": "ENSECAT00000099022.1", "sequence": t})
    results = {"human": HUMAN, "human_length": len(human), "products": []}
    controls = [{"accession": MOUSE, "length": len(mouse), "ensembl": "", "sequence": mouse}]
    for e in entries + controls:
        b = e["sequence"]
        al, m = align(human, b)
        n = len(m)
        ident = sum(human[i] == b[j] for i, j in m.items())
        sites = {
            str(p): (b[m[p - 1]] + str(m[p - 1] + 1)) if (p - 1) in m else "-" for p in SITES
        }
        auto = "".join(b[m[i]] if i in m else "-" for i in range(446, 456))
        results["products"].append(
            {
                "accession": e["accession"],
                "is_target": e["accession"] == TARGET,
                "length": e["length"],
                "ensembl": e["ensembl"],
                "paired": n,
                "identity_paired_percent": round(100 * ident / n, 1),
                "human_coverage_percent": round(100 * n / len(human), 1),
                "aligned_sites": sites,
                "human_447_456": human[446:456],
                "aligned_447_456": auto,
                "n_term_1_404": seg_identity(human, b, m, 1, SPLIT),
                "c_term_405_524": seg_identity(human, b, m, SPLIT + 1, len(human)),
                "c_terminal_tail": b[-60:],
            }
        )
    gc = json.loads(
        get(f"https://rest.uniprot.org/genecentric/search?query=accession:{TARGET}&format=json", "application/json")
    )["results"][0]
    results["genecentric_canonical"] = gc["canonicalProtein"]["id"]
    results["genecentric_related"] = [r["id"] for r in gc.get("relatedProteins", [])]
    (HERE / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")

    lines = [
        "# OMA1 (horse): comparison of all horse gene-model products with human Q96E52 (re-review)",
        "",
        "Generated by `compare_horse_models_rereview.py` (live UniProt REST). "
        "Global alignment: Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extend -0.5. "
        "Segment identity is identical residues divided by the length of the human segment.",
        "",
        "| UniProt | length | Ensembl transcript | identity (paired) | human coverage | id. human 1-404 | id. human 405-524 | H327 | E328 | H331 | E392 | C407 | C465 | aligned to human 447-456 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for p in results["products"]:
        s = p["aligned_sites"]
        name = p["accession"] + (" (target)" if p["is_target"] else "") + (" (mouse control)" if p["accession"] == MOUSE else "")
        lines.append(
            f"| {name} | {p['length']} | {p['ensembl'] or '-'} | {p['identity_paired_percent']}% | "
            f"{p['human_coverage_percent']}% | {p['n_term_1_404']['identity_over_human_segment_percent']}% | "
            f"{p['c_term_405_524']['identity_over_human_segment_percent']}% | {s['327']} | {s['328']} | {s['331']} | "
            f"{s['392']} | {s['407']} | {s['465']} | {p['aligned_447_456']} (human {p['human_447_456']}) |"
        )
    lines += [
        "",
        "## UniProt gene-centric grouping (reference proteome UP000002281)",
        "",
        f"- canonical protein: {results['genecentric_canonical']}",
        f"- related proteins: {', '.join(results['genecentric_related'])}",
    ]
    lines += ["", "## C-terminal 60 residues of each product", ""]
    for p in results["products"]:
        lines.append(f"- {p['accession']}: `{p['c_terminal_tail']}`")
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
