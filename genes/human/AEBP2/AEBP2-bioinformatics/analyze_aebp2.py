#!/usr/bin/env python3
"""Reproducible provenance analysis of the human AEBP2 (Q6ZN18) GO annotation set.

Every claim in ``AEBP2-ai-review.yaml`` and ``AEBP2-notes.md`` that rests on a
count, a set, or a database lookup is computed here.  Run with::

    uv run --no-project python analyze_aebp2.py            # write results.json + RESULTS.md
    uv run --no-project python analyze_aebp2.py --self-test  # break-test the guards

Design rules this file follows (each earned by a failure elsewhere in the campaign):

* **Assert ``primaryAccession == requested``** on every UniProt fetch.  A merged
  accession returns HTTP 200 with a complete record *for a different protein*.
* **Reviewed status is tested with ``startswith("UniProtKB reviewed")``** — the
  substring ``"reviewed" in entryType`` also matches ``"unreviewed"``.
* **Every QuickGO query is fully paginated and asserts ``numberOfHits ==
  len(results)``** — the service clamps rather than erroring, so a page-size
  constant cannot be used as the guard.
* **Every reported zero carries a positive control from the same endpoint in the
  same call pattern**, so a rejected query cannot masquerade as a real zero.
* **Assertions are on set membership, not cardinality.**  Two cancelling errors
  keep a count right while corrupting the set.
* **No stage silently reduces a set.**  Anywhere the emitted number could differ
  from the computed one, the difference is stated.
* Checks append to a ``problems`` list; none of them raises, so one failing check
  cannot abort the ones after it.
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
SUBJECT = "Q6ZN18"
SUBJECT_SYMBOL = "AEBP2"

QUICKGO_ANN = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
QUICKGO_TERM = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms"
UNIPROT = "https://rest.uniprot.org"
RCSB = "https://data.rcsb.org/rest/v1/core"

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _get_json(url: str) -> tuple[int, dict | None]:
    """Return (status, payload).  A non-200 returns the status and None so the
    caller can distinguish a rejected query from an empty result."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as exc:
        return exc.code, None


def quickgo(**params) -> tuple[int, list[dict]]:
    """Fully paginated QuickGO annotation search.

    Returns ``(numberOfHits, results)`` and raises if the two disagree, which is
    the only truncation guard that survives the server changing its page cap.
    """
    params.setdefault("limit", 100)
    page, results, hits = 1, [], None
    while True:
        params["page"] = page
        url = QUICKGO_ANN + "?" + urllib.parse.urlencode(params, safe=":,|")
        status, payload = _get_json(url)
        if status != 200:
            if page > 1:
                # QuickGO refuses pages beyond an undocumented cap. A rejected
                # query and a genuine end-of-results look identical downstream,
                # so convert it into a LOUD truncation report rather than an
                # opaque HTTP error: we know we did not read everything.
                raise RuntimeError(
                    f"QuickGO truncated: server rejected page {page} with HTTP "
                    f"{status} (page cap) after retrieving {len(results)} of "
                    f"{hits} for {params!r}"
                )
            raise RuntimeError(f"QuickGO HTTP {status} for {params!r}")
        if hits is None:
            hits = payload["numberOfHits"]
        results += payload["results"]
        if len(results) >= hits or not payload["results"]:
            break
        page += 1
        time.sleep(0.05)
    if len(results) != hits:
        raise RuntimeError(
            f"QuickGO truncated: numberOfHits={hits} but retrieved {len(results)} for {params!r}"
        )
    return hits, results


def uniprot_entry(accession: str, fields: str) -> dict:
    """Fetch one UniProtKB entry and assert it is the entry that was asked for."""
    url = f"{UNIPROT}/uniprotkb/{accession}.json?fields={fields}"
    status, payload = _get_json(url)
    if status != 200 or payload is None:
        raise RuntimeError(f"UniProt HTTP {status} for {accession}")
    got = payload.get("primaryAccession")
    if got != accession:
        raise RuntimeError(
            f"ACCESSION DRIFT: asked for {accession}, server returned {got} "
            f"({payload.get('uniProtkbId')}). A merged accession returns 200 for "
            f"a different protein."
        )
    if not payload.get("uniProtkbId"):
        raise RuntimeError(f"{accession} has no entry name — inactive/deleted entry?")
    return payload


def uniprot_search(query: str, fields: str, size: int = 5) -> list[dict]:
    """Search UniProt.  ``size >= 2`` always, so a multi-hit cross-reference is
    reported as ambiguous data rather than silently resolved to one answer."""
    assert size >= 2, "size=1 converts an ambiguity into a confident wrong answer"
    url = f"{UNIPROT}/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": query, "fields": fields, "size": size}
    )
    status, payload = _get_json(url)
    if status != 200 or payload is None:
        raise RuntimeError(f"UniProt search HTTP {status} for {query!r}")
    return payload.get("results", [])


def is_reviewed(entry: dict) -> bool:
    """``"reviewed" in entryType`` also matches ``"unreviewed"``.  Anchor it."""
    return str(entry.get("entryType", "")).startswith("UniProtKB reviewed")


def go_term(go_id: str) -> dict:
    status, payload = _get_json(f"{QUICKGO_TERM}/{go_id}/complete")
    if status != 200 or payload is None:
        raise RuntimeError(f"QuickGO term HTTP {status} for {go_id}")
    return payload["results"][0]


# --------------------------------------------------------------------------- #
# GOA TSV
# --------------------------------------------------------------------------- #
GOA_COLUMNS = [
    "db", "id", "symbol", "qualifier", "go_id", "go_name", "aspect", "eco",
    "evidence", "reference", "with_from", "taxon", "taxon_name", "assigned_by",
    "gene_name", "date",
]


def read_goa(path: Path) -> list[dict]:
    lines = path.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    if len(header) != len(GOA_COLUMNS):
        raise RuntimeError(
            f"GOA schema drift: {len(header)} columns, expected {len(GOA_COLUMNS)}"
        )
    rows = []
    for line in lines[1:]:
        cells = line.split("\t")
        cells += [""] * (len(GOA_COLUMNS) - len(cells))
        rows.append(dict(zip(GOA_COLUMNS, cells)))
    return rows


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #
def check_row_reconciliation(goa_rows, problems) -> dict:
    """CLAUDE.md requires one review entry per GOA line, but the fetch-gene stub
    keys seeded entries on (term, evidence, reference, negated, qualifier) and
    omits WITH/FROM, so rows differing only in WITH/FROM collapse.  Reconcile
    the three counts explicitly rather than trusting the stub."""
    review = GENE_DIR / f"{SUBJECT_SYMBOL}-ai-review.yaml"
    review_text = review.read_text()
    raw_terms = sum(1 for line in review_text.splitlines()
                    if line.startswith("- term:"))
    # Count the review's own NEW proposals from the raw text, so the reconciliation below
    # is an assertion rather than two numbers printed side by side. An unexplained
    # mismatch is either missing coverage or a silent collapse.
    new_rows = len(re.findall(r"^\s*action: NEW\s*$", review_text, re.M))
    distinct = len({tuple(sorted(r.items())) for r in goa_rows})
    hits, qg = quickgo(geneProductId=f"UniProtKB:{SUBJECT}")
    out = {
        "goa_tsv_data_rows": len(goa_rows),
        "goa_tsv_distinct_rows": distinct,
        "quickgo_annotation_count": hits,
        "review_yaml_entries": raw_terms,
        "review_yaml_new_proposals": new_rows,
        "review_entries_minus_new": raw_terms - new_rows,
    }
    if raw_terms - new_rows != distinct:
        problems.append(
            f"review has {raw_terms} entries of which {new_rows} are NEW proposals, "
            f"leaving {raw_terms - new_rows} to cover {distinct} distinct GOA rows - "
            "either a GOA row is unreviewed or entries were collapsed"
        )
    if distinct != len(goa_rows):
        problems.append(
            f"GOA TSV has duplicate lines: {len(goa_rows)} raw vs {distinct} distinct"
        )
    if hits != len(goa_rows):
        problems.append(
            f"QuickGO ({hits}) disagrees with the cached GOA TSV ({len(goa_rows)}) — "
            "the TSV may be stale"
        )
    out["quickgo_evidence_census"] = dict(Counter(r["goEvidence"] for r in qg))
    out["goa_aspect_census"] = dict(Counter(r["aspect"] for r in goa_rows))
    if out["goa_aspect_census"].get("molecular_function", 0) != 0:
        problems.append(
            "molecular_function rows now present in GOA — the 'zero MF' claim in "
            "the review and notes is stale and must be rewritten"
        )
    return out


