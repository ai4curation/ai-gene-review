"""Compare horse USP8 F7BV54 with experimentally characterised human and mouse USP8.

Fetches (live, UniProt REST) horse F7BV54, human P40818 (isoform 1) and mouse
Q80U87, records each entry's PANTHER family/subfamily cross-reference, aligns
horse globally to each ortholog and reports identity, coverage, internal gaps,
coverage of human landmark segments, and the horse residue at each human
functional site:

* MIT domain 33-116 (CHMP binding, endosomal targeting), rhodanese 195-313,
  SH3-binding motif 405-413 (STAM binding), USP domain 777-1109;
* the 14-3-3 binding motif around phospho-Ser718 (human 713-720, the Cushing
  disease hotspot);
* catalytic Cys786 (nucleophile) and His1067 (proton acceptor).

It also lists (i) the PAINT IBD rows in the local PTHR21646 PAINT file whose
seeds include human P40818 or mouse MGI:1934029, and (ii) the IBA annotations
QuickGO currently holds for human P40818 and mouse Q80U87. A node from which
both human and mouse inherit is ancestral to the boreoeutherian USP8 lineage,
which includes horse.

Writes RESULTS.md and results.json next to this script. Run from repo root:
    uv run python genes/HORSE/USP8__F7BV54/USP8__F7BV54-bioinformatics/compare_f7bv54.py
"""

import json
import re
from pathlib import Path
from urllib.request import urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PAINT = REPO / "interpro/panther/PTHR21646/PTHR21646-paint.tsv"
SEEDS = ("UniProtKB:P40818", "MGI:MGI:1934029")
TARGET = "F7BV54"
HUMAN = "P40818"
MOUSE = "Q80U87"
SEGMENTS = {
    "MIT 33-116": (33, 116),
    "rhodanese 195-313": (195, 313),
    "SH3-binding 405-413": (405, 413),
    "14-3-3 motif 713-720": (713, 720),
    "USP 777-1109": (777, 1109),
}
SITES = {718: "S", 786: "C", 1067: "H"}


def fetch(url: str) -> str:
    with urlopen(url) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    return "".join(fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])


def panther(acc: str) -> list[str]:
    txt = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.txt")
    return re.findall(r"^DR   PANTHER; (PTHR\d+(?::SF\d+)?);", txt, flags=re.M)


def align_map(ref: str, qry: str):
    aligner = Align.PairwiseAligner(
        mode="global", match_score=2, mismatch_score=-1,
        open_gap_score=-10, extend_gap_score=-0.5,
    )
    aln = aligner.align(ref, qry)[0]
    blocks = list(zip(*aln.aligned))
    m = {}
    for (s, e), (t, u) in blocks:
        for i, j in zip(range(s, e), range(t, u)):
            m[i + 1] = j + 1
    gaps = []
    for ((_, e1), (_, u1)), ((s2, _), (t2, _)) in zip(blocks, blocks[1:]):
        if s2 > e1:
            gaps.append(f"ref {e1 + 1}-{s2} absent from horse")
        if t2 > u1:
            gaps.append(f"horse {u1 + 1}-{t2} inserted")
    return m, gaps


def compare(ref: str, qry: str, landmarks: bool) -> dict:
    m, gaps = align_map(ref, qry)
    ident = sum(ref[i - 1] == qry[j - 1] for i, j in m.items())
    out = {
        "paired": len(m),
        "identity_percent": round(100 * ident / len(m), 2),
        "ref_coverage_percent": round(100 * len(m) / len(ref), 2),
        "gaps": gaps,
    }
    if landmarks:
        seg = {}
        for name, (a, b) in SEGMENTS.items():
            present = [k for k in range(a, b + 1) if k in m]
            same = sum(ref[k - 1] == qry[m[k] - 1] for k in present)
            seg[name] = {
                "aligned": f"{len(present)}/{b - a + 1}",
                "identical": f"{same}/{b - a + 1}",
                "human": ref[a - 1:b] if b - a < 12 else None,
                "horse": "".join(qry[m[k] - 1] for k in present) if b - a < 12 else None,
            }
        out["segments"] = seg
        out["sites"] = {
            f"{aa}{p}": (f"{qry[m[p] - 1]}{m[p]}" if p in m else "absent") for p, aa in SITES.items()
        }
        out["c_terminus_human_1090_end"] = ref[1089:]
        out["c_terminus_horse"] = qry[m[1090] - 1:] if 1090 in m else None
    return out


