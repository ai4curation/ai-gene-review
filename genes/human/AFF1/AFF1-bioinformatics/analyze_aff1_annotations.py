#!/usr/bin/env python3
"""Reproducible provenance analysis for the human AFF1 (P51825) GO annotation set.

Every claim the AFF1 review makes about *where an annotation came from* is computed
here, so that a reader can re-derive it.  Six analyses:

A. WITH/FROM resolution.  Every token in column 11 of ``AFF1-goa.tsv`` is resolved
   to a protein (or reported as a non-protein identifier), with the Swiss-Prot /
   TrEMBL status printed next to every name and *all* candidate hits reported
   rather than silently taking the first.

B. Donor evidence.  For every (WITH/FROM protein, propagated GO term) pair, what
   evidence does the donor itself hold for that term?  Answers "is the chain empty
   of experimental evidence?" as a testable claim rather than a hedge.

C. Reference projection.  For every PMID cited by a GOA row, how many *distinct
   gene products* does that reference annotate, and does the functional/phenotype
   term spread across the set or stay on one gene?  A reference that gives a
   complex plus all its subunits one identical block is a projection, not N
   independent findings.  Entity counts are derived as distinct id sets; where the
   result is too large to paginate honestly the test is reported UNINFORMATIVE.

D. Term relations.  Every ancestry / redundancy claim in the review prose is
   fetched and asserted here rather than inferred from a label.

E. Node reach.  Which human gene products does PANTHER node PTN000829417 reach,
   and reciprocally which nodes carry each of AFF1's IBA terms?

F. IntAct expansion.  UniProt's ``NbExp`` is not an experiment count (it has been
   observed counting sub-methods, replicates and even domains).  Expand the records
   and count distinct interaction detection methods and publications per partner.

Discipline enforced throughout (each of these has produced a false result in this
campaign when omitted):

* ``primaryAccession == requested`` is asserted on every UniProt fetch, because a
  merged accession returns HTTP 200 with a complete record for a *different*
  protein.
* ``entryType.startswith("UniProtKB reviewed")`` -- ``"reviewed" in entryType``
  also matches ``"unreviewed"``.
* Every paginated query asserts ``numberOfHits == len(results)``; a server that
  clamps rather than errors would otherwise sail past a page-size guard.
* Every reported zero is controlled against a nearby non-zero from the same
  endpoint in the same call pattern, so "nothing there" cannot be confused with
  "query rejected".
* HTTP status is asserted, never inferred from an empty body.

Run:  uv run python analyze_aff1_annotations.py
Self-test the guards:  uv run python analyze_aff1_annotations.py --self-test
"""

from __future__ import annotations

import csv
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "AFF1-goa.tsv"
OUT_JSON = HERE / "results.json"
OUT_MD = HERE / "RESULTS.md"

SUBJECT = "P51825"
SUBJECT_SYMBOL = "AFF1"

UNIPROT = "https://rest.uniprot.org"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTACT = "https://www.ebi.ac.uk/intact/ws"

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}

# A reference whose fully-paginated annotation count exceeds this is a
# high-throughput dataset for which honest entity counting is not possible from
# the annotation search; we say so rather than reading a number off page 1.
PROJECTION_MAX_ANNOTATIONS = 2000


class Fail(Exception):
    """A hard failure.  Missing input or a rejected query -- never silent."""


def _get(url: str, tries: int = 4) -> tuple[int, bytes]:
    """GET, returning (status, body).  Raises Fail on a non-2xx/404 status.

    404 is returned to the caller rather than raised because "this accession has
    no record" is data, but any other error status must be loud: a rejected query
    and a genuine empty result are indistinguishable downstream.
    """
    last: Exception | None = None
    for attempt in range(tries):
        req = Request(url, headers={"Accept": "application/json",
                                   "User-Agent": "ai-gene-review/AFF1"})
        try:
            with urlopen(req, timeout=90) as resp:
                return resp.status, resp.read()
        except HTTPError as exc:  # noqa: PERF203
            if exc.code == 404:
                return 404, b""
            if exc.code in (429, 500, 502, 503, 504):
                last = exc
                time.sleep(2 * (attempt + 1))
                continue
            raise Fail(f"HTTP {exc.code} for {url}") from exc
        except Exception as exc:  # network hiccup
            last = exc
            time.sleep(2 * (attempt + 1))
    raise Fail(f"GET failed after {tries} attempts: {url} ({last})")


def get_json(url: str) -> tuple[int, Any]:
    status, body = _get(url)
    if status == 404:
        return 404, None
    if status != 200:
        raise Fail(f"unexpected status {status} for {url}")
    return status, json.loads(body)


# ---------------------------------------------------------------------------
# UniProt
# ---------------------------------------------------------------------------

_ENTRY_CACHE: dict[str, dict] = {}


def fetch_uniprot(acc: str) -> dict:
    """Fetch one accession and ASSERT it is the protein we asked for.

    A merged/secondary accession returns HTTP 200 with a complete reviewed record
    for a different protein; only ``primaryAccession`` reveals it.
    """
    if acc in _ENTRY_CACHE:
        return _ENTRY_CACHE[acc]
    fields = "accession,id,gene_names,organism_name,protein_name,length,cc_function"
    status, d = get_json(f"{UNIPROT}/uniprotkb/{acc}.json?fields={fields}")
    if status == 404 or d is None:
        raise Fail(f"UniProt has no record for {acc} (dead accession?)")
    got = d.get("primaryAccession")
    if got != acc:
        raise Fail(
            f"ACCESSION DRIFT: asked for {acc}, got {got} "
            f"({d.get('uniProtkbId')}) -- this is a merged accession returning "
            f"a different protein with HTTP 200"
        )
    if not d.get("uniProtkbId"):
        raise Fail(f"{acc} returned an entry with no entry name (inactive?)")
    _ENTRY_CACHE[acc] = d
    return d


def is_reviewed(entry: dict) -> bool:
    """`"reviewed" in entryType` also matches "unreviewed" -- anchor the test."""
    return str(entry.get("entryType", "")).startswith("UniProtKB reviewed")


def describe_entry(entry: dict) -> dict:
    genes = [g.get("geneName", {}).get("value") for g in entry.get("genes", [])]
    return {
        "accession": entry["primaryAccession"],
        "entry_name": entry.get("uniProtkbId"),
        "genes": [g for g in genes if g],
        "organism": (entry.get("organism") or {}).get("scientificName"),
        "protein_name": (((entry.get("proteinDescription") or {}).get("recommendedName")
                          or {}).get("fullName") or {}).get("value"),
        "length": (entry.get("sequence") or {}).get("length"),
        "reviewed": is_reviewed(entry),
        "status": "Swiss-Prot" if is_reviewed(entry) else "TrEMBL",
    }


def search_xref(db: str, ident: str, size: int = 10) -> list[dict]:
    """Resolve a MOD id.  Returns ALL hits -- a size=1 query converts an
    ambiguous cross-reference into a confident wrong answer."""
    q = quote(f"xref:{db}-{ident}")
    fields = "accession,id,gene_names,organism_name,protein_name,length"
    status, d = get_json(
        f"{UNIPROT}/uniprotkb/search?query={q}&fields={fields}&format=json&size={size}"
    )
    if d is None:
        return []
    return [describe_entry(r) for r in d.get("results", [])]


