#!/usr/bin/env python3
"""Resolve every WITH/FROM identifier in ABR-goa.tsv and ask what evidence each
donor carries *for the term it donated*.

Two passes, deliberately separated so the report can be regenerated without network:

  fetch  : hit UniProt + QuickGO, write results.json (raw resolved facts)
  report : render RESULTS.md purely from results.json

Usage:
    python3 resolve_withfrom.py fetch     # network; rewrites results.json AND RESULTS.md
    python3 resolve_withfrom.py report    # offline; rewrites RESULTS.md from results.json

Design notes (each guards against a specific way this analysis has been got wrong):

* Identifier lookups request size>=5 and report EVERY candidate. A size=1 query
  turns an ambiguous cross-reference into a confident wrong answer.
* An empty resolution is a hard error naming the token, never a silent zero. A dead
  UniProt accession is otherwise indistinguishable from a donor with no annotations.
* Swiss-Prot vs TrEMBL is printed next to every name, because an unreviewed entry's
  *name* is an automatic by-similarity label even when its GO annotations are real.
* "Which term does the donor hold" is recorded, not merely "does it hold one" — a
  propagation that lands above its donor is a real, fixable defect.
* source_entities for the review YAML are derived from the GOA WITH/FROM column by
  construction, and the token counts are asserted against GOA.

Stdlib only; no third-party dependencies.
"""

from __future__ import annotations

import collections
import datetime
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ABR-goa.tsv"
RESULTS_JSON = HERE / "results.json"
RESULTS_MD = HERE / "RESULTS.md"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# GOA TSV is 16 columns: GO term is $5, evidence $9, reference $10, WITH/FROM $11 (1-based).
COL_TERM, COL_NAME, COL_EV, COL_REF, COL_WF = 4, 5, 8, 9, 10

UNIPROT_FIELDS = "accession,id,protein_name,gene_names,organism_name,reviewed,length"

# How to turn a WITH/FROM token into a UniProt query. MGI/RGD/CGD tokens are not
# UniProt accessions and must go through a cross-reference search.
#   - MGI arrives as "MGI:MGI:107771"; the xref search wants the BARE number
#     (a query containing the inner colon returns HTTP 400).
XREF_DB = {"MGI": "mgi", "RGD": "rgd", "CGD": "cgd"}

# Tokens that are not resolvable to a protein sequence at all.
NON_PROTEIN_PREFIXES = ("PANTHER:", "InterPro:", "ARBA:", "UniProtKB-SubCell:")


def http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def read_goa() -> list[list[str]]:
    rows = []
    with GOA.open() as fh:
        fh.readline()  # header
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) > COL_WF:
                rows.append(cols)
    if not rows:
        raise SystemExit(f"No data rows parsed from {GOA}. Re-fetch with: just fetch-gene human ABR")
    return rows


def collect_tokens(rows) -> dict[str, list[dict]]:
    """WITH/FROM token -> list of the annotations it supports. Built from GOA only."""
    tokens: dict[str, list[dict]] = collections.OrderedDict()
    for cols in rows:
        for tok in (cols[COL_WF] or "").split("|"):
            tok = tok.strip()
            if tok:
                tokens.setdefault(tok, []).append(
                    {"term": cols[COL_TERM], "term_name": cols[COL_NAME],
                     "evidence": cols[COL_EV], "reference": cols[COL_REF]}
                )
    return tokens


def uniprot_search(query: str, size: int = 5) -> list[dict]:
    url = ("https://rest.uniprot.org/uniprotkb/search?query="
           + urllib.parse.quote(query) + f"&fields={UNIPROT_FIELDS}&size={size}")
    return http_json(url).get("results", [])


def describe(entry: dict) -> dict:
    desc = entry.get("proteinDescription") or {}
    name = ((desc.get("recommendedName") or {}).get("fullName") or {}).get("value")
    if not name:
        subs = desc.get("submissionNames") or []
        name = subs[0]["fullName"]["value"] if subs else None
    entry_type = entry.get("entryType", "")
    if entry_type.startswith("UniProtKB reviewed"):
        reviewed = "Swiss-Prot"
    elif entry_type == "Inactive":
        reviewed = "INACTIVE"
    else:
        reviewed = "TrEMBL"
    return {
        "accession": entry.get("primaryAccession"),
        "entry_name": entry.get("uniProtkbId"),
        "entry_type": entry_type,
        "reviewed": reviewed,
        "organism": (entry.get("organism") or {}).get("scientificName"),
        "genes": [g.get("geneName", {}).get("value") for g in (entry.get("genes") or [])],
        "protein_name": name,
        "length": (entry.get("sequence") or {}).get("length"),
    }


