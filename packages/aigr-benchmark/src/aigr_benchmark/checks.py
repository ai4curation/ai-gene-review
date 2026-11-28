"""Deterministic checks for time-split annotation benchmarks.

Each check takes a :class:`Context` (baseline and current GO releases, the
current-release ontology, IC, PANTHER subfamilies) and one target annotation,
and returns ``CheckResult`` dicts conforming to ``schema/benchmark.yaml``. The
builder uses the same functions to select and grade targets, and ``run_checks``
reruns them over a finished benchmark, so hand edits and review-derived targets
are held to the same tests.
"""

from __future__ import annotations

import functools
import json
import re
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from jsonschema.exceptions import best_match
from jsonschema.protocols import Validator
from jsonschema.validators import validator_for

from aigr_benchmark.sources import (
    DEFAULT_CACHE,
    Annotation,
    InformationContent,
    Ontology,
    uniprot_entry,
)

#: The LinkML schema, and the closed JSON Schema generated from it (`just gen-models`).
SCHEMA = Path(__file__).resolve().parent / "schema" / "benchmark.yaml"
JSON_SCHEMA = SCHEMA.with_suffix(".schema.json")
#: Review actions that keep a claim; anything else contests it.
REVIEW_KEEPS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "TOO_GENERAL"})
REVIEW_CONTESTS = frozenset({"REMOVE", "MARK_AS_OVER_ANNOTATED"})
TOP_REFERENCE_SHARE_LIMIT = 0.25
#: A reference supplying targets to more than this fraction of items is flagged.
ITEM_SHARE_LIMIT = 0.1

Result = dict[str, Any]


def result(
    check: str,
    status: str,
    message: str,
    item_id: str | None = None,
    term_id: str | None = None,
    evidence: list[str] | None = None,
) -> Result:
    """Build a CheckResult dict, omitting empty slots.

    >>> result("novelty", "PASS", "ok", "B-P1", "GO:1")
    {'check': 'novelty', 'status': 'PASS', 'message': 'ok', 'item_id': 'B-P1', 'term_id': 'GO:1'}
    """
    out: Result = {"check": check, "status": status, "message": message}
    if item_id:
        out["item_id"] = item_id
    if term_id:
        out["term_id"] = term_id
    if evidence:
        out["evidence"] = evidence
    return out


def row_text(a: Annotation) -> str:
    """Compact text for a GAF row used as check evidence."""
    neg = "NOT|" if a.negated else ""
    return f"{a.protein} {neg}{a.qualifier} {a.term} {a.evidence} {a.reference} {a.assigned_by} {a.date}"


@dataclass
class Context:
    """Everything the checks read: two releases, one ontology, IC and homologs."""

    ontology: Ontology
    baseline: dict[str, list[Annotation]]
    current: dict[str, list[Annotation]]
    ic: InformationContent
    subfamily: dict[str, str] = field(default_factory=dict)
    near_duplicate_threshold: float = 0.8
    cutoff: str = ""
    excluded_terms: frozenset[str] = frozenset()
    cache: Path = DEFAULT_CACHE
    _members: dict[str, set[str]] = field(default_factory=dict, repr=False)

    def members(self, protein: str) -> set[str]:
        """Other proteins in the same PANTHER subfamily."""
        if not self._members:
            for member, family in self.subfamily.items():
                self._members.setdefault(family, set()).add(member)
        sf = self.subfamily.get(protein)
        return (self._members.get(sf, set()) - {protein}) if sf else set()

    def implies(self, annotated: str, target: str) -> bool:
        """True when an annotation to ``annotated`` entails ``target``."""
        return target in self.ontology.ancestors(self.ontology.resolve(annotated))

    def baseline_rows(
        self, protein: str, experimental: bool | None = None, negated: bool = False
    ) -> list[Annotation]:
        """Baseline rows for a protein, filtered by experimental flag and NOT."""
        return [
            a
            for a in self.baseline.get(protein, [])
            if a.negated == negated
            and (experimental is None or a.experimental == experimental)
        ]