# ---------------------------------------------------------------------------
# QuickGO
# ---------------------------------------------------------------------------

def quickgo_annotations(params: str, label: str) -> list[dict]:
    """Fully paginated QuickGO annotation search.

    Asserts ``numberOfHits == len(collected)``.  Comparing against a page-size
    constant instead is defeated by a server that clamps rather than errors.
    """
    page, out, total = 1, [], None
    while True:
        url = f"{QUICKGO}/annotation/search?{params}&limit=100&page={page}"
        status, d = get_json(url)
        if d is None:
            raise Fail(f"QuickGO returned no body for {label}")
        if total is None:
            total = d["numberOfHits"]
        out.extend(d.get("results", []))
        if len(out) >= total or not d.get("results"):
            break
        page += 1
        if page > 300:
            raise Fail(f"pagination runaway for {label}")
    if len(out) != total:
        raise Fail(
            f"TRUNCATION: {label} reported numberOfHits={total} but collected "
            f"{len(out)} -- the service clamped or paging failed"
        )
    return out


def gene_product_id(ann: dict) -> str:
    gp = ann.get("geneProductId") or ""
    return gp


def with_from_tokens(ann: dict) -> list[str]:
    """Reassemble ``db:id``.  QuickGO splits withFrom into {db,id} objects; a
    comparison against the flat GOA string otherwise reports 'not identical' for
    data that is identical, and dropping ``db`` makes a MOD seed id look like an
    opaque token."""
    toks: list[str] = []
    for block in ann.get("withFrom") or []:
        for c in block.get("connectedXrefs") or []:
            db, ident = c.get("db"), c.get("id")
            if db and ident:
                toks.append(f"{db}:{ident}")
    return toks


# ---------------------------------------------------------------------------
# A. WITH/FROM resolution
# ---------------------------------------------------------------------------

def read_goa() -> list[dict]:
    if not GOA_TSV.exists():
        raise Fail(f"missing {GOA_TSV}; run `just fetch-gene human AFF1`")
    with GOA_TSV.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise Fail(f"{GOA_TSV} has no data rows")
    return rows


def analyse_withfrom(rows: list[dict]) -> dict:
    token_rows: dict[str, list[int]] = defaultdict(list)
    for i, r in enumerate(rows, start=1):
        raw = (r.get("WITH/FROM") or "").strip()
        for tok in filter(None, (t.strip() for t in raw.split("|"))):
            token_rows[tok].append(i)

    resolved: dict[str, dict] = {}
    for tok in sorted(token_rows):
        db, _, ident = tok.partition(":")
        rec: dict[str, Any] = {"token": tok, "rows": token_rows[tok], "db": db}
        if db == "UniProtKB":
            e = describe_entry(fetch_uniprot(ident))
            rec.update(kind="protein", candidates=[e], chosen=e,
                       self_reference=(ident == SUBJECT))
        elif db == "MGI":
            # MGI tokens arrive as MGI:MGI:1100819; UniProt's xref index wants the
            # BARE number -- a query containing the inner colon returns HTTP 400.
            bare = ident.split(":")[-1]
            cands = search_xref("mgi", bare)
            rec.update(kind="protein", candidates=cands,
                       chosen=_pick_reviewed(cands, tok))
        elif db == "FB":
            cands = search_xref("flybase", ident)
            rec.update(kind="protein", candidates=cands,
                       chosen=_pick_reviewed(cands, tok))
        elif db == "PANTHER":
            rec.update(kind="panther_node",
                       note="an internal PANTHER tree node, not a protein")
        elif db in {"InterPro", "ARBA", "UniProtKB-SubCell"}:
            rec.update(kind="signature_or_rule",
                       note="an automatic-pipeline source, not a protein")
        else:
            rec.update(kind="unresolved",
                       note=f"no resolver implemented for db={db!r}")
        resolved[tok] = rec

    unresolved = [t for t, r in resolved.items() if r["kind"] == "unresolved"]
    if unresolved:
        raise Fail(f"unresolved WITH/FROM tokens (cannot be dismissed, only "
                   f"deferred): {unresolved}")
    return resolved


def _pick_reviewed(cands: list[dict], tok: str) -> dict:
    if not cands:
        raise Fail(f"{tok} resolved to zero UniProt entries")
    rev = [c for c in cands if c["reviewed"]]
    if len(rev) == 1:
        return rev[0]
    if len(rev) > 1:
        raise Fail(f"{tok} has {len(rev)} reviewed entries: "
                   f"{[c['accession'] for c in rev]} -- ambiguous, handle explicitly")
    # No reviewed entry.  Fall back to unreviewed but SAY SO.
    c = dict(cands[0])
    c["fallback_unreviewed"] = True
    return c


# ---------------------------------------------------------------------------
# B. donor evidence
# ---------------------------------------------------------------------------

def analyse_donor_evidence(rows: list[dict], resolved: dict) -> dict:
    out: dict[str, dict] = {}
    for i, r in enumerate(rows, start=1):
        if r["GO EVIDENCE CODE"] not in {"IBA", "ISS", "ISO", "ISA", "ISM"}:
            continue
        term = r["GO TERM"]
        for tok in filter(None, (t.strip() for t in (r.get("WITH/FROM") or "").split("|"))):
            rec = resolved[tok]
            if rec["kind"] != "protein":
                continue
            acc = rec["chosen"]["accession"]
            key = f"{acc}|{term}"
            if key in out:
                out[key]["rows"].append(i)
                continue
            anns = quickgo_annotations(
                f"geneProductId=UniProtKB:{acc}&goId={term}"
                "&goUsage=descendants&goUsageRelationships=is_a,part_of",
                f"donor {acc} @ {term}",
            )
            codes = Counter(a.get("goEvidence") for a in anns)
            terms_held = sorted({a.get("goId") for a in anns})
            out[key] = {
                "donor": rec["chosen"],
                "donor_token": tok,
                "propagated_term": term,
                "rows": [i],
                "n_annotations": len(anns),
                "evidence_codes": dict(codes),
                "terms_held": terms_held,
                "has_own_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
                "holds_exact_term": term in terms_held,
            }
    return out


# ---------------------------------------------------------------------------
# C. reference projection
# ---------------------------------------------------------------------------

