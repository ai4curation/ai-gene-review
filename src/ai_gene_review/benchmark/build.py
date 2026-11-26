"""Build time-split annotation benchmarks from a BenchmarkSpec.

Two modes share item assembly and grading:

* ``GOA_TIME_SPLIT``: targets are current-release rows that pass the spec's
  filters and are absent from the baseline release (see ``checks.novelty``).
* ``REVIEW_DERIVED``: targets are ACCEPT and NEW annotations from ai-gene-review
  reviews, kept only when they are also absent from the baseline release.

Sampling is seeded, so a spec plus its pinned sources reproduces the benchmark
(the UniProt feature query is current-only; its release is recorded).
"""

from __future__ import annotations

import random
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.benchmark.checks import (
    DIFFICULTY_ORDER,
    Context,
    difficulty,
    find_review,
    grading_results,
    knowledge_category,
    novelty,
    review_actions,
)
from ai_gene_review.benchmark.sources import (
    ASPECT_ROOTS,
    CAFA_EVIDENCE,
    DEFAULT_CACHE,
    Annotation,
    InformationContent,
    Ontology,
    by_protein,
    fetch_release,
    iter_positive,
    panther_subfamilies,
    pubmed_dates,
    read_gaf,
    snapshot,
    uniprot_records,
    uniprot_stream,
)
from ai_gene_review.evaluation.cafa import DEFAULT_EXCLUDED_TERMS

REVIEW_TARGET_ACTIONS = frozenset({"ACCEPT", "NEW"})


def load_context(spec: dict, cache: Path = DEFAULT_CACHE) -> tuple[Context, list[dict]]:
    """Fetch and load the spec's pinned sources; return the context and SourceSnapshots."""
    code = spec["taxon"]["gaf_code"]
    baseline_files = fetch_release(spec["baseline_release"], code, cache)
    current_files = fetch_release(spec["current_release"], code, cache)
    if spec["baseline_release"] > str(spec["cutoff_date"]):
        raise ValueError(
            f"baseline release {spec['baseline_release']} is after cutoff {spec['cutoff_date']}"
        )
    ontology = Ontology.load(current_files.ontology)
    baseline = by_protein(read_gaf(baseline_files.gaf))
    current = by_protein(read_gaf(current_files.gaf))
    experimental = {
        protein: {a.term for a in iter_positive(rows) if a.experimental}
        for protein, rows in baseline.items()
    }
    taxon_id = spec["taxon"]["id"].split(":")[1]
    panther_rows, uniprot_release = uniprot_stream(
        f"organism_id:{taxon_id} AND reviewed:true",
        "accession,xref_panther",
        cache,
        f"panther-{taxon_id}",
    )
    ctx = Context(
        ontology=ontology,
        baseline=baseline,
        current=current,
        ic=InformationContent.from_terms(ontology, experimental),
        subfamily=panther_subfamilies(panther_rows),
        near_duplicate_threshold=spec.get("near_duplicate_threshold", 0.8),
        cutoff=str(spec["cutoff_date"]),
        excluded_terms=frozenset(spec.get("excluded_terms") or DEFAULT_EXCLUDED_TERMS),
        cache=cache,
    )
    sources = [
        snapshot(
            "baseline_gaf",
            baseline_files.gaf_url,
            baseline_files.gaf,
            baseline_files.release,
        ),
        snapshot(
            "current_gaf",
            current_files.gaf_url,
            current_files.gaf,
            current_files.release,
        ),
        snapshot(
            "current_ontology",
            current_files.ontology_url,
            current_files.ontology,
            current_files.release,
        ),
        {
            "name": "panther_subfamilies",
            "url": "https://rest.uniprot.org/uniprotkb/stream",
            "release": uniprot_release,
            "query": f"organism_id:{taxon_id} AND reviewed:true (fields accession,xref_panther)",
        },
    ]
    return ctx, sources


def in_scope(ctx: Context, spec: dict, term: str, evidence: str) -> bool:
    """Does a term/evidence pair pass the spec's aspect, branch, evidence and exclusion filters?"""
    aspect = ctx.ontology.aspect(term)
    if aspect is None or term in ctx.excluded_terms or term in ctx.ontology.obsolete:
        return False
    if aspect not in (spec.get("aspects") or ASPECT_ROOTS):
        return False
    if evidence not in (spec.get("evidence_codes") or CAFA_EVIDENCE):
        return False
    branches = spec.get("go_branches")
    return not branches or bool(set(branches) & ctx.ontology.ancestors(term))


