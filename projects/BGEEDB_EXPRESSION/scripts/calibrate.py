"""Pilot A (corpus): does Bgee expression track curators' annotation decisions?

For every reviewed, non-negated human annotation whose GO term names an
anatomy (go-plus logical definition, or nearest ancestor's), compare the
term's anatomy with the gene's Bgee 15.2 calls and assign an expression tier:

    ENRICHED    present in the term's anatomy, and that anatomy is among the
                gene's own top 10% of sampled entities (by Bgee expression score)
    CONSISTENT  present in the term's anatomy, not enriched
    ABSENT      Bgee has calls in or around the anatomy, all absent
    ABSENT_*    absent, but uninformative for a stated reason: a developmental
                term read against stage-merged (mostly adult) calls; a regulated
                process (the regulator may act from elsewhere); an extracellular
                or ligand product (non-cell-autonomous); a transcriptionally
                quiescent target cell (sperm, erythrocyte, platelet)
    NO_DATA     Bgee has nothing in or around the anatomy

The same tiers are computed for a shuffled baseline (each term paired with a
random corpus gene, fixed seed) so "consistent" can be read against chance.
Rates are then tabulated by the reviewer's action and by evidence group.

This is a calibration, not a classifier: reviewers' actions are the reference,
and the question is whether expression separates ACCEPT from REMOVE well
enough to be worth reading as one piece of evidence among several.

Inputs: the cache written by ``extract_corpus.py``.
Outputs: ``results/corpus_calibration.yaml``, ``results/corpus_leads.tsv``,
``.cache/bgee_expression/corpus_verdicts.tsv`` (full table).

Usage (from repo root):
    uv run python projects/BGEEDB_EXPRESSION/scripts/calibrate.py
"""

from __future__ import annotations

import csv
import math
import pickle
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402

ENRICH_PCT = 0.90
SEED = 20261108
TIERS = ["ENRICHED", "CONSISTENT", "ABSENT", "ABSENT_REGULATOR", "ABSENT_QUIESCENT", "ABSENT_DEVELOPMENTAL", "ABSENT_NONAUTONOMOUS", "NO_DATA"]
EVIDENCE_GROUPS = {
    "EXPERIMENTAL": {"EXP", "IDA", "IPI", "IMP", "IGI", "HDA", "HMP", "HGI", "HTP"},
    "IEP": {"IEP", "HEP"},
    "IBA": {"IBA"},
    "IEA": {"IEA"},
    "SEQUENCE": {"ISS", "ISO", "ISA", "ISM", "IGC", "RCA"},
    "AUTHOR_CURATOR": {"TAS", "NAS", "IC"},
}
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE"}
REJECTED = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}


def evidence_group(code: str) -> str:
    for g, codes in EVIDENCE_GROUPS.items():
        if code in codes:
            return g
    return "OTHER"


class Profile:
    """A gene's Bgee calls, with its own score distribution for percentiles."""

    def __init__(self, calls: list[bc.Call]):
        self.calls = [c for c in calls if c.quality in ("gold", "silver") and c.score == c.score]
        self.scores = sorted(c.score for c in self.calls)

    def percentile(self, score: float) -> float:
        if not self.scores:
            return 0.0
        below = sum(1 for s in self.scores if s < score)
        return below / len(self.scores)


def tier_for(go_id: str, prof: Profile, go: bc.GoAnatomy, anat: bc.Anatomy, memo: dict,
             nonautonomous: bool = False) -> tuple[str, float, list[str], str]:
    """Return (tier, percentile, evidence entities, base class)."""
    targets = memo.get(go_id)
    if targets is None:
        tg, _, _ = go.targets(go_id)
        targets = sorted({a for _, a in tg})
        memo[go_id] = targets
    if not targets:
        return "NO_ANATOMY", 0.0, [], "NO_ANATOMY"
    v = bc.classify_annotation(go_id, prof.calls, go, anat, nonautonomous=nonautonomous)
    if v.cls in bc.CONSISTENT:
        best = max(c.score for c in prof.calls if c.entity in v.evidence and c.state == "present")
        pct = prof.percentile(best)
        return ("ENRICHED" if pct >= ENRICH_PCT else "CONSISTENT"), pct, v.evidence, v.cls
    return v.cls, 0.0, v.evidence, v.cls