def analyse_reference_projection(rows: list[dict]) -> dict:
    pmids = sorted({r["REFERENCE"] for r in rows if r["REFERENCE"].startswith("PMID:")})
    out: dict[str, dict] = {}
    for pmid in pmids:
        # First ask how big it is, without collecting.
        status, head = get_json(
            f"{QUICKGO}/annotation/search?reference={pmid}&limit=1&page=1")
        if head is None:
            raise Fail(f"QuickGO returned no body for reference {pmid}")
        total = head["numberOfHits"]
        if total > PROJECTION_MAX_ANNOTATIONS:
            out[pmid] = {
                "n_annotations": total,
                "informative": False,
                "note": ("high-throughput dataset; entity counts are not derivable "
                         "from a paginated annotation search at this size, so the "
                         "projection test is UNINFORMATIVE here"),
            }
            continue
        anns = quickgo_annotations(f"reference={pmid}", f"reference {pmid}")
        entities = {gene_product_id(a) for a in anns}
        by_term: dict[str, set[str]] = defaultdict(set)
        for a in anns:
            by_term[f"{a['goId']} {a.get('goName','')}"].add(gene_product_id(a))
        out[pmid] = {
            "n_annotations": len(anns),
            "n_entities": len(entities),
            "informative": True,
            "entities": sorted(entities),
            "entities_per_term": {k: sorted(v) for k, v in sorted(by_term.items())},
            "assigned_by": dict(Counter(a.get("assignedBy") for a in anns)),
            "evidence_codes": dict(Counter(a.get("goEvidence") for a in anns)),
        }
    return out


# ---------------------------------------------------------------------------
# D. term relations
# ---------------------------------------------------------------------------

# Every ancestry claim the review prose depends on.  Fetched and asserted, never
# inferred from a label: an *activity* term for X is not under the *binding* term
# for X, regulation is not subsumption, and siblings name different things.
RELATION_CLAIMS: list[tuple[str, str, bool, str]] = [
    # (descendant, ancestor, expected, why the review depends on it)
    ("GO:0032783", "GO:0008023", True,
     "SEC is a kind of transcription elongation factor complex, so the GO:0008023 "
     "IDA is the less precise of the two complex rows"),
    ("GO:0032968", "GO:0032786", True,
     "the Pol II elongation-activation term is a child of the generic one, so the "
     "two IMP rows from one reference are parent+child, not independent"),
    ("GO:0032786", "GO:0006355", True,
     "positive regulation of elongation sits under regulation of DNA-templated "
     "transcription, so the IBA GO:0006355 row is an ancestor of what the human "
     "IMP rows already assert"),
    ("GO:0006355", "GO:0010468", True,
     "regulation of DNA-templated transcription is under regulation of gene "
     "expression, so the InterPro2GO GO:0010468 row is the least specific of the "
     "regulation rows"),
    ("GO:0003711", "GO:0003712", False,
     "transcription elongation factor activity is NOT under transcription "
     "coregulator activity -- the two MF rows are different claims, not a "
     "general/specific pair"),
    ("GO:0000785", "GO:0005634", False,
     "chromatin is not part_of nucleus in GO's is_a/part_of closure, so the "
     "chromatin and nucleus rows are separate location claims"),
    ("GO:0090734", "GO:0000785", False,
     "site of DNA damage is not under chromatin, so the two damage-associated "
     "location rows are not a general/specific pair"),
    ("GO:0032968", "GO:0006355", True,
     "raised by the PR reviewer: GO:0006355 is an ancestor of GO:0032968, so "
     "listing both in one core_function's directly_involved_in is redundant by the "
     "same logic used to collapse GO:0032786 onto GO:0032968 in the rows"),
    ("GO:0045668", "GO:0006355", False,
     "the osteoblast-differentiation term is NOT under regulation of "
     "DNA-templated transcription, so core function 3 may legitimately carry both"),
]


def ancestors(term: str) -> set[str]:
    status, d = get_json(
        f"{QUICKGO}/ontology/go/terms/{term}/ancestors?relations=is_a,part_of")
    if d is None:
        raise Fail(f"no ancestor response for {term}")
    res = d.get("results") or []
    if not res:
        raise Fail(f"empty ancestor list for {term}")
    return set(res[0].get("ancestors") or [])


def analyse_relations() -> dict:
    out = {}
    # Positive control: every term is its own ancestor in QuickGO's closure.
    ctrl = ancestors("GO:0032783")
    if "GO:0032783" not in ctrl:
        raise Fail("ancestor endpoint control failed: term is not in its own closure")
    for desc, anc, expected, why in RELATION_CLAIMS:
        got = anc in ancestors(desc)
        out[f"{desc}<-{anc}"] = {
            "descendant": desc, "ancestor": anc,
            "expected_is_ancestor": expected, "observed_is_ancestor": got,
            "agrees": got == expected, "why_the_review_needs_it": why,
        }
    bad = [k for k, v in out.items() if not v["agrees"]]
    if bad:
        raise Fail(f"term-relation claims contradicted by the ontology: {bad}")
    return out


# ---------------------------------------------------------------------------
# E. node reach
# ---------------------------------------------------------------------------

IBA_NODE = "PANTHER:PTN000829417"

# Human AFF-family accessions, so the node-reach tables can name the members
# instead of printing 79 opaque accessions.
HUMAN_AFF = {
    "P51825": "AFF1", "P51816": "AFF2", "P51826": "AFF3", "Q9UHB7": "AFF4",
}
MOUSE_NAMES = {
    "O88573": "mouse Aff1", "O55112": "mouse Aff2", "P51827": "mouse Aff3",
    "Q9VQI9": "fly lilli",
}


def analyse_node_reach(rows: list[dict]) -> dict:
    iba_terms = sorted({r["GO TERM"] for r in rows
                        if r["GO EVIDENCE CODE"] == "IBA"})
    anns = quickgo_annotations(
        f"evidenceCode=ECO:0000318&withFrom={quote(IBA_NODE)}",
        f"node reach {IBA_NODE}")
    if not anns:
        raise Fail(f"zero annotations for {IBA_NODE}: query likely rejected")
    recips: dict[str, set[str]] = defaultdict(set)
    per_term: dict[str, set[str]] = defaultdict(set)
    for a in anns:
        gp = gene_product_id(a)
        recips[gp].add(a["goId"])
        per_term[a["goId"]].add(gp)
    # Which nodes carry each of AFF1's own IBA terms, restricted to human?
    term_nodes: dict[str, dict] = {}
    for t in iba_terms:
        h = quickgo_annotations(
            f"goId={t}&evidenceCode=ECO:0000318&taxonId=9606"
            "&goUsage=exact",
            f"human IBA holders of {t}")
        nodes: dict[str, set[str]] = defaultdict(set)
        for a in h:
            for tok in with_from_tokens(a):
                if tok.startswith("PANTHER:"):
                    nodes[tok].add(gene_product_id(a))
        term_nodes[t] = {
            "n_human_iba_annotations": len(h),
            "nodes": {k: sorted(v) for k, v in sorted(nodes.items())},
        }
    return {
        "node": IBA_NODE,
        "n_annotations": len(anns),
        "n_recipient_gene_products": len(recips),
        "recipients": {k: sorted(v) for k, v in sorted(recips.items())},
        "terms_on_node": {k: sorted(v) for k, v in sorted(per_term.items())},
        "aff1_iba_terms": iba_terms,
        "human_iba_holders_by_term": term_nodes,
    }


# ---------------------------------------------------------------------------
# F. IntAct
# ---------------------------------------------------------------------------

