"""Receipt store: one YAML per source. Entries keyed by id.

Fields: id, title, url, relevance (1-5, null if not assessed), assessed (bool),
rationale, method (rule:<name> | haiku | opus), plus optional extra fields.
"""
import yaml, pathlib, json, sys
OUT = pathlib.Path(__file__).resolve().parents[1]

def path(source): return OUT / f"{source}-receipts.yaml"

def load(source):
    p = path(source)
    if not p.exists(): return {"source": source, "entries": {}}
    d = yaml.load(p.read_text(), Loader=yaml.CSafeLoader)
    d["entries"] = {e["id"]: e for e in d["entries"]}
    return d

def save(d, description=None):
    OUT.mkdir(parents=True, exist_ok=True)
    if description: d["description"] = description
    out = {k: v for k, v in d.items() if k != "entries"}
    FIRST = ("id", "title", "relevance", "assessed", "rationale", "method")
    order = lambda e: {**{k: e[k] for k in FIRST if k in e}, **{k: v for k, v in e.items() if k not in FIRST}}
    out["entries"] = [order(e) for e in sorted(d["entries"].values(), key=lambda e: (-(e.get("relevance") or 0), str(e["id"])))]
    path(d["source"]).write_text(yaml.dump(out, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True, width=120))

def put(d, id, *, relevance, rationale, method, overwrite_method=None, **extra):
    """Set a receipt. Never overwrite a more careful judgement (opus > haiku > rule)."""
    rank = lambda m: 2 if m == "opus" else 1 if m == "haiku" else 0
    cur = d["entries"].get(id)
    if cur and cur.get("method") and rank(cur["method"]) > rank(method): return False
    e = dict(cur or {}); e.update(extra)
    e.update(id=id, relevance=relevance, assessed=relevance is not None, rationale=rationale, method=method)
    d["entries"][id] = e
    return True

def stats(source):
    import collections
    d = load(source); E = d["entries"].values()
    print(source, len(d["entries"]), collections.Counter(e.get("relevance") for e in E),
          collections.Counter(e["method"].split(":")[0] for e in E))

if __name__ == "__main__":
    for s in sys.argv[1:]: stats(s)
