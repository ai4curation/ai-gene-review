#!/usr/bin/env python
"""Genome-wide coherence pilot for *E. coli* MG1655.

This is the first pilot for the GENOME_WIDE_VALIDATION project. It implements the
**coherence** criterion of the completeness / coherence / consistency framework
(Tawfiq, Kulmanov & Hoehndorf 2026, Brief Bioinform 27(3):bbag336) at the
whole-genome level, using constraints already encoded in the Gene Ontology.

Idea
----
GO encodes ``has_part`` (RO:0000051) axioms: a process/function ``C`` that
``has_part`` ``F`` depends on ``F``. At the *genome* level, if any protein in a
genome is annotated with ``C`` (or a descendant), then some protein in the same
genome should be annotated with ``F`` (or a descendant) — otherwise the annotated
process is missing a required part. Coherence is the fraction of activated
``has_part`` dependencies that are satisfied.

    coherence(g) = 1 - |missing| / |activated|

where a pair ``(C, F)`` is *activated* when ``C`` is present in genome ``g`` and
*missing* when ``F`` is not present.

"Present in genome g" follows the GO true-path rule: a class is present if it, or
any of its ``is_a`` / ``part_of`` descendants, is directly annotated. We compute
this by closing the directly-annotated terms upward over ``is_a`` + ``part_of``.

Scope & honesty
---------------
* Uses **asserted** ``has_part`` axioms from ``go.obo``. The reference paper uses
  an ELK reasoner to also recover *inferred* ``has_part some X`` subclasses (5038
  pairs); the asserted set is a tractable, honest subset. The pair count we use
  is reported in the output, not hard-coded.
* Data are downloaded live (and cached) from official sources; nothing is
  fabricated. If a download fails the script exits non-zero rather than inventing
  numbers.
* This pilot implements coherence only; completeness (essential-function set) and
  consistency (taxon constraints) are documented next steps. A small, clearly
  labelled *illustrative* completeness probe for a handful of universally
  essential processes is included as a sanity check, not as the completeness
  metric.

Run
---
    uv run python coherence_pilot.py

Outputs (written next to this script):
    RESULTS.md         human-readable summary with the real numbers
    violations.tsv     every activated-but-unsatisfied has_part dependency
"""

from __future__ import annotations

import gzip
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / "cache"

GO_OBO_URL = "https://current.geneontology.org/ontology/go.obo"
ECOLI_GAF_URL = "http://current.geneontology.org/annotations/ecocyc.gaf.gz"

GO_OBO = CACHE / "go.obo"
ECOLI_GAF = CACHE / "ecocyc.gaf.gz"

# Illustrative only: a few processes no free-living cell can omit. NOT the
# completeness metric (which needs a curated minimal-genome essential set).
ESSENTIAL_PROBE = {
    "GO:0006260": "DNA replication",
    "GO:0006351": "DNA-templated transcription",
    "GO:0006412": "translation",
    "GO:0009058": "biosynthetic process",
    "GO:0006096": "glycolytic process",
}


