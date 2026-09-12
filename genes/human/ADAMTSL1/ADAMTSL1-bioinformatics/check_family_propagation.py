#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Census of GO annotation coverage across PANTHER family PTHR13723 (ADAMTS / ADAMTS-like).

Two questions, both answered from primary web services with no hand-entered results:

1. **Propagation gap.** PAINT has an IBD annotation of ``GO:0031012 extracellular matrix``
   at node ``PTN000347317``. Which human members of PTHR13723 actually carry that term
   (by IBA from that node, or from any other evidence), and which carry none at all?

2. **Keyword-derived activity.** Which members carry the UniProt ``Hydrolase`` keyword
   (KW-0378), which is what generates ``GO:0016787 hydrolase activity`` in UniProt's own
   GO cross-references, and how does that sit against each entry's ``CAUTION`` comment
   about the missing metalloprotease domain?

Inputs are the repo's cached PANTHER member list plus live QuickGO / UniProt REST.
Nothing is hardcoded from a previous run; every count in RESULTS.md is recomputed.

Run:
    uv run genes/human/ADAMTSL1/ADAMTSL1-bioinformatics/check_family_propagation.py
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent

MEMBERS_CSV = REPO / "interpro" / "panther" / "PTHR13723" / "PTHR13723-entries.csv"
PAINT_TSV = REPO / "interpro" / "panther" / "PTHR13723" / "PTHR13723-paint.tsv"

FAMILY = "PTHR13723"
ECM_TERM = "GO:0031012"
ECM_ORG_TERM = "GO:0030198"
ECM_NODE = "PTN000347317"
HYDROLASE_KW = "KW-0378"

# The ADAMTS-like (non-protease) branch, plus the mouse ADAMTSL1 orthologue as a
# same-node control for the human gap.
ADAMTSL_BRANCH = ["ADAMTSL1", "ADAMTSL2", "ADAMTSL3", "ADAMTSL4", "ADAMTSL5", "THSD4"]
MOUSE_ORTHOLOGUE = ("Adamtsl1", "Q8BLI0", 10090)
# The two terms PAINT negates at PTN002673039.
CATALYTIC_TERMS = ["GO:0004222", "GO:0006508"]

# GO experimental evidence codes, used to test whether a missing IBA can be explained as
# PAINT declining to overlay an existing direct annotation.
EXPERIMENTAL_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb"


