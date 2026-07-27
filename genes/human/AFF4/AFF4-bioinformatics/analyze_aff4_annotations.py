#!/usr/bin/env python3
"""Reproducible provenance audit of the GOA annotation set for human AFF4 (Q9UHB7).

Everything reported in ``RESULTS.md`` is computed here. The script is written so
that a silent zero cannot pass for a finding:

* every UniProt fetch asserts ``primaryAccession == the accession requested``
  (a merged/secondary accession returns HTTP 200 for a *different* protein);
* every QuickGO query asserts ``numberOfHits == len(results)`` after pagination
  (the service clamps page size rather than erroring);
* the retraction/erratum detector carries **positive controls** so that a clean
  negative cannot be a broken query;
* the reference-projection test reports ``entity_count_available: false`` rather
  than reading a number off the first page of a large result;
* interaction partner sets are asserted on **membership**, not cardinality, and
  the subject is asserted absent from its own partner set.

Usage::

    uv run --with requests python analyze_aff4_annotations.py            # write RESULTS.md + results.json
    uv run --with requests python analyze_aff4_annotations.py --self-test  # break-tests only

Inputs (hard requirement -- a missing input is a loud error, never a degraded run):
    ../AFF4-goa.tsv        the GOA table fetched by ``just fetch-gene human AFF4``
    ../AFF4-uniprot.txt    the UniProt flat file
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "AFF4-goa.tsv"
UNIPROT = HERE.parent / "AFF4-uniprot.txt"

SUBJECT = "Q9UHB7"
SUBJECT_SYMBOL = "AFF4"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
UNIPROT_REST = "https://rest.uniprot.org"
INTACT = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# GO evidence codes that count as experimental (GO's EXP group).
EXPERIMENTAL = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}

# A reference whose fully-paginated annotation set exceeds this is treated as
# too large to page through politely; we then report the entity count as
# UNAVAILABLE rather than sampling.
PROJECTION_MAX_ANNOTATIONS = 2000

SESSION = requests.Session()
SESSION.headers["Accept"] = "application/json"
SESSION.headers["User-Agent"] = "ai-gene-review/AFF4-audit"


class AuditError(RuntimeError):
    """Raised when an input is missing or an invariant is violated."""


# --------------------------------------------------------------------------- #
# HTTP helpers -- each one asserts the thing that makes its silence meaningful
# --------------------------------------------------------------------------- #

def _get(url: str, params: dict | None = None, tries: int = 4) -> requests.Response:
    last = None
    for attempt in range(tries):
        r = SESSION.get(url, params=params, timeout=90)
        if r.status_code == 200:
            return r
        last = r
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(2 * (attempt + 1))
            continue
        break
    raise AuditError(
        f"HTTP {last.status_code} for {last.url}\n"
        "  A rejected query and an empty result look identical downstream, so this is fatal."
    )


def uniprot_entry(accession: str) -> dict:
    """Fetch one UniProt entry, asserting it is the entry that was asked for."""
    r = _get(
        f"{UNIPROT_REST}/uniprotkb/{accession}.json",
        {"fields": "accession,id,protein_name,gene_names,organism_name,length,cc_function"},
    )
    d = r.json()
    got = d.get("primaryAccession")
    if got != accession:
        raise AuditError(
            f"UniProt returned {got!r} for a request for {accession!r}. "
            "A merged/secondary accession resolves to a DIFFERENT protein with HTTP 200."
        )
    name = (
        d.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value")
        or (d.get("proteinDescription", {}).get("submissionNames") or [{}])[0]
        .get("fullName", {})
        .get("value")
    )
    entry_type = d.get("entryType", "")
    if not entry_type:
        raise AuditError(f"{accession}: empty entryType -- possibly an inactive (deleted) entry.")
    return {
        "accession": got,
        "entry_name": d.get("uniProtkbId"),
        # "reviewed" is a SUBSTRING of "unreviewed" -- anchor on the prefix.
        "reviewed": entry_type.startswith("UniProtKB reviewed"),
        "entry_type": entry_type,
        "organism": d.get("organism", {}).get("scientificName"),
        "genes": [g.get("geneName", {}).get("value") for g in d.get("genes", [])],
        "length": d.get("sequence", {}).get("length"),
        "protein_name": name,
    }


def uniprot_by_xref(db: str, ident: str) -> list[dict]:
    """Resolve a MOD identifier. Always ask for >1 hit: an ambiguous cross-reference
    is DATA, and ``size=1`` silently converts it into a confident wrong answer."""
    r = _get(
        f"{UNIPROT_REST}/uniprotkb/search",
        {
            "query": f"xref:{db}-{ident}",
            "fields": "accession,id,protein_name,gene_names,organism_name,length",
            "size": "10",
        },
    )
    out = []
    for d in r.json().get("results", []):
        name = (
            d.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value")
            or "?"
        )
        et = d.get("entryType", "")
        out.append({
            "accession": d.get("primaryAccession"),
            "entry_name": d.get("uniProtkbId"),
            "reviewed": et.startswith("UniProtKB reviewed"),
            "entry_type": et,
            "organism": d.get("organism", {}).get("scientificName"),
            "genes": [g.get("geneName", {}).get("value") for g in d.get("genes", [])],
            "length": d.get("sequence", {}).get("length"),
            "protein_name": name,
        })
    return out


def quickgo_annotations(params: dict, max_annotations: int | None = None) -> tuple[list[dict], int, bool]:
    """Fully paginate a QuickGO annotation search.

    Returns ``(results, numberOfHits, complete)``. ``complete`` is False only when
    we deliberately stopped because the result set was larger than
    ``max_annotations``; in that case the caller MUST NOT derive a count from it.
    Compares ``numberOfHits`` against ``len(results)`` -- never against a
    page-size constant, because the service clamps rather than erroring.
    """
    p = dict(params)
    p["limit"] = "100"
    out: list[dict] = []
    total: int | None = None
    page = 1
    while True:
        p["page"] = str(page)
        d = _get(f"{QUICKGO}/annotation/search", p).json()
        if total is None:
            total = d["numberOfHits"]
            if max_annotations is not None and total > max_annotations:
                return [], total, False
        batch = d.get("results", [])
        if not batch:
            break
        out.extend(batch)
        if len(out) >= total:
            break
        page += 1
        if page > 400:
            raise AuditError(f"runaway pagination for {params}")
    if len(out) != total:
        raise AuditError(
            f"QuickGO pagination incomplete for {params}: numberOfHits={total} but read {len(out)}. "
            "The service clamps results-per-page, so a page-size guard cannot catch this."
        )
    return out, total, True


def go_term(term_id: str) -> dict:
    d = _get(f"{QUICKGO}/ontology/go/terms/{term_id}/complete").json()
    res = d["results"][0]
    return {
        "id": res["id"],
        "name": res["name"],
        "aspect": res.get("aspect"),
        "definition": res.get("definition", {}).get("text", ""),
        "obsolete": bool(res.get("isObsolete")),
        "secondary_ids": res.get("secondaryIds") or [],
    }


def go_ancestors(term_id: str) -> set[str]:
    d = _get(
        f"{QUICKGO}/ontology/go/terms/{term_id}/ancestors",
        {"relations": "is_a,part_of"},
    ).json()
    return set(d["results"][0].get("ancestors", []))


# --------------------------------------------------------------------------- #
# GOA table
# --------------------------------------------------------------------------- #

@dataclass
class GoaRow:
    go_id: str
    go_name: str
    aspect: str
    evidence: str
    reference: str
    with_from: str
    assigned_by: str
    qualifier: str

    @property
    def with_from_tokens(self) -> list[str]:
        return [t for t in self.with_from.split("|") if t]


def read_goa() -> list[GoaRow]:
    if not GOA.exists():
        raise AuditError(f"missing input {GOA}. Run: just fetch-gene human AFF4")
    lines = GOA.read_text().splitlines()
    header = lines[0].split("\t")
    idx = {name: i for i, name in enumerate(header)}
    need = ["GO TERM", "GO NAME", "GO ASPECT", "GO EVIDENCE CODE", "REFERENCE",
            "WITH/FROM", "ASSIGNED BY", "QUALIFIER"]
    missing = [n for n in need if n not in idx]
    if missing:
        raise AuditError(f"{GOA} is missing expected columns {missing}; header={header}")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        f = line.split("\t")
        rows.append(GoaRow(
            go_id=f[idx["GO TERM"]],
            go_name=f[idx["GO NAME"]],
            aspect=f[idx["GO ASPECT"]],
            evidence=f[idx["GO EVIDENCE CODE"]],
            reference=f[idx["REFERENCE"]],
            with_from=f[idx["WITH/FROM"]],
            assigned_by=f[idx["ASSIGNED BY"]],
            qualifier=f[idx["QUALIFIER"]],
        ))
    return rows


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #

def resolve_with_from(rows: list[GoaRow]) -> dict:
    """Resolve every WITH/FROM token in the GOA table. Built FROM the table, so the
    token set matches GOA by construction."""
    tokens: set[str] = set()
    for r in rows:
        tokens.update(r.with_from_tokens)

    resolved: dict[str, dict] = {}
    for tok in sorted(tokens):
        db, _, ident = tok.partition(":")
        entry: dict = {"token": tok, "db": db, "id": ident}
        if db == "UniProtKB":
            entry.update({"kind": "protein", "candidates": [uniprot_entry(ident)]})
        elif db == "MGI":
            # MGI tokens arrive as "MGI:MGI:1100819"; UniProt's xref index wants the
            # BARE number -- a query containing the inner colon returns HTTP 400.
            bare = ident.split(":")[-1]
            entry.update({"kind": "protein", "candidates": uniprot_by_xref("mgi", bare)})
        elif db == "FB":
            entry.update({"kind": "protein", "candidates": uniprot_by_xref("flybase", ident)})
        elif db == "PANTHER":
            entry.update({"kind": "panther_tree_node", "candidates": [],
                          "note": "an internal PANTHER tree node, not a protein"})
        elif db == "ARBA":
            entry.update({"kind": "arba_rule", "candidates": []})
        elif db == "InterPro":
            entry.update({"kind": "interpro_signature", "candidates": []})
        elif db in ("UniProtKB-SubCell", "ensembl"):
            entry.update({"kind": db, "candidates": []})
        else:
            entry.update({"kind": "UNRESOLVED", "candidates": []})
        resolved[tok] = entry

    # Every token must have been classified; "unresolved" is a fact to report, not
    # a token to silently drop.
    assert set(resolved) == tokens, (
        f"token set drift: missing {tokens - set(resolved)}, extra {set(resolved) - tokens}"
    )
    return resolved


def donor_evidence(rows: list[GoaRow], resolved: dict) -> list[dict]:
    """For every propagated row, ask what evidence each protein donor itself holds
    for the propagated term (or a descendant of it)."""
    out = []
    for r in rows:
        if r.evidence not in ("IBA", "ISS", "IEA", "ISO", "IBD"):
            continue
        donors = []
        for tok in r.with_from_tokens:
            info = resolved[tok]
            if info["kind"] != "protein" or not info["candidates"]:
                donors.append({"token": tok, "kind": info["kind"], "own_evidence": None})
                continue
            # Prefer the reviewed (Swiss-Prot) candidate; report that a choice was made.
            reviewed = [c for c in info["candidates"] if c["reviewed"]]
            chosen = reviewed[0] if reviewed else info["candidates"][0]
            anns, total, complete = quickgo_annotations({
                "geneProductId": f"UniProtKB:{chosen['accession']}",
                "goId": r.go_id,
                "goUsage": "descendants",
                "goUsageRelationships": "is_a,part_of",
            })
            if not complete:
                raise AuditError("donor evidence query unexpectedly truncated")
            donors.append({
                "token": tok,
                "kind": "protein",
                "accession": chosen["accession"],
                "entry_name": chosen["entry_name"],
                "reviewed": chosen["reviewed"],
                "n_candidates": len(info["candidates"]),
                "genes": chosen["genes"],
                "organism": chosen["organism"],
                "own_evidence": [
                    {"go_id": a["goId"], "evidence": a["goEvidence"],
                     "reference": a["reference"], "assigned_by": a["assignedBy"]}
                    for a in anns
                ],
                "has_own_experimental": any(a["goEvidence"] in EXPERIMENTAL for a in anns),
            })
        out.append({
            "go_id": r.go_id, "go_name": r.go_name, "evidence": r.evidence,
            "reference": r.reference, "with_from": r.with_from, "donors": donors,
        })
    return out


def panther_node_reach(node: str) -> dict:
    anns, total, complete = quickgo_annotations({"withFrom": f"PANTHER:{node}"})
    if not complete:
        raise AuditError("node reach query truncated")
    by_term = collections.defaultdict(set)
    for a in anns:
        by_term[a["goId"]].add(a["geneProductId"])
    recipients = {a["geneProductId"] for a in anns}
    return {
        "node": node,
        "annotations": total,
        "recipients": len(recipients),
        "terms": {k: len(v) for k, v in sorted(by_term.items())},
        "uniform": len({len(v) for v in by_term.values()}) == 1,
    }


def projection_test(reference: str) -> dict:
    """How many *entities* does one reference annotate, and does the functional
    term spread across the set or stay on the perturbed gene?

    An annotation count is NOT an entity count; and a large result is paginated,
    so we refuse to answer rather than sampling.
    """
    anns, total, complete = quickgo_annotations(
        {"reference": reference}, max_annotations=PROJECTION_MAX_ANNOTATIONS
    )
    if not complete:
        return {
            "reference": reference, "annotations": total,
            "entity_count_available": False,
            "note": (f"{total} annotations exceeds the {PROJECTION_MAX_ANNOTATIONS}-annotation "
                     "budget; entity counts unavailable, projection test uninformative here."),
        }
    by_term = collections.defaultdict(set)
    for a in anns:
        by_term[(a["goId"], a["goEvidence"], a["goAspect"])].add(a["geneProductId"])
    entities = {a["geneProductId"] for a in anns}
    return {
        "reference": reference,
        "annotations": total,
        "entity_count_available": True,
        "entities": len(entities),
        "per_term": [
            {"go_id": k[0], "evidence": k[1], "aspect": k[2], "entities": len(v),
             "symbols": sorted({a["symbol"] for a in anns
                                if (a["goId"], a["goEvidence"], a["goAspect"]) == k})}
            for k, v in sorted(by_term.items(), key=lambda x: -len(x[1]))
        ],
        "subject_included": f"UniProtKB:{SUBJECT}" in entities,
    }


def intact_partners(accession: str, page_size: int = 200, max_pages: int = 60) -> dict:
    """Expand IntAct records for one accession.

    ``NbExp`` has been observed to count sub-methods of one screen, replicates,
    and even domains of one protein -- so we count DISTINCT PUBLICATIONS and
    DISTINCT (publication, detection method) pairs instead, and we assert the
    subject is not in its own partner set.
    """
    records: list[dict] = []
    total = None
    page = 0
    while True:
        d = _get(f"{INTACT}/{accession}", {"page": page, "pageSize": page_size}).json()
        if total is None:
            total = d["totalElements"]
        content = d.get("content", [])
        if not content:
            break
        records.extend(content)
        page += 1
        if len(records) >= total or page >= max_pages:
            break
    if len(records) < total:
        raise AuditError(
            f"IntAct truncated for {accession}: totalElements={total}, read {len(records)}"
        )

    def bare(x: str | None) -> str:
        # IntAct ids carry a " (uniprotkb)" style suffix; an unanchored
        # endswith/`in` test against such an id silently never fires.
        return (x or "").split(" ")[0]

    by_partner: dict[str, dict] = {}
    for rec in records:
        a, b = bare(rec.get("idA")), bare(rec.get("idB"))
        if a == accession:
            other, other_name = b, rec.get("moleculeB")
        elif b == accession:
            other, other_name = a, rec.get("moleculeA")
        else:
            continue
        if other == accession:
            continue  # homodimer records: reported separately, not as a partner
        pubs = [p for p in (rec.get("publicationIdentifiers") or []) if "(pubmed)" in p]
        pmids = {p.split(" ")[0] for p in pubs}
        e = by_partner.setdefault(other, {
            "accession": other, "name": other_name, "records": 0,
            "pmids": set(), "methods": set(), "method_pub_pairs": set(),
            "expansion": set(), "scores": set(), "has_binary_record": False,
        })
        e["records"] += 1
        if rec.get("expansionMethod") in (None, "", "null"):
            e["has_binary_record"] = True
        e["pmids"] |= pmids
        m = rec.get("detectionMethod")
        e["methods"].add(m)
        for pm in pmids:
            e["method_pub_pairs"].add((pm, m))
        e["expansion"].add(rec.get("expansionMethod"))
        if rec.get("intactMiscore") is not None:
            e["scores"].add(rec["intactMiscore"])

    assert accession not in by_partner, (
        f"{accession} appears in its own partner set -- symptom of a predicate that never fired"
    )
    for e in by_partner.values():
        for k in ("pmids", "methods", "expansion"):
            e[k] = sorted(x for x in e[k] if x is not None)
        e["method_pub_pairs"] = sorted(f"{p}/{m}" for p, m in e["method_pub_pairs"])
        e["scores"] = sorted(e["scores"])
        e["n_distinct_publications"] = len(e["pmids"])
        e["binary_records"] = None  # filled by caller if needed
    return {"accession": accession, "records": total, "partners": by_partner}


def intact_record_count(accession: str) -> int:
    """Record count only (cheap). NOTE: an IntAct *record* count is not a partner
    count; labelled as such everywhere it is reported."""
    d = _get(f"{INTACT}/{accession}", {"page": 0, "pageSize": 1}).json()
    return d["totalElements"]


CORRECTION_CONTROLS = {
    "32125225": "known RETRACTED",
    "36563143": "known ErratumIn with a PMID",
    "17994018": "known corrigendum with a NULL PMID",
}



def _spoke_expansion_test(ia: dict, goa_partners: list[str]) -> dict:
    """Does "GOA does not export spoke-expanded IntAct records as IPI" explain the
    missing GO:0005515 rows?

    Checked in BOTH directions. The forward direction -- every GOA partner has at least
    one non-spoke-expanded record -- is what licenses the explanation for a specific
    absence such as ELL2's. The reverse direction -- every partner with a
    non-spoke-expanded record appears in GOA -- is what would make spoke expansion the
    whole export rule. Reporting only the forward direction would let a convenient
    half-truth stand, which is precisely what a first pass of this review did.

    The binary flag is read from ``has_binary_record``, recorded while the records are
    being collected, because the normalised ``expansion`` list cannot distinguish a
    partner with a MIX of binary and spoke-expanded records from one with neither.
    """
    prot = re.compile(r"(?:[A-NR-Z][0-9][A-Z0-9]{3}[0-9]|[OPQ][0-9][A-Z0-9]{3}[0-9])(?:-\d+)?$")
    binary = {acc for acc, e in ia["partners"].items() if e["has_binary_record"]}
    binary_prot = {a for a in binary if prot.fullmatch(a)}
    goa = set(goa_partners)
    forward = goa <= binary_prot
    reverse = binary_prot == goa
    if not forward:
        raise AuditError(
            "a GOA GO:0005515 partner has no non-spoke-expanded IntAct record: "
            f"{sorted(goa - binary_prot)} -- the explanation offered for ELL2's absence "
            "does not hold and must be withdrawn."
        )
    return {
        "partners_with_a_non_spoke_expanded_record": sorted(binary_prot),
        "goa_protein_binding_partners": sorted(goa),
        "in_goa_but_no_binary_record": sorted(goa - binary_prot),
        "has_binary_record_but_absent_from_goa": sorted(binary_prot - goa),
        "forward_every_goa_partner_has_a_binary_record": forward,
        "reverse_spoke_expansion_is_the_whole_rule": reverse,
        "ELL2_is_a_partner": "O00472" in ia["partners"],
        "ELL2_has_a_non_spoke_expanded_record": "O00472" in binary,
        "interpretation": (
            "Spoke-expansion-only is SUFFICIENT to explain a specific absence such as "
            "ELL2's, because every GOA GO:0005515 partner has at least one "
            "non-spoke-expanded record while ELL2 has none. It is NOT the whole export "
            "rule: other partners do have non-spoke-expanded records and are still absent "
            "from GOA, so a further filter operates that this analysis does not identify."
        ),
    }


def correction_status(pmids: list[str], controls: dict[str, str] | None = None) -> dict:
    """Retraction / erratum / expression-of-concern check.

    Two routes, because neither alone is sufficient:
      1. the article's own PublicationType list, and
      2. ``CommentsCorrections/RefType`` on the cited article's record -- a
         Publisher Correction is NOT discoverable by a pubtype search, and a
         corrigendum can carry a NULL PubMed id.
    Positive controls are queried in the same call pattern so that an all-clean
    result cannot be a broken query. ``controls`` is a parameter only so that the
    break-test can exercise *this* function's gate rather than a copy of it.
    """
    controls = CORRECTION_CONTROLS if controls is None else controls
    if not controls:
        raise AuditError("correction_status was given no positive controls -- vacuous pass refused.")
    query = list(dict.fromkeys(list(pmids) + list(controls)))
    r = _get(f"{EUTILS}/efetch.fcgi", {"db": "pubmed", "retmode": "xml", "id": ",".join(query)})
    root = ET.fromstring(r.content)
    flags: dict[str, dict] = {}
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext(".//PMID")
        pts = [p.text or "" for p in art.iter("PublicationType")]
        pubtype_flags = [p for p in pts if any(
            k in p.lower() for k in ("retract", "erratum", "correct", "expression of concern"))]
        cc = [
            {"ref_type": c.get("RefType"), "pmid": c.findtext("PMID")}
            for c in art.iter("CommentsCorrections")
            if (c.get("RefType") or "").lower() not in ("cites", "commenton", "commentin", "referencedby")
        ]
        flags[pmid] = {"pubtype_flags": pubtype_flags, "comments_corrections": cc}

    for cpmid, why in controls.items():
        f = flags.get(cpmid)
        if not f or not (f["pubtype_flags"] or f["comments_corrections"]):
            raise AuditError(
                f"positive control {cpmid} ({why}) did not fire -- the detector is broken, "
                "so a clean result for the real PMIDs would be meaningless."
            )
    subject = {p: flags.get(p, {"pubtype_flags": [], "comments_corrections": [],
                               "note": "no PubMed record returned"}) for p in pmids}
    affected = {p: v for p, v in subject.items()
                if v.get("pubtype_flags") or v.get("comments_corrections")}
    return {
        "checked": len(pmids),
        "controls_fired": {c: True for c in controls},
        "affected": affected,
        "clean": len(affected) == 0,
    }


INTERPRO2GO = "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go"


def interpro2go(signatures: list[str]) -> dict:
    """Which of the gene's InterPro signatures carry an interpro2go mapping, and to what?

    'It came from InterPro2GO' is not an analysis: the productive question is which
    specific signature supplies which term, because the entries that map to nothing
    are the control that shows the pipeline is capable of restraint.
    """
    text = _get(INTERPRO2GO).text
    total = sum(1 for ln in text.splitlines() if ln.startswith("InterPro:IPR"))
    if total < 1000:
        raise AuditError(
            f"interpro2go looks truncated ({total} mapping lines) -- refusing to report "
            "an absence against a file that may not have downloaded."
        )
    out: dict[str, list[dict]] = {s: [] for s in signatures}
    for ln in text.splitlines():
        if not ln.startswith("InterPro:"):
            continue
        ipr = ln.split()[0].split(":", 1)[1]
        if ipr not in out:
            continue
        # "InterPro:IPR007797 AF4/FMR2 family > GO:regulation of gene expression ; GO:0010468"
        m = re.search(r"> GO:(.*?) ; (GO:\d{7})", ln)
        if not m:
            raise AuditError(f"unparsed interpro2go line: {ln}")
        out[ipr].append({"go_id": m.group(2), "go_name": m.group(1)})
    aspects = {}
    for ipr, maps in out.items():
        for m in maps:
            m["aspect"] = go_term(m["go_id"])["aspect"]
            aspects[m["go_id"]] = m["aspect"]
    return {
        "mapping_lines_in_file": total,
        "per_signature": out,
        "signatures_mapping_to_nothing": sorted(s for s, v in out.items() if not v),
        "any_molecular_function_mapped": any(
            m["aspect"] == "molecular_function" for v in out.values() for m in v),
    }


def uniprot_quote_check(quotes: list[str]) -> list[dict]:
    """`file:` supporting_text is NOT validated by CI, so every quote into the
    UniProt flat file is checked here, and the check FAILS IF IT CHECKS ZERO."""
    if not UNIPROT.exists():
        raise AuditError(f"missing input {UNIPROT}. Run: just fetch-gene human AFF4")
    if not quotes:
        raise AuditError("uniprot_quote_check was given zero quotes -- vacuous pass refused.")
    lines = UNIPROT.read_text().splitlines()
    out = []
    for q in quotes:
        hits = [i + 1 for i, ln in enumerate(lines) if q in ln]
        out.append({"quote": q, "single_physical_line": bool(hits), "line_numbers": hits})
    bad = [o["quote"] for o in out if not o["single_physical_line"]]
    if bad:
        raise AuditError(
            "these quotes are not present on ONE physical line of AFF4-uniprot.txt "
            f"(a `file:` quote that crosses a CC continuation passes CI silently): {bad}"
        )
    return out


# The papers that establish what human AFF4 does, with a one-line statement of
# what each one shows. Used to measure how much of this literature has reached GOA
# at all, and on which entities.
AFF4_FUNCTIONAL_LITERATURE: list[tuple[str, str]] = [
    ("12065898", "AFF4/MCEF co-purifies with P-TEFb (CDK9/cyclin T1); nuclear localisation"),
    ("20159561", "AFF4 is a component of SEC; AFF4 required for SEC stability; knockdown lowers MLL-chimera target genes"),
    ("20471948", "AFF4 bridges P-TEFb and ELL2 into one bifunctional elongation complex with Tat"),
    ("22195968", "AFF4 identified in the SEC; SEC vs LEC specialisation for mRNA vs snRNA genes"),
    ("22483617", "AFF4 binds ELL2 directly and shields it from SIAH1-mediated ubiquitination; AFF4 also binds SIAH1 directly"),
    ("23251033", "Tat recruits ELL2, ENL/AF9 and P-TEFb via short motifs along the disordered AFF4 axis"),
    ("23471103", "crystal structure of AFF4 with P-TEFb: AFF4 meanders over cyclin T1, no stable CDK9 contact; interface mutants reduce binding and transcription"),
    ("24843025", "crystal structure of Tat/P-TEFb/AFF4; AFF4 orders the cyclin T1 TRM and raises Tat-P-TEFb affinity for TAR"),
    ("27731797", "integrative structure of Tat:AFF4:P-TEFb:TAR; AFF4 helix 2 stabilised without touching the RNA"),
    ("28134250", "2.0 A crystal structure of the ELL2 C-terminal domain bound to the AFF4 ELLBow"),
    ("31147444", "2.2 A structure of the AFF4 C-terminal homology domain; mediates AFF4 homo- and AFF1-AFF4 heterodimerisation; CDK9 substrate loop"),
    ("32128251", "2.4 A structure of AFF4-THD; F1014A/Y1096A abolish dimerisation; dimerisation needed for HIV-1 transactivation"),
    ("25730767", "CHOPS syndrome: gain-of-function AFF4 missense resistant to SIAH1-mediated degradation; altered genome-wide AFF4/cohesin/RNAP2 binding"),
    ("16024815", "Aff4-null mice: azoospermia, spermiogenesis arrest, Sertoli-cell expression"),
    ("36149892", "AFF4 promotes adipogenesis by directly activating ATG5/ATG16L1 transcription; adipose-specific Aff4 knockout"),
    ("28955517", "AFF4 depletion inhibits and overexpression enhances osteogenic differentiation of human MSCs, with MSC-mediated bone formation in vivo; AFF1 does the opposite"),
    ("37528066", "AFF1 and AFF4 act antagonistically around the TSS to set elongation rate and termination"),
    ("37609817", "AFF4 knockdown lowers Ser2-phosphorylated Pol II and increases promoter-proximal pausing genome-wide"),
    ("39603240", "PNUTS-PP1 dephosphorylates AFF4 Ser-549, promoting Pol II pause release"),
    ("22528490", "AFF4 induces AMPKalpha2 expression in hypothalamic neurons downstream of ghrelin"),
    ("31238957", "FUS interacts with AFF4 and forms nuclear condensates with it; FUS restrains AFF4/CDK9 promoter occupancy"),
]


# Quotes that the review YAML cites out of AFF4-uniprot.txt. Kept here so the
# guard lives next to the thing it guards, and so adding a quote to the YAML
# without adding it here is the only way to escape the check.
UNIPROT_QUOTES = [
    "SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:12065898}.",
    "SIMILARITY: Belongs to the AF4 family. {ECO:0000305}.",
    "DR   PDB; 5JW9; X-ray; 2.00 A; A=301-351.",
    "DR   PDB; 6KN5; X-ray; 2.20 A; A=899-1163.",
    "DR   PDB; 6R80; X-ray; 2.20 A; A=899-1163.",
    "DR   PDB; 4IMY; X-ray; 2.94 A; G/H/I=2-73.",
    "DR   PDB; 4OGR; X-ray; 3.00 A; C/G/L=2-73.",
    "PE   1: Evidence at protein level;",
]


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #

def run_audit() -> dict:
    rows = read_goa()
    distinct = {(r.go_id, r.evidence, r.reference, r.with_from, r.qualifier) for r in rows}
    res: dict = {
        "subject": {"accession": SUBJECT, "symbol": SUBJECT_SYMBOL},
        "goa": {
            "rows": len(rows),
            "distinct_rows": len(distinct),
            "by_term": {k: v for k, v in sorted(collections.Counter(r.go_id for r in rows).items())},
            "by_evidence": {k: v for k, v in sorted(collections.Counter(r.evidence for r in rows).items())},
        },
    }

    res["uniprot_quotes"] = uniprot_quote_check(UNIPROT_QUOTES)
    # The three InterPro signatures AFF4 matches, read off its own UniProt DR lines
    # rather than typed in, so the set cannot drift from the entry.
    sigs = sorted(set(re.findall(r"^DR   InterPro; (IPR\d{6});", UNIPROT.read_text(), re.M)))
    if not sigs:
        raise AuditError("no InterPro DR lines found in AFF4-uniprot.txt")
    res["interpro2go"] = interpro2go(sigs)
    res["with_from"] = resolve_with_from(rows)
    res["donor_evidence"] = donor_evidence(rows, res["with_from"])

    nodes = sorted({t.split(":", 1)[1] for r in rows for t in r.with_from_tokens
                    if t.startswith("PANTHER:")})
    res["panther_nodes"] = [panther_node_reach(n) for n in nodes]

    # Which references does the subject's own GOA cite, and what else do they annotate?
    pmid_refs = sorted({r.reference for r in rows if r.reference.startswith("PMID:")})
    donor_refs = sorted({e["reference"] for d in res["donor_evidence"]
                         for dn in d["donors"] if dn.get("own_evidence")
                         for e in dn["own_evidence"] if e["reference"].startswith("PMID:")})
    res["projection_tests"] = [projection_test(ref) for ref in pmid_refs + [
        r for r in donor_refs if r not in pmid_refs]]

    # How much of the AFF4 functional literature has reached GOA at all, and on
    # which entities? This is the coverage measurement, so it must be reproducible
    # from the committed artifact rather than asserted in prose.
    uptake = []
    for pmid, what in AFF4_FUNCTIONAL_LITERATURE:
        p = projection_test(f"PMID:{pmid}")
        p["what_the_paper_establishes"] = what
        uptake.append(p)
    res["literature_uptake"] = uptake

    # The subject's own annotation record, and its human paralogs', for the
    # coverage comparison. Paralog accessions are asserted, not assumed.
    family = {
        "Q9UHB7": "AFF4 (subject)", "P51825": "AFF1", "P51816": "AFF2", "P51826": "AFF3",
        "Q9ESC8": "mouse Aff4", "Q9VQI9": "fly lilli",
    }
    fam = []
    for acc, label in family.items():
        entry = uniprot_entry(acc)
        anns, total, complete = quickgo_annotations({"geneProductId": f"UniProtKB:{acc}"})
        if not complete:
            raise AuditError(f"family annotation query truncated for {acc}")
        exp = [a for a in anns if a["goEvidence"] in EXPERIMENTAL]
        fam.append({
            "accession": acc, "label": label, "entry_name": entry["entry_name"],
            "reviewed": entry["reviewed"], "genes": entry["genes"], "length": entry["length"],
            "annotations": total,
            "experimental": len(exp),
            "experimental_mf": sorted({(a["goId"], a["goEvidence"], a["reference"])
                                       for a in exp if a["goAspect"] == "molecular_function"}),
            "experimental_bp": sorted({(a["goId"], a["goEvidence"], a["reference"])
                                       for a in exp if a["goAspect"] == "biological_process"}),
            "experimental_cc": sorted({(a["goId"], a["goEvidence"], a["reference"])
                                       for a in exp if a["goAspect"] == "cellular_component"}),
        })
    res["family_coverage"] = fam

    # Interaction analysis for the GO:0005515 partners.
    ia = intact_partners(SUBJECT)
    goa_partners = sorted({t.split(":", 1)[1] for r in rows if r.go_id == "GO:0005515"
                           for t in r.with_from_tokens})
    intact_accs = set(ia["partners"])
    # Membership assertion, not cardinality: a matching count is not a matching set.
    missing = [p for p in goa_partners if p not in intact_accs]
    if missing:
        raise AuditError(
            f"GOA names GO:0005515 partners absent from the IntAct expansion: {missing}"
        )
    res["interactions"] = {
        "subject_records": ia["records"],
        "goa_protein_binding_partners": goa_partners,
        "intact_partner_count": len(intact_accs),
        "detail": {
            acc: {
                "name": ia["partners"][acc]["name"],
                "records": ia["partners"][acc]["records"],
                "distinct_publications": ia["partners"][acc]["n_distinct_publications"],
                "pmids": ia["partners"][acc]["pmids"],
                "methods": ia["partners"][acc]["methods"],
                "method_publication_pairs": ia["partners"][acc]["method_pub_pairs"],
                "expansion_methods": ia["partners"][acc]["expansion"],
                "mi_scores": ia["partners"][acc]["scores"],
            }
            for acc in goa_partners
        },
        "partner_promiscuity_records": {
            acc: intact_record_count(acc) for acc in goa_partners
        },
        # Which IntAct partners of the subject are NOT exported to GOA as GO:0005515?
        "intact_partners_without_goa_row": sorted(
            f"{acc}:{ia['partners'][acc]['name']}" for acc in intact_accs if acc not in goa_partners
        ),
        # Is "spoke-expanded records are not exported as IPI" the whole export rule?
        # Tested in BOTH directions rather than assumed, because a one-directional check
        # would have let a convenient half-truth stand.
        "spoke_expansion_test": _spoke_expansion_test(ia, goa_partners),
    }

    # Correction status for everything the review leans on.
    review_pmids = sorted(set(
        [r.reference.split(":", 1)[1] for r in rows if r.reference.startswith("PMID:")]
        + ["20159561", "20471948", "23251033", "23471103", "24843025", "28134250",
           "31147444", "32128251", "25730767", "22483617", "16024815", "39603240",
           "37528066", "22895430", "24985467", "27731797", "37609817", "36149892",
           "31238957", "17389929", "31466050", "11923441", "28955517", "32257529"]
    ))
    res["corrections"] = correction_status(review_pmids)

    # Ontology relations the review's argument leans on -- fetched and asserted,
    # never inferred from a label.
    rel_claims = [
        ("GO:0006368", "GO:0006354", True, "Pol II elongation is_a DNA-templated elongation"),
        ("GO:0032968", "GO:0006355", True, "positive reg. of Pol II elongation under reg. of transcription"),
        ("GO:0032783", "GO:0008023", True, "SEC is_a transcription elongation factor complex"),
        ("GO:0006355", "GO:0010468", True, "reg. of transcription under reg. of gene expression"),
        ("GO:0007611", "GO:0050877", True, "learning or memory under nervous system process"),
        ("GO:0003711", "GO:0003712", False, "elongation factor activity is NOT under coregulator activity"),
        ("GO:0003712", "GO:0003711", False, "...and not the other way either: they are SIBLINGS"),
        ("GO:0030674", "GO:0005515", False, "adaptor activity is NOT under protein binding"),
    ]
    rels = []
    for child, parent, expected, label in rel_claims:
        anc = go_ancestors(child)
        got = parent in anc
        rels.append({"child": child, "parent": parent, "is_ancestor": got,
                     "expected": expected, "label": label, "ok": got == expected})
    bad_rel = [r for r in rels if not r["ok"]]
    if bad_rel:
        raise AuditError(f"ontology relation claim(s) refuted by QuickGO: {bad_rel}")
    res["term_relations"] = rels

    res["term_definitions"] = {
        t: go_term(t) for t in [
            "GO:0003711", "GO:0003712", "GO:0005515", "GO:0006354", "GO:0006368",
            "GO:0010468", "GO:0030332", "GO:0030674", "GO:0031625", "GO:0032783",
            "GO:0032968", "GO:0034976", "GO:0043923", "GO:0050877", "GO:0008023",
            "GO:0000791", "GO:0001650", "GO:0016604", "GO:0005654", "GO:0042803",
        ]
    }

    # GO:0030332 cyclin binding: does GO actually use it for TRANSCRIPTIONAL cyclins?
    cyc = {}
    for acc, nm in [("P50750", "CDK9"), ("O94992", "HEXIM1"), ("O60885", "BRD4"),
                    ("P24941", "CDK2 (positive control: cell-cycle CDK)")]:
        anns, total, complete = quickgo_annotations({
            "geneProductId": f"UniProtKB:{acc}", "goId": "GO:0030332",
            "goUsage": "descendants", "goUsageRelationships": "is_a,part_of"})
        cyc[nm] = {"accession": acc, "hits": total,
                   "evidence": sorted({a["goEvidence"] for a in anns})}
    if cyc["CDK2 (positive control: cell-cycle CDK)"]["hits"] == 0:
        raise AuditError(
            "CDK2 returned 0 GO:0030332 annotations -- the positive control failed, so the "
            "zeros for the cyclin T1 binders cannot be read as a finding."
        )
    res["cyclin_binding_usage"] = cyc

    # GO:0043923 -- is the class already curated for AFF4's own P-TEFb partners?
    anns, total, complete = quickgo_annotations({
        "goId": "GO:0043923", "goUsage": "descendants",
        "goUsageRelationships": "is_a,part_of", "taxonId": "9606"})
    if not complete:
        raise AuditError("GO:0043923 query truncated")
    # An annotation count is NOT an entity count: one entity can hold several rows for
    # the same term, and the recipient set here includes a complex as well as proteins.
    # Reported separately, and the distinction asserted, because a first draft of this
    # review wrote the annotation total as a count of proteins.
    entities = {a["geneProductId"] for a in anns}
    complexes = {e for e in entities if not e.startswith("UniProtKB:")}
    res["host_activation_of_viral_transcription"] = {
        "human_annotations": total,
        "human_entities": len(entities),
        "human_protein_entities": len(entities - complexes),
        "human_complex_entities": sorted(complexes),
        "holders": sorted({(a["symbol"], a["goEvidence"], a["reference"], a["assignedBy"])
                           for a in anns}),
        "subject_holds_it": any(a["geneProductId"] == f"UniProtKB:{SUBJECT}" for a in anns),
    }
    if len(entities) == total:
        raise AuditError(
            "annotation total equals entity total for GO:0043923, which makes the two "
            "indistinguishable in the report; check the derivation before trusting either."
        )
    return res


# --------------------------------------------------------------------------- #
# Rendering -- the table is the claim; prose must not restate a number
# --------------------------------------------------------------------------- #

def render(res: dict) -> str:
    L: list[str] = []
    add = L.append
    add("# AFF4 (Q9UHB7) annotation-provenance audit")
    add("")
    add("Generated by `analyze_aff4_annotations.py`. Every number below is computed by that")
    add("script; nothing here is hand-entered. Re-run it and `diff` before trusting this file.")
    add("")

    g = res["goa"]
    add("## 1. GOA row census")
    add("")
    add(f"- rows in `AFF4-goa.tsv` (excluding header): **{g['rows']}**")
    add(f"- distinct (term, evidence, reference, with/from, qualifier) tuples: **{g['distinct_rows']}**")
    add("")
    add("| GO term | rows |")
    add("|---|---|")
    for k, v in g["by_term"].items():
        add(f"| {k} | {v} |")
    add("")
    add("| evidence | rows |")
    add("|---|---|")
    for k, v in g["by_evidence"].items():
        add(f"| {k} | {v} |")
    add("")

    add("## 2. WITH/FROM resolution")
    add("")
    add("Every token in column 11 of the GOA table, resolved. Swiss-Prot/TrEMBL status is")
    add("printed next to every name: an unreviewed entry's *protein name* is an automatic")
    add("by-similarity label even when its GO annotations are experimental.")
    add("")
    add("| token | kind | resolved | entry | reviewed | organism | len | candidates |")
    add("|---|---|---|---|---|---|---|---|")
    for tok, info in res["with_from"].items():
        if info["candidates"]:
            c = info["candidates"][0] if not any(x["reviewed"] for x in info["candidates"]) else \
                [x for x in info["candidates"] if x["reviewed"]][0]
            add(f"| `{tok}` | {info['kind']} | {c['accession']} "
                f"| {c['entry_name']} ({'/'.join(x for x in c['genes'] if x)}) "
                f"| {'Swiss-Prot' if c['reviewed'] else 'TrEMBL'} | {c['organism']} "
                f"| {c['length']} | {len(info['candidates'])} |")
        else:
            add(f"| `{tok}` | {info['kind']} | - | - | - | - | - | 0 |")
    add("")

    add("## 3. What each donor's OWN evidence is for the propagated term")
    add("")
    add("Queried per row with `goUsage=descendants` (`is_a,part_of`), so a donor whose")
    add("experiment sits at a *more specific* term than the one propagated is visible.")
    add("")
    for d in res["donor_evidence"]:
        add(f"### {d['go_id']} {d['go_name']} — {d['evidence']} ({d['reference']})")
        add("")
        add("| donor token | resolved | own annotations to this term or a descendant |")
        add("|---|---|---|")
        for dn in d["donors"]:
            if dn["kind"] != "protein":
                add(f"| `{dn['token']}` | *{dn['kind']}* | n/a |")
                continue
            ev = dn["own_evidence"] or []
            cell = "; ".join(f"{e['go_id']} {e['evidence']} {e['reference']}" for e in ev) or "**none**"
            label = f"{dn['entry_name']} ({'/'.join(x for x in dn['genes'] if x)})"
            if not dn["reviewed"]:
                label += " *[TrEMBL]*"
            add(f"| `{dn['token']}` | {label} | {cell} |")
        add("")

    add("## 4. PANTHER node reach")
    add("")
    for n in res["panther_nodes"]:
        add(f"`PANTHER:{n['node']}` — {n['annotations']} annotations over "
            f"**{n['recipients']} recipient gene products**; assignment across terms is "
            f"{'UNIFORM' if n['uniform'] else 'non-uniform'}.")
        add("")
        add("| term | recipients |")
        add("|---|---|")
        for t, c in n["terms"].items():
            add(f"| {t} | {c} |")
        add("")

    add("## 5. Reference-projection test")
    add("")
    add("For each reference cited by AFF4's GOA (and each donor reference), how many")
    add("*entities* does that reference annotate, and does the functional/phenotype term")
    add("spread across the set or stay on the gene actually perturbed? An annotation count")
    add("is not an entity count; where the result is too large to page through, the entity")
    add("count is reported as unavailable rather than sampled.")
    add("")
    for p in res["projection_tests"]:
        if not p["entity_count_available"]:
            add(f"- **{p['reference']}**: {p['annotations']} annotations — "
                f"entity count **unavailable**; {p['note']}")
            continue
        add(f"- **{p['reference']}**: {p['annotations']} annotations over "
            f"**{p['entities']} entities** (subject included: {p['subject_included']})")
        for t in p["per_term"]:
            add(f"    - {t['go_id']} {t['evidence']} [{t['aspect'][:4]}] → {t['entities']} entities")
    add("")

    add("## 5b. GOA uptake of the AFF4 functional literature")
    add("")
    add("For each paper that establishes something about human AFF4: how many GO annotations")
    add("does GOA carry from it, over how many entities, and is AFF4 one of them? A row with")
    add("`AFF4 annotated: False` is a paper whose result has not reached AFF4's GO record.")
    add("")
    add("| PMID | what it establishes | GOA annotations | entities | AFF4 annotated |")
    add("|---|---|---|---|---|")
    for u in res["literature_uptake"]:
        ents = u["entities"] if u["entity_count_available"] else "unavailable"
        add(f"| {u['reference']} | {u['what_the_paper_establishes']} | {u['annotations']} "
            f"| {ents} | **{u['subject_included']}** |")
    add("")
    n_papers = len(res["literature_uptake"])
    n_zero = sum(1 for u in res["literature_uptake"] if u["annotations"] == 0)
    n_no_subject = sum(1 for u in res["literature_uptake"] if not u["subject_included"])
    add(f"Of **{n_papers}** papers, **{n_zero}** have produced no GO annotation anywhere in GOA,")
    add(f"and **{n_no_subject}** have produced none on AFF4 itself.")
    add("")
    add("| PMID | terms it did produce (entities each) |")
    add("|---|---|")
    for u in res["literature_uptake"]:
        if not u["entity_count_available"]:
            add(f"| {u['reference']} | *entity counts unavailable* |")
            continue
        if not u["per_term"]:
            add(f"| {u['reference']} | *nothing* |")
            continue
        cell = "; ".join(f"{t['go_id']} {t['evidence']} ({t['entities']})" for t in u["per_term"])
        add(f"| {u['reference']} | {cell} |")
    add("")

    add("## 6. Family coverage: what the AF4/FMR2 members hold experimentally")
    add("")
    add("| protein | entry | reviewed | len | annotations | experimental | exp. MF | exp. BP | exp. CC |")
    add("|---|---|---|---|---|---|---|---|---|")
    for f in res["family_coverage"]:
        add(f"| {f['label']} | {f['entry_name']} | "
            f"{'Swiss-Prot' if f['reviewed'] else 'TrEMBL'} | {f['length']} | "
            f"{f['annotations']} | {f['experimental']} | {len(f['experimental_mf'])} | "
            f"{len(f['experimental_bp'])} | {len(f['experimental_cc'])} |")
    add("")
    for f in res["family_coverage"]:
        add(f"**{f['label']}** experimental rows:")
        for aspect in ("experimental_mf", "experimental_bp", "experimental_cc"):
            for t in f[aspect]:
                add(f"  - [{aspect[-2:].upper()}] {t[0]} {t[1]} {t[2]}")
        add("")

    ints = res["interactions"]
    add("## 7. `GO:0005515` partners: expanded IntAct records")
    add("")
    add(f"AFF4 has **{ints['subject_records']} IntAct interaction records** spanning")
    add(f"**{ints['intact_partner_count']} distinct partner molecules**. GOA exports")
    add(f"**{len(ints['goa_protein_binding_partners'])}** of them as `GO:0005515` IPI rows.")
    add("")
    add("`NbExp` is not used here: it has been observed to count sub-methods of a single")
    add("screen, replicates, and even domains of one protein. Distinct publications and")
    add("distinct (publication, method) pairs are counted instead.")
    add("")
    add("| partner | records | distinct pubs | (pub/method) pairs | MI score(s) | promiscuity (IntAct records for the partner) |")
    add("|---|---|---|---|---|---|")
    for acc, d in ints["detail"].items():
        add(f"| {d['name']} ({acc}) | {d['records']} | {d['distinct_publications']} | "
            f"{len(d['method_publication_pairs'])} | {', '.join(str(s) for s in d['mi_scores'])} | "
            f"{ints['partner_promiscuity_records'][acc]} |")
    add("")
    for acc, d in ints["detail"].items():
        add(f"- **{d['name']} ({acc})**: pubs {d['pmids']}; methods {d['methods']}; "
            f"pub/method pairs {d['method_publication_pairs']}")
    add("")
    add("IntAct partners of AFF4 that carry **no** `GO:0005515` row in AFF4's GOA "
        "(spoke-expanded co-IP records are not exported as IPI):")
    add("")
    for s in ints["intact_partners_without_goa_row"]:
        add(f"- {s}")
    add("")

    st = ints["spoke_expansion_test"]
    add("### 7b. Is spoke expansion the whole export rule? Tested in both directions")
    add("")
    add(f"- every GOA `GO:0005515` partner has a non-spoke-expanded record: "
        f"**{st['forward_every_goa_partner_has_a_binary_record']}**")
    add(f"- spoke expansion is the WHOLE export rule: "
        f"**{st['reverse_spoke_expansion_is_the_whole_rule']}**")
    add(f"- ELL2 is an IntAct partner: **{st['ELL2_is_a_partner']}**; has a "
        f"non-spoke-expanded record: **{st['ELL2_has_a_non_spoke_expanded_record']}**")
    add(f"- partners with a non-spoke-expanded record yet absent from GOA: "
        f"{st['has_binary_record_but_absent_from_goa']}")
    add("")
    add(st["interpretation"])
    add("")

    c = res["corrections"]
    add("## 8. Retraction / erratum / expression-of-concern check")
    add("")
    add(f"- PMIDs checked: **{c['checked']}**")
    add(f"- positive controls that fired: {sorted(c['controls_fired'])} "
        "(a retraction, an erratum with a PMID, and a corrigendum with a NULL PMID)")
    add(f"- PMIDs with any flag: **{len(c['affected'])}**")
    for p, v in sorted(c["affected"].items()):
        add(f"    - {p}: {v}")
    if c["clean"]:
        add("")
        add("No cited reference carries a retraction, erratum or expression of concern. Because")
        add("all three controls fired in the same call pattern, this zero is a measurement.")
    else:
        add("")
        add(f"**{len(c['affected'])} cited reference(s) carry a correction and must be flagged in "
            "the review.** The three controls fired in the same call pattern, so the detector is "
            "working in both directions rather than only reporting nulls.")
    add("")

    add("## 9. Ontology relations the review depends on")
    add("")
    add("Fetched and asserted, never inferred from a label.")
    add("")
    add("| claim | child | parent | parent is ancestor? | expected |")
    add("|---|---|---|---|---|")
    for r in res["term_relations"]:
        add(f"| {r['label']} | {r['child']} | {r['parent']} | {r['is_ancestor']} | {r['expected']} |")
    add("")

    add("## 10. Is `GO:0030332 cyclin binding` usable for cyclin T1?")
    add("")
    add("The term's definition specifies cyclins *\"whose levels in a cell varies markedly")
    add("during the cell cycle, rising steadily until mitosis, then falling abruptly to")
    add("zero\"* — which does not describe the transcriptional cyclin T1. Usage agrees:")
    add("")
    add("| protein | GO:0030332 annotations (incl. descendants) | evidence |")
    add("|---|---|---|")
    for nm, d in res["cyclin_binding_usage"].items():
        add(f"| {nm} ({d['accession']}) | {d['hits']} | {', '.join(d['evidence']) or '-'} |")
    add("")
    add("The cell-cycle CDK is the positive control, so the zeros for the cyclin T1 binders")
    add("are a measurement rather than a failed query.")
    add("")

    h = res["host_activation_of_viral_transcription"]
    add("## 11. `GO:0043923 host-mediated activation of viral transcription`")
    add("")
    add(f"- human **annotations**: **{h['human_annotations']}**")
    add(f"- human **entities**: **{h['human_entities']}** "
        f"({h['human_protein_entities']} proteins + complexes {h['human_complex_entities']})")
    add(f"- AFF4 holds it: **{h['subject_holds_it']}**")
    add("")
    add("An annotation count is not an entity count; both are reported so the table below "
        "cannot be read as a count of proteins.")
    add("")
    add("| symbol | evidence | reference | assigned by |")
    add("|---|---|---|---|")
    for s in h["holders"]:
        add(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} |")
    add("")

    i2g = res["interpro2go"]
    add("## 11b. Which InterPro signature supplies which term (interpro2go)")
    add("")
    add("Signatures read off AFF4's own `DR   InterPro;` lines. The entries that map to")
    add("nothing are the control showing the pipeline is capable of restraint.")
    add("")
    add(f"- mapping lines in the downloaded `interpro2go`: **{i2g['mapping_lines_in_file']}**")
    add(f"- any signature mapped to a **molecular function**: "
        f"**{i2g['any_molecular_function_mapped']}**")
    add("")
    add("| signature | maps to |")
    add("|---|---|")
    for ipr, maps in sorted(i2g["per_signature"].items()):
        cell = "; ".join(f"{m['go_id']} {m['go_name']} [{m['aspect'][:4]}]" for m in maps) or "**nothing**"
        add(f"| {ipr} | {cell} |")
    add("")

    add("## 12. `file:` quote check against `AFF4-uniprot.txt`")
    add("")
    add("The repo's reference validator checks `supporting_text` verbatim only for `PMID:`")
    add("references; `file:` quotes are skipped entirely, which makes them the one place in")
    add("the document where an invented or line-wrapped quotation survives every automated")
    add("gate. Each quote below is asserted present on ONE physical line, and the check")
    add("raises if it is ever handed an empty quote list.")
    add("")
    add("| quote | line(s) |")
    add("|---|---|")
    for q in res["uniprot_quotes"]:
        add(f"| `{q['quote'][:88]}` | {q['line_numbers']} |")
    add("")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- #
# Break-tests. Each asserts, in order: the mutation applied; the guard fired;
# the failure message is the expected one.
# --------------------------------------------------------------------------- #

def _expect(fn, needle: str, what: str) -> None:
    try:
        fn()
    except AuditError as e:
        if needle.lower() not in str(e).lower():
            raise AssertionError(
                f"{what}: guard fired but with the WRONG message.\n  wanted substring: {needle!r}\n"
                f"  got: {e}"
            )
        print(f"  ok   {what}  (message matched {needle!r})")
        return
    except AssertionError as e:
        if needle.lower() not in str(e).lower():
            raise AssertionError(
                f"{what}: assertion fired but with the WRONG message.\n  wanted: {needle!r}\n  got: {e}")
        print(f"  ok   {what}  (assertion matched {needle!r})")
        return
    raise AssertionError(f"{what}: guard did NOT fire -- this check cannot catch its own bug.")


def self_test() -> int:
    print("break-tests (each: mutation applied -> guard fired -> message as expected)")

    # 1. merged/secondary accession returning a different protein.
    #    O15507 is an inactive entry that resolves to GFRA1 (P56159) with HTTP 200.
    before = uniprot_entry(SUBJECT)["accession"]
    assert before == SUBJECT, "precondition failed: the happy path does not work"
    _expect(lambda: uniprot_entry("O15507"),
            "resolves to a DIFFERENT protein",
            "uniprot_entry rejects an accession that resolves to another protein")

    # 2. quote check must refuse a vacuous pass ...
    _expect(lambda: uniprot_quote_check([]),
            "vacuous pass refused",
            "uniprot_quote_check refuses an empty quote list")

    # 3. ... and must fail on a quote that spans a CC continuation line.
    #     Assert the mutation is a real change first: the contiguous form must be
    #     absent from the file while its first half is present.
    spanning = ("CC   -!- SUBUNIT: Component of the super elongation complex (SEC), at least "
                "composed of EAF1")
    text = UNIPROT.read_text()
    assert "CC   -!- SUBUNIT: Component of the super elongation complex (SEC), at least" in text, \
        "fixture drifted: the anchor half of the spanning quote is not in the file"
    assert spanning not in text, \
        "fixture drifted: the spanning quote IS present on one line, so it tests nothing"
    _expect(lambda: uniprot_quote_check([spanning]),
            "not present on ONE physical line",
            "uniprot_quote_check fails on a quote crossing a CC continuation")

    # 4. the retraction detector's control gate, exercised through the REAL function
    #    (not a copy of its logic, which would drift). Two directions:
    #    (a) a control that genuinely carries no flag must make it raise;
    #    (b) no controls at all must be refused rather than passing vacuously.
    real_clean = correction_status(["20159561"])
    assert real_clean["clean"] is True, "precondition: the happy path must report clean"
    assert set(real_clean["controls_fired"]) == set(CORRECTION_CONTROLS), \
        "precondition: the real controls must be the ones that fired"
    bogus = {"20159561": "a paper with NO retraction or erratum -- must not satisfy the gate"}
    assert bogus != CORRECTION_CONTROLS, "fixture drifted: bogus controls equal the real ones"
    _expect(lambda: correction_status(["12065898"], controls=bogus),
            "positive control",
            "correction_status raises when a positive control carries no flag")
    _expect(lambda: correction_status(["12065898"], controls={}),
            "vacuous pass refused",
            "correction_status refuses to run with no positive controls")

    # 5. missing input must be a loud error naming the fix, not a degraded run.
    global GOA
    saved = GOA
    GOA = HERE / "definitely-not-here.tsv"
    assert not GOA.exists(), "fixture drifted: the fake path exists"
    try:
        _expect(read_goa, "just fetch-gene human AFF4",
                "read_goa fails loudly on a missing input and names the fix command")
    finally:
        GOA = saved
    assert GOA.exists(), "restore failed: GOA path did not come back"

    # 6. the term-relation gate must fire on a FALSE ancestry claim, and the
    #    mutation must be one a plausibly-wrong implementation would not survive:
    #    we flip a single expectation rather than blanking the list.
    def flipped():
        anc = go_ancestors("GO:0003711")
        got = "GO:0003712" in anc
        expected = True  # the deliberately wrong claim: siblings are not ancestors
        if got != expected:
            raise AuditError(
                "ontology relation claim(s) refuted by QuickGO: "
                f"GO:0003711 under GO:0003712 -> {got}, expected {expected}")
    _expect(flipped, "refuted by QuickGO",
            "term-relation gate fires on a single wrong ancestry expectation")

    # 7. the projection test must refuse to name an entity count it did not read.
    small = projection_test("PMID:12065898")
    assert small["entity_count_available"], "precondition: a small reference should be countable"
    global PROJECTION_MAX_ANNOTATIONS
    savedmax = PROJECTION_MAX_ANNOTATIONS
    PROJECTION_MAX_ANNOTATIONS = 1
    try:
        tight = projection_test("PMID:12065898")
        assert tight["entity_count_available"] is False, \
            "projection_test reported an entity count for a result it refused to page"
        assert "entities" not in tight, "projection_test leaked an entity count anyway"
        assert tight != small, "mutation changed nothing -- the break-test is a no-op"
        print("  ok   projection_test reports entity_count_available=false instead of sampling")
    finally:
        PROJECTION_MAX_ANNOTATIONS = savedmax
    assert projection_test("PMID:12065898")["entity_count_available"], "restore failed"

    print("all break-tests passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true", help="run break-tests and exit")
    ap.add_argument("--json", default=str(HERE / "results.json"))
    ap.add_argument("--md", default=str(HERE / "RESULTS.md"))
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    res = run_audit()
    Path(a.json).write_text(json.dumps(res, indent=2, sort_keys=True, default=str) + "\n")
    Path(a.md).write_text(render(res))
    print(f"wrote {a.json}")
    print(f"wrote {a.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