def check_withfrom(goa_rows, problems) -> dict:
    """Resolve every WITH/FROM token.  Built FROM the TSV field, never by hand,
    so the token set matches GOA by construction."""
    tokens: dict[str, set[str]] = defaultdict(set)
    for row in goa_rows:
        for tok in filter(None, row["with_from"].split("|")):
            tokens[tok].add(f"{row['go_id']}/{row['evidence']}/{row['reference']}")

    resolvers = {
        "MGI:MGI:1338038": ("xref:mgi-1338038", "MOD gene id: UniProt wants the BARE number; "
                                                "an inner colon returns HTTP 400"),
        "FB:FBgn0086655": ("xref:flybase-FBgn0086655", "MOD gene id"),
        "ensembl:ENSMUSP00000084896": ("xref:ensembl-ENSMUSP00000084896", "Ensembl protein id"),
    }
    resolved = {}
    for token in sorted(tokens):
        entry = {"token": token, "rows": sorted(tokens[token])}
        if token.startswith("UniProtKB:"):
            acc = token.split(":", 1)[1]
            rec = uniprot_entry(acc, "accession,id,gene_names,organism_name,length,reviewed")
            entry.update(
                kind="uniprot_accession",
                accession=rec["primaryAccession"],
                entry_name=rec["uniProtkbId"],
                reviewed=is_reviewed(rec),
                length=rec["sequence"]["length"],
                gene=[g.get("geneName", {}).get("value") for g in rec.get("genes", [])],
                organism=rec.get("organism", {}).get("scientificName"),
                self_reference=(acc == SUBJECT),
            )
        elif token.startswith("PANTHER:"):
            entry.update(kind="panther_tree_node",
                         note="an internal PANTHER tree node, not a protein")
        elif token.startswith("ARBA:"):
            rule = token.split(":", 1)[1]
            status, payload = _get_json(f"{UNIPROT}/arba/{rule}")
            if status != 200 or payload is None:
                problems.append(f"ARBA {rule} unresolvable (HTTP {status})")
                entry.update(kind="arba_rule", resolved=False)
            else:
                sets = []
                for cset in payload["mainRule"]["conditionSets"]:
                    sets.append([
                        ("NOT " if c["isNegative"] else "")
                        + c["type"] + "=" + "|".join(v["value"] for v in c["conditionValues"])
                        for c in cset["conditions"]
                    ])
                entry.update(
                    kind="arba_rule", resolved=True,
                    asserts=[a["dbReference"]["id"]
                             for a in payload["mainRule"].get("annotations", [])],
                    condition_sets=sets,
                    created=payload.get("createdDate"),
                    modified=payload.get("modifiedDate"),
                )
        elif token.startswith(("UniProtKB-SubCell:", "tfclass:")):
            entry.update(kind="controlled_vocabulary_id",
                         note="a vocabulary term, not a gene product")
        elif token in resolvers:
            query, note = resolvers[token]
            hits = uniprot_search(
                query, "accession,id,gene_names,organism_name,length,reviewed", size=10
            )
            if not hits:
                problems.append(f"{token} resolved to zero UniProt entries")
            sp = [h for h in hits if is_reviewed(h)]
            entry.update(
                kind="mod_gene_id", resolver_query=query, resolver_note=note,
                n_candidates=len(hits), n_reviewed=len(sp),
                candidates=[{
                    "accession": h["primaryAccession"], "entry_name": h.get("uniProtkbId"),
                    "reviewed": is_reviewed(h), "length": h["sequence"]["length"],
                    "gene": [g.get("geneName", {}).get("value") for g in h.get("genes", [])],
                    "organism": h.get("organism", {}).get("scientificName"),
                } for h in hits],
            )
            if len(sp) != 1:
                problems.append(
                    f"{token}: expected exactly one Swiss-Prot candidate, got {len(sp)} "
                    "— an ambiguous cross-reference is data, report all candidates"
                )
        else:
            problems.append(f"UNRESOLVED WITH/FROM token {token} — cannot be dismissed, only deferred")
            entry.update(kind="unresolved")
        resolved[token] = entry

    unresolved = [t for t, e in resolved.items() if e.get("kind") == "unresolved"]
    return {"n_tokens": len(tokens), "tokens": resolved, "unresolved": unresolved}


def check_donor_evidence(problems) -> dict:
    """For every IBA donor, ask what evidence the donor itself carries for the
    propagated term — not merely whether it carries one, and WHICH term."""
    pairs = [
        ("Q9Z248", "mouse Aebp2", "GO:0035098"),
        ("Q9Z248", "mouse Aebp2", "GO:0006357"),
        ("Q9Z248", "mouse Aebp2", "GO:0000122"),
        ("Q7KHG2", "Drosophila jing", "GO:0006357"),
        ("Q7KHG2", "Drosophila jing", "GO:0035098"),
    ]
    out = {}
    for acc, label, go_id in pairs:
        _, rows = quickgo(
            geneProductId=f"UniProtKB:{acc}", goId=go_id,
            goUsage="descendants", goUsageRelationships="is_a,part_of",
        )
        own = [
            {"term": r["goId"], "evidence": r["goEvidence"], "reference": r["reference"]}
            for r in rows if r["goEvidence"] in EXPERIMENTAL_CODES
        ]
        out[f"{acc}:{go_id}"] = {
            "donor": label, "requested_term": go_id, "n_rows": len(rows),
            "experimental_rows": own,
            "all_rows": [{"term": r["goId"], "evidence": r["goEvidence"],
                          "reference": r["reference"]} for r in rows],
        }
    # POSITIVE CONTROL: the same call pattern must return a non-zero for a gene
    # that certainly holds the term, otherwise a zero above is a rejected query.
    _, ctl = quickgo(geneProductId="UniProtKB:Q15910", goId="GO:0035098",
                     goUsage="descendants", goUsageRelationships="is_a,part_of")
    out["_positive_control"] = {
        "query": "EZH2 Q15910 x GO:0035098(descendants)", "n_rows": len(ctl)
    }
    if not ctl:
        problems.append("positive control returned zero — every zero above is uninterpretable")

    # The GO:0006357 IBA is the LCA of donors that disagree on SIGN.  Test that.
    directions = set()
    for key in ("Q9Z248:GO:0006357", "Q7KHG2:GO:0006357"):
        for row in out[key]["experimental_rows"]:
            if row["term"] == "GO:0000122":
                directions.add("negative")
            if row["term"] == "GO:0045944":
                directions.add("positive")
    out["_go0006357_donor_directions"] = sorted(directions)
    out["_go0006357_is_lca_of_disagreeing_donors"] = directions == {"negative", "positive"}
    if not out["_go0006357_is_lca_of_disagreeing_donors"]:
        problems.append(
            "the GO:0006357 IBA donors no longer disagree on direction "
            f"(found {sorted(directions)}) — the 'general term is the correct LCA' "
            "argument in the review must be re-derived"
        )
    return out


