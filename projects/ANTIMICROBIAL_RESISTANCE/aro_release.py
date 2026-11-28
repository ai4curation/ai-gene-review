#!/usr/bin/env python3
"""ARO release handling for the ARO->GO mapping: fetch, propagate, check.

The curated mapping (``aro2go.sssom.yaml``) is checked against one pinned CARD release
(``aro_release.yaml``). This module is the single place that knows how to

* **fetch** a CARD release (ontology + data tarballs) into ``.cache/aro/`` (git-ignored): the pinned
  one by default, CARD's newest with ``--latest`` (the drift probe, ``just check-aro-latest``);
* **propagate** a mapping from an ARO term to the gene/determinant terms it applies to; and
* **check** the mapping set against a release: label drift, ids missing from the release,
  and coverage of CARD's "AMR Gene Family" category.

Propagation rule
----------------
ARO has two axes that matter here, joined by different relations:

* the **gene axis** (determinant -> AMR gene family -> broader family) uses ``is_a``;
* the **mechanism axis** (e.g. ``antibiotic inactivation``) is reached from the gene axis by
  ``participates_in`` (RO:0000056), asserted on a family node, and the mechanism terms are
  themselves arranged by ``is_a``.

A mapping on ARO term ``S`` applies to a gene ``G`` when either

* ``G is_a* S`` (``exact`` when ``G == S``, else ``narrower``); or
* ``G is_a* X``, ``X participates_in Y`` and ``Y is_a* S`` (``participates_in``).

Before this rule existed only the first clause was implemented, so every mechanism row
(mapped on a mechanism term, which no gene is an ``is_a`` descendant of) reached nothing.
Other ARO relations are deliberately *not* followed: ``confers_resistance_to_antibiotic`` and
``confers_resistance_to_drug_class`` point to chemical entities (the drug, not a mechanism or a
family), ``part_of``/``has_part`` join complex subunits and gene clusters, and the regulation
relations join regulators to their targets; none of them makes a gene an instance of a mapped
family or a participant in a mapped mechanism.

Usage::

    uv run python projects/ANTIMICROBIAL_RESISTANCE/aro_release.py fetch
    uv run python projects/ANTIMICROBIAL_RESISTANCE/aro_release.py check
    uv run python projects/ANTIMICROBIAL_RESISTANCE/aro_release.py coverage -o projects/ANTIMICROBIAL_RESISTANCE/FAMILY_COVERAGE.md
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import tarfile
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from functools import lru_cache
from pathlib import Path

import typer
import yaml

PROJECT_DIR = Path(__file__).resolve().parent
REPO = PROJECT_DIR.parents[1]
DEFAULT_CACHE = REPO / ".cache" / "aro"
PIN_FILE = PROJECT_DIR / "aro_release.yaml"
SSSOM_FILE = PROJECT_DIR / "aro2go.sssom.yaml"
TRIAGE_FILE = PROJECT_DIR / "aro_family_triage.yaml"

CARD_LATEST_URLS = ("https://card.mcmaster.ca/latest/ontology", "https://card.mcmaster.ca/latest/data")


def card_release_urls(version: str) -> tuple[str, str]:
    """Download URLs (ontology, data) of one CARD release, so a pinned release stays fetchable.

    >>> card_release_urls("4.0.2")[0]
    'https://card.mcmaster.ca/download/5/ontology-v4.0.2.tar.bz2'
    """
    return (
        f"https://card.mcmaster.ca/download/5/ontology-v{version}.tar.bz2",
        f"https://card.mcmaster.ca/download/0/broadstreet-v{version}.tar.bz2",
    )

NOT_IN_RELEASE = "NOT_IN_ONTOLOGY_RELEASE"

app = typer.Typer(help=__doc__, no_args_is_help=True)


# ---------------------------------------------------------------------------
# Ontology access (a minimal OBO reader: ARO is shipped as a flat OBO file)
# ---------------------------------------------------------------------------


@dataclass(eq=False)  # identity hashing: the ontology is an lru_cache key
class AroOntology:
    """The parts of an ARO OBO release that the mapping needs.

    >>> aro = AroOntology.from_obo_text(MINI_OBO)
    >>> aro.labels["ARO:2"]
    'beta-lactamase'
    >>> sorted(aro.is_a["ARO:3"])
    ['ARO:2']
    >>> aro.participates_in["ARO:2"]
    ['ARO:11']
    """

    labels: dict[str, str] = field(default_factory=dict)
    is_a: dict[str, list[str]] = field(default_factory=dict)
    participates_in: dict[str, list[str]] = field(default_factory=dict)
    obsolete: set[str] = field(default_factory=set)
    date: str = ""

    @classmethod
    def from_obo_text(cls, text: str) -> "AroOntology":
        onto = cls()
        current: str | None = None
        in_term = False
        for line in text.splitlines():
            if line.startswith("["):
                in_term = line.strip() == "[Term]"
                current = None
                continue
            if not in_term:
                if line.startswith("date: ") and not onto.date:
                    onto.date = line[len("date: "):].strip()
                continue
            if line.startswith("id: "):
                current = line[4:].strip()
            elif current is None:
                continue
            elif line.startswith("name: "):
                onto.labels[current] = line[6:].strip()
            elif line.startswith("is_a: "):
                onto.is_a.setdefault(current, []).append(line[6:].split("!")[0].strip())
            elif line.startswith("relationship: participates_in "):
                target = line.split()[2]
                onto.participates_in.setdefault(current, []).append(target)
            elif line.startswith("is_obsolete: true"):
                onto.obsolete.add(current)
        return onto

    @classmethod
    def from_obo(cls, path: Path) -> "AroOntology":
        return cls.from_obo_text(path.read_text())

    def isa_ancestors_or_self(self, term: str) -> set[str]:
        """``term`` and all its ``is_a`` ancestors.

        >>> sorted(AroOntology.from_obo_text(MINI_OBO).isa_ancestors_or_self("ARO:4"))
        ['ARO:1', 'ARO:2', 'ARO:3', 'ARO:4']
        """
        return set(_isa_closure(self, term))

    def mechanisms(self, term: str) -> set[str]:
        """Mechanism terms ``term`` reaches by ``is_a* o participates_in o is_a*``.

        >>> sorted(AroOntology.from_obo_text(MINI_OBO).mechanisms("ARO:4"))
        ['ARO:10', 'ARO:11']
        """
        reached: set[str] = set()
        for anc in self.isa_ancestors_or_self(term):
            for mech in self.participates_in.get(anc, []):
                reached |= self.isa_ancestors_or_self(mech)
        return reached


@lru_cache(maxsize=None)
def _isa_closure(onto: AroOntology, term: str) -> frozenset[str]:
    out = {term}
    for parent in onto.is_a.get(term, []):
        out |= _isa_closure(onto, parent)
    return frozenset(out)


def applicable_subjects(onto: AroOntology, term: str) -> dict[str, str]:
    """Map every ARO term whose mappings apply to ``term`` -> how it applies.

    Values are ``exact``, ``narrower`` (gene axis, via ``is_a``) or ``participates_in``
    (mechanism axis). A term reachable both ways keeps its gene-axis relation.

    >>> aro = AroOntology.from_obo_text(MINI_OBO)
    >>> rel = applicable_subjects(aro, "ARO:4")
    >>> rel["ARO:4"], rel["ARO:2"], rel["ARO:10"]
    ('exact', 'narrower', 'participates_in')
    """
    rel = {m: "participates_in" for m in onto.mechanisms(term)}
    for anc in onto.isa_ancestors_or_self(term):
        rel[anc] = "exact" if anc == term else "narrower"
    return rel


MINI_OBO = """format-version: 1.2
date: 11:08:2026 08:59