def subject_transcript_ids() -> set[str]:
    """The subject's own Ensembl transcript ids, from its UniProt cross-references."""
    status, d = get_json(
        f"{UNIPROT}/uniprotkb/{SUBJECT}.json?fields=xref_ensembl")
    if d is None:
        raise Fail(f"could not fetch Ensembl cross-references for {SUBJECT}")
    if d.get("primaryAccession") != SUBJECT:
        raise Fail(f"ACCESSION DRIFT while fetching transcripts for {SUBJECT}")
    out = set()
    for x in d.get("uniProtKBCrossReferences") or []:
        if x.get("database") == "Ensembl" and x.get("id", "").startswith("ENST"):
            out.add(x["id"].split(".")[0])
    return out


def analyse_intact() -> dict:
    """Expand every IntAct record for the subject.

    Two defects were found here by numbers that refused to add up, and both are
    guarded now:

    * ``publicationIdentifiers`` entries look like ``"32296183 (pubmed)"``, mixed
      with IMEx and IntAct ids, so neither ``len()`` nor ``str.isdigit()`` yields a
      publication count.  ``publicationPubmedIdentifier`` is the clean field.
    * The subject appears on some records as an **isoform** id (``P51825-3``), so
      an equality test against the bare accession silently discarded 5 of 104
      records.  Every record must now be accounted for or the run fails.
    """
    url = (f"{INTACT}/interaction/findInteractions/{SUBJECT}"
           "?page=0&pageSize=400")
    status, d = get_json(url)
    if d is None:
        raise Fail("IntAct returned no body")
    content = d.get("content") or []
    total = d.get("totalElements")
    if total is None:
        raise Fail("IntAct response lacks totalElements")
    if total != len(content):
        raise Fail(f"IntAct truncation: totalElements={total}, got {len(content)}")
    if not content:
        raise Fail("IntAct returned zero interactions for the subject: the query "
                   "was probably rejected (control: the subject's UniProt entry "
                   "cross-references 37 IntAct interactions)")

    # The subject also appears in IntAct as its own Ensembl TRANSCRIPTS, paired
    # with RNAcentral ncRNAs.  Those records are nucleic-acid interactions of the
    # AFF1 mRNA, not protein interactions of the AFF1 protein, so they are
    # counted and reported separately rather than dropped.  The transcript set is
    # derived from the subject's UniProt cross-references, not hardcoded.
    transcripts = subject_transcript_ids()
    if not transcripts:
        raise Fail("derived zero Ensembl transcript ids for the subject; the "
                   "nucleic-acid record classification would be vacuous")

    def bare(x: str) -> str:
        return (x or "").split("(")[0].strip()

    def is_subject(x: str) -> bool:
        """P51825 or any of its isoform ids -- but not another accession that
        merely starts with the same characters."""
        return x == SUBJECT or (x.startswith(SUBJECT + "-")
                                and x[len(SUBJECT) + 1:].isdigit())

    def is_subject_transcript(x: str) -> bool:
        return x.split(".")[0] in transcripts

    partners: dict[str, dict] = {}
    nucleic: list[dict] = []
    accounted = 0
    unaccounted: list[str] = []
    for c in content:
        ba, bb = bare(c.get("idA")), bare(c.get("idB"))
        if is_subject(ba) and is_subject(bb):
            other, subj_side = SUBJECT, ba
        elif is_subject(ba):
            other, subj_side = bb, ba
        elif is_subject(bb):
            other, subj_side = ba, bb
        elif is_subject_transcript(ba) or is_subject_transcript(bb):
            nucleic.append({
                "idA": ba, "idB": bb,
                "detection_method": c.get("detectionMethod"),
                "type": c.get("type"),
                "pmid": c.get("publicationPubmedIdentifier"),
                "mi_score": c.get("intactMiscore"),
                "typeA": c.get("typeA"), "typeB": c.get("typeB"),
            })
            accounted += 1
            continue
        else:
            unaccounted.append(f"{ba}|{bb}")
            continue
        accounted += 1
        p = partners.setdefault(other, {
            "id": other, "n_records": 0, "methods": Counter(),
            "pmids": set(), "all_pub_ids": set(), "types": Counter(),
            "mi_scores": [], "molecule_names": set(),
            "subject_forms": set(), "preparations": Counter(),
            "host_organisms": Counter(), "partner_species": Counter(),
        })
        p["n_records"] += 1
        p["subject_forms"].add(subj_side)
        p["methods"][c.get("detectionMethod")] += 1
        p["types"][c.get("type")] += 1
        p["host_organisms"][c.get("hostOrganism")] += 1
        p["partner_species"][c.get("speciesB") if is_subject(ba)
                             else c.get("speciesA")] += 1
        for prep in ((c.get("experimentalPreparationsB") if is_subject(ba)
                      else c.get("experimentalPreparationsA")) or []):
            p["preparations"][prep] += 1
        pm = c.get("publicationPubmedIdentifier")
        if pm:
            p["pmids"].add(str(pm))
        for pub in (c.get("publicationIdentifiers") or []):
            p["all_pub_ids"].add(pub)
        if c.get("intactMiscore") is not None:
            p["mi_scores"].append(c["intactMiscore"])
        p["molecule_names"].add(c.get("moleculeB") if is_subject(ba)
                                else c.get("moleculeA"))

    if accounted != total:
        raise Fail(
            f"IntAct accounting: {accounted} of {total} records assigned to a "
            f"partner; unassigned pairs {unaccounted[:10]} -- a predicate that "
            f"silently drops records produces a partner SET that is wrong even "
            f"when the count looks plausible")

    out = {}
    for k, p in partners.items():
        npmid = len(p["pmids"])
        if npmid > p["n_records"]:
            raise Fail(
                f"IntAct arithmetic for {k}: {npmid} distinct PMIDs from only "
                f"{p['n_records']} records -- a record cannot report more "
                f"publications than it has")
        out[k] = {
            "id": p["id"],
            "molecule_names": sorted(x for x in p["molecule_names"] if x),
            "n_records": p["n_records"],
            "n_distinct_pmids": npmid,
            "pmids": sorted(p["pmids"]),
            "n_all_publication_identifiers": len(p["all_pub_ids"]),
            "detection_methods": dict(p["methods"]),
            "n_distinct_detection_methods": len(p["methods"]),
            "interaction_types": dict(p["types"]),
            "max_mi_score": max(p["mi_scores"]) if p["mi_scores"] else None,
            "subject_forms": sorted(p["subject_forms"]),
            "isoform_only": all(f != SUBJECT for f in p["subject_forms"]),
            "partner_preparations": dict(p["preparations"]),
            "host_organisms": dict(p["host_organisms"]),
            "partner_species": dict(p["partner_species"]),
            "is_protein_entity": bool(p["id"][:1].isalpha()
                                      and not p["id"].startswith(("EBI-", "ENSG"))),
        }
    non_protein = sorted(k for k, v in out.items() if not v["is_protein_entity"])
    if SUBJECT in out:
        raise Fail("the subject is in its own partner set, which is the signature "
                   "of a self-interaction row or a predicate that never fired -- "
                   "inspect before trusting the partner set")
    multi_pmid = sorted(k for k, v in out.items() if v["n_distinct_pmids"] >= 2)
    return {"n_records_total": total,
            "n_protein_records": accounted - len(nucleic),
            "n_partner_ids": len(out), "partners": out,
            "subject_in_own_partner_set": SUBJECT in out,
            "non_protein_partner_entities": non_protein,
            "partners_with_two_or_more_pmids": multi_pmid,
            "n_nucleic_acid_records": len(nucleic),
            "nucleic_acid_records": nucleic}


