#!/usr/bin/env python3
"""Evaluate function requirement (NOT) rules against annotations.

A function requirement rule says that a protein enabling a GO term carries at least
one of a list of features (InterPro entries, or a transmembrane segment), and
optionally that some features exclude the term. The useful direction is the
contrapositive: a protein with none of the required features, or with an excluding
one, is unlikely to enable the term. Rules live in
``rules/function_requirements/function-requirement-rules.yaml`` and follow
``src/ai_gene_review/schema/function_requirement_rules.yaml``.

Two commands:

``acceptance``
    Tests each rule against every protein in GOA with an experimental
    (ECO:0000269 and descendants) annotation to the rule's term, fetched from
    QuickGO, with features from UniProt. A sound rule flags few of these, and each
    flag is either a rule gap or an experimental annotation worth questioning.

``sweep``
    Applies the rules to the GOA rows of every gene folder in ``genes/``, using the
    cached ``*-uniprot.txt`` for features, and joins the existing review action.

>>> rule = {"id": "FRR:9999", "term": {"id": "GO:0008955"}, "qualifiers": ["enables"],
...         "requires_any_of": [{"id": "IPR001264"}], "strength": "REQUIRED"}
>>> evaluate(rule, ProteinFeatures("P0AD68", frozenset({"IPR001460"}), 1)).value
'MISSING_REQUIRED'
>>> evaluate(rule, ProteinFeatures("P02918", frozenset({"IPR001264"}), 1)).value
'SATISFIED'
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
RULES_PATH = (
    REPO_ROOT / "rules" / "function_requirements" / "function-requirement-rules.yaml"
)
REPORT_DIR = REPO_ROOT / "reports" / "function-requirements"
CACHE_DIR = REPO_ROOT / ".cache" / "function-requirements"

QUICKGO_DOWNLOAD = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
UNIPROT_ACCESSIONS = "https://rest.uniprot.org/uniprotkb/accessions"
EXPERIMENTAL_ECO = "ECO:0000269"

Rule = dict[str, Any]


class Verdict(str, Enum):
    """Outcome of applying one rule to one protein."""

    SATISFIED = "SATISFIED"
    MISSING_REQUIRED = "MISSING_REQUIRED"
    EXCLUDED = "EXCLUDED"


@dataclass(frozen=True)
class ProteinFeatures:
    """The features of one protein that rules can test."""

    accession: str
    interpro: frozenset[str]
    transmembrane_segments: int


def load_rules(path: Path = RULES_PATH) -> list[Rule]:
    """Load the curated rules.

    >>> [r["id"] for r in load_rules()][:2]
    ['FRR:0001', 'FRR:0002']
    """
    data = yaml.safe_load(path.read_text())
    return list(data["rules"])


def evaluate(rule: Rule, features: ProteinFeatures) -> Verdict:
    """Apply one rule to one protein's features.

    An excluding feature takes precedence over a required one.
    """
    if features.interpro & {f["id"] for f in rule.get("excluded_by_any_of", [])}:
        return Verdict.EXCLUDED
    if features.interpro & {f["id"] for f in rule.get("requires_any_of", [])}:
        return Verdict.SATISFIED
    if (
        rule.get("requires_transmembrane_segment")
        and features.transmembrane_segments > 0
    ):
        return Verdict.SATISFIED
    return Verdict.MISSING_REQUIRED


def parse_uniprot_flatfile(text: str) -> ProteinFeatures:
    """Read the primary accession, InterPro entries and TRANSMEM count from a flat file."""
    accession = ""
    interpro: set[str] = set()
    tm = 0
    for line in text.splitlines():
        if line.startswith("AC   ") and not accession:
            accession = line[5:].split(";")[0].strip()
        elif line.startswith("DR   InterPro; "):
            interpro.add(line.split(";")[1].strip())
        elif line.startswith("FT   TRANSMEM"):
            tm += 1
    return ProteinFeatures(accession, frozenset(interpro), tm)


def parse_uniprot_tsv(text: str) -> dict[str, tuple[ProteinFeatures, dict[str, str]]]:
    """Parse UniProt REST TSV (Entry, Protein names, Organism, InterPro, Transmembrane)."""
    out: dict[str, tuple[ProteinFeatures, dict[str, str]]] = {}
    for row in csv.DictReader(io.StringIO(text), delimiter="\t"):
        interpro = frozenset(x for x in row["InterPro"].split(";") if x)
        features = ProteinFeatures(
            row["Entry"], interpro, row["Transmembrane"].count("TRANSMEM")
        )
        out[row["Entry"]] = (
            features,
            {"protein_name": row["Protein names"], "organism": row["Organism"]},
        )
    return out


def term_closures(rules: list[Rule]) -> dict[str, set[str]]:
    """Map each rule id to the GO ids it applies to.

    The closure is the term (with is_a descendants if asked) minus each exempt
    term and its is_a descendants.
    """
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    go = get_adapter("sqlite:obo:go")

    def subtree(term: str) -> set[str]:
        return set(go.descendants(term, predicates=[IS_A], reflexive=True))

    closures = {}
    for r in rules:
        term = r["term"]["id"]
        closure = subtree(term) if r["include_descendants"] else {term}
        for exempt in r.get("exempt_terms", []):
            closure -= subtree(exempt["id"])
        closures[r["id"]] = closure
    return closures


def _applies(rule: Rule, closure: set[str], go_id: str, qualifier: str) -> bool:
    """Whether a rule covers an annotation row.

    Negated rows are excluded explicitly: GOA writes them as ``NOT|enables``, and a
    NOT annotation already says the protein lacks the activity, so a rule has nothing
    to flag.

    >>> rule = {"qualifiers": ["enables"]}
    >>> _applies(rule, {"GO:1"}, "GO:1", "enables"), _applies(rule, {"GO:1"}, "GO:1", "NOT|enables")
    (True, False)
    """
    if qualifier.startswith("NOT"):
        return False
    return go_id in closure and qualifier in rule["qualifiers"]


def _flag_row(
    rule: Rule, verdict: Verdict, features: ProteinFeatures
) -> dict[str, str]:
    """Columns shared by sweep and acceptance rows."""
    excluded = features.interpro & {f["id"] for f in rule.get("excluded_by_any_of", [])}
    return {
        "rule_id": rule["id"],
        "strength": rule["strength"],
        "verdict": verdict.value,
        "excluding_features": ";".join(sorted(excluded)),
        "transmembrane_segments": str(features.transmembrane_segments),
    }


# --------------------------------------------------------------------------- sweep


def _review_actions(gene_dir: Path) -> dict[tuple[str, str, str], str]:
    """Map (term id, evidence, reference) to the review action in a gene's review."""
    paths = list(gene_dir.glob("*-ai-review.yaml"))
    if not paths:
        return {}
    review = yaml.load(
        paths[0].read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    )
    actions: dict[tuple[str, str, str], str] = {}
    for a in review.get("existing_annotations") or []:
        key = (
            str((a.get("term") or {}).get("id")),
            str(a.get("evidence_type")),
            str(a.get("original_reference_id")),
        )
        actions[key] = str((a.get("review") or {}).get("action") or "")
    return actions


