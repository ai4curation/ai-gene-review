#!/usr/bin/env python3
"""Which GO term is actually true of every member of PANTHER node PTN009058710?

This is a **node**-level audit, not a gene-level one. AADACL2, AADACL3 and AADACL4 each
carry one identical `GO:0016787 hydrolase activity` IBA row (GO_REF:0000033) whose
WITH/FROM field is the same 17 tokens in all three records, so the question "could that
row have carried a more specific term?" has one answer for all three genes and is audited
once here rather than three times. It lives in the AADACL2 folder because AADACL2's own
`RESULTS.md` already tabulates the per-node term assignment for the family; AADACL4's and
AADACL3's reviews cite this file.

The three candidate terms, and what each one requires of a donor:

  GO:0016787 hydrolase activity      -- the donor hydrolyses some bond
  GO:0052689 carboxylic ester hydrolase activity
                                     -- the donor hydrolyses a carboxylic ester bond
  GO:0017171 serine hydrolase activity
                                     -- the donor is a hydrolase AND its nucleophile is
                                        a serine (the GO definition demands a catalytic
                                        triad with a serine nucleophile)

For each donor the script reads the chemistry off two independent sources rather than off
a protein name: the donor's own UniProt EC numbers / CATALYTIC ACTIVITY reactions, and the
donor's own curated GO molecular-function annotations classified by GO ancestry (fetched,
not assumed). The nucleophile identity is read off the donor's own UniProt ACT_SITE
features. Then each candidate term is tested against every donor and the counts are
computed, so "is this term the LCA of its donor set?" is answered by measurement.

Deliberate discipline, each point having cost a previous round:
  * `size=1` is never used on an identifier lookup: a cross-reference that maps to several
    accessions is data, and the script reports every hit with its Swiss-Prot/TrEMBL status
    instead of silently picking one.
  * MGI tokens arrive as `MGI:MGI:1915008`; UniProt's `xref:mgi-` wants the bare number
    (an inner colon returns HTTP 400).
  * `PANTHER:PTN...` is an internal tree node, not a protein, and is reported as such.
  * An unreviewed (TrEMBL) entry's NAME is never used as evidence of what a protein does;
    only its curated GO annotations and annotated features count, and the reviewed status
    is printed next to every claim.
  * The WITH/FROM sets are read out of the committed GOA TSVs, never retyped. Equality across
    the three paralogs is *measured*, not assumed, from two independent sources: the committed
    TSVs, and a per-accession fetch from QuickGO (Q6P093, Q5VUY0, Q5VUY2). Where both exist they
    are cross-checked against each other, and a gene present in neither is a hard error. The
    QuickGO path was introduced while one of the three reviews was still an open PR and its folder
    was absent here; it is retained now that all three are present, because two independent
    sources agreeing is worth more than one.
  * A missing input is never silently converted into an absence: a gene whose TSV is absent is
    named in the output with the reason, and the run aborts unless QuickGO covers it, so no
    gene drops out of the equality test unnoticed.
  * The family node's donor set is the WITH/FROM of the GO:0016020 row PAINT transferred from
    PTN009058713, and is labelled as such: the PANTHER tree is not fetched, so the node's
    membership is not enumerated and no claim is made that it is.
  * The nucleophile call is reported with its basis. For most donors UniProt annotates the
    triad but does not label which member is the nucleophile, so the call rests on the
    N-terminal-most position of a nucleophile-acid-base triad; the GDXG elbow pentapeptide is
    reported alongside it so the reader can check the position independently. A sensitivity
    analysis re-runs the term test with every positionally-inferred nucleophile downgraded to
    undetermined, to show whether the verdict depends on that rule.

Run with:
    uv run --no-project --with requests python audit_node_PTN009058710.py

Outputs `node_PTN009058710.json` next to this file; `NODE_PTN009058710.md` is prose
written from that JSON.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
REPO = HERE
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent

GENES = ["AADACL2", "AADACL3", "AADACL4"]
# The three human paralogs that share this row. Accessions are listed so the WITH/FROM set can be
# measured from QuickGO independently of whether a gene's folder is present in the tree.
PARALOG_ACCESSIONS = {"AADACL2": "Q6P093", "AADACL3": "Q5VUY0", "AADACL4": "Q5VUY2"}
AUDITED_TERM = "GO:0016787"
AUDITED_REF = "GO_REF:0000033"
FAMILY_ROW_TERM = "GO:0016020"  # the other IBA row, transferred from the family node

CANDIDATES = {
    "GO:0016787": "hydrolase activity",
    "GO:0052689": "carboxylic ester hydrolase activity",
    "GO:0017171": "serine hydrolase activity",
}

# InterPro signatures whose membership decides which PANTHER node a donor can sit under.
SIGNATURES = {
    "IPR017157": "Arylacetamide deacetylase family (subfamily-specific)",
    "IPR050300": "GDXG lipolytic enzyme family",
    "IPR013094": "Alpha/beta hydrolase fold-3 (fold-level)",
    "IPR029058": "Alpha/beta hydrolase superfamily fold",
}

UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
UNIPROT_FIELDS = ",".join([
    "accession", "id", "reviewed", "protein_name", "gene_names", "organism_name",
    "ec", "cc_catalytic_activity", "ft_act_site", "cc_function", "sequence",
    "xref_interpro",
])
QUICKGO_ANN = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
QUICKGO_ANC = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{}/ancestors"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

SESSION = requests.Session()
SESSION.headers["Accept"] = "application/json"


def die(msg: str) -> None:
    sys.exit(f"ERROR: {msg}")


def get(url: str, **params):
    r = SESSION.get(url, params=params or None, timeout=120)
    r.raise_for_status()
    return r


# --------------------------------------------------------------------------- inputs


def quickgo_with_from(accession: str) -> list[str]:
    """The audited row's WITH/FROM set for one protein, fetched live from QuickGO.

    This exists so that the "identical across all three paralogs" claim is measured for every
    gene from a source that does not depend on the tree's contents - it was added when one of the
    three had no folder here - and so that, once every folder is present, two independent sources
    have to agree. Returned in GOA token form (db:id), sorted, so it is directly comparable with
    the TSV column.
    """
    payload = get(QUICKGO_ANN, geneProductId=f"UniProtKB:{accession}", goId=AUDITED_TERM,
                  evidenceCode="ECO:0000318", limit=100).json()
    rows = [r for r in payload.get("results", [])
            if r["goId"] == AUDITED_TERM and r["goEvidence"] == "IBA"
            and r["reference"] == AUDITED_REF]
    if len(rows) != 1:
        die(f"QuickGO returned {len(rows)} {AUDITED_TERM} IBA/{AUDITED_REF} rows for "
            f"{accession}; expected exactly 1")
    tokens = [f"{x['db']}:{x['id']}"
              for c in (rows[0].get("withFrom") or []) for x in c["connectedXrefs"]]
    if not tokens:
        die(f"QuickGO returned no WITH/FROM tokens for {accession}")
    return sorted(tokens)


def read_with_from(gene: str) -> dict:
    """Read the WITH/FROM sets straight out of the committed GOA TSV. Never retyped."""
    tsv = REPO / "genes" / "human" / gene / f"{gene}-goa.tsv"
    if not tsv.exists():
        # Not silently an absence: named in the output, printed, and the run aborts later
        # unless QuickGO covers this gene instead.
        print(f"NOTE: {tsv.relative_to(REPO)} is not in this checkout "
              f"(regenerate with `just fetch-gene human {gene}`); "
              f"{gene}'s WITH/FROM set will be measured from QuickGO instead.")
        return {"present": False, "path": str(tsv.relative_to(REPO)),
                "why_absent": "gene folder not present in this checkout",
                "covered_by": "QuickGO"}
    rows = list(csv.DictReader(tsv.open(), delimiter="\t"))
    if not rows:
        die(f"{tsv} is empty; regenerate with `just fetch-gene human {gene}`")
    out = {"present": True, "path": str(tsv.relative_to(REPO))}
    for label, term in (("audited_row", AUDITED_TERM), ("family_row", FAMILY_ROW_TERM)):
        hits = [r for r in rows
                if r["GO TERM"] == term and r["GO EVIDENCE CODE"] == "IBA"
                and r["REFERENCE"] == AUDITED_REF]
        if label == "audited_row" and len(hits) != 1:
            die(f"expected exactly one {term} IBA/{AUDITED_REF} row in {tsv}, found {len(hits)}")
        out[label] = [t for t in (hits[0]["WITH/FROM"].split("|") if hits else []) if t]
    return out


def query_for(token: str) -> str | None:
    db, _, rest = token.partition(":")
    if db == "UniProtKB":
        return f"accession:{rest}"
    if db == "MGI":
        return f"xref:mgi-{rest.split(':')[-1]}"  # bare number: an inner colon -> HTTP 400
    if db == "RGD":
        return f"xref:rgd-{rest}"
    if db == "SGD":
        return f"xref:sgd-{rest}"
    if db == "AGI_LocusCode":
        return f"xref:araport-{rest}"
    if db == "PANTHER":
        return None  # a tree node, not a protein
    die(f"no resolver for WITH/FROM token {token!r}; add one rather than skipping it")


# ------------------------------------------------------------------- GO ancestry


_ANC_CACHE: dict[str, set[str]] = {}


def ancestors(go_id: str) -> set[str]:
    if go_id not in _ANC_CACHE:
        payload = get(QUICKGO_ANC.format(go_id), relations="is_a").json()
        results = payload.get("results") or []
        if not results:
            die(f"QuickGO returned no ancestry for {go_id}")
        _ANC_CACHE[go_id] = set(results[0].get("ancestors") or [go_id])
    return _ANC_CACHE[go_id]


ESTER_ROOT = "GO:0052689"       # carboxylic ester hydrolase activity
AMIDE_ROOT = "GO:0016810"       # acting on C-N (but not peptide) bonds
HYDROLASE_ROOT = "GO:0016787"
LYASE_ROOT = "GO:0016829"


def go_mf_profile(accession: str) -> dict:
    """The donor's own curated MF annotations, classified by fetched GO ancestry."""
    payload = get(QUICKGO_ANN, geneProductId=f"UniProtKB:{accession}",
                  aspect="molecular_function", limit=200).json()
    terms: dict[str, dict] = {}
    for r in payload.get("results", []):
        t = terms.setdefault(r["goId"], {"evidence": set()})
        t["evidence"].add(r["goEvidence"])
    profile = {"terms": {}, "ester": [], "amide": [], "lyase": [], "hydrolase": []}
    for go_id, info in sorted(terms.items()):
        anc = ancestors(go_id)
        ev = sorted(info["evidence"])
        rec = {"evidence": ev,
               "experimental": sorted(set(ev) & EXPERIMENTAL),
               "under_ester": ESTER_ROOT in anc,
               "under_amide": AMIDE_ROOT in anc,
               "under_lyase": LYASE_ROOT in anc,
               "under_hydrolase": HYDROLASE_ROOT in anc}
        profile["terms"][go_id] = rec
        for key, flag in (("ester", "under_ester"), ("amide", "under_amide"),
                          ("lyase", "under_lyase"), ("hydrolase", "under_hydrolase")):
            if rec[flag] and go_id not in (HYDROLASE_ROOT,):
                profile[key].append(go_id)
        if go_id == HYDROLASE_ROOT:
            profile["hydrolase"].append(go_id)
    return profile


