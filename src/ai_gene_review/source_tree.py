"""Read repository files either from the working tree or from a pinned git commit.

Derived benchmark reports (GO-GPT three-level overlap, BioReason sidecars, the
ProtNLM summary) are reported as a dated snapshot: their inputs are read at a
declared commit, so ordinary curation of the working tree cannot stale them.
Both readers share one small interface, keyed by repository-relative POSIX paths.

>>> tree = WorkingTree(Path("."))
>>> tree.is_file("pyproject.toml")
True
>>> "pyproject.toml" in tree.glob("*.toml")
True
>>> snapshot = git_snapshot(Path("."), "HEAD")
>>> len(snapshot.commit)
40
>>> b"[project]" in snapshot.read_bytes("pyproject.toml")
True
>>> snapshot.glob("src/**/source_tree.py")
['src/ai_gene_review/source_tree.py']
>>> snapshot.is_file("no/such/file.txt")
False
"""

from __future__ import annotations

import subprocess
import weakref
from dataclasses import dataclass, field
from fnmatch import fnmatchcase
from functools import cached_property, lru_cache
from pathlib import Path
from typing import IO, Protocol

import yaml

BENCHMARK_POLICY = Path("projects/BIOREASON_COMPARISON/benchmark-policy.yaml")
"""Declares ``review_snapshot_commit`` / ``review_snapshot_date`` for the benchmark reports."""


class SourceTree(Protocol):
    """Read-only access to repository files by repository-relative path."""

    def read_bytes(self, path: str) -> bytes: ...

    def read_text(self, path: str) -> str: ...

    def is_file(self, path: str) -> bool: ...

    def glob(self, pattern: str) -> list[str]: ...


def match_path(path: str, pattern: str) -> bool:
    """Match a relative path against a glob, with ``Path.glob`` semantics.

    ``*`` never crosses ``/``; a ``**`` segment matches zero or more directories.

    >>> match_path("genes/human/TP53/TP53-goa.tsv", "genes/*/*/*-goa.tsv")
    True
    >>> match_path("genes/human/TP53/sub/TP53-goa.tsv", "genes/*/*/*-goa.tsv")
    False
    >>> match_path("genes/human/TP53/sub/TP53-goa.tsv", "genes/**/*-goa.tsv")
    True
    >>> match_path("genes/TP53-goa.tsv", "genes/**/*-goa.tsv")
    True
    >>> match_path("reports/TP53-goa.tsv", "genes/**/*-goa.tsv")
    False
    """
    return _match_parts(tuple(path.split("/")), tuple(pattern.split("/")))


def _match_parts(path: tuple[str, ...], pattern: tuple[str, ...]) -> bool:
    if not pattern:
        return not path
    head, rest = pattern[0], pattern[1:]
    if head == "**":
        return any(_match_parts(path[i:], rest) for i in range(len(path) + 1))
    return bool(path) and fnmatchcase(path[0], head) and _match_parts(path[1:], rest)


@dataclass(frozen=True)
class WorkingTree:
    """Files as they are on disk under ``root``."""

    root: Path

    def read_bytes(self, path: str) -> bytes:
        return (self.root / path).read_bytes()

    def read_text(self, path: str) -> str:
        return self.read_bytes(path).decode("utf-8")

    def is_file(self, path: str) -> bool:
        return (self.root / path).is_file()

    def glob(self, pattern: str) -> list[str]:
        return sorted(
            p.relative_to(self.root).as_posix() for p in self.root.glob(pattern)
        )


def _close_batch(process: subprocess.Popen[bytes]) -> None:
    stdin: IO[bytes] | None = process.stdin
    if stdin is not None:
        stdin.close()
    process.wait()


@dataclass
class GitSnapshot:
    """Files exactly as committed at ``commit``, read without touching the working tree.

    Blobs are streamed through one long-lived ``git cat-file --batch`` process,
    so reading thousands of files costs one subprocess, not thousands.
    """

    repo_root: Path
    commit: str
    _cache: dict[str, bytes] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", "--quiet", f"{self.commit}^{{commit}}"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"Snapshot commit {self.commit} is not available locally; "
                f"run `git fetch --depth=1 origin {self.commit}`."
            )
        self.commit = result.stdout.strip()

    @cached_property
    def _blobs(self) -> dict[str, str]:
        """Map every committed file path to its blob id."""
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "-z", self.commit],
            cwd=self.repo_root,
            capture_output=True,
            check=True,
        ).stdout.decode("utf-8")
        blobs: dict[str, str] = {}
        for entry in filter(None, listing.split("\0")):
            meta, path = entry.split("\t", 1)
            _mode, kind, object_id = meta.split()
            if kind == "blob":
                blobs[path] = object_id
        return blobs

    @cached_property
    def _batch(self) -> subprocess.Popen[bytes]:
        process = subprocess.Popen(
            ["git", "cat-file", "--batch"],
            cwd=self.repo_root,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        weakref.finalize(self, _close_batch, process)
        return process

    def read_bytes(self, path: str) -> bytes:
        if path not in self._cache:
            if path not in self._blobs:
                raise FileNotFoundError(f"{path} does not exist at {self.commit}")
            process = self._batch
            assert process.stdin is not None and process.stdout is not None
            process.stdin.write(f"{self._blobs[path]}\n".encode())
            process.stdin.flush()
            _object_id, _kind, size = process.stdout.readline().split()
            self._cache[path] = process.stdout.read(int(size))
            process.stdout.read(1)  # trailing newline after each blob
        return self._cache[path]

    def read_text(self, path: str) -> str:
        return self.read_bytes(path).decode("utf-8")

    def is_file(self, path: str) -> bool:
        return path in self._blobs

    def glob(self, pattern: str) -> list[str]:
        return sorted(path for path in self._blobs if match_path(path, pattern))


@lru_cache(maxsize=None)
def git_snapshot(repo_root: Path, commit: str) -> GitSnapshot:
    """Return a shared reader for ``commit`` so repeated callers reuse one process."""
    return GitSnapshot(repo_root.resolve(), commit)


@dataclass(frozen=True)
class ReviewSnapshot:
    """The declared commit and date at which the benchmark reports are computed."""

    commit: str
    date: str

    @property
    def short(self) -> str:
        """Abbreviated commit id for prose.

        >>> ReviewSnapshot("c7551cb3dbd677b6f68c80f9e333d43249ee79c3", "2026-09-27").short
        'c7551cb3db'
        """
        return self.commit[:10]


def declared_review_snapshot(repo_root: Path) -> ReviewSnapshot:
    """Read the review snapshot declared in the benchmark policy.

    >>> snapshot = declared_review_snapshot(Path("."))
    >>> len(snapshot.commit), len(snapshot.date)
    (40, 10)
    """
    policy = yaml.safe_load((repo_root / BENCHMARK_POLICY).read_text(encoding="utf-8"))
    return ReviewSnapshot(
        commit=str(policy["review_snapshot_commit"]),
        date=str(policy["review_snapshot_date"]),
    )


def review_snapshot_tree(repo_root: Path) -> GitSnapshot:
    """Reader for the repository as it was at the declared review snapshot."""
    return git_snapshot(repo_root, declared_review_snapshot(repo_root).commit)


def commit_date(repo_root: Path, commit: str) -> str:
    """Committer date (``YYYY-MM-DD``, git ``%cs``) of ``commit``."""
    return subprocess.run(
        ["git", "show", "-s", "--format=%cs", commit],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
