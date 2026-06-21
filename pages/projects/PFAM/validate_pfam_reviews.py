#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Validate the hand-curated, entry-centric Pfam reviews under interpro/pfam/<PFAM>/.

The review files (``<PFAM>-review.yaml``, class PfamEntryReview) are hand-curated:
the supporting_examples / counter_examples are reviewer-picked and verified against
UniProt, so this script does NOT regenerate them. It checks the structural claims
that LinkML + linkml-term-validator cannot, then refreshes the human-readable index.

Checks per review (cache-dependent ones degrade to warnings if ./data is absent):
  1. pfam_id matches the directory/file, and the subject member_pfam (is_subject) == pfam_id;
  2. pfam_id is actually a member of interpro.id (InterPro member_list);
  3. the member_pfams listed match the InterPro entry's real Pfam membership;
  4. each proposed GO id exists in go-basic, is not obsolete, and its aspect matches;
  5. for PROPOSED annotations with mapping_viability NOT_VIABLE, the parent InterPro
     entry carries no equivalent interpro2go term (id/ancestor/descendant);
  6. every gene_review path on an example/counter-example exists on disk;
  7. REJECTED annotations have >=1 counter_example in the SAME family (pfam_id),
     i.e. the heterogeneity claim is actually backed.

Then regenerates projects/PFAM/PROPOSED_MAPPINGS.md from the reviews.

Inputs (cached under ./data, git-ignored; from analyze_pfam_go_gaps.py --download +
the Pfam FTP): interpro.xml.gz, interpro2go.txt, go-basic.obo, Pfam-A.clans.tsv.gz.

