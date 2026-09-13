"""Survey the IEP (Inferred from Expression Pattern) evidence code across the corpus.

Two independent views are produced, because they answer different questions:

1. **GOA view** -- every ``genes/*/*/*-goa.tsv`` row, i.e. what GOA actually
   ships. This gives aspect, qualifier, assigned-by and taxon distributions for
   IEP without any reviewer bias, and lets us check GO's own rule that IEP is
   restricted to biological process.
2. **Review view** -- every ``genes/*/*/*-ai-review.yaml`` annotation with
   ``evidence_type: IEP``. This gives the reviewer disposition (ACCEPT,
   REMOVE, ...) and, crucially, the same disposition for the other evidence
   codes so IEP can be compared against a baseline rather than judged in a
   vacuum.

A third measurement asks whether an IEP row is *load-bearing*: for each IEP
annotation, does the same gene review carry the same GO term (exact id) under a
non-IEP evidence code? An IEP row that merely duplicates an IDA/IMP call costs
nothing; an IEP row that is the sole support for a term is where the evidence
code's weakness actually propagates into the annotation set.

Run::

    uv run python projects/IEP/iep_corpus_survey.py

The GO closure is computed with OAK against ``sqlite:obo:go`` by default. Set
``IEP_GO_ADAPTER`` to any other OAK selector (e.g.
``pronto:/path/to/go-basic.obo``) if the SQLite build is unreachable.

Writes ``projects/IEP/iep-corpus-survey.md`` and prints a summary.
"""

from __future__ import annotations

import csv
import os
import re
import statistics
from collections import Counter, defaultdict
from math import ceil, comb
from pathlib import Path

import yaml

from ai_gene_review.analysis.subtraction_report import make_go_ancestor_fn

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = Path(__file__).resolve().parent / "iep-corpus-survey.md"
GO_ADAPTER = os.environ.get("IEP_GO_ADAPTER", "sqlite:obo:go")

# GOA caches do not all use the same aspect vocabulary: most spell the aspect
# out, a few use the single-letter GAF convention. Normalise so the aspect
# tallies (and the GORULE:0000006 check that reads them) are not split across
# two spellings of the same value.
ASPECTS = {
    "P": "biological_process",
    "F": "molecular_function",
    "C": "cellular_component",
}

# Coarse GO branches used to characterise what IEP is actually used to say.
# Order matters: the first matching branch wins, so the more specific
# stimulus-response branch is tested before the generic development branch.
# Terms parented under both (e.g. a defence-response term that is also a
# developmental one) are therefore counted as stimulus-response.
BRANCHES = [
    ("GO:0050896", "response to stimulus"),
    ("GO:0032502", "developmental process"),
    ("GO:0065007", "biological regulation"),
    ("GO:0008152", "metabolic process"),
    ("GO:0051179", "localization"),
    ("GO:0005575", "cellular component"),
    ("GO:0003674", "molecular function"),
]

# Evidence codes compared against IEP in the disposition table. Chosen to span
# the experimental codes IEP sits alongside plus the two big inferred codes.
BASELINE_CODES = ["IDA", "IMP", "IGI", "IPI", "IEP", "IBA", "ISO", "IEA", "TAS", "NAS"]

# Disposition columns. ``UNREVIEWED`` is the bucket for annotations carrying no
# ``review.action`` at all; it is listed so the action columns sum to the
# reviewed total rather than silently dropping rows out of the table.
ACTIONS = [
    "ACCEPT",
    "KEEP_AS_NON_CORE",
    "MODIFY",
    "MARK_AS_OVER_ANNOTATED",
    "REMOVE",
    "UNDECIDED",
    "PENDING",
    "UNREVIEWED",
]
# Actions that say "this annotation, as written, is not a keeper".
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}