def paint_rows() -> list[str]:
    rows = []
    for line in PAINT.read_text().splitlines()[1:]:
        f = line.split("\t")
        if f[4] == "IBD" and any(x in f[6].split("|") for x in SEEDS):
            n = len(f[6].split("|"))
            rows.append(f"{f[1]} {f[2]} ({f[3]}) IBD negated={f[5]}; {n} seed(s)")
    return rows


def quickgo_iba(acc: str) -> list[str]:
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
        f"geneProductId={acc}&evidenceCode=ECO:0000318&limit=100"
    )
    d = json.loads(fetch(url))
    out = []
    for r in d["results"]:
        wf = ",".join(x["id"] for w in r.get("withFrom") or [] for x in w["connectedXrefs"])
        out.append(f"{r['goId']} {r['goAspect']} with/from {wf}")
    return sorted(out)


def main() -> None:
    seqs = {a: fasta_seq(a) for a in (TARGET, HUMAN, MOUSE)}
    res = {
        "lengths": {a: len(s) for a, s in seqs.items()},
        "panther": {a: panther(a) for a in seqs},
        "vs_human": compare(seqs[HUMAN], seqs[TARGET], landmarks=True),
        "vs_mouse": compare(seqs[MOUSE], seqs[TARGET], landmarks=False),
        "paint_ibd_rows_seeded_by_human_or_mouse_usp8": paint_rows(),
        "quickgo_iba": {a: quickgo_iba(a) for a in (HUMAN, MOUSE, TARGET)},
    }
    (HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")
    h, mo = res["vs_human"], res["vs_mouse"]
    lines = [
        "# USP8 horse F7BV54 vs human P40818 and mouse Q80U87",
        "",
        "Generated by compare_f7bv54.py (live UniProt REST). Global alignment: Biopython PairwiseAligner,",
        "match 2, mismatch -1, gap open -10, gap extend -0.5. Landmark coordinates are human P40818 positions.",
        "",
        "## Lengths and PANTHER placement",
        "",
    ]
    for a in seqs:
        lines.append(f"- {a}: {res['lengths'][a]} aa; PANTHER {', '.join(res['panther'][a])}")
    lines += [
        "",
        "## Pairwise",
        "",
        f"- vs human P40818: {h['identity_percent']}% identity over {h['paired']} paired residues; "
        f"{h['ref_coverage_percent']}% of human covered; gaps: {'; '.join(h['gaps']) or 'none'}",
        f"- vs mouse Q80U87: {mo['identity_percent']}% identity over {mo['paired']} paired residues; "
        f"{mo['ref_coverage_percent']}% of mouse covered; gaps: {'; '.join(mo['gaps']) or 'none'}",
        "",
        "## Human landmarks in F7BV54",
        "",
    ]
    for k, v in h["segments"].items():
        extra = f" (human {v['human']}, horse {v['horse']})" if v["human"] else ""
        lines.append(f"- {k}: {v['aligned']} aligned, {v['identical']} identical{extra}")
    lines.append("- Sites: " + ", ".join(f"human {k} -> horse {v}" for k, v in h["sites"].items()))
    lines.append(f"- C-terminus from human 1090: human {h['c_terminus_human_1090_end']}; horse {h['c_terminus_horse']}")
    lines += ["", "## PAINT IBD rows seeded by human P40818 or mouse Usp8 (local PTHR21646 file)", ""]
    lines += [f"- {r}" for r in res["paint_ibd_rows_seeded_by_human_or_mouse_usp8"]]
    lines += ["", "## IBA annotations in QuickGO", ""]
    for a, rows in res["quickgo_iba"].items():
        lines.append(f"- {a}: {len(rows)} IBA rows")
        lines += [f"  - {r}" for r in rows]
    lines.append("")
    (HERE / "RESULTS.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
