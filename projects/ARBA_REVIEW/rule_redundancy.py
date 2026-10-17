#!/usr/bin/env python
"""Redundancy among ARBA GO rules, and a review of the generic rules.

Reads every ARBA rule from UniProt (``rest.uniprot.org/arba/stream``, cached
under ``.cache/arba/``) and analyses the rules that assert a GO term. Each such
rule asserts exactly one term from one or more OR'd condition sets; a condition
set is an AND of signatures (InterPro, CATH FunFam, PANTHER), optional taxon
restrictions and optional negative conditions.

Three measures:

1. **Same-term redundancy.** Rules that assert the same GO term, and whether
   their condition sets share signatures or are exact duplicates. (In the
   current release ARBA keeps one rule per term, so this is zero; it is kept as
   a check.)
2. **Subsumption.** A condition set of rule R (term T) is *covered* when another
   rule asserts a strict descendant of T (is_a/part_of) from a condition set
   whose signatures are a subset of R's, with no negative conditions and either
   no taxon restriction or the same one. Every protein R's set matches then also
   receives the more specific term, so R adds nothing there. This is a
   conservative, structural test: it ignores coverage that only shows up in
   protein data. UniProt keeps only the most specific ARBA term on a protein,
   so a covered set never emits an annotation; the script tests this on seeded
   random samples of fully covered, partly covered and all rules, counting
   each rule's annotations in QuickGO.
3. **Gene-side check.** For the generic rules (term with more than 200 GO
   descendants, at least 10 annotations in gene reviews), how often the reviewed
   gene already carries a strict descendant of the rule's term, from another ARBA
   rule or from any source, and how reviewers judged the rule's rows.
   UniProt-wide annotation counts come from QuickGO (``withFrom=ARBA:...``).

Writes ``RULE_REDUNDANCY.md`` (summary and generic-rule review table) and
``rule_redundancy.tsv`` (per-rule measures for every GO rule).

Usage::

    uv run python projects/ARBA_REVIEW/rule_redundancy.py
"""

from __future__ import annotations

import collections
import csv
import glob
import json
import random
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

import requests

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from gene_side_failures import descendant_counts  # noqa: E402

CACHE = Path(".cache/arba/arba_rules.json")
COUNTS_CACHE = Path(".cache/arba/quickgo_rule_counts.json")
ARBA_URL = "https://rest.uniprot.org/arba/stream?query=*&format=json"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PREDS = ("rdfs:subClassOf", "BFO:0000050")
GENERIC_DESCENDANTS = 200
GENERIC_MIN_ROWS = 10
SAMPLE = 60
SEED = 7


@dataclass(frozen=True)
class ConditionSet:
    """Signatures (ANDed), taxon restrictions and negative conditions of one set."""

    signatures: frozenset[str]
    taxa: frozenset[str]
    negatives: frozenset[str]


@dataclass
class Rule:
    """An ARBA rule asserting one GO term."""

    id: str
    term: str
    sets: list[ConditionSet]


def load_rules() -> list[Rule]:
    """ARBA rules that assert a GO term, from the cached UniProt download."""
    if not CACHE.exists():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(ARBA_URL, timeout=600)
        r.raise_for_status()
        CACHE.write_bytes(r.content)
    rules = []
    for raw in json.loads(CACHE.read_text())["results"]:
        terms = [a["dbReference"]["id"] for a in raw["mainRule"].get("annotations", [])
                 if a.get("dbReference", {}).get("database") == "GO"]
        if not terms:
            continue
        sets = []
        for cs in raw["mainRule"]["conditionSets"]:
            sig, tax, neg = set(), set(), set()
            for c in cs["conditions"]:
                values = [f"{c['type']}:{v['value']}" for v in c.get("conditionValues", [])]
                if c.get("isNegative"):
                    neg.update(values)
                elif c["type"] == "taxon":
                    tax.update(values)
                else:
                    sig.update(values)
            sets.append(ConditionSet(frozenset(sig), frozenset(tax), frozenset(neg)))
        for term in terms:
            rules.append(Rule(raw["uniRuleId"], term, sets))
    ids = [r.id for r in rules]
    if len(ids) != len(set(ids)):
        raise ValueError("a rule asserts several GO terms; results are keyed by rule id")
    return rules