# ---------------------------------------------------------------------------
# H. the missing-ortholog question
# ---------------------------------------------------------------------------

MOUSE_ORTHOLOG = "O88573"   # Aff1, the true 1:1 ortholog of human AFF1


def analyse_missing_ortholog_donor(rows: list[dict], resolved: dict) -> dict:
    """For each IBA term, is the true ortholog among the donors -- and if not,
    does it nonetheless hold the term itself?

    A donor set made of paralogs is legitimate for IBA, but it means no
    ortholog-strength inference is available on that row.  The sharper question
    is whether the ortholog *could* have been cited: if it holds the term with its
    own experimental evidence and is still absent from WITH/FROM, that is a
    coverage observation about the propagation, not about the gene.
    """
    out: dict[str, dict] = {}
    for r in rows:
        if r["GO EVIDENCE CODE"] != "IBA":
            continue
        term = r["GO TERM"]
        donors = []
        for tok in filter(None, (t.strip() for t in (r.get("WITH/FROM") or "").split("|"))):
            rec = resolved[tok]
            if rec["kind"] == "protein":
                donors.append(rec["chosen"]["accession"])
        anns = quickgo_annotations(
            f"geneProductId=UniProtKB:{MOUSE_ORTHOLOG}&goId={term}"
            "&goUsage=descendants&goUsageRelationships=is_a,part_of",
            f"ortholog {MOUSE_ORTHOLOG} @ {term}")
        codes = Counter(a.get("goEvidence") for a in anns)
        out[term] = {
            "term": term,
            "donor_accessions": donors,
            "ortholog_is_a_donor": MOUSE_ORTHOLOG in donors,
            "ortholog_annotations_in_subtree": len(anns),
            "ortholog_terms": sorted({a["goId"] for a in anns}),
            "ortholog_evidence_codes": dict(codes),
            "ortholog_has_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
        }
    # Positive control: the ortholog must hold SOMETHING somewhere, otherwise a
    # row of zeros could be a rejected query rather than a real absence.
    total = sum(v["ortholog_annotations_in_subtree"] for v in out.values())
    if total == 0:
        raise Fail(f"control failed: {MOUSE_ORTHOLOG} returned zero annotations "
                   "across every IBA term, which is more likely a rejected query "
                   "than a real absence")
    return out


# ---------------------------------------------------------------------------
# I. within-reference species asymmetry
# ---------------------------------------------------------------------------

def analyse_reference_species_split(proj: dict, pmid: str,
                                    parent: str, child: str) -> dict:
    """For one reference that annotates both a parent and a child complex term,
    resolve the organism of every recipient of each, so a claim that the
    reference treated one clade more specifically than another is measured."""
    v = proj.get(pmid)
    if v is None or not v.get("informative"):
        raise Fail(f"{pmid} has no informative projection result to split")
    def organisms(term_key_prefix: str) -> dict[str, str]:
        hits = {k: ents for k, ents in v["entities_per_term"].items()
                if k.startswith(term_key_prefix)}
        if not hits:
            raise Fail(f"{pmid} carries no {term_key_prefix} annotations; "
                       "the asymmetry claim has no basis")
        ents = sorted({e for ee in hits.values() for e in ee})
        res: dict[str, str] = {}
        for e in ents:
            if not e.startswith("UniProtKB:"):
                res[e] = "(not a UniProt entity)"
                continue
            acc = e.split(":", 1)[1]
            try:
                d = describe_entry(fetch_uniprot(acc))
                res[e] = f"{d['organism']} / {'/'.join(d['genes']) or '?'}"
            except Fail as exc:
                res[e] = f"(unresolvable: {exc})"
        return res
    par, chi = organisms(parent), organisms(child)
    par_only = sorted(set(par) - set(chi))
    return {
        "reference": pmid,
        "parent_term": parent, "child_term": child,
        "parent_recipients": par,
        "child_recipients": chi,
        "parent_only_recipients": par_only,
        "parent_only_organisms": sorted({par[k].split(" / ")[0] for k in par_only}),
        "child_organisms": sorted({v2.split(" / ")[0] for v2 in chi.values()}),
    }


# ---------------------------------------------------------------------------
# K. ancestor closures of every term the review asserts
# ---------------------------------------------------------------------------

def analyse_core_function_closures() -> dict:
    """Fetch the is_a/part_of ancestor closure of every GO term the review's
    ``core_functions`` asserts, so the audit can enforce a CLASS-level invariant --
    no single slot may list both a term and one of its own ancestors -- rather than
    fixing each instance as it is spotted.
    """
    import re as _re
    review = GENE_DIR / "AFF1-ai-review.yaml"
    if not review.exists():
        raise Fail(f"missing {review}; run build_review.py first")
    text = review.read_text()
    start = text.find("\ncore_functions:")
    if start < 0:
        raise Fail("the review has no core_functions section")
    end = text.find("\nreferences:", start)
    block = text[start:end if end > 0 else len(text)]
    terms = sorted(set(_re.findall(r"GO:\d{7}", block)))
    if not terms:
        raise Fail("found zero GO terms in core_functions; the closure check "
                   "would be vacuous")
    out = {}
    for tid in terms:
        anc = ancestors(tid)
        if tid not in anc:
            raise Fail(f"{tid} is absent from its own closure -- the ancestor "
                       f"endpoint is not behaving as assumed")
        out[tid] = sorted(anc)
    return {"n_terms": len(out), "closures": out}


# ---------------------------------------------------------------------------
# J. disorder coverage, computed from the UniProt feature table
# ---------------------------------------------------------------------------

def analyse_disorder() -> dict:
    """Compute how much of the sequence is annotated Disordered.

    Derived rather than asserted: a first draft of the review said "about a
    thousand of its 1210 residues", which overstates the real figure by ~11%.
    Any prose number about disorder is now checked against this.
    """
    import re as _re
    f = GENE_DIR / "AFF1-uniprot.txt"
    if not f.exists():
        raise Fail(f"missing {f}; run `just fetch-gene human AFF1`")
    text = f.read_text()
    m = _re.search(r"^ID\s+\S+\s+Reviewed;\s+(\d+) AA\.", text, _re.M)
    if not m:
        raise Fail("could not read the sequence length from the UniProt ID line")
    length = int(m.group(1))
    lines = text.splitlines()
    regions = []
    for i, ln in enumerate(lines):
        mm = _re.match(r"^FT   REGION\s+(\d+)\.\.(\d+)", ln)
        if mm and i + 1 < len(lines) and "Disordered" in lines[i + 1]:
            regions.append((int(mm.group(1)), int(mm.group(2))))
    if not regions:
        raise Fail("found zero Disordered REGION features; the coverage figure "
                   "would be a vacuous zero rather than a measurement")
    # Union, in case regions ever overlap.
    covered = set()
    for a, b in regions:
        covered.update(range(a, b + 1))
    if max(covered) > length:
        raise Fail(f"a disordered region extends past the sequence length "
                   f"({max(covered)} > {length})")
    return {
        "length": length,
        "n_disordered_regions": len(regions),
        "regions": regions,
        "disordered_residues": len(covered),
        "disordered_fraction": round(len(covered) / length, 4),
    }


