"""Check remapping TSVs for the GO:0014029 obsoletion.

For each row of remap/*.tsv (excluding *.input.tsv):
  * supporting_text must be a verbatim (whitespace-normalised) substring of the
    cached publications/PMID_<n>.md for supporting_reference;
  * every replacement id must be a live GO term whose label matches, or 'NTR'
    with one of the two proposed labels;
  * proposed_action must be one of REPLACE, REMOVE, UNDECIDED, OVER_ANNOTATED
    (gain-of-function-only evidence: not carried forward to any replacement).

Usage: uv run python projects/NEURAL_CREST_FORMATION_OBSOLETION/check_remap.py [files...]
"""
import csv
import glob
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
NTR = {"neural plate border formation", "neural crest progenitor maintenance"}
ACTIONS = {"REPLACE", "REMOVE", "UNDECIDED", "OVER_ANNOTATED"}
_cache = {}


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def go_label(gid):
    if gid not in _cache:
        url = f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{gid}"
        with urllib.request.urlopen(url, timeout=60) as r:
            res = json.load(r)["results"]
        _cache[gid] = (res[0]["name"], res[0].get("isObsolete", False)) if res else (None, None)
    return _cache[gid]


def check(path):
    errors = 0
    rows = list(csv.DictReader(open(path), delimiter="\t"))
    for i, r in enumerate(rows, 2):
        where = f"{path}:{i} {r.get('symbol')} {r.get('reference')}"
        act = r.get("proposed_action", "")
        if act not in ACTIONS:
            print(f"ERROR {where}: proposed_action {act!r}"); errors += 1
        ids = [x for x in (r.get("replacement_ids") or "").split(";") if x.strip()]
        labels = [x.strip() for x in (r.get("replacement_labels") or "").split(";") if x.strip()]
        if act == "REPLACE" and not ids:
            print(f"ERROR {where}: REPLACE without replacement_ids"); errors += 1
        if len(ids) != len(labels):
            print(f"ERROR {where}: {len(ids)} ids vs {len(labels)} labels"); errors += 1
        for gid, lab in zip(ids, labels):
            gid = gid.strip()
            if gid == "NTR":
                if lab not in NTR:
                    print(f"ERROR {where}: NTR label {lab!r} not a proposed term"); errors += 1
                continue
            name, obs = go_label(gid)
            if name is None or obs:
                print(f"ERROR {where}: {gid} missing or obsolete"); errors += 1
            elif norm(name) != norm(lab):
                print(f"ERROR {where}: {gid} label {lab!r} != {name!r}"); errors += 1
        ref, quote = r.get("supporting_reference", ""), r.get("supporting_text", "")
        if quote:
            m = re.match(r"PMID:(\d+)$", ref.strip())
            pub = ROOT / f"publications/PMID_{m.group(1)}.md" if m else None
            if not pub or not pub.exists():
                print(f"ERROR {where}: no cached publication for {ref!r}"); errors += 1
            elif norm(quote) not in norm(pub.read_text()):
                print(f"ERROR {where}: quote not found in {pub.name}"); errors += 1
        elif act != "UNDECIDED":
            print(f"ERROR {where}: no supporting_text for a {act} decision"); errors += 1
    print(f"{path}: {len(rows)} rows, {errors} errors")
    return errors


if __name__ == "__main__":
    files = sys.argv[1:] or [f for f in glob.glob(str(ROOT / "projects/NEURAL_CREST_FORMATION_OBSOLETION/remap/*.tsv"))
                             if not f.endswith(".input.tsv")]
    sys.exit(1 if sum(check(f) for f in files) else 0)
