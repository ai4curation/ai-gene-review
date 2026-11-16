"""Report which ontology terms the committed term-validator cache cannot answer.

``linkml-term-validator`` (LTV) checks term ids and labels cache-first: labels come
from ``cache/<prefix>/terms.csv`` and dynamic-enum memberships from
``cache/enums/*.csv``, and only a miss goes to the ontology adapter. When every
term a file uses is in the committed cache, its term check needs no ontology
service, so an outage cannot affect it (ai4curation/ai-gene-review#5731).

This tool measures that coverage. It runs LTV with ``--offline`` on the given
files, which resolves only from the cache and reports each miss, and sorts what
LTV reports into:

* **label misses**: ``Term 'X' not found in offline cache``;
* **enum-membership misses**: ``Cannot validate 'X' against dynamic enum 'E'
  offline``;
* **label mismatches**: the cached label differs from the file's label. Offline,
  this cannot tell a stale cache from a wrong label in the file. They are split
  by CI's own policy (``BLOCKING_LABEL_MISMATCH`` in ``cli.py``): an NCBITaxon
  mismatch blocks CI, while a GO mismatch is advisory, because GO labels lag
  between GOA and GO releases. A large advisory count usually means the cached
  GO labels need refreshing, not that reviews need editing;
* **other findings**: any other error or warning, such as a term outside its enum.

A file the run did not account for (LTV crashed, could not read it, printed
something this parser does not recognise, or announced more issues than were
parsed) is listed under ``unchecked_files``,
and the report is then ``complete: false``: the tool fails closed, so a coverage
gate can never pass because nothing was checked.

Not every miss is an outage risk. ``conf/oak_config.yaml`` serves some prefixes
from a SQLite build that oaklib downloads once and caches (GO, RHEA) and others
from a remote service at validation time (``ols:``, e.g. NCBITaxon). Each miss is
marked ``needs_network`` unless its adapter is a known local scheme (``sqlite:``,
``simpleobo:``, ``pronto:``, ``obograph:``); an unknown scheme counts as remote.
``--network-only`` restricts ``--check`` to the misses that need the network.

``--warm`` measures coverage, runs LTV online on the same files (which fills the
cache with whatever the service can answer), and measures again, so the report
shows the before/after miss counts and whether the online pass reached the
service. Warming writes to the cache directory (the committed ``cache/`` by
default); review the diff, run ``just lint-caches`` and commit it like any other
change.

Usage::

    uv run python -m ai_gene_review.tools.ontology_cache_coverage genes/human/TP53
    uv run python -m ai_gene_review.tools.ontology_cache_coverage --warm --check FILES...

The tool recognises the three review kinds CI routes through
``scripts/term_validate.sh``: gene reviews (``*-ai-review.yaml``), prediction
reviews (``*-predictions-review.yaml``) and PANTHER family reviews
(``interpro/panther/**/PTHR*-review.yaml``). The manual ``*2go`` mapping-set and
Pfam-entry QA recipes in the justfile also run LTV, but outside CI.

Exit codes with ``--check``: 0 covered, 1 cache misses, 2 incomplete run or bad
arguments.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from ai_gene_review.cli import BLOCKING_LABEL_MISMATCH, _tool_command

PROJECT_ROOT = Path(__file__).resolve().parents[3]
GENE_SCHEMA = Path("src/ai_gene_review/schema/gene_review.yaml")
FAMILY_SCHEMA = Path("src/ai_gene_review/schema/family_review.yaml")
OAK_CONFIG = Path("conf/oak_config.yaml")
DEFAULT_CACHE_DIR = Path("cache")
BATCH_SIZE = 200
LOCAL_ADAPTER_SCHEMES = frozenset({"sqlite", "simpleobo", "pronto", "obograph"})

LABEL_MISS = re.compile(r"Term '(?P<curie>[^']+)' not found in offline cache")
ENUM_MISS = re.compile(
    r"Cannot validate '(?P<curie>[^']+)' against dynamic enum '(?P<enum>[^']+)' offline"
)
LABEL_MISMATCH = re.compile(r"Label mismatch for '(?P<curie>[^']+)'")
FILE_HEADER = re.compile(
    r"^(?:❌|✅) (?P<name>\S+\.ya?ml)(?: - (?P<issues>\d+) issue\(s\):)?\s*$"
)
SINGLE_FILE_RESULT = re.compile(r"^(?:✅ Validation passed|❌ Validation failed)")
FINDING_LINE = re.compile(
    r"^\s*(?:❌ (?P<error>ERROR)|⚠️\s+(?P<warn>WARN)): (?P<message>.+)$"
)
# Same alternatives as scripts/term_validate.sh, which documents LTV's outage contract.
OUTAGE_BANNER = re.compile(
    r"ontology service unavailable|could not reach ontology service", re.IGNORECASE
)


def remote_prefixes(config_path: Path) -> set[str]:
    """Return the prefixes whose OAK adapter may contact a service at validation time.

    A prefix is local only when its adapter scheme is in ``LOCAL_ADAPTER_SCHEMES``;
    ``null`` (skipped) prefixes are not validated at all.

    >>> prefixes = remote_prefixes(PROJECT_ROOT / OAK_CONFIG)
    >>> "NCBITaxon" in prefixes, "GO" in prefixes, "PMID" in prefixes
    (True, False, False)
    """
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    adapters = config.get("ontology_adapters") or {}
    return {
        prefix
        for prefix, adapter in adapters.items()
        if isinstance(adapter, str)
        and adapter.split(":", 1)[0] not in LOCAL_ADAPTER_SCHEMES
    }


def prefix_of(curie: str) -> str:
    """Return the prefix of a CURIE.

    >>> prefix_of("NCBITaxon:9606")
    'NCBITaxon'
    """
    return curie.split(":", 1)[0]


@dataclass(frozen=True)
class DocumentKind:
    """A document kind LTV validates: its schema and target class."""

    schema: Path
    target_class: str


GENE_REVIEW = DocumentKind(GENE_SCHEMA, "GeneReview")
PREDICTION_REVIEW = DocumentKind(GENE_SCHEMA, "PredictionReview")
FAMILY_REVIEW = DocumentKind(FAMILY_SCHEMA, "FamilyReview")


def document_kind(path: Path) -> DocumentKind | None:
    """Return the LTV document kind for a file, or None if CI does not term-check it.

    >>> document_kind(Path("genes/human/TP53/TP53-ai-review.yaml")).target_class
    'GeneReview'
    >>> document_kind(Path("genes/9PSED/X/X-dashboard-predictions-review.yaml")).target_class
    'PredictionReview'
    >>> document_kind(Path("interpro/panther/PTHR1/PTHR1-review.yaml")).target_class
    'FamilyReview'
    >>> document_kind(Path("modules/il10_signaling.yaml")) is None
    True
    """
    name = path.name
    if name.endswith("-predictions-review.yaml"):
        return PREDICTION_REVIEW
    if name.endswith("-ai-review.yaml"):
        return GENE_REVIEW
    if (
        name.startswith("PTHR")
        and name.endswith("-review.yaml")
        and "panther" in path.parts
    ):
        return FAMILY_REVIEW
    return None


def expand_inputs(inputs: list[Path]) -> dict[DocumentKind, list[Path]]:
    """Group the given files, and the recognised files under given directories, by kind."""
    grouped: dict[DocumentKind, list[Path]] = defaultdict(list)
    seen: set[Path] = set()
    for item in inputs:
        if item.is_dir():
            candidates = sorted(item.rglob("*.yaml"))
        elif item.is_file():
            candidates = [item]
        else:
            raise FileNotFoundError(f"Input does not exist: {item}")
        for candidate in candidates:
            kind = document_kind(candidate)
            resolved = candidate.resolve()
            if kind is not None and resolved not in seen:
                seen.add(resolved)
                grouped[kind].append(candidate)
    return dict(grouped)


def batches(files: list[Path], size: int = BATCH_SIZE) -> list[list[Path]]:
    """Split files into batches of at most ``size`` with no repeated basename.

    LTV names each file in its output by basename only, so two files sharing a
    basename (``rpoB-ai-review.yaml`` in several organisms) must never share a
    batch, or their findings could not be told apart.

    >>> [[p.as_posix() for p in b] for b in batches(
    ...     [Path("a/x.yaml"), Path("b/x.yaml"), Path("a/y.yaml")], size=5)]
    [['a/x.yaml', 'a/y.yaml'], ['b/x.yaml']]
    >>> [len(b) for b in batches([Path(f"{i}.yaml") for i in range(5)], size=2)]
    [2, 2, 1]
    """
    result: list[list[Path]] = []
    names: list[set[str]] = []
    for path in files:
        for batch, batch_names in zip(result, names):
            if len(batch) < size and path.name not in batch_names:
                batch.append(path)
                batch_names.add(path.name)
                break
        else:
            result.append([path])
            names.append({path.name})
    return result


@dataclass
class WarmPass:
    """Outcome of the online warming pass."""

    batches: int = 0
    outage_batches: int = 0
    failed_batches: int = 0
    misses_before: int = 0

    def to_dict(self, misses_after: int) -> dict:
        """Return a plain mapping for the report."""
        return {
            "online_batches": self.batches,
            "outage_batches": self.outage_batches,
            "failed_batches": self.failed_batches,
            "misses_before": self.misses_before,
            "misses_after": misses_after,
        }


@dataclass
class CoverageReport:
    """Cache misses and other term findings from an offline LTV run."""

    files_checked: int = 0
    label_misses: defaultdict[str, set[str]] = field(
        default_factory=lambda: defaultdict(set)
    )
    enum_misses: defaultdict[tuple[str, str], set[str]] = field(
        default_factory=lambda: defaultdict(set)
    )
    label_mismatches: list[tuple[str, str]] = field(default_factory=list)
    other_findings: list[tuple[str, str, str]] = field(default_factory=list)
    unchecked_files: dict[str, str] = field(default_factory=dict)
    unattributed_output: list[str] = field(default_factory=list)
    remote: set[str] = field(default_factory=set)
    warm: WarmPass | None = None

    @property
    def covered(self) -> bool:
        """True when the cache answered every term check that ran."""
        return not self.label_misses and not self.enum_misses

    @property
    def complete(self) -> bool:
        """True when every file was checked and all validator output was understood."""
        return not self.unchecked_files and not self.unattributed_output

    def needs_network(self, curie: str) -> bool:
        """True when a miss on ``curie`` would go to a remote ontology service."""
        return prefix_of(curie) in self.remote

    def miss_count(self) -> int:
        """Count distinct label and enum-membership misses."""
        return len(self.label_misses) + len(self.enum_misses)

    def network_misses(self) -> int:
        """Count the misses that would need a remote ontology service."""
        return sum(self.needs_network(c) for c in self.label_misses) + sum(
            self.needs_network(c) for c, _ in self.enum_misses
        )

    def to_dict(self) -> dict:
        """Return a plain, deterministically ordered mapping for YAML output."""
        result: dict = {
            "files_checked": self.files_checked,
            "complete": self.complete,
            "covered": self.covered,
            "misses_needing_network": self.network_misses(),
            "missing_labels": [
                {
                    "curie": curie,
                    "needs_network": self.needs_network(curie),
                    "files": sorted(files),
                }
                for curie, files in sorted(self.label_misses.items())
            ],
            "missing_enum_memberships": [
                {
                    "curie": curie,
                    "enum": enum,
                    "needs_network": self.needs_network(curie),
                    "files": sorted(files),
                }
                for (curie, enum), files in sorted(self.enum_misses.items())
            ],
            "blocking_label_mismatches": [
                {"file": path, "message": message}
                for path, message in sorted(self.label_mismatches)
                if BLOCKING_LABEL_MISMATCH.search(message)
            ],
            "advisory_label_mismatches": [
                {"file": path, "message": message}
                for path, message in sorted(self.label_mismatches)
                if not BLOCKING_LABEL_MISMATCH.search(message)
            ],
            "other_findings": [
                {"file": path, "severity": severity, "message": message}
                for path, severity, message in sorted(self.other_findings)
            ],
            "unchecked_files": [
                {"file": path, "reason": reason}
                for path, reason in sorted(self.unchecked_files.items())
            ],
            "unattributed_output": list(self.unattributed_output),
        }
        if self.label_mismatches:
            result["label_mismatch_note"] = (
                "The cached label differs from the file's: the cache may be stale or "
                "the file may be wrong. CI blocks on NCBITaxon mismatches only; GO "
                "mismatches are advisory (GO release lag), and many of them usually "
                "mean the cached GO labels need refreshing."
            )
        if self.warm is not None:
            result["warm"] = self.warm.to_dict(self.miss_count())
        return result

    def blocking_mismatch_count(self) -> int:
        """Count label mismatches that CI treats as errors."""
        return sum(
            bool(BLOCKING_LABEL_MISMATCH.search(message))
            for _, message in self.label_mismatches
        )


def parse_offline_output(
    output: str, returncode: int, files: list[Path], report: CoverageReport
) -> None:
    """Add one offline LTV run's findings to ``report``, failing closed.

    ``files`` must have unique basenames (see ``batches``). LTV names each file in
    a multi-file run; a single-file run names none but prints one result line.
    Any file LTV did not account for is recorded in ``unchecked_files``.

    >>> report = CoverageReport(remote={"NCBITaxon"})
    >>> out = '''
    ... ❌ X-predictions-review.yaml - 3 issue(s):
    ...   ❌ ERROR: Cannot validate 'NCBITaxon:1' against dynamic enum 'NCBITaxonEnum' offline: enum closure not materialized
    ...   ❌ ERROR: Term 'NCBITaxon:1' not found in offline cache
    ...   ⚠️  WARN: Label mismatch for 'GO:0000002': expected 'a', got 'b'
    ... ✅ Y-predictions-review.yaml
    ... '''
    >>> files = [Path("a/X-predictions-review.yaml"), Path("b/Y-predictions-review.yaml")]
    >>> parse_offline_output(out, 1, files, report)
    >>> d = report.to_dict()
    >>> d["missing_labels"]
    [{'curie': 'NCBITaxon:1', 'needs_network': True, 'files': ['a/X-predictions-review.yaml']}]
    >>> d["missing_enum_memberships"][0]["enum"], report.network_misses()
    ('NCBITaxonEnum', 2)
    >>> len(d["advisory_label_mismatches"]), d["blocking_label_mismatches"], d["complete"]
    (1, [], True)

    A header announcing more issues than were parsed means the finding format was
    not understood, so the file is unchecked:

    >>> report = CoverageReport()
    >>> parse_offline_output("❌ X-predictions-review.yaml - 2 issue(s):", 1, files[:1], report)
    >>> report.unchecked_files
    {'a/X-predictions-review.yaml': 'validator announced 2 issue(s) but 0 were parsed'}

    A run that names only one of two files, or crashes, leaves files unchecked:

    >>> report = CoverageReport()
    >>> parse_offline_output("✅ X-predictions-review.yaml", 0, files, report)
    >>> report.complete, list(report.unchecked_files)
    (False, ['b/Y-predictions-review.yaml'])
    >>> report = CoverageReport()
    >>> parse_offline_output("Traceback (most recent call last):", 1, files[:1], report)
    >>> report.complete, report.covered
    (False, True)
    """
    by_name = {path.name: path.as_posix() for path in files}
    accounted: set[str] = set()
    announced: dict[str, int] = {}
    parsed: defaultdict[str, int] = defaultdict(int)
    current: str | None = files[0].as_posix() if len(files) == 1 else None
    for line in output.splitlines():
        header = FILE_HEADER.match(line)
        if header:
            current = by_name.get(header.group("name"))
            if current is None:
                report.unattributed_output.append(line.strip())
            else:
                accounted.add(current)
                if header.group("issues") is not None:
                    announced[current] = int(header.group("issues"))
            continue
        if len(files) == 1 and SINGLE_FILE_RESULT.match(line):
            accounted.add(files[0].as_posix())
            continue
        finding = FINDING_LINE.match(line)
        if not finding:
            continue
        severity = finding.group("error") or finding.group("warn")
        message = finding.group("message").strip()
        if current is not None:
            parsed[current] += 1
        if current is None:
            report.unattributed_output.append(message)
        elif match := LABEL_MISS.search(message):
            report.label_misses[match.group("curie")].add(current)
        elif match := ENUM_MISS.search(message):
            report.enum_misses[(match.group("curie"), match.group("enum"))].add(current)
        elif LABEL_MISMATCH.search(message):
            report.label_mismatches.append((current, message))
        else:
            report.other_findings.append((current, severity, message))
    reason = (
        f"validator exited {returncode} without a result for this file"
        if returncode
        else "validator printed no result for this file"
    )
    for path in files:
        posix = path.as_posix()
        if posix not in accounted:
            report.unchecked_files[posix] = reason
        elif announced.get(posix, parsed[posix]) != parsed[posix]:
            report.unchecked_files[posix] = (
                f"validator announced {announced[posix]} issue(s) "
                f"but {parsed[posix]} were parsed"
            )


def ltv_command(
    kind: DocumentKind, files: list[Path], offline: bool, cache_dir: Path
) -> list[str]:
    """Build the LTV ``validate-data`` command for one batch of same-kind files.

    >>> cmd = ltv_command(GENE_REVIEW, [Path("x-ai-review.yaml")], False, Path("cache"))
    >>> "--offline" in cmd, cmd[cmd.index("--cache-dir") + 1]
    (False, 'cache')
    >>> "--offline" in ltv_command(GENE_REVIEW, [], True, Path("cache"))
    True
    """
    command = [
        *_tool_command("linkml-term-validator"),
        "validate-data",
        *[path.as_posix() for path in files],
        "-s",
        kind.schema.as_posix(),
        "-t",
        kind.target_class,
        "--labels",
        "-c",
        OAK_CONFIG.as_posix(),
        "--cache-dir",
        cache_dir.as_posix(),
    ]
    if offline:
        command.append("--offline")
    return command


def run_ltv(
    kind: DocumentKind, files: list[Path], offline: bool, cache_dir: Path
) -> tuple[str, int]:
    """Run LTV from the project root; return its combined output and exit code."""
    completed = subprocess.run(
        ltv_command(kind, files, offline, cache_dir),
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = "\n".join(part for part in (completed.stdout, completed.stderr) if part)
    return output, completed.returncode


def classify_online_pass(output: str, returncode: int) -> str:
    """Classify one online warming run as ``ok``, ``outage`` or ``failed``.

    ``validate-data`` exits 0 or 1 when it ran (1 also covers warnings); LTV exits
    2 with an "ontology service unavailable" banner when it could not reach the
    service.

    >>> classify_online_pass("✅ Validation passed", 0)
    'ok'
    >>> classify_online_pass("Terms could not be checked: ontology service unavailable", 2)
    'outage'
    >>> classify_online_pass("Traceback (most recent call last):", 2)
    'failed'
    """
    if returncode in (0, 1):
        return "ok"
    if OUTAGE_BANNER.search(output):
        return "outage"
    return "failed"


def relative_to_root(path: Path) -> Path:
    """Express ``path`` relative to the project root, as LTV runs from there."""
    resolved = path.resolve()
    if resolved.is_relative_to(PROJECT_ROOT):
        return resolved.relative_to(PROJECT_ROOT)
    return resolved


def offline_pass(
    work: list[tuple[DocumentKind, list[Path]]], cache_dir: Path, label: str
) -> CoverageReport:
    """Measure coverage offline over prepared batches."""
    report = CoverageReport(remote=remote_prefixes(PROJECT_ROOT / OAK_CONFIG))
    for number, (kind, batch) in enumerate(work, start=1):
        print(
            f"[{label}] batch {number}/{len(work)}: {len(batch)} {kind.target_class}",
            file=sys.stderr,
        )
        output, returncode = run_ltv(kind, batch, offline=True, cache_dir=cache_dir)
        unchecked_before = len(report.unchecked_files)
        parse_offline_output(output, returncode, batch, report)
        report.files_checked += len(batch) - (
            len(report.unchecked_files) - unchecked_before
        )
    return report


def measure_coverage(
    grouped: dict[DocumentKind, list[Path]],
    warm: bool,
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> CoverageReport:
    """Measure coverage offline; with ``warm``, also warm online and re-measure."""
    work = [
        (kind, batch)
        for kind, files in grouped.items()
        for batch in batches([relative_to_root(path) for path in files])
    ]
    if not warm:
        return offline_pass(work, cache_dir, "offline")
    before = offline_pass(work, cache_dir, "before warm")
    # Only batches holding a miss (or an unchecked file) have anything to warm.
    to_warm = set(before.unchecked_files)
    for misses in (*before.label_misses.values(), *before.enum_misses.values()):
        to_warm |= misses
    warm_work = [
        (kind, batch)
        for kind, batch in work
        if any(path.as_posix() in to_warm for path in batch)
    ]
    warm_pass = WarmPass(batches=len(warm_work), misses_before=before.miss_count())
    for number, (kind, batch) in enumerate(warm_work, start=1):
        print(f"[warm] batch {number}/{len(warm_work)}", file=sys.stderr)
        output, returncode = run_ltv(kind, batch, offline=False, cache_dir=cache_dir)
        outcome = classify_online_pass(output, returncode)
        if outcome == "outage":
            warm_pass.outage_batches += 1
        elif outcome == "failed":
            warm_pass.failed_batches += 1
    report = offline_pass(work, cache_dir, "after warm")
    report.warm = warm_pass
    return report


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", type=Path, help="Files or directories")
    parser.add_argument(
        "--warm",
        action="store_true",
        help="Warm the cache online between two offline measurements",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 on cache misses and 2 on an incomplete run",
    )
    parser.add_argument(
        "--network-only",
        action="store_true",
        help="With --check, fail only on misses that need a remote ontology service",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=DEFAULT_CACHE_DIR,
        help="LTV cache directory, relative to the project root (default: cache)",
    )
    parser.add_argument("-o", "--output", type=Path, help="Write the YAML report here")
    args = parser.parse_args(argv)
    if args.network_only and not args.check:
        parser.error("--network-only only applies with --check")

    grouped = expand_inputs(args.inputs)
    if not grouped:
        print(
            "No gene, prediction or family review files found in the inputs.",
            file=sys.stderr,
        )
        return 2
    report = measure_coverage(grouped, warm=args.warm, cache_dir=args.cache_dir)
    text = yaml.safe_dump(report.to_dict(), sort_keys=False, allow_unicode=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    print(
        f"{report.files_checked} files; {report.miss_count()} cache misses "
        f"({report.network_misses()} needing the network); "
        f"{len(report.label_mismatches)} label mismatches "
        f"({report.blocking_mismatch_count()} blocking in CI); "
        f"{len(report.other_findings)} other findings; "
        f"{len(report.unchecked_files)} unchecked files",
        file=sys.stderr,
    )
    if report.warm is not None and report.warm.outage_batches:
        print(
            f"Warning: {report.warm.outage_batches} warming batch(es) hit an "
            "ontology-service outage; the cache was not filled for them.",
            file=sys.stderr,
        )
    if not args.check:
        return 0
    if not report.complete:
        return 2
    failing = report.network_misses() if args.network_only else report.miss_count()
    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())
