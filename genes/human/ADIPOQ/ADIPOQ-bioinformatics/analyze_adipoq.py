#!/usr/bin/env python3
"""Reproducible evidence for the human ADIPOQ (Q15848) GO annotation review.

Five independent checks, each of which decides at least one verdict in
``ADIPOQ-ai-review.yaml``:

A. ``goa_reconciliation`` -- how many distinct GOA rows exist, and how many the
   ``fetch-gene`` stub collapsed.  The seeder keys entries on
   ``(GO id, evidence, reference, negated, qualifier)`` and omits ``WITH/FROM``,
   so per-partner IPI rows collapse.  We need one review entry per GOA row.

B. ``reference_projection`` -- for every reference that supplies a TAS / RCA /
   NAS / HDA row, ask QuickGO how many *distinct entities* that same reference
   annotates.  One reference giving N entities one identical term is a bulk
   import, not N author statements.

C. ``intact_census`` -- how many *distinct experiments* (not ``NbExp``
   sub-methods) support the ``GO:0005515`` rows, and where each partner lives.
   ADIPOQ is a cleaved-signal-peptide secreted protein; a partner confined to
   the cytosol/nucleus/mitochondrion cannot meet it in vivo.

D. ``iba_donors`` -- resolve every IBA WITH/FROM token and ask what evidence
   that donor itself carries *for the propagated term*.

E. ``thermogenesis_cross_product`` -- GO:0120162 (positive) and GO:0120163
   (negative) regulation of cold-induced thermogenesis are each cited to *both*
   PMID:24531262 and PMID:26166748.  Detect the full 2x2 cross-product, which
   is a citation defect independent of what the papers say.

Design rules taken from the campaign brief:
  * anti-truncation guards compare ``numberOfHits`` against ``len(results)``,
    never against a page-size constant we chose;
  * ``entryType.startswith("UniProtKB reviewed")`` -- ``"reviewed" in x`` also
    matches ``"unreviewed"``;
  * every accession lookup prints the entry name, and an empty/dead entry is a
    hard error, not a silent zero;
  * missing input is a hard error naming the fix command, never a quiet
    ``{"available": False}``.

Usage::

    uv run python analyze_adipoq.py            # run all checks, write results.json
    uv run python analyze_adipoq.py --self-test  # break-test the guards
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "ADIPOQ-goa.tsv"
REVIEW_YAML = GENE_DIR / "ADIPOQ-ai-review.yaml"
RESULTS_JSON = HERE / "results.json"

ACC = "Q15848"

QUICKGO_ANN = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTACT = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"

# QuickGO clamps annotation search results-per-page at 100.  We never compare
# against this number; it is only the page size we request.
PAGE = 100

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}

# Compartments a cleaved-signal-peptide secreted protein cannot reach.
CYTOFACING = ("Cytoplasm", "Cytosol", "Nucleus", "Mitochondrion",
              "Peroxisome", "Cytoplasmic")


class CheckFailure(Exception):
    """A check could not be computed.  Never degrade silently."""


def _get_json(url: str, tries: int = 4) -> dict:
    last = None
    for i in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            resp = urllib.request.urlopen(req, timeout=90)
        except urllib.error.HTTPError as exc:            # noqa: PERF203
            last = f"HTTP {exc.code} for {url}"
            if exc.code in (400, 404):
                raise CheckFailure(last) from exc
        except Exception as exc:                          # network flake
            last = f"{type(exc).__name__}: {exc} for {url}"
        else:
            # Assert the HTTP status explicitly: a rejected query and an empty
            # result look identical downstream.
            if resp.status != 200:
                raise CheckFailure(f"HTTP {resp.status} for {url}")
            return json.load(resp)
        time.sleep(2 * (i + 1))
    raise CheckFailure(f"gave up after {tries} tries: {last}")


# --------------------------------------------------------------------------
# A. GOA row reconciliation
# --------------------------------------------------------------------------

def read_goa() -> tuple[list[dict], list[str]]:
    if not GOA_TSV.exists():
        raise CheckFailure(
            f"missing {GOA_TSV}; run `just fetch-gene human ADIPOQ` to create it")
    lines = GOA_TSV.read_text().splitlines()
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        rows.append(dict(zip(header, line.split("\t"))))
    return rows, header


def goa_reconciliation(rows: list[dict]) -> dict:
    """Count GOA rows against the review YAML's ``- term:`` entries."""
    def key(r):
        return (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"],
                r["QUALIFIER"], r["WITH/FROM"], r["ASSIGNED BY"])

    distinct = {key(r) for r in rows}
    # what the seeder would produce: WITH/FROM and ASSIGNED BY dropped
    seeder_key = {(r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"],
                   r["QUALIFIER"]) for r in rows}

    review_entries = review_new = None
    if REVIEW_YAML.exists():
        rtxt = REVIEW_YAML.read_text()
        review_entries = sum(1 for ln in rtxt.splitlines()
                             if ln.startswith("- term:"))
        # NEW rows are the reviewer's own proposals, not GOA rows, so they are
        # excluded before reconciling.  Counted from the emitted file, which is
        # the artifact that ships.
        review_new = len(re.findall(r"^\s*action:\s*NEW\s*$", rtxt, re.M))

    return {
        "goa_rows_raw": len(rows),
        "goa_rows_distinct": len(distinct),
        "seeder_collapsed_to": len(seeder_key),
        "collapse_loss": len(distinct) - len(seeder_key),
        "review_yaml_entries": review_entries,
        "review_yaml_new_rows": review_new,
        "review_yaml_from_goa": (None if review_entries is None
                                 else review_entries - review_new),
        "reconciles": (review_entries - review_new == len(distinct)
                       if review_entries is not None else None),
    }