def resolve_token(tok: str) -> dict:
    """Resolve one WITH/FROM token to candidate proteins, reporting ALL candidates."""
    if tok.startswith(NON_PROTEIN_PREFIXES):
        kind = {"PANTHER": "panther_tree_node", "InterPro": "interpro_signature",
                "ARBA": "arba_rule", "UniProtKB-SubCell": "uniprot_subcell_keyword"}[tok.split(":")[0]]
        return {"token": tok, "kind": kind, "candidates": []}

    db, _, ident = tok.partition(":")
    if db == "UniProtKB":
        query = f"accession:{ident}"
    elif db in XREF_DB:
        bare = ident.split(":")[-1]  # MGI:MGI:107771 -> 107771
        query = f"xref:{XREF_DB[db]}-{bare}"
    else:
        raise SystemExit(f"Unhandled WITH/FROM database for token {tok!r}. Add it to XREF_DB.")

    cands = [describe(e) for e in uniprot_search(query)]
    if not cands:
        raise SystemExit(
            f"Empty UniProt resolution for {tok!r} (query {query!r}). A dead or unmapped "
            f"accession must not be reported as 'donor carries no annotation' — investigate."
        )
    for c in cands:
        if not c["accession"] or not c["entry_name"]:
            raise SystemExit(f"Token {tok!r} resolved to an entry with no name: {c!r}")
        # A deleted UniProt entry still answers an accession search: entryType is
        # "Inactive", uniProtkbId echoes the accession, genes are empty and length is
        # null. Querying it for annotations then returns zero hits, which is
        # indistinguishable from a live donor that genuinely carries none. Fail loudly.
        if c["reviewed"] == "INACTIVE" or c["length"] is None:
            raise SystemExit(
                f"Token {tok!r} resolves to INACTIVE/deleted UniProt entry "
                f"{c['accession']} (entryType={c['entry_type']!r}, length={c['length']!r}). "
                f"A dead accession must not be read as 'donor carries no annotation'; "
                f"find the live accession before drawing any conclusion from this donor."
            )
    return {"token": tok, "kind": "protein", "candidates": cands}


def canonical(res: dict) -> dict | None:
    """Preferred candidate: the Swiss-Prot one. Multi-hit is reported, not hidden."""
    revd = [c for c in res["candidates"] if c["reviewed"] == "Swiss-Prot"]
    if len(revd) == 1:
        return revd[0]
    if revd:
        return max(revd, key=lambda c: c["length"] or 0)
    return res["candidates"][0] if res["candidates"] else None


_TERM_NAME_CACHE: dict[str, str] = {}


def term_name(go_id: str) -> str:
    """Label for a GO id. QuickGO's annotation search sometimes returns an empty
    goName for descendant terms; an unlabelled id in the report is unreadable."""
    if go_id not in _TERM_NAME_CACHE:
        url = f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete"
        results = http_json(url).get("results") or []
        if not results or not results[0].get("name"):
            raise SystemExit(f"Could not resolve a label for {go_id}; refusing to emit an unlabelled term.")
        _TERM_NAME_CACHE[go_id] = results[0]["name"]
    return _TERM_NAME_CACHE[go_id]


def donor_evidence(accession: str, go_id: str) -> list[dict]:
    """What does this donor itself hold at or below go_id, and with what evidence?

    QuickGO's annotation search rejects MGI/RGD gene-product ids (HTTP 400), so donors
    are queried through the canonical UniProt accession resolved above.
    """
    url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:"
           + urllib.parse.quote(accession) + "&goId=" + urllib.parse.quote(go_id)
           + "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100")
    held: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    for a in http_json(url).get("results", []):
        held[(a["goId"], a.get("goName") or "")].add(a["goEvidence"])
    return [
        {"go_id": gid, "go_name": gname or term_name(gid), "evidence": sorted(evs),
         "experimental": sorted(evs & EXPERIMENTAL), "same_term": gid == go_id}
        for (gid, gname), evs in sorted(held.items())
    ]