def rates(counter: Counter) -> dict:
    n = sum(counter[t] for t in TIERS)
    out = {"n": n}
    for t in TIERS:
        out[t] = round(counter[t] / n, 3) if n else None
    informative = sum(counter[t] for t in TIERS if t != "NO_DATA")
    out["absent_given_data"] = round(counter["ABSENT"] / informative, 3) if informative else None
    out["enriched_given_data"] = round(counter["ENRICHED"] / informative, 3) if informative else None
    return out


def risk_ratio(a: int, n1: int, c: int, n2: int) -> dict:
    """P(tier | rejected) / P(tier | retained), with a Katz 95% interval.

    >>> risk_ratio(10, 100, 5, 100)["ratio"]
    2.0
    """
    p1 = a / n1 if n1 else 0.0
    p2 = c / n2 if n2 else 0.0
    out = {"rejected": f"{a}/{n1}", "retained": f"{c}/{n2}", "ratio": None, "ci95": None}
    if a and c:
        rr = p1 / p2
        se = math.sqrt(1 / a - 1 / n1 + 1 / c - 1 / n2)
        out["ratio"] = round(rr, 2)
        out["ci95"] = [round(math.exp(math.log(rr) - 1.96 * se), 2), round(math.exp(math.log(rr) + 1.96 * se), 2)]
    return out


def likelihood_ratios(verdicts: list[dict], group: str | None) -> dict:
    """How much more often each tier occurs on rejected than on retained rows."""
    rej = [v for v in verdicts if v["action"] in REJECTED and (group is None or v["evidence_group"] == group)]
    ret = [v for v in verdicts if v["action"] in RETAINED and (group is None or v["evidence_group"] == group)]
    rej = [v for v in rej if v["tier"] != "NO_DATA"]
    ret = [v for v in ret if v["tier"] != "NO_DATA"]
    out = {}
    for tier in ("ENRICHED", "CONSISTENT", "ABSENT"):
        a = sum(1 for v in rej if v["tier"] == tier)
        c = sum(1 for v in ret if v["tier"] == tier)
        out[tier] = risk_ratio(a, len(rej), c, len(ret))
    # Any absence, before the regulator / quiescent / developmental /
    # non-autonomous screens are applied.
    a = sum(1 for v in rej if v["tier"].startswith("ABSENT"))
    c = sum(1 for v in ret if v["tier"].startswith("ABSENT"))
    out["ABSENT_UNSCREENED"] = risk_ratio(a, len(rej), c, len(ret))
    return out