def _download(url: str, dest: Path) -> None:
    """Fetch ``url`` to ``dest`` via curl (uses the environment proxy/CA). Cached."""
    if dest.exists() and dest.stat().st_size > 0:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {url} -> {dest.name}")
    result = subprocess.run(
        ["curl", "-sSL", "--fail", "--max-time", "300", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not dest.exists() or dest.stat().st_size == 0:
        raise SystemExit(f"download failed for {url}: {result.stderr.strip()}")


def parse_obo(path: Path) -> tuple[dict[str, str], dict[str, set[str]], list[tuple[str, str]], set[str]]:
    """Parse a GO ``.obo`` file.

    Returns ``(names, parents, has_part_pairs, obsolete)`` where

    * ``names``  maps GO id -> primary name
    * ``parents`` maps GO id -> set of true-path parents (``is_a`` + ``part_of``)
    * ``has_part_pairs`` is a list of ``(C, F)`` meaning ``C has_part F``
    * ``obsolete`` is the set of obsolete term ids
    """
    names: dict[str, str] = {}
    parents: dict[str, set[str]] = defaultdict(set)
    has_part_pairs: list[tuple[str, str]] = []
    obsolete: set[str] = set()

    cur: str | None = None
    is_obsolete = False
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if line == "[Term]":
            cur = None
            is_obsolete = False
            continue
        if line.startswith("[") and line != "[Term]":
            cur = None  # a non-Term stanza (e.g. [Typedef])
            continue
        if not line or cur is None and not line.startswith("id: "):
            if not line.startswith("id: "):
                continue
        if line.startswith("id: GO:"):
            cur = line[len("id: "):].strip()
            continue
        if cur is None:
            continue
        if line.startswith("name: "):
            names[cur] = line[len("name: "):].strip()
        elif line == "is_obsolete: true":
            is_obsolete = True
            obsolete.add(cur)
        elif line.startswith("is_a: GO:"):
            parent = line[len("is_a: "):].split("!")[0].strip()
            parents[cur].add(parent)
        elif line.startswith("relationship: part_of GO:"):
            parent = line[len("relationship: part_of "):].split("!")[0].strip()
            parents[cur].add(parent)
        elif line.startswith("relationship: has_part GO:"):
            part = line[len("relationship: has_part "):].split("!")[0].strip()
            has_part_pairs.append((cur, part))
    # drop obsolete-involving records
    has_part_pairs = [(c, f) for c, f in has_part_pairs if c not in obsolete and f not in obsolete]
    return names, parents, has_part_pairs, obsolete


def parse_gaf_terms(path: Path) -> set[str]:
    """Return the set of GO ids directly annotated (non-NOT) in a GAF."""
    terms: set[str] = set()
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 5:
                continue
            qualifier = cols[3]
            if "NOT" in qualifier.split("|"):
                continue
            go_id = cols[4]
            if go_id.startswith("GO:"):
                terms.add(go_id)
    return terms


def ancestor_closure(seeds: set[str], parents: dict[str, set[str]]) -> set[str]:
    """Close ``seeds`` upward over ``parents`` (true-path present set)."""
    present: set[str] = set()
    stack = list(seeds)
    while stack:
        node = stack.pop()
        if node in present:
            continue
        present.add(node)
        stack.extend(parents.get(node, ()))
    return present


def main() -> None:
    _download(GO_OBO_URL, GO_OBO)
    _download(ECOLI_GAF_URL, ECOLI_GAF)

    names, parents, has_part_pairs, obsolete = parse_obo(GO_OBO)
    annotated = parse_gaf_terms(ECOLI_GAF)
    # Restrict seeds to terms the ontology knows and that are not obsolete.
    annotated_known = {t for t in annotated if t in names and t not in obsolete}
    present = ancestor_closure(annotated_known, parents)

    # Coherence over activated has_part dependencies.
    activated: list[tuple[str, str]] = []
    missing: list[tuple[str, str]] = []
    for c, f in has_part_pairs:
        if c in present:
            activated.append((c, f))
            if f not in present:
                missing.append((c, f))

    n_act = len(activated)
    n_missing = len(missing)
    coherence = (1 - n_missing / n_act) * 100 if n_act else float("nan")

    # Illustrative completeness probe.
    probe_rows = []
    for go_id, label in ESSENTIAL_PROBE.items():
        probe_rows.append((go_id, label, go_id in present))

    # --- write violations.tsv ---
    viol_path = HERE / "violations.tsv"
    with viol_path.open("w") as fh:
        fh.write("whole_term_id\twhole_term_label\tmissing_part_id\tmissing_part_label\n")
        for c, f in sorted(missing):
            fh.write(f"{c}\t{names.get(c, '?')}\t{f}\t{names.get(f, '?')}\n")

    # --- write RESULTS.md ---
    lines = []
    lines.append("# E. coli MG1655 — genome-wide coherence pilot (results)\n")
    lines.append(
        "Generated by `coherence_pilot.py`. Numbers are computed live from the "
        "cached downloads; nothing here is hand-edited.\n"
    )
    lines.append("## Inputs\n")
    lines.append(f"- GO ontology: `{GO_OBO_URL}` (asserted `has_part` axioms)")
    lines.append(f"- E. coli annotations: `{ECOLI_GAF_URL}` (EcoCyc GAF)")
    lines.append(f"- Directly annotated GO terms (non-NOT): **{len(annotated)}** "
                 f"({len(annotated_known)} resolvable & non-obsolete)")
    lines.append(f"- Present set after `is_a`+`part_of` closure: **{len(present)}** classes")
    lines.append(f"- Asserted `has_part` pairs in GO: **{len(has_part_pairs)}**\n")
    lines.append("## Coherence\n")
    lines.append(f"- Activated dependencies (whole present in genome): **{n_act}**")
    lines.append(f"- Unsatisfied (required part absent): **{n_missing}**")
    lines.append(f"- **Coherence = {coherence:.1f}%**\n")
    lines.append("Each unsatisfied dependency is a reviewable lead — a process annotated in "
                 "the genome whose required part is annotated on no protein. See "
                 "`violations.tsv` for the full list. Top examples:\n")
    for c, f in sorted(missing)[:15]:
        lines.append(f"- `{c}` {names.get(c, '?')} **has_part** `{f}` {names.get(f, '?')} — part not present")
    if not missing:
        lines.append("- (none — all activated dependencies satisfied)")
    lines.append("\n## Illustrative completeness probe (sanity check, not the metric)\n")
    for go_id, label, ok in probe_rows:
        lines.append(f"- {'✓' if ok else '✗'} `{go_id}` {label}")
    lines.append("\n## Caveats\n")
    lines.append("- Asserted `has_part` only; the reference paper adds ELK-inferred pairs "
                 "(~5038). A low count here reflects GO's sparse asserted process-level "
                 "`has_part`, so coherence is a *lower bound on detectable* violations.")
    lines.append("- A violation can be a genuine biological gap **or** a missing annotation "
                 "(this check never looks at sequence). Resolve flagged gaps with a "
                 "sequence-level tool (GapMind / Pathway Tools) before acting.")
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")

    # --- console summary ---
    print(f"annotated terms: {len(annotated)} (known {len(annotated_known)})")
    print(f"present (closed): {len(present)}")
    print(f"has_part pairs: {len(has_part_pairs)}  activated: {n_act}  missing: {n_missing}")
    print(f"coherence: {coherence:.1f}%")
    print(f"wrote {viol_path.name} and RESULTS.md")


if __name__ == "__main__":
    main()