def survey_goa() -> dict:
    """Tally IEP rows across every cached GOA file."""
    aspects: Counter[str] = Counter()
    qualifiers: Counter[str] = Counter()
    assigned_by: Counter[str] = Counter()
    taxa: Counter[str] = Counter()
    terms: Counter[tuple[str, str]] = Counter()
    code_totals: Counter[str] = Counter()
    genes_with_iep: set[str] = set()
    total_rows = 0

    for path in sorted(REPO_ROOT.glob("genes/*/*/*-goa.tsv")):
        with open(path, newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                code = (row.get("GO EVIDENCE CODE") or "").strip()
                if not code:
                    continue
                total_rows += 1
                code_totals[code] += 1
                if code != "IEP":
                    continue
                genes_with_iep.add(str(path.parent.relative_to(REPO_ROOT / "genes")))
                aspect = (row.get("GO ASPECT") or "?").strip()
                aspects[ASPECTS.get(aspect, aspect)] += 1
                qualifiers[(row.get("QUALIFIER") or "?").strip()] += 1
                assigned_by[(row.get("ASSIGNED BY") or "?").strip()] += 1
                taxa[(row.get("TAXON NAME") or "?").strip()] += 1
                terms[
                    (
                        (row.get("GO TERM") or "?").strip(),
                        (row.get("GO NAME") or "?").strip(),
                    )
                ] += 1

    return {
        "total_rows": total_rows,
        "code_totals": code_totals,
        "aspects": aspects,
        "qualifiers": qualifiers,
        "assigned_by": assigned_by,
        "taxa": taxa,
        "terms": terms,
        "genes_with_iep": genes_with_iep,
    }


def classify_branch(term_id: str, ancestors) -> str:
    """Name the coarse GO branch ``term_id`` falls under (first match wins)."""
    anc = ancestors(term_id)
    for root, label in BRANCHES:
        if root in anc:
            return label
    return "unclassified"


def survey_reviews(ancestors) -> dict:
    """Tally reviewer dispositions for IEP rows and for the baseline codes."""
    # evidence code -> action -> count
    disposition: dict[str, Counter[str]] = defaultdict(Counter)
    # evidence code -> [rows, rows whose term is in core_functions]
    core_grounding: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    branches: Counter[str] = Counter()
    branch_negative: Counter[str] = Counter()
    # (species, branch) -> rows / flagged rows, so the branch flag rates can be
    # checked for species confounding rather than pooled across the corpus.
    branch_by_species: Counter[tuple[str, str]] = Counter()
    branch_by_species_negative: Counter[tuple[str, str]] = Counter()
    # branch -> distinct gene directories contributing rows / flagged rows.
    branch_genes: defaultdict[str, set[str]] = defaultdict(set)
    branch_negative_genes: defaultdict[str, set[str]] = defaultdict(set)
    iep_terms: Counter[tuple[str, str]] = Counter()
    iep_negative_terms: Counter[tuple[str, str]] = Counter()
    iep_files: set[str] = set()
    iep_by_species: Counter[str] = Counter()
    iep_by_gene: Counter[str] = Counter()
    # (species, gene, term, label, action, reason)
    iep_rows: list[tuple[str, str, str, str, str, str]] = []
    corroborated = 0
    sole_support = 0
    sole_support_negative = 0
    # Closure-aware variant of the same measurement: an IEP row also counts as
    # corroborated when a non-IEP row in the same review carries an ancestor or
    # descendant of its term (an IDA ``cellular response to heat`` corroborates
    # an IEP ``response to heat``).
    corroborated_closure = 0
    core_grounded = 0
    core_grounded_accept = 0

    for path in sorted(REPO_ROOT.glob("genes/*/*/*-ai-review.yaml")):
        with open(path) as fh:
            review = yaml.safe_load(fh)
        if not isinstance(review, dict):
            continue
        anns = review.get("existing_annotations") or []
        if not isinstance(anns, list):
            continue

        species = path.parent.parent.name
        gene = review.get("gene_symbol") or path.parent.name

        # Terms carried by non-IEP evidence in this same review.
        non_iep_terms = {
            (ann.get("term") or {}).get("id")
            for ann in anns
            if isinstance(ann, dict)
            and ann.get("evidence_type") != "IEP"
            and not ann.get("negated")
        }
        core_terms = collect_core_terms(review)

        for ann in anns:
            if not isinstance(ann, dict):
                continue
            code = ann.get("evidence_type")
            action = (
                (ann.get("review") or {}) if isinstance(ann.get("review"), dict) else {}
            ).get("action")
            term = ann.get("term") or {}
            term_id = term.get("id") or "?"
            term_label = term.get("label") or "?"
            if code:
                disposition[code][action or "UNREVIEWED"] += 1
                core_grounding[code][0] += 1
                if term_id in core_terms:
                    core_grounding[code][1] += 1
            if code != "IEP":
                continue
            reason = (
                (ann.get("review") or {}).get("reason")
                if isinstance(ann.get("review"), dict)
                else None
            ) or ""

            gene_key = f"{species}/{path.parent.name}"
            iep_files.add(str(path.relative_to(REPO_ROOT)))
            iep_by_species[species] += 1
            iep_by_gene[gene_key] += 1
            iep_terms[(term_id, term_label)] += 1
            iep_rows.append(
                (
                    species,
                    str(gene),
                    term_id,
                    term_label,
                    action or "UNREVIEWED",
                    reason,
                )
            )
            branch = classify_branch(term_id, ancestors)
            branches[branch] += 1
            branch_by_species[(species, branch)] += 1
            branch_genes[branch].add(gene_key)
            if action in NEGATIVE_ACTIONS:
                iep_negative_terms[(term_id, term_label)] += 1
                branch_negative[branch] += 1
                branch_by_species_negative[(species, branch)] += 1
                branch_negative_genes[branch].add(gene_key)
            if term_id in non_iep_terms:
                corroborated += 1
                corroborated_closure += 1
            else:
                sole_support += 1
                if action in NEGATIVE_ACTIONS:
                    sole_support_negative += 1
                if related_by_closure(term_id, non_iep_terms, ancestors):
                    corroborated_closure += 1
            if term_id in core_terms:
                core_grounded += 1
                if action == "ACCEPT":
                    core_grounded_accept += 1

    return {
        "disposition": disposition,
        "core_grounding": core_grounding,
        "branches": branches,
        "branch_negative": branch_negative,
        "branch_by_species": branch_by_species,
        "branch_by_species_negative": branch_by_species_negative,
        "branch_genes": branch_genes,
        "branch_negative_genes": branch_negative_genes,
        "iep_terms": iep_terms,
        "iep_negative_terms": iep_negative_terms,
        "iep_files": iep_files,
        "iep_by_species": iep_by_species,
        "iep_by_gene": iep_by_gene,
        "iep_rows": iep_rows,
        "corroborated": corroborated,
        "corroborated_closure": corroborated_closure,
        "sole_support": sole_support,
        "sole_support_negative": sole_support_negative,
        "core_grounded": core_grounded,
        "core_grounded_accept": core_grounded_accept,
    }


def related_by_closure(term_id: str, other_terms, ancestors) -> bool:
    """True if any of ``other_terms`` is an ancestor or descendant of ``term_id``.

    Used for the closure-aware corroboration count: exact term-id equality
    misses the common case where the corroborating evidence sits on a
    neighbouring term in the same lineage.
    """
    anc = ancestors(term_id)
    for other in other_terms:
        if not other or other == term_id:
            continue
        if other in anc or term_id in ancestors(other):
            return True
    return False


def concentration(counts: Counter[str]) -> dict:
    """Summarise how unevenly IEP rows are spread over the genes carrying them."""
    values = sorted(counts.values(), reverse=True)
    total = sum(values)
    if not values:
        return {"genes": 0, "rows": 0, "median": 0, "top_decile_genes": 0}
    top_n = max(1, ceil(0.10 * len(values)))
    heavy = [v for v in values if v >= 5]
    return {
        "genes": len(values),
        "rows": total,
        "median": statistics.median(values),
        "max": values[0],
        "top_decile_genes": top_n,
        "top_decile_rows": sum(values[:top_n]),
        "heavy_genes": len(heavy),
        "heavy_rows": sum(heavy),
    }


def collect_core_terms(review: dict) -> set[str]:
    """GO term ids appearing anywhere in a review's ``core_functions`` block."""
    out: set[str] = set()
    for cf in review.get("core_functions") or []:
        if not isinstance(cf, dict):
            continue
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            val = cf.get(slot)
            if isinstance(val, dict) and val.get("id"):
                out.add(val["id"])
        for slot in (
            "locations",
            "in_complex",
            "directly_involved_in",
            "anatomical_locations",
        ):
            vals = cf.get(slot)
            if isinstance(vals, list):
                for v in vals:
                    if isinstance(v, dict) and v.get("id"):
                        out.add(v["id"])
            elif isinstance(vals, dict) and vals.get("id"):
                out.add(vals["id"])
        for sub in cf.get("supported_by") or []:
            if isinstance(sub, dict) and isinstance(sub.get("term"), dict):
                if sub["term"].get("id"):
                    out.add(sub["term"]["id"])
    return out


def go_release() -> str:
    """The GO release the closure was computed against, for provenance.

    Recorded instead of the adapter string, which may be a machine-local path
    when ``IEP_GO_ADAPTER`` is used and would be meaningless to a reader.
    """
    from oaklib import get_adapter

    try:
        meta = get_adapter(GO_ADAPTER).ontology_metadata_map("go")
    except Exception:
        return "unknown"
    for values in meta.values():
        for value in values if isinstance(values, list) else [values]:
            match = re.search(r"\d{4}-\d{2}-\d{2}", str(value))
            if match:
                return match.group(0)
    return "unknown"


def pct(n: int, d: int) -> str:
    return f"{100.0 * n / d:.1f}%" if d else "n/a"


def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p for the 2x2 table ``[[a, b], [c, d]]``.

    Computed by summing hypergeometric probabilities no larger than the
    observed one. Written out rather than pulling in SciPy so the survey has no
    dependency beyond what the reviews themselves need; verified against
    ``scipy.stats.fisher_exact``.
    """
    n = a + b + c + d
    if not n or not (a + b) or not (c + d) or not (a + c) or not (b + d):
        return 1.0
    row1, col1 = a + b, a + c
    denom = comb(n, col1)

    def prob(x: int) -> float:
        return comb(row1, x) * comb(n - row1, col1 - x) / denom

    observed = prob(a)
    lo = max(0, col1 - (n - row1))
    hi = min(row1, col1)
    # Relative tolerance guards against summing away a tie lost to rounding.
    total = sum(
        p for x in range(lo, hi + 1) if (p := prob(x)) <= observed * 1e-7 + observed
    )
    return min(1.0, total)


def main() -> None:
    ancestors = make_go_ancestor_fn(GO_ADAPTER)
    goa = survey_goa()
    rev = survey_reviews(ancestors)

    iep_goa = goa["code_totals"]["IEP"]
    lines: list[str] = []
    add = lines.append

    # The report is a data dump whose gene column spans species, so bare
    # symbols here are ambiguous by construction; do not autolink them.
    add("---")
    add('title: "IEP corpus survey"')
    add("autolink_gene_symbols: false")
    add("---")
    add("")
    add("# IEP corpus survey")
    add("")
    add(
        "Generated by `projects/IEP/iep_corpus_survey.py`. Two views: raw GOA "
        "(`*-goa.tsv`, what GOA ships) and reviewed (`*-ai-review.yaml`, what "
        "reviewers concluded)."
    )
    add("")
    add(
        f"GO closure computed against GO release **{go_release()}** (OAK "
        "adapter `sqlite:obo:go` by default; override with `IEP_GO_ADAPTER`). "
        "The coarse branch tallies can move by a row or two between GO "
        "releases, as terms are obsoleted or reparented; everything else is "
        "release-independent."
    )
    add("")
    add(
        "**What the reviewer dispositions are.** Every `action` counted below "
        "comes from this repository's own `*-ai-review.yaml` files, which are "
        "AI-generated reviews produced under the guidance in `CLAUDE.md`. They "
        "are not independent adjudication of GO curators. See the "
        "[limitations note](../IEP.md#what-flagged-means-and-does-not-mean)."
    )
    add("")

    add("## GOA view")
    add("")
    add(f"- Annotation rows across all cached GOA files: **{goa['total_rows']:,}**")
    add(
        f"- IEP rows: **{iep_goa:,}** ({pct(iep_goa, goa['total_rows'])} of all rows), "
        f"in **{len(goa['genes_with_iep']):,}** gene directories"
    )
    add("")
    add("### Evidence-code frequency (top 15)")
    add("")
    add("| Code | Rows | Share |")
    add("|---|---:|---:|")
    for code, n in goa["code_totals"].most_common(15):
        add(f"| {code} | {n:,} | {pct(n, goa['total_rows'])} |")
    add("")

    add("### IEP by GO aspect")
    add("")
    add("| Aspect | Rows | Share of IEP |")
    add("|---|---:|---:|")
    for aspect, n in goa["aspects"].most_common():
        add(f"| {aspect} | {n:,} | {pct(n, iep_goa)} |")
    add("")

    add("### IEP by qualifier")
    add("")
    add("| Qualifier | Rows | Share of IEP |")
    add("|---|---:|---:|")
    for qual, n in goa["qualifiers"].most_common(10):
        add(f"| {qual or '(none)'} | {n:,} | {pct(n, iep_goa)} |")
    add("")

    add("### IEP by assigning group (top 15)")
    add("")
    add("| Assigned by | Rows | Share of IEP |")
    add("|---|---:|---:|")
    for group, n in goa["assigned_by"].most_common(15):
        add(f"| {group} | {n:,} | {pct(n, iep_goa)} |")
    add("")

    add("### IEP by taxon (top 15)")
    add("")
    add("| Taxon | Rows |")
    add("|---|---:|")
    for taxon, n in goa["taxa"].most_common(15):
        add(f"| {taxon} | {n:,} |")
    add("")

    add("### Most frequent IEP terms in GOA (top 25)")
    add("")
    add("| GO term | Label | Rows |")
    add("|---|---|---:|")
    for (tid, label), n in goa["terms"].most_common(25):
        add(f"| {tid} | {label} | {n:,} |")
    add("")

    add("## Review view")
    add("")
    iep_reviewed = sum(rev["disposition"]["IEP"].values())
    add(
        f"- Reviewed IEP rows: **{iep_reviewed:,}** across "
        f"**{len(rev['iep_files']):,}** gene review files"
    )
    add(
        f"- IEP rows whose exact GO term is also carried by a non-IEP annotation "
        f"in the same review: **{rev['corroborated']:,}** "
        f"({pct(rev['corroborated'], iep_reviewed)})"
    )
    add(
        f"- IEP rows where IEP is the **sole** carrier of that GO term: "
        f"**{rev['sole_support']:,}** ({pct(rev['sole_support'], iep_reviewed)}), "
        f"of which **{rev['sole_support_negative']:,}** were REMOVE/MARK_OVER/MODIFY"
    )
    add(
        f"- Same measurement with is_a/part_of closure (an ancestor or "
        f"descendant of the IEP term under a non-IEP code also counts as "
        f"corroboration): **{rev['corroborated_closure']:,}** corroborated "
        f"({pct(rev['corroborated_closure'], iep_reviewed)}), so the sole-carrier "
        f"share falls to "
        f"**{pct(iep_reviewed - rev['corroborated_closure'], iep_reviewed)}**. "
        f"The exact-match figure above is therefore an upper bound on sole carriage."
    )
    add(
        f"- IEP rows whose term also appears in the review's `core_functions`: "
        f"**{rev['core_grounded']:,}** ({pct(rev['core_grounded'], iep_reviewed)}), "
        f"of which **{rev['core_grounded_accept']:,}** were also ACCEPTed "
        f"(the rest reach `core_functions` on the strength of a co-annotated "
        f"non-IEP row)"
    )
    add("")

    conc = concentration(rev["iep_by_gene"])
    add("### How concentrated IEP is over genes")
    add("")
    add(
        f"- Gene directories carrying at least one reviewed IEP row: "
        f"**{conc['genes']:,}**; median IEP rows per such gene: "
        f"**{conc['median']:g}**; maximum: **{conc['max']:,}**"
    )
    add(
        f"- The top 10% of IEP-carrying genes ({conc['top_decile_genes']:,} genes) "
        f"carry **{conc['top_decile_rows']:,}** rows, "
        f"**{pct(conc['top_decile_rows'], conc['rows'])}** of the total"
    )
    add(
        f"- Genes with 5 or more IEP rows: **{conc['heavy_genes']:,}** "
        f"({pct(conc['heavy_genes'], conc['genes'])} of IEP-carrying genes), "
        f"carrying **{pct(conc['heavy_rows'], conc['rows'])}** of all IEP rows "
        f"(this is the statistic comparable to the global atlas)"
    )
    add("")
    add("| Gene | IEP rows |")
    add("|---|---:|")
    for gene_key, n in rev["iep_by_gene"].most_common(10):
        add(f"| {gene_key} | {n:,} |")
    add("")

    add("### Disposition by evidence code")
    add("")
    header = "| Code | Reviewed | " + " | ".join(ACTIONS) + " | % negative |"
    add(header)
    add("|---|---:|" + "---:|" * (len(ACTIONS) + 1))
    for code in BASELINE_CODES:
        counts = rev["disposition"].get(code)
        if not counts:
            continue
        total = sum(counts.values())
        neg = sum(counts[a] for a in NEGATIVE_ACTIONS)
        cells = " | ".join(str(counts.get(a, 0)) for a in ACTIONS)
        add(f"| {code} | {total:,} | {cells} | **{pct(neg, total)}** |")
    add("")
    add(
        "`% negative` = REMOVE + MARK_AS_OVER_ANNOTATED + MODIFY, i.e. rows a "
        "reviewer judged not keepable as written, over the `Reviewed` total. "
        "That total is every annotation row carrying the code, including the "
        "`PENDING` and `UNREVIEWED` ones, so the action columns sum to it."
    )
    add("")

    add("### How often each code lands on core function")
    add("")
    add("| Code | Reviewed | ACCEPT | % ACCEPT | Term in `core_functions` | % core |")
    add("|---|---:|---:|---:|---:|---:|")
    for code in BASELINE_CODES:
        counts = rev["disposition"].get(code)
        if not counts:
            continue
        total = sum(counts.values())
        accepted = counts.get("ACCEPT", 0)
        rows, in_core = rev["core_grounding"][code]
        add(
            f"| {code} | {total:,} | {accepted:,} | {pct(accepted, total)} | "
            f"{in_core:,} | {pct(in_core, rows)} |"
        )
    add("")
    add(
        "`% core` credits a code whenever the term it carries also appears in "
        "`core_functions`, even if the term got there on the strength of a "
        "different code annotating it too. It is therefore generous to every "
        "code, and most generous to codes that frequently co-annotate."
    )
    add("")

    add("### What IEP is used to say (GO branch, is_a + part_of closure)")
    add("")
    add("| Branch | IEP rows | Share | Genes | Flagged | % flagged | Genes flagged |")
    add("|---|---:|---:|---:|---:|---:|---:|")
    total_branch = sum(rev["branches"].values())
    for branch, n in rev["branches"].most_common():
        neg = rev["branch_negative"][branch]
        add(
            f"| {branch} | {n:,} | {pct(n, total_branch)} | "
            f"{len(rev['branch_genes'][branch]):,} | {neg} | {pct(neg, n)} | "
            f"{len(rev['branch_negative_genes'][branch]):,} |"
        )
    add("")
    add(
        "Branch assignment is **first match wins** in the order listed in "
        "`BRANCHES`, with `response to stimulus` tested before "
        "`developmental process`, so a term parented under both is counted as "
        "stimulus-response."
    )
    add("")

    add("### Branch flag rates, split by species")
    add("")
    add(
        "The pooled branch comparison above can be confounded by review batch: "
        "if one species dominates one branch, the branch flag rate may be "
        "measuring that species' review batch instead. This table splits the "
        "two largest branches by species and gives a two-sided Fisher exact "
        "test of the developmental-versus-stimulus flag-rate difference within "
        "each."
    )
    add("")
    add(
        "| Species | response to stimulus | flagged | % | "
        "developmental process | flagged | % | Fisher p |"
    )
    add("|---|---:|---:|---:|---:|---:|---:|---:|")
    species_seen = sorted(
        {sp for sp, _ in rev["branch_by_species"]},
        key=lambda sp: -rev["iep_by_species"][sp],
    )
    stim_total = rev["branches"]["response to stimulus"]
    stim_total_neg = rev["branch_negative"]["response to stimulus"]
    dev_total = rev["branches"]["developmental process"]
    dev_total_neg = rev["branch_negative"]["developmental process"]
    for sp in species_seen:
        stim = rev["branch_by_species"][(sp, "response to stimulus")]
        stim_neg = rev["branch_by_species_negative"][(sp, "response to stimulus")]
        dev = rev["branch_by_species"][(sp, "developmental process")]
        dev_neg = rev["branch_by_species_negative"][(sp, "developmental process")]
        if not stim and not dev:
            continue
        p = fisher_exact_two_sided(dev_neg, dev - dev_neg, stim_neg, stim - stim_neg)
        add(
            f"| {sp} | {stim:,} | {stim_neg} | {pct(stim_neg, stim)} | "
            f"{dev:,} | {dev_neg} | {pct(dev_neg, dev)} | "
            f"{p:.3f} |"
        )
    p_pooled = fisher_exact_two_sided(
        dev_total_neg,
        dev_total - dev_total_neg,
        stim_total_neg,
        stim_total - stim_total_neg,
    )
    add(
        f"| **all** | **{stim_total:,}** | **{stim_total_neg}** | "
        f"**{pct(stim_total_neg, stim_total)}** | **{dev_total:,}** | "
        f"**{dev_total_neg}** | **{pct(dev_total_neg, dev_total)}** | "
        f"**{p_pooled:.3f}** |"
    )
    add("")
    add(
        f"Pooled, the developmental branch flags at "
        f"{pct(dev_total_neg, dev_total)} against "
        f"{pct(stim_total_neg, stim_total)} for stimulus-response, on "
        f"{dev_total_neg}/{dev_total} versus {stim_total_neg}/{stim_total} — "
        f"**not separable from noise** (two-sided Fisher p = {p_pooled:.2f}). "
        f"The developmental rows are at least not a single review batch: they "
        f"span {len(rev['branch_genes']['developmental process']):,} gene "
        f"directories. Treat the gap as suggestive of the mechanism argued "
        f"from the worked examples, not as evidence for it."
    )
    add("")

    add("### Reviewed IEP rows by species (top 15)")
    add("")
    add("| Species | IEP rows |")
    add("|---|---:|")
    for sp, n in rev["iep_by_species"].most_common(15):
        add(f"| {sp} | {n:,} |")
    add("")

    add("### Most frequently flagged IEP terms")
    add("")
    add("| GO term | Label | IEP rows | Flagged (REMOVE/MARK_OVER/MODIFY) |")
    add("|---|---|---:|---:|")
    for (tid, label), n in rev["iep_negative_terms"].most_common(25):
        add(f"| {tid} | {label} | {rev['iep_terms'][(tid, label)]} | {n} |")
    add("")

    add("### All flagged IEP rows")
    add("")
    add("| Species | Gene | GO term | Label | Action |")
    add("|---|---|---|---|---|")
    for species, gene, tid, label, action, _reason in sorted(rev["iep_rows"]):
        if action in NEGATIVE_ACTIONS:
            add(f"| {species} | {gene} | {tid} | {label} | {action} |")
    add("")

    OUT_PATH.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)}")
    print(f"GOA: {iep_goa:,} IEP rows / {goa['total_rows']:,} total")
    print(f"Reviewed: {iep_reviewed:,} IEP rows in {len(rev['iep_files']):,} files")
    for code in BASELINE_CODES:
        counts = rev["disposition"].get(code)
        if not counts:
            continue
        total = sum(counts.values())
        neg = sum(counts[a] for a in NEGATIVE_ACTIONS)
        print(f"  {code:5} n={total:6,}  negative={pct(neg, total)}")


if __name__ == "__main__":
    main()
