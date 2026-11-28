"""Score the catalytic-activity calls in results/*.jsonl against truth.json."""
import collections, glob, json, pathlib
HERE = pathlib.Path(__file__).parent
T = {t["accession"]: t for t in json.loads((HERE / "truth.json").read_text())}
def positions(ans, key):
    return {d.get("position") for d in (ans.get(key) or []) if isinstance(d, dict)}
for f in sorted(glob.glob(str(HERE / "results" / "*.jsonl"))):
    R = [json.loads(l) for l in open(f)]; ok = [r for r in R if r.get("ans")]
    print(f"\n== {pathlib.Path(f).stem}: {len(R)} calls, {len(R)-len(ok)} unparsed, effort {ok[0]['effort']}, cost ${sum(r.get('cost') or 0 for r in R):.2f}")
    rows = collections.defaultdict(collections.Counter); flagged = collections.Counter(); still = collections.Counter(); wtsite = collections.Counter()
    for r in ok:
        t = T[r["accession"]]; a = r["ans"]; key = (t["group"], r["variant"])
        rows[key][str(a.get("catalytically_active")).lower()] += 1
        site = {"asp_to_asn": t.get("asp"), "lys_to_met": t.get("lys"), "site_to_ala": t.get("site")}.get(r["variant"])
        if site:   # mutant: was the mutated position reported as substituted, or still listed as an intact catalytic residue?
            flagged[key] += site in positions(a, "substituted_or_missing")
            still[key] += site in positions(a, "catalytic_residues") and site not in positions(a, "substituted_or_missing")
        elif t["group"] in ("kinase", "enzyme"):   # wild type: is the curated catalytic position among those listed?
            want = [t["asp"], t["lys"]] if t["group"] == "kinase" else [t["site"]]
            wtsite[key] += all(w in positions(a, "catalytic_residues") for w in want)
    for key in sorted(rows):
        n = sum(rows[key].values()); c = rows[key]
        extra = f"; curated catalytic position(s) listed {wtsite[key]}/{n}" if key[1] == "wt" and key[0] != "pseudo" else (
                f"; mutated position flagged as substituted {flagged[key]}/{n}, still listed as intact {still[key]}/{n}" if key[1] != "wt" else "")
        print(f"  {key[0]:7s} {key[1]:11s} n={n}: active yes {c['yes']}  no {c['no']}  uncertain {c['uncertain']}{extra}")
