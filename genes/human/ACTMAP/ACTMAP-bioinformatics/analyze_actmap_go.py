#!/usr/bin/env python3
"""Audit ACTMAP's GO record: WITH/FROM resolution, reciprocal-propagation check,
peptidase-branch definition audit, and a census of GO:0004239 usage.

Standard library only (urllib + csv + json), so the analysis is reproducible with
no dependency resolution:

    python3 analyze_actmap_go.py            # writes results.json + RESULTS.md

Every claim in RESULTS.md is computed here; nothing is hardcoded. Missing input
files are a hard error naming the command that regenerates them.
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent

GOA_TSV = HERE.parent / "ACTMAP-goa.tsv"
UNIPROT_TXT = HERE.parent / "ACTMAP-uniprot.txt"
PANTHER_CSV = REPO / "interpro" / "panther" / "PTHR28631" / "PTHR28631-entries.csv"

# The mouse orthologue, whose curation state bears on what the human record can
# receive by orthology.
MOUSE_ORTHOLOG = "J3QPC3"

TARGET = "Q5BKX5"  # human ACTMAP
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
UNIPROT = "https://rest.uniprot.org/uniprotkb"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# Terms whose definitions and is_a closures decide the branch question.
TERMS_OF_INTEREST = [
    "GO:0004239",  # initiator methionyl aminopeptidase activity (annotated to ACTMAP)
    "GO:0070005",  # cysteine-type aminopeptidase activity (annotated to ACTMAP)
    "GO:0004177",  # aminopeptidase activity
    "GO:0008238",  # exopeptidase activity
    "GO:0008242",  # omega peptidase activity
    "GO:0016920",  # pyroglutamyl-peptidase activity (the blocked-N-terminus precedent)
    "GO:0008234",  # cysteine-type peptidase activity
    "GO:0016485",  # protein processing
]

# Model organisms used for the GO:0004239 census. A full census is impractical
# (>44k annotations, overwhelmingly IEA); these five taxa give a well-defined,
# reproducible sample that includes every reviewed ACTMAP-family member.
CENSUS_TAXA = ["9606", "10090", "7227", "7955", "559292"]


def assert_complete_page(data: dict, url: str) -> dict:
    """QuickGO caps a response at `limit`, so a count taken from numberOfHits and a
    breakdown taken from results can silently disagree once the cap is hit. Fail loudly
    instead, naming the fix - the same discipline as the WITH/FROM token assertion.
    """
    total, got = data.get("numberOfHits"), len(data.get("results", []))
    if total is not None and got != total:
        raise SystemExit(
            f"TRUNCATED RESPONSE: {url}\n  numberOfHits={total} but only {got} results "
            "returned; raise limit or paginate before trusting any per-product breakdown"
        )
    return data


def get_json(url: str, tries: int = 4) -> dict:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.load(fh)
        except Exception as exc:  # network flake: retry with backoff
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last}")


def require(path: Path, fix: str) -> None:
    if not path.exists():
        raise SystemExit(f"MISSING INPUT: {path}\n  regenerate with: {fix}")


# --------------------------------------------------------------------------- #
# 1. GOA rows and their WITH/FROM tokens
# --------------------------------------------------------------------------- #
def read_goa() -> list[dict]:
    require(GOA_TSV, "just fetch-gene human ACTMAP")
    rows = []
    with GOA_TSV.open() as fh:
        for rec in csv.DictReader(fh, delimiter="\t"):
            rows.append(
                {
                    "term": rec["GO TERM"],
                    "term_label": rec["GO NAME"],
                    "aspect": rec["GO ASPECT"],
                    "evidence": rec["GO EVIDENCE CODE"],
                    "reference": rec["REFERENCE"],
                    "qualifier": rec["QUALIFIER"],
                    "assigned_by": rec["ASSIGNED BY"],
                    "with_from": [t for t in rec["WITH/FROM"].split("|") if t],
                }
            )
    if not rows:
        raise SystemExit(f"{GOA_TSV} parsed to zero rows - schema change?")
    return rows


def resolve_uniprot(acc: str) -> dict:
    """Resolve an accession, fetching size=2 so a multi-hit is visible rather than
    silently collapsed, and asserting the entry actually is the one requested
    (a merged/deleted accession otherwise returns a different protein's name)."""
    fields = "accession,id,protein_name,gene_names,organism_name,reviewed,length"
    url = f"{UNIPROT}/search?query=accession:{acc}&fields={fields}&format=json&size=2"
    data = get_json(url)
    hits = data.get("results", [])
    out = {"requested": acc, "n_hits": len(hits), "candidates": []}
    for r in hits:
        desc = r.get("proteinDescription", {})
        name = (desc.get("recommendedName") or {}).get("fullName", {}).get("value")
        if not name:
            subs = desc.get("submissionNames") or []
            name = subs[0]["fullName"]["value"] if subs else None
        out["candidates"].append(
            {
                "accession": r.get("primaryAccession"),
                "entry_name": r.get("uniProtkbId"),
                "protein_name": name,
                "genes": [g.get("geneName", {}).get("value") for g in r.get("genes", [])],
                "organism": r.get("organism", {}).get("scientificName"),
                "reviewed": r.get("entryType"),
                "length": r.get("sequence", {}).get("length"),
            }
        )
    exact = [c for c in out["candidates"] if c["accession"] == acc]
    out["live"] = bool(exact)
    if not out["live"]:
        out["warning"] = (
            f"accession {acc} did not return itself - dead/merged entry, "
            "or the query matched a different protein"
        )
    return out


def source_evidence(acc: str, go_id: str) -> dict:
    """What evidence does this source itself carry for the propagated term, and
    does its own WITH/FROM point back at the target (reciprocal circularity)?"""
    url = (
        f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{acc}&goId={go_id}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    data = assert_complete_page(get_json(url), url)
    anns, points_back = [], []
    for r in data.get("results", []):
        wf = []
        for w in r.get("withFrom") or []:
            for x in w.get("connectedXrefs") or []:
                wf.append(f"{x['db']}:{x['id']}")
        anns.append(
            {
                "go_id": r.get("goId"),
                "evidence": r.get("goEvidence"),
                "reference": r.get("reference"),
                "assigned_by": r.get("assignedBy"),
                "with_from": wf,
            }
        )
        if any(t.endswith(TARGET) for t in wf):
            points_back.append(r.get("reference"))
    return {
        "n_annotations": data.get("numberOfHits"),
        "annotations": anns,
        "has_own_experimental": sorted(
            {a["evidence"] for a in anns if a["evidence"] in EXPERIMENTAL}
        ),
        "experimental_references": sorted(
            {a["reference"] for a in anns if a["evidence"] in EXPERIMENTAL}
        ),
        "reciprocal_references": sorted(set(points_back)),
    }


# --------------------------------------------------------------------------- #
# 2. Ontology-branch audit
# --------------------------------------------------------------------------- #
def term_record(go_id: str) -> dict:
    complete = get_json(f"{QUICKGO}/ontology/go/terms/{go_id}/complete")["results"][0]
    anc = get_json(
        f"{QUICKGO}/ontology/go/terms/{go_id}/ancestors?relations=is_a,part_of"
    )["results"][0]
    return {
        "id": go_id,
        "name": complete.get("name"),
        "definition": (complete.get("definition") or {}).get("text"),
        "is_obsolete": complete.get("isObsolete"),
        "secondary_ids": complete.get("secondaryIds"),
        "comment": complete.get("comment"),
        "ec_xrefs": sorted(
            {x["dbId"] for x in (complete.get("xRefs") or []) if x.get("dbCode") == "EC"}
        ),
        "ancestors": sorted(anc.get("ancestors") or []),
    }


# --------------------------------------------------------------------------- #
# 3. GO:0004239 census across model organisms
# --------------------------------------------------------------------------- #
def actmap_family_accessions() -> dict[str, str]:
    require(PANTHER_CSV, "just fetch-gene human ACTMAP")
    fam = {}
    with PANTHER_CSV.open() as fh:
        for rec in csv.DictReader(fh):
            fam[rec["id"]] = rec["gene"]
    if not fam:
        raise SystemExit(f"{PANTHER_CSV} parsed to zero rows - schema change?")
    return fam


def family_wide_usage(go_id: str, family: dict[str, str]) -> dict:
    """Ask every reviewed family member directly whether it carries the term.

    The taxon-restricted census below cannot see family members outside its five
    taxa (bovine and Xenopus, here), so it UNDERSTATES how many family members
    would be corrected by a term fix. This per-member query is the honest count.
    """
    members = {}
    for acc, gene in sorted(family.items()):
        url = (
            f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{acc}"
            f"&goId={go_id}&goUsage=exact&limit=100"
        )
        data = assert_complete_page(get_json(url), url)
        res = data.get("results", [])
        members[acc] = {
            "gene": gene,
            "carries_term": bool(res),
            "evidence": sorted({r.get("goEvidence") for r in res if r.get("goEvidence")}),
            "references": sorted({r.get("reference") for r in res if r.get("reference")}),
        }
    carrying = [a for a, v in members.items() if v["carries_term"]]
    return {
        "go_id": go_id,
        "n_reviewed_members": len(members),
        "n_carrying_term": len(carrying),
        "members": members,
    }


def census(go_id: str, family: dict[str, str]) -> dict:
    url = (
        f"{QUICKGO}/annotation/search?goId={go_id}&goUsage=exact"
        f"&taxonId={','.join(CENSUS_TAXA)}&limit=200"
    )
    data = assert_complete_page(get_json(url), url)
    # Deliberately NOT wrapped in assert_complete_page: this call asks for limit=1
    # purely to read numberOfHits, so results is expected to be shorter than the total
    # and the guard would (correctly) abort. No breakdown is derived from it.
    total_all_taxa = get_json(
        f"{QUICKGO}/annotation/search?goId={go_id}&goUsage=exact&limit=1"
    ).get("numberOfHits")
    products: dict[str, dict] = {}
    for r in data.get("results", []):
        acc = (r.get("geneProductId") or "").split(":")[-1]
        entry = products.setdefault(
            acc,
            {
                "symbol": r.get("symbol"),
                "taxon": r.get("taxonId"),
                "evidence": set(),
                "references": set(),
            },
        )
        entry["evidence"].add(r.get("goEvidence"))
        entry["references"].add(r.get("reference"))

    family_symbols = {s.lower() for s in family.values()}
    in_family, others = {}, {}
    for acc, rec in products.items():
        sym = (rec["symbol"] or "").lower()
        bucket = in_family if (acc in family or sym in family_symbols) else others
        bucket[acc] = {
            "symbol": rec["symbol"],
            "taxon": rec["taxon"],
            "evidence": sorted(e for e in rec["evidence"] if e),
            "references": sorted(x for x in rec["references"] if x),
        }
    other_symbols = sorted({(v["symbol"] or "?").upper() for v in others.values()})
    return {
        "go_id": go_id,
        "annotations_all_taxa": total_all_taxa,
        "census_taxa": CENSUS_TAXA,
        "annotations_in_census_taxa": data.get("numberOfHits"),
        "n_gene_products_in_census": len(products),
        "actmap_family_products": in_family,
        "n_actmap_family_products": len(in_family),
        "other_products": others,
        "n_other_products": len(others),
        "other_symbols": other_symbols,
    }


# --------------------------------------------------------------------------- #
# 3b. Is the substrate-specific process term in the right branch, and who else
#     carries it? Both questions decide whether ACTMAP can use GO:0030047.
# --------------------------------------------------------------------------- #
BRANCH_PROBES = {
    "GO:0006508": "proteolysis",
    "GO:0036211": "protein modification process",
    "GO:0030036": "actin cytoskeleton organization",
    "GO:0051604": "protein maturation",
}
NAA80 = "Q93015"          # the enzyme performing the NEXT step of actin maturation
FLY_ORTHOLOG = "Q9VCE8"   # CG33108, whose FlyBase ISS explains the human GO:0070005 assigner


def process_branch_audit() -> dict:
    out = {"terms": {}, "probes": BRANCH_PROBES}
    for go_id in ("GO:0016485", "GO:0030047", "GO:0007014"):
        anc = get_json(
            f"{QUICKGO}/ontology/go/terms/{go_id}/ancestors?relations=is_a,part_of"
        )["results"][0]
        ancestors = sorted(anc.get("ancestors") or [])
        out["terms"][go_id] = {
            "name": anc.get("name"),
            "ancestors": ancestors,
            "under": {probe: probe in ancestors for probe in BRANCH_PROBES},
        }
    a, b = out["terms"]["GO:0016485"]["under"], out["terms"]["GO:0030047"]["under"]
    out["proteolysis_and_modification_are_disjoint"] = (
        a["GO:0006508"] and not a["GO:0036211"] and b["GO:0036211"] and not b["GO:0006508"]
    )
    naa80_url = (
        f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{NAA80}"
        "&goId=GO:0030047&goUsage=exact&limit=100"
    )
    naa80 = assert_complete_page(get_json(naa80_url), naa80_url)
    out["naa80_GO_0030047"] = {
        "accession": NAA80,
        "n": naa80.get("numberOfHits"),
        "rows": [
            {"evidence": r.get("goEvidence"), "reference": r.get("reference"),
             "assigned_by": r.get("assignedBy")}
            for r in naa80.get("results", [])
        ],
    }
    fly_url = f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{FLY_ORTHOLOG}&limit=100"
    fly = assert_complete_page(get_json(fly_url), fly_url)
    out["fly_ortholog"] = {
        "accession": FLY_ORTHOLOG,
        "n": fly.get("numberOfHits"),
        "rows": [
            {
                "go_id": r.get("goId"),
                "evidence": r.get("goEvidence"),
                "reference": r.get("reference"),
                "assigned_by": r.get("assignedBy"),
                "with_from": [
                    f"{x['db']}:{x['id']}"
                    for w in (r.get("withFrom") or [])
                    for x in (w.get("connectedXrefs") or [])
                ],
            }
            for r in fly.get("results", [])
        ],
    }
    return out


# --------------------------------------------------------------------------- #
# 4. Curation state of the orthologue and of the evolutionary-model pipeline
# --------------------------------------------------------------------------- #
def curation_state() -> dict:
    url = f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{MOUSE_ORTHOLOG}&limit=200"
    data = assert_complete_page(get_json(url), url)
    rows = [
        {
            "go_id": r.get("goId"),
            "aspect": r.get("goAspect"),
            "evidence": r.get("goEvidence"),
            "reference": r.get("reference"),
            "assigned_by": r.get("assignedBy"),
        }
        for r in data.get("results", [])
    ]
    nd = [r for r in rows if r["evidence"] == "ND"]

    require(UNIPROT_TXT, "just fetch-gene human ACTMAP")
    pan_go = [
        line.strip()
        for line in UNIPROT_TXT.read_text().splitlines()
        if line.startswith("DR   PAN-GO;")
    ]
    return {
        "mouse_ortholog": MOUSE_ORTHOLOG,
        "mouse_n_annotations": data.get("numberOfHits"),
        "mouse_annotations": rows,
        "mouse_nd_rows": nd,
        "mouse_has_root_nd_in_all_aspects": sorted({r["aspect"] for r in nd})
        == ["biological_process", "cellular_component", "molecular_function"],
        "human_pan_go_dr_lines": pan_go,
    }


# --------------------------------------------------------------------------- #
def main() -> int:
    goa = read_goa()
    tokens: list[str] = []
    for row in goa:
        tokens.extend(row["with_from"])
    # Build the source set FROM the GOA field, never by hand.
    uniprot_tokens = [t for t in tokens if t.startswith("UniProtKB:")]
    accs = sorted({t.split(":", 1)[1] for t in uniprot_tokens})

    resolved = {a: resolve_uniprot(a) for a in accs}
    for a, r in resolved.items():
        if not r["live"]:
            print(f"WARNING: {r['warning']}", file=sys.stderr)

    # Per-row source evidence, keyed on the row's own term.
    propagated = []
    for row in goa:
        if not row["with_from"]:
            continue
        for tok in row["with_from"]:
            if not tok.startswith("UniProtKB:"):
                propagated.append({"row_term": row["term"], "source": tok, "resolvable": False})
                continue
            acc = tok.split(":", 1)[1]
            propagated.append(
                {
                    "row_term": row["term"],
                    "row_evidence": row["evidence"],
                    "row_reference": row["reference"],
                    "source": tok,
                    "resolvable": True,
                    "resolved": resolved[acc],
                    "own_evidence_for_term": source_evidence(acc, row["term"]),
                }
            )

    # Invariant: every WITH/FROM token in GOA is accounted for exactly once.
    n_tokens_in_goa = sum(len(r["with_from"]) for r in goa)
    assert len(propagated) == n_tokens_in_goa, (
        f"source list drifted: {len(propagated)} entries vs {n_tokens_in_goa} GOA tokens"
    )

    terms = {t: term_record(t) for t in TERMS_OF_INTEREST}
    family = actmap_family_accessions()
    cen = census("GO:0004239", family)
    fam_wide = family_wide_usage("GO:0004239", family)

    # The branch question, computed rather than asserted.
    exo = terms["GO:0008238"]
    branch = {
        "exopeptidase_definition": exo["definition"],
        "exopeptidase_requires_free_terminus": "free N-terminal amino group"
        in (exo["definition"] or ""),
        "annotated_mf_terms_under_exopeptidase": {
            t: ("GO:0008238" in terms[t]["ancestors"])
            for t in ("GO:0004239", "GO:0070005")
        },
        "omega_peptidase_under_exopeptidase": "GO:0008238" in terms["GO:0008242"]["ancestors"],
        "pyroglutamyl_precedent_parents": {
            "under_omega_peptidase": "GO:0008242" in terms["GO:0016920"]["ancestors"],
            "under_cysteine_type_peptidase": "GO:0008234" in terms["GO:0016920"]["ancestors"],
            "under_aminopeptidase": "GO:0004177" in terms["GO:0016920"]["ancestors"],
        },
    }

    results = {
        "target": TARGET,
        "goa_rows": goa,
        "n_goa_rows": len(goa),
        "with_from_tokens": tokens,
        "propagated_rows": propagated,
        "terms": terms,
        "branch_audit": branch,
        "census_GO_0004239": cen,
        "family_wide_GO_0004239": fam_wide,
        "panther_family": {"id": "PTHR28631", "reviewed_members": family},
        "curation_state": curation_state(),
        "process_branch_audit": process_branch_audit(),
    }
    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print(f"wrote {HERE/'results.json'} and {HERE/'RESULTS.md'}")
    return 0


def render(r: dict) -> str:
    L: list[str] = []
    add = L.append
    add("# ACTMAP GO-record audit\n")
    add(
        "Generated by `analyze_actmap_go.py` (standard library only). "
        "Re-run to regenerate; nothing below is hardcoded.\n"
    )

    add("\n## 1. GOA rows and WITH/FROM resolution\n")
    add(f"`{r['n_goa_rows']}` GOA rows; "
        f"`{len(r['with_from_tokens'])}` WITH/FROM tokens in total.\n")
    add("\n| term | label | evidence | reference | assigned by | WITH/FROM |")
    add("|---|---|---|---|---|---|")
    sep = " \\| "
    for row in r["goa_rows"]:
        wf = sep.join(row["with_from"]) or "-"
        add(
            f"| {row['term']} | {row['term_label']} | {row['evidence']} | "
            f"{row['reference']} | {row['assigned_by']} | {wf} |"
        )

    add("\n### Resolved sources\n")
    seen: set[str] = set()
    for tok in r["with_from_tokens"]:
        if not tok.startswith("UniProtKB:") and tok not in seen:
            seen.add(tok)
            add(f"- `{tok}` - not a UniProt accession; not resolved here.")
    for p in r["propagated_rows"]:
        if not p.get("resolvable"):
            continue
        res = p["resolved"]
        key = res["requested"]
        if key in seen:
            continue
        seen.add(key)
        for c in res["candidates"]:
            add(
                f"- `{res['requested']}` -> **{c['accession']}** ({c['entry_name']}), "
                f"{c['protein_name']}, gene `{c['genes']}`, {c['organism']}, "
                f"{c['length']} aa, {c['reviewed']}; hits returned for the query: "
                f"{res['n_hits']}; requested accession returned itself: {res['live']}"
            )

    add("\n### Does each source carry its own evidence for the term it donated?\n")
    add("| row term | source | source's own evidence for that term | its WITH/FROM points back at the target? |")
    add("|---|---|---|---|")
    for p in r["propagated_rows"]:
        if not p.get("resolvable"):
            continue
        own = p["own_evidence_for_term"]
        ev = ", ".join(
            f"{a['evidence']} ({a['reference']}, {a['assigned_by']})" for a in own["annotations"]
        )
        back = ", ".join(own["reciprocal_references"]) or "no"
        add(f"| {p['row_term']} | `{p['source']}` | {ev} | {back} |")

    b = r["branch_audit"]
    add("\n## 2. Which peptidase branch do ACTMAP's MF terms sit in?\n")
    add(f"`GO:0008238` exopeptidase activity definition:\n\n> {b['exopeptidase_definition']}\n")
    add(
        f"- definition contains the clause \"free N-terminal amino group\": "
        f"**{b['exopeptidase_requires_free_terminus']}**"
    )
    for t, under in b["annotated_mf_terms_under_exopeptidase"].items():
        add(f"- `{t}` ({r['terms'][t]['name']}) is under `GO:0008238`: **{under}**")
    add(
        f"- `GO:0008242` omega peptidase activity is under `GO:0008238`: "
        f"**{b['omega_peptidase_under_exopeptidase']}**"
    )
    add("\nPrecedent for a single-residue-releasing enzyme acting on a *blocked* N-terminus:")
    for k, v in b["pyroglutamyl_precedent_parents"].items():
        add(f"- `GO:0016920` pyroglutamyl-peptidase activity {k.replace('_', ' ')}: **{v}**")

    add("\n### Term records\n")
    for t, rec in r["terms"].items():
        add(f"- **{t}** {rec['name']} - EC xrefs `{rec['ec_xrefs'] or '-'}`; "
            f"obsolete: {rec['is_obsolete']}; comment: {rec['comment'] or '-'}")
        add(f"  - def: {rec['definition']}")

    c = r["census_GO_0004239"]
    add(f"\n## 3. Census of `{c['go_id']}` usage\n")
    add(
        f"- annotations to `{c['go_id']}` across all taxa: **{c['annotations_all_taxa']}** "
        "(overwhelmingly IEA, so a full census is impractical)"
    )
    add(
        f"- restricted to taxa `{','.join(c['census_taxa'])}`: "
        f"**{c['annotations_in_census_taxa']}** annotations on "
        f"**{c['n_gene_products_in_census']}** gene products"
    )
    add(
        f"- of these, **{c['n_actmap_family_products']}** are ACTMAP-family "
        f"(PANTHER PTHR28631) and **{c['n_other_products']}** are not"
    )
    add(f"- non-ACTMAP symbols carrying the term: `{', '.join(c['other_symbols'])}`")
    add("\n| ACTMAP-family product | symbol | taxon | evidence | references |")
    add("|---|---|---|---|---|")
    for acc, v in sorted(c["actmap_family_products"].items()):
        add(
            f"| {acc} | {v['symbol']} | {v['taxon']} | {', '.join(v['evidence'])} | "
            f"{', '.join(v['references'])} |"
        )

    fw = r["family_wide_GO_0004239"]
    add(
        f"\n### Family-wide usage of `{fw['go_id']}` (not taxon-restricted)\n"
    )
    add(
        f"The census above is limited to five taxa and therefore **understates** the family. "
        f"Asking each reviewed PTHR28631 member directly: "
        f"**{fw['n_carrying_term']} of {fw['n_reviewed_members']}** carry the term.\n"
    )
    add("| accession | gene | carries GO:0004239 | evidence | references |")
    add("|---|---|---|---|---|")
    for acc, v in fw["members"].items():
        add(
            f"| {acc} | {v['gene']} | {v['carries_term']} | "
            f"{', '.join(v['evidence']) or '-'} | {', '.join(v['references']) or '-'} |"
        )

    pb = r["process_branch_audit"]
    add("\n## 3b. Can ACTMAP use a substrate-specific *process* term?\n")
    add("| term | name | " + " | ".join(f"under {k}" for k in pb["probes"]) + " |")
    add("|---|---|" + "---|" * len(pb["probes"]))
    for go_id, v in pb["terms"].items():
        cells = " | ".join(str(v["under"][k]) for k in pb["probes"])
        add(f"| {go_id} | {v['name']} | {cells} |")
    # Build the clause from the flags, so the narrative cannot contradict its own
    # number if QuickGO ever changes.
    def clause(go_id: str) -> str:
        u = pb["terms"][go_id]["under"]
        parts = [
            ("" if u[k] else "NOT ") + f"under `{k}`"
            for k in ("GO:0006508", "GO:0036211")
        ]
        return f"`{go_id} {pb['terms'][go_id]['name']}` is " + " and is ".join(parts)

    disjoint = pb["proteolysis_and_modification_are_disjoint"]
    add(
        f"\n- **GO keeps proteolysis and protein modification in disjoint branches: "
        f"{disjoint}** - {clause('GO:0016485')}, while {clause('GO:0030047')}."
        + ("" if disjoint else " NOTE: the disjointness test did NOT hold on this run, so any"
           " argument resting on it must be re-examined.")
    )
    n8 = pb["naa80_GO_0030047"]
    add(
        f"- NAA80 (`{n8['accession']}`) carries `GO:0030047` **{n8['n']}** time(s): "
        + ", ".join(f"{x['evidence']} ({x['reference']}, {x['assigned_by']})" for x in n8["rows"])
        + " - but NAA80's reaction is an acetyl *transfer*, an additive modification, so the "
        "precedent does not extend to peptide-bond hydrolysis."
    )
    fo = pb["fly_ortholog"]
    add(f"- Drosophila ortholog `{fo['accession']}` (CG33108) carries {fo['n']} annotation(s):")
    for x in fo["rows"]:
        add(
            f"  - {x['go_id']} {x['evidence']} ({x['reference']}) assigned by "
            f"**{x['assigned_by']}**, WITH/FROM `{', '.join(x['with_from']) or '-'}`"
        )

    cs = r["curation_state"]
    add("\n## 4. Curation state of the orthologue and of the evolutionary-model pipeline\n")
    add(
        f"- mouse orthologue `{cs['mouse_ortholog']}` carries "
        f"**{cs['mouse_n_annotations']}** GO annotations"
    )
    add(
        f"- of which **{len(cs['mouse_nd_rows'])}** are root `ND` (no data) rows: "
        + ", ".join(f"`{x['go_id']}` ({x['reference']}, {x['assigned_by']})" for x in cs["mouse_nd_rows"])
    )
    add(
        f"- root `ND` present in all three aspects: "
        f"**{cs['mouse_has_root_nd_in_all_aspects']}** - i.e. the model organism database has "
        "not curated the gene, so the mouse knockout phenotype is unrepresented and the human "
        "record has nothing to receive by orthology beyond the UniProt annotations"
    )
    for line in cs["human_pan_go_dr_lines"]:
        add(f"- human UniProt cross-reference: `{line}`")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