# ------------------------------------------------------------------ UniProt entry


def act_sites(entry: dict) -> list[dict]:
    seq = entry.get("sequence", {}).get("value", "")
    out = []
    for f in entry.get("features", []):
        if f.get("type") != "Active site":
            continue
        pos = f["location"]["start"]["value"]
        if not seq or pos > len(seq):
            die(f"ACT_SITE {pos} outside the fetched sequence for {entry['primaryAccession']}")
        out.append({
            "position": pos,
            "residue": seq[pos - 1],
            "description": f.get("description", ""),
            "evidence": sorted({e.get("evidenceCode", "") for e in f.get("evidences", [])}),
        })
    return sorted(out, key=lambda d: d["position"])


def nucleophile(sites: list[dict]) -> dict:
    """The nucleophile of an alpha/beta-hydrolase triad.

    Preference order: an ACT_SITE UniProt itself describes as the nucleophile; else the
    N-terminal-most ACT_SITE, which is the nucleophile-elbow residue in the canonical
    nucleophile-acid-base order of this fold. The order is checked rather than assumed:
    if the two downstream sites are not an acid and a histidine the call is reported as
    undetermined instead of guessed.
    """
    if not sites:
        return {"determined": False, "why": "no ACT_SITE annotated"}
    named = [s for s in sites if "nucleophile" in s["description"].lower()]
    if named:
        s = named[0]
        return {"determined": True, "position": s["position"], "residue": s["residue"],
                "basis": "UniProt describes this ACT_SITE as the nucleophile",
                "evidence": s["evidence"]}
    if len(sites) == 1:
        s = sites[0]
        return {"determined": True, "position": s["position"], "residue": s["residue"],
                "basis": "only one ACT_SITE annotated (partial triad annotation)",
                "evidence": s["evidence"]}
    downstream = [s["residue"] for s in sites[1:]]
    if not (downstream[0] in "DE" and "H" in downstream):
        return {"determined": False,
                "why": f"ACT_SITE order {[s['residue'] for s in sites]} is not "
                       f"nucleophile-acid-base, so the nucleophile cannot be read off position"}
    s = sites[0]
    return {"determined": True, "position": s["position"], "residue": s["residue"],
            "basis": "N-terminal-most of a nucleophile-acid-base triad",
            "evidence": s["evidence"]}


