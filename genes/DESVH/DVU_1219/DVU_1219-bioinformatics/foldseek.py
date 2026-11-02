"""Structural homology of DVU_1219 (Q72CR4): Foldseek web search of the AlphaFold DB model.

Downloads AF-Q72CR4-F1 (model and per-residue pLDDT), submits it to the Foldseek server
(search.foldseek.com, 3Di+AA mode) against PDB100 and AFDB-SwissProt, and saves the top hits with
their alignments (query/target ranges, E-value, TM-score-like prob, identity).
For hits whose UniProt entry has ACT_SITE features, it maps those catalytic residues through the
structural alignment onto the query and reports the query residue placed there.

Usage: python3 -I foldseek.py OUTDIR
"""
import io
import json
import re
import sys
import tarfile
import time
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ACC = "Q72CR4"
UA = {"User-Agent": "python-urllib/3"}  # the AlphaFold file server returns 403 to curl user agents


def get(url, timeout=120):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def submit(pdb: bytes, dbs):
    b = uuid.uuid4().hex
    parts = []
    def field(n, v):
        parts.append(f"--{b}\r\nContent-Disposition: form-data; name=\"{n}\"\r\n\r\n{v}\r\n".encode())
    parts.append(f"--{b}\r\nContent-Disposition: form-data; name=\"q\"; filename=\"q.pdb\"\r\n"
                 f"Content-Type: application/octet-stream\r\n\r\n".encode() + pdb + b"\r\n")
    field("mode", "3diaa")
    for d in dbs:
        field("database[]", d)
    parts.append(f"--{b}--\r\n".encode())
    req = urllib.request.Request("https://search.foldseek.com/api/ticket", data=b"".join(parts),
                                 headers={**UA, "Content-Type": f"multipart/form-data; boundary={b}"})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())


def uniprot_sites(acc):
    try:
        txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", 60).decode()
    except Exception:  # noqa: BLE001
        return None, []
    de = re.search(r"^DE   (?:RecName|SubName): Full=([^;{]+)", txt, re.M)
    feats = []
    for m in re.finditer(r"^FT   (ACT_SITE|SITE)\s+(\d+)\n((?:FT {19}.*\n)*)", txt, re.M):
        note = re.search(r'/note="([^"]+)"', m.group(3))
        feats.append({"pos": int(m.group(2)), "note": note.group(1) if note else ""})
    return (de.group(1).strip() if de else None), feats


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    meta = json.loads(get(f"https://alphafold.ebi.ac.uk/api/prediction/{ACC}"))[0]
    pdb = get(meta["pdbUrl"])
    (out / f"AF-{ACC}.pdb").write_bytes(pdb)
    plddt = {}
    for line in pdb.decode().splitlines():
        if line.startswith("ATOM") and line[12:16].strip() == "CA":
            plddt[int(line[22:26])] = float(line[60:66])
    res = {"af_model": meta["pdbUrl"], "global_plddt": meta.get("globalMetricValue"),
           "plddt_by_segment": {}}
    for a, b in ((1, 45), (46, 122), (123, 583), (584, 731)):
        v = [plddt[i] for i in range(a, b + 1) if i in plddt]
        res["plddt_by_segment"][f"{a}-{b}"] = round(sum(v) / len(v), 1)
    tk = submit(pdb, ["pdb100", "afdb-swissprot"])
    tid = tk["id"]
    print("ticket", tid, tk.get("status"), flush=True)
    for _ in range(120):
        st = json.loads(get(f"https://search.foldseek.com/api/ticket/{tid}"))
        if st["status"] in ("COMPLETE", "ERROR"):
            break
        time.sleep(10)
    if st["status"] != "COMPLETE":
        raise SystemExit(f"foldseek ticket {tid}: {st}")
    raw = json.loads(get(f"https://search.foldseek.com/api/result/{tid}/0", 300))
    (out / "foldseek_raw.json").write_text(json.dumps(raw))
    hits_out = {}
    for block in raw["results"]:
        db = block["db"]
        rows = []
        for aln in (block.get("alignments") or []):
            for h in (aln if isinstance(aln, list) else [aln]):
                rows.append({k: h.get(k) for k in ("target", "prob", "eval", "score", "seqId", "qStartPos", "qEndPos",
                                                   "dbStartPos", "dbEndPos", "qLen", "dbLen", "taxName")} |
                            {"qAln": h.get("qAln"), "dbAln": h.get("dbAln")})
        hits_out[db] = rows
    res["n_hits"] = {db: len(r) for db, r in hits_out.items()}
    # catalytic-residue transfer from AFDB-SwissProt hits with ACT_SITE annotations
    mapped = []
    for h in hits_out.get("afdb-swissprot", [])[:25]:
        m = re.search(r"AF-([A-Z0-9]+)-F", h["target"])
        if not m:
            continue
        acc = m.group(1)
        name, feats = uniprot_sites(acc)
        h["uniprot_name"] = name
        if not feats:
            continue
        qi, ti = h["qStartPos"], h["dbStartPos"]
        t2q = {}
        for qa, ta in zip(h["qAln"], h["dbAln"]):
            if qa != "-" and ta != "-":
                t2q[ti] = (qi, qa, ta)
            if qa != "-":
                qi += 1
            if ta != "-":
                ti += 1
        for f in feats:
            q = t2q.get(f["pos"])
            mapped.append({"target": acc, "target_name": name, "eval": h["eval"], "site": f["note"],
                           "target_pos": f["pos"], "target_res": q[2] if q else None,
                           "query_pos": q[0] if q else None, "query_res": q[1] if q else None})
    res["catalytic_transfer"] = mapped
    res["top_hits"] = {db: [{k: v for k, v in r.items() if k not in ("qAln", "dbAln")} for r in rows[:25]]
                       for db, rows in hits_out.items()}
    (out / "foldseek_results.json").write_text(json.dumps(res, indent=1))
    print("pLDDT", res["global_plddt"], res["plddt_by_segment"])
    for db, rows in res["top_hits"].items():
        print("==", db, res["n_hits"][db])
        for r in rows[:25]:
            print(f"  {r['target'][:60]:<60} E={r['eval']:.2g} prob={r['prob']} id={r['seqId']} q{r['qStartPos']}-{r['qEndPos']} "
                  f"t{r['dbStartPos']}-{r['dbEndPos']}/{r['dbLen']} {r.get('uniprot_name') or ''} [{r.get('taxName')}]")
    print("catalytic transfer:")
    for m in mapped:
        print("  ", m)


if __name__ == "__main__":
    main()