def novelty(
    ctx: Context, protein: str, term: str, negated: bool, item_id: str | None = None
) -> Result:
    """Is the target absent from the baseline release with experimental evidence?

    A positive target is not new when a baseline experimental row is to the
    term, to a descendant, or to an alt_id or obsolete id that the current
    ontology maps onto either. A NOT target is not new when a baseline
    experimental NOT row is to the term or an ancestor.
    """
    if negated:
        hits = [
            a
            for a in ctx.baseline_rows(protein, experimental=True, negated=True)
            if ctx.ontology.resolve(a.term) in ctx.ontology.ancestors(term)
        ]
    else:
        hits = [
            a
            for a in ctx.baseline_rows(protein, experimental=True)
            if ctx.implies(a.term, term)
        ]
    if hits:
        return result(
            "novelty",
            "FAIL",
            f"already known at baseline from {len(hits)} row(s)",
            item_id,
            term,
            [row_text(a) for a in hits[:5]],
        )
    return result(
        "novelty",
        "PASS",
        "absent from baseline (term, descendants, merged ids)",
        item_id,
        term,
    )


def prior_prediction(
    ctx: Context, protein: str, term: str, item_id: str | None = None
) -> Result:
    """Was the term (or a descendant) predicted on the protein before the cutoff?"""
    hits = [
        a
        for a in ctx.baseline_rows(protein, experimental=False)
        if ctx.implies(a.term, term)
    ]
    if hits:
        codes = sorted({a.evidence for a in hits})
        return result(
            "prior_prediction",
            "WARN",
            f"predicted before cutoff by {','.join(codes)}",
            item_id,
            term,
            [row_text(a) for a in hits[:5]],
        )
    return result(
        "prior_prediction",
        "PASS",
        "not predicted on this protein at baseline",
        item_id,
        term,
    )


def homolog_leakage(
    ctx: Context, protein: str, term: str, item_id: str | None = None
) -> Result:
    """Was the term experimentally annotated on a same-subfamily homolog before the cutoff?"""
    hits = [
        a
        for member in sorted(ctx.members(protein))
        for a in ctx.baseline_rows(member, experimental=True)
        if ctx.implies(a.term, term)
    ]
    sf = ctx.subfamily.get(protein, "no PANTHER subfamily")
    if hits:
        homologs = sorted({a.protein for a in hits})
        return result(
            "homolog_leakage",
            "WARN",
            f"known on {len(homologs)} {sf} homolog(s) at baseline",
            item_id,
            term,
            [row_text(a) for a in hits[:5]],
        )
    if not ctx.members(protein):
        return result(
            "homolog_leakage",
            "INFO",
            f"not checked: {sf} has no other member in this species",
            item_id,
            term,
        )
    return result(
        "homolog_leakage", "PASS", f"not on {sf} homologs at baseline", item_id, term
    )


def near_duplicate(
    ctx: Context, protein: str, term: str, item_id: str | None = None
) -> Result:
    """Closest baseline experimental term on the protein in the same aspect (Lin similarity)."""
    aspect = ctx.ontology.aspect(term)
    scored = sorted(
        (
            (ctx.ic.lin(ctx.ontology.resolve(a.term), term), a.term)
            for a in ctx.baseline_rows(protein, experimental=True)
            if ctx.ontology.aspect(ctx.ontology.resolve(a.term)) == aspect
            and a.term not in ctx.excluded_terms
        ),
        reverse=True,
    )
    if not scored:
        return result(
            "near_duplicate",
            "INFO",
            "not applicable: no baseline experimental term in this aspect",
            item_id,
            term,
        )
    score, closest = scored[0]
    label = ctx.ontology.label(closest)
    message = f"closest baseline term {closest} {label} (Lin {score:.2f})"
    status = "WARN" if score >= ctx.near_duplicate_threshold else "PASS"
    return result("near_duplicate", status, message, item_id, term)