def goa_candidates(ctx: Context, spec: dict) -> dict[str, list[Annotation]]:
    """New current-release rows per protein that pass the spec filters."""
    candidates: dict[str, list[Annotation]] = defaultdict(list)
    for protein, rows in ctx.current.items():
        for a in rows:
            if a.negated and not spec.get("include_negated"):
                continue
            if not in_scope(ctx, spec, a.term, a.evidence):
                continue
            if novelty(ctx, protein, a.term, a.negated)["status"] == "PASS":
                candidates[protein].append(a)
    cap = spec.get("max_proteins_per_reference")
    if cap:
        proteins_by_ref: dict[str, set[str]] = defaultdict(set)
        for protein, rows in candidates.items():
            for a in rows:
                proteins_by_ref[a.reference].add(protein)
        bulk = {ref for ref, proteins in proteins_by_ref.items() if len(proteins) > cap}
        candidates = defaultdict(
            list,
            {
                protein: kept
                for protein, rows in candidates.items()
                if (kept := [a for a in rows if a.reference not in bulk])
            },
        )
    return dict(candidates)


def target_from_row(
    ctx: Context, a: Annotation, extra_refs: list[str]
) -> dict[str, Any]:
    """TargetAnnotation dict from a current-release GAF row."""
    target: dict[str, Any] = {
        "term": {"id": a.term, "label": ctx.ontology.label(a.term)},
        "aspect": a.aspect,
        "qualifier": a.qualifier,
        "evidence_code": a.evidence,
        "reference": a.reference,
        "assigned_by": a.assigned_by,
        "date": a.date,
        "source": "GOA_RELEASE",
    }
    if a.negated:
        target["negated"] = True
    if a.with_from:
        target["with_from"] = a.with_from
    if extra_refs:
        target["notes"] = "also supported by " + ", ".join(extra_refs)
    return target


def collapse_rows(ctx: Context, rows: list[Annotation]) -> list[dict[str, Any]]:
    """One target per (term, negated); the first reference in sort order represents the rest."""
    grouped: dict[tuple[str, bool], list[Annotation]] = defaultdict(list)
    for a in rows:
        grouped[(a.term, a.negated)].append(a)
    targets = []
    for key in sorted(grouped):
        ordered = sorted(grouped[key], key=lambda a: (a.reference, a.evidence))
        others = sorted({a.reference for a in ordered[1:]} - {ordered[0].reference})
        targets.append(target_from_row(ctx, ordered[0], others))
    return targets


def grade(ctx: Context, protein: str, target: dict) -> None:
    """Set knowledge_category and difficulty on a target in place."""
    target["knowledge_category"] = knowledge_category(ctx, protein, target["aspect"])
    if not target.get("negated"):
        target["difficulty"] = difficulty(
            grading_results(ctx, protein, target["term"]["id"])
        )


def attach_review(genes_dir: Path, item: dict) -> None:
    """Record the ai-gene-review action on each target, when the gene has a review."""
    review = find_review(
        genes_dir, item.get("gene_symbol"), item["protein"].split(":", 1)[1]
    )
    if review is None:
        return
    for target in item["target_annotations"]:
        target["review_file"] = str(review)
        actions = review_actions(review, target["term"]["id"])
        if actions and "review_action" not in target:
            target["review_action"] = ",".join(actions)


def make_item(
    ctx: Context,
    spec: dict,
    protein: str,
    symbol: str,
    name: str,
    targets: list[dict],
    features: list[dict],
    rng: random.Random,
    genes_dir: Path,
) -> dict[str, Any]:
    """Assemble and grade one BenchmarkItem."""
    for target in targets:
        grade(ctx, protein, target)
    item: dict[str, Any] = {
        "id": f"{spec['id']}-{protein.split(':', 1)[1]}",
        "protein": protein,
        "gene_symbol": symbol,
        "protein_name": name,
        "taxon": spec["taxon"]["id"],
        "split": "DEV" if rng.random() < spec.get("dev_fraction", 0.0) else "TEST",
        "target_annotations": targets,
    }
    if features:
        item["features"] = features
    item = {k: v for k, v in item.items() if v not in ("", None)}
    graded = [t["difficulty"] for t in targets if "difficulty" in t]
    if graded:
        item["difficulty"] = max(graded, key=DIFFICULTY_ORDER.__getitem__)
    attach_review(genes_dir, item)
    return item


def feature_members(spec: dict, cache: Path) -> tuple[dict[str, list[str]], list[dict]]:
    """For each feature quota, the proteins its UniProt query returns; plus SourceSnapshots."""
    members: dict[str, list[str]] = {}
    sources = []
    for quota in spec.get("features") or []:
        rows, release = uniprot_stream(
            quota["uniprot_query"],
            "accession,gene_primary,protein_name",
            cache,
            f"feature-{spec['id']}-{quota['feature'].lower()}",
        )
        members[quota["feature"]] = sorted(f"UniProtKB:{r['Entry']}" for r in rows)
        sources.append(
            {
                "name": f"feature_{quota['feature'].lower()}",
                "url": "https://rest.uniprot.org/uniprotkb/stream",
                "release": release,
                "query": quota["uniprot_query"],
            }
        )
    return members, sources


