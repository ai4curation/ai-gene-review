"""How is a Complex Portal complex's molecular function attributed to its subunits?

Complex Portal (CP) records molecular-function (MF) GO terms on the complex
itself. GOA copies CP's process and location terms to every subunit, but not
the MF. This script asks, for each CP complex that carries an MF term and has
at least one subunit reviewed in this repository, how the same activity is
attributed on the subunits:

* in GOA (from any group): ``enables``, ``contributes_to``, or no row for the
  term or a descendant;
* in the gene review's ``core_functions``: as ``molecular_function``, as
  ``contributes_to_molecular_function``, or not at all.

It summarises the patterns per complex-activity pair (one enabler, all
enablers, all contributors, nobody) and lists subunit-level disagreements
between GOA and the review. Nothing is hardcoded: inputs are CP's
``complextab`` species files, a GO ``go-basic.obo`` and the repository's
cached ``*-goa.tsv`` and ``*-ai-review.yaml`` files.

Usage::

    uv run python projects/COMPLEXPORTAL/scripts/cp_mf_attribution.py \
        COMPLEXTAB_DIR GO_BASIC_OBO OUT_YAML

COMPLEXTAB_DIR holds files downloaded from
https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/
(``<taxid>.tsv``; ``*_predicted.tsv`` files are skipped).
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader

REPO = Path(__file__).resolve().parents[3]
GO_RE = re.compile(r"(GO:\d{7})\(([^)]*)\)")
ACC_RE = re.compile(
    r"\b([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})\b"
)


def parse_obo(path: Path):
    namespace: dict[str, str] = {}
    parents: dict[str, set[str]] = defaultdict(set)
    alt: dict[str, str] = {}
    cur = None
    in_term = False
    with path.open() as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("["):
                in_term = line == "[Term]"
                cur = None
                continue
            if not in_term:
                continue
            if line.startswith("id: "):
                cur = line[4:]
            elif cur and line.startswith("namespace: "):
                namespace[cur] = line[11:]
            elif cur and line.startswith("alt_id: "):
                alt[line[8:]] = cur
            elif cur and line.startswith("is_a: "):
                parents[cur].add(line[6:].split()[0])
    return namespace, parents, alt


def ancestors(term: str, parents, cache: dict) -> set[str]:
    if term in cache:
        return cache[term]
    out: set[str] = set()
    stack = [term]
    while stack:
        t = stack.pop()
        for p in parents.get(t, ()):
            if p not in out:
                out.add(p)
                stack.append(p)
    cache[term] = out
    return out


def load_complexes(d: Path):
    complexes = []
    for f in sorted(d.glob("*.tsv")):
        if "predicted" in f.name:
            continue
        with f.open(newline="") as fh:
            rows = csv.reader(fh, delimiter="\t")
            header = next(rows)
            for r in rows:
                rec = dict(zip(header, r))
                participants_field = rec.get("Expanded participant list") or rec.get(
                    "Identifiers (and stoichiometry) of molecules in complex", ""
                )
                accs = []
                set_members = set()
                for tok in participants_field.split("|"):
                    found = ACC_RE.findall(tok)
                    if tok.startswith("[") and len(found) > 1:
                        set_members.update(found)
                    for a in found:
                        if a not in accs:
                            accs.append(a)
                complexes.append(
                    {
                        "ac": rec["#Complex ac"],
                        "name": rec["Recommended name"],
                        "taxon": rec["Taxonomy identifier"],
                        "evidence": rec["Evidence Code"].split("(")[0],
                        "subunits": accs,
                        "set_members": set_members,
                        "go": GO_RE.findall(rec.get("Go Annotations", "")),
                    }
                )
    return complexes


def index_reviews():
    idx = {}
    for p in REPO.glob("genes/*/*/*-ai-review.yaml"):
        with p.open() as fh:
            for line in fh:
                if line.startswith("id:"):
                    idx.setdefault(line.split(":", 1)[1].strip().strip("'\""), p)
                    break
    return idx


def term_matches(t: str, target: str, alt, parents, cache) -> bool:
    t = alt.get(t, t)
    return t == target or target in ancestors(t, parents, cache)


def main(complextab: str, obo: str, out: str) -> None:
    namespace, parents, alt = parse_obo(Path(obo))
    cache: dict = {}
    complexes = load_complexes(Path(complextab))
    reviews = index_reviews()

    pairs = []
    review_cache: dict[Path, tuple] = {}

    def gene_data(p: Path):
        if p not in review_cache:
            doc = yaml.load(p.read_text(), Loader=Loader) or {}
            goa = []
            gp = p.with_name(p.name.replace("-ai-review.yaml", "-goa.tsv"))
            if gp.exists():
                with gp.open(newline="") as fh:
                    for r in csv.DictReader(fh, delimiter="\t"):
                        if r.get("GO ASPECT") == "molecular_function":
                            goa.append(r)
            review_cache[p] = (doc, goa)
        return review_cache[p]

    n_cp_mf = 0
    for cx in complexes:
        mfs = [
            (g, n)
            for g, n in cx["go"]
            if namespace.get(alt.get(g, g)) == "molecular_function"
        ]
        if not mfs:
            continue
        n_cp_mf += 1
        reviewed = [a for a in cx["subunits"] if a in reviews]
        if not reviewed:
            continue
        for g, gname in mfs:
            subs = []
            for a in cx["subunits"]:
                p = reviews.get(a)
                if p is None:
                    subs.append({"accession": a, "reviewed": False})
                    continue
                doc, goa = gene_data(p)
                quals = Counter()
                for r in goa:
                    if term_matches(r["GO TERM"], g, alt, parents, cache):
                        quals[r["QUALIFIER"]] += 1
                actions = Counter()
                for ea in doc.get("existing_annotations") or []:
                    tid = (ea.get("term") or {}).get("id")
                    if tid and term_matches(tid, g, alt, parents, cache):
                        act = (ea.get("review") or {}).get("action", "NONE")
                        actions[act] += 1
                core = set()
                for cf in doc.get("core_functions") or []:
                    mf = (cf.get("molecular_function") or {}).get("id")
                    ct = (cf.get("contributes_to_molecular_function") or {}).get("id")
                    if mf and term_matches(mf, g, alt, parents, cache):
                        core.add("enables")
                    if ct and term_matches(ct, g, alt, parents, cache):
                        core.add("contributes_to")
                goa_call = (
                    "enables"
                    if any(q == "enables" for q in quals)
                    else "contributes_to"
                    if any(q == "contributes_to" for q in quals)
                    else "NOT_only"
                    if quals
                    else "none"
                )
                core_call = (
                    "enables"
                    if "enables" in core
                    else "contributes_to"
                    if "contributes_to" in core
                    else "none"
                )
                subs.append(
                    {
                        "accession": a,
                        "reviewed": True,
                        "gene": f"{p.parent.parent.name}/{p.parent.name}",
                        "goa": goa_call,
                        "goa_qualifiers": dict(quals),
                        "review_actions": dict(actions),
                        "core": core_call,
                        "paralog_set_member": a in cx["set_members"],
                    }
                )
            pairs.append(
                {
                    "complex": cx["ac"],
                    "complex_name": cx["name"],
                    "taxon": cx["taxon"],
                    "term": {"id": g, "label": gname},
                    "n_subunits": len(cx["subunits"]),
                    "subunits": subs,
                }
            )

    def pattern(subs, key):
        rv = [s for s in subs if s["reviewed"]]
        calls = Counter(s[key] for s in rv)
        n = len(rv)
        e, c = calls.get("enables", 0), calls.get("contributes_to", 0)
        if n == 0:
            return "no_reviewed"
        if e == 0 and c == 0:
            return "nobody"
        if e == n:
            return "all_enables"
        if c == n:
            return "all_contributes_to"
        if e and c:
            return "mixed_enables_and_contributes_to"
        if e == 1:
            return "single_enabler_rest_unannotated"
        if e:
            return "several_enablers_rest_unannotated"
        return "some_contributes_to_rest_unannotated"

    def summarise(subset):
        return {
            "pairs": len(subset),
            "goa_pattern": dict(Counter(pattern(p["subunits"], "goa") for p in subset).most_common()),
            "review_core_pattern": dict(
                Counter(pattern(p["subunits"], "core") for p in subset).most_common()
            ),
        }

    hetero = [p for p in pairs if p["n_subunits"] > 1]
    homo = [p for p in pairs if p["n_subunits"] == 1]
    fully = [p for p in hetero if all(s["reviewed"] for s in p["subunits"])]

    subunit_cross = Counter()
    disagreements = []
    for p in hetero:
        for s in p["subunits"]:
            if not s["reviewed"]:
                continue
            subunit_cross[f"goa={s['goa']} | core={s['core']}"] += 1
            if {s["goa"], s["core"]} == {"enables", "contributes_to"} or (
                s["goa"] == "enables" and s["core"] == "none" and any(
                    a in ("REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY")
                    for a in s["review_actions"]
                )
            ):
                disagreements.append(
                    {
                        "complex": p["complex"],
                        "complex_name": p["complex_name"],
                        "term": p["term"],
                        "gene": s["gene"],
                        "goa": s["goa"],
                        "goa_qualifiers": s["goa_qualifiers"],
                        "core": s["core"],
                        "review_actions": s["review_actions"],
                    }
                )

    result = {
        "generated": str(date.today()),
        "inputs": {
            "complextab_files": sorted(f.name for f in Path(complextab).glob("*.tsv") if "predicted" not in f.name),
            "go_obo": Path(obo).name,
        },
        "counts": {
            "cp_complexes_loaded": len(complexes),
            "cp_complexes_with_mf": n_cp_mf,
            "complex_mf_pairs_with_a_reviewed_subunit": len(pairs),
            "homomeric_pairs": len(homo),
            "heteromeric_pairs": len(hetero),
            "heteromeric_pairs_all_subunits_reviewed": len(fully),
        },
        "heteromeric_summary": summarise(hetero),
        "heteromeric_fully_reviewed_summary": summarise(fully),
        "homomeric_summary": summarise(homo),
        "subunit_goa_vs_review_core": dict(subunit_cross.most_common()),
        "disagreements": disagreements,
        "fully_reviewed_pairs": fully,
    }
    Path(out).write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print(yaml.safe_dump({k: result[k] for k in ("counts", "heteromeric_summary", "heteromeric_fully_reviewed_summary", "homomeric_summary", "subunit_goa_vs_review_core")}, sort_keys=False))
    print("disagreements:", len(disagreements))


if __name__ == "__main__":
    main(*sys.argv[1:4])