def sweep_genes(
    gene_dirs: Iterable[Path], rules: list[Rule], closures: dict[str, set[str]]
) -> list[dict[str, str]]:
    """Flag GOA rows in gene folders that violate a rule.

    Only rows that violate a rule are returned. The review file is read only for
    genes with a violation.
    """
    out = []
    for gene_dir in sorted(gene_dirs):
        uniprot = list(gene_dir.glob("*-uniprot.txt"))
        goa = list(gene_dir.glob("*-goa.tsv"))
        if not uniprot or not goa:
            continue
        features = parse_uniprot_flatfile(uniprot[0].read_text(errors="replace"))
        flagged = []
        with goa[0].open() as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                for rule in rules:
                    if not _applies(
                        rule, closures[rule["id"]], row["GO TERM"], row["QUALIFIER"]
                    ):
                        continue
                    verdict = evaluate(rule, features)
                    if verdict is not Verdict.SATISFIED:
                        flagged.append((rule, verdict, row))
        if not flagged:
            continue
        actions = _review_actions(gene_dir)
        gene = f"{gene_dir.parent.name}/{gene_dir.name}"
        for rule, verdict, row in flagged:
            key = (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"])
            out.append(
                {
                    "gene": gene,
                    "accession": row["GENE PRODUCT ID"],
                    "go_id": row["GO TERM"],
                    "go_label": row["GO NAME"],
                    "qualifier": row["QUALIFIER"],
                    "evidence": row["GO EVIDENCE CODE"],
                    "reference": row["REFERENCE"],
                    "assigned_by": row["ASSIGNED BY"],
                    "review_action": actions.get(key, ""),
                    **_flag_row(rule, verdict, features),
                }
            )
    return out


# ---------------------------------------------------------------------- acceptance


def _get(url: str, accept: str) -> str:
    """GET with retries; network calls are the one place exceptions are retried."""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept})
            with urllib.request.urlopen(req, timeout=300) as resp:
                return str(resp.read().decode())
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def fetch_experimental_annotations(
    term: str, include_descendants: bool, cache_dir: Path
) -> list[dict[str, str]]:
    """Experimental protein annotations to a term from QuickGO (cached)."""
    cache = (
        cache_dir / f"quickgo-{term.replace(':', '_')}-{int(include_descendants)}.tsv"
    )
    if not cache.exists():
        params = {
            "goId": term,
            "goUsage": "descendants" if include_descendants else "exact",
            "goUsageRelationships": "is_a",
            "evidenceCode": EXPERIMENTAL_ECO,
            "evidenceCodeUsage": "descendants",
            "geneProductType": "protein",
            "downloadLimit": "2000000",
        }
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(
            _get(f"{QUICKGO_DOWNLOAD}?{urllib.parse.urlencode(params)}", "text/tsv")
        )
    return list(csv.DictReader(io.StringIO(cache.read_text()), delimiter="\t"))