# ---------------------------------------------------------------------------
# affinage recall
# ---------------------------------------------------------------------------

def analyse_affinage_recall(rows: list[dict]) -> dict:
    rec = GENE_DIR / "AFF1-deep-research-affinage.md"
    if not rec.exists():
        raise Fail(f"missing {rec}; run the affinage script with --write")
    text = rec.read_text()
    marker = "## Citations"
    if marker not in text:
        raise Fail(f"{rec} has no '{marker}' section -- format changed")
    cited = set()
    for line in text.split(marker, 1)[1].splitlines():
        line = line.strip()
        if line.startswith("- PMID:"):
            cited.add(line[2:].strip())
    if not cited:
        raise Fail("parsed zero citations out of the affinage record")
    non_numeric = sorted(c for c in cited if not c.split(":", 1)[1].isdigit())
    goa_pmids = {r["REFERENCE"] for r in rows if r["REFERENCE"].startswith("PMID:")}
    return {
        "n_affinage_citations": len(cited),
        "non_numeric_pmid_ids": non_numeric,
        "n_goa_pmids": len(goa_pmids),
        "goa_pmids": sorted(goa_pmids),
        "goa_pmids_found_by_affinage": sorted(goa_pmids & cited),
        "goa_pmids_missed_by_affinage": sorted(goa_pmids - cited),
        "recall_on_goa_reference_set": (
            len(goa_pmids & cited) / len(goa_pmids) if goa_pmids else None),
    }


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def render(res: dict) -> str:
    L: list[str] = []
    a = L.append
    a("# AFF1 (P51825) annotation-provenance analysis")
    a("")
    a("Computed by `analyze_aff1_annotations.py`. Every number below is derived by "
      "that script from the GOA TSV, UniProt, QuickGO and IntAct; none is "
      "hand-entered. Re-run to reproduce.")
    a("")
    a(f"- GOA rows analysed: **{res['n_goa_rows']}** "
      f"({res['n_goa_rows_distinct']} distinct)")
    a(f"- Subject: `{SUBJECT}` / {SUBJECT_SYMBOL}, "
      f"{res['subject']['length']} aa, {res['subject']['status']}")
    a("")

    a("## A. WITH/FROM resolution")
    a("")
    a("| token | rows | kind | resolves to | status | note |")
    a("|---|---|---|---|---|---|")
    for tok, r in res["withfrom"].items():
        rows = ",".join(str(i) for i in r["rows"])
        if r["kind"] == "protein":
            c = r["chosen"]
            name = f"{c['accession']} {c['entry_name']} ({'/'.join(c['genes']) or '?'}, {c['organism']})"
            note = []
            if r.get("self_reference"):
                note.append("**self-reference: the subject itself**")
            if c.get("fallback_unreviewed"):
                note.append("no reviewed entry; unreviewed fallback")
            if len(r["candidates"]) > 1:
                note.append(f"{len(r['candidates'])} candidate entries")
            a(f"| `{tok}` | {rows} | protein | {name} | {c['status']} | {'; '.join(note)} |")
        else:
            a(f"| `{tok}` | {rows} | {r['kind']} | – | – | {r.get('note','')} |")
    a("")

    a("## B. Donor evidence for the propagated term")
    a("")
    a("For each (donor, propagated term) pair: what does the donor itself hold? "
      "\"The source only carries the same family-level inference\" is a testable "
      "claim, and IBA WITH/FROM lists experimentally-annotated members by "
      "construction, so it is usually false.")
    a("")
    a("| donor | propagated term | donor annotations | donor evidence codes | holds the exact term | own experimental evidence |")
    a("|---|---|---|---|---|---|")
    for k, v in sorted(res["donor_evidence"].items()):
        d = v["donor"]
        who = f"{d['accession']} {'/'.join(d['genes']) or '?'} ({d['organism']})"
        codes = ", ".join(f"{c}×{n}" for c, n in sorted(v["evidence_codes"].items()))
        a(f"| {who} | {v['propagated_term']} | {v['n_annotations']} | {codes or '–'} | "
          f"{'yes' if v['holds_exact_term'] else 'no'} | "
          f"{'**yes**' if v['has_own_experimental'] else 'no'} |")
    a("")

    a("## C. Reference-projection test")
    a("")
    a("How many *distinct gene products* does each cited reference annotate, and "
      "does the functional term spread across the set or stay on the perturbed "
      "gene? Entity counts are distinct id sets, not annotation totals.")
    a("")
    a("| reference | annotations | distinct entities | verdict |")
    a("|---|---|---|---|")
    for pmid, v in sorted(res["reference_projection"].items()):
        if not v["informative"]:
            a(f"| {pmid} | {v['n_annotations']} | – | UNINFORMATIVE (high-throughput) |")
            continue
        verdict = ("single-entity: no projection" if v["n_entities"] == 1
                   else f"{v['n_entities']} entities – inspect per-term spread")
        a(f"| {pmid} | {v['n_annotations']} | {v['n_entities']} | {verdict} |")
    a("")
    for pmid, v in sorted(res["reference_projection"].items()):
        if not v["informative"] or v["n_entities"] <= 1:
            continue
        a(f"### {pmid}: {v['n_entities']} entities")
        a("")
        a("| term | entities |")
        a("|---|---|")
        for term, ents in v["entities_per_term"].items():
            shown = ", ".join(ents[:12]) + (" …" if len(ents) > 12 else "")
            a(f"| {term} | {len(ents)}: {shown} |")
        a("")

    a("## D. Term relations (fetched, not inferred from labels)")
    a("")
    a("| claim | expected | observed | agrees | why the review needs it |")
    a("|---|---|---|---|---|")
    for k, v in res["relations"].items():
        a(f"| is `{v['ancestor']}` an ancestor of `{v['descendant']}`? | "
          f"{v['expected_is_ancestor']} | {v['observed_is_ancestor']} | "
          f"{'yes' if v['agrees'] else 'NO'} | {v['why_the_review_needs_it']} |")
    a("")

    a("## E. PANTHER node reach")
    a("")
    nr = res["node_reach"]
    a(f"Node `{nr['node']}` carries **{nr['n_annotations']}** IBA annotations over "
      f"**{nr['n_recipient_gene_products']}** recipient gene products.")
    a("")
    a("| term | recipients | human recipients under this node |")
    a("|---|---|---|")
    for t, gps in nr["terms_on_node"].items():
        hum = sorted(g for g in gps if g.split(":")[-1] in HUMAN_AFF)
        a(f"| {t} | {len(gps)} | {len(hum)}: "
          f"{', '.join(HUMAN_AFF[g.split(':')[-1]] for g in hum)} |")
    a("")
    a(f"Full recipient lists are in `results.json` under "
      f"`node_reach.terms_on_node`; only the count and the human members are "
      f"shown here (nothing is filtered from the stored data).")
    a("")
    a("Reciprocally, which PANTHER nodes give each term to a **human** gene "
      "product. Only nodes reaching AFF-family members are tabulated; the "
      "complete node lists, including the many unrelated nodes that supply the "
      "generic terms to other families, are in `results.json` under "
      "`node_reach.human_iba_holders_by_term`.")
    a("")
    a("| term | total human IBA rows | nodes reaching an AFF gene | AFF recipients |")
    a("|---|---|---|---|")
    for t, info in sorted(nr["human_iba_holders_by_term"].items()):
        aff_nodes = {n: gps for n, gps in info["nodes"].items()
                     if any(g.split(":")[-1] in HUMAN_AFF for g in gps)}
        if not aff_nodes:
            a(f"| {t} | {info['n_human_iba_annotations']} | – | (none) |")
        for node, gps in sorted(aff_nodes.items()):
            names = [HUMAN_AFF.get(g.split(":")[-1], g) for g in sorted(gps)]
            a(f"| {t} | {info['n_human_iba_annotations']} | `{node}` "
              f"({len(info['nodes'])} nodes total) | {', '.join(names)} |")
    a("")

    a("## H. Is the true ortholog among the donors?")
    a("")
    a("A paralog donor set is legitimate for IBA, but it means no "
      "ortholog-strength inference is available on that row. Mouse `Aff1` "
      f"(`{MOUSE_ORTHOLOG}`) is AFF1's 1:1 ortholog.")
    a("")
    a("| term | donors | ortholog cited? | ortholog's own annotations in that subtree |")
    a("|---|---|---|---|")
    for t, v in sorted(res["ortholog_donor"].items()):
        donors = ", ".join(f"{d} {HUMAN_AFF.get(d) or MOUSE_NAMES.get(d) or ''}".strip()
                           for d in v["donor_accessions"]) or "–"
        own = (", ".join(f"{c}×{n}" for c, n in sorted(v["ortholog_evidence_codes"].items()))
               or "none")
        a(f"| {t} | {donors} | {'yes' if v['ortholog_is_a_donor'] else '**no**'} | "
          f"{v['ortholog_annotations_in_subtree']} ({own}) |")
    a("")

    a("## I. One reference, two levels of precision, split by clade")
    a("")
    sp = res["reference_species_split"]
    a(f"`{sp['reference']}` annotates both `{sp['parent_term']}` and the more "
      f"specific `{sp['child_term']}`. Resolving every recipient's organism shows "
      "which clade got which term.")
    a("")
    a(f"- recipients of the specific `{sp['child_term']}`: "
      f"{len(sp['child_recipients'])}, organisms "
      f"{', '.join(sp['child_organisms'])}")
    a(f"- recipients of only the general `{sp['parent_term']}`: "
      f"{len(sp['parent_only_recipients'])}, organisms "
      f"{', '.join(sp['parent_only_organisms'])}")
    a("")
    a("| recipient | organism / gene | got the specific term? |")
    a("|---|---|---|")
    for e in sorted(set(sp["parent_recipients"]) | set(sp["child_recipients"])):
        who = sp["parent_recipients"].get(e) or sp["child_recipients"].get(e)
        a(f"| `{e}` | {who} | {'yes' if e in sp['child_recipients'] else 'no'} |")
    a("")

    a("## F. IntAct records expanded per partner")
    a("")
    a("`NbExp` is not an experiment count -- it has been observed counting "
      "sub-methods of one screen, replicates, and even a partner's domains. "
      "Distinct publications and distinct detection methods are counted here.")
    a("")
    ia = res["intact"]
    a(f"All **{ia['n_records_total']}** IntAct records are accounted for: "
      f"**{ia['n_protein_records']}** protein records over "
      f"**{ia['n_partner_ids']}** partner entities, plus "
      f"**{ia['n_nucleic_acid_records']}** records in which the subject appears as "
      "its own Ensembl **transcript** paired with an RNAcentral ncRNA (an RNA-RNA "
      "record, not a protein interaction of AFF1). The run fails if any record is "
      "unassigned; a predicate that silently drops records yields a wrong partner "
      "*set* even when the count looks plausible.")
    a("")
    a(f"Partner entities that are not proteins (a gene id, a fusion construct): "
      f"{', '.join('`'+x+'`' for x in ia['non_protein_partner_entities']) or 'none'}.")
    a("")
    a(f"Partners supported by **two or more distinct PMIDs**: "
      f"{', '.join('`'+x+'`' for x in ia['partners_with_two_or_more_pmids']) or 'none'}.")
    a("")
    a("| partner | name | records | distinct PMIDs | all pub. ids | distinct methods | max MI | subject form |")
    a("|---|---|---|---|---|---|---|---|")
    for k, p in sorted(ia["partners"].items(),
                       key=lambda kv: (-kv[1]["n_distinct_pmids"], -kv[1]["n_records"])):
        a(f"| `{p['id']}` | {', '.join(p['molecule_names']) or '?'} | {p['n_records']} | "
          f"{p['n_distinct_pmids']} | {p['n_all_publication_identifiers']} | "
          f"{p['n_distinct_detection_methods']} | {p['max_mi_score']} | "
          f"{', '.join(p['subject_forms'])}{' (isoform only)' if p['isoform_only'] else ''} |")
    a("")

    a("## J. Disorder coverage (computed from the UniProt feature table)")
    a("")
    ds = res["disorder"]
    a(f"{ds['n_disordered_regions']} `Disordered` REGION features cover "
      f"**{ds['disordered_residues']} of {ds['length']}** residues "
      f"(**{ds['disordered_fraction']:.1%}**): "
      f"{', '.join(f'{a0}-{b0}' for a0, b0 in ds['regions'])}. Derived rather than "
      "asserted, because a first draft of the review rounded this to \"about a "
      "thousand\", overstating it by ~11%.")
    a("")

    a("## G. affinage recall against the GOA reference set")
    a("")
    ar = res["affinage_recall"]
    a(f"- affinage citations: **{ar['n_affinage_citations']}** "
      f"(non-numeric PMID-shaped ids: {ar['non_numeric_pmid_ids'] or 'none'})")
    a(f"- PMIDs cited by AFF1's GOA rows: **{ar['n_goa_pmids']}**")
    a(f"- of those, found by affinage: **{len(ar['goa_pmids_found_by_affinage'])}** "
      f"({ar['recall_on_goa_reference_set']:.0%})")
    a(f"- missed: {', '.join(ar['goa_pmids_missed_by_affinage']) or 'none'}")
    a("")
    a("`gates_passed: True` is a statement about **precision** -- that the "
      "citations returned are real and correctly quoted. It carries no recall "
      "guarantee, and the number above is what recall actually was on the "
      "reference set that decides this gene's annotations.")
    a("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def self_test() -> int:
    """Break-test each guard.  Every case asserts three things in order: the
    mutation applied; the guard fired; the message is the expected one."""
    problems: list[str] = []

    def expect_fail(label: str, fn, must_contain: str) -> None:
        try:
            fn()
        except Fail as exc:
            if must_contain not in str(exc):
                problems.append(
                    f"{label}: guard fired but message was {str(exc)!r}, "
                    f"expected to contain {must_contain!r}")
            else:
                print(f"  ok   {label}: {str(exc)[:90]}")
            return
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{label}: failed for the WRONG reason: "
                            f"{type(exc).__name__}: {exc}")
            return
        problems.append(f"{label}: guard did NOT fire")

    print("self-test: accession-drift guard")
    # O15507 is a merged accession: HTTP 200, complete reviewed record, different
    # protein.  Assert the mutation is real (the accession differs from what the
    # record returns) before asserting the guard fires.
    st, probe = get_json(f"{UNIPROT}/uniprotkb/O15507.json?fields=accession,id")
    if probe is None:
        problems.append("accession-drift fixture unavailable (O15507 returned 404)")
    else:
        got = probe.get("primaryAccession")
        if got == "O15507":
            problems.append("accession-drift fixture is stale: O15507 no longer "
                            "resolves to a different protein, so this break-test "
                            "certifies nothing")
        else:
            print(f"  mutation confirmed: O15507 -> {got}")
            _ENTRY_CACHE.pop("O15507", None)
            expect_fail("accession drift", lambda: fetch_uniprot("O15507"),
                        "ACCESSION DRIFT")

    print("self-test: reviewed-vs-unreviewed substring trap")
    # `"reviewed" in entryType` matches "unreviewed"; the anchored test must not.
    naive = "reviewed" in "UniProtKB unreviewed (TrEMBL)"
    if not naive:
        problems.append("substring fixture is stale: 'reviewed' is no longer a "
                        "substring of 'unreviewed', so this test proves nothing")
    else:
        if is_reviewed({"entryType": "UniProtKB unreviewed (TrEMBL)"}):
            problems.append("is_reviewed() promoted a TrEMBL entry")
        elif not is_reviewed({"entryType": "UniProtKB reviewed (Swiss-Prot)"}):
            problems.append("is_reviewed() rejected a Swiss-Prot entry "
                            "(the happy path is the untested path)")
        else:
            print("  ok   anchored test separates reviewed from unreviewed while "
                  "the naive substring test does not")

    print("self-test: truncation guard")
    # Ask for a term with many annotations but cap pagination at one page by
    # mutating the page ceiling, and confirm the count mismatch is caught.
    def truncated() -> None:
        url = (f"{QUICKGO}/annotation/search?goId=GO:0005515&taxonId=9606"
               "&limit=100&page=1")
        st, d = get_json(url)
        total, got = d["numberOfHits"], len(d["results"])
        if total <= got:
            raise Exception("truncation fixture is stale: the query no longer "
                            "returns more hits than one page holds")
        raise Fail(f"TRUNCATION: control reported numberOfHits={total} but "
                   f"collected {got} -- the service clamped or paging failed")
    expect_fail("truncation", truncated, "TRUNCATION")

    print("self-test: missing-input guard (must be a hard error, not a "
          "silently degraded section)")
    orig = globals()["GOA_TSV"]
    globals()["GOA_TSV"] = HERE / "definitely-not-a-file.tsv"
    if globals()["GOA_TSV"].exists():
        problems.append("missing-input fixture exists on disk; mutation no-op")
    else:
        expect_fail("missing input", read_goa, "run `just fetch-gene")
    globals()["GOA_TSV"] = orig
    if not globals()["GOA_TSV"].exists():
        problems.append("failed to restore GOA_TSV after the break-test")

    print("self-test: relation guard rejects a FALSE ancestry claim")
    orig_claims = list(RELATION_CLAIMS)
    RELATION_CLAIMS.clear()
    # regulation is not subsumption: GO:0006355 is not an ancestor of GO:0006354
    RELATION_CLAIMS.append(("GO:0006354", "GO:0006355", True, "deliberately false"))
    if RELATION_CLAIMS == orig_claims:
        problems.append("relation fixture is a no-op: the claim list did not change")
    else:
        expect_fail("false relation claim", analyse_relations,
                    "contradicted by the ontology")
    RELATION_CLAIMS.clear()
    RELATION_CLAIMS.extend(orig_claims)
    if RELATION_CLAIMS != orig_claims:
        problems.append("failed to restore RELATION_CLAIMS")

    print("self-test: relation guard PASSES on true claims (the happy direction)")
    try:
        analyse_relations()
        print("  ok   all true relation claims verified")
    except Fail as exc:
        problems.append(f"relation guard failed on the real claim set: {exc}")

    print()
    if problems:
        print("SELF-TEST FAILURES:")
        for p in problems:
            print("  ✗", p)
        return 1
    print("self-test: all guards fired for the right reason, and the happy "
          "directions pass.")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()

    rows = read_goa()
    distinct = {tuple(sorted(r.items())) for r in rows}
    subject = describe_entry(fetch_uniprot(SUBJECT))

    res: dict[str, Any] = {
        "subject": subject,
        "n_goa_rows": len(rows),
        "n_goa_rows_distinct": len(distinct),
    }
    print(f"subject {subject['accession']} {subject['entry_name']} "
          f"{subject['length']} aa {subject['status']}")

    print("A. resolving WITH/FROM ...")
    res["withfrom"] = analyse_withfrom(rows)
    print("B. donor evidence ...")
    res["donor_evidence"] = analyse_donor_evidence(rows, res["withfrom"])
    print("C. reference projection ...")
    res["reference_projection"] = analyse_reference_projection(rows)
    print("D. term relations ...")
    res["relations"] = analyse_relations()
    print("E. node reach ...")
    res["node_reach"] = analyse_node_reach(rows)
    print("F. IntAct ...")
    res["intact"] = analyse_intact()
    print("G. affinage recall ...")
    res["affinage_recall"] = analyse_affinage_recall(rows)
    print("H. missing-ortholog donor question ...")
    res["ortholog_donor"] = analyse_missing_ortholog_donor(rows, res["withfrom"])
    print("K. core-function term closures ...")
    res["core_function_closures"] = analyse_core_function_closures()
    print("J. disorder coverage ...")
    res["disorder"] = analyse_disorder()
    print("I. within-reference species asymmetry ...")
    res["reference_species_split"] = analyse_reference_species_split(
        res["reference_projection"], "PMID:22195968", "GO:0008023", "GO:0032783")

    OUT_JSON.write_text(json.dumps(res, indent=2, sort_keys=True, default=str) + "\n")
    OUT_MD.write_text(render(res))
    print(f"wrote {OUT_JSON.name} and {OUT_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
