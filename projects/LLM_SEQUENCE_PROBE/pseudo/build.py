"""Build the pseudoenzyme test set from UniProt Swiss-Prot. Writes truth.json beside this file.

Three groups:
  kinase   - active protein kinases with a curated proton-acceptor Asp and ATP-binding Lys; each also as two
             single-residue in-silico dead mutants (catalytic Asp->Asn, ATP Lys->Met)
  pseudo   - natural kinase-fold proteins whose Swiss-Prot name says "inactive" (not human/mouse/rat)
  enzyme   - non-kinase enzymes with a curated active site; each also with the first active-site residue -> Ala
"""
import json, random, time, urllib.parse, urllib.request, pathlib
rng = random.Random(20261118)
def get(url):
    for a in range(4):
        try:
            with urllib.request.urlopen(url, timeout=90) as r: return json.load(r)
        except Exception as e: err = e; time.sleep(2 * (a + 1))
    raise SystemExit(f"FAIL {url} {err}")
def search(q, n=500):
    return get("https://rest.uniprot.org/uniprotkb/search?format=json&size=%d&query=%s" % (n, urllib.parse.quote(q)))["results"]
NOT_MODEL = "NOT organism_id:9606 NOT organism_id:10090 NOT organism_id:10116"
def name(r): return r["proteinDescription"]["recommendedName"]["fullName"]["value"]
def base(r, group): return dict(group=group, accession=r["primaryAccession"], name=name(r), organism=r["organism"]["scientificName"], wt=r["sequence"]["value"])
def mut(seq, pos, new): return seq[:pos - 1] + new + seq[pos:]
out = []
# active kinases
picked = 0
for r in rng.sample(search(f'reviewed:true AND family:"protein kinase superfamily" AND ft_act_site:* AND length:[280 TO 650] AND existence:1 {NOT_MODEL}'), 300):
    if "nactive" in name(r) or picked == 20: continue
    seq = r["sequence"]["value"]; fs = r["features"]
    asp = [f["location"]["start"]["value"] for f in fs if f["type"] == "Active site" and "Proton acceptor" in f.get("description", "")]
    lys = [f["location"]["start"]["value"] for f in fs if f["type"] == "Binding site" and f.get("ligand", {}).get("name") == "ATP"
           and f["location"]["start"]["value"] == f["location"]["end"]["value"]]
    if len(asp) != 1 or len(lys) != 1 or seq[asp[0] - 1] != "D" or seq[lys[0] - 1] != "K": continue
    d = base(r, "kinase"); d.update(asp=asp[0], lys=lys[0], variants={"wt": seq, "asp_to_asn": mut(seq, asp[0], "N"), "lys_to_met": mut(seq, lys[0], "M")})
    out.append(d); picked += 1
# natural pseudokinases
ps = [r for r in search(f'reviewed:true AND protein_name:inactive AND family:"protein kinase superfamily" AND length:[280 TO 900] {NOT_MODEL}') if "nactive" in name(r)]
for r in rng.sample(ps, min(20, len(ps))):
    d = base(r, "pseudo"); d["variants"] = {"wt": r["sequence"]["value"]}
    d["caution"] = [c["texts"][0]["value"] for c in r.get("comments", []) if c["commentType"] in ("CAUTION", "DOMAIN") and c.get("texts")]
    out.append(d)
# other enzymes
picked = 0
for r in rng.sample(search(f'reviewed:true AND ft_act_site:* AND ec:* AND length:[150 TO 450] AND existence:1 NOT family:"protein kinase superfamily" {NOT_MODEL}'), 300):
    if picked == 20: break
    seq = r["sequence"]["value"]; acts = [f for f in r["features"] if f["type"] == "Active site" and f["location"]["start"].get("value")]
    if not acts or seq[acts[0]["location"]["start"]["value"] - 1] == "A": continue
    p = acts[0]["location"]["start"]["value"]
    d = base(r, "enzyme"); d.update(site=p, site_residue=seq[p - 1], site_role=acts[0].get("description", ""),
        ec=[e["value"] for e in r["proteinDescription"]["recommendedName"].get("ecNumbers", [])], variants={"wt": seq, "site_to_ala": mut(seq, p, "A")})
    out.append(d); picked += 1
for d in out: del d["wt"]
pathlib.Path(__file__).with_name("truth.json").write_text(json.dumps(out, indent=1))
import collections; print(collections.Counter(d["group"] for d in out))
for d in out: print(d["group"], d["accession"], d["organism"][:28], "|", d["name"][:70])