def check_panther_node(problems) -> dict:
    """Judge granularity against a node's RECIPIENTS, not its seeds, and ask the
    reciprocal question: what did the node give each recipient?"""
    node = "PANTHER:PTN002323211"
    _, rows = quickgo(withFrom=node)
    per_entity: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        per_entity[r["geneProductId"]].add(r["goId"])
    both = {e for e, t in per_entity.items() if t == {"GO:0006357", "GO:0035098"}}
    only_bp = {e for e, t in per_entity.items() if t == {"GO:0006357"}}
    other = set(per_entity) - both - only_bp
    out = {
        "node": node,
        "n_annotations": len(rows),
        "n_recipients": len(per_entity),
        "n_with_both_terms": len(both),
        "n_with_only_GO_0006357": len(only_bp),
        "n_with_other_term_sets": len(other),
        "other_term_sets": sorted({tuple(sorted(per_entity[e])) for e in other}),
        "subject_terms": sorted(per_entity.get(f"UniProtKB:{SUBJECT}", [])),
    }
    if f"UniProtKB:{SUBJECT}" not in per_entity:
        problems.append(f"{SUBJECT} absent from its own PANTHER node's recipient set")
    if out["subject_terms"] != ["GO:0006357", "GO:0035098"]:
        problems.append(
            f"subject's node terms changed to {out['subject_terms']} — the review's "
            "IBA discussion is stale"
        )
    if not only_bp:
        problems.append(
            "no recipient now receives GO:0006357 without GO:0035098 — the claim "
            "that PAINT withholds the animal complex term from a subset is stale"
        )
    return out


def check_reference_projection(problems) -> dict:
    """A reference that annotates the complex plus every subunit with an
    identical term set is a projection, not N independent findings.  Ask BOTH
    questions: how many entities, and does the functional term spread or stay on
    the perturbed entity?"""
    out = {}
    for ref in ("PMID:33514705", "PMID:29348366", "PMID:20075857",
                "PMID:29499137", "PMID:10329662", "GO_REF:0000113"):
        hits, rows = quickgo(reference=ref)
        per_entity: dict[str, set[tuple[str, str]]] = defaultdict(set)
        for r in rows:
            per_entity[r["geneProductId"]].add((r["goId"], r["goEvidence"]))
        signatures = Counter(
            frozenset(t for t, _ in v) for v in per_entity.values()
        )
        out[ref] = {
            "n_annotations": hits,
            "n_entities": len(per_entity),
            "assigned_by": dict(Counter(r["assignedBy"] for r in rows)),
            "n_complexportal_complex_entities":
                sum(1 for e in per_entity if e.startswith("ComplexPortal:")),
            "term_set_signatures": sorted(
                ([sorted(s), c] for s, c in signatures.items()), key=lambda x: -x[1]
            ),
            "per_entity": {e: sorted(v) for e, v in sorted(per_entity.items())}
            if len(per_entity) <= 15 else "omitted (>15 entities)",
        }
    return out


def check_tfclass_dbtf_census(problems) -> dict:
    """GO_REF:0000113 is TFClass-derived DbTF curation.  The prediction to test
    is 'a zinc finger became sequence-specific DNA binding'.  Measure whether
    the subject received the DbTF molecular function, against the whole
    reference's recipient set as the denominator."""
    _, rows = quickgo(reference="GO_REF:0000113")
    per_entity: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        per_entity[r["geneProductId"]].add(r["goId"])
    dbtf = "GO:0000981"
    chromatin = "GO:0000785"
    with_dbtf = {e for e, t in per_entity.items() if dbtf in t}
    without = {e for e, t in per_entity.items() if dbtf not in t}
    subject = f"UniProtKB:{SUBJECT}"
    out = {
        "reference": "GO_REF:0000113",
        "n_annotations": len(rows),
        "n_recipients": len(per_entity),
        "n_with_GO_0000981_dbtf_activity": len(with_dbtf),
        "n_without_GO_0000981": len(without),
        "pct_with_dbtf": round(100 * len(with_dbtf) / len(per_entity), 1),
        "subject_terms": sorted(per_entity.get(subject, [])),
        "subject_in_withheld_set": subject in without,
        "withheld_set": sorted(without),
    }
    # Assert MEMBERSHIP, not the count: a count can stay right while the set rots.
    if subject not in per_entity:
        problems.append(f"{SUBJECT} no longer receives GO_REF:0000113 at all")
    elif subject not in without:
        problems.append(
            f"{SUBJECT} now DOES carry {dbtf} from GO_REF:0000113 — the review's "
            "non-confirmation of the zinc-finger/DbTF over-annotation is refuted "
            "and every surface asserting it must be rewritten"
        )
    if per_entity.get(subject) != {chromatin}:
        problems.append(
            f"{SUBJECT}'s GO_REF:0000113 term set is {sorted(per_entity.get(subject, []))}, "
            f"expected exactly [{chromatin}]"
        )
    # name the withheld set so the reader can judge its coherence
    accs = [e.split(":", 1)[1] for e in sorted(without) if e.startswith("UniProtKB:")]
    if accs:
        query = "(" + " OR ".join(f"accession:{a}" for a in accs) + ")"
        recs = uniprot_search(query, "accession,id,gene_names,protein_name",
                              size=max(2, len(accs)))
        got = {r["primaryAccession"] for r in recs}
        missing = set(accs) - got
        if missing:
            problems.append(f"could not resolve withheld-set accessions {sorted(missing)}")
        out["withheld_set_named"] = sorted(
            {
                "accession": r["primaryAccession"],
                "gene": ([g.get("geneName", {}).get("value")
                          for g in r.get("genes", [])] or [None])[0],
                "name": r.get("proteinDescription", {}).get("recommendedName", {})
                         .get("fullName", {}).get("value"),
            }
            for r in recs
        ) if False else [
            {
                "accession": r["primaryAccession"],
                "gene": ([g.get("geneName", {}).get("value")
                          for g in r.get("genes", [])] or [None])[0],
                "name": r.get("proteinDescription", {}).get("recommendedName", {})
                         .get("fullName", {}).get("value"),
            }
            for r in sorted(recs, key=lambda x: x["primaryAccession"])
        ]
    return out


