"""Build the sequence -> structure test set from PDB entries released on or after 2026-08-01.

One protein entity per entry, X-ray, <= 2.5 A, 100-350 residues. Ground truth comes from the deposited mmCIF:
helix and strand ranges (_struct_conf, _struct_sheet_range), CA coordinates, title and keywords. All positions use
label_seq_id, i.e. numbering of the deposited construct sequence that the model is shown.
`prior_homologs` is the number of PDB entities released before 2026-06-01 with >= 30% sequence identity
(RCSB sequence search), a proxy for whether a similar structure could have been seen in training.
"""
import json, pathlib, random, shlex, time, urllib.request
rng = random.Random(20261118); HERE = pathlib.Path(__file__).parent
def http(url, body=None, raw=False):
    for a in range(4):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as r:
                t = r.read().decode()
                return t if raw else (json.loads(t) if t.strip() else {})
        except Exception as e: err = e; time.sleep(2 * (a + 1))
    print("FAIL", url, err); return None
def term(attr, op, val): return {"type": "terminal", "service": "text", "parameters": {"attribute": attr, "operator": op, "value": val}}
def loops(cif):
    """Minimal mmCIF reader: returns {category: list of row dicts} for loop_ and single-row categories."""
    toks = []; lines = cif.split("\n"); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith(";"):
            buf = [l[1:]]; i += 1
            while not lines[i].startswith(";"): buf.append(lines[i]); i += 1
            toks.append(("v", "".join(buf)))
        elif l.startswith("#") or not l.strip(): toks.append(("end", None))
        else:
            try: parts = shlex.split(l, posix=True)
            except ValueError: parts = l.split()
            for p in parts: toks.append(("k" if p.startswith("_") else ("loop" if p == "loop_" else "v"), p))
        i += 1
    out = {}; i = 0
    while i < len(toks):
        k, v = toks[i]
        if k == "loop":
            i += 1; keys = []
            while toks[i][0] == "k": keys.append(toks[i][1]); i += 1
            vals = []
            while i < len(toks) and toks[i][0] == "v": vals.append(toks[i][1]); i += 1
            cat = keys[0].split(".")[0]; n = len(keys)
            out[cat] = [dict(zip((x.split(".")[1] for x in keys), vals[j:j + n])) for j in range(0, len(vals), n)]
        elif k == "k" and i + 1 < len(toks) and toks[i + 1][0] == "v":
            cat, f = v.split("."); out.setdefault(cat, [{}])[0][f] = toks[i + 1][1]; i += 2
        else: i += 1
    return out
q = {"query": {"type": "group", "logical_operator": "and", "nodes": [
        term("rcsb_accession_info.initial_release_date", "greater_or_equal", "2026-08-01"),
        term("rcsb_entry_info.resolution_combined", "less_or_equal", 2.5),
        term("exptl.method", "exact_match", "X-RAY DIFFRACTION"),
        term("rcsb_entry_info.polymer_entity_count_protein", "equals", 1),
        term("rcsb_entry_info.polymer_entity_count", "equals", 1),
        term("entity_poly.rcsb_sample_sequence_length", "range", {"from": 100, "to": 350, "include_lower": True, "include_upper": True})]},
     "return_type": "entry", "request_options": {"paginate": {"start": 0, "rows": 2000}}}
ids = [r["identifier"] for r in http("https://search.rcsb.org/rcsbsearch/v2/query", q)["result_set"]]
print(len(ids), "candidate entries"); rng.shuffle(ids)
out = []; seen = set(); need = {"novel": 15, "known": 15}
GQL = '{entry(entry_id:"%s"){struct{title} struct_keywords{pdbx_keywords text} rcsb_accession_info{initial_release_date} polymer_entities{entity_poly{pdbx_seq_one_letter_code_can} rcsb_entity_source_organism{scientific_name} rcsb_polymer_entity_container_identifiers{uniprot_ids} rcsb_polymer_entity{pdbx_description}}}}'
for pid in ids:
    if not any(need.values()): break
    g = (http("https://data.rcsb.org/graphql", {"query": GQL % pid}) or {}).get("data", {}).get("entry")
    if not g: continue
    pe = g["polymer_entities"][0]; seq = "".join((pe["entity_poly"]["pdbx_seq_one_letter_code_can"] or "").split())
    if not seq or set(seq) - set("ACDEFGHIKLMNPQRSTVWY") or seq in seen: continue
    sq = {"query": {"type": "group", "logical_operator": "and", "nodes": [
            {"type": "terminal", "service": "sequence", "parameters": {"evalue_cutoff": 0.001, "identity_cutoff": 0.3, "sequence_type": "protein", "value": seq}},
            term("rcsb_accession_info.initial_release_date", "less", "2026-06-01")]},
          "return_type": "polymer_entity", "request_options": {"return_counts": True}}
    prior = http("https://search.rcsb.org/rcsbsearch/v2/query", sq)
    if prior is None: continue
    n = prior.get("total_count", 0)
    # strata: "novel" = no PDB entity at >= 30% identity released before June 2026; "known" = at least 20
    stratum = "novel" if n == 0 else ("known" if n >= 20 else None)
    if not stratum or not need[stratum]: continue
    c = loops(http(f"https://files.rcsb.org/download/{pid}.cif", raw=True) or "")
    ep = c.get("_entity_poly", [{}])[0]
    chain = ep.get("pdbx_strand_id", "A").split(",")[0]
    ca = {}; lab = None
    for a in c.get("_atom_site", []):
        if a["group_PDB"] == "ATOM" and a["label_atom_id"] == "CA" and a["auth_asym_id"] == chain and a.get("pdbx_PDB_model_num", "1") == "1" and a["label_seq_id"].isdigit():
            ca.setdefault(int(a["label_seq_id"]), [float(a["Cartn_x"]), float(a["Cartn_y"]), float(a["Cartn_z"])]); lab = a["label_asym_id"]
    if len(ca) < 0.8 * len(seq): continue
    hel = [[int(r["beg_label_seq_id"]), int(r["end_label_seq_id"])] for r in c.get("_struct_conf", []) if r.get("conf_type_id", "").startswith("HELX") and r.get("beg_label_asym_id") == lab]
    strd = sorted({(int(r["beg_label_seq_id"]), int(r["end_label_seq_id"])) for r in c.get("_struct_sheet_range", []) if r.get("beg_label_asym_id") == lab})
    if not hel and not strd: continue
    seen.add(seq); need[stratum] -= 1
    out.append(dict(pdb=pid, stratum=stratum, prior_homologs=n, released=g["rcsb_accession_info"]["initial_release_date"][:10], title=g["struct"]["title"],
        keywords=g["struct_keywords"]["pdbx_keywords"], keyword_text=g["struct_keywords"]["text"], description=pe["rcsb_polymer_entity"]["pdbx_description"],
        organism=[o["scientific_name"] for o in pe.get("rcsb_entity_source_organism") or []], uniprot=(pe["rcsb_polymer_entity_container_identifiers"] or {}).get("uniprot_ids"),
        sequence=seq, helices=hel, strands=[list(s) for s in strd], ca={str(k): v for k, v in sorted(ca.items())}))
    print(pid, stratum, n, len(seq), len(ca), len(hel), len(strd), out[-1]["organism"], "|", out[-1]["title"][:70], flush=True)
(HERE / "truth.json").write_text(json.dumps(out))
