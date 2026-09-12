"""Render curation indexes from authored FamilyReview YAML and frozen scope."""

import collections
import csv
import json
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
PUBLIC = "https://github.com/ai4curation/ai-gene-review/blob/main/"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def gene_name(row):
    symbol, species = row["gene_symbol"], row["species"]
    if (ROOT / "genes" / species / symbol).is_dir():
        return species + "/" + symbol
    return symbol + " (" + species + ")"


def main():
    scope = list(csv.DictReader((BASE / "scope.csv").open()))
    mapping = list(csv.DictReader((BASE / "mapping.csv").open()))
    groups = json.loads((BASE / "family-groups.json").read_text())
    extra = json.loads((BASE / "additional-context-families.json").read_text())
    unassigned = json.loads((BASE / "unassigned-results.json").read_text())
    unmapped = {r["accession"]: r for r in unassigned["cases"]}
    families = sorted(set(groups) | {r["family"] for r in extra})
    docs = {
        f: yaml.safe_load(
            (ROOT / "interpro/panther" / f / f"{f}-review.yaml").read_text()
        )
        for f in families
    }
    bridges = {}
    for bridge in unassigned["verified_same_gene_bridges"]:
        assert bridge["relationship"] == "SAME_GENE_CONTEXT_ONLY"
        assert bridge["shared_gene_identifiers"]
        context_families = {value.split(":")[0] for value in bridge["context_panther"]}
        assert len(context_families) == 1, (
            "Multiple context families require explicit indexing"
        )
        bridges[bridge["target_accession"]] = next(iter(context_families))
    roles = collections.defaultdict(set)
    for row in scope:
        roles[row["accession"]].add(row["role"])
    coverage = []
    for r in mapping:
        row = dict(r)
        assigned = list(filter(None, r["families"].split(";")))
        row.update(
            roles=";".join(sorted(roles[r["accession"]])),
            family_reviews=";".join(
                f"interpro/panther/{f}/{f}-review.yaml" for f in assigned
            ),
            gene_context_family=bridges.get(r["accession"], ""),
            curation_status="FAMILY_BOUNDARY_REVIEW"
            if assigned
            else "INDIVIDUAL_DOMAIN_FAMILY_ASSESSMENT",
            unassigned_assessment=unmapped.get(r["accession"], {}).get(
                "assessment", ""
            ),
        )
        coverage.append(row)
    with (BASE / "coverage.csv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(coverage[0]))
        writer.writeheader()
        writer.writerows(coverage)
    summary = {
        "cohort_memberships": len(scope),
        "distinct_accessions": len(mapping),
        "distinct_prediction_targets": sum(
            "prediction_target" in v for v in roles.values()
        ),
        "distinct_paired_references": sum(
            "paired_reference" in v for v in roles.values()
        ),
        "mapped_exact_accessions": sum(bool(r["families"]) for r in mapping),
        "unassigned_exact_accessions": len(unmapped),
        "exact_assignment_families": len(groups),
        "additional_context_families": len(extra),
        "family_reviews": len(docs),
        "review_status": dict(
            collections.Counter(d["review_status"] for d in docs.values())
        ),
        "functional_coherence": dict(
            collections.Counter(d["functional_coherence"] for d in docs.values())
        ),
        "term_scopes": dict(
            collections.Counter(
                t["scope"] for d in docs.values() for t in d.get("term_assessments", [])
            )
        ),
        "cohorts": dict(collections.Counter(r["cohort"] for r in scope)),
    }
    (BASE / "coverage-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        "---",
        'title: "ProtNLM family curation: gene index"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Gene-to-family index",
        "",
        "[Family curation overview](../family-curation.md) · [Family assessments](family-index.md)",
        "",
        "Every selected exact protein record and paired human reference is listed once. A gene-context link is not a PANTHER assignment for the exact input.",
        "",
        "| Gene / organism | Exact accession | Cohorts | Exact-record family review | Separate gene context / unassigned assessment |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(
        coverage, key=lambda x: (x["species"], x["gene_symbol"], x["accession"])
    ):
        exact = (
            ", ".join(
                f"[{f}](family-index.md#{f.lower()})"
                for f in r["families"].split(";")
                if f
            )
            or "Unassigned"
        )
        context = r["gene_context_family"]
        detail = (
            f"Canonical context: [{context}](family-index.md#{context.lower()}). "
            if context
            else ""
        )
        if r["unassigned_assessment"]:
            detail += f"[{cell(r['unassigned_assessment'])}](unassigned-cases.md)"
        lines.append(
            f"| {cell(gene_name(r))} | [{r['accession']}](https://www.uniprot.org/uniprotkb/{r['accession']}/entry) | {cell(r['cohort'])} | {exact} | {detail} |"
        )
    (BASE / "gene-index.md").write_text("\n".join(lines) + "\n")
    lines = [
        "---",
        'title: "ProtNLM benchmark family assessments"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Family assessments",
        "",
        "[Overview](../family-curation.md) · [Gene index](gene-index.md)",
        "",
        "An unresolved family grant can coexist with strong evidence for a particular member. Listed subfamilies and representatives are a scoped set, not an exhaustive phylogeny.",
        "",
    ]
    status_rows = []
    lines += [
        "Review status records whether curation is complete. Term scope records whether a family-wide transfer is supported; COMPLETE does not imply FAMILY_WIDE.",
        "",
        "[Filterable scope data](family-status.csv) separates unresolved term boundaries from review completion.",
        "",
        "| Family | Review status | Term scopes |",
        "|---|---|---|",
    ]
    for f in families:
        d = docs[f]
        scopes = collections.Counter(t["scope"] for t in d.get("term_assessments", []))
        label = "; ".join(f"{scope}: {count}" for scope, count in sorted(scopes.items())) or "No term grants asserted"
        status_rows.append({"family_id": f, "review_status": d["review_status"],
                            "term_scopes": label, "unresolved_terms": scopes["UNRESOLVED"],
                            "family_wide_terms": scopes["FAMILY_WIDE"]})
        lines.append(f"| [{f}](#{f.lower()}) | {d['review_status']} | {label} |")
    lines += [""]
    with (BASE / "family-status.csv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(status_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(status_rows)
    for f in families:
        d = docs[f]
        lines += [
            f"## {f}",
            "",
            f"**{d.get('preferred_name', d['family_name'])}** — {d['functional_coherence']}; {d['review_status']}",
            "",
            d["summary"],
            "",
            d.get("coherence_reason", ""),
            "",
        ]
        members = ", ".join(
            gene_name(r) + " (" + r["accession"] + ")" for r in groups.get(f, [])
        )
        if members:
            lines += ["**Exact benchmark/reference members:** " + members, ""]
        if f in bridges.values():
            targets = ", ".join(a for a, context in bridges.items() if context == f)
            lines += [
                f"**Separate canonical gene context:** {targets}; exact inputs remain unassigned. See [identity evidence](unassigned-cases.md).",
                "",
            ]
        if d.get("term_assessments"):
            lines += [
                "| Function / process / component | Scope | Boundary |",
                "|---|---|---|",
            ]
            for t in d["term_assessments"]:
                term = t["assessed_term"]
                lines.append(
                    f"| [{cell(term['label'])}](https://www.ebi.ac.uk/QuickGO/term/{term['id']}) ({term['id']}) | {t['scope']} | {cell(t.get('scope_reason', ''))} |"
                )
            lines += [""]
        path = f"interpro/panther/{f}/{f}-review.yaml"
        lines += [f"[Structured review and supporting sources]({PUBLIC}{path})", ""]
    (BASE / "family-index.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