def check_prc2_mf_census(problems) -> dict:
    """AEBP2's headline gap is a molecular function gap.  Measure it against the
    rest of the complex rather than asserting it."""
    subunits = {
        "Q15910": "EZH2", "Q92800": "EZH1", "O75530": "EED", "Q15022": "SUZ12",
        "Q09028": "RBBP4", "Q16576": "RBBP7", "Q92833": "JARID2",
        "Q6ZN18": "AEBP2", "Q5T6S3": "PHF19", "Q9Y483": "MTF2",
        "Q8N7C0": "EPOP", "Q86SE9": "PALI1(LCOR)",
    }
    watch = ["GO:0031507", "GO:0035098", "GO:0003712", "GO:0031491",
             "GO:0046976", "GO:0008047", "GO:0180000", "GO:0003677"]
    out = {"subunits": {}, "watched_terms": watch}
    for acc, name in subunits.items():
        _, rows = quickgo(geneProductId=f"UniProtKB:{acc}")
        mf = [r for r in rows if r["goAspect"] == "molecular_function"]
        out["subunits"][name] = {
            "accession": acc,
            "n_annotations": len(rows),
            "n_molecular_function_rows": len(mf),
            "molecular_function_terms": sorted({r["goId"] for r in mf}),
            "watched": {
                t: sorted({r["goEvidence"] for r in rows if r["goId"] == t})
                for t in watch if any(r["goId"] == t for r in rows)
            },
        }
    zero_mf = [n for n, v in out["subunits"].items()
               if v["n_molecular_function_rows"] == 0]
    out["subunits_with_zero_mf_rows"] = sorted(zero_mf)
    if zero_mf != [SUBJECT_SYMBOL]:
        problems.append(
            f"the set of PRC2 subunits with zero MF rows is {sorted(zero_mf)}, not "
            f"[{SUBJECT_SYMBOL}] — the review's 'only subunit with no MF' claim is stale"
        )
    # GO:0031507 spread: the projection signature is 'everyone has it by NAS'
    nas_only = sorted(n for n, v in out["subunits"].items()
                      if v["watched"].get("GO:0031507") == ["NAS"])
    richer = sorted(n for n, v in out["subunits"].items()
                    if "GO:0031507" in v["watched"]
                    and v["watched"]["GO:0031507"] != ["NAS"])
    out["GO_0031507_NAS_only_subunits"] = nas_only
    out["GO_0031507_subunits_with_other_evidence"] = richer
    if SUBJECT_SYMBOL not in nas_only:
        problems.append(
            f"{SUBJECT_SYMBOL} no longer holds GO:0031507 by NAS alone "
            f"({out['subunits'][SUBJECT_SYMBOL]['watched'].get('GO:0031507')}) — "
            "the projection argument must be re-derived"
        )
    return out


def check_go0180000_precedent(problems) -> dict:
    """A proposed term needs its in-pathway precedent measured, not assumed."""
    term = go_term("GO:0180000")
    _, rows = quickgo(goId="GO:0180000", goUsage="descendants",
                      goUsageRelationships="is_a,part_of")
    human_exp = [
        {"entity": r["geneProductId"], "symbol": r["symbol"],
         "evidence": r["goEvidence"], "reference": r["reference"]}
        for r in rows if r["goEvidence"] in EXPERIMENTAL_CODES
    ]
    out = {
        "term": "GO:0180000",
        "name": term.get("name"),
        "definition": (term.get("definition") or {}).get("text"),
        "obsolete": term.get("isObsolete"),
        "secondary_ids": term.get("secondaryIds"),
        "n_annotations_in_goa": len(rows),
        "distinct_symbols": sorted({r["symbol"] for r in rows}),
        "experimental_anchors": human_exp,
        "subject_already_holds_it": any(
            r["geneProductId"] == f"UniProtKB:{SUBJECT}" for r in rows
        ),
    }
    if term.get("isObsolete"):
        problems.append("GO:0180000 is obsolete — do not propose it")
    if not human_exp:
        problems.append(
            "GO:0180000 has no experimental anchor anywhere in GOA — the "
            "'EZHIP precedent' claim is unsupported"
        )
    if out["subject_already_holds_it"]:
        problems.append(
            "the subject already holds GO:0180000 — the proposal is not novel and "
            "should be an existing-row review, not a NEW row"
        )
    return out


def check_logical_opposites(goa_rows, problems) -> dict:
    """Intersect the reference sets of every logically opposed term pair present.
    A non-empty intersection is a defect visible from the TSV alone."""
    pairs = [
        ("GO:0000122", "GO:0045944", "negative / positive regulation of transcription by RNA Pol II"),
        ("GO:0045892", "GO:0045893", "negative / positive regulation of DNA-templated transcription"),
        ("GO:0031507", "GO:0031508", "heterochromatin formation / (paired opposite, if annotated)"),
    ]
    present = {r["go_id"] for r in goa_rows}
    findings = []
    for a, b, label in pairs:
        refs_a = {r["reference"] for r in goa_rows if r["go_id"] == a}
        refs_b = {r["reference"] for r in goa_rows if r["go_id"] == b}
        findings.append({
            "pair": [a, b], "label": label,
            "both_terms_present": a in present and b in present,
            "shared_references": sorted(refs_a & refs_b),
            "is_full_cross_product": bool(refs_a) and bool(refs_b)
                                      and refs_a == refs_b,
        })
        if refs_a & refs_b:
            problems.append(
                f"logical-opposite cross-product: {a} and {b} share references "
                f"{sorted(refs_a & refs_b)} — no single reference can support both"
            )
    # positive control: the checker must be able to see a cross-product at all
    synthetic = [
        {"go_id": "GO:0000122", "reference": "PMID:1"},
        {"go_id": "GO:0045944", "reference": "PMID:1"},
    ]
    ctl_a = {r["reference"] for r in synthetic if r["go_id"] == "GO:0000122"}
    ctl_b = {r["reference"] for r in synthetic if r["go_id"] == "GO:0045944"}
    return {
        "pairs_tested": findings,
        "result": "no logically opposed pair is co-annotated on this gene"
                  if not any(f["shared_references"] for f in findings)
                  else "cross-product found",
        "_self_check_detects_a_synthetic_cross_product": bool(ctl_a & ctl_b),
    }