# --------------------------------------------------------------------------
# B. Reference-projection test
# --------------------------------------------------------------------------

def _quickgo_all(params: dict, cap_annotations: int = 3000):
    """Fully paginate a QuickGO annotation search.

    Returns ``(results, numberOfHits, complete)``.  ``complete`` is False when
    the reference is too large to paginate honestly -- in which case entity
    counts are reported as unavailable rather than derived from a sample.
    """
    first = dict(params, limit=PAGE, page=1)
    d = _get_json(QUICKGO_ANN + "?" + urllib.parse.urlencode(first))
    total = d["numberOfHits"]
    if total > cap_annotations:
        return [], total, False
    out = list(d["results"])
    page = 1
    while len(out) < total:
        page += 1
        d = _get_json(QUICKGO_ANN + "?" +
                      urllib.parse.urlencode(dict(params, limit=PAGE, page=page)))
        if not d["results"]:
            break
        out.extend(d["results"])
    # Compare against len(results), never against the page size we chose.
    if len(out) != total:
        raise CheckFailure(
            f"truncated: got {len(out)} of numberOfHits={total} for {params}")
    return out, total, True


def reference_projection(rows: list[dict]) -> dict:
    """For each non-IEA/non-experimental-primary reference, count entities."""
    interesting = {"TAS", "NAS", "RCA", "HDA", "IPI"}
    refs = sorted({r["REFERENCE"] for r in rows
                   if r["GO EVIDENCE CODE"] in interesting
                   and r["REFERENCE"].startswith("PMID:")})
    out = {}
    for ref in refs:
        results, total, complete = _quickgo_all({"reference": ref})
        if not complete:
            out[ref] = {
                "annotations": total,
                "entities": None,
                "note": "too large to paginate; entity count unavailable, "
                        "projection test not run",
                "our_terms": sorted({r["GO TERM"] for r in rows
                                     if r["REFERENCE"] == ref}),
            }
            continue
        per_term = defaultdict(set)
        ev = defaultdict(set)
        by = defaultdict(set)
        for a in results:
            per_term[a["goId"]].add(a["geneProductId"])
            ev[a["goId"]].add(a["goEvidence"])
            by[a["goId"]].add(a["assignedBy"])
        out[ref] = {
            "annotations": total,
            "entities": len({a["geneProductId"] for a in results}),
            "terms": {
                g: {"entities": len(s),
                    "evidence": sorted(ev[g]),
                    "assigned_by": sorted(by[g])}
                for g, s in sorted(per_term.items(), key=lambda kv: -len(kv[1]))
            },
            "our_terms": sorted({r["GO TERM"] for r in rows
                                 if r["REFERENCE"] == ref}),
        }
    return out


# --------------------------------------------------------------------------
# C. IntAct census + partner topology
# --------------------------------------------------------------------------