def knowledge_category(ctx: Context, protein: str, aspect: str) -> str:
    """CAFA knowledge category at baseline, on experimental rows outside the excluded terms."""
    aspects = {
        a.aspect
        for a in ctx.baseline_rows(protein, experimental=True)
        if a.term not in ctx.excluded_terms
    }
    if not aspects:
        return "NO_KNOWLEDGE"
    return "PARTIAL_KNOWLEDGE" if aspect in aspects else "LIMITED_KNOWLEDGE"


def difficulty(results: list[Result]) -> str:
    """Grade a target from its prior_prediction, homolog_leakage and near_duplicate results.

    >>> difficulty([{"check": "prior_prediction", "status": "WARN"}])
    'EASY'
    >>> difficulty([{"check": "near_duplicate", "status": "WARN"}, {"check": "homolog_leakage", "status": "PASS"}])
    'MEDIUM'
    >>> difficulty([])
    'HARD'
    """
    flagged = {r["check"] for r in results if r["status"] == "WARN"}
    if flagged & {"prior_prediction", "homolog_leakage"}:
        return "EASY"
    if "near_duplicate" in flagged:
        return "MEDIUM"
    return "HARD"


DIFFICULTY_ORDER = {"EASY": 0, "MEDIUM": 1, "HARD": 2}


def grading_results(
    ctx: Context, protein: str, term: str, item_id: str | None = None
) -> list[Result]:
    """The three checks that set difficulty."""
    return [
        prior_prediction(ctx, protein, term, item_id),
        homolog_leakage(ctx, protein, term, item_id),
        near_duplicate(ctx, protein, term, item_id),
    ]


def present_in_current(
    ctx: Context, protein: str, target: dict, item_id: str
) -> Result:
    """Is the target row (term, evidence, reference) in the current release?"""
    term = target["term"]["id"]
    negated = bool(target.get("negated"))
    rows = [
        a
        for a in ctx.current.get(protein, [])
        if a.term == term and a.negated == negated
    ]
    exact = [
        a
        for a in rows
        if a.evidence == target["evidence_code"] and a.reference == target["reference"]
    ]
    if exact:
        return result(
            "present_in_current",
            "PASS",
            "row present in current release",
            item_id,
            term,
        )
    if rows:
        return result(
            "present_in_current",
            "INFO",
            "term present with other evidence or reference",
            item_id,
            term,
            [row_text(a) for a in rows[:3]],
        )
    status = "INFO" if target["source"] == "AIGR_REVIEW" else "FAIL"
    return result(
        "present_in_current",
        status,
        "term not on this protein in current release",
        item_id,
        term,
    )


def date_window(ctx: Context, target: dict, item_id: str) -> Result | None:
    """GAF date on or after the cutoff (informational, since GO re-stamps dates)."""
    gaf_date = target.get("gaf_date")
    if not gaf_date:
        return None
    cutoff = ctx.cutoff.replace("-", "")
    term = target["term"]["id"]
    if gaf_date >= cutoff:
        return result(
            "date_window",
            "PASS",
            f"GAF date {gaf_date} on or after cutoff",
            item_id,
            term,
        )
    return result(
        "date_window",
        "WARN",
        f"GAF date {gaf_date} before cutoff yet absent from baseline "
        "(late export or filtered from the baseline release)",
        item_id,
        term,
    )


CC_BLOCK = re.compile(r"^CC   (.*)$", re.MULTILINE)


