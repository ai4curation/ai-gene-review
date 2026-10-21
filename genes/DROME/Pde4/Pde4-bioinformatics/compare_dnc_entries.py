# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare the dnc UniProt entry Q9W4S9 (isoforms N/G) with the canonical
dnc entry P12252 (isoform II) and the human PDE4D (Q08499) catalytic domain.

Reports lengths, shared identical C-terminal block, and whether the PDE4
catalytic residues annotated on P12252 (ACT_SITE/BINDING features) are conserved
at the aligned positions in Q9W4S9. Results are computed, not hardcoded.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["Q9W4S9", "P12252", "Q08499"]


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def main() -> None:
    entries = {a: fetch(a) for a in ACCS}
    seqs = {a: e["sequence"]["value"] for a, e in entries.items()}
    out: dict = {"lengths": {a: len(s) for a, s in seqs.items()}}

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.end_gap_score = 0  # free end gaps: N-termini differ by design

    q, p = seqs["Q9W4S9"], seqs["P12252"]
    aln = aligner.align(q, p)[0]
    # map P12252 positions -> Q9W4S9 positions
    p2q = {}
    for (qs, qe), (ps, pe) in zip(*aln.aligned):
        for i in range(qe - qs):
            p2q[ps + i + 1] = qs + i + 1
    ident = sum(1 for pp, qq in p2q.items() if p[pp - 1] == q[qq - 1])
    out["Q9W4S9_vs_P12252"] = {
        "aligned_positions": len(p2q),
        "identical_positions": ident,
        "first_aligned_P12252_pos": min(p2q),
        "first_aligned_Q9W4S9_pos": p2q[min(p2q)],
    }
    # longest identical C-terminal suffix
    k = 0
    while k < min(len(q), len(p)) and q[-1 - k] == p[-1 - k]:
        k += 1
    out["identical_C_terminal_suffix_length"] = k

    feats = []
    for f in entries["P12252"].get("features", []):
        if f["type"] in ("Active site", "Binding site", "Domain"):
            s = f["location"]["start"]["value"]
            e = f["location"]["end"]["value"]
            rec = {"type": f["type"], "P12252": [s, e], "desc": f.get("description", "")
                   or f.get("ligand", {}).get("name", "")}
            if s in p2q and e in p2q:
                rec["Q9W4S9"] = [p2q[s], p2q[e]]
                rec["residues_identical"] = all(
                    pp in p2q and p[pp - 1] == q[p2q[pp] - 1] for pp in range(s, e + 1)
                )
            else:
                rec["Q9W4S9"] = None
            feats.append(rec)
    out["P12252_features_mapped"] = feats

    # catalytic domain identity of Q9W4S9 vs human PDE4D (PDE4 subfamily check)
    h = seqs["Q08499"]
    aln2 = aligner.align(q, h)[0]
    pairs = [(qs + i, hs + i) for (qs, qe), (hs, he) in zip(*aln2.aligned) for i in range(qe - qs)]
    dom = [(a, b) for a, b in pairs if 568 <= a < 898]
    out["Q9W4S9_PDEase_domain_vs_human_PDE4D"] = {
        "aligned": len(dom),
        "identical": sum(1 for a, b in dom if q[a] == h[b]),
    }
    print(json.dumps(out, indent=2, default=int))


if __name__ == "__main__":
    main()
