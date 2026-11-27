"""Local alignment of C. elegans CEC-10 (Q9N4L7) against fungal SBF/MBF family members.

Fetches sequences from UniProt REST and InterPro domain matches from the InterPro API,
runs Smith-Waterman (BLOSUM62, gap open -11, extend -1) and estimates significance
with a shuffled-subject Z-score (100 shuffles). Results are printed, not hardcoded.
Usage: uv run python align_vs_swi6_family.py > results.txt
"""
import json
import random
import statistics
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "Q9N4L7"
SUBJECTS = {
    "P09959": "S.cerevisiae Swi6 (SBF/MBF non-DNA-binding subunit)",
    "P01129": "S.pombe Cdc10 (MBF non-DNA-binding subunit)",
    "P41412": "S.pombe Res2 (MBF DNA-binding subunit; IBD seed)",
    "P33520": "S.pombe Res1 (MBF DNA-binding subunit)",
    "P39678": "S.cerevisiae Mbp1 (MBF DNA-binding subunit)",
    "P25302": "S.cerevisiae Swi4 (SBF DNA-binding subunit)",
}


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def seq(acc):
    lines = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()
    return "".join(lines[1:])


def interpro_matches(acc):
    url = f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/?page_size=100"
    try:
        d = json.loads(fetch(url))
    except Exception as e:  # report, do not invent
        return [f"InterPro query failed: {e}"]
    out = []
    for r in d.get("results", []):
        m = r["metadata"]
        locs = []
        for p in r.get("proteins", []):
            for loc in p.get("entry_protein_locations") or []:
                for f in loc["fragments"]:
                    locs.append(f"{f['start']}-{f['end']}")
        out.append(f"{m['source_database']}:{m['accession']} {m.get('name')} [{','.join(locs)}]")
    return sorted(out)


def aligner():
    a = Align.PairwiseAligner()
    a.mode = "local"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    return a


def main():
    random.seed(1)
    al = aligner()
    q = seq(QUERY)
    print(f"Query {QUERY} length {len(q)}")
    print("InterPro matches for query:")
    for m in interpro_matches(QUERY):
        print("  ", m)
    for acc, desc in SUBJECTS.items():
        s = seq(acc)
        best = al.align(q, s)[0]
        score = best.score
        shuf = []
        for _ in range(100):
            l = list(s)
            random.shuffle(l)
            shuf.append(al.score(q, "".join(l)))
        z = (score - statistics.mean(shuf)) / statistics.stdev(shuf)
        qa, sa = best.aligned
        qs, qe = qa[0][0] + 1, qa[-1][1]
        ss, se = sa[0][0] + 1, sa[-1][1]
        ident = sum(
            1 for (a0, a1), (b0, b1) in zip(qa, sa) for i in range(a1 - a0) if q[a0 + i] == s[b0 + i]
        )
        alen = sum(a1 - a0 for a0, a1 in qa)
        print(
            f"\n{acc} {desc} len={len(s)}\n  SW score={score:.0f} shuffled mean={statistics.mean(shuf):.1f} "
            f"sd={statistics.stdev(shuf):.1f} Z={z:.1f}\n  query {qs}-{qe} vs subject {ss}-{se}; "
            f"aligned residues={alen}, identity={ident}/{alen} ({100*ident/alen:.0f}%)"
        )
        print("  subject InterPro:", "; ".join(m for m in interpro_matches(acc) if "pfam" in m.lower() or "ipr" in m.lower())[:600])


if __name__ == "__main__":
    main()