def uniprot_leakage(
    entry_text: str, term: str, label: str | None, item_id: str
) -> list[Result]:
    """Does the current UniProt entry expose the target?

    >>> entry = "CC   -!- FUNCTION: Has protein kinase activity.\\nDR   GO; GO:0004672; F:protein kinase activity; IDA:UniProtKB.\\n"
    >>> [r["status"] for r in uniprot_leakage(entry, "GO:0004672", "protein kinase activity", "x")]
    ['INFO', 'WARN']
    >>> [r["status"] for r in uniprot_leakage("", "GO:0004672", "protein kinase activity", "x")]
    ['PASS', 'PASS']
    """
    out = []
    if f"DR   GO; {term};" in entry_text:
        out.append(
            result(
                "uniprot_leakage",
                "INFO",
                "current UniProt DR GO line carries the target "
                "(block UniProt/QuickGO for tool-using predictors)",
                item_id,
                term,
            )
        )
    else:
        out.append(
            result(
                "uniprot_leakage",
                "PASS",
                "not in current UniProt DR GO lines",
                item_id,
                term,
            )
        )
    comments = " ".join(CC_BLOCK.findall(entry_text)).lower()
    comments = re.sub(r"\s+", " ", comments)
    if label and label.lower() in comments:
        out.append(
            result(
                "uniprot_leakage",
                "WARN",
                f"label '{label}' appears in UniProt comment text",
                item_id,
                term,
            )
        )
    else:
        out.append(
            result(
                "uniprot_leakage",
                "PASS",
                "label not in UniProt comment text",
                item_id,
                term,
            )
        )
    return out


def reference_recency(
    target: dict, predictors: list[dict], item_id: str
) -> list[Result]:
    """Was the target's earliest supporting reference published after each predictor's training cutoff?

    >>> t = {"term": {"id": "GO:1"}, "reference": "PMID:1", "reference_date": "2025-09-01"}
    >>> [r["status"] for r in reference_recency(t, [{"name": "peptalk:m", "model_training_cutoff": "2026-06-01"}], "x")]
    ['WARN']
    >>> [r["status"] for r in reference_recency(t, [{"name": "interproscan"}], "x")]
    ['INFO']
    """
    term = target["term"]["id"]
    published = target.get("reference_date")
    out = []
    for predictor in predictors:
        cutoff = predictor.get("model_training_cutoff")
        name = predictor["name"]
        if not cutoff or not published:
            missing = (
                "model training cutoff"
                if not cutoff
                else f"publication date of {target['reference']}"
            )
            out.append(
                result(
                    "reference_recency",
                    "INFO",
                    f"{name}: {missing} unknown",
                    item_id,
                    term,
                )
            )
        elif published > cutoff:
            out.append(
                result(
                    "reference_recency",
                    "PASS",
                    f"{name}: {target['reference']} published {published}, after model cutoff {cutoff}",
                    item_id,
                    term,
                )
            )
        else:
            out.append(
                result(
                    "reference_recency",
                    "WARN",
                    f"{name}: {target['reference']} published {published}, before model cutoff {cutoff}",
                    item_id,
                    term,
                )
            )
    return out


def decoy_check(ctx: Context, protein: str, decoy: dict, item_id: str) -> Result:
    """A decoy must not entail, or be entailed by, a current annotation of the protein."""
    term = decoy["term"]["id"]
    hits = [
        a
        for a in ctx.current.get(protein, [])
        if not a.negated
        and (
            term in ctx.ontology.ancestors(ctx.ontology.resolve(a.term))
            or ctx.ontology.resolve(a.term) in ctx.ontology.ancestors(term)
        )
    ]
    if hits:
        return result(
            "decoy",
            "FAIL",
            "decoy is related to a current annotation of the protein",
            item_id,
            term,
            [row_text(a) for a in hits[:3]],
        )
    return result(
        "decoy", "PASS", "decoy unrelated to current annotations", item_id, term
    )


STOP_TOKENS = frozenset(
    {
        "activity",
        "of",
        "the",
        "process",
        "regulation",
        "positive",
        "negative",
        "to",
        "in",
        "and",
        "via",
        "by",
        "involved",
        "complex",
        "protein",
        "cell",
        "cellular",
    }
)


def content_tokens(text: str) -> set[str]:
    """Lower-case word tokens minus GO boilerplate.

    >>> sorted(content_tokens("UDP-glucose 4,6-dehydratase activity"))
    ['4', '6', 'dehydratase', 'glucose', 'udp']
    """
    return {
        t for t in re.split(r"[^a-z0-9]+", text.lower()) if t and t not in STOP_TOKENS
    }


