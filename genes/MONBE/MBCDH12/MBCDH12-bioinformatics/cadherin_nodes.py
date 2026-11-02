"""Choanoflagellate cadherins carrying classical-cadherin GO terms by propagation.

For M. brevicollis A9V8Y4 (MBCDH12) and S. rosetta F2UD23, F2UFV3, F2USU1:
1. PANTHER tree (PTHR24027, public tree API): taxon label and leaf organisms
   of the PAINT nodes PTN000616280 and PTN008601603, and the ancestor path of
   the A9V8Y4 leaf (the only one of the four in the reference tree).
2. Pfam domains per protein (InterPro REST), and presence of PF01049
   (Cadherin_C, the beta-catenin-binding cytoplasmic domain).
3. Sequence checks (UniProt REST): SH2 FLVR-arginine motif, PTP
   (H/V)C(X5)R signature, counts of EC-repeat calcium-binding motifs in the
   ectodomain, and the transmembrane topology from UniProt.
No results are hardcoded; run with `python3 cadherin_nodes.py`.
"""
import collections
import json
import re
import urllib.request

UA = {"User-Agent": "curl/8"}
TREE = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR24027"
PFAM = "https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{}?page_size=200"
UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.json"
PROTEINS = ["A9V8Y4", "F2UD23", "F2UFV3", "F2USU1"]
NODES = ["PTN000616280", "PTN008601603"]


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def kids(node):
    k = node.get("children", {}).get("annotation_node", [])
    return [k] if isinstance(k, dict) else k


def walk(node, path, out):
    here = path + [node]
    out.append((node, here))
    for k in kids(node):
        walk(k, here, out)
    return out


def leaves_under(node):
    return [n for n, _ in walk(node, [], []) if not kids(n)]


print("## 1. PANTHER PTHR24027 tree")
try:
    root = get_json(TREE)["search"]["tree_topology"]["annotation_node"]
    allnodes = walk(root, [], [])
    print(f"root {root.get('persistent_id')} species={root.get('species')}")
    for pid in NODES:
        hit = [(n, p) for n, p in allnodes if n.get("persistent_id") == pid]
        if not hit:
            print(f"{pid}: not found in tree")
            continue
        n, p = hit[0]
        lv = leaves_under(n)
        orgs = collections.Counter(x.get("organism") for x in lv)
        print(f"{pid}: species={n.get('species')} event={n.get('event_type')} "
              f"subfamily={n.get('sf_name') or ''} leaves={len(lv)}")
        print("   leaf organisms:", "; ".join(f"{o}={c}" for o, c in sorted(orgs.items(), key=lambda t: str(t[0]))))
        print("   ancestors:", " > ".join(f"{a.get('persistent_id')}({a.get('species')})" for a in p[:-1]))
    for n, p in allnodes:
        gid = f"{n.get('gene_id') or ''} {n.get('node_name') or ''}"
        for acc in PROTEINS:
            if acc in gid:
                print(f"leaf {acc} [{gid.strip()}] organism={n.get('organism')}")
                print("   ancestors:", " > ".join(f"{a.get('persistent_id')}({a.get('species')})" for a in p[:-1]))
except Exception as e:  # report, do not invent
    print("tree fetch failed:", e)

print("\n## 2. Pfam domains (InterPro REST)")
for acc in PROTEINS:
    try:
        res = get_json(PFAM.format(acc))["results"]
        names = sorted({(r["metadata"]["accession"], r["metadata"]["name"]) for r in res})
        has = any(a == "PF01049" for a, _ in names)
        print(f"{acc}: " + ", ".join(f"{a}:{nm}" for a, nm in names))
        print(f"   PF01049 (Cadherin_C) present: {has}")
    except Exception as e:
        print(acc, "pfam fetch failed:", e)

print("\n## 3. Sequence features (UniProt REST)")
for acc in PROTEINS:
    try:
        d = get_json(UNIPROT.format(acc))
        seq = d["sequence"]["value"]
        feats = d.get("features", [])
        tm = [(f["location"]["start"]["value"], f["location"]["end"]["value"])
              for f in feats if f["type"] == "Transmembrane"]
        print(f"{acc}: length={len(seq)} TM={tm}")
        if tm:
            print(f"   cytoplasmic tail after TM: {len(seq) - tm[-1][1]} aa")
        ecto = seq[:tm[0][0]] if tm else seq
        # Canonical EC-repeat calcium-binding motifs (DXNDN, LDRE-type, DXD)
        dxndn = len(re.findall(r"D.N[DE][NHD]", ecto))
        ldre = len(re.findall(r"[LIVM]D[RYK]E", ecto))
        ncad = sum(1 for f in feats if f["type"] == "Domain" and f.get("description") == "Cadherin")
        print(f"   ectodomain cadherin repeats (UniProt Domain features)={ncad}; "
              f"DXN[DE][NHD] motifs={dxndn}; [LIVM]D[RYK]E motifs={ldre}")
        for f in feats:
            if f["type"] != "Domain":
                continue
            desc = f.get("description", "")
            s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
            sub = seq[s - 1:e]
            if desc == "SH2":
                m = [(s + x.start(), x.group()) for x in re.finditer(r"[FYWL][LIVM][VIL]R[DEQNS].", sub)]
                print(f"   SH2 {s}-{e}: FLVR-type motif(s) {m or 'none found'}")
                print(f"   SH2 sequence: {sub}")
            if desc.startswith("Tyrosine-protein phosphatase"):
                m = [(s + x.start(), x.group()) for x in re.finditer(r"[IVLH]HC..G..R[STC]", sub)]
                print(f"   PTP {s}-{e}: HCxxGxxR[ST] signature(s) {m or 'none found'}")
                m2 = [(s + x.start(), x.group()) for x in re.finditer(r"KNRY", sub)]
                print(f"   PTP KNRY (pTyr-recognition loop): {m2 or 'none found'}")
                m3 = [(s + x.start(), x.group()) for x in re.finditer(r"WPD", sub)]
                print(f"   PTP WPD loop: {m3 or 'none found'}")
    except Exception as e:
        print(acc, "uniprot fetch failed:", e)