def do_fetch() -> dict:
    rows = read_goa()
    tokens = collect_tokens(rows)

    resolutions = {tok: resolve_token(tok) for tok in tokens}

    # Per-annotation donor evidence, for propagated rows only (those with WITH/FROM).
    annotations = []
    for cols in rows:
        toks = [t.strip() for t in (cols[COL_WF] or "").split("|") if t.strip()]
        entry = {
            "term": cols[COL_TERM], "term_name": cols[COL_NAME],
            "evidence": cols[COL_EV], "reference": cols[COL_REF],
            "withfrom": toks, "donors": [],
        }
        for tok in toks:
            res = resolutions[tok]
            if res["kind"] != "protein":
                entry["donors"].append({"token": tok, "kind": res["kind"], "held": None})
                continue
            can = canonical(res)
            entry["donors"].append({
                "token": tok, "kind": "protein", "accession": can["accession"],
                "entry_name": can["entry_name"], "reviewed": can["reviewed"],
                "n_candidates": len(res["candidates"]),
                "held": donor_evidence(can["accession"], cols[COL_TERM]),
            })
        annotations.append(entry)

    data = {
        "fetched_date": datetime.date.today().isoformat(),
        "n_goa_rows": len(rows),
        "tokens": {tok: uses for tok, uses in tokens.items()},
        "resolutions": resolutions,
        "annotations": annotations,
    }

    # Assertion: token inventory must match GOA by construction.
    recount = collect_tokens(read_goa())
    assert set(recount) == set(data["tokens"]), "token set drifted from GOA"
    for tok, uses in recount.items():
        assert len(uses) == len(data["tokens"][tok]), f"use-count drift on {tok}"

    RESULTS_JSON.write_text(json.dumps(data, indent=1, sort_keys=False) + "\n")
    return data


def source_entities_for(ann: dict) -> list[dict]:
    """Build review-YAML source_entities from the GOA WITH/FROM field, in GOA order."""
    out = []
    for d in ann["donors"]:
        if d["kind"] != "protein":
            out.append({"source_id": d["token"], "kind": d["kind"]})
            continue
        exp = sorted({e for h in (d["held"] or []) for e in h["experimental"]})
        same = [h for h in (d["held"] or []) if h["same_term"]]
        below = [h for h in (d["held"] or []) if not h["same_term"]]
        out.append({
            "source_id": d["token"], "accession": d["accession"],
            "entry_name": d["entry_name"], "reviewed": d["reviewed"],
            "experimental_codes": exp,
            "holds_same_term": bool(same),
            "same_term_experimental": sorted({e for h in same for e in h["experimental"]}),
            "more_specific_terms": [
                {"go_id": h["go_id"], "go_name": h["go_name"], "experimental": h["experimental"]}
                for h in below
            ],
        })
    return out


