"""List the leaves that receive IBA annotations from the PAINT nodes seeded by
XcpS, XcpW and XcpV, and classify them by the protein name UniProt gives them.

Usage: python node_leaves.py [outdir]
Queries the QuickGO annotation API (withFrom=<PTN node>, goId=<term>).
Names are mostly automatic (UniRule/ProtNLM) and are used only as a coarse
indicator of what kind of protein sits under each node.
"""
import collections, json, os, re, ssl, sys, urllib.request

NODES = [
    ("PTN000768597", "GO:0015628", "XcpS/GspF seed"),
    ("PTN002218419", "GO:0015628", "IBA node on XcpW/GspJ in current GOA"),
    ("PTN002446812", "GO:0015628", "XcpW/GspJ seed node in PAINT seed file"),
    ("PTN002446181", "GO:0015627", "XcpV/GspI seed"),
]
CA = os.environ.get("REQUESTS_CA_BUNDLE") or "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()


def fetch(node, go):
    prots, page = {}, 1
    while True:
        url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
               f"withFrom={node}&goId={go}&limit=200&page={page}&includeFields=name")
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        res = json.load(urllib.request.urlopen(req, context=CTX, timeout=90))
        for r in res["results"]:
            prots[r["geneProductId"]] = (r.get("symbol") or "", r.get("name") or "")
        if page >= res["pageInfo"]["total"]:
            break
        page += 1
    return prots


def classify(sym, name):
    t = f"{sym} {name}"
    if re.search(r"secretion system|gsp[A-Z]|xcp[A-Z]|eps[A-Z]|exe[A-Z]|out[A-Z]|lsp[A-Z]|xps[A-Z]|xcs[A-Z]", t):
        return "T2SS-named"
    if re.search(r"\bpil[A-Z]\b|\bpil[A-Z]_\d|[Pp]ilus|[Ff]imbri|hofC|tcpE|msh[A-Z]|Tt1218|^[Pp]ilin$|\bPilin\b", t):
        return "T4P/MSHA/TCP-named"
    return "generic/other"


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out, "node_leaves.tsv"), "w") as fh, \
         open(os.path.join(out, "node_summary.txt"), "w") as sm:
        fh.write("node\tgo_id\tprotein\tsymbol\tname\tclass\n")
        for node, go, note in NODES:
            try:
                prots = fetch(node, go)
            except Exception as e:  # report, do not invent
                sm.write(f"{node} {go} ({note}): query failed: {e}\n")
                continue
            c = collections.Counter()
            for acc, (s, n) in sorted(prots.items()):
                k = classify(s, n)
                c[k] += 1
                fh.write(f"{node}\t{go}\t{acc}\t{s}\t{n}\t{k}\n")
            line = (f"{node} {go} ({note}): {len(prots)} proteins; "
                    + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))
            sm.write(line + "\n")
            print(line)


if __name__ == "__main__":
    main()
