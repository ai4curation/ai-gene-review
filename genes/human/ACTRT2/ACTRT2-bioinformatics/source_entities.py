"""Build and then VERIFY the `propagation_review.source_entities` blocks of the ACTRT2 review.

Hand-maintained WITH/FROM lists have drifted on most genes in this campaign that tried them, and
the drift is invisible to eye inspection. So this script is the single source of truth for those
blocks:

  uv run python source_entities.py emit    -> print the YAML blocks to paste into the review
  uv run python source_entities.py verify  -> fail loudly if the committed review has drifted

`verify` is the part that matters. It asserts, for every IBA row of ACTRT2-goa.tsv:

  * the review has a propagation_review.source_entities list for that row;
  * the set of source_id values equals the set of WITH/FROM tokens EXACTLY - no missing token,
    no invented one;
  * the counts agree.

The invariant relating what is found to what is checked is stated explicitly and both directions
are asserted, so a future edit that drops or adds a token fails here rather than shipping.

Source status assignment is a judgement, but a *rule*, applied uniformly rather than per row:
a donor SUPPORTS_TRANSFER only if it gives ACTRT2 an ortholog-strength inference for the term it
donated. For GO:0005200 no donor does: resolving all ten seeds gives conventional actins, the
Arp2/3 nucleator pair and the two yeast dynactin ARPs, with no ARP-T of any kind, so every source
on that row is SUPPORTS_SOURCE_BUT_NOT_TARGET and the row is generalised to the parent. (An earlier
version of this rule granted SUPPORTS_TRANSFER to the two dynactin ARPs on the ground that their
non-polymerising structural route resembles ACTRT2's; that was withdrawn - see the comment on
TRANSFERABLE_ROUTE.) For GO:0015629 the node itself supports the transfer, because the term is the
genuine LCA of its heterogeneous donor set.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "ACTRT2-goa.tsv"
REVIEW = GENE_DIR / "ACTRT2-ai-review.yaml"
RESULTS = HERE / "results.json"

# No donor of GO:0005200 supports the term for ACTRT2, so this mapping is empty by design.
#
# An earlier version of this file marked the two yeast dynactin ARPs as SUPPORTS_TRANSFER, on the
# ground that their route to the term (a non-polymerising structural subunit of an actin-like
# assembly) is the route ACTRT2 also has. That was withdrawn after the merged ACTRT3 review, which
# holds the byte-identical row, made the decisive point: the merged ACTR10 ACCEPT of this row rests
# on yeast ARP10 being ACTR10's OWN ORTHOLOG inside the seed set. Resolving all ten seeds confirms
# there is no ARP-T donor of any kind, so ACTRT2 has no ortholog-strength donor and an analogous
# route in a different family is not the same thing as one.
TRANSFERABLE_ROUTE: dict[str, str] = {}

# Kept as commentary because the distinction is real even though it no longer changes any status.
ANALOGOUS_BUT_NOT_ORTHOLOGOUS = {
    "SGD:S000001171": "S. cerevisiae ARP1/centractin (P38696, Swiss-Prot; IDA). Builds the "
    "dynactin minifilament rather than F-actin, so its route to the term does not require "
    "polymerisation - the closest analogue in the seed set, but a dynactin ARP, not an ARP-T.",
    "SGD:S000002513": "S. cerevisiae ARP10 (Q04549, Swiss-Prot; IPI x3). The true ARP11 ortholog, "
    "which caps rather than extends the dynactin filament. It is the donor that earns ACTR10 its "
    "ACCEPT of this same row, and it is an ortholog of ACTR10, not of ACTRT2.",
}

NODE_COMMENTS = {
    "PTN000940351": "PANTHER internal tree node, not a protein. The single node from which "
    "GO:0005200 propagates anywhere in PTHR11937; the same term is explicitly negated as an IRD "
    "at eight other nodes of the family, and this clade has not yet been given a decision. At the "
    "nearest adjudicated neighbour, PTN008986528, PAINT substituted the parent GO:0005198 on the "
    "same day, which is the level this review adopts.",
    "PTN002631484": "PANTHER internal tree node, not a protein. A deep node donating GO:0015629 "
    "to 18 human genes spanning 33.7 to 100 per cent identity to beta-actin, so the generic term "
    "it carries is the true LCA of a heterogeneous donor set.",
}


def load_goa() -> list[dict]:
    if not GOA_TSV.exists():
        raise FileNotFoundError(f"missing {GOA_TSV}\n  regenerate with: just fetch-gene human ACTRT2")
    with GOA_TSV.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise RuntimeError(f"{GOA_TSV} has no annotation rows")
    return rows


def iba_rows(goa: list[dict]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for r in goa:
        if r["GO EVIDENCE CODE"] != "IBA":
            continue
        tokens = [t for t in r["WITH/FROM"].split("|") if t]
        if r["GO TERM"] in out:
            raise RuntimeError(
                f"{r['GO TERM']} appears on more than one IBA row; the one-row-per-term "
                "assumption in this script no longer holds"
            )
        out[r["GO TERM"]] = tokens
    if not out:
        raise RuntimeError("no IBA rows found; the GOA TSV column layout may have changed")
    return out


def resolutions() -> dict:
    """Token -> resolved label, from the analysis output rather than from memory."""
    if not RESULTS.exists():
        raise FileNotFoundError(
            f"missing {RESULTS}\n  regenerate with: uv run python analyze_actrt2.py"
        )
    data = json.loads(RESULTS.read_text())
    out: dict[str, dict] = {}
    for go_id, rec in data["iba_sources"].items():
        for tok in rec["tokens"]:
            hits = tok["hits"]
            if not hits:
                out.setdefault(tok["token"], {"label": tok["note"], "experimental": None})
                continue
            # Prefer the reviewed entry when a cross-reference is ambiguous, and say so. The
            # arithmetic below used to be `len(hits) - len(reviewed)`, which silently reported an
            # INACTIVE (merged or deleted) hit as a TrEMBL entry, and `hits[0]` could pick a dead
            # entry as the primary one. This is the fourth site in this review where the same
            # inactive-entry class had to be handled after being fixed elsewhere, so the categories
            # are now counted explicitly rather than inferred by subtraction.
            reviewed = [h for h in hits if h["reviewed"] == "Swiss-Prot"]
            unreviewed = [h for h in hits if h["reviewed"] == "TrEMBL"]
            inactive = [h for h in hits if h["reviewed"] == "INACTIVE"]
            live = reviewed + unreviewed
            if not live:
                out.setdefault(tok["token"], {
                    "label": f"{len(inactive)} candidate entries, all INACTIVE (merged or deleted); "
                             "no live entry to describe",
                    "experimental": None,
                })
                continue
            primary = live[0]
            # Count the OTHER entries, not all of them. A first version counted every unreviewed hit,
            # so a token with a single TrEMBL hit described itself as "also maps to 1 TrEMBL entries".
            # Caught by diffing the freshly emitted blocks against the committed ones, which is the
            # only reason a label regression like this is visible at all.
            others = [h for h in hits if h is not primary]
            parts = []
            n_trembl = sum(1 for h in others if h["reviewed"] == "TrEMBL")
            n_inactive = sum(1 for h in others if h["reviewed"] == "INACTIVE")
            if n_trembl:
                parts.append(f"{n_trembl} TrEMBL {'entry' if n_trembl == 1 else 'entries'}")
            if n_inactive:
                parts.append(f"{n_inactive} INACTIVE {'entry' if n_inactive == 1 else 'entries'}")
            extra = f"; cross-reference also maps to {' and '.join(parts)}" if parts else ""
            genes = "/".join(primary["genes"]) or primary["name"]
            label = (
                f"{primary['organism']} {genes} ({primary['accession']}, {primary['reviewed']}"
                f"{extra})"
            )
            ev = tok.get("own_evidence") or {}
            out.setdefault(tok["token"], {"label": label, "experimental": ev.get("has_experimental")})
    return out


def build(go_id: str, tokens: list[str], res: dict) -> list[dict]:
    entries = []
    for tok in tokens:
        if tok.startswith("PANTHER:"):
            node = tok.split(":", 1)[1]
            entries.append(
                {
                    "source_id": tok,
                    "source_label": f"PANTHER ancestral node {node}",
                    # For GO:0005200 the node supports the general parent for this clade, not the
                    # specific child, so it does not support the transfer as published.
                    "source_status": "SUPPORTS_SOURCE_BUT_NOT_TARGET"
                    if go_id == "GO:0005200" else "SUPPORTS_TRANSFER",
                    "comment": NODE_COMMENTS[node],
                }
            )
            continue
        info = res[tok]
        entry = {
            "source_id": tok,
            "source_label": info["label"],
        }
        if go_id == "GO:0005200" and tok in TRANSFERABLE_ROUTE:
            entry["source_status"] = "SUPPORTS_TRANSFER"
            entry["comment"] = TRANSFERABLE_ROUTE[tok]
        else:
            entry["source_status"] = "SUPPORTS_SOURCE_BUT_NOT_TARGET"
            if go_id == "GO:0005200":
                entry["comment"] = ANALOGOUS_BUT_NOT_ORTHOLOGOUS.get(tok) or (
                    "Carries its own experimental evidence for the term, earned through filament "
                    "formation or nucleation; the protomer-interface measurement shows that route "
                    "is not available to ACTRT2, and no ARP-T donor is present in the seed set to "
                    "supply an ortholog-strength inference instead."
                )
            else:
                entry["comment"] = (
                    "Carries its own experimental evidence for GO:0015629, but ACTRT2's evidenced "
                    "compartment is GO:0033011 perinuclear theca, which is a GO:0005856 descendant "
                    "and not a GO:0015629 descendant."
                )
        if info["experimental"] is False:
            entry["comment"] = (
                "No experimental evidence of its own for the donated term. " + entry["comment"]
            )
        entries.append(entry)
    assert len(entries) == len(tokens), (
        f"built {len(entries)} entries from {len(tokens)} tokens on {go_id}"
    )
    return entries


def emit() -> None:
    goa = load_goa()
    res = resolutions()
    for go_id, tokens in iba_rows(goa).items():
        print(f"# ---- {go_id}: {len(tokens)} WITH/FROM tokens ----")
        print(yaml.dump({"source_entities": build(go_id, tokens, res)}, sort_keys=False, width=98))


def verify() -> int:
    goa = load_goa()
    rows = iba_rows(goa)
    review = yaml.safe_load(REVIEW.read_text())
    problems: list[str] = []
    checked = 0
    for ann in review["existing_annotations"]:
        if ann.get("evidence_type") != "IBA":
            continue
        go_id = ann["term"]["id"]
        if go_id not in rows:
            problems.append(f"{go_id}: IBA row in the review is not an IBA row in the GOA TSV")
            continue
        pr = (ann.get("review") or {}).get("propagation_review") or {}
        entities = pr.get("source_entities")
        if not entities:
            problems.append(f"{go_id}: no propagation_review.source_entities")
            continue
        got = [e["source_id"] for e in entities]
        want = rows[go_id]
        if len(got) != len(set(got)):
            problems.append(f"{go_id}: duplicated source_id values in the review")
        missing = sorted(set(want) - set(got))
        extra = sorted(set(got) - set(want))
        if missing:
            problems.append(f"{go_id}: {len(missing)} GOA tokens absent from the review: {missing}")
        if extra:
            problems.append(f"{go_id}: {len(extra)} review sources absent from GOA: {extra}")
        if len(got) != len(want):
            problems.append(f"{go_id}: {len(got)} sources vs {len(want)} GOA tokens")
        checked += 1
    # The invariant: every IBA row in GOA must have been checked. Re-running a detector after an
    # edit only proves the edit did not leave behind what the detector looks for, so assert that
    # the number of rows examined equals the number that exist.
    if checked != len(rows):
        problems.append(
            f"checked {checked} IBA rows but the GOA TSV has {len(rows)}; the review is missing an "
            "IBA row entirely, which a per-row check cannot see"
        )
    if problems:
        print("SOURCE ENTITY DRIFT:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"OK: {checked} IBA rows, source_entities match the GOA WITH/FROM field exactly")
    for go_id, tokens in rows.items():
        print(f"  {go_id}: {len(tokens)} tokens")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if mode == "emit":
        emit()
    elif mode == "verify":
        raise SystemExit(verify())
    else:
        raise SystemExit(f"unknown mode {mode!r}; use emit or verify")
