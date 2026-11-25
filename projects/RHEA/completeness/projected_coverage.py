"""Coverage of Swiss-Prot RHEA masters by GO HEAD xrefs plus staged SSSOM rows (exact/broad to a GO id)."""
import sys, json, yaml, collections
D, SS = sys.argv[1], sys.argv[2]
rows = json.load(open(f"{D}/coverage.json"))["rows"]
staged = {}
for m in yaml.safe_load(open(SS))["mappings"]:
    if str(m["object_id"]).startswith("GO:") and m["predicate_id"] in ("skos:exactMatch", "skos:broadMatch"):
        staged[m["subject_id"].split(":")[1]] = True
c = collections.Counter(); e = collections.Counter()
for rid, cat, n in rows:
    k = "covered_in_GO" if cat in ("exact", "go_broader") else ("staged" if rid in staged else "open")
    c[k] += 1; e[k] += n
for k in ("covered_in_GO", "staged", "open"): print(f"{k:14s} {c[k]:6d} reactions {e[k]:7d} entry-reaction pairs")
