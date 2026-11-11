"""Re-review analysis: exon structure of horse DNMT3A transcript models vs human canonical.

Fetches transcript structures from the Ensembl REST API and lists exon lengths,
flagging exons present in the reference horse model (ENSECAT00000027101, F6Q5D1)
but absent from the benchmark model (ENSECAT00000098563, A0A9L0TK01).

Run:  uv run python compare_exons_rereview.py > RESULTS-rereview-exons.txt
"""

import json
import time
import urllib.request

TRANSCRIPTS = {
    "ENSECAT00000098563": "horse, A0A9L0TK01 (benchmark)",
    "ENSECAT00000027101": "horse, F6Q5D1",
    "ENST00000321117": "human canonical, Q9Y6K1",
}


def lookup(tid: str) -> dict:
    req = urllib.request.Request(
        f"https://rest.ensembl.org/lookup/id/{tid}?expand=1",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def main() -> None:
    exons: dict[str, list[tuple[int, int]]] = {}
    for tid, label in TRANSCRIPTS.items():
        d = lookup(tid)
        ex = sorted(((e["start"], e["end"]) for e in d["Exon"]), reverse=d["strand"] == -1)
        exons[tid] = ex
        lengths = [e - s + 1 for s, e in ex]
        print(f"{tid} ({label}): strand {d['strand']}, {len(ex)} exons")
        print(f"  exon lengths 5'->3': {lengths}")
        time.sleep(1)
    bench = set(exons["ENSECAT00000098563"])
    ref = exons["ENSECAT00000027101"]
    print("\nExons of ENSECAT00000027101 absent from ENSECAT00000098563:")
    for i, (s, e) in enumerate(ref, start=1):
        if (s, e) not in bench:
            print(f"  exon {i}: {s}-{e} ({e - s + 1} nt)")


if __name__ == "__main__":
    main()
