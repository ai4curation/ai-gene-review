# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython==1.85", "requests"]
# ///
"""Subfamily, catalytic-triad and C-terminal hydropathy analysis for CG34171-PB (A8DZ15).

Steps (all inputs read from files or fetched live; nothing hardcoded about the outcome):
1. Read the PANTHER 19.0 fruit-fly classification file and list every D. melanogaster
   member of the subfamily that contains A8DZ15.
2. Read the PAINT table for PTHR24256 and map each FlyBase seed of PTN000667087 to its
   PANTHER 19.0 subfamily.
3. Fetch member sequences from UniProt REST, add bovine trypsin P00760 as an active
   reference, align with MAFFT L-INS-i, and read the residue at the trypsin catalytic
   His/Asp/Ser columns (P00760 positions taken from its UniProt ACT_SITE features).
4. Report pairwise identity of A8DZ15 to every member and build an NJ tree.
5. Kyte-Doolittle hydropathy of the A8DZ15 C-terminus (19-residue window).

Usage: uv run subfamily_analysis.py <repo_root> <outdir>
"""

import csv
import json
import subprocess
import sys
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

TARGET = "A8DZ15"
NODE = "PTN000667087"
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4,
    "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
    "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}


def read_fly_classification(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        ids = dict(x.split("=", 1) for x in parts[0].split("|")[1:])
        rows.append({"fbgn": ids.get("FlyBase"), "acc": parts[1], "symbol": parts[2],
                     "subfamily": parts[3]})
    return rows


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def main() -> None:
    root = Path(sys.argv[1])
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    fly = read_fly_classification(root / ".cache/panther/PTHR19.0_fruit_fly")
    target_row = next(r for r in fly if r["acc"] == TARGET)
    sub = target_row["subfamily"]
    members = [r for r in fly if r["subfamily"] == sub]
    by_fbgn = {r["fbgn"]: r for r in fly}

    seeds = set()
    with open(root / "interpro/panther/PTHR24256/PTHR24256-paint.tsv") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["node"] == NODE:
                for s in row["seeds"].split("|"):
                    if s.startswith("FB:"):
                        seeds.add((row["go_id"], s[3:]))
    seed_map = [
        {"go_id": go, "fbgn": fb, "symbol": by_fbgn.get(fb, {}).get("symbol"),
         "subfamily_19_0": by_fbgn.get(fb, {}).get("subfamily")}
        for go, fb in sorted(seeds)
    ]

    records = {}
    for r in members:
        j = fetch(r["acc"])
        records[r["acc"]] = j
    ref = fetch("P00760")
    ref_act = sorted(f["location"]["start"]["value"] for f in ref["features"]
                     if f["type"] == "Active site")
    fasta = out / "sf_members_plus_trypsin.fasta"
    with open(fasta, "w") as fh:
        for acc, j in records.items():
            fh.write(f">{acc}\n{j['sequence']['value']}\n")
        fh.write(f">P00760\n{ref['sequence']['value']}\n")
    aln_path = out / "sf_members_plus_trypsin.aln.fasta"
    with open(aln_path, "w") as fh:
        subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)],
                       stdout=fh, check=True)
    aln = AlignIO.read(aln_path, "fasta")
    seqs = {rec.id: str(rec.seq) for rec in aln}

    def col_of(acc: str, pos: int) -> int:
        n = 0
        for i, c in enumerate(seqs[acc]):
            if c != "-":
                n += 1
                if n == pos:
                    return i
        raise ValueError(pos)

    def pos_at(acc: str, col: int) -> tuple[str, int | None]:
        c = seqs[acc][col]
        if c == "-":
            return "-", None
        return c, len(seqs[acc][: col + 1].replace("-", ""))

    cols = [col_of("P00760", p) for p in ref_act]
    triad = []
    for r in members:
        res = [pos_at(r["acc"], c) for c in cols]
        domains = [f"{f['location']['start']['value']}-{f['location']['end']['value']}:"
                   f"{f.get('description', '')}" for f in records[r["acc"]]["features"]
                   if f["type"] == "Domain"]
        triad.append({"acc": r["acc"], "symbol": r["symbol"],
                      "length": len(records[r["acc"]]["sequence"]["value"]),
                      "his": f"{res[0][0]}{res[0][1] or ''}", "asp": f"{res[1][0]}{res[1][1] or ''}",
                      "ser": f"{res[2][0]}{res[2][1] or ''}",
                      "triad_intact": [x[0] for x in res] == ["H", "D", "S"],
                      "domains": domains})

    def identity(a: str, b: str) -> float:
        pairs = [(x, y) for x, y in zip(seqs[a], seqs[b]) if x != "-" and y != "-"]
        return round(100 * sum(x == y for x, y in pairs) / len(pairs), 1) if pairs else 0.0

    ident = sorted(({"acc": r["acc"], "symbol": r["symbol"], "pct_identity": identity(TARGET, r["acc"])}
                    for r in members if r["acc"] != TARGET), key=lambda d: -d["pct_identity"])

    calc = DistanceCalculator("identity")
    tree = DistanceTreeConstructor(calc, "nj").build_tree(aln)
    Phylo.write(tree, out / "sf_members_plus_trypsin_nj.nwk", "newick")

    tseq = records[TARGET]["sequence"]["value"]
    w = 19
    tail = [(i + 1, round(sum(KD[c] for c in tseq[i:i + w]) / w, 2))
            for i in range(len(tseq) - w - 30, len(tseq) - w + 1)]
    max_win = max(tail, key=lambda t: t[1])

    result = {
        "target": TARGET, "panther_19_0_subfamily": sub, "subfamily_size_fly": len(members),
        "paint_node_seed_subfamilies": seed_map, "trypsin_reference_active_sites": ref_act,
        "catalytic_residues": triad, "identity_to_target": ident,
        "c_terminal_kd_max_window": {"start": max_win[0], "end": max_win[0] + w - 1,
                                     "mean_kd": max_win[1],
                                     "segment": tseq[max_win[0] - 1: max_win[0] - 1 + w]},
        "c_terminal_kd_windows": tail,
    }
    (out / "subfamily_results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({k: v for k, v in result.items() if k != "c_terminal_kd_windows"}, indent=2))
    Phylo.draw_ascii(tree)


if __name__ == "__main__":
    main()
