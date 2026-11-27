"""Run InterProScan 5 (EBI REST service) on a protein FASTA and save the JSON and a TSV summary.

Usage: python3 -I iprscan.py FASTA OUTDIR [JOBID]
If JOBID is given, an already-submitted job is polled instead of submitting a new one
(EBI fair-use blocks repeated submissions). The submitter e-mail is read from $EBI_EMAIL.
Writes OUTDIR/iprscan.json and OUTDIR/iprscan_matches.tsv (db, accession, name, start, end, evalue,
InterPro entry). Uses all default member databases plus SignalP/Phobius/TMHMM where the service offers them.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://www.ebi.ac.uk/Tools/services/rest/iprscan5"
import os
EMAIL = os.environ.get("EBI_EMAIL", "")


def post(fasta: str) -> str:
    data = urllib.parse.urlencode({"email": EMAIL, "sequence": fasta, "goterms": "true",
                                   "pathways": "false", "stype": "p"}).encode()
    req = urllib.request.Request(BASE + "/run", data=data, headers={"User-Agent": "curl/8.5.0"})
    return urllib.request.urlopen(req, timeout=120).read().decode().strip()


def get(path: str) -> bytes:
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "curl/8.5.0"})
    return urllib.request.urlopen(req, timeout=300).read()


def main():
    fasta = Path(sys.argv[1]).read_text()
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    job = sys.argv[3] if len(sys.argv) > 3 else post(fasta)
    print("job", job, flush=True)
    for _ in range(240):
        st = get(f"/status/{job}").decode().strip()
        if st in ("FINISHED", "ERROR", "FAILURE", "NOT_FOUND"):
            break
        time.sleep(15)
    print("status", st, flush=True)
    if st != "FINISHED":
        raise SystemExit(f"InterProScan job {job} ended with {st}")
    js = json.loads(get(f"/result/{job}/json"))
    (out / "iprscan.json").write_text(json.dumps(js, indent=1))
    rows = []
    for res in js["results"]:
        for m in res["matches"]:
            sig = m["signature"]
            lib = sig["signatureLibraryRelease"]["library"]
            ent = sig.get("entry") or {}
            for loc in m["locations"]:
                rows.append([lib, sig["accession"], sig.get("name") or sig.get("description") or "",
                             str(loc["start"]), str(loc["end"]), str(loc.get("evalue", m.get("evalue", ""))),
                             (ent.get("accession") or "") + " " + (ent.get("name") or "")])
    rows.sort(key=lambda r: (int(r[3]), r[0]))
    with open(out / "iprscan_matches.tsv", "w") as fh:
        fh.write("db\taccession\tname\tstart\tend\tevalue\tinterpro\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print(open(out / "iprscan_matches.tsv").read())


if __name__ == "__main__":
    main()