def ec_numbers(entry: dict) -> list[str]:
    desc = entry.get("proteinDescription", {})
    ecs = [x["value"] for x in (desc.get("recommendedName", {}).get("ecNumbers") or [])]
    for c in entry.get("comments", []):
        if c.get("commentType") == "CATALYTIC ACTIVITY":
            for x in (c.get("reaction", {}).get("ecNumbers") or []):
                ecs.append(x["id"])
    return sorted(set(ecs))


def reactions(entry: dict) -> list[str]:
    return [c["reaction"]["name"] for c in entry.get("comments", [])
            if c.get("commentType") == "CATALYTIC ACTIVITY" and c.get("reaction", {}).get("name")]


def fetch_entries(query: str) -> list[dict]:
    """size=5, never 1: an ambiguous cross-reference must surface, not be resolved away."""
    r = get(UNIPROT, query=query, fields=UNIPROT_FIELDS, size=5, format="json")
    total = r.headers.get("x-total-results")
    results = r.json().get("results", [])
    if not results:
        die(f"UniProt returned no entry for query {query!r}")
    return results, total


def describe(entry: dict) -> dict:
    acc = entry["primaryAccession"]
    desc = entry.get("proteinDescription", {})
    name = (desc.get("recommendedName", {}).get("fullName", {}).get("value")
            or next((s.get("fullName", {}).get("value")
                     for s in desc.get("submissionNames", [])), None))
    sites = act_sites(entry)
    nuc = nucleophile(sites)
    seq = entry.get("sequence", {}).get("value", "")
    # The GDXG nucleophile elbow is a G-x-[ST]-x-G pentapeptide centred on the nucleophile, so
    # printing it lets a reader check a positionally-inferred call without trusting the rule.
    if nuc.get("determined") and seq:
        p = nuc["position"]
        nuc["elbow_pentapeptide"] = seq[max(p - 3, 0):p + 2]
    interpro = sorted({x["id"] for x in entry.get("uniProtKBCrossReferences", [])
                       if x.get("database") == "InterPro"})
    reviewed = entry.get("entryType", "").endswith("(Swiss-Prot)")
    return {
        "accession": acc,
        "entry_name": entry.get("uniProtkbId"),
        "reviewed": reviewed,
        "status": "Swiss-Prot" if reviewed else "TrEMBL",
        "protein_name": name,
        "genes": [g.get("geneName", {}).get("value") for g in entry.get("genes", [])
                  if g.get("geneName")],
        "organism": entry.get("organism", {}).get("scientificName"),
        "length": entry.get("sequence", {}).get("length"),
        "ec": ec_numbers(entry),
        "reactions": reactions(entry),
        "act_sites": sites,
        "nucleophile": nuc,
        "interpro_of_interest": {k: (k in interpro) for k in SIGNATURES},
        "go_mf": go_mf_profile(acc),
    }