[Term]
id: ARO:1
name: AMR gene family

[Term]
id: ARO:2
name: beta-lactamase
is_a: ARO:1
relationship: participates_in ARO:11

[Term]
id: ARO:3
name: class A beta-lactamase
is_a: ARO:2

[Term]
id: ARO:4
name: TEM-1
is_a: ARO:3

[Term]
id: ARO:10
name: antibiotic inactivation

[Term]
id: ARO:11
name: hydrolysis of beta-lactam antibiotic
is_a: ARO:10
"""


# ---------------------------------------------------------------------------
# Release files
# ---------------------------------------------------------------------------


@dataclass
class Release:
    """One fetched CARD release in the cache directory."""

    cache: Path

    @property
    def obo(self) -> Path:
        return self.cache / "aro.obo"

    @property
    def categories(self) -> Path:
        return self.cache / "aro_categories.tsv"

    @property
    def index(self) -> Path:
        return self.cache / "aro_index.tsv"

    @property
    def metadata(self) -> dict:
        return yaml.safe_load((self.cache / "release.yaml").read_text())

    def require(self) -> None:
        missing = [p for p in (self.obo, self.categories, self.cache / "release.yaml") if not p.exists()]
        if missing:
            raise typer.BadParameter(
                f"No CARD release in {self.cache} (missing {', '.join(p.name for p in missing)}); "
                "run `just fetch-aro` first."
            )

    def amr_gene_families(self) -> dict[str, str]:
        """CARD's 'AMR Gene Family' category: ARO id -> name."""
        with self.categories.open(newline="") as fh:
            return {
                r["ARO Accession"]: r["ARO Name"]
                for r in csv.DictReader(fh, delimiter="\t")
                if r["ARO Category"] == "AMR Gene Family"
            }

    def family_mechanisms(self) -> dict[str, Counter]:
        """AMR gene family name -> Counter of CARD-asserted resistance mechanisms of its models."""
        out: dict[str, Counter] = {}
        with self.index.open(newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                for fam in r["AMR Gene Family"].split(";"):
                    counter = out.setdefault(fam.strip(), Counter())
                    for mech in r["Resistance Mechanism"].split(";"):
                        counter[mech.strip()] += 1
        return out


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def obo_date_iso(obo_date: str) -> str:
    """Convert the OBO header date (``dd:mm:yyyy HH:MM``) to ISO ``yyyy-mm-dd``.

    >>> obo_date_iso("11:08:2026 08:59")
    '2026-08-11'
    """
    day, month, year = obo_date.split()[0].split(":")
    return f"{year}-{month}-{day}"


def _download(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=300) as resp:  # noqa: S310 - fixed https URL
        return resp.read()


def _members(blob: bytes, names: set[str]) -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:bz2") as tar:
        for member in tar.getmembers():
            name = Path(member.name).name
            if name in names and member.isfile():
                extracted = tar.extractfile(member)
                assert extracted is not None
                out[name] = extracted.read()
    return out


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


@dataclass
class CheckResult:
    label_drift: list[tuple[str, str, str, str]] = field(default_factory=list)  # (file, id, ours, aro)
    missing: list[tuple[str, str, str]] = field(default_factory=list)  # (file, id, our label)
    version_mismatch: list[str] = field(default_factory=list)
    untriaged_families: list[tuple[str, str]] = field(default_factory=list)
    stale_triage: list[tuple[str, str]] = field(default_factory=list)  # triaged but now mapped

    @property
    def ok(self) -> bool:
        return not (
            self.label_drift or self.missing or self.version_mismatch or self.untriaged_families or self.stale_triage
        )


def load_sssom(path: Path = SSSOM_FILE) -> dict:
    return yaml.safe_load(path.read_text())


def load_triage(path: Path = TRIAGE_FILE) -> dict:
    return yaml.safe_load(path.read_text())


def family_status(onto: AroOntology, families: dict[str, str], sssom: dict) -> dict[str, tuple[str, str]]:
    """Classify each AMR gene family: ``MAPPED``, ``COVERED_BY_ANCESTOR``, ``GO_GAP`` (a
    NoTermFound row on the family or an ancestor) or ``UNMAPPED``, with the deciding ARO subject.

    Precedence is deliberate: a GO term inherited from a mapped ancestor outranks a gap row, so a
    family with both is counted as covered (its gap row still stands as a request for a more
    specific term).

    >>> aro = AroOntology.from_obo_text(MINI_OBO)
    >>> sssom = {"mappings": [{"subject_id": "ARO:2", "object_id": "GO:0008800"}]}
    >>> family_status(aro, {"ARO:2": "beta-lactamase", "ARO:3": "class A"}, sssom)
    {'ARO:2': ('MAPPED', 'ARO:2'), 'ARO:3': ('COVERED_BY_ANCESTOR', 'ARO:2')}
    """
    go_subjects = {m["subject_id"] for m in sssom["mappings"] if str(m["object_id"]).startswith("GO:")}
    gap_subjects = {m["subject_id"] for m in sssom["mappings"] if m["object_id"] == "sssom:NoTermFound"}
    status: dict[str, tuple[str, str]] = {}
    for fam in families:
        if fam in go_subjects:
            status[fam] = ("MAPPED", fam)
            continue
        ancestors = onto.isa_ancestors_or_self(fam)
        covering = sorted((ancestors - {fam}) & go_subjects)
        gaps = sorted(ancestors & gap_subjects)
        if covering:
            status[fam] = ("COVERED_BY_ANCESTOR", covering[0])
        elif gaps:
            status[fam] = ("GO_GAP", gaps[0])
        else:
            status[fam] = ("UNMAPPED", "")
    return status


def check(onto: AroOntology, release_meta: dict, pin: dict, sssom: dict, triage: dict, families: dict[str, str]) -> CheckResult:
    result = CheckResult()
    if release_meta["card_version"] != pin["card_version"]:
        result.version_mismatch.append(
            f"cached CARD release {release_meta['card_version']} != pinned {pin['card_version']}"
        )
    elif release_meta.get("aro_obo_sha256") != pin["aro_obo_sha256"]:
        result.version_mismatch.append(
            f"cached aro.obo sha256 {str(release_meta.get('aro_obo_sha256'))[:12]}... differs from the pinned "
            f"{pin['aro_obo_sha256'][:12]}... for the same CARD version (re-run `just fetch-aro`)"
        )
    pinned_source = f"CARD {pin['card_version']} (ARO {pin['aro_date']})"
    if sssom.get("subject_source_version") != pinned_source:
        result.version_mismatch.append(
            f"aro2go.sssom.yaml subject_source_version {sssom.get('subject_source_version')!r} != {pinned_source!r}"
        )
    rows = [("aro2go.sssom.yaml", m["subject_id"], m["subject_label"]) for m in sssom["mappings"]]
    for f in triage["families"]:
        if f["reason"] == NOT_IN_RELEASE:
            # CARD lists the id as an AMR gene family but the ontology release has no such term.
            if f["id"] in onto.labels:
                result.stale_triage.append((f["id"], f["label"]))
            continue
        rows.append(("aro_family_triage.yaml", f["id"], f["label"]))
    for file, term, label in rows:
        if term not in onto.labels or term in onto.obsolete:
            result.missing.append((file, term, label))
        elif onto.labels[term] != label:
            result.label_drift.append((file, term, label, onto.labels[term]))
    status = family_status(onto, families, sssom)
    triaged = {f["id"] for f in triage["families"]}
    for fam, (state, _) in sorted(status.items()):
        if state == "UNMAPPED" and fam not in triaged:
            result.untriaged_families.append((fam, families[fam]))
        if state != "UNMAPPED" and fam in triaged and fam in onto.labels:
            result.stale_triage.append((fam, families[fam]))
    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@app.command()
def fetch(
    cache: Path = typer.Option(DEFAULT_CACHE, help="Cache directory for the release files"),
    latest: bool = typer.Option(False, help="Fetch CARD's latest release instead of the pinned one"),
    update_pin: bool = typer.Option(False, help="Rewrite aro_release.yaml to the fetched release"),
) -> None:
    """Download a CARD release (the pinned one by default) into the cache."""
    pin = yaml.safe_load(PIN_FILE.read_text())
    urls = CARD_LATEST_URLS if latest else card_release_urls(pin["card_version"])
    cache.mkdir(parents=True, exist_ok=True)
    onto_files = _members(_download(urls[0]), {"aro.obo"})
    data_files = _members(_download(urls[1]), {"aro_categories.tsv", "aro_index.tsv", "card.json"})
    (cache / "aro.obo").write_bytes(onto_files["aro.obo"])
    (cache / "aro_categories.tsv").write_bytes(data_files["aro_categories.tsv"])
    (cache / "aro_index.tsv").write_bytes(data_files["aro_index.tsv"])
    card_version = json.loads(data_files["card.json"])["_version"]
    aro_date = obo_date_iso(AroOntology.from_obo(cache / "aro.obo").date)
    meta = {
        "card_version": card_version,
        "aro_date": aro_date,
        "aro_obo_sha256": sha256(cache / "aro.obo"),
        "fetched": date.today().isoformat(),
        "sources": list(card_release_urls(card_version)),
    }
    (cache / "release.yaml").write_text(yaml.safe_dump(meta, sort_keys=False))
    typer.echo(f"Fetched CARD {card_version} (ARO {aro_date}) into {cache}")
    if update_pin:
        pin = {k: meta[k] for k in ("card_version", "aro_date", "aro_obo_sha256", "sources")}
        PIN_FILE.write_text(
            "# The CARD/ARO release the ARO->GO mapping was last checked against.\n"
            "# Written by `aro_release.py fetch --latest --update-pin`; `just check-aro-release` compares to it\n"
            "# (CARD version and the sha256 of aro.obo).\n"
            + yaml.safe_dump(pin, sort_keys=False)
        )
        typer.echo(f"Updated {PIN_FILE.name}")


@app.command("check")
def check_cmd(cache: Path = typer.Option(DEFAULT_CACHE, help="Cache directory holding the fetched release")) -> None:
    """Check the mapping set against the fetched release; exit 1 on any drift."""
    release = Release(cache)
    release.require()
    onto = AroOntology.from_obo(release.obo)
    pin = yaml.safe_load(PIN_FILE.read_text())
    result = check(onto, release.metadata, pin, load_sssom(), load_triage(), release.amr_gene_families())
    for line in result.version_mismatch:
        typer.echo(f"VERSION  {line}")
    for file, term, ours, theirs in result.label_drift:
        typer.echo(f"LABEL    {file}: {term} {ours!r} -> ARO now {theirs!r}")
    for file, term, ours in result.missing:
        typer.echo(f"MISSING  {file}: {term} {ours!r} is not a live term in this ARO release")
    for term, label in result.untriaged_families:
        typer.echo(f"COVERAGE {term} {label!r}: AMR gene family neither mapped nor triaged")
    for term, label in result.stale_triage:
        typer.echo(f"STALE    {term} {label!r}: triaged as unmapped but now mapped or covered")
    if not result.ok:
        raise typer.Exit(1)
    typer.echo(f"OK: mapping set consistent with CARD {release.metadata['card_version']}")


@app.command()
def coverage(
    cache: Path = typer.Option(DEFAULT_CACHE, help="Cache directory holding the fetched release"),
    output: Path = typer.Option(PROJECT_DIR / "FAMILY_COVERAGE.md", "-o", "--output"),
) -> None:
    """Write the AMR-gene-family coverage report (markdown)."""
    release = Release(cache)
    release.require()
    onto = AroOntology.from_obo(release.obo)
    sssom = load_sssom()
    triage = {f["id"]: f for f in load_triage()["families"]}
    families = release.amr_gene_families()
    mechs = release.family_mechanisms()
    status = family_status(onto, families, sssom)
    go_by_subject: dict[str, list[str]] = {}
    for m in sssom["mappings"]:
        if str(m["object_id"]).startswith("GO:"):
            go_by_subject.setdefault(m["subject_id"], []).append(f"{m['object_id']} {m['object_label']}")
    counts = Counter(state for state, _ in status.values())
    reasons = Counter(triage[f]["reason"] for f, (s, _) in status.items() if s == "UNMAPPED" and f in triage)
    meta = release.metadata
    lines = [
        "---",
        'title: "AMR gene family coverage of the ARO→GO mapping"',
        "---",
        "",
        "# AMR gene family coverage of the ARO→GO mapping",
        "",
        f"Generated by `aro_release.py coverage` against **CARD {meta['card_version']}** "
        f"(ARO release {meta['aro_date']}). Every term in CARD's *AMR Gene Family* category "
        "(`aro_categories.tsv`) is listed once. Part of the "
        "[Antimicrobial Resistance project](../ANTIMICROBIAL_RESISTANCE.md); the mapping itself is "
        "[`aro2go.sssom.yaml`](aro2go.sssom.yaml) and the triage of unmapped families is "
        "[`aro_family_triage.yaml`](aro_family_triage.yaml).",
        "",
        "## Summary",
        "",
        f"- AMR gene families in the release: **{len(families)}**",
        f"- Mapped directly (a GO row on the family itself): **{counts['MAPPED']}**",
        f"- Covered by a mapped ancestor family (exact-or-narrower propagation): **{counts['COVERED_BY_ANCESTOR']}**",
        f"- Recorded GO gaps (`sssom:NoTermFound`, a GO term request candidate): **{counts['GO_GAP']}**",
        f"- Not mapped, with a recorded reason: **{counts['UNMAPPED']}**",
        "",
        "| reason (unmapped families) | families |",
        "|---|---:|",
    ]
    for reason, n in reasons.most_common():
        lines.append(f"| `{reason}` | {n} |")
    lines += [
        "",
        "## All families",
        "",
        "| ARO | family | CARD mechanism(s) | status | GO / reason |",
        "|---|---|---|---|---|",
    ]
    order = {"MAPPED": 0, "GO_GAP": 1, "COVERED_BY_ANCESTOR": 2, "UNMAPPED": 3}
    for fam in sorted(families, key=lambda f: (order[status[f][0]], families[f].lower())):
        state, subject = status[fam]
        mech = "; ".join(m for m, _ in mechs.get(families[fam], Counter()).most_common()) or "—"
        if state == "MAPPED":
            detail = "<br>".join(go_by_subject[fam])
        elif state == "COVERED_BY_ANCESTOR":
            detail = f"via {subject} {onto.labels.get(subject, '')}: " + "; ".join(go_by_subject[subject])
        elif state == "GO_GAP":
            detail = "no suitable GO term" + ("" if subject == fam else f" (gap row on {subject} {onto.labels.get(subject, '')})")
        else:
            entry = triage.get(fam)
            detail = f"`{entry['reason']}`: {entry['explanation']}" if entry else "**untriaged**"
        lines.append(f"| {fam} | {families[fam]} | {mech} | {state} | {detail} |")
    output.write_text("\n".join(lines) + "\n")
    typer.echo(f"Wrote {output} ({len(families)} families)")


if __name__ == "__main__":
    app()
