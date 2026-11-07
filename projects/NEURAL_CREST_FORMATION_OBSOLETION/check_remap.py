"""Check remapping TSVs for the GO:0014029 obsoletion.

For each row of remap/*.tsv (excluding *.input.tsv):
  * supporting_text must be a verbatim (whitespace-normalised) substring of the
    cached publications/PMID_<n>.md for supporting_reference;
  * every replacement id must be a live GO term whose label matches, or 'NTR'
    with one of the two proposed labels;
  * proposed_action must be one of REPLACE, REMOVE, UNDECIDED, OVER_ANNOTATED
    (gain-of-function-only evidence: not carried forward to any replacement);
  * reference_section_type, if set, must be a ManuscriptSection value, and TITLE
    or ABSTRACT must match where the quote actually sits in the cached record
    (cached full texts carry no internal headings, so body quotes stay blank);
  * source_error, if set, must be a CurationErrorTypeEnum value (see
    docs/curation_errors.md).

Usage: uv run python projects/NEURAL_CREST_FORMATION_OBSOLETION/check_remap.py [files...]
"""
import csv
import glob
import json
import pathlib
import re
import sys
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
NTR = {"neural plate border formation", "neural crest progenitor maintenance"}
ACTIONS = {"REPLACE", "REMOVE", "UNDECIDED", "OVER_ANNOTATED"}
_ENUMS = yaml.safe_load(open(ROOT / "src/ai_gene_review/schema/gene_review.yaml"))["enums"]
SECTIONS = set(_ENUMS["ManuscriptSection"]["permissible_values"])
ERROR_TYPES = set(_ENUMS["CurationErrorTypeEnum"]["permissible_values"])
_cache = {}


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def quote_section(ref, quote):
    """TITLE or ABSTRACT if the quote sits there in the cached record, else None.

    Cached full texts have no internal section headings, so a quote from the body
    cannot be placed and returns None.
    """
    m = re.match(r"PMID:(\d+)$", (ref or "").strip())
    pub = ROOT / f"publications/PMID_{m.group(1)}.md" if m else None
    if not quote or not pub or not pub.exists():
        return None
    text = pub.read_text()
    title = re.search(r"^# (.+)$", text, re.M)
    abstract = re.search(r"^## Abstract\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if title and norm(quote) in norm(title.group(1)):
        return "TITLE"
    if abstract and norm(quote) in norm(abstract.group(1)):
        return "ABSTRACT"
    return None


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
        sec, err = r.get("reference_section_type") or "", r.get("source_error") or ""
        if sec and sec not in SECTIONS:
            print(f"ERROR {where}: reference_section_type {sec!r} not a ManuscriptSection"); errors += 1
        elif sec in ("TITLE", "ABSTRACT") and quote and quote_section(ref, quote) != sec:
            print(f"ERROR {where}: quote is not in the {sec} of the cached record"); errors += 1
        if err and err not in ERROR_TYPES:
            print(f"ERROR {where}: source_error {err!r} not a CurationErrorTypeEnum value"); errors += 1
    print(f"{path}: {len(rows)} rows, {errors} errors")
    return errors


if __name__ == "__main__":
    files = sys.argv[1:] or [f for f in glob.glob(str(ROOT / "projects/NEURAL_CREST_FORMATION_OBSOLETION/remap/*.tsv"))
                             if not f.endswith(".input.tsv")]
    sys.exit(1 if sum(check(f) for f in files) else 0)
