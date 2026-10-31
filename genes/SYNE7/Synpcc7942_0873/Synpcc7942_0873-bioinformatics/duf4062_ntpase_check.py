"""Test whether CP088958.1_900 (Q31PW6, Synpcc7942_0873) could be a NACHT/P-loop NTPase.

Two checks:
1. Motif scan of the query for Walker A (GxxxxGK[ST], plus relaxed forms) and Walker B
   (hhhhD[DE]).
2. UniProtKB counts of DUF4062 (IPR025139) proteins that also carry NACHT (IPR007111)
   or P-loop NTPase (IPR027417), overall and among proteins of length <= 450 aa
   (the query is 362 aa); also the reviewed DUF4062 entries.

Writes $BERIL_RUN_DIR/results.json and tables/duf4062_cooccurrence.tsv.
"""
import argparse
import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

REST = "https://rest.uniprot.org/uniprotkb/search"
MOTIFS = {
    "walker_a_strict": r"G....GK[ST]",
    "walker_a_relaxed": r"[GA]....GK[ST]",
    "gk_st": r"GK[ST]",
    "walker_b": r"[LIVMFA]{4}D[DE]",
}
QUERIES = {
    "duf4062_all": "xref:interpro-IPR025139",
    "duf4062_nacht": "xref:interpro-IPR025139 AND xref:interpro-IPR007111",
    "duf4062_ploop": "xref:interpro-IPR025139 AND xref:interpro-IPR027417",
    "duf4062_le450": "xref:interpro-IPR025139 AND length:[1 TO 450]",
    "duf4062_le450_nacht": "xref:interpro-IPR025139 AND length:[1 TO 450] AND xref:interpro-IPR007111",
    "duf4062_le450_ploop": "xref:interpro-IPR025139 AND length:[1 TO 450] AND xref:interpro-IPR027417",
    "duf4062_gt450": "xref:interpro-IPR025139 AND length:[451 TO 100000]",
    "duf4062_gt450_ploop": "xref:interpro-IPR025139 AND length:[451 TO 100000] AND xref:interpro-IPR027417",
}


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.headers, r.read().decode()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def count(q):
    h, _ = get(f"{REST}?{urllib.parse.urlencode({'query': q, 'size': 0})}")
    return int(h["X-Total-Results"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", type=Path, required=True)
    a = ap.parse_args()
    out = Path(os.environ["BERIL_RUN_DIR"])
    (out / "tables").mkdir(parents=True, exist_ok=True)

    seq = "".join(l.strip() for l in a.fasta.read_text().splitlines() if not l.startswith(">"))
    motifs = {k: [[m.start() + 1, m.group()] for m in re.finditer(p, seq)] for k, p in MOTIFS.items()}

    counts = {k: count(q) for k, q in QUERIES.items()}
    frac = {
        "ploop_frac_all": counts["duf4062_ploop"] / counts["duf4062_all"],
        "nacht_frac_all": counts["duf4062_nacht"] / counts["duf4062_all"],
        "ploop_frac_le450": counts["duf4062_le450_ploop"] / counts["duf4062_le450"],
        "nacht_frac_le450": counts["duf4062_le450_nacht"] / counts["duf4062_le450"],
        "ploop_frac_gt450": counts["duf4062_gt450_ploop"] / counts["duf4062_gt450"],
    }
    _, reviewed = get(f"{REST}?{urllib.parse.urlencode({'query': QUERIES['duf4062_all'] + ' AND reviewed:true', 'fields': 'accession,protein_name,organism_name,length,xref_interpro', 'format': 'tsv'})}")
    _, rel = get("https://rest.uniprot.org/uniprotkb/Q31PW6?fields=accession&format=tsv")

    with open(out / "tables" / "duf4062_cooccurrence.tsv", "w") as f:
        f.write("set\tquery\tcount\n")
        for k, q in QUERIES.items():
            f.write(f"{k}\t{q}\t{counts[k]}\n")
    res = {
        "query_length": len(seq),
        "motif_hits": motifs,
        "uniprot_counts": counts,
        "fractions": frac,
        "reviewed_duf4062_tsv": reviewed,
    }
    (out / "results.json").write_text(json.dumps(res, indent=1))
    print(json.dumps({k: v for k, v in res.items() if k != "reviewed_duf4062_tsv"}, indent=1))
    print(reviewed)


if __name__ == "__main__":
    main()
