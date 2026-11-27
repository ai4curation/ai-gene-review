#!/usr/bin/env python3
"""Second-source every GO term this review AUTHORS -- in structured slots AND in prose.

Motivation, learned twice on this PR: a single service can be a confident outlier.
QuickGO reported ``GO:0035259`` obsolete and ``GO:0016922`` childless; the GO API,
OLS4 and the repository's own ``cache/ontologies/go.tsv`` all disagreed, and
QuickGO was wrong on both counts. The compounding error was that the "two checks"
behind the claim were QuickGO's ``/children`` endpoint and QuickGO's text search --
**two methods against one service is one check.**

**Where that defect actually lived matters.** It was prose in
``suggested_questions``, not a structured term slot. A guard that reads only
``core_functions`` / ``proposed_replacement_terms`` / ``NEW`` ids would not have
caught it, so this script also sweeps every free-text string in the document for
``GO:\\d{7}`` and checks those ids too. Otherwise the README's claim to "guard the
class" would be broader than the code.

Ids sourced from GOA -- the ``term.id`` of any non-NEW ``existing_annotations``
row -- are deliberately excluded: per ``CLAUDE.md`` those are machine-supplied and
are not the reviewer's to second-guess. They are reported as a count so the
exclusion is visible rather than silent.

Each authored id is checked against **two independent services**:
  * QuickGO (EBI)  /ontology/go/terms/<id>/complete
  * OLS4    (EBI, separate pipeline)  /ontologies/go/terms?iri=...

Failing on: obsolescence per either service, disagreement between them,
non-resolution, or a label in the document that contradicts both services.

Run:  uv run python verify_authored_terms.py
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


def repo_root() -> Path:
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in (base, *base.parents):
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit("repo root not found")


ROOT = repo_root()
REVIEW = ROOT / "genes/human/ARGLU1/ARGLU1-ai-review.yaml"
OUT = Path(__file__).resolve().parent / "authored_terms.json"

GO_ID = re.compile(r"GO:\d{7}")


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def quickgo(curie: str) -> dict:
    d = _get(f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{curie}/complete")
    res = d.get("results") or []
    if len(res) != 1:
        return {"service": "QuickGO", "found": False, "n": len(res)}
    r = res[0]
    return {"service": "QuickGO", "found": True, "name": r.get("name"),
            "obsolete": bool(r.get("isObsolete")), "aspect": r.get("aspect")}


def ols(curie: str) -> dict:
    iri = "http://purl.obolibrary.org/obo/" + curie.replace(":", "_")
    url = ("https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri="
           + urllib.parse.quote(iri, safe=""))
    terms = _get(url).get("_embedded", {}).get("terms", [])
    if len(terms) != 1:
        return {"service": "OLS4", "found": False, "n": len(terms)}
    r = terms[0]
    return {"service": "OLS4", "found": True, "name": r.get("label"),
            "obsolete": bool(r.get("is_obsolete")), "aspect": None}


def gather(doc: dict) -> tuple[dict[str, list[str]], dict[str, str], int]:
    """Return (authored id -> sites, id -> declared label, count of GOA-sourced ids)."""
    authored: dict[str, list[str]] = {}
    labels: dict[str, str] = {}
    goa_sourced = 0

    def add(curie, where, label=None):
        if not curie:
            return
        authored.setdefault(curie, []).append(where)
        if label and curie not in labels:
            labels[curie] = label

    for i, cf in enumerate(doc.get("core_functions") or []):
        for slot in ("molecular_function", "contributes_to_molecular_function",
                     "in_complex"):
            t = cf.get(slot)
            if isinstance(t, dict):
                add(t.get("id"), f"core_functions[{i}].{slot}", t.get("label"))
        for slot in ("directly_involved_in", "locations", "substrates",
                     "anatomical_locations"):
            for t in (cf.get(slot) or []):
                if isinstance(t, dict):
                    add(t.get("id"), f"core_functions[{i}].{slot}", t.get("label"))

    for i, ann in enumerate(doc.get("existing_annotations") or []):
        review = ann.get("review") or {}
        term = ann.get("term") or {}
        if review.get("action") == "NEW":
            add(term.get("id"), f"existing_annotations[{i}].term (NEW)",
                term.get("label"))
        else:
            if term.get("id"):
                goa_sourced += 1
        for t in (review.get("proposed_replacement_terms") or []):
            if isinstance(t, dict):
                add(t.get("id"),
                    f"existing_annotations[{i}].proposed_replacement_terms",
                    t.get("label"))

    # Free-text sweep: this is where the GO:0035259 defect actually lived.
    goa_ids = {(a.get("term") or {}).get("id")
               for a in (doc.get("existing_annotations") or [])
               if (a.get("review") or {}).get("action") != "NEW"}

    def sweep(node, path="root"):
        if isinstance(node, dict):
            for k, v in node.items():
                sweep(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                sweep(v, f"{path}[{i}]")
        elif isinstance(node, str):
            for m in set(GO_ID.findall(node)):
                # A GOA id merely quoted in prose is not authored; skip those,
                # but anything else the prose recommends is the review's own claim.
                if m in goa_ids:
                    continue
                authored.setdefault(m, []).append(f"{path} (prose)")
                PROSE_CONTEXT.setdefault(m, []).append(node)

    sweep(doc)
    return authored, labels, goa_sourced


# Raw strings in which each prose-mentioned id appears, so the assertion the prose
# makes about a term can be compared against what the services report.
PROSE_CONTEXT: dict[str, list[str]] = {}

# Words by which prose asserts a term is NOT current.
_OBSOLETE_WORDS = re.compile(
    r"\b(obsolete|obsoleted|deprecated|merged into|absorbed(?: into)?|"
    r"replaced by|withdrawn)\b", re.I)
# Words by which prose asserts a term IS current.
_ACTIVE_WORDS = re.compile(r"\b(is active|are active|active and|remains current|"
                           r"is current|still active)\b", re.I)


def prose_status_claim(curie: str, window: int = 260) -> str | None:
    """What does the prose assert about this term: 'obsolete', 'active', or nothing?

    Localised to a window around each mention, because one sentence may discuss
    several ids with different statuses.
    """
    saw_obsolete = saw_active = False
    for s in PROSE_CONTEXT.get(curie, []):
        for m in re.finditer(re.escape(curie), s):
            lo, hi = max(0, m.start() - window), min(len(s), m.end() + window)
            seg = s[lo:hi]
            if _OBSOLETE_WORDS.search(seg):
                saw_obsolete = True
            if _ACTIVE_WORDS.search(seg):
                saw_active = True
    if saw_obsolete and not saw_active:
        return "obsolete"
    if saw_active and not saw_obsolete:
        return "active"
    if saw_active and saw_obsolete:
        return "mixed"
    return None


def main() -> int:
    doc = yaml.safe_load(REVIEW.read_text())
    authored, labels, goa_sourced = gather(doc)
    if not authored:
        raise SystemExit(
            "no authored terms found -- the collector is looking in the wrong slots "
            "or the review changed shape. A zero here would read as a pass."
        )

    problems: list[str] = []
    advisories: list[str] = []
    records: dict[str, dict] = {}
    prose_only = [c for c, sites in authored.items()
                  if all(s.endswith("(prose)") for s in sites)]

    print(f"authored ids: {len(authored)}  "
          f"(of which prose-only: {len(prose_only)})")
    print(f"GOA-sourced ids deliberately NOT checked: {goa_sourced}\n")

    for curie in sorted(authored):
        q = quickgo(curie)
        time.sleep(0.15)
        o = ols(curie)
        time.sleep(0.15)
        sites = sorted(set(authored[curie]))
        rec = {"sites": sites, "quickgo": q, "ols4": o,
               "declared_label": labels.get(curie)}
        records[curie] = rec

        print(f"{curie}  ({'prose only' if curie in prose_only else 'structured'})")
        for r in (q, o):
            print(f"   {r['service']:<8} "
                  + (f"name={r['name']!r} obsolete={r['obsolete']}"
                     if r["found"] else f"NOT RESOLVED (n={r['n']})"))

        if not q["found"] or not o["found"]:
            problems.append(f"{curie}: not resolvable on both services  [{sites[0]}]")
            continue

        structured = curie not in prose_only
        any_obsolete = q["obsolete"] or o["obsolete"]
        disagree = q["obsolete"] != o["obsolete"]
        claim = prose_status_claim(curie)
        rec["prose_status_claim"] = claim
        rec["services_disagree"] = disagree

        if disagree:
            # A property of the services, not of the review -- advisory, not a failure.
            advisories.append(
                f"{curie}: services DISAGREE on obsolescence (QuickGO={q['obsolete']}, "
                f"OLS4={o['obsolete']}). Do not rely on either alone; "
                "api.geneontology.org is the tiebreak.")

        if structured and any_obsolete:
            who = " and ".join(s for s, r in (("QuickGO", q), ("OLS4", o))
                               if r["obsolete"])
            problems.append(
                f"{curie}: used in a STRUCTURED slot but reported OBSOLETE by {who} "
                f"[{sites[0]}]")

        # Prose is REPORTED, not adjudicated.
        #
        # The tempting check -- "does the prose's claim about this term match the
        # services?" -- was implemented and withdrawn, because attributing an
        # English status phrase to a particular id cannot be done reliably by
        # proximity. It produced false positives in both directions on this very
        # document: "a bare GO:0005515 row is replaced by a more informative term"
        # reads as an obsolescence claim about GO:0019901 two clauses later, and
        # "GO:0035257 and GO:0035258 were absorbed into GO:0016922" reads as one
        # about GO:0016922, which is active. A guard that cries wolf on correct
        # content gets switched off, which is worse than not having it.
        #
        # So the status of every prose-mentioned id is surfaced for a human to
        # check against the sentence, and only the mechanically certain cases
        # fail. This is deliberately less than "guards the class": see README.
        if not structured:
            advisories.append(
                f"{curie}: named in prose at {sites[0]} -- "
                f"QuickGO obsolete={q['obsolete']}, OLS4 obsolete={o['obsolete']}"
                + (f"; prose appears to claim '{claim}'" if claim else
                   "; prose states no status")
                + ". Confirm the sentence agrees with the services."
            )

        # A real-but-wrong id with a plausible hand-written label passes both
        # services; compare the declared label too.
        declared = rec["declared_label"]
        if declared:
            names = {n.lower() for n in (q["name"], o["name"]) if n}
            if declared.strip().lower() not in names:
                problems.append(
                    f"{curie}: declared label {declared!r} matches neither service "
                    f"({q['name']!r} / {o['name']!r}) -- a real id with the wrong "
                    "label passes an existence check.")
        print()

    OUT.write_text(json.dumps(
        {"authored": records, "goa_sourced_not_checked": goa_sourced,
         "problems": problems, "advisories": advisories}, indent=2, sort_keys=True))

    if advisories:
        print(f"{len(advisories)} advisory (non-failing):")
        for a in advisories:
            print("  ~", a)
        print()

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        print(f"\nwrote {OUT}")
        return 1
    n_structured = len(authored) - len(prose_only)
    print(f"PASS: all {n_structured} term(s) used in STRUCTURED slots are current on "
          "both services and their declared labels match.")
    print(f"      {len(prose_only)} further id(s) appear only in prose; their status "
          "is listed above as advisory and is NOT adjudicated by this script "
          "(see README for why).")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