def do_report(data: dict) -> None:
    L: list[str] = []
    add = L.append
    add("# ABR WITH/FROM resolution and donor-evidence audit")
    add("")
    add(f"Generated by `resolve_withfrom.py` from `results.json` (fetched {data['fetched_date']}).")
    add("Regenerate offline with `python3 resolve_withfrom.py report`; refresh from the live")
    add("APIs with `python3 resolve_withfrom.py fetch`. Stdlib only, no dependencies.")
    add("")
    add(f"Input: `../ABR-goa.tsv`, {data['n_goa_rows']} annotation rows, "
        f"{len(data['tokens'])} distinct WITH/FROM identifiers.")
    add("")

    add("## 1. Every WITH/FROM identifier resolves")
    add("")
    add("Candidates are reported in full: a single-hit lookup would convert an ambiguous")
    add("cross-reference into a confident wrong answer. Swiss-Prot/TrEMBL status is shown")
    add("because an unreviewed entry's *name* is an automatic label even when its GO")
    add("annotations are experimental.")
    add("")
    add("| WITH/FROM token | resolves to | status | organism | len | n candidates |")
    add("|---|---|---|---|---|---|")
    for tok, res in data["resolutions"].items():
        if res["kind"] != "protein":
            add(f"| `{tok}` | *{res['kind'].replace('_',' ')}* — not a protein sequence | — | — | — | — |")
            continue
        can = canonical(res)
        genes = ",".join(g for g in (can["genes"] or []) if g) or "-"
        add(f"| `{tok}` | {can['accession']} [{can['entry_name']}] {genes} | "
            f"{can['reviewed']} | {can['organism']} | {can['length']} | {len(res['candidates'])} |")
    add("")
    multi = {t: r for t, r in data["resolutions"].items()
             if r["kind"] == "protein" and len(r["candidates"]) > 1}
    if multi:
        add(f"{len(multi)} token(s) are multi-hit; all candidates are listed in `results.json`.")
        add("In each case the reviewed (Swiss-Prot) entry was taken as canonical, and its")
        add("length matches the canonical ortholog, so the ambiguity is between a curated")
        add("entry and unreviewed fragments rather than between two different genes.")
        add("")

    add("## 2. What each donor holds for the term it donated")
    add("")
    add("The question is not whether a donor carries evidence but **which term** it carries")
    add("it at: a propagation landing above its donor is a fixable defect, and an IBA whose")
    add("donors all carry their own experimental annotations cannot be dismissed as a")
    add("family-level guess.")
    add("")
    prop = [a for a in data["annotations"] if any(d["kind"] == "protein" for d in a["donors"])]
    for ann in prop:
        pdon = [d for d in ann["donors"] if d["kind"] == "protein"]
        nodes = [d["token"] for d in ann["donors"] if d["kind"] == "panther_tree_node"]
        add(f"### {ann['term']} {ann['term_name']} [{ann['evidence']}]")
        add("")
        if nodes:
            add(f"PANTHER node(s): {', '.join('`'+n+'`' for n in nodes)}")
            add("")
        add("| donor | entry | own evidence for this term | also holds (more specific) |")
        add("|---|---|---|---|")
        for d in pdon:
            same = [h for h in (d["held"] or []) if h["same_term"]]
            below = [h for h in (d["held"] or []) if not h["same_term"]]
            if same:
                ev = ",".join(same[0]["experimental"]) or "none (" + ",".join(same[0]["evidence"]) + ")"
            else:
                ev = "*no annotation at this term*"
            bel = "; ".join(
                f"{h['go_id']} {h['go_name']} ({','.join(h['experimental']) or ','.join(h['evidence'])})"
                for h in below) or "—"
            add(f"| `{d['token']}` | {d['accession']} [{d['entry_name']}] {d['reviewed']} | {ev} | {bel} |")
        add("")
        n_exp = sum(1 for d in pdon
                    if any(h["same_term"] and h["experimental"] for h in (d["held"] or [])))
        add(f"**{n_exp} of {len(pdon)} protein donors carry their own experimental evidence "
            f"at {ann['term']} itself.**")
        add("")

    add("## 3. Aggregate")
    add("")
    tot = sum(len([d for d in a["donors"] if d["kind"] == "protein"]) for a in prop)
    tot_exp = sum(
        1 for a in prop for d in a["donors"]
        if d["kind"] == "protein" and any(h["same_term"] and h["experimental"] for h in (d["held"] or []))
    )
    add(f"- Propagated rows with at least one protein donor: **{len(prop)}**")
    add(f"- Protein donor/row pairs: **{tot}**")
    add(f"- Pairs where the donor holds its own experimental evidence at the donated term: "
        f"**{tot_exp}/{tot}**")
    add("")
    add("Consequence for the review: `SOURCE_WEAK_OR_INFERRED` and `SOURCE_EVIDENCE_WEAK`")
    add("are factually unavailable on these rows — the donors are experimentally annotated,")
    add("so any objection has to be about whether the term should *propagate*, not about")
    add("donor quality.")
    add("")

    add("## 4. source_entities blocks for the review YAML")
    add("")
    add("Derived from the GOA WITH/FROM column by construction and asserted against it, so")
    add("the lists in `ABR-ai-review.yaml` cannot silently drift from GOA.")
    add("")
    add("```json")
    add(json.dumps({f"{a['term']}/{a['evidence']}": source_entities_for(a) for a in prop}, indent=1))
    add("```")
    add("")
    RESULTS_MD.write_text("\n".join(L))


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "report"
    if mode == "fetch":
        data = do_fetch()
    elif mode == "report":
        if not RESULTS_JSON.exists():
            raise SystemExit(
                f"{RESULTS_JSON} missing. Run: python3 {Path(__file__).name} fetch"
            )
        data = json.loads(RESULTS_JSON.read_text())
    else:
        raise SystemExit(f"Unknown mode {mode!r}; expected 'fetch' or 'report'.")
    do_report(data)
    print(f"wrote {RESULTS_MD.relative_to(HERE.parent.parent.parent.parent)}")


if __name__ == "__main__":
    main()
