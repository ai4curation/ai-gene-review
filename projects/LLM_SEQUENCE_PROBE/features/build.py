"""Build a ground-truth set: random TrEMBL bacterial/archaeal proteins (set B) + DUF probe proteins (set A)."""
import csv, json, pathlib, random, sys, urllib.request, urllib.parse, time
S = sys.argv[1]; rng = random.Random(20261118)
def get(url):
    for a in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r: return json.load(r)
        except Exception as e: err = e; time.sleep(2 * (a + 1))
    print("FAIL", url, err, file=sys.stderr); return None
accs = []
# set B: random accession prefixes -> unbiased-ish draw from TrEMBL
while len(accs) < 45:
    L = rng.randint(150, 450); srt = rng.choice(["accession", "mass", "organism_name", "gene"]) + rng.choice([" asc", " desc"])
    q = f"(taxonomy_id:2 OR taxonomy_id:2157) AND reviewed:false AND length:[{L} TO {L}] AND fragment:false AND database:pfam"
    d = get("https://rest.uniprot.org/uniprotkb/search?format=json&size=25&fields=accession&sort=" + urllib.parse.quote(srt) + "&query=" + urllib.parse.quote(q))
    hits = [r["primaryAccession"] for r in (d or {}).get("results", [])]
    if not hits: break
    accs.append(("B", rng.choice(hits)))
rows = list(csv.DictReader(open(f"{S}/data/confirm_sequences.tsv"), delimiter="\t"))
accs += [("A", r["accession"]) for r in rng.sample(rows, 15)]
out = []
for st, acc in accs:
    u = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    ip = get(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{acc}") or {"results": []}
    if not u: continue
    pf = []
    for e in ip["results"]:
        m = e["metadata"]
        short = (get(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{m['accession']}") or {}).get("metadata", {}).get("name", {})
        for loc in e["proteins"][0]["entry_protein_locations"]:
            pf.append(dict(accession=m["accession"], name=m["name"], short=short.get("short") if isinstance(short, dict) else None,
                           start=loc["fragments"][0]["start"], end=loc["fragments"][-1]["end"]))
    feats = u.get("features", [])
    pd = u["proteinDescription"]
    names = pd.get("recommendedName") or (pd.get("submissionNames") or [{}])[0]
    out.append(dict(set=st, accession=acc, organism=u["organism"]["scientificName"], sequence=u["sequence"]["value"],
        name=names.get("fullName", {}).get("value"), ec=[e["value"] for e in names.get("ecNumbers", [])],
        pfam=pf, tm=[(f["location"]["start"]["value"], f["location"]["end"]["value"]) for f in feats if f["type"] == "Transmembrane"],
        signal=any(f["type"] == "Signal" for f in feats),
        go=[(x["id"], next(p["value"] for p in x["properties"] if p["key"] == "GoTerm")) for x in u["uniProtKBCrossReferences"] if x["database"] == "GO"]))
json.dump(out, open(pathlib.Path(__file__).with_name("truth.json"), "w"), indent=1)
import collections
print(len(out), collections.Counter(o["set"] for o in out), "with TM:", sum(bool(o["tm"]) for o in out), "signal:", sum(o["signal"] for o in out), "EC:", sum(bool(o["ec"]) for o in out))
for o in out[:12]: print(o["set"], o["accession"], o["name"], [p["short"] for p in o["pfam"]], len(o["tm"]))