def _uniprot_entry(acc: str) -> dict:
    """Resolve one accession.  A dead/empty entry is a hard error."""
    base = acc.split("-")[0]
    url = (f"{UNIPROT}/{base}.json?fields=id,accession,protein_name,gene_names,"
           f"organism_name,length,cc_subcellular_location,ft_signal,ft_transmem")
    d = _get_json(url)
    name = d.get("uniProtkbId")
    if not name:
        raise CheckFailure(
            f"{acc} resolved to an entry with no entry name -- likely a deleted "
            f"accession; a silent zero here would read as 'no annotations'")
    locs = []
    for c in d.get("comments", []):
        if c["commentType"] == "SUBCELLULAR LOCATION":
            for l in c.get("subcellularLocations", []):
                v = l.get("location", {}).get("value")
                if v:
                    locs.append(v)
    feats = Counter(f["type"] for f in d.get("features", []))
    return {
        "accession": base,
        "entry_name": name,
        # "reviewed" is a substring of "unreviewed" -- anchor the test.
        "reviewed": d["entryType"].startswith("UniProtKB reviewed"),
        "entry_type": d["entryType"],
        "gene": ([g["geneName"]["value"] for g in d.get("genes", [])
                  if "geneName" in g] or [None])[0],
        "length": d["sequence"]["length"],
        "locations": locs,
        "has_signal_peptide": feats.get("Signal", 0) > 0,
        "n_transmembrane": feats.get("Transmembrane", 0),
    }


def intact_census(rows: list[dict]) -> dict:
    d = _get_json(f"{INTACT}/{ACC}?page=0&pageSize=1000")
    content = d["content"]
    total = d.get("totalElements")
    if total is not None and len(content) != total:
        raise CheckFailure(
            f"IntAct truncated: {len(content)} of totalElements={total}")

    methods = Counter(c.get("detectionMethod") for c in content)
    pubs = Counter()
    for c in content:
        pmid = next((p.split()[0] for p in (c.get("publicationIdentifiers") or [])
                     if p.endswith("(pubmed)")), "unknown")
        pubs[pmid] += 1

    # How many *publications* support each partner?  A partner seen in exactly
    # one publication is a singleton: no independent replication anywhere.
    partner_pubs: dict[str, set[str]] = defaultdict(set)
    for c in content:
        pmid = next((p.split()[0] for p in (c.get("publicationIdentifiers") or [])
                     if p.endswith("(pubmed)")), "unknown")
        for side in ("interactorA", "interactorB"):
            ident = (c.get(side) or {}).get("preferredIdentifier") if isinstance(
                c.get(side), dict) else None
            if ident and ident != ACC:
                partner_pubs[ident].add(pmid)
        # flat schema fallback used by the current IntAct WS
        for k in ("moleculeA", "moleculeB", "idA", "idB"):
            v = c.get(k)
            if isinstance(v, str) and v and v != ACC:
                partner_pubs[v].add(pmid)

    # Partners on the GO:0005515 rows, one per WITH/FROM token.
    partners = sorted({r["WITH/FROM"].replace("UniProtKB:", "")
                       for r in rows if r["GO TERM"] == "GO:0005515"})
    ipi_rows = [r for r in rows if r["GO EVIDENCE CODE"] == "IPI"]
    resolved, cytofacing, isoform_rows, unreviewed = [], [], [], []
    for p in partners:
        e = _uniprot_entry(p)
        e["with_from_token"] = p
        if "-" in p:
            isoform_rows.append(p)
        if not e["reviewed"]:
            unreviewed.append(p)
        secreted = (e["has_signal_peptide"]
                    or any("Secreted" in l or "extracellular" in l.lower()
                           or "Golgi" in l or "Endoplasmic reticulum lumen" in l
                           or "Lysosome" in l
                           for l in e["locations"]))
        membrane = e["n_transmembrane"] > 0
        only_cyto = (not secreted and not membrane
                     and any(any(c in l for c in CYTOFACING)
                             for l in e["locations"]))
        e["reaches_secretory_or_extracellular"] = bool(secreted)
        e["cytofacing_only"] = bool(only_cyto)
        if only_cyto:
            cytofacing.append(p)
        resolved.append(e)

    y2h = sum(v for m, v in methods.items() if m and "hybrid" in m)
    return {
        "intact_total_interactions": len(content),
        "detection_methods": dict(methods.most_common()),
        "two_hybrid_submethods": sorted(
            m for m in methods if m and "hybrid" in m),
        "n_two_hybrid_interactions": y2h,
        "interactions_per_publication": dict(pubs.most_common()),
        "distinct_publications": len(pubs),
        "largest_single_publication": pubs.most_common(1)[0] if pubs else None,
        "n_goa_ipi_rows": len(ipi_rows),
        "goa_ipi_references": sorted({r["REFERENCE"] for r in ipi_rows}),
        "partner_publication_counts": {
            k: sorted(v) for k, v in sorted(partner_pubs.items())},
        "n_partners_seen_in_one_publication_only": sum(
            1 for v in partner_pubs.values() if len(v) == 1),
        "goa_ipi_partners": len(partners),
        "partners_resolved": len(resolved),
        "partners_unreviewed": unreviewed,
        "partners_cited_as_isoform": isoform_rows,
        "partners_cytofacing_only": cytofacing,
        "n_cytofacing_only": len(cytofacing),
        "partner_detail": resolved,
    }