def feature_record(quota: dict) -> dict[str, Any]:
    """ItemFeature for a protein matched by a quota's query."""
    return {
        "feature": quota["feature"],
        "source": f"UniProtKB query: {quota['uniprot_query']}",
        "literature_checked": False,
    }


def pmid(reference: str) -> str | None:
    """Bare PMID of a PMID: reference.

    >>> pmid("PMID:123"), pmid("GO_REF:0000024")
    ('123', None)
    """
    return reference.split(":", 1)[1] if reference.startswith("PMID:") else None


def recent_enough(floor: str | None, references: list[str], cache: Path) -> set[str]:
    """References whose PubMed date is on or after ``floor`` (all references when floor is unset)."""
    if not floor:
        return set(references)
    dates = pubmed_dates([p for r in references if (p := pmid(r))], cache)
    return {r for r in references if (p := pmid(r)) and dates.get(p, "") >= str(floor)}


def date_filtered(
    candidates: dict[str, list[Annotation]], floor: str | None, cache: Path
) -> dict[str, list[Annotation]]:
    """Candidates restricted to rows whose reference passes ``recent_enough``."""
    if not floor:
        return candidates
    keep = recent_enough(
        floor,
        sorted({a.reference for rows in candidates.values() for a in rows}),
        cache,
    )
    return {
        p: kept
        for p, rows in candidates.items()
        if (kept := [a for a in rows if a.reference in keep])
    }


def add_sequences(items: list[dict], cache: Path) -> None:
    """Pin each item's current UniProt name, entry name, sequence and sequence version."""
    records = uniprot_records((i["protein"].split(":", 1)[1] for i in items), cache)
    for item in items:
        record = records.get(item["protein"].split(":", 1)[1])
        if record is None:
            continue
        item["entry_name"] = record["Entry Name"]
        item.setdefault("protein_name", record["Protein names"].split(" (")[0])
        item["sequence_version"] = int(record["Sequence version"])
        item["sequence"] = record["Sequence"]


def add_reference_dates(items: list[dict], cache: Path) -> None:
    """Record PubMed publication dates on targets with PMID references."""
    targets = [t for item in items for t in item["target_annotations"]]
    dates = pubmed_dates([p for t in targets if (p := pmid(t["reference"]))], cache)
    for target in targets:
        found = dates.get(pmid(target["reference"]) or "")
        if found:
            target["reference_date"] = found


def related(ctx: Context, a: str, b: str) -> bool:
    """True when either term entails the other."""
    return a in ctx.ontology.ancestors(b) or b in ctx.ontology.ancestors(a)


def add_decoys(ctx: Context, spec: dict, items: list[dict], rng: random.Random) -> None:
    """Give each item decoy terms drawn from other items' positive targets."""
    count = spec.get("decoys_per_item", 0)
    if not count:
        return
    pool = sorted(
        {
            (t["term"]["id"], item["id"])
            for item in items
            for t in item["target_annotations"]
            if not t.get("negated")
        }
    )
    for item in items:
        known = {
            ctx.ontology.resolve(a.term)
            for a in iter_positive(ctx.current.get(item["protein"], []))
        }
        known |= {t["term"]["id"] for t in item["target_annotations"]}
        eligible = sorted(
            {
                term: source
                for term, source in pool
                if source != item["id"]
                and not any(related(ctx, term, k) for k in known)
            }.items()
        )
        decoys = rng.sample(eligible, min(count, len(eligible)))
        item["decoys"] = [
            {
                "term": {"id": term, "label": ctx.ontology.label(term)},
                "aspect": ctx.ontology.aspect(term),
                "drawn_from": source,
            }
            for term, source in sorted(decoys)
        ]


def finish(
    spec: dict,
    ctx: Context,
    sources: list[dict],
    items: list[dict],
    cache: Path,
    rng: random.Random,
) -> dict[str, Any]:
    """Pin sequences and reference dates, draw decoys, and wrap the items in a Benchmark."""
    add_sequences(items, cache)
    add_reference_dates(items, cache)
    add_decoys(ctx, spec, items, rng)
    sources = sources + [
        {
            "name": "uniprot_sequences",
            "url": "https://rest.uniprot.org/uniprotkb/stream",
            "query": f"accessions of the {len(items)} items (fields {'accession,id,protein_name,sequence_version,sequence'})",
        },
        {
            "name": "pubmed_dates",
            "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
            "query": "sortpubdate of each PMID target reference",
        },
    ]
    return benchmark_shell(spec, sources, items)