def go_tables(terms: set[str]) -> tuple[dict[str, set[str]], dict[str, str]]:
    """Strict is_a/part_of ancestors and labels for *terms*, from the oaklib GO build."""
    descendant_counts()  # ensures the GO database is present
    con = sqlite3.connect(Path.home() / ".data/oaklib/go.db")
    ancestors: dict[str, set[str]] = {}
    for t in terms:
        q = f"SELECT object FROM entailed_edge WHERE subject = ? AND predicate IN {PREDS!r} AND object != ?"
        ancestors[t] = {r[0] for r in con.execute(q, (t, t))}
    labels = dict(con.execute("SELECT subject, value FROM rdfs_label_statement WHERE subject LIKE 'GO:%'"))
    return ancestors, labels


def same_term_redundancy(rules: list[Rule]) -> dict[str, dict]:
    """Per rule: other rules asserting its term, how many share a signature, duplicate sets."""
    by_term: dict[str, list[Rule]] = collections.defaultdict(list)
    for r in rules:
        by_term[r.term].append(r)
    out = {}
    for term, group in by_term.items():
        for r in group:
            sigs = {s for cs in r.sets for s in cs.signatures}
            others = [o for o in group if o.id != r.id]
            sharing = [o for o in others if sigs & {s for cs in o.sets for s in cs.signatures}]
            other_sets = {cs for o in others for cs in o.sets}
            out[r.id] = {"same_term_rules": len(others), "same_term_sharing_signature": len(sharing),
                         "duplicate_sets": sum(1 for cs in r.sets if cs in other_sets)}
    return out


def subsumption(rules: list[Rule], ancestors: dict[str, set[str]]) -> dict[str, dict]:
    """Per rule: condition sets covered by a rule asserting a strict descendant term."""
    index: dict[str, list[tuple[Rule, ConditionSet]]] = collections.defaultdict(list)
    for r in rules:
        for cs in r.sets:
            if cs.negatives or not cs.signatures:
                continue
            for s in cs.signatures:
                index[s].append((r, cs))
    out = {}
    for r in rules:
        covered = 0
        by: collections.Counter = collections.Counter()
        for cs in r.sets:
            hit = None
            for s in cs.signatures:
                for other, ocs in index.get(s, ()):
                    if (other.id != r.id and r.term in ancestors.get(other.term, ())
                            and ocs.signatures <= cs.signatures
                            and (not ocs.taxa or ocs.taxa == cs.taxa)):
                        hit = other
                        break
                if hit:
                    break
            if hit:
                covered += 1
                by[hit.term] += 1
        out[r.id] = {"sets": len(r.sets), "covered_sets": covered,
                     "covered_by_terms": "|".join(t for t, _ in by.most_common(5))}
    return out


def gene_side(rules_of_interest: set[str]) -> dict[str, dict]:
    """For each rule's rows in gene reviews: actions, and whether a strict descendant is present."""
    rows = list(csv.DictReader(open(HERE / "gene_side_rows.tsv"), delimiter="\t"))
    for r in rows:
        r["rule_ids"] = [x.replace("ARBA:", "") for x in r["rules"].split("|") if x]
    rows = [r for r in rows if set(r["rule_ids"]) & rules_of_interest]
    genes = {r["gene"] for r in rows}
    annotations: dict[str, list[tuple[str, bool]]] = {}
    for g in genes:
        goa = glob.glob(f"genes/{g}/*-goa.tsv")
        annotations[g] = [
            (a["GO TERM"], a["REFERENCE"] == "GO_REF:0000117")
            for a in (csv.DictReader(open(goa[0]), delimiter="\t") if goa else [])
            if not a["QUALIFIER"].startswith("NOT")
        ]
    terms = {t for v in annotations.values() for t, _ in v}
    ancestors, _ = go_tables(terms)
    out: dict[str, dict] = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        desc = [arba for t, arba in annotations.get(r["gene"], []) if r["term"] in ancestors.get(t, ())]
        for rid in set(r["rule_ids"]) & rules_of_interest:
            c = out[rid]
            c["rows"] += 1
            c[r["action"]] += 1
            c["descendant_any"] += bool(desc)
            c["descendant_arba"] += any(desc)
    return out