def header_leakage(
    protein_name: str, term: str, label: str | None, item_id: str
) -> Result:
    """Does the protein name (shown in the FULL condition) give the target away?

    WARN when at least 60% of the label's content tokens occur in the name.

    >>> header_leakage("UDP-D-glucose 4,6-dehydratase", "GO:1", "UDP-glucose 4,6-dehydratase activity", "x")["status"]
    'WARN'
    >>> header_leakage("Myeloperoxidase", "GO:2", "nucleosome binding", "x")["status"]
    'PASS'
    """
    tokens = content_tokens(label or "")
    shared = tokens & content_tokens(protein_name)
    if tokens and len(shared) / len(tokens) >= 0.6:
        return result(
            "header_leakage",
            "WARN",
            f"protein name '{protein_name}' shares {sorted(shared)} with "
            "the target label (FULL-header conditions)",
            item_id,
            term,
        )
    return result(
        "header_leakage",
        "PASS",
        "target label not given away by the protein name",
        item_id,
        term,
    )


FEATURE_KEYWORDS = {
    "PSEUDOENZYME": re.compile(
        r"inactive|pseudo|lacks? (the )?(conserved )?catalytic", re.I
    )
}


def uniprot_names_and_comments(entry_text: str) -> tuple[str, list[str]]:
    r"""The protein's own DE names and its CC paragraphs (one string per ``-!-`` topic).

    Names of chains or domains (after ``Contains:`` or ``Includes:``) are left
    out: "Kallikrein-11 inactive chain 1" names a cleavage product, not the
    protein.

    >>> names, cc = uniprot_names_and_comments("DE   RecName: Full=Inactive kinase X;\nCC   -!- FUNCTION: Binds ATP.\nCC       More.\nCC   -!- DOMAIN: Pseudo.\n")
    >>> names, cc
    ('RecName: Full=Inactive kinase X;', ['FUNCTION: Binds ATP. More.', 'DOMAIN: Pseudo.'])
    >>> uniprot_names_and_comments("DE   RecName: Full=Kallikrein-11;\nDE   Contains:\nDE     RecName: Full=Kallikrein-11 inactive chain 1;\n")[0]
    'RecName: Full=Kallikrein-11;'
    """
    own: list[str] = []
    for line in entry_text.splitlines():
        if not line.startswith("DE   "):
            continue
        text = line[5:].strip()
        if text in ("Contains:", "Includes:"):
            break
        own.append(text)
    names = " ".join(own)
    paragraphs: list[str] = []
    for line in entry_text.splitlines():
        if line.startswith("CC   -!- "):
            paragraphs.append(line[9:].strip())
        elif line.startswith("CC       ") and paragraphs:
            paragraphs[-1] += " " + line[2:].strip()
    return names, paragraphs


def feature_label(entry_text: str, feature: str, item_id: str) -> Result:
    r"""Does the UniProt entry support a query-derived feature label in its names, or only in comments?

    >>> feature_label("DE   RecName: Full=Inactive kinase X;\n", "PSEUDOENZYME", "x")["status"]
    'PASS'
    >>> r = feature_label("DE   RecName: Full=Kinase X;\nCC   -!- FUNCTION: [Isoform 2]: Catalytically inactive.\n", "PSEUDOENZYME", "x")
    >>> r["status"], r["evidence"]
    ('WARN', ['FUNCTION: [Isoform 2]: Catalytically inactive.'])
    """
    pattern = FEATURE_KEYWORDS[feature]
    names, paragraphs = uniprot_names_and_comments(entry_text)
    if pattern.search(names):
        return result(
            "feature_label",
            "PASS",
            f"{feature} label supported by the UniProt protein name",
            item_id,
        )
    hits = [p for p in paragraphs if pattern.search(p)]
    if hits:
        return result(
            "feature_label",
            "WARN",
            f"{feature} label rests on comment text only "
            "(check it is about this protein's canonical form)",
            item_id,
            evidence=hits[:3],
        )
    return result(
        "feature_label",
        "WARN",
        f"neither the protein's own names nor its comments support the {feature} label "
        "(the query may have matched a chain or domain name, or the entry was revised)",
        item_id,
    )