def benchmark_shell(
    spec: dict, sources: list[dict], items: list[dict]
) -> dict[str, Any]:
    """Benchmark dict around drawn items."""
    out: dict[str, Any] = {
        "id": spec["id"],
        "title": spec["title"],
        "created": date.today().isoformat(),
        "spec": spec,
        "sources": sources,
        "items": sorted(items, key=lambda i: i["id"]),
    }
    if spec.get("description"):
        out["description"] = spec["description"]
    return out


def build_goa(
    spec: dict, ctx: Context, sources: list[dict], cache: Path, genes_dir: Path
) -> dict[str, Any]:
    """Draw a GOA_TIME_SPLIT benchmark."""
    rng = random.Random(spec.get("seed", 0))
    all_candidates = goa_candidates(ctx, spec)
    candidates = date_filtered(all_candidates, spec.get("min_reference_date"), cache)
    members, feature_sources = feature_members(spec, cache)
    quotas = spec.get("features") or []

    def features_of(protein: str) -> list[dict]:
        return [feature_record(q) for q in quotas if protein in members[q["feature"]]]

    chosen: dict[str, list[dict]] = {}
    rows_of: dict[str, list[Annotation]] = {}
    for quota in quotas:
        quota_candidates = date_filtered(
            all_candidates,
            quota.get("min_reference_date", spec.get("min_reference_date")),
            cache,
        )
        pool = [
            p
            for p in members[quota["feature"]]
            if p in quota_candidates and p not in chosen
        ]
        for protein in rng.sample(pool, min(quota["count"], len(pool))):
            chosen[protein] = features_of(protein)
            rows_of[protein] = quota_candidates[protein]
    remaining = sorted(set(candidates) - set(chosen))
    for protein in rng.sample(
        remaining, min(spec["size"] - len(chosen), len(remaining))
    ):
        chosen[protein] = features_of(protein)
        rows_of[protein] = candidates[protein]
    items = []
    for protein in sorted(chosen):
        rows = rows_of[protein]
        items.append(
            make_item(
                ctx,
                spec,
                protein,
                rows[0].symbol,
                rows[0].name,
                collapse_rows(ctx, rows),
                chosen[protein],
                rng,
                genes_dir,
            )
        )
    return finish(spec, ctx, sources + feature_sources, items, cache, rng)


def review_targets(ctx: Context, spec: dict, review: dict, path: Path) -> list[dict]:
    """New, in-scope ACCEPT/NEW targets from one review."""
    protein = f"UniProtKB:{review['id']}"
    targets = []
    seen = set()
    for row in review.get("existing_annotations") or []:
        action = (row.get("review") or {}).get("action")
        term = (row.get("term") or {}).get("id", "")
        evidence = row.get("evidence_type", "")
        negated = bool(row.get("negated"))
        if action not in REVIEW_TARGET_ACTIONS or (term, negated) in seen:
            continue
        if negated and not spec.get("include_negated"):
            continue
        if not in_scope(ctx, spec, term, evidence):
            continue
        if novelty(ctx, protein, term, negated)["status"] != "PASS":
            continue
        reference = row.get("original_reference_id") or next(
            (
                s.get("reference_id")
                for s in (row.get("review") or {}).get("supported_by") or []
            ),
            None,
        )
        if not reference:
            continue
        seen.add((term, negated))
        target: dict[str, Any] = {
            "term": {"id": term, "label": ctx.ontology.label(term)},
            "aspect": ctx.ontology.aspect(term),
            "evidence_code": evidence,
            "reference": reference,
            "source": "AIGR_REVIEW",
            "review_action": action,
            "review_file": str(path),
        }
        if negated:
            target["negated"] = True
        targets.append(target)
    return targets


def build_from_reviews(
    spec: dict,
    ctx: Context,
    sources: list[dict],
    review_paths: list[Path],
    genes_dir: Path,
    cache: Path,
) -> dict[str, Any]:
    """Draw a REVIEW_DERIVED benchmark from the given review files."""
    rng = random.Random(spec.get("seed", 0))
    items = []
    for path in sorted(review_paths):
        review = yaml.safe_load(path.read_text())
        targets = review_targets(ctx, spec, review, path)
        keep = recent_enough(
            spec.get("min_reference_date"), [t["reference"] for t in targets], cache
        )
        targets = [t for t in targets if t["reference"] in keep]
        if targets:
            items.append(
                make_item(
                    ctx,
                    spec,
                    f"UniProtKB:{review['id']}",
                    review.get("gene_symbol", ""),
                    "",
                    targets,
                    [],
                    rng,
                    genes_dir,
                )
            )
    items = items[: spec["size"]]
    sources = sources + [
        {
            "name": "aigr_reviews",
            "url": "https://github.com/ai4curation/ai-gene-review",
            "query": " ".join(str(p) for p in sorted(review_paths)),
        }
    ]
    return finish(spec, ctx, sources, items, cache, rng)
