"""Apply scores/*.jsonl to receipts. File name prefix -> source. method from file name (haiku|opus).
Reports items in batch files that have no receipt yet."""
import json, sys, pathlib, re, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent)); import rcpt
S = pathlib.Path(__file__).parent.parent
SRC = {"gh": ("go-annotation-issues", "gh/batches"), "wiki": ("go-wiki", "wiki/batches"),
       "papers": ("papers", "papers/batches"), "drive": ("go-drive", "drive/batches")}
for key, (source, bdir) in SRC.items():
    files = sorted((S / "scores").glob(f"{key}-*.jsonl"))
    if not files: continue
    d = rcpt.load(source); n = collections.Counter(); bad = []
    for f in files:
        method = "opus" if "-opus-" in f.name else "haiku"
        for line in f.read_text().splitlines():
            if not line.strip(): continue
            j = json.loads(line)
            if j["id"] not in d["entries"]: bad.append(j["id"]); continue
            r = j["relevance"]; assert r in (1, 2, 3, 4, 5), j
            if rcpt.put(d, j["id"], relevance=r, rationale=j["rationale"].strip(), method=method): n[method] += 1
    rcpt.save(d)
    # gaps: items in scored batches still pending
    missing = {}
    for f in files:
        b = re.sub(r"^\w+-(opus-)?", "", f.stem) if "-opus-" not in f.name else None
        if not b: continue
        ids = re.findall(r"^=== ITEM (.+)$", (S / bdir / f"{b}.md").read_text(), re.M)
        m = [i for i in ids if d["entries"][i]["method"] == "rule:pending"]
        if m: missing[b] = m
    pend = sum(e["method"] == "rule:pending" for e in d["entries"].values())
    print(source, dict(n), "unknown ids:", bad[:5], "pending:", pend, "gaps:", {k: len(v) for k, v in missing.items()})
    json.dump(missing, open(S / f"scores/{key}-gaps.json", "w"))

# careful (opus) second-pass files: route by id prefix
vfiles = sorted((S / "scores").glob("verify-*.jsonl"))
if vfiles:
    route = lambda i: ("go-wiki" if i.startswith("wiki:") else "go-annotation-issues" if i.startswith("issue:")
                       else "go-drive" if i.startswith("drive:") else "papers")
    docs = {}; n = collections.Counter(); bad = []
    for f in vfiles:
        for line in f.read_text().splitlines():
            if not line.strip(): continue
            j = json.loads(line); src = route(j["id"])
            d = docs.setdefault(src, rcpt.load(src))
            if j["id"] not in d["entries"]: bad.append(j["id"]); continue
            prev = d["entries"][j["id"]]
            extra = {"first_pass": {"relevance": prev.get("relevance"), "rationale": prev.get("rationale")}} if prev["method"] == "haiku" else {}
            rcpt.put(d, j["id"], relevance=int(j["relevance"]), rationale=j["rationale"].strip(), method="opus", **extra); n[src] += 1
    for d in docs.values(): rcpt.save(d)
    print("opus verify:", dict(n), "unknown:", bad[:5])