# ------------------------------------------------------------------ term testing


def truth(donor: dict) -> dict:
    """Test each candidate term against one donor. TRUE / FALSE / UNDETERMINED.

    Chemistry is taken from two independent readings and they must not conflict: the
    donor's own EC numbers, and its own curated GO MF annotations classified by fetched
    ancestry. A protein name is never used.
    """
    ec = donor["ec"]
    go = donor["go_mf"]
    ec_hydrolase = any(e.startswith("3.") for e in ec)
    ec_ester = any(e.startswith("3.1.") for e in ec)
    ec_amide = any(e.startswith("3.5.") for e in ec)
    ec_lyase = any(e.startswith("4.") for e in ec)
    go_ester = bool(go["ester"])
    go_amide = bool(go["amide"])
    go_lyase = bool(go["lyase"])
    go_hydrolase = bool(go["hydrolase"]) or go_ester or go_amide

    verdict = {}

    # GO:0016787 -- does the donor hydrolyse anything?
    if ec_hydrolase or go_hydrolase:
        verdict["GO:0016787"] = "TRUE"
    else:
        verdict["GO:0016787"] = "FALSE" if (ec_lyase or go_lyase) else "UNDETERMINED"

    # GO:0052689 -- does the donor hydrolyse a carboxylic ester?
    if ec_ester or go_ester:
        verdict["GO:0052689"] = "TRUE"
    elif ec_amide or go_amide:
        verdict["GO:0052689"] = "FALSE"
    else:
        verdict["GO:0052689"] = "UNDETERMINED"

    # GO:0017171 -- hydrolase with a serine nucleophile.
    nuc = donor["nucleophile"]
    if not nuc.get("determined"):
        verdict["GO:0017171"] = "UNDETERMINED"
    elif verdict["GO:0016787"] != "TRUE":
        verdict["GO:0017171"] = "UNDETERMINED"
    else:
        verdict["GO:0017171"] = "TRUE" if nuc["residue"] == "S" else "FALSE"

    return {
        "verdict": verdict,
        "ec_flags": {"hydrolase": ec_hydrolase, "ester": ec_ester,
                     "amide": ec_amide, "lyase": ec_lyase},
        "go_flags": {"ester": go["ester"], "amide": go["amide"],
                     "lyase": go["lyase"], "hydrolase": go["hydrolase"]},
        "nucleophile_residue": nuc.get("residue"),
    }


