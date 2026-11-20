"""Add one receipt per extra copy where several drive files share an identical path."""
import sys, json, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent)); import rcpt
S = pathlib.Path(__file__).parent.parent
M = json.load(open(S / "drive_all.json")); d = rcpt.load("go-drive")
by = collections.defaultdict(list)
for x in M: by[x["Path"]].append(x)
n = 0
for p, xs in by.items():
    if len(xs) < 2: continue
    base = d["entries"]["drive:" + p]
    for x in xs:
        if x["ID"] == base.get("drive_id"): continue
        e = dict(base); e.pop("first_pass", None)
        rcpt.put(d, f"drive:{p}#{x['ID']}", relevance=base["relevance"], method="rule:duplicate-filename",
                 rationale="Another file with the identical name in the same folder (only one copy could be downloaded); receipt mirrors "
                           f"the scored copy: {base['rationale']}",
                 **{k: v for k, v in e.items() if k not in ("id", "relevance", "rationale", "method", "assessed", "drive_id", "url", "modified")},
                 **{"drive_id": x["ID"], "url": f"https://drive.google.com/open?id={x['ID']}", "modified": (x.get("ModTime") or "")[:10]})
        n += 1
rcpt.save(d); print("added", n, "total", len(d["entries"]), "manifest", len(M))