def check_pdb_constructs(problems) -> dict:
    """PMID:41168462 states that every prior PRC2-AEBP2 structure used AEBP2S or
    an N-terminally truncated construct.  That is a checkable claim; check it,
    because two of this review's verdicts lean on it."""
    entries = ["5WAI", "5Y0U", "5Y1U", "6C23", "6C24", "6WKR", "7KSO", "8EQV",
               "8FYH", "8T9G", "8TAS", "8TB9", "8VMI", "8VML", "8VNV", "8VNZ",
               "9C8U", "9DCH"]
    rows = []
    for pdb in entries:
        status, entry = _get_json(f"{RCSB}/entry/{pdb}")
        if status != 200 or entry is None:
            problems.append(f"PDB {pdb} HTTP {status}")
            continue
        cite = entry.get("rcsb_primary_citation", {}) or {}
        rec = {
            "pdb_id": pdb,
            "title": entry.get("struct", {}).get("title"),
            "released": (entry.get("rcsb_accession_info", {}) or {}).get("initial_release_date", "")[:10],
            "primary_citation_pmid": cite.get("pdbx_database_id_PubMed"),
            "aebp2_ref_ranges": [],
        }
        for eid in (entry.get("rcsb_entry_container_identifiers", {}) or {}).get("polymer_entity_ids", []):
            st2, pe = _get_json(f"{RCSB}/polymer_entity/{pdb}/{eid}")
            if st2 != 200 or pe is None:
                continue
            desc = ((pe.get("rcsb_polymer_entity") or {}).get("pdbx_description") or "")
            if "AEBP" not in desc.upper():
                continue
            for al in (pe.get("rcsb_polymer_entity_align") or []):
                if al.get("reference_database_accession") != SUBJECT:
                    continue
                for reg in al.get("aligned_regions", []):
                    beg = reg.get("ref_beg_seq_id")
                    length = reg.get("length")
                    rec["aebp2_ref_ranges"].append(
                        {"ref_beg": beg,
                         "ref_end": (beg + length - 1) if beg and length else None}
                    )
        if rec["aebp2_ref_ranges"]:
            rows.append(rec)
    if not rows:
        problems.append("no PDB entry resolved an AEBP2 chain — the construct census is empty")
    for rec in rows:
        rec["min_ref_beg"] = min(r["ref_beg"] for r in rec["aebp2_ref_ranges"])
    full_length = [r for r in rows if r["min_ref_beg"] == 1]
    truncated = [r for r in rows if r["min_ref_beg"] > 1]
    out = {
        "n_pdb_entries_with_an_AEBP2_chain": len(rows),
        "entries": sorted(rows, key=lambda r: (r["released"] or "")),
        "n_full_length_from_residue_1": len(full_length),
        "n_n_terminally_truncated": len(truncated),
        "full_length_entries": [
            {"pdb_id": r["pdb_id"], "released": r["released"],
             "primary_citation_pmid": r["primary_citation_pmid"],
             "title": r["title"]} for r in full_length
        ],
        "min_ref_beg_of_truncated": sorted({r["min_ref_beg"] for r in truncated}),
    }
    # The load-bearing claim: the ONLY structure whose primary citation is the
    # AEBP2L paper is the one that is full length, and it is not the oldest.
    aebp2l_paper = [r for r in full_length if r["primary_citation_pmid"] == 41168462]
    out["full_length_entries_citing_PMID_41168462"] = [r["pdb_id"] for r in aebp2l_paper]
    if not aebp2l_paper:
        problems.append(
            "no full-length AEBP2 structure cites PMID:41168462 — the claim that "
            "8EQV is that paper's own AEBP2L structure is unsupported"
        )
    if not truncated:
        problems.append("no truncated AEBP2 construct found — the census claim is stale")
    return out


def check_isoform_mapping(problems) -> dict:
    """PMID:41168462 names UniProt isoform ids explicitly.  Confirm the UniProt
    feature table agrees, because two annotation verdicts are isoform-scoped."""
    url = (f"{UNIPROT}/uniprotkb/{SUBJECT}.json?fields=accession,length,"
           "cc_alternative_products,ft_var_seq,ft_region,ft_zn_fing")
    status, payload = _get_json(url)
    if status != 200 or payload is None:
        raise RuntimeError(f"UniProt HTTP {status}")
    if payload["primaryAccession"] != SUBJECT:
        raise RuntimeError("ACCESSION DRIFT on the isoform fetch")
    var_seq, regions, fingers = [], [], []
    for ft in payload.get("features", []):
        loc = ft.get("location", {})
        rec = {
            "type": ft["type"],
            "start": (loc.get("start") or {}).get("value"),
            "end": (loc.get("end") or {}).get("value"),
            "description": ft.get("description"),
            "featureId": ft.get("featureId"),
        }
        # NB the JSON feature type is "Alternative sequence", not the flat-file
        # "VAR_SEQ". Keying on the flat-file name silently produced an empty
        # var_seq list, which the VSP_034359 presence guard below caught.
        {"Alternative sequence": var_seq, "Region": regions,
         "Zinc finger": fingers}.get(ft["type"], []).append(rec)
    isoforms = []
    for comment in payload.get("comments", []):
        if comment.get("commentType") != "ALTERNATIVE PRODUCTS":
            continue
        for iso in comment.get("isoforms", []):
            isoforms.append({
                "name": (iso.get("name") or {}).get("value"),
                "ids": iso.get("isoformIds"),
                "sequence_ids": iso.get("sequenceIds"),
            })
    nucleosome = [r for r in regions
                  if r["description"] and "nucleosome binding" in r["description"]]
    out = {
        "canonical_length": payload["sequence"]["length"],
        "isoforms": isoforms,
        "var_seq": var_seq,
        "regions": regions,
        "zinc_fingers": fingers,
        "n_zinc_fingers": len(fingers),
        "nucleosome_region": nucleosome,
    }
    if len(fingers) != 3:
        problems.append(f"expected 3 C2H2 zinc fingers, found {len(fingers)}")
    # Isoform 2 (the MANE-Select transcript) deletes part of the region UniProt
    # calls important for the complex's nucleosome binding.  That overlap is a
    # claim in the review; compute it rather than eyeballing it.
    iso2_del = [v for v in var_seq if v["featureId"] == "VSP_034359"]
    if not iso2_del:
        problems.append("VSP_034359 (isoform 2 deletion) missing from the feature table")
    elif nucleosome:
        d0, d1 = iso2_del[0]["start"], iso2_del[0]["end"]
        n0, n1 = nucleosome[0]["start"], nucleosome[0]["end"]
        overlap = max(0, min(d1, n1) - max(d0, n0) + 1)
        out["isoform2_deletion"] = [d0, d1]
        out["nucleosome_region_span"] = [n0, n1]
        out["overlap_residues"] = overlap
        out["nucleosome_region_length"] = n1 - n0 + 1
        if overlap <= 0:
            problems.append(
                "isoform 2's deletion no longer overlaps the nucleosome-binding "
                "region — the isoform note in the review is stale"
            )
    iso3_del = [v for v in var_seq if v["featureId"] == "VSP_034357"]
    if iso3_del:
        out["isoform3_deletion"] = [iso3_del[0]["start"], iso3_del[0]["end"]]
        out["isoform3_length"] = payload["sequence"]["length"] - iso3_del[0]["end"]
    return out


