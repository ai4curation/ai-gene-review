"""PP_1134 homology checks. (1) global alignment of dashboard query vs Q88NS1;
(2) NCBI BLAST of Q88NS1 against swissprot and pdbaa.
Usage: python3 -I homology.py OUTDIR"""
import json, os, sys, time, urllib.request, urllib.parse
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
def fasta(p):
    return "".join(l.strip() for l in open(p) if not l.startswith(">"))
def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "curl/8.5.0"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read().decode()
q = fasta(os.path.join(here, "query_dashboard.fasta"))
up = get("https://rest.uniprot.org/uniprotkb/Q88NS1.fasta")
s = "".join(up.splitlines()[1:])
# simple Needleman-Wunsch with identity scoring (small proteins, fine)
def nw(a, b, gap=-2, mm=-1, ma=2):
    n, m = len(a), len(b)
    S = [[0]*(m+1) for _ in range(n+1)]; T = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): S[i][0] = 0; T[i][0] = 1   # free end gaps
    for j in range(1, m+1): S[0][j] = 0; T[0][j] = 2
    for i in range(1, n+1):
        for j in range(1, m+1):
            d = S[i-1][j-1] + (ma if a[i-1] == b[j-1] else mm)
            u = S[i-1][j] + (gap if j < m else 0); l = S[i][j-1] + (gap if i < n else 0)
            S[i][j], T[i][j] = max((d, 0), (u, 1), (l, 2))
    i, j, pairs = n, m, []
    while i > 0 or j > 0:
        t = T[i][j] if i > 0 and j > 0 else (1 if i > 0 else 2)
        if t == 0: pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif t == 1: i -= 1
        else: j -= 1
    return pairs[::-1]
pairs = nw(q, s)
ident = sum(q[i] == s[j] for i, j in pairs)
mism = [{"query_pos": i+1, "query": q[i], "subject_pos": j+1, "subject": s[j]} for i, j in pairs if q[i] != s[j]]
res = {"query_len": len(q), "subject_len": len(s), "aligned_pairs": len(pairs), "identical": ident,
       "pct_identity_aligned": round(100*ident/len(pairs), 2),
       "query_aligned_range": [pairs[0][0]+1, pairs[-1][0]+1], "subject_aligned_range": [pairs[0][1]+1, pairs[-1][1]+1],
       "query_unaligned_nterm": q[:pairs[0][0]], "mismatches": mism}
print(json.dumps(res, indent=1))
def blast(db):
    """NCBI BLAST URL API (EBI JDispatcher refused jobs on 2026-10-30: fair-use block)."""
    import re
    B = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"
    data = urllib.parse.urlencode({"CMD": "Put", "PROGRAM": "blastp", "DATABASE": db, "QUERY": s,
                                   "EXPECT": "1e-5", "HITLIST_SIZE": 100, "TOOL": "ai-gene-review", "EMAIL": "noreply@example.org"}).encode()
    r = get(B, data)
    rid = re.search(r"RID = (\S+)", r).group(1)
    st = None
    for _ in range(120):
        time.sleep(15)
        r = get(B + "?CMD=Get&FORMAT_OBJECT=SearchInfo&RID=" + rid)
        m = re.search(r"Status=(\w+)", r); st = m.group(1) if m else None
        if st in ("READY", "FAILED", "UNKNOWN"): break
    r = get(B + "?CMD=Get&FORMAT_TYPE=JSON2_S&RID=" + rid)
    js = json.loads(r)
    srch = js["BlastOutput2"][0]["report"]["results"]["search"]
    if "Error" in srch.get("message", ""):
        raise RuntimeError(srch["message"])
    hits = []
    for h in srch.get("hits", []):
        d = h["description"][0]; hsp = h["hsps"][0]
        hits.append({"acc": d.get("accession"), "desc": d.get("title"), "os": d.get("sciname"), "len": h.get("len"),
                     "identity": round(100*hsp["identity"]/hsp["align_len"], 1), "align_len": hsp["align_len"],
                     "q_from": hsp["query_from"], "q_to": hsp["query_to"], "evalue": hsp["evalue"]})
    return {"rid": rid, "status": st, "query": "Q88NS1", "db": db, "hits": hits}
res["blast_swissprot"] = blast("swissprot")
res["blast_pdb"] = blast("pdbaa")
for k in ("blast_swissprot", "blast_pdb"):
    print(k, res[k]["status"])
    for h in res[k]["hits"][:25]:
        print(" ", h["acc"], h["identity"], h["align_len"], h["evalue"], h["desc"], "|", h["os"])
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
