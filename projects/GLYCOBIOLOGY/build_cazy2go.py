#!/usr/bin/env python3
"""Generate a CAZy-family -> GO molecular-function mapping (SSSOM), reproducibly.

This extends the hand-curated seed (``cazy2go.sssom.yaml``, 5 exemplar GT families)
to ALL CAZy enzyme families for which a relationship can be derived from public
data, by chaining two authoritative sources:

    CAZy family  --(reviewed Swiss-Prot xrefs)-->  EC number  --(ec2go)-->  GO MF

No mapping is hand-typed or invented: every row is the join of a UniProtKB
(reviewed) CAZy<->EC cross-reference with the GO ``ec2go`` external mapping.

Sources (fetched live):
  * UniProtKB REST: reviewed entries carrying both a CAZy xref and an EC number
    (``reviewed:true AND database:cazy AND ec:*``), fields accession,ec,xref_cazy.
  * GO ec2go: https://current.geneontology.org/ontology/external2go/ec2go

Predicate logic (mirrors the curated seed / interpro2go):
  * A family whose member ECs resolve (via ec2go) to exactly ONE GO MF term is
    mono-specific at GO altitude  ->  skos:exactMatch.
  * A family resolving to MULTIPLE GO MF terms is poly-specific; each GO term is
    NARROWER than the family  ->  skos:narrowMatch (one row per term). These are
    the families where CAZy family alone is too coarse and subfamily/EC
    resolution is required before propagating.

Caveat (the redundancy property): because each row is derived *through* an EC
that already reaches GO via ec2go, every generated row is by construction
"EC-reachable". Its value is the same as interpro2go's: it lets a protein be
annotated from CAZy family membership even when it lacks an EC/ec2go annotation.
The marginal-vs-ec2go contribution must still be closure-filtered per the
RHEA EC-masking method (see GLYCOBIOLOGY-resource-reuse.md).

Usage:
    uv run python projects/GLYCOBIOLOGY/build_cazy2go.py \
        -o projects/GLYCOBIOLOGY/cazy2go.generated.sssom.yaml
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

EC2GO_URL = "https://current.geneontology.org/ontology/external2go/ec2go"
UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
UA = {"User-Agent": "ai-gene-review-cazy2go/1.0"}


def _get(url: str) -> urllib.request.addinfourl:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)


def load_ec2go() -> dict[str, list[tuple[str, str]]]:
    """Return {EC_number: [(GO_id, GO_label), ...]} from the GO ec2go file.

    ec2go lines look like:
        EC:2.4.1.101 > GO:alpha-1,3-mannosyl... ; GO:0003827
    """
    text = _get(EC2GO_URL).read().decode("utf-8", "replace")
    out: dict[str, list[tuple[str, str]]] = defaultdict(list)
    line_re = re.compile(r"^EC:(\S+)\s*>\s*GO:(.+?)\s*;\s*(GO:\d+)\s*$")
    for line in text.splitlines():
        if line.startswith("!"):
            continue
        m = line_re.match(line.strip())
        if not m:
            continue
        ec, go_label, go_id = m.group(1), m.group(2).strip(), m.group(3)
        out[ec].append((go_id, go_label))
    return out


def load_cazy_ec() -> tuple[dict[str, Counter], dict[str, set[str]]]:
    """Page UniProtKB for reviewed CAZy<->EC pairs.

    Returns:
        fam_ec:      {CAZy_family: Counter({EC: n_reviewed_entries})}
        fam_members: {CAZy_family: set(accessions)}  (for member counts)
    """
    fam_ec: dict[str, Counter] = defaultdict(Counter)
    fam_members: dict[str, set[str]] = defaultdict(set)
    params = {
        "query": "reviewed:true AND database:cazy AND ec:*",
        "fields": "accession,ec,xref_cazy",
        "format": "tsv",
        "size": "500",
    }
    url = UNIPROT_URL + "?" + urllib.parse.urlencode(params)
    n_rows = 0
    while url:
        resp = _get(url)
        body = resp.read().decode("utf-8", "replace")
        lines = body.splitlines()
        for line in lines[1:]:  # skip header
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            acc, ec_field, cazy_field = parts[0], parts[1], parts[2]
            ecs = [e.strip() for e in ec_field.split(";") if e.strip()]
            fams = [f.strip() for f in cazy_field.split(";") if f.strip()]
            if not ecs or not fams:
                continue
            n_rows += 1
            for fam in fams:
                fam_members[fam].add(acc)
                for ec in ecs:
                    fam_ec[fam][ec] += 1
        # follow cursor pagination via Link header
        link = resp.headers.get("Link", "")
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    print(f"  UniProt: {n_rows} reviewed CAZy+EC entries -> {len(fam_ec)} families", file=sys.stderr)
    return fam_ec, fam_members


# Generic high-altitude MF parents that ec2go sometimes attaches to a family member's EC.
# When a family ALSO has a more specific child term, these are redundant and dropped (the
# "trivial redundancy filter"); kept only when they are the sole term a family resolves to.
GENERIC_PARENTS = {
    "GO:0016740",  # transferase activity
    "GO:0016757",  # glycosyltransferase activity
    "GO:0016758",  # hexosyltransferase activity / pentosyltransferase
    "GO:0016798",  # hydrolase activity, acting on glycosyl bonds
    "GO:0004553",  # hydrolase activity, hydrolyzing O-glycosyl compounds
}


def build_rows(fam_ec, fam_members, ec2go):
    """Build SSSOM mapping rows (list of dicts), sorted by family."""
    rows = []
    stats = Counter()

    def fam_sort_key(f: str):
        m = re.match(r"([A-Za-z]+)(\d+)", f)
        return (m.group(1), int(m.group(2))) if m else (f, 0)

    for fam in sorted(fam_ec, key=fam_sort_key):
        # collect GO terms reachable from this family's ECs
        go_terms: dict[str, str] = {}  # go_id -> label
        go_support: dict[str, list[str]] = defaultdict(list)  # go_id -> [ECs]
        for ec, _n in fam_ec[fam].most_common():
            for go_id, go_label in ec2go.get(ec, []):
                go_terms.setdefault(go_id, go_label)
                go_support[go_id].append(ec)
        if not go_terms:
            stats["families_no_ec2go"] += 1
            continue
        # trivial redundancy filter: drop generic MF parents when a specific child is present
        specific = {g: lbl for g, lbl in go_terms.items() if g not in GENERIC_PARENTS}
        if specific and len(specific) < len(go_terms):
            dropped = set(go_terms) - set(specific)
            stats["generic_parent_rows_filtered"] += len(dropped)
            go_terms = specific
        n_members = len(fam_members[fam])
        n_ec = len(fam_ec[fam])
        single = len(go_terms) == 1
        stats["families_mapped"] += 1
        stats["families_exact" if single else "families_narrow"] += 1
        for go_id, go_label in sorted(go_terms.items()):
            predicate = "skos:exactMatch" if single else "skos:narrowMatch"
            ecs = sorted(set(go_support[go_id]))
            rows.append({
                "subject_id": f"CAZy:{fam}",
                "subject_label": fam,
                "predicate_id": predicate,
                "predicate_label": "exact match" if single else "narrow match",
                "object_id": go_id,
                "object_label": go_label,
                "mapping_justification": "semapv:CompositeMatching",
                "comment": (
                    f"Derived: CAZy {fam} -> EC {','.join(ecs)} (ec2go) -> {go_id}. "
                    f"{n_members} reviewed Swiss-Prot member(s), {n_ec} distinct EC(s) in family. "
                    + ("Mono-specific at GO altitude." if single
                       else "Poly-specific family: term applies to a subfamily; resolve subfamily/EC before propagating.")
                ),
            })
            stats["rows"] += 1
    return rows, stats


def write_sssom(rows, stats, out_path):
    import yaml
    header = (
        "# CAZy family -> GO molecular-function mapping (SSSOM) -- GENERATED, DO NOT HAND-EDIT\n"
        "#\n"
        "# Auto-generated by projects/GLYCOBIOLOGY/build_cazy2go.py. Each row is the live join of a\n"
        "# reviewed UniProtKB CAZy<->EC cross-reference with the GO ec2go external mapping -- no row is\n"
        "# hand-typed. The hand-curated, review-backed rows live in the sibling cazy2go.sssom.yaml.\n"
        "#\n"
        "# exactMatch = family's ECs resolve to a single GO MF (mono-specific); narrowMatch = family is\n"
        "# poly-specific and the GO term applies to a subfamily only (needs subfamily/EC resolution).\n"
        "# Every row is EC-reachable by construction; closure-filter against ec2go for marginal value\n"
        "# (see GLYCOBIOLOGY-resource-reuse.md).\n"
        f"# Generated: {datetime.date.today().isoformat()} | "
        f"families_mapped={stats['families_mapped']} "
        f"(exact={stats['families_exact']}, poly={stats['families_narrow']}), "
        f"rows={stats['rows']}, families_without_ec2go_term={stats['families_no_ec2go']}\n"
    )
    doc = {
        "curie_map": {
            "CAZy": "http://www.cazy.org/",
            "GO": "http://purl.obolibrary.org/obo/GO_",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "semapv": "https://w3id.org/semapv/vocab/",
            "sssom": "https://w3id.org/sssom/",
        },
        "mapping_set_id": "https://w3id.org/ai4curation/ai-gene-review/mappings/cazy2go-generated",
        "mapping_set_title": "CAZy family -> GO molecular function (generated via UniProt CAZy+EC x ec2go)",
        "mapping_set_description": (
            "Auto-generated CAZy-family -> GO molecular-function mappings, derived by chaining reviewed "
            "UniProtKB CAZy<->EC cross-references with the GO ec2go mapping. exactMatch = mono-specific "
            "family; narrowMatch = poly-specific family (GO term applies to a subfamily). Companion to "
            "the hand-curated cazy2go.sssom.yaml seed."
        ),
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator_label": ["AI Gene Review project (build_cazy2go.py)"],
        "mappings": rows,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(header)
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", default="projects/GLYCOBIOLOGY/cazy2go.generated.sssom.yaml")
    args = ap.parse_args()
    print("Loading ec2go ...", file=sys.stderr)
    ec2go = load_ec2go()
    print(f"  ec2go: {len(ec2go)} EC numbers", file=sys.stderr)
    print("Loading CAZy<->EC from UniProt (reviewed) ...", file=sys.stderr)
    fam_ec, fam_members = load_cazy_ec()
    rows, stats = build_rows(fam_ec, fam_members, ec2go)
    write_sssom(rows, stats, args.output)
    print(f"Wrote {args.output}: {json.dumps(dict(stats))}", file=sys.stderr)


if __name__ == "__main__":
    main()