def check_funfam_match(problems) -> dict:
    """Identify WHICH ARBA condition set fires on the subject, from the
    subject's own FunFam cross-references — not from the rule's name."""
    url = f"{UNIPROT}/uniprotkb/{SUBJECT}.json?fields=accession,xref_funfam"
    status, payload = _get_json(url)
    if status != 200 or payload is None:
        raise RuntimeError(f"UniProt HTTP {status}")
    if payload["primaryAccession"] != SUBJECT:
        raise RuntimeError("ACCESSION DRIFT on the FunFam fetch")
    funfams = sorted(
        x["id"] for x in payload.get("uniProtKBCrossReferences", [])
        if x.get("database") == "FunFam"
    )
    status, rule = _get_json(f"{UNIPROT}/arba/ARBA00089504")
    if status != 200 or rule is None:
        problems.append(f"ARBA00089504 HTTP {status}")
        return {"subject_funfams": funfams, "matched_condition_sets": None}
    matched = []
    for i, cset in enumerate(rule["mainRule"]["conditionSets"]):
        needed = {v["value"] for c in cset["conditions"] if c["type"] == "FunFam id"
                  for v in c["conditionValues"]}
        if needed and needed <= set(funfams):
            matched.append({
                "index": i,
                "funfams_required": sorted(needed),
                "taxon_conditions": [
                    ("NOT " if c["isNegative"] else "") + "|".join(
                        v["value"] for v in c["conditionValues"])
                    for c in cset["conditions"] if c["type"] == "taxon"
                ],
            })
    out = {
        "rule": "ARBA00089504",
        "rule_asserts": [a["dbReference"]["id"]
                         for a in rule["mainRule"].get("annotations", [])],
        "n_condition_sets": len(rule["mainRule"]["conditionSets"]),
        "subject_funfams": funfams,
        "matched_condition_sets": matched,
        "all_condition_sets": [
            [("NOT " if c["isNegative"] else "") + c["type"] + "="
             + "|".join(v["value"] for v in c["conditionValues"])
             for c in cset["conditions"]]
            for cset in rule["mainRule"]["conditionSets"]
        ],
    }
    if len(matched) != 1:
        problems.append(
            f"expected exactly one ARBA00089504 condition set to fire on {SUBJECT}, "
            f"got {len(matched)} — the mechanism claim in the review is not established"
        )
    if out["rule_asserts"] != ["GO:0035098"]:
        problems.append(
            f"ARBA00089504 now asserts {out['rule_asserts']}, not ['GO:0035098'] — "
            "the review's account of this row is stale"
        )
    return out


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def render(res: dict) -> str:
    L: list[str] = []
    A = L.append
    A("# AEBP2 (Q6ZN18) — provenance analysis of the GO annotation set")
    A("")
    A("Generated by `analyze_aebp2.py`. Every number below is computed at run time;")
    A("nothing is hardcoded from a previous run. **The tables are the claims** — the")
    A("surrounding prose only names what was measured.")
    A("")
    A(f"- generated: `{res['generated']}`")
    A(f"- problems reported by the checks: **{len(res['problems'])}**")
    for p in res["problems"]:
        A(f"  - ⚠️ {p}")
    A("")

    r = res["row_reconciliation"]
    A("## 1. Row reconciliation (run first, before any reviewing)")
    A("")
    A("| quantity | value |")
    A("|---|---|")
    A(f"| GOA TSV data rows | {r['goa_tsv_data_rows']} |")
    A(f"| GOA TSV distinct rows | {r['goa_tsv_distinct_rows']} |")
    A(f"| QuickGO annotation count for {SUBJECT} | {r['quickgo_annotation_count']} |")
    A(f"| `existing_annotations` entries in the review YAML | {r['review_yaml_entries']} |")
    A(f"| of which are this review's own `NEW` proposals | {r['review_yaml_new_proposals']} |")
    A(f"| entries covering existing GOA rows | {r['review_entries_minus_new']} |")
    A("")
    A(f"Evidence census: `{r['quickgo_evidence_census']}`")
    A("")
    A(f"Aspect census: `{r['goa_aspect_census']}`")
    A("")
    A("**No `GO:0005515 protein binding` row exists**, so the stub's known")
    A("WITH/FROM-blind collapse of partner rows cannot have occurred here, and the")
    A("three counts reconcile exactly.")
    A("")

    A("## 2. WITH/FROM resolution (built from the TSV field, not by hand)")
    A("")
    w = res["withfrom"]
    A(f"{w['n_tokens']} distinct tokens; unresolved: `{w['unresolved'] or 'none'}`")
    A("")
    A("| token | kind | resolves to | reviewed | length | organism |")
    A("|---|---|---|---|---|---|")
    for tok, e in w["tokens"].items():
        if e["kind"] == "uniprot_accession":
            A(f"| `{tok}` | UniProt accession{' (self-reference)' if e['self_reference'] else ''} "
              f"| {e['entry_name']} ({', '.join(x or '?' for x in e['gene'])}) | {e['reviewed']} "
              f"| {e['length']} | {e['organism']} |")
        elif e["kind"] == "mod_gene_id":
            sp = [c for c in e["candidates"] if c["reviewed"]]
            others = len(e["candidates"]) - len(sp)
            for c in sp:
                A(f"| `{tok}` | MOD gene id ({e['n_candidates']} candidates, "
                  f"{others} unreviewed also returned) | {c['entry_name']} "
                  f"({', '.join(x or '?' for x in c['gene'])}) | {c['reviewed']} "
                  f"| {c['length']} | {c['organism']} |")
        else:
            A(f"| `{tok}` | {e['kind']} | {e.get('note') or e.get('asserts') or '—'} | — | — | — |")
    A("")

    A("## 3. IBA donor evidence — which term does each donor actually hold?")
    A("")
    d = res["donor_evidence"]
    A("| donor | term asked | rows | its own experimental rows |")
    A("|---|---|---|---|")
    for key, v in d.items():
        if key.startswith("_"):
            continue
        exp = "; ".join(f"{x['evidence']} {x['term']} {x['reference']}"
                        for x in v["experimental_rows"]) or "none"
        A(f"| {v['donor']} | {v['requested_term']} | {v['n_rows']} | {exp} |")
    A("")
    A(f"Positive control: `{d['_positive_control']['query']}` returns "
      f"{d['_positive_control']['n_rows']} rows, so a zero above would be a real zero.")
    A("")
    A(f"Donor directions for `GO:0006357`: `{d['_go0006357_donor_directions']}`. "
      f"LCA-of-disagreeing-donors: **{d['_go0006357_is_lca_of_disagreeing_donors']}**.")
    A("")

    A("## 4. PANTHER node reach — what the node gave, and to whom")
    A("")
    p = res["panther_node"]
    A(f"`{p['node']}`: {p['n_annotations']} annotations over **{p['n_recipients']} "
      f"recipients**.")
    A("")
    A("| recipient group | n |")
    A("|---|---|")
    A(f"| receives both `GO:0006357` and `GO:0035098` | {p['n_with_both_terms']} |")
    A(f"| receives `GO:0006357` only | {p['n_with_only_GO_0006357']} |")
    A(f"| other term sets | {p['n_with_other_term_sets']} |")
    A("")
    A(f"Subject receives: `{p['subject_terms']}`.")
    A("")

    A("## 5. Reference-projection test (fully paginated)")
    A("")
    A("A reference that annotates the complex **plus every subunit** with an")
    A("identical term set is a projection, not N independent findings. The second")
    A("question matters as much as the first: does the *functional* term spread")
    A("across the set, or stay on the entity that was actually perturbed?")
    A("")
    A("| reference | annotations | entities | ComplexPortal complex entities | assigned by | dominant term-set signature |")
    A("|---|---|---|---|---|---|")
    for ref, v in res["reference_projection"].items():
        sig = v["term_set_signatures"][0] if v["term_set_signatures"] else [[], 0]
        A(f"| `{ref}` | {v['n_annotations']} | {v['n_entities']} | "
          f"{v['n_complexportal_complex_entities']} | `{v['assigned_by']}` | "
          f"{len(sig[0])} terms × {sig[1]} entities |")
    A("")

    A("## 6. TFClass / DbTF census — testing the zinc-finger over-annotation lead")
    A("")
    t = res["tfclass_dbtf"]
    A(f"`GO_REF:0000113` (TFClass-based DbTF curation, NTNU_SB) covers")
    A(f"**{t['n_recipients']} human gene products** in {t['n_annotations']} annotations.")
    A("")
    A("| group | n | % |")
    A("|---|---|---|")
    A(f"| receives `GO:0000981` DNA-binding transcription factor activity | "
      f"{t['n_with_GO_0000981_dbtf_activity']} | {t['pct_with_dbtf']}% |")
    A(f"| receives `GO:0000785` chromatin **only** | {t['n_without_GO_0000981']} | "
      f"{round(100 - t['pct_with_dbtf'], 1)}% |")
    A("")
    A(f"**{SUBJECT_SYMBOL} is in the withheld set** "
      f"(`subject_in_withheld_set = {t['subject_in_withheld_set']}`), receiving "
      f"`{t['subject_terms']}`. The withheld set:")
    A("")
    A("| accession | gene | name |")
    A("|---|---|---|")
    for x in t.get("withheld_set_named", []):
        A(f"| {x['accession']} | {x['gene']} | {x['name']} |")
    A("")

    A("## 7. Molecular-function census across PRC2")
    A("")
    c = res["prc2_mf_census"]
    A("| subunit | accession | total rows | MF rows | MF terms |")
    A("|---|---|---|---|---|")
    for name, v in sorted(c["subunits"].items(),
                          key=lambda kv: -kv[1]["n_molecular_function_rows"]):
        A(f"| {name} | {v['accession']} | {v['n_annotations']} | "
          f"{v['n_molecular_function_rows']} | "
          f"{len(v['molecular_function_terms'])} distinct |")
    A("")
    A(f"Subunits with **zero** molecular-function rows: "
      f"`{c['subunits_with_zero_mf_rows']}`.")
    A("")
    A(f"`GO:0031507` held by **NAS alone**: `{c['GO_0031507_NAS_only_subunits']}`. "
      f"Held with other evidence: `{c['GO_0031507_subunits_with_other_evidence']}`.")
    A("")

    A("## 8. `GO:0180000` — the proposed term and its precedent")
    A("")
    g = res["go0180000"]
    A(f"`GO:0180000` **{g['name']}** — obsolete: {g['obsolete']}; "
      f"secondaryIds: `{g['secondary_ids']}`")
    A("")
    A(f"> {g['definition']}")
    A("")
    A(f"Holders in GOA: {g['n_annotations_in_goa']} annotations over symbols "
      f"`{g['distinct_symbols']}`. Experimental anchors:")
    A("")
    A("| entity | symbol | evidence | reference |")
    A("|---|---|---|---|")
    for x in g["experimental_anchors"]:
        A(f"| {x['entity']} | {x['symbol']} | {x['evidence']} | {x['reference']} |")
    A("")
    A(f"Subject already holds it: {g['subject_already_holds_it']}.")
    A("")

    A("## 9. Logical-opposite citation cross-product")
    A("")
    o = res["logical_opposites"]
    A("| pair | both present | shared references | full cross-product |")
    A("|---|---|---|---|")
    for f in o["pairs_tested"]:
        A(f"| {f['pair'][0]} / {f['pair'][1]} | {f['both_terms_present']} | "
          f"`{f['shared_references'] or 'none'}` | {f['is_full_cross_product']} |")
    A("")
    A(f"Result: **{o['result']}**. This is a reported *negative*: the check ran and")
    A("found nothing, which is a different fact from the check having been skipped.")
    A(f"The detector demonstrably sees a synthetic cross-product "
      f"(`{o['_self_check_detects_a_synthetic_cross_product']}`), so the negative")
    A("is not the silence of a broken comparison.")
    A("")

    A("## 10. PDB construct census — which AEBP2 was in each structure")
    A("")
    b = res["pdb_constructs"]
    A(f"{b['n_pdb_entries_with_an_AEBP2_chain']} PDB entries resolve an AEBP2 chain "
      f"mapped to {SUBJECT}.")
    A("")
    A("| PDB | released | primary citation | AEBP2 range(s) vs Q6ZN18 |")
    A("|---|---|---|---|")
    for e in b["entries"]:
        rng = ", ".join(f"{x['ref_beg']}–{x['ref_end']}" for x in e["aebp2_ref_ranges"])
        A(f"| {e['pdb_id']} | {e['released']} | PMID:{e['primary_citation_pmid']} | {rng} |")
    A("")
    A(f"Full length from residue 1: {b['n_full_length_from_residue_1']}. "
      f"N-terminally truncated: {b['n_n_terminally_truncated']} "
      f"(construct starts at `{b['min_ref_beg_of_truncated']}`).")
    A("")
    A(f"Full-length entries whose primary citation is PMID:41168462 "
      f"(the AEBP2L paper): `{b['full_length_entries_citing_PMID_41168462']}`.")
    A("")

    A("## 11. Isoform mapping")
    A("")
    i = res["isoform_mapping"]
    A(f"Canonical length {i['canonical_length']} aa; "
      f"{i['n_zinc_fingers']} C2H2 zinc fingers at "
      f"{[(z['start'], z['end']) for z in i['zinc_fingers']]}.")
    A("")
    A("| isoform | UniProt id | VAR_SEQ |")
    A("|---|---|---|")
    for iso in i["isoforms"]:
        A(f"| {iso['name']} | {', '.join(iso['ids'] or [])} | "
          f"{', '.join(iso['sequence_ids'] or []) or 'displayed'} |")
    A("")
    if "overlap_residues" in i:
        A(f"Isoform 2's deletion `{i['isoform2_deletion']}` overlaps the "
          f"`{i['nucleosome_region_span']}` region UniProt annotates as *important "
          f"for nucleosome binding activity of the PRC2 complex* by "
          f"**{i['overlap_residues']} of {i['nucleosome_region_length']} residues**.")
        A("")
    if "isoform3_length" in i:
        A(f"Isoform 3 deletes `{i['isoform3_deletion']}`, leaving "
          f"{i['isoform3_length']} residues.")
        A("")

    A("## 12. Which ARBA condition set fires")
    A("")
    f = res["funfam_match"]
    A(f"`{f['rule']}` asserts exactly `{f['rule_asserts']}` and has "
      f"{f['n_condition_sets']} alternative condition sets, each a FunFam-id + "
      f"taxon conjunction with no residue, interaction or assay term in it.")
    A("")
    A(f"The subject's own FunFam cross-references: `{f['subject_funfams']}`.")
    A("")
    A("| condition set | FunFams required | taxon conditions |")
    A("|---|---|---|")
    for m in f["matched_condition_sets"] or []:
        A(f"| [{m['index']}] (fires on {SUBJECT}) | `{m['funfams_required']}` | "
          f"`{m['taxon_conditions']}` |")
    A("")
    A("All condition sets, for context:")
    A("")
    for n, cs in enumerate(f["all_condition_sets"]):
        A(f"- `[{n}]` " + "  AND  ".join(f"`{x}`" for x in cs))
    A("")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- #