# --------------------------------------------------------------------------
# D. IBA donors
# --------------------------------------------------------------------------

_XREF_DB = {"MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "FB": "flybase"}


def _mod_to_uniprot(token: str) -> list[dict]:
    """Resolve a MOD id (MGI:MGI:106675, RGD:2229, ...) to UniProt entries.

    MGI tokens arrive as ``MGI:MGI:106675``; UniProt's ``xref:mgi-`` index
    wants the bare number -- a query containing the inner colon returns HTTP
    400.  Always fetch size>1 and report every candidate: an ambiguous
    cross-reference is data, not a missing input.
    """
    db, _, rest = token.partition(":")
    idx = _XREF_DB.get(db)
    if not idx:
        return []
    bare = rest.split(":")[-1]
    url = (f"{UNIPROT}/search?query=xref:{idx}-{bare}"
           f"&fields=id,accession,gene_names,organism_name&size=10&format=json")
    try:
        d = _get_json(url)
    except CheckFailure:
        return []
    return [{"accession": r["primaryAccession"],
             "entry_name": r["uniProtkbId"],
             "reviewed": r["entryType"].startswith("UniProtKB reviewed"),
             "gene": ([g["geneName"]["value"] for g in r.get("genes", [])
                       if "geneName" in g] or [None])[0]}
            for r in d.get("results", [])]


def _donor_evidence(gp_id: str, go_id: str) -> list[str] | None:
    """What evidence does this donor carry for this term (or descendants)?

    QuickGO's ``geneProductId`` rejects MOD ids (MGI:, RGD:, FB:, WB:) with
    HTTP 400.  Return None so a rejected query is distinguishable from a
    genuine empty result.
    """
    if not gp_id.startswith("UniProtKB:"):
        return None
    params = {"geneProductId": gp_id, "goId": go_id,
              "goUsage": "descendants",
              "goUsageRelationships": "is_a,part_of", "limit": PAGE, "page": 1}
    try:
        d = _get_json(QUICKGO_ANN + "?" + urllib.parse.urlencode(params))
    except CheckFailure:
        return None
    if d["numberOfHits"] != len(d["results"]):
        raise CheckFailure(
            f"donor query truncated for {gp_id}/{go_id}: "
            f"{len(d['results'])} of {d['numberOfHits']}")
    return sorted({a["goEvidence"] for a in d["results"]})


# Ontology relations the review's prose asserts.  Regulation is NOT subsumption
# in GO, and the activity branch is NOT under the binding branch -- both traps
# were live in this review's first draft, which claimed GO:0048018 receptor
# ligand activity was a descendant of GO:0005102 signaling receptor binding.
# It is not.  Each entry is (child, ancestor, expected_membership).
ASSERTED_RELATIONS = [
    ("GO:0005179", "GO:0048018", True),   # hormone activity IS a receptor ligand activity
    ("GO:0005179", "GO:0140677", True),   # ... under molecular function activator activity
    ("GO:0005179", "GO:0005102", False),  # ... but NOT under signaling receptor binding
    ("GO:0048018", "GO:0005102", False),  # the correction that prompted this check
    ("GO:0005125", "GO:0048018", True),   # cytokine activity is a sibling of hormone activity
    ("GO:0042803", "GO:0042802", True),   # homodimerization IS an identical protein binding
    ("GO:0006635", "GO:0019395", True),   # beta-oxidation IS a fatty acid oxidation
    ("GO:0046321", "GO:0019395", False),  # regulation is not subsumption
    ("GO:0090336", "GO:0050873", False),  # regulation is not subsumption
    ("GO:0010906", "GO:0006006", False),  # regulation is not subsumption
]


def term_relations() -> dict:
    """Fetch, record and assert the is_a/part_of relations the review claims.

    Evidence must be born in the repository: a relation checked only in
    conversation is not checkable by a reader of the tree, and a reviewer in a
    sandbox with no network cannot re-run the query.  The fetched ancestor sets
    go into results.json.
    """
    out = {"asserted": [], "ancestors": {}}
    for child, ancestor, expected in ASSERTED_RELATIONS:
        if child not in out["ancestors"]:
            u = (f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
                 f"{child}/ancestors?relations=is_a,part_of")
            d = _get_json(u)
            res = d.get("results") or []
            if not res:
                raise CheckFailure(f"no ancestor record for {child}")
            out["ancestors"][child] = sorted(res[0].get("ancestors") or [])
        observed = ancestor in out["ancestors"][child]
        out["asserted"].append({
            "child": child, "ancestor": ancestor,
            "expected_is_ancestor": expected,
            "observed_is_ancestor": observed,
            "agrees": observed == expected,
        })
    return out


def receptor_coverage(rows: list[dict]) -> dict:
    """Do GO/GOA record adiponectin's three characterised receptors?

    AdipoR1 (Q96A54) and AdipoR2 (Q86V24) were cloned in PMID:12802337;
    T-cadherin/CDH13 (P55290) was identified as the receptor for hexameric and
    HMW adiponectin in PMID:15210937 and reconfirmed in PMID:26166748.  A gap
    on the receptor side is a coverage finding, so it is measured rather than
    asserted -- and it is checked from BOTH directions, because a partner can
    be recorded on the receptor's record without appearing on ADIPOQ's.
    """
    ours = {r["WITH/FROM"].replace("UniProtKB:", "")
            for r in rows if r["GO TERM"] == "GO:0005515"}
    out = {}
    for acc, sym in [("Q96A54", "ADIPOR1"), ("Q86V24", "ADIPOR2"),
                     ("P55290", "CDH13")]:
        results, total, complete = _quickgo_all(
            {"geneProductId": f"UniProtKB:{acc}"}, cap_annotations=3000)
        if not complete:
            out[sym] = {"note": "too large to paginate"}
            continue
        back = [{"goId": a["goId"], "evidence": a["goEvidence"],
                 "reference": a["reference"]}
                for a in results
                if any(x["id"] == ACC
                       for w in (a.get("withFrom") or [])
                       for x in w["connectedXrefs"])]
        e = _uniprot_entry(acc)
        out[sym] = {
            "accession": acc,
            "entry_name": e["entry_name"],
            "reviewed": e["reviewed"],
            "on_adipoq_goa": acc in ours,
            "total_annotations": total,
            "annotations_naming_adipoq_in_withfrom": back,
        }
    return out


def node_reach(rows: list[dict]) -> dict:
    """Which human genes does each PANTHER node reach for each IBA term?

    The brief's reciprocal question: *which node's reach is exactly my gene
    set, and what did it give them?*  A term whose evidence is family-wide but
    which sits on an ortholog node is misplaced downward, and vice versa.
    """
    out = {}
    for r in rows:
        if r["GO EVIDENCE CODE"] != "IBA":
            continue
        nodes = [t.split(":", 1)[1] for t in r["WITH/FROM"].split("|")
                 if t.startswith("PANTHER:")]
        results, total, complete = _quickgo_all(
            {"evidenceCode": "ECO:0000318", "goId": r["GO TERM"],
             "taxonId": "9606"}, cap_annotations=6000)
        if not complete:
            out[r["GO TERM"]] = {"human_iba_rows": total,
                                 "note": "too large to paginate; reach unknown"}
            continue
        reach = defaultdict(list)
        for a in results:
            ids = {x["id"] for w in (a.get("withFrom") or [])
                   for x in w["connectedXrefs"]}
            for n in nodes:
                if n in ids:
                    reach[n].append(a.get("symbol") or a["geneProductId"])
        out[r["GO TERM"]] = {
            "term_name": r["GO NAME"],
            "nodes": nodes,
            "human_iba_rows_for_term": total,
            "human_genes_reached_by_node": {
                n: sorted(set(v)) for n, v in reach.items()},
        }
    return out


def iba_donors(rows: list[dict]) -> dict:
    out = {}
    for r in rows:
        if r["GO EVIDENCE CODE"] != "IBA":
            continue
        tokens = [t for t in r["WITH/FROM"].split("|") if t]
        nodes = [t for t in tokens if t.startswith("PANTHER:")]
        entities = [t for t in tokens if not t.startswith("PANTHER:")]
        detail = []
        for t in entities:
            ev = _donor_evidence(t, r["GO TERM"])
            resolved_via = "direct UniProtKB id" if ev is not None else None
            candidates = []
            if ev is None:
                # QuickGO rejects MOD ids: resolve through UniProt's xref index
                # and report the fallback rather than dropping the token.
                candidates = _mod_to_uniprot(t)
                sw = [c for c in candidates if c["reviewed"]] or candidates
                if sw:
                    ev = _donor_evidence("UniProtKB:" + sw[0]["accession"],
                                         r["GO TERM"])
                    resolved_via = (f"UniProt xref fallback -> "
                                    f"{sw[0]['accession']} ({sw[0]['entry_name']})")
            detail.append({
                "source_id": t,
                "self_reference": t == f"UniProtKB:{ACC}",
                "resolved_via": resolved_via,
                "xref_candidates": candidates,
                "evidence_for_term": ev,
                "queryable": ev is not None,
                "has_own_experimental": (
                    bool(set(ev or []) & EXPERIMENTAL) if ev is not None else None),
            })
        out[r["GO TERM"]] = {
            "term_name": r["GO NAME"],
            "panther_nodes": nodes,
            "n_tokens": len(tokens),
            "self_referential": any(d["self_reference"] for d in detail),
            "donors": detail,
        }
    return out


# --------------------------------------------------------------------------
# E. Thermogenesis citation cross-product
# --------------------------------------------------------------------------

def thermogenesis_cross_product(rows: list[dict]) -> dict:
    """GO:0120162 / GO:0120163 are logical opposites.

    If the same reference set supports both, at least one pairing is wrong,
    whatever the papers say.  Detected from the TSV alone -- no text reading.
    """
    pos, neg = "GO:0120162", "GO:0120163"
    refs = defaultdict(set)
    for r in rows:
        if r["GO TERM"] in (pos, neg) and r["REFERENCE"].startswith("PMID:"):
            refs[r["GO TERM"]].add(r["REFERENCE"])
    shared = refs[pos] & refs[neg]
    return {
        "positive_term": pos,
        "negative_term": neg,
        "positive_refs": sorted(refs[pos]),
        "negative_refs": sorted(refs[neg]),
        "shared_references": sorted(shared),
        "is_full_cross_product": bool(shared) and refs[pos] == refs[neg],
        "n_misattributable_rows": len(shared),
    }


# --------------------------------------------------------------------------
# guards / self-test
# --------------------------------------------------------------------------

def guards(res: dict) -> list[str]:
    """Invariants that must hold.  Append to problems; never raise."""
    problems: list[str] = []

    rec = res.get("goa_reconciliation")
    if not rec:
        problems.append("guard: goa_reconciliation missing -- vacuous pass")
    else:
        if rec["goa_rows_distinct"] <= 0:
            problems.append("guard: zero distinct GOA rows")
        if rec["review_yaml_entries"] is not None and not rec["reconciles"]:
            problems.append(
                f"guard: review YAML has {rec['review_yaml_from_goa']} "
                f"GOA-derived entries ({rec['review_yaml_entries']} total, "
                f"{rec['review_yaml_new_rows']} NEW) but GOA has "
                f"{rec['goa_rows_distinct']} distinct rows")

    ic = res.get("intact_census")
    if not ic:
        problems.append("guard: intact_census missing -- vacuous pass")
    else:
        if ic["partners_resolved"] != ic["goa_ipi_partners"]:
            problems.append(
                f"guard: resolved {ic['partners_resolved']} of "
                f"{ic['goa_ipi_partners']} GO:0005515 partners")
        # 'reviewed' substring bug detector: a 100% reviewed set is suspicious
        # only if we never observed the unreviewed branch anywhere.  Assert the
        # test itself discriminates.
        if not any(not p["reviewed"] for p in ic["partner_detail"]):
            det = [p for p in ic["partner_detail"]
                   if not p["entry_type"].startswith("UniProtKB reviewed")]
            if det:
                problems.append(
                    "guard: reviewed-status test disagrees with entry_type "
                    "-- likely the 'reviewed' in 'unreviewed' substring bug")

    ib = res.get("iba_donors")
    if ib is None:
        problems.append("guard: iba_donors missing -- vacuous pass")
    elif not ib:
        problems.append("guard: iba_donors empty; ADIPOQ has IBA rows in GOA "
                        "-- an empty result here is a defect, not a finding")
    else:
        for term, d in ib.items():
            if not d["donors"]:
                problems.append(f"guard: {term} IBA has no donor tokens")
            # Assert presence, do not just validate on match.
            if not any(x["source_id"].startswith("PANTHER:")
                       for x in [{"source_id": n} for n in d["panther_nodes"]]):
                problems.append(f"guard: {term} IBA names no PANTHER node")

    tc = res.get("thermogenesis_cross_product")
    if not tc:
        problems.append("guard: thermogenesis_cross_product missing")
    elif tc["shared_references"] and not tc["is_full_cross_product"]:
        # partial overlap is still a defect, just a differently-shaped one
        pass

    tr = res.get("term_relations")
    if tr is None:
        problems.append("guard: term_relations missing -- vacuous pass")
    elif not tr.get("asserted"):
        problems.append("guard: term_relations asserted[] is empty; the check "
                        "exists to police prose claims, so an empty list is a "
                        "defect not a pass")
    else:
        for a in tr["asserted"]:
            if not a["agrees"]:
                problems.append(
                    f"guard: prose asserts {a['child']} "
                    f"{'IS' if a['expected_is_ancestor'] else 'is NOT'} under "
                    f"{a['ancestor']}, but GO says the opposite")

    rc = res.get("receptor_coverage")
    if rc is None:
        problems.append("guard: receptor_coverage missing -- vacuous pass")
    elif set(rc) != {"ADIPOR1", "ADIPOR2", "CDH13"}:
        problems.append(f"guard: receptor_coverage resolved {sorted(rc)}, "
                        "expected ADIPOR1, ADIPOR2, CDH13")

    rp = res.get("reference_projection")
    if not rp:
        problems.append("guard: reference_projection missing -- vacuous pass")

    return problems


def self_test() -> int:
    """Break-test each guard in the direction it exists to catch."""
    failures = []

    def expect(name, res, needle):
        got = guards(res)
        if not any(needle in g for g in got):
            failures.append(f"{name}: expected a problem containing "
                            f"{needle!r}, got {got}")

    # 1. happy path must be clean (a check can be wrong about success too)
    happy = {
        "goa_reconciliation": {"goa_rows_distinct": 5, "review_yaml_entries": 6,
                               "review_yaml_new_rows": 1,
                               "review_yaml_from_goa": 5, "reconciles": True},
        "intact_census": {"partners_resolved": 2, "goa_ipi_partners": 2,
                          "partner_detail": [
                              {"reviewed": True,
                               "entry_type": "UniProtKB reviewed (Swiss-Prot)"},
                              {"reviewed": False,
                               "entry_type": "UniProtKB unreviewed (TrEMBL)"}]},
        "iba_donors": {"GO:1": {"donors": [{"source_id": "UniProtKB:X"}],
                                "panther_nodes": ["PANTHER:PTN1"]}},
        "thermogenesis_cross_product": {"shared_references": [],
                                        "is_full_cross_product": False},
        "reference_projection": {"PMID:1": {}},
        "receptor_coverage": {"ADIPOR1": {}, "ADIPOR2": {}, "CDH13": {}},
        "term_relations": {"asserted": [{"child": "GO:1", "ancestor": "GO:2",
                                         "expected_is_ancestor": True,
                                         "observed_is_ancestor": True,
                                         "agrees": True}]},
    }
    if guards(happy):
        failures.append(f"happy path should be clean, got {guards(happy)}")

    # 2. missing section must fail loudly, not pass vacuously
    for section, needle in [("goa_reconciliation", "goa_reconciliation missing"),
                            ("receptor_coverage", "receptor_coverage missing"),
                            ("term_relations", "term_relations missing"),
                            ("intact_census", "intact_census missing"),
                            ("iba_donors", "iba_donors missing"),
                            ("reference_projection",
                             "reference_projection missing")]:
        broken = {k: v for k, v in happy.items() if k != section}
        expect(f"missing-{section}", broken, needle)

    # 3. empty iba_donors on a gene that has IBA rows
    b = dict(happy, iba_donors={})
    expect("empty-iba", b, "iba_donors empty")

    # 4. review/GOA mismatch
    b = dict(happy, goa_reconciliation={"goa_rows_distinct": 5,
                                        "review_yaml_entries": 4,
                                        "review_yaml_new_rows": 0,
                                        "review_yaml_from_goa": 4,
                                        "reconciles": False})
    expect("row-mismatch", b, "but GOA has 5 distinct rows")

    # 5. partner resolution shortfall
    b = dict(happy, intact_census=dict(happy["intact_census"],
                                       partners_resolved=1))
    expect("partner-shortfall", b, "resolved 1 of 2")

    # 6. the 'reviewed' substring bug: every partner marked reviewed while an
    #    entry_type says unreviewed
    b = dict(happy, intact_census={
        "partners_resolved": 1, "goa_ipi_partners": 1,
        "partner_detail": [{"reviewed": True,
                            "entry_type": "UniProtKB unreviewed (TrEMBL)"}]})
    expect("substring-bug", b, "substring bug")

    # 7. IBA row with no PANTHER node
    b = dict(happy, iba_donors={"GO:1": {"donors": [{"source_id": "UniProtKB:X"}],
                                         "panther_nodes": []}})
    expect("no-panther", b, "names no PANTHER node")

    # 8c. a prose claim contradicted by the ontology
    b = dict(happy, term_relations={"asserted": [
        {"child": "GO:0048018", "ancestor": "GO:0005102",
         "expected_is_ancestor": True, "observed_is_ancestor": False,
         "agrees": False}]})
    expect("relation-contradicted", b, "but GO says the opposite")

    # 8d. empty relation list must not pass vacuously
    b = dict(happy, term_relations={"asserted": []})
    expect("relation-empty", b, "asserted[] is empty")

    # 8b. receptor_coverage missing one receptor
    b = dict(happy, receptor_coverage={"ADIPOR1": {}, "CDH13": {}})
    expect("partial-receptors", b, "expected ADIPOR1, ADIPOR2, CDH13")

    # 8. the cross-product detector must actually fire on the shipped data
    rows, _ = read_goa()
    tc = thermogenesis_cross_product(rows)
    if not tc["shared_references"]:
        failures.append("cross-product detector does not fire on the committed "
                        "GOA TSV, which is the defect it was written for")

    # 9. and must NOT fire when the references are correctly split
    fake = [
        {"GO TERM": "GO:0120162", "REFERENCE": "PMID:26166748"},
        {"GO TERM": "GO:0120163", "REFERENCE": "PMID:24531262"},
    ]
    if thermogenesis_cross_product(fake)["shared_references"]:
        failures.append("cross-product detector fires on a correctly-split "
                        "citation set (false positive)")

    for f in failures:
        print("SELF-TEST FAIL:", f)
    print(f"self-test: {14 - len(failures)}/14 direction(s) OK"
          if not failures else f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--offline", action="store_true",
                    help="run only the checks that need no network")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    rows, _ = read_goa()
    res: dict = {
        "accession": ACC,
        "goa_reconciliation": goa_reconciliation(rows),
        "thermogenesis_cross_product": thermogenesis_cross_product(rows),
    }
    if not args.offline:
        res["reference_projection"] = reference_projection(rows)
        res["intact_census"] = intact_census(rows)
        res["iba_donors"] = iba_donors(rows)
        res["node_reach"] = node_reach(rows)
        res["receptor_coverage"] = receptor_coverage(rows)
        res["term_relations"] = term_relations()

    problems = guards(res)
    res["guard_problems"] = problems

    RESULTS_JSON.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ("intact_census", "reference_projection")},
                     indent=2)[:4000])
    if problems:
        print("\nGUARD PROBLEMS:")
        for p in problems:
            print("  -", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
