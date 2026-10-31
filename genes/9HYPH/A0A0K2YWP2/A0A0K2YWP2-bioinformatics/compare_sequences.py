"""Compare the T-G1 PgeF fragment (A0A0K2YWP2) with WSM2073 Mesau_02205 (L0KKS2)
and E. coli PgeF (P33644), and check UniParc identity.

Usage (from repo root):
    uv run python genes/9HYPH/A0A0K2YWP2/A0A0K2YWP2-bioinformatics/compare_sequences.py

Fetches sequences live from UniProt REST, writes results.json next to this script
and prints a summary. Nothing is hardcoded except the accessions and the
E. coli PgeF catalytic-triad positions reported in the literature (His/Cys107/His
motif; Cys107 from PMID:40632566), which are only used to look up the aligned
residues in L0KKS2.
"""
import json
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"fragment": "A0A0K2YWP2", "wsm2073": "L0KKS2", "ecoli": "P33644"}


def fetch_json(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def fetch(acc):
    d = fetch_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    return d["sequence"]["value"], d.get("extraAttributes", {}).get("uniParcId")


def aligner(mode):
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = mode
    return a


def stats(aln):
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    return {"aligned_columns": len(cols), "identical": ident,
            "percent_identity": round(100 * ident / len(cols), 1) if cols else None}


def main():
    seqs, uniparc = {}, {}
    for k, acc in ACCS.items():
        seqs[k], uniparc[k] = fetch(acc)
    out = {"lengths": {ACCS[k]: len(v) for k, v in seqs.items()},
           "uniparc": {ACCS[k]: v for k, v in uniparc.items()},
           "identical_sequence": seqs["fragment"] == seqs["wsm2073"]}

    loc = aligner("local").align(seqs["fragment"], seqs["wsm2073"])[0]
    out["fragment_vs_L0KKS2_local"] = stats(loc)
    out["fragment_span_on_L0KKS2"] = [int(loc.aligned[1][0][0]) + 1, int(loc.aligned[1][-1][1])]
    out["fragment_vs_L0KKS2_alignment"] = str(loc).splitlines()

    glob = aligner("global").align(seqs["ecoli"], seqs["wsm2073"])[0]
    out["P33644_vs_L0KKS2_global"] = stats(glob)
    # map E. coli residue numbers to L0KKS2 via the alignment
    mapping = {}
    for (ea, eb), (la, lb) in zip(glob.aligned[0], glob.aligned[1]):
        for i in range(eb - ea):
            mapping[ea + i + 1] = la + i + 1
    # E. coli Cys107 (PMID:40632566); report the E. coli residue and the aligned L0KKS2 residue
    triad = {}
    for pos in [107]:
        lpos = mapping.get(pos)
        triad[f"P33644_{seqs['ecoli'][pos-1]}{pos}"] = (
            f"L0KKS2_{seqs['wsm2073'][lpos-1]}{lpos}" if lpos else "gap")
    out["catalytic_cys_mapping"] = triad
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if not k.endswith("alignment")}, indent=2))
    print("\n".join(out["fragment_vs_L0KKS2_alignment"]))


if __name__ == "__main__":
    main()