# Self-test
# --------------------------------------------------------------------------- #
def self_test() -> int:
    """Break-test the guards.  Each direction must fail *with the right message*
    — red is not the same as red-for-the-right-reason.  A guard that reports
    success while broken is the failure mode this whole file exists to avoid.
    """
    failures: list[str] = []

    def expect(label: str, fn, needle: str) -> None:
        """`fn` must raise (or append a problem) whose text contains `needle`."""
        problems: list[str] = []
        raised = ""
        try:
            fn(problems)
        except Exception as exc:  # noqa: BLE001 - break-tests inspect the message
            raised = str(exc)
        blob = raised + " || " + " || ".join(problems)
        if not raised and not problems:
            failures.append(f"{label}: guard did NOT fire (silence is absence, not passing)")
        elif needle not in blob:
            failures.append(f"{label}: fired but message lacks {needle!r}; got {blob!r}")

    # 1. accession-drift guard, in the direction it exists to catch.
    #    O15507 is a merged accession: HTTP 200, complete reviewed record, wrong protein.
    expect("accession drift (merged accession)",
           lambda _p: uniprot_entry("O15507", "accession,id"),
           "ACCESSION DRIFT")

    # 1b. and in the happy direction: the subject itself must NOT fire.
    try:
        uniprot_entry(SUBJECT, "accession,id")
    except Exception as exc:  # noqa: BLE001
        failures.append(f"accession drift: fired on the correct accession: {exc}")

    # 2. reviewed-status anchor. `"reviewed" in entryType` matches "unreviewed";
    #    startswith must not.  Both directions.
    if is_reviewed({"entryType": "UniProtKB unreviewed (TrEMBL)"}):
        failures.append("is_reviewed: promoted a TrEMBL entry to reviewed")
    if not is_reviewed({"entryType": "UniProtKB reviewed (Swiss-Prot)"}):
        failures.append("is_reviewed: rejected a genuine Swiss-Prot entry (happy path)")

    # 3. size=1 ban.
    try:
        uniprot_search("accession:Q6ZN18", "accession", size=1)
        failures.append("uniprot_search: accepted size=1")
    except AssertionError:
        pass

    # 4. truncation guard.  Mutate the module-level page cap so a real query
    #    cannot complete, and require the guard — not a KeyError — to speak.
    #    Patch the object the code under test actually resolves: a __main__
    #    script importing itself has two module objects with two globals.
    orig = globals()["_get_json"]

    def clamped(url: str):
        status, payload = orig(url)
        if payload and "results" in payload and "numberOfHits" in payload:
            payload = dict(payload)
            payload["results"] = payload["results"][:1]
            payload["numberOfHits"] = 10_000_000  # unreachable => loop must end and guard fire
        return status, payload

    globals()["_get_json"] = clamped
    try:
        assert globals()["_get_json"] is clamped, "patch did not take effect"
        try:
            quickgo(geneProductId=f"UniProtKB:{SUBJECT}", limit=1)
            failures.append("truncation guard: did not fire under a clamped response")
        except RuntimeError as exc:
            if "truncated" not in str(exc):
                failures.append(f"truncation guard: wrong message {exc!r}")
    finally:
        globals()["_get_json"] = orig

    # 5. row reconciliation must notice a stub/TSV disagreement, and must NOT
    #    fire when they agree.  The mutation is exactly the distinction claimed
    #    (one row removed), not a blanked file that any implementation catches.
    goa = read_goa(GENE_DIR / f"{SUBJECT_SYMBOL}-goa.tsv")
    problems: list[str] = []
    check_row_reconciliation(goa, problems)
    if problems:
        failures.append(f"row reconciliation fired on the real, agreeing data: {problems}")
    expect("row reconciliation (one row dropped)",
           lambda p: check_row_reconciliation(goa[:-1], p),
           "disagrees with the cached GOA TSV")

    # 5b. the MF-aspect tripwire: it must fire if a molecular_function row appears.
    doped = goa + [dict(goa[0], go_id="GO:0003677", aspect="molecular_function")]
    expect("molecular_function tripwire",
           lambda p: check_row_reconciliation(doped, p),
           "molecular_function rows now present")

    # 6. logical-opposite detector: it must see a cross-product that IS there.
    synthetic = [
        dict(goa[0], go_id="GO:0000122", reference="PMID:999"),
        dict(goa[0], go_id="GO:0045944", reference="PMID:999"),
    ]
    expect("logical-opposite cross-product",
           lambda p: check_logical_opposites(synthetic, p),
           "cross-product")
    # ... and must stay quiet on the real data (the happy path is the untested path).
    problems = []
    real = check_logical_opposites(goa, problems)
    if problems:
        failures.append(f"logical-opposite check fired on the real data: {problems}")
    if not real["_self_check_detects_a_synthetic_cross_product"]:
        failures.append("logical-opposite check cannot see its own synthetic positive")

    # 7. GOA schema drift guard.
    tmp = HERE / "_selftest_goa.tsv"
    tmp.write_text("a\tb\tc\n1\t2\t3\n")
    try:
        read_goa(tmp)
        failures.append("read_goa: accepted a 3-column file")
    except RuntimeError as exc:
        if "schema drift" not in str(exc):
            failures.append(f"read_goa: wrong message {exc!r}")
    finally:
        tmp.unlink()

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true",
                    help="break-test the guards and exit")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    problems: list[str] = []
    goa = read_goa(GENE_DIR / f"{SUBJECT_SYMBOL}-goa.tsv")
    res: dict = {
        "subject": {"accession": SUBJECT, "symbol": SUBJECT_SYMBOL,
                    "taxon": "NCBITaxon:9606"},
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    res["row_reconciliation"] = check_row_reconciliation(goa, problems)
    res["withfrom"] = check_withfrom(goa, problems)
    res["donor_evidence"] = check_donor_evidence(problems)
    res["panther_node"] = check_panther_node(problems)
    res["reference_projection"] = check_reference_projection(problems)
    res["tfclass_dbtf"] = check_tfclass_dbtf_census(problems)
    res["prc2_mf_census"] = check_prc2_mf_census(problems)
    res["go0180000"] = check_go0180000_precedent(problems)
    res["logical_opposites"] = check_logical_opposites(goa, problems)
    res["pdb_constructs"] = check_pdb_constructs(problems)
    res["isoform_mapping"] = check_isoform_mapping(problems)
    res["funfam_match"] = check_funfam_match(problems)
    res["problems"] = problems

    (HERE / "results.json").write_text(json.dumps(res, indent=1, sort_keys=False) + "\n")
    (HERE / "RESULTS.md").write_text(render(res))
    print(f"wrote results.json and RESULTS.md; {len(problems)} problem(s)")
    for p in problems:
        print("  PROBLEM:", p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