Run via:  just validate-pfam-reviews   (also runs linkml-validate + linkml-term-validator)
"""
from __future__ import annotations

import collections
import gzip
import sys
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

import yaml

HERE = Path(__file__).parent
DATA = HERE / "data"
REPO = HERE.parent.parent
PFAM_DIR = REPO / "interpro" / "pfam"

ASPECT_NS = {
    "molecular_function": "molecular_function",
    "biological_process": "biological_process",
    "cellular_component": "cellular_component",
}


def parse_interpro(path: Path):
    ipr_pfam = collections.defaultdict(set)
    pf2ipr = {}
    cur, in_ml = None, False
    with gzip.open(path, "rb") as fh:
        for ev, el in ET.iterparse(fh, events=("start", "end")):
            if el.tag == "interpro":
                if ev == "start":
                    cur = el.get("id")
                else:
                    el.clear(); cur = None
            elif el.tag == "member_list":
                in_ml = ev == "start"
            elif el.tag == "db_xref" and ev == "start" and in_ml and cur and el.get("db") == "PFAM":
                ipr_pfam[cur].add(el.get("dbkey"))
                pf2ipr[el.get("dbkey")] = cur
    return pf2ipr, ipr_pfam


def parse_interpro2go(path: Path):
    ipr2go = collections.defaultdict(set)
    for line in path.read_text().splitlines():
        if line.startswith("InterPro:"):
            p = line.split(" ; ")
            if len(p) == 2:
                ipr2go[line.split()[0].split(":")[1]].add(p[1].strip())
    return ipr2go


def parse_go(path: Path):
    name, ns, obs = {}, {}, set()
    parents, alt = collections.defaultdict(set), {}
    cur, it = None, False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            it, cur = True, None; continue
        if line.startswith("["):
            it = False; continue
        if not it:
            continue
        if line.startswith("id: "):
            cur = line[4:].strip()
        elif line.startswith("name: ") and cur:
            name[cur] = line[6:].strip()
        elif line.startswith("namespace: ") and cur:
            ns[cur] = line[11:].strip()
        elif line.startswith("alt_id: ") and cur:
            alt[line[8:].strip()] = cur
        elif line.startswith("is_obsolete: true") and cur:
            obs.add(cur)
        elif line.startswith("is_a: ") and cur:
            parents[cur].add(line[6:].split("!")[0].strip())
        elif line.startswith("relationship: part_of ") and cur:
            parents[cur].add(line.split("part_of", 1)[1].split("!")[0].strip())
    return name, ns, obs, parents, alt


def main() -> int:
    reviews = {}
    for f in sorted(PFAM_DIR.glob("PF*/PF*-review.yaml")):
        reviews[f] = yaml.safe_load(f.read_text())
    if not reviews:
        print("ERROR: no interpro/pfam/*/*-review.yaml files found", file=sys.stderr)
        return 1

    cache_ok = all((DATA / n).exists() for n in
                   ["interpro.xml.gz", "interpro2go.txt", "go-basic.obo"])
    if cache_ok:
        pf2ipr, ipr_pfam = parse_interpro(DATA / "interpro.xml.gz")
        ipr2go = parse_interpro2go(DATA / "interpro2go.txt")
        go_name, go_ns, go_obs, go_parents, go_alt = parse_go(DATA / "go-basic.obo")

        def norm(g):
            return go_alt.get(g, g)

        @lru_cache(maxsize=None)
        def ancestors(g):
            g = norm(g); seen, stack = set(), list(go_parents.get(g, ()))
            while stack:
                p = stack.pop()
                if p in seen:
                    continue
                seen.add(p); stack.extend(go_parents.get(p, ()))
            return seen
    else:
        print("WARNING: ./data cache absent; skipping membership/GO/premise checks "
              "(run analyze_pfam_go_gaps.py --download to enable).", file=sys.stderr)

    errors = []
    for f, r in reviews.items():
        pf = r.get("pfam_id", "")
        tag = f.parent.name
        if pf != tag or f.name != f"{pf}-review.yaml":
            errors.append(f"{tag}: pfam_id/path mismatch (pfam_id={pf})")
        ic = r.get("interpro", {})
        ipr = str(ic.get("id", "")).replace("InterPro:", "")
        members = ic.get("member_pfams", []) or []
        subj = [m for m in members if m.get("is_subject")]
        if not (len(subj) == 1 and subj[0].get("id") == f"Pfam:{pf}"):
            errors.append(f"{pf}: exactly one member_pfam must have is_subject:true and equal Pfam:{pf}")

        if cache_ok:
            if pf2ipr.get(pf) != ipr:
                errors.append(f"{pf}: member parent is {pf2ipr.get(pf)}, not {ipr}")
            real = {f"Pfam:{m}" for m in ipr_pfam.get(ipr, set())}
            listed = {m.get("id") for m in members}
            if real and listed != real:
                errors.append(f"{pf}: member_pfams {sorted(listed)} != InterPro {ipr} members {sorted(real)}")
            entry_go = {norm(g) for g in ipr2go.get(ipr, set())}
            for a in r.get("proposed_annotations", []) or []:
                gid = norm(str(a.get("term", {}).get("id", "")))
                if gid not in go_name:
                    errors.append(f"{pf}: GO {gid} not in go-basic"); continue
                if gid in go_obs:
                    errors.append(f"{pf}: GO {gid} obsolete")
                if go_ns.get(gid) != ASPECT_NS.get(a.get("aspect")):
                    errors.append(f"{pf}: GO {gid} aspect {go_ns.get(gid)} != declared {a.get('aspect')}")
                if a.get("status") == "PROPOSED" and ic.get("mapping_viability") == "NOT_VIABLE":
                    if gid in entry_go or ancestors(gid) & entry_go or any(gid in ancestors(eg) for eg in entry_go):
                        errors.append(f"{pf}: parent {ipr} already maps {gid} or a relative (premise false)")

        for a in r.get("proposed_annotations", []) or []:
            ex = (a.get("supporting_examples") or []) + (a.get("counter_examples") or [])
            for e in ex:
                gr = e.get("gene_review")
                if gr and not (REPO / gr).exists():
                    errors.append(f"{pf}: gene_review path does not exist: {gr}")
            if a.get("status") == "REJECTED":
                same = [c for c in (a.get("counter_examples") or [])
                        if c.get("member_pfam") == f"Pfam:{pf}"]
                if not same:
                    errors.append(f"{pf}: REJECTED annotation needs >=1 counter_example in the same family (Pfam:{pf})")

    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 2

    write_index(reviews)
    print(f"OK: {len(reviews)} Pfam entry reviews validated"
          f"{' (full checks)' if cache_ok else ' (structural checks only; cache absent)'}.")
    return 0


def write_index(reviews: dict) -> None:
    asp = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
    items = sorted(reviews.items(), key=lambda kv: kv[1].get("pfam_id", ""))
    prop = [(f, r) for f, r in items
            if any(a.get("status") == "PROPOSED" for a in r.get("proposed_annotations", []) or [])]
    rej = [(f, r) for f, r in items
           if all(a.get("status") == "REJECTED" for a in r.get("proposed_annotations", []) or [])
           and (r.get("proposed_annotations") or [])]
    out = ["---", 'title: "Pfam entry reviews (proposed GO + verified rejections)"', "---", "",
           "# Pfam entry reviews — proposed GO where InterPro can't, with member verification", "",
           "> Index of the curated **per-Pfam entry reviews** under "
           "`interpro/pfam/<PFAM>/<PFAM>-review.yaml` (schema: "
           "`src/ai_gene_review/schema/pfam_entry_review.yaml`). Each proposal is grounded in "
           "**characterized SwissProt members** and tested against **counter-examples**; a family "
           "whose own members are functionally heterogeneous is recorded as **REJECTED**. "
           "Validate with `just validate-pfam-reviews`. See [parent project](../PFAM.md).", ""]

    def row(pf, r, a):
        ex = (a.get("supporting_examples") or [{}])[0].get("accession", "")
        return (f"| {pf} | {r.get('pfam_name','')} | "
                f"[`{pf}-review.yaml`](../../interpro/pfam/{pf}/{pf}-review.yaml) | "
                f"{a['relation']['label']} | {a['term']['id']} {a['term']['label']} | "
                f"{asp.get(a['aspect'], a['aspect'])} | {a.get('confidence','')} | {ex} |")

    out += [f"## Proposed ({len(prop)} families)", "",
            "| Pfam | family | review | relation | proposed GO | aspect | conf. | example |",
            "|---|---|---|---|---|---|---|---|"]
    for f, r in prop:
        for a in r.get("proposed_annotations", []) or []:
            if a.get("status") == "PROPOSED":
                out.append(row(r["pfam_id"], r, a))

    out += ["", f"## Rejected on member verification ({len(rej)} families)", "",
            "These families are named for a function but their reviewed members are "
            "functionally heterogeneous (counter-examples in the *same* family), so the "
            "term would over-annotate even at the Pfam level.", "",
            "| Pfam | family | review | term that does NOT hold | why (same-family counter-example) |",
            "|---|---|---|---|---|"]
    for f, r in rej:
        for a in r.get("proposed_annotations", []) or []:
            cex = next((c for c in (a.get("counter_examples") or [])
                        if c.get("member_pfam") == f"Pfam:{r['pfam_id']}"), {})
            out.append(f"| {r['pfam_id']} | {r.get('pfam_name','')} | "
                       f"[`{r['pfam_id']}-review.yaml`](../../interpro/pfam/{r['pfam_id']}/{r['pfam_id']}-review.yaml) | "
                       f"{a['term']['id']} {a['term']['label']} | "
                       f"{cex.get('protein_name','')} ({cex.get('ec','no EC')}) |")
    out.append("")
    (HERE / "PROPOSED_MAPPINGS.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