def fetch_features(
    accessions: Iterable[str], cache_dir: Path
) -> dict[str, tuple[ProteinFeatures, dict[str, str]]]:
    """Features for UniProt accessions, fetched in batches and cached as JSON."""
    cache = cache_dir / "uniprot-features.json"
    stored: dict[str, Any] = json.loads(cache.read_text()) if cache.exists() else {}
    need = sorted(set(accessions) - set(stored))
    fields = "accession,protein_name,organism_name,xref_interpro,ft_transmem"
    for i in range(0, len(need), 200):
        query = urllib.parse.urlencode(
            {
                "accessions": ",".join(need[i : i + 200]),
                "fields": fields,
                "format": "tsv",
            }
        )
        for acc, (f, meta) in parse_uniprot_tsv(
            _get(f"{UNIPROT_ACCESSIONS}?{query}", "text/plain")
        ).items():
            stored[acc] = {
                "interpro": sorted(f.interpro),
                "tm": f.transmembrane_segments,
                **meta,
            }
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(stored))
    return {
        acc: (
            ProteinFeatures(acc, frozenset(v["interpro"]), v["tm"]),
            {"protein_name": v["protein_name"], "organism": v["organism"]},
        )
        for acc, v in stored.items()
    }


def acceptance(
    rules: list[Rule], closures: dict[str, set[str]], cache_dir: Path = CACHE_DIR
) -> tuple[list[dict[str, str]], list[dict[str, Any]]]:
    """Test rules against experimental GOA annotations.

    Returns (violating rows, one summary per rule). Rows are per protein and term;
    accessions are reduced to the canonical entry (isoform suffix dropped).
    """
    rows, summary = [], []
    for rule in rules:
        annotations = [
            a
            for a in fetch_experimental_annotations(
                rule["term"]["id"], rule["include_descendants"], cache_dir
            )
            if _applies(rule, closures[rule["id"]], a["GO TERM"], a["QUALIFIER"])
        ]
        by_protein: dict[str, list[dict[str, str]]] = defaultdict(list)
        for a in annotations:
            by_protein[a["GENE PRODUCT ID"].split("-")[0]].append(a)
        features = fetch_features(by_protein, cache_dir)
        verdicts: Counter[str] = Counter()
        for acc, anns in sorted(by_protein.items()):
            if acc not in features:
                verdicts["NOT_IN_UNIPROT"] += 1
                continue
            f, meta = features[acc]
            verdict = evaluate(rule, f)
            verdicts[verdict.value] += 1
            if verdict is Verdict.SATISFIED:
                continue
            rows.append(
                {
                    "accession": acc,
                    **meta,
                    "go_ids": ";".join(sorted({a["GO TERM"] for a in anns})),
                    "evidence": ";".join(sorted({a["GO EVIDENCE CODE"] for a in anns})),
                    "references": ";".join(sorted({a["REFERENCE"] for a in anns})),
                    "assigned_by": ";".join(sorted({a["ASSIGNED BY"] for a in anns})),
                    **_flag_row(rule, verdict, f),
                }
            )
        tested = sum(v for k, v in verdicts.items() if k != "NOT_IN_UNIPROT")
        flagged = tested - verdicts[Verdict.SATISFIED.value]
        summary.append(
            {
                "rule_id": rule["id"],
                "term": f"{rule['term']['id']} {rule['term']['label']}",
                "strength": rule["strength"],
                "proteins_tested": tested,
                "flagged": flagged,
                "flagged_fraction": round(flagged / tested, 3) if tested else None,
                "not_in_uniprot": verdicts["NOT_IN_UNIPROT"],
            }
        )
    return rows, summary


# ----------------------------------------------------------------------------- CLI


def _write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write rows as TSV with columns in first-seen order."""
    path.parent.mkdir(parents=True, exist_ok=True)
    columns: list[str] = []
    for r in rows:
        columns += [k for k in r if k not in columns]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=columns, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=["acceptance", "sweep"])
    parser.add_argument("--rules", type=Path, default=RULES_PATH)
    parser.add_argument("--out-dir", type=Path, default=REPORT_DIR)
    parser.add_argument("--genes-root", type=Path, default=REPO_ROOT / "genes")
    args = parser.parse_args(argv)
    rules = load_rules(args.rules)
    closures = term_closures(rules)
    if args.command == "acceptance":
        rows, summary = acceptance(rules, closures)
        _write_tsv(args.out_dir / "acceptance.tsv", rows)
        _write_tsv(args.out_dir / "acceptance-summary.tsv", summary)
        for s in summary:
            print(
                f"{s['rule_id']} {s['term']}: {s['flagged']}/{s['proteins_tested']} flagged"
            )
    else:
        rows = sweep_genes(args.genes_root.glob("*/*"), rules, closures)
        _write_tsv(args.out_dir / "sweep.tsv", rows)
        counts = Counter(
            (r["rule_id"], r["review_action"] or "UNREVIEWED") for r in rows
        )
        for (rule_id, action), n in sorted(counts.items()):
            print(f"{rule_id}\t{action}\t{n}")


if __name__ == "__main__":
    main()
