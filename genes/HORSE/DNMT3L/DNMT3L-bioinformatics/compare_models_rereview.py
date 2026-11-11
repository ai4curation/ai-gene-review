"""Re-review comparison of horse DNMT3L gene models with human and mouse DNMT3L.

Fetches current UniProt sequences (horse A0A9L0T837 and F6YVL8, human Q9UJW3,
mouse Q9CWR8), runs global pairwise alignments (BLOSUM62, gap open -10,
extend -0.5) and reports identity, coverage, conservation of the ADD-domain
zinc-ligand cysteines/histidines (human Cys/His positions in the ADD domain
41-173) and of human Phe261 (DNMT3A interface; F261A abolishes binding,
PMID:17713477). Writes results-rereview.json. No values are hardcoded.

Run: uv run --with biopython --with requests python compare_models_rereview.py
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"horse_A0A9L0T837": "A0A9L0T837", "horse_F6YVL8": "F6YVL8",
        "human_Q9UJW3": "Q9UJW3", "mouse_Q9CWR8": "Q9CWR8"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def mapping(ref: str, tgt: str) -> tuple[dict[int, int], object]:
    aln = aligner().align(ref, tgt)[0]
    m: dict[int, int] = {}
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(int(re_ - rs)):
            m[int(rs) + i + 1] = int(ts) + i + 1
    return m, aln


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    human = seqs["human_Q9UJW3"]
    # ADD-domain (human 41-173) Cys/His candidate zinc ligands, plus F261.
    sites = [i + 1 for i, c in enumerate(human) if 41 <= i + 1 <= 173 and c in "CH"]
    sites.append(261)
    out = {"lengths": {k: len(v) for k, v in seqs.items()}, "comparisons": {}}
    for k, s in seqs.items():
        if k == "human_Q9UJW3":
            continue
        m, aln = mapping(human, s)
        ident = sum(1 for p, q in m.items() if human[p - 1] == s[q - 1])
        site_report = {}
        for p in sites:
            q = m.get(p)
            site_report[f"{human[p-1]}{p}"] = s[q - 1] + str(q) if q else "gap"
        # human C-terminal region (residues 300-386) identity
        cterm = [p for p in m if p >= 300]
        cterm_id = sum(1 for p in cterm if human[p - 1] == s[m[p] - 1])
        out["comparisons"][k] = {
            "paired_residues": len(m),
            "identical": ident,
            "identity_over_paired": round(ident / len(m), 4),
            "human_coverage": round(len(m) / len(human), 4),
            "target_coverage": round(len(m) / len(s), 4),
            "first_paired_target_residue": min(m.values()),
            "human_300_386_paired": len(cterm),
            "human_300_386_identity": round(cterm_id / len(cterm), 4) if cterm else None,
            "sites": site_report,
            "alignment": str(aln),
        }
    # horse model vs horse model
    m, aln = mapping(seqs["horse_A0A9L0T837"], seqs["horse_F6YVL8"])
    a, b = seqs["horse_A0A9L0T837"], seqs["horse_F6YVL8"]
    out["horse_models"] = {"paired": len(m),
                           "identical": sum(1 for p, q in m.items() if a[p-1] == b[q-1]),
                           "alignment": str(aln)}
    with open("results-rereview.json", "w") as fh:
        json.dump(out, fh, indent=2)
    for k, v in out["comparisons"].items():
        print(k, {x: v[x] for x in v if x not in ("alignment",)})
    print("horse models", {x: out["horse_models"][x] for x in ("paired", "identical")})
    print(out["lengths"])


if __name__ == "__main__":
    main()