def find_review(genes_dir: Path, symbol: str | None, accession: str) -> Path | None:
    """The ai-gene-review review for an accession, found by symbol and checked by id."""
    if not symbol or not genes_dir.exists():
        return None
    for path in sorted(genes_dir.glob(f"*/{symbol}/{symbol}-ai-review.yaml")):
        if (yaml.safe_load(path.read_text()) or {}).get("id") == accession:
            return path
    return None


def review_actions(review_path: Path, term: str) -> list[str]:
    """Actions a review gives the existing annotations to a term."""
    data = yaml.safe_load(review_path.read_text())
    return sorted(
        {
            (row.get("review") or {}).get("action", "PENDING")
            for row in data.get("existing_annotations") or []
            if (row.get("term") or {}).get("id") == term
        }
    )


def review_agreement(target: dict, item_id: str) -> Result | None:
    """Compare a target with the review action recorded on it."""
    action = target.get("review_action")
    if not target.get("review_file"):
        return None
    term = target["term"]["id"]
    if not action:
        return result(
            "review_agreement", "INFO", "term not in the gene's review", item_id, term
        )
    actions = set(action.split(","))
    if actions & REVIEW_CONTESTS:
        return result(
            "review_agreement",
            "WARN",
            f"review contests the target ({action})",
            item_id,
            term,
        )
    if actions & REVIEW_KEEPS:
        return result(
            "review_agreement",
            "PASS",
            f"review keeps the target ({action})",
            item_id,
            term,
        )
    return result("review_agreement", "INFO", f"review action {action}", item_id, term)


@functools.cache
def json_schema_validator(target_class: str) -> Validator:
    """A validator for one class of the bundled JSON Schema.

    >>> json_schema_validator("Benchmark").schema["$ref"]
    '#/$defs/Benchmark'
    """
    schema = json.loads(JSON_SCHEMA.read_text())
    if target_class not in schema["$defs"]:
        raise ValueError(f"{target_class} is not a class in {SCHEMA.name}")
    rooted = {
        "$schema": schema["$schema"],
        "$defs": schema["$defs"],
        "$ref": f"#/$defs/{target_class}",
    }
    # The class follows the dialect the generated schema declares, as LinkML's
    # validator does, and checks formats (``date``) the same way.
    cls = validator_for(rooted)
    return cls(rooted, format_checker=cls.FORMAT_CHECKER)


def validate_schema(data: dict, target_class: str) -> list[str]:
    """Closed JSON Schema validation problems for a document, one message per error.

    The JSON Schema is generated from the LinkML schema, so this gives the same
    results as ``linkml-validate`` with the closed JSON Schema plugin, without
    needing LinkML at run time.

    >>> validate_schema({"check": "novelty", "status": "PASS", "message": "ok"}, "CheckResult")
    []
    >>> validate_schema({"check": "novelty", "status": "MAYBE", "message": "ok"}, "CheckResult")
    ["'MAYBE' is not one of ['PASS', 'INFO', 'WARN', 'FAIL'] in /status"]
    """
    return [
        f"{error.message} in /{'/'.join(str(p) for p in error.absolute_path)}"
        for error in (
            best_match([e]) for e in json_schema_validator(target_class).iter_errors(data)
        )
    ]