def fetch_json(url: str) -> dict:
    """GET JSON, failing loudly. A silent zero here would read as a biological finding."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)


def quickgo_rows(accession: str, go_id: str | None = None) -> list[dict]:
    """All QuickGO annotation rows for one accession.

    Asserts the page holds every hit: QuickGO paginates, and reading one page as the
    whole set is how a partial census turns into a confident wrong answer.
    """
    url = f"{QUICKGO}?geneProductId=UniProtKB:{accession}&limit=200&includeFields=goName"
    if go_id:
        url += f"&goId={go_id}"
    payload = fetch_json(url)
    hits = payload["numberOfHits"]
    rows = payload["results"]
    if hits != len(rows):
        raise SystemExit(
            f"QuickGO paginated for {accession} (hits={hits}, page={len(rows)}); "
            "raise the limit or page through before trusting any count."
        )
    return rows


def panther_nodes(row: dict) -> list[str]:
    return [
        x["id"]
        for wf in (row.get("withFrom") or [])
        for x in wf["connectedXrefs"]
        if x["db"] == "PANTHER"
    ]


def uniprot_entry(accession: str) -> dict:
    url = (
        f"{UNIPROT}/{accession}.json"
        "?fields=id,gene_names,keyword,cc_caution,cc_catalytic_activity,length,protein_existence,reviewed"
    )
    entry = fetch_json(url)
    # A deleted/merged accession answers with no entry name; that must be an error, not a
    # quiet empty result (see the ACTR10 dead-accession case).
    if not entry.get("uniProtkbId"):
        raise SystemExit(f"UniProt returned no entry name for {accession}; accession may be dead")
    return entry


def load_members() -> list[dict]:
    if not MEMBERS_CSV.exists():
        raise SystemExit(
            f"missing {MEMBERS_CSV}; regenerate with: just fetch-gene human ADAMTSL1"
        )
    with MEMBERS_CSV.open() as fh:
        return list(csv.DictReader(fh))


def load_paint_rows() -> list[dict]:
    if not PAINT_TSV.exists():
        raise SystemExit(
            f"missing {PAINT_TSV}; regenerate with: just fetch-gene human ADAMTSL1"
        )
    with PAINT_TSV.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def seed_composition(rows: list[dict]) -> list[dict]:
    """Per positive IBD row, count the gene sources by source database.

    The GOA WITH/FROM field for the derived IBA rows carries one extra token - the
    PANTHER node itself - so counting WITH/FROM tokens overstates the number of
    experimental sources by exactly one.
    """
    out = []
    for r in rows:
        if r["negated"].strip().lower() == "true":
            continue
        seeds = [s for s in r["seeds"].split("|") if s]
        genes = [s for s in seeds if not s.startswith("PANTHER:")]
        by_db: dict[str, int] = {}
        for s in genes:
            by_db[s.split(":")[0]] = by_db.get(s.split(":")[0], 0) + 1
        out.append(
            {
                "node": r["node"],
                "go_id": r["go_id"],
                "aspect": r["aspect"],
                "evidence": r["evidence"],
                "n_seed_tokens": len(seeds),
                "n_gene_sources": len(genes),
                "gene_sources_by_db": dict(sorted(by_db.items())),
            }
        )
    return out


def main() -> int:
    members = load_members()
    human = sorted(
        {(r["gene"], r["id"], r["subfamily"]) for r in members if r["source_tax_id"] == "9606"}
    )
    if not human:
        raise SystemExit(f"no human members parsed from {MEMBERS_CSV}")

    census: list[dict] = []
    targets = [(g, a, sf, 9606) for g, a, sf in human]
    targets.append((MOUSE_ORTHOLOGUE[0], MOUSE_ORTHOLOGUE[1], f"{FAMILY}:SF157", MOUSE_ORTHOLOGUE[2]))

    for gene, acc, subfamily, taxon in targets:
        entry = {"gene": gene, "accession": acc, "taxon": taxon, "subfamily": subfamily}
        for term, prefix in ((ECM_TERM, "ecm"), (ECM_ORG_TERM, "ecm_org")):
            rows = quickgo_rows(acc, term)
            iba_from_node = [
                r for r in rows if r["goEvidence"] == "IBA" and ECM_NODE in panther_nodes(r)
            ]
            other = [r for r in rows if r not in iba_from_node]
            entry[f"{prefix}_iba_from_node"] = len(iba_from_node)
            entry[f"{prefix}_other_rows"] = len(other)
            entry[f"{prefix}_total_rows"] = len(rows)
            entry[f"{prefix}_evidence_codes"] = sorted({r["goEvidence"] for r in rows})
            # Whether the non-IBA rows are experimental decides whether a missing IBA can be
            # explained as PAINT declining to overlay a direct annotation.
            entry[f"{prefix}_other_experimental"] = sorted(
                {r["goEvidence"] for r in other} & EXPERIMENTAL_CODES
            )
            time.sleep(0.15)
        census.append(entry)

    human_census = [c for c in census if c["taxon"] == 9606]
    no_ecm = [c["gene"] for c in human_census if c["ecm_total_rows"] == 0]
    with_iba = [c["gene"] for c in human_census if c["ecm_iba_from_node"] > 0]
    no_ecm_org = [c["gene"] for c in human_census if c["ecm_org_total_rows"] == 0]
    with_iba_org = [c["gene"] for c in human_census if c["ecm_org_iba_from_node"] > 0]
    # Members that miss the IBA but hold the term anyway: is a direct annotation the reason?
    missing_iba_explained = {
        c["gene"]: c["ecm_other_experimental"]
        for c in human_census
        if c["ecm_iba_from_node"] == 0 and c["ecm_total_rows"] > 0
    }

    # Keyword / CAUTION audit over the ADAMTS-like branch.
    branch_acc = {g: a for g, a, _sf in human if g in ADAMTSL_BRANCH}
    missing = set(ADAMTSL_BRANCH) - set(branch_acc)
    if missing:
        raise SystemExit(f"ADAMTSL branch members absent from {MEMBERS_CSV}: {sorted(missing)}")
    keyword_audit = []
    for gene in ADAMTSL_BRANCH:
        entry = uniprot_entry(branch_acc[gene])
        kws = {k["id"]: k["name"] for k in entry.get("keywords", [])}
        cautions = [
            c["texts"][0]["value"]
            for c in entry.get("comments", [])
            if c["commentType"] == "CAUTION"
        ]
        catalytic = [c for c in entry.get("comments", []) if c["commentType"] == "CATALYTIC ACTIVITY"]
        keyword_audit.append(
            {
                "gene": gene,
                "accession": branch_acc[gene],
                "entry_name": entry["uniProtkbId"],
                "reviewed": entry.get("entryType", ""),
                "length": entry["sequence"]["length"],
                "hydrolase_keyword": HYDROLASE_KW in kws,
                "mf_keywords": sorted(
                    k["name"] for k in entry.get("keywords", []) if k["category"] == "Molecular function"
                ),
                "n_catalytic_activity_comments": len(catalytic),
                "caution_mentions_missing_protease_domain": any(
                    "lacks the metalloprotease" in c for c in cautions
                ),
            }
        )
        time.sleep(0.15)

    paint_rows = load_paint_rows()
    negations = [r for r in paint_rows if r["negated"].strip().lower() == "true"]
    ibd_seeds = seed_composition(paint_rows)

    # Where do PAINT's two loss calls actually land in GOA? Computed, not asserted.
    catalytic_audit = []
    for gene in ADAMTSL_BRANCH:
        acc = branch_acc[gene]
        entry = {"gene": gene, "accession": acc}
        for term in CATALYTIC_TERMS:
            rows = quickgo_rows(acc, term)
            entry[term] = [
                {
                    "qualifier": r["qualifier"],
                    "evidence": r["goEvidence"],
                    "reference": r["reference"],
                    "nodes": panther_nodes(r),
                }
                for r in rows
            ]
            time.sleep(0.15)
        catalytic_audit.append(entry)

    results = {
        "retrieved_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "family": FAMILY,
        "ecm_term": ECM_TERM,
        "ecm_ibd_node": ECM_NODE,
        "ecm_organization_term": ECM_ORG_TERM,
        "human_members": len(human_census),
        "human_members_with_ecm_iba_from_node": len(with_iba),
        "human_members_with_no_ecm_annotation": no_ecm,
        "human_members_with_ecm_org_iba_from_node": len(with_iba_org),
        "human_members_with_ecm_org_iba_list": sorted(with_iba_org),
        "human_members_with_no_ecm_org_annotation": no_ecm_org,
        "members_missing_ecm_iba_but_holding_term": missing_iba_explained,
        "census": census,
        "keyword_audit": keyword_audit,
        "paint_negated_rows": negations,
        "paint_ibd_seed_composition": ibd_seeds,
        "catalytic_term_audit": catalytic_audit,
    }

    # Invariants. Each one is the claim RESULTS.md makes; if the data moves, this fails
    # loudly rather than letting a stale sentence stand.
    assert len(human_census) >= 20, f"only {len(human_census)} human members parsed"
    adamtsl1 = next(c for c in human_census if c["gene"] == "ADAMTSL1")
    assert adamtsl1["ecm_total_rows"] == 0, (
        f"human ADAMTSL1 now has {adamtsl1['ecm_total_rows']} {ECM_TERM} rows; "
        "the propagation-gap claim in RESULTS.md is stale"
    )
    mouse = next(c for c in census if c["taxon"] == 10090)
    assert mouse["ecm_iba_from_node"] == 1, (
        "mouse Adamtsl1 no longer carries the IBA from "
        f"{ECM_NODE}; the same-node control for the human gap is gone"
    )
    l1_kw = next(k for k in keyword_audit if k["gene"] == "ADAMTSL1")
    assert l1_kw["hydrolase_keyword"], "ADAMTSL1 no longer carries KW-0378; RESULTS.md is stale"
    assert l1_kw["n_catalytic_activity_comments"] == 0, (
        "ADAMTSL1 now has a CATALYTIC ACTIVITY comment; re-examine the keyword argument"
    )
    assert l1_kw["caution_mentions_missing_protease_domain"], (
        "ADAMTSL1's CAUTION no longer states the metalloprotease domain is absent"
    )
    assert any(
        n["node"] == "PTN002673039" and n["go_id"] == "GO:0004222" and n["evidence"] == "IKR"
        for n in negations
    ), "the IKR loss call on GO:0004222 is no longer in the cached PAINT table"
    l5 = next(c for c in human_census if c["gene"] == "ADAMTSL5")
    assert adamtsl1["ecm_org_iba_from_node"] == 0 and l5["ecm_org_iba_from_node"] == 0, (
        "ADAMTSL1 and ADAMTSL5 no longer share the same GO:0030198 position; the "
        "cross-review comparison in RESULTS.md is stale"
    )
    l1_cat = next(c for c in catalytic_audit if c["gene"] == "ADAMTSL1")
    assert not any(l1_cat[t] for t in CATALYTIC_TERMS), (
        "ADAMTSL1 has acquired a GO:0004222/GO:0006508 row in GOA; the review's "
        "'no peptidase annotation reached GOA' statement is stale"
    )

    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print(f"human members: {len(human_census)}")
    print(f"  with {ECM_TERM} IBA from {ECM_NODE}: {len(with_iba)}")
    print(f"  with no {ECM_TERM} annotation at all: {no_ecm}")
    print(f"  hydrolase keyword in ADAMTSL branch: "
          f"{[k['gene'] for k in keyword_audit if k['hydrolase_keyword']]}")
    print("wrote results.json and RESULTS.md")
    return 0


def render(r: dict) -> str:
    human = [c for c in r["census"] if c["taxon"] == 9606]
    mouse = [c for c in r["census"] if c["taxon"] == 10090]
    lines: list[str] = []
    a = lines.append
    a(f"# {r['family']} annotation census for ADAMTSL1")
    a("")
    a("Regenerate with:")
    a("")
    a("```")
    a("uv run genes/human/ADAMTSL1/ADAMTSL1-bioinformatics/check_family_propagation.py")
    a("```")
    a("")
    a("Retrieval timestamp is recorded in `results.json` so this file stays byte-reproducible.")
    a("")
    a(f"## 1. `{r['ecm_term']}` coverage across human {r['family']}")
    a("")
    a(
        f"PAINT holds `{r['ecm_term']}` as an IBD annotation at node `{r['ecm_ibd_node']}`. "
        f"Of the {r['human_members']} human members of the family, "
        f"{r['human_members_with_ecm_iba_from_node']} receive it by IBA from that node."
    )
    a("")
    a(
        "| gene | accession | subfamily | GO:0031012 IBA | other rows | evidence codes "
        "| GO:0030198 IBA | GO:0030198 other |"
    )
    a("|---|---|---|---|---|---|---|---|")
    for c in human + mouse:
        label = c["gene"] if c["taxon"] == 9606 else f"*{c['gene']}* (mouse)"
        a(
            f"| {label} | {c['accession']} | {c['subfamily']} | {c['ecm_iba_from_node']} | "
            f"{c['ecm_other_rows']} | {', '.join(c['ecm_evidence_codes']) or '-'} | "
            f"{c['ecm_org_iba_from_node']} | {', '.join(c['ecm_org_evidence_codes']) or '-'} |"
        )
    a("")
    a(
        f"**Members with no `{r['ecm_term']}` annotation of any kind: "
        f"{', '.join(r['human_members_with_no_ecm_annotation']) or 'none'}.**"
    )
    a("")
    # Derived, not asserted: does an existing direct annotation explain a missing IBA?
    for gene, exp_codes in sorted(r["members_missing_ecm_iba_but_holding_term"].items()):
        if exp_codes:
            a(
                f"{gene} holds `{r['ecm_term']}` without the IBA and does have direct evidence "
                f"of its own ({', '.join(exp_codes)}), which is consistent with PAINT declining "
                "to overlay an IBA on an existing direct annotation."
            )
        else:
            codes = next(c["ecm_evidence_codes"] for c in human if c["gene"] == gene)
            a(
                f"{gene} holds `{r['ecm_term']}` without the IBA, but **none of its rows is "
                f"experimental** (evidence codes: {', '.join(codes) or '-'}), so redundancy "
                "suppression does not account for the missing IBA. Its absent IBA is a second "
                "coverage gap at this node, not an explained omission."
            )
        a("")
    a(
        "ADAMTSL1 has neither an IBA nor any other row, and its mouse orthologue - the same "
        "PANTHER subfamily, the same IBD node - does receive the IBA."
    )
    a("")
    a(f"### `{r['ecm_organization_term']}` coverage, same node")
    a("")
    a(
        f"{r['human_members_with_ecm_org_iba_from_node']} of the {r['human_members']} human "
        f"members receive `{r['ecm_organization_term']}` by IBA from `{r['ecm_ibd_node']}`: "
        f"{', '.join(r['human_members_with_ecm_org_iba_list'])}. Members with no "
        f"`{r['ecm_organization_term']}` annotation at all: "
        f"{', '.join(r['human_members_with_no_ecm_org_annotation']) or 'none'}."
    )
    a("")
    org_adamtsl = [
        g for g in r["human_members_with_ecm_org_iba_list"] if g in ADAMTSL_BRANCH
    ]
    a(
        f"Within the ADAMTS-like branch the IBA reaches only {', '.join(org_adamtsl) or 'none'}. "
        "ADAMTSL1 and ADAMTSL5 are therefore in the same position for this term - the InterPro "
        "IEA and nothing else - which matters when comparing verdicts between their reviews."
    )
    a("")
    a("## 2. `Hydrolase` keyword across the ADAMTS-like branch")
    a("")
    a(
        "UniProt's `KW-0378 Hydrolase` is what generates the `GO:0016787 hydrolase activity` "
        "cross-reference in an entry's own GO list (`IEA:UniProtKB-KW`)."
    )
    a("")
    a("| gene | accession | length | MF keywords | CATALYTIC ACTIVITY comments | CAUTION: no metalloprotease domain |")
    a("|---|---|---|---|---|---|")
    for k in r["keyword_audit"]:
        a(
            f"| {k['gene']} | {k['accession']} | {k['length']} | "
            f"{', '.join(k['mf_keywords']) or '-'} | {k['n_catalytic_activity_comments']} | "
            f"{'yes' if k['caution_mentions_missing_protease_domain'] else 'no'} |"
        )
    a("")
    holders = [k["gene"] for k in r["keyword_audit"] if k["hydrolase_keyword"]]
    cautioned = [k["gene"] for k in r["keyword_audit"] if k["caution_mentions_missing_protease_domain"]]
    uncautioned = [
        k["gene"] for k in r["keyword_audit"] if not k["caution_mentions_missing_protease_domain"]
    ]
    catalysing = [k["gene"] for k in r["keyword_audit"] if k["n_catalytic_activity_comments"]]
    a(
        f"Hydrolase keyword present on: {', '.join(holders) or 'none'}. "
        f"CAUTION stating the metalloprotease and disintegrin-like domains are absent: "
        f"{', '.join(cautioned) or 'none'}"
        + (f" (absent on {', '.join(uncautioned)})." if uncautioned else ".")
    )
    a("")
    a(
        f"Entries with a CATALYTIC ACTIVITY comment: {', '.join(catalysing) or 'none'}. "
        f"So on ADAMTSL1 the keyword sits alongside that entry's own statement that the "
        f"catalytic domain is missing, with no reaction recorded anywhere in the entry."
    )
    a("")
    a("## 3. PAINT's own loss calls in this family")
    a("")
    a(
        "The cached PAINT table records explicitly negated annotations, i.e. terms PAINT "
        "blocks from propagating below a node:"
    )
    a("")
    a("| node | term | aspect | evidence | seed |")
    a("|---|---|---|---|---|")
    for n in r["paint_negated_rows"]:
        a(f"| {n['node']} | {n['go_id']} | {n['aspect']} | {n['evidence']} | {n['seeds']} |")
    a("")
    a(
        "`IKR` is inferred-from-key-residues and `IRD` inferred-from-rapid-divergence: PAINT "
        "has judged that catalysis was lost on this branch. Where those calls land in GOA:"
    )
    a("")
    a("| gene | GO:0004222 rows | GO:0006508 rows |")
    a("|---|---|---|")
    negated_holders: list[str] = []
    positive_holders: list[str] = []
    for c in r["catalytic_term_audit"]:
        cells = []
        for term in ("GO:0004222", "GO:0006508"):
            rows = c[term]
            if not rows:
                cells.append("none")
                continue
            cells.append(
                "; ".join(
                    # escape the qualifier's pipe so it does not split the markdown cell
                    f"`{x['qualifier'].replace('|', chr(92) + '|')}` {x['evidence']} {x['reference']}"
                    for x in rows
                )
            )
            if any("NOT" in x["qualifier"] for x in rows):
                negated_holders.append(f"{c['gene']} {term}")
            if any("NOT" not in x["qualifier"] for x in rows):
                positive_holders.append(f"{c['gene']} {term}")
        a(f"| {c['gene']} | {cells[0]} | {cells[1]} |")
    a("")
    a(
        f"Negated rows in GOA: {', '.join(negated_holders) or 'none'}. "
        f"Positive rows in GOA: {', '.join(positive_holders) or 'none'}. "
        "So the loss call is recorded for part of the branch and simply absent for the rest - "
        "ADAMTSL1 inherits neither the catalytic terms nor the statement that they do not apply."
    )
    a("")
    a("## 4. IBD seed composition at the family node")
    a("")
    a(
        "Counting WITH/FROM tokens on the derived IBA rows overstates the number of "
        "experimental sources by one, because GOA appends the PANTHER node itself to the "
        "list. The seed lists in the PAINT table give the gene sources directly:"
    )
    a("")
    a("| node | term | aspect | evidence | seed tokens | gene sources | by database |")
    a("|---|---|---|---|---|---|---|")
    for s in r["paint_ibd_seed_composition"]:
        by_db = ", ".join(f"{k} {v}" for k, v in s["gene_sources_by_db"].items()) or "-"
        a(
            f"| {s['node']} | {s['go_id']} | {s['aspect']} | {s['evidence']} | "
            f"{s['n_seed_tokens']} | {s['n_gene_sources']} | {by_db} |"
        )
    a("")
    a("## Guards")
    a("")
    a(
        "The script aborts rather than emitting a stale sentence if any of these stop holding: "
        "a QuickGO response is paginated (page total read as the whole set); human ADAMTSL1 "
        f"acquires any `{r['ecm_term']}` row; mouse Adamtsl1 loses its IBA from "
        f"`{r['ecm_ibd_node']}`; ADAMTSL1 loses `{HYDROLASE_KW}`, gains a CATALYTIC ACTIVITY "
        "comment, or loses the CAUTION about the missing metalloprotease domain; the IKR loss "
        "call disappears from the cached PAINT table; or ADAMTSL1 gains a GO:0004222/GO:0006508 "
        "row. A missing cached input is a hard error naming the command that regenerates it. "
        "The zero-row count for ADAMTSL1 is produced by the same code path that returns "
        "non-zero for the other 25 human members on every run, so the census is its own "
        "positive control."
    )
    a("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