def arba_stacking() -> tuple[int, int]:
    """Reviewed genes carrying an ARBA term together with an ARBA descendant of it, and all genes."""
    by_gene: dict[str, set[str]] = collections.defaultdict(set)
    for r in csv.DictReader(open(HERE / "gene_side_rows.tsv"), delimiter="\t"):
        by_gene[r["gene"]].add(r["term"])
    ancestors, _ = go_tables({t for ts in by_gene.values() for t in ts})
    stacked = sum(1 for ts in by_gene.values() if any(a in ancestors.get(b, ()) for a in ts for b in ts))
    return stacked, len(by_gene)


def quickgo_counts(rule_ids: list[str]) -> dict[str, dict]:
    """Annotation counts per rule from QuickGO, all taxa and human (cached)."""
    cache = json.loads(COUNTS_CACHE.read_text()) if COUNTS_CACHE.exists() else {}
    for rid in rule_ids:
        if rid in cache:
            continue
        counts = {}
        for key, extra in (("all", {}), ("human", {"taxonId": 9606, "taxonUsage": "exact"})):
            r = requests.get(QUICKGO, params={"withFrom": f"ARBA:{rid}", "limit": 1, **extra},
                             headers={"Accept": "application/json"}, timeout=120)
            r.raise_for_status()
            counts[key] = r.json()["numberOfHits"]
        cache[rid] = counts
    COUNTS_CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return cache


def pct(a: float, b: float) -> str:
    return f"{100 * a / b:.0f}%" if b else "-"