def stats(benchmark: dict, ic: InformationContent) -> tuple[dict, list[Result]]:
    """Balance and coverage statistics, plus WARN results for imbalance."""
    items = benchmark["items"]
    targets = [(item, t) for item in items for t in item["target_annotations"]]
    counts: dict[str, Counter] = defaultdict(Counter)
    for item, t in targets:
        counts["aspect"][t["aspect"]] += 1
        counts["evidence_code"][t["evidence_code"]] += 1
        counts["knowledge_category"][t.get("knowledge_category", "UNSET")] += 1
        counts["difficulty"][t.get("difficulty", "UNSET")] += 1
        counts["negated"][str(bool(t.get("negated")))] += 1
        counts["assigned_by"][t.get("assigned_by", "UNSET")] += 1
        counts["source"][t["source"]] += 1
    for item in items:
        counts["split"][item["split"]] += 1
        for feature in item.get("features") or [{"feature": "NONE"}]:
            counts["feature"][feature["feature"]] += 1
    references = Counter(t["reference"] for _, t in targets)
    per_item = [len(item["target_annotations"]) for item in items]
    top_share = references.most_common(1)[0][1] / len(targets) if targets else 0.0
    table = [
        {"dimension": dim, "value": value, "count": n}
        for dim in sorted(counts)
        for value, n in sorted(counts[dim].items())
    ]
    table += [
        {"dimension": "top_reference", "value": ref, "count": n}
        for ref, n in references.most_common(5)
    ]
    out = {
        "n_items": len(items),
        "n_targets": len(targets),
        "counts": table,
        "targets_per_item_min": min(per_item, default=0),
        "targets_per_item_median": float(statistics.median(per_item))
        if per_item
        else 0.0,
        "targets_per_item_max": max(per_item, default=0),
        "mean_information_content": round(
            statistics.mean(ic.ic(t["term"]["id"]) for _, t in targets), 3
        )
        if targets
        else 0.0,
        "top_reference_share": round(top_share, 3),
    }
    findings = []
    spec = benchmark["spec"]
    if len(items) < spec["size"]:
        findings.append(
            result(
                "balance", "WARN", f"{len(items)} items drawn, {spec['size']} requested"
            )
        )
    for aspect in spec.get("aspects") or ["F", "P", "C"]:
        if not counts["aspect"][aspect]:
            findings.append(
                result("balance", "WARN", f"no targets in requested aspect {aspect}")
            )
    for quota in spec.get("features") or []:
        got = counts["feature"][quota["feature"]]
        if got < quota["count"]:
            findings.append(
                result(
                    "balance",
                    "WARN",
                    f"{got} {quota['feature']} items, {quota['count']} requested",
                )
            )
    items_by_reference: dict[str, set[str]] = defaultdict(set)
    for item, t in targets:
        items_by_reference[t["reference"]].add(item["id"])
    for ref, item_ids in sorted(items_by_reference.items()):
        if len(item_ids) > max(1, ITEM_SHARE_LIMIT * len(items)):
            findings.append(
                result(
                    "balance",
                    "WARN",
                    f"{ref} supplies targets to {len(item_ids)}/{len(items)} items, "
                    "so their scores are not independent",
                )
            )
    if top_share > TOP_REFERENCE_SHARE_LIMIT:
        ref, n = references.most_common(1)[0]
        findings.append(
            result("balance", "WARN", f"{ref} supplies {n}/{len(targets)} targets")
        )
    if not findings:
        findings.append(
            result(
                "balance",
                "PASS",
                "requested size, aspects and quotas met; no dominant reference",
            )
        )
    return out, findings