def main() -> int:
    withfrom = {g: read_with_from(g) for g in GENES}
    present = [g for g in GENES if withfrom[g]["present"]]
    if "AADACL2" not in present:
        die("need at least the AADACL2 GOA TSV; run `just fetch-gene human AADACL2`")

    # Equality is measured for every paralog, not only the ones with a folder in this tree:
    # the TSV where it exists, QuickGO for all three, and the two cross-checked against each
    # other wherever both are available.
    from_tsv = {g: withfrom[g]["audited_row"] for g in present}
    from_quickgo = {g: quickgo_with_from(acc) for g, acc in PARALOG_ACCESSIONS.items()}
    for g in present:
        if sorted(from_tsv[g]) != from_quickgo[g]:
            die(f"{g}: committed GOA TSV and live QuickGO disagree on the WITH/FROM set "
                f"({len(from_tsv[g])} vs {len(from_quickgo[g])} tokens); re-run "
                f"`just fetch-gene human {g}`")
    # Every paralog must be covered by at least one source, or the equality test is incomplete.
    # PARALOG_ACCESSIONS is what makes that true today, so assert the coverage rather than
    # testing a condition that cannot fail: if a gene is ever added to GENES without an
    # accession, this fires instead of the gene silently dropping out of the comparison.
    uncovered = [g for g in GENES if g not in present and g not in from_quickgo]
    if uncovered:  # not an assert: python -O strips those, and this promise must not vanish
        die(f"no WITH/FROM source for {uncovered}: neither a committed GOA TSV nor an entry in "
            f"PARALOG_ACCESSIONS, so the equality test would silently omit them")

    reference = from_tsv["AADACL2"]
    identical_genes = sorted(from_quickgo)
    identical = all(from_quickgo[g] == sorted(reference) for g in identical_genes)
    if not identical:
        die("the WITH/FROM sets differ between paralogs; the shared-node premise of this "
            f"audit does not hold: { {g: len(v) for g, v in from_quickgo.items()} }")

    donors: dict[str, dict] = {}
    for token in reference:
        q = query_for(token)
        if q is None:
            donors[token] = {"kind": "panther_node",
                             "note": "PANTHER internal tree node, not a protein"}
            continue
        hits, total = fetch_entries(q)
        described = [describe(e) for e in hits]
        reviewed = [d for d in described if d["reviewed"]]
        # One protein per token: prefer the reviewed entry, but keep every candidate on
        # the record so an ambiguous cross-reference is visible rather than resolved away.
        chosen = reviewed[0] if reviewed else described[0]
        donors[token] = {
            "kind": "protein",
            "query": q,
            "x_total_results": total,
            "n_candidates": len(described),
            "candidates": [{"accession": d["accession"], "status": d["status"],
                            "protein_name": d["protein_name"], "length": d["length"]}
                           for d in described],
            "chose": chosen["accession"],
            "chose_basis": "only reviewed entry" if len(reviewed) == 1
                           else ("first of several reviewed entries" if reviewed
                                 else "no reviewed entry exists; unreviewed used and flagged"),
            "protein": chosen,
            "assessment": truth(chosen),
        }

    proteins = {t: d for t, d in donors.items() if d["kind"] == "protein"}
    counts = {}
    for term in CANDIDATES:
        tally = {"TRUE": [], "FALSE": [], "UNDETERMINED": []}
        for t, d in proteins.items():
            tally[d["assessment"]["verdict"][term]].append(d["protein"]["entry_name"])
        counts[term] = {k: sorted(v) for k, v in tally.items()} | {
            "n_true": len(tally["TRUE"]), "n_false": len(tally["FALSE"]),
            "n_undetermined": len(tally["UNDETERMINED"]),
            "true_of_every_donor": not tally["FALSE"] and not tally["UNDETERMINED"],
            "false_of_no_donor": not tally["FALSE"],
        }

    # Which candidate survives every donor? That is the term the node can license.
    licensed = [t for t in CANDIDATES if counts[t]["false_of_no_donor"]]
    most_specific = None
    for t in ("GO:0017171", "GO:0052689", "GO:0016787"):
        if t in licensed:
            most_specific = t
            break

    # The donor set PAINT cites at the family node, taken from the GO:0016020 row's WITH/FROM.
    # This is not an enumeration of PTN009058713's membership: the PANTHER tree is not fetched,
    # so what is measured is "the donors PAINT cites at that node", which is what a PAINT node
    # annotation rests on. The independent line of evidence that the deep node's blockers lie
    # outside the family is the IPR017157 membership split, which *is* measured per donor.
    family_tokens = withfrom["AADACL2"]["family_row"]
    family_members = sorted(
        {donors[t]["protein"]["entry_name"] for t in family_tokens
         if t in donors and donors[t]["kind"] == "protein"}
    )
    # What the family node's own donors carry for the mechanism term, so the node-move
    # recommendation rests on their evidence codes rather than on a recollection of them.
    family_mechanism = {}
    for t in family_tokens:
        if t.startswith("PANTHER:"):
            continue  # the node itself, not a protein
        d = donors.get(t)
        if d is None:
            die(f"family-row token {t} is not in the audited row's WITH/FROM set, so it was "
                f"never resolved; resolve it explicitly rather than dropping it from the "
                f"family-node tally")
        if d["kind"] != "protein":
            die(f"family-row token {t} did not resolve to a protein")
        pr_ = d["protein"]
        rec = pr_["go_mf"]["terms"].get("GO:0017171")
        family_mechanism[pr_["entry_name"]] = {
            "accession": pr_["accession"],
            "GO:0017171_evidence": rec["evidence"] if rec else [],
            "GO:0017171_experimental": rec["experimental"] if rec else [],
            "in_IPR017157": pr_["interpro_of_interest"]["IPR017157"],
            "nucleophile": pr_["nucleophile"].get("residue"),
        }
    n_family_ida = sum(1 for v in family_mechanism.values() if "IDA" in v["GO:0017171_evidence"])
    blockers = {t: counts[t]["FALSE"] for t in CANDIDATES if counts[t]["FALSE"]}
    signature_split = {
        sig: {
            "in": sorted(d["protein"]["entry_name"] for d in proteins.values()
                         if d["protein"]["interpro_of_interest"][sig]),
            "out": sorted(d["protein"]["entry_name"] for d in proteins.values()
                          if not d["protein"]["interpro_of_interest"][sig]),
        }
        for sig in SIGNATURES
    }

    # Sensitivity: does the verdict depend on the positional nucleophile rule? Re-test the
    # mechanism term with every positionally-inferred nucleophile downgraded to undetermined,
    # and separately with only the single refuting donor downgraded.
    LABELLED = "UniProt describes this ACT_SITE as the nucleophile"
    sensitivity = {}
    for name, downgrade in (
        ("only_the_refuting_donor_undetermined",
         lambda d: d["assessment"]["verdict"]["GO:0017171"] == "FALSE"),
        ("every_positionally_inferred_nucleophile_undetermined",
         lambda d: d["protein"]["nucleophile"].get("basis") != LABELLED),
    ):
        tally = {"TRUE": [], "FALSE": [], "UNDETERMINED": []}
        for d in proteins.values():
            v = "UNDETERMINED" if downgrade(d) else d["assessment"]["verdict"]["GO:0017171"]
            tally[v].append(d["protein"]["entry_name"])
        sensitivity[name] = {
            "term": "GO:0017171",
            "n_true": len(tally["TRUE"]), "n_false": len(tally["FALSE"]),
            "n_undetermined": len(tally["UNDETERMINED"]),
            "true_of_every_donor": not tally["FALSE"] and not tally["UNDETERMINED"],
            "TRUE": sorted(tally["TRUE"]),
        }

    out = {
        "audited": {"term": AUDITED_TERM, "reference": AUDITED_REF,
                    "node": "PANTHER:PTN009058710",
                    "genes_sharing_the_row": identical_genes,
                    "measured_from_committed_tsv": present,
                    "measured_from_quickgo": sorted(from_quickgo),
                    "genes_with_no_tsv_in_this_tree":
                        {g: withfrom[g]["why_absent"] for g in GENES if g not in present},
                    "with_from_identical_across_genes": identical,
                    "n_with_from_tokens": len(reference)},
        "candidate_terms": CANDIDATES,
        "donors": donors,
        "counts": counts,
        "terms_no_donor_refutes": licensed,
        "most_specific_licensed_term": most_specific,
        "blockers_per_term": blockers,
        "family_node": {"node": "PANTHER:PTN009058713", "row": FAMILY_ROW_TERM,
                        "membership_enumerated": False,
                        "what_is_measured": "the donors PAINT cites at this node on the "
                                            f"{FAMILY_ROW_TERM} row, not the node's membership",
                        "with_from": family_tokens, "donors_painter_cites": family_members,
                        "members": family_members,
                        "mechanism_term_support": family_mechanism,
                        "n_members_with_GO_0017171_IDA": n_family_ida},
        "interpro_membership_split": signature_split,
        "sensitivity_GO_0017171": sensitivity,
    }
    (HERE / "node_PTN009058710.json").write_text(json.dumps(out, indent=1, default=list))

    # console summary
    print(f"WITH/FROM identical across {identical_genes}: {identical} "
          f"({len(reference)} tokens); TSV for {present}, QuickGO for {sorted(from_quickgo)}")
    print(f"{len(proteins)} of {len(reference)} tokens resolve to a protein\n")
    hdr = f"{'entry':16s} {'status':11s} {'nuc':5s} {'elbow':6s} {'EC':22s} 787 689 171"
    print(hdr)
    print("-" * len(hdr))
    for t, d in donors.items():
        if d["kind"] != "protein":
            print(f"{t:16s} {'-':11s} {'-':5s} {'-':6s} {'PANTHER tree node':22s}")
            continue
        p, a = d["protein"], d["assessment"]
        nuc = p["nucleophile"]
        nucs = f"{nuc.get('residue','?')}{nuc.get('position','')}" if nuc.get("determined") else "?"
        v = a["verdict"]
        elbow = nuc.get("elbow_pentapeptide", "-")
        print(f"{p['entry_name']:16s} {p['status']:11s} {nucs:5s} {elbow:6s} "
              f"{','.join(p['ec'])[:22]:22s} "
              f"{v['GO:0016787']:3.3s} {v['GO:0052689']:3.3s} {v['GO:0017171']:3.3s}")
    print()
    for term, label in CANDIDATES.items():
        c = counts[term]
        print(f"{term} {label}: TRUE {c['n_true']}, FALSE {c['n_false']}, "
              f"UNDETERMINED {c['n_undetermined']}"
              + (f"  -- refuted by {c['FALSE']}" if c["FALSE"] else ""))
    print(f"\nterms no donor refutes: {licensed}")
    print(f"most specific licensed term: {most_specific}")
    print(f"family node PTN009058713 donors PAINT cites: {family_members}; "
          f"{n_family_ida} of {len(family_mechanism)} carry GO:0017171 by IDA")
    print(f"IPR017157 members among donors: {signature_split['IPR017157']['in']}")
    print("\nGO:0017171 sensitivity to the positional nucleophile rule:")
    for name, r in sensitivity.items():
        print(f"  {name}: TRUE {r['n_true']}, FALSE {r['n_false']}, "
              f"UNDETERMINED {r['n_undetermined']}, "
              f"true_of_every_donor={r['true_of_every_donor']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