def main() -> None:
    go = bc.load_go_anatomy()
    anat = bc.load_anatomy()
    with (bc.CACHE / "corpus_calls.pkl").open("rb") as fh:
        blob = pickle.load(fh)
    profiles = {gid: Profile(c) for gid, c in blob["calls"].items()}
    with (bc.CACHE / "corpus_annotations.tsv").open() as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t") if not r["negated"] and r["ensembl"] in profiles]

    secreted = bc.nonautonomous_genes(rows, go, REJECTED)
    gene_of = {gid: sym for gid, sym in blob["symbols"].items()}
    memo: dict[str, list[str]] = {}
    rng = random.Random(SEED)
    genes = sorted(profiles)
    verdicts = []
    for r in rows:
        prof = profiles[r["ensembl"]]
        tier, pct, ev, base = tier_for(r["go_id"], prof, go, anat, memo, r["gene"] in secreted)
        if tier == "NO_ANATOMY":
            continue
        shuffled = genes[rng.randrange(len(genes))]
        s_tier, s_pct, _, _ = tier_for(r["go_id"], profiles[shuffled], go, anat, memo, gene_of.get(shuffled) in secreted)
        verdicts.append({**r, "tier": tier, "base_class": base, "percentile": round(pct, 3),
                         "evidence_entities": "|".join(ev[:8]), "targets": "|".join(memo[r["go_id"]]),
                         "shuffled_gene": blob["symbols"].get(shuffled, shuffled), "shuffled_tier": s_tier,
                         "evidence_group": evidence_group(r["evidence"])})

    full = bc.CACHE / "corpus_verdicts.tsv"
    with full.open("w", newline="") as fh:
        w = csv.DictWriter(fh, list(verdicts[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(verdicts)

    by_action: dict[str, Counter] = defaultdict(Counter)
    by_group_action: dict[tuple[str, str], Counter] = defaultdict(Counter)
    by_aspect: dict[str, Counter] = defaultdict(Counter)
    shuffled_all: Counter = Counter()
    shuffled_by_action: dict[str, Counter] = defaultdict(Counter)
    for v in verdicts:
        by_action[v["action"]][v["tier"]] += 1
        by_aspect[v["aspect"]][v["tier"]] += 1
        shuffled_all[v["shuffled_tier"]] += 1
        shuffled_by_action[v["action"]][v["shuffled_tier"]] += 1
        bucket = "RETAINED" if v["action"] in RETAINED else "REJECTED" if v["action"] in REJECTED else None
        if bucket:
            by_group_action[(v["evidence_group"], bucket)][v["tier"]] += 1

    n_genes = len({v["gene"] for v in verdicts})
    summary = {
        "bgee_release": bc.BGEE_RELEASE,
        "go_release": go.version,
        "enrichment_percentile": ENRICH_PCT,
        "shuffle_seed": SEED,
        "annotations_considered": len(rows),
        "nonautonomous_genes": len(secreted),
        "anatomy_bearing_annotations": len(verdicts),
        "anatomy_bearing_genes": n_genes,
        "distinct_anatomy_terms": len({v["go_id"] for v in verdicts}),
        "by_action": {a: rates(c) for a, c in sorted(by_action.items(), key=lambda kv: -sum(kv[1].values()))},
        "shuffled_by_action": {a: rates(c) for a, c in sorted(shuffled_by_action.items(), key=lambda kv: -sum(kv[1].values()))},
        "shuffled_baseline": rates(shuffled_all),
        "by_aspect": {a: rates(c) for a, c in by_aspect.items()},
        "by_evidence_group": {
            f"{g}/{b}": rates(c) for (g, b), c in sorted(by_group_action.items())
        },
        "rejected_vs_retained_given_data": {
            (g or "ALL"): likelihood_ratios(verdicts, g)
            for g in (None, "EXPERIMENTAL", "IBA", "IEA", "SEQUENCE", "AUTHOR_CURATOR", "IEP")
        },
        "percentile_median_by_action": {
            a: round(statistics.median([v["percentile"] for v in verdicts if v["action"] == a and v["tier"] in ("ENRICHED", "CONSISTENT")] or [0]), 3)
            for a in by_action
        },
    }
    bc.RESULTS.mkdir(parents=True, exist_ok=True)
    (bc.RESULTS / "corpus_calibration.yaml").write_text(yaml.safe_dump(summary, sort_keys=False, width=100))

    # Leads: where expression disagrees with the reviewer's call.
    leads = []
    for v in verdicts:
        # Presence is not evidence for function (see rejected_vs_retained), so
        # only absence on a retained inference is worth a second look.
        if v["action"] in RETAINED and v["tier"] == "ABSENT" and v["evidence_group"] in ("IBA", "IEA", "SEQUENCE"):
            leads.append(("RETAINED_INFERENCE_BUT_ABSENT", v))
    with (bc.RESULTS / "corpus_leads.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["lead_type", "gene", "go_id", "go_label", "evidence", "action", "tier", "percentile", "targets", "evidence_entities"])
        for kind, v in sorted(leads, key=lambda kv: (kv[0], kv[1]["gene"], kv[1]["go_id"])):
            w.writerow([kind, v["gene"], v["go_id"], v["go_label"], v["evidence"], v["action"], v["tier"],
                        v["percentile"], v["targets"], v["evidence_entities"]])
    print(yaml.safe_dump({k: summary[k] for k in ("anatomy_bearing_annotations", "anatomy_bearing_genes", "shuffled_baseline")}, sort_keys=False))
    print(f"{len(leads)} leads -> {bc.RESULTS / 'corpus_leads.tsv'}")


if __name__ == "__main__":
    main()