def run_checks(
    benchmark: dict, ctx: Context, genes_dir: Path | None = None, uniprot: bool = True
) -> dict:
    """Run every check over a benchmark and return a CheckReport dict."""
    results: list[Result] = [
        result("schema", "FAIL", problem)
        for problem in validate_schema(benchmark, "Benchmark")
    ] or [result("schema", "PASS", "Benchmark validates against schema/benchmark.yaml")]
    predictors = benchmark["spec"].get("predictors") or []
    if not predictors:
        results.append(
            result(
                "reference_recency",
                "INFO",
                "No predictors declared. Training cutoff fairness is unassessed.",
            )
        )
    for item in benchmark["items"]:
        protein, item_id = item["protein"], item["id"]
        accession = protein.split(":", 1)[1]
        entry = uniprot_entry(accession, ctx.cache) if uniprot else None
        if entry is not None:
            results += [
                feature_label(entry, f["feature"], item_id)
                if f["feature"] in FEATURE_KEYWORDS
                else result(
                    "feature_label",
                    "INFO",
                    f"no label check implemented for {f['feature']}",
                    item_id,
                )
                for f in item.get("features") or []
            ]
        for target in item["target_annotations"]:
            term = target["term"]["id"]
            negated = bool(target.get("negated"))
            results.append(novelty(ctx, protein, term, negated, item_id))
            results.append(present_in_current(ctx, protein, target, item_id))
            results += [
                r
                for r in (
                    date_window(ctx, target, item_id),
                    review_agreement(target, item_id),
                )
                if r
            ]
            if not negated:
                graded = grading_results(ctx, protein, term, item_id)
                results += graded
                recorded = target.get("difficulty")
                if recorded and recorded != difficulty(graded):
                    results.append(
                        result(
                            "difficulty",
                            "WARN",
                            f"recorded difficulty {recorded} but checks give {difficulty(graded)}",
                            item_id,
                            term,
                        )
                    )
            if entry is not None:
                results += uniprot_leakage(
                    entry, term, target["term"].get("label"), item_id
                )
            results += reference_recency(target, predictors, item_id)
            if item.get("protein_name"):
                results.append(
                    header_leakage(
                        item["protein_name"], term, target["term"].get("label"), item_id
                    )
                )
        for decoy in item.get("decoys") or []:
            results.append(decoy_check(ctx, protein, decoy, item_id))
    stat_block, balance = stats(benchmark, ctx.ic)
    results += balance
    summary = []
    for check in dict.fromkeys(r["check"] for r in results):
        statuses = Counter(r["status"] for r in results if r["check"] == check)
        summary.append(
            {
                "check": check,
                "passed": statuses["PASS"],
                "info": statuses["INFO"],
                "warned": statuses["WARN"],
                "failed": statuses["FAIL"],
            }
        )
    return {
        "benchmark_id": benchmark["id"],
        "generated": date.today().isoformat(),
        "sources": benchmark.get("sources", []),
        "summary": summary,
        "results": results,
        "stats": stat_block,
    }


def report_markdown(report: dict) -> str:
    """Human-readable rendering of a CheckReport."""
    lines = [
        f"# Check report: {report['benchmark_id']}",
        "",
        f"Generated {report['generated']}.",
        "",
        "| check | pass | info | warn | fail |",
        "|---|---|---|---|---|",
    ]
    lines += [
        f"| {s['check']} | {s['passed']} | {s['info']} | {s['warned']} | {s['failed']} |"
        for s in report["summary"]
    ]
    st = report["stats"]
    lines += [
        "",
        "## Stats",
        "",
        f"{st['n_items']} items, {st['n_targets']} targets; targets per item "
        f"{st['targets_per_item_min']}/{st['targets_per_item_median']}/{st['targets_per_item_max']} "
        f"(min/median/max); mean IC {st['mean_information_content']} bits; "
        f"top reference share {st['top_reference_share']}.",
        "",
        "| dimension | value | count |",
        "|---|---|---|",
    ]
    lines += [
        f"| {c['dimension']} | {c['value']} | {c['count']} |" for c in st["counts"]
    ]
    flagged = [r for r in report["results"] if r["status"] in ("WARN", "FAIL")]
    lines += [
        "",
        f"## Warnings and failures ({len(flagged)})",
        "",
        "| check | status | item | term | message |",
        "|---|---|---|---|---|",
    ]
    lines += [
        f"| {r['check']} | {r['status']} | {r.get('item_id', '')} | {r.get('term_id', '')} | "
        f"{r['message'].replace('|', '/')} |"
        for r in flagged
    ]
    lines += ["", "## Sources", ""]
    lines += [
        f"- {s['name']}: {s['url']} (release {s.get('release', '')}, sha256 {s.get('sha256', 'n/a')})"
        for s in report["sources"]
    ]
    return "\n".join(lines) + "\n"