def main() -> None:
    rules = load_rules()
    ancestors, labels = go_tables({r.term for r in rules})
    ndesc = descendant_counts()
    same = same_term_redundancy(rules)
    sub = subsumption(rules, ancestors)

    with open(HERE / "rule_redundancy.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rule", "term", "label", "go_descendants", "condition_sets", "covered_sets",
                    "covered_by_terms", "same_term_rules", "same_term_sharing_signature", "duplicate_sets"])
        for r in sorted(rules, key=lambda x: x.id):
            s, m = sub[r.id], same[r.id]
            w.writerow([r.id, r.term, labels.get(r.term, ""), ndesc.get(r.term, 0), s["sets"],
                        s["covered_sets"], s["covered_by_terms"], m["same_term_rules"],
                        m["same_term_sharing_signature"], m["duplicate_sets"]])

    by_term = collections.Counter(r.term for r in rules)
    multi = [t for t, n in by_term.items() if n > 1]
    total_sets = sum(len(r.sets) for r in rules)
    covered_sets = sum(sub[r.id]["covered_sets"] for r in rules)
    fully = [r for r in rules if sub[r.id]["covered_sets"] == len(r.sets)]
    dup_sets = sum(same[r.id]["duplicate_sets"] for r in rules)

    rng = random.Random(SEED)
    partly = [r for r in rules if 0 < sub[r.id]["covered_sets"] < len(r.sets)]
    samples = {
        "fully covered": rng.sample(fully, min(SAMPLE, len(fully))),
        "partly covered": rng.sample(partly, min(SAMPLE, len(partly))),
        "all GO rules": rng.sample(rules, SAMPLE),
    }
    sample_counts = quickgo_counts(sorted({r.id for grp in samples.values() for r in grp}))
    stacked, n_genes = arba_stacking()

    gs_rows = list(csv.DictReader(open(HERE / "gene_side_rules.tsv"), delimiter="\t"))
    gs_ids = {r["rule"] for r in gs_rows if int(r["rows"]) >= GENERIC_MIN_ROWS}
    term_of = {r.id: r.term for r in rules}
    generic = [rid for rid in gs_ids if ndesc.get(term_of.get(rid, ""), 0) > GENERIC_DESCENDANTS]
    gene = gene_side(set(generic))
    counts = quickgo_counts(sorted(generic))
    counts.update(sample_counts)
    generic.sort(key=lambda rid: -(gene[rid]["REMOVE"] + gene[rid]["MARK_AS_OVER_ANNOTATED"] + gene[rid]["MODIFY"]))

    lines = [
        "---",
        'title: "ARBA rule redundancy and generic rules"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# ARBA rule redundancy and generic rules",
        "",
        "Generated by `rule_redundancy.py`; do not edit by hand. Per-rule measures for every",
        "GO-asserting rule are in [rule_redundancy.tsv](rule_redundancy.tsv).",
        "",
        "## Redundancy across all ARBA GO rules",
        "",
        f"- ARBA GO rules: **{len(rules)}**, each asserting one term, with **{total_sets}** condition sets.",
        f"- GO terms asserted by more than one rule: **{len(multi)}** of {len(by_term)}, covering "
        f"**{sum(by_term[t] for t in multi)}** rules.",
        f"- Rules that share a signature with another rule asserting the same term: "
        f"**{sum(1 for r in rules if same[r.id]['same_term_sharing_signature'])}**.",
        f"- Condition sets duplicated exactly in another rule for the same term: **{dup_sets}**.",
        f"- Condition sets covered by a rule asserting a more specific term: **{covered_sets}** "
        f"({pct(covered_sets, total_sets)}); rules covered in every set: **{len(fully)}**.",
        f"- Reviewed genes that carry both an ARBA term and an ARBA descendant of it: **{stacked}** of "
        f"{n_genes}. UniProt keeps the most specific ARBA term, so generic and specific ARBA rules do not "
        "stack on a protein; a covered condition set is dead weight rather than a source of extra annotations.",
        "",
        "## Do covered rules produce annotations?",
        "",
        f"QuickGO annotation counts for seeded random samples (seed {SEED}, up to {SAMPLE} rules each):",
        "",
        "| sample | rules sampled | with no annotations | median annotations |",
        "|---|---:|---:|---:|",
        *[
            f"| {name} | {len(vals)} | {sum(v == 0 for v in vals)} ({pct(sum(v == 0 for v in vals), len(vals))}) "
            f"| {vals[len(vals) // 2]:,} |"
            for name, vals in ((n, sorted(sample_counts[r.id]["all"] for r in grp)) for n, grp in samples.items())
        ],
        "",
        "## Generic rules seen in gene reviews",
        "",
        f"Rules whose term has more than {GENERIC_DESCENDANTS} GO descendants and that produced at least "
        f"{GENERIC_MIN_ROWS} annotations in our gene reviews ({len(generic)} rules). *Covered* is the share of the "
        "rule's condition sets that a more specific rule also matches. *Descendant present* is the share of "
        "the rule's reviewed annotations where the gene already has a more specific term, from any source "
        "(and from ARBA). *Kept* and *rejected* are the reviews' actions on the rule's rows.",
        "",
        "| rule | term | annotations (human) | sets | covered | rows | descendant present: any (ARBA) "
        "| kept | modified | rejected |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rid in generic:
        g, s = gene[rid], sub[rid]
        rej = g["REMOVE"] + g["MARK_AS_OVER_ANNOTATED"]
        kept = g["ACCEPT"] + g["KEEP_AS_NON_CORE"]
        lines.append(
            f"| {rid} | {labels.get(term_of[rid], term_of[rid])} | {counts[rid]['all']:,} ({counts[rid]['human']:,}) "
            f"| {s['sets']} | {pct(s['covered_sets'], s['sets'])} | {g['rows']} "
            f"| {pct(g['descendant_any'], g['rows'])} ({pct(g['descendant_arba'], g['rows'])}) "
            f"| {pct(kept, g['rows'])} | {pct(g['MODIFY'], g['rows'])} | {pct(rej, g['rows'])} |")
    (HERE / "RULE_REDUNDANCY.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[10:]))


if __name__ == "__main__":
    main()
