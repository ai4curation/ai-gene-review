#!/usr/bin/env python3
"""Load the Rhea reaction network and the rhea2go GO mapping (live, cached).

Two indices are built from public data, both fetched live:

* ``participant_to_reactions`` — ChEBI curie -> set of Rhea reaction ids that use
  it as a participant, from the Rhea REST API (``columns=rhea-id,chebi-id``).
* ``reaction_to_go`` — Rhea id -> (GO id, GO label), from the GO Consortium's
  ``rhea2go`` external2go mapping (the GOA ``GO_REF:0000116`` pipeline source,
  the same file used by the RHEA project).

Nothing is hardcoded; results are cached on disk under ``.cache/``.
"""
from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

RHEA_API = "https://www.rhea-db.org/rhea"
RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
CACHE = Path(__file__).parent / ".cache"

_R2G = re.compile(r"RHEA:(\d+) > GO:(.+) ; (GO:\d+)")


def _get_text(url: str, timeout: int = 120, retries: int = 3) -> str:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-metabolomics/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode(errors="replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"request failed after {retries} tries: {url}: {last}")


def _cached_text(name: str, url: str) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / name
    if f.exists():
        return f.read_text()
    text = _get_text(url)
    f.write_text(text)
    return text


def load_rhea2go() -> dict[str, tuple[str, str]]:
    """Rhea id (numeric str) -> (GO id, GO label)."""
    out: dict[str, tuple[str, str]] = {}
    for line in _cached_text("rhea2go.txt", RHEA2GO_URL).splitlines():
        m = _R2G.match(line)
        if m:
            out[m.group(1)] = (m.group(3), m.group(2))
    return out


def load_reaction_participants() -> dict[str, set[str]]:
    """Rhea id (numeric str) -> set of participant ChEBI curies."""
    params = urllib.parse.urlencode(
        {"query": "", "columns": "rhea-id,chebi-id", "format": "tsv", "limit": 200000}
    )
    text = _cached_text("rhea_participants.tsv", f"{RHEA_API}?{params}")
    out: dict[str, set[str]] = {}
    for line in text.splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        rid = parts[0].replace("RHEA:", "").strip()
        chebis = {c.strip() for c in parts[1].split(";") if c.startswith("CHEBI:")}
        if rid and chebis:
            out[rid] = chebis
    return out


class RheaIndex:
    """Forward and reverse indices over the Rhea reaction network."""

    def __init__(self) -> None:
        self.reaction_to_go = load_rhea2go()
        self.reaction_to_participants = load_reaction_participants()
        self.participant_to_reactions: dict[str, set[str]] = defaultdict(set)
        for rid, chebis in self.reaction_to_participants.items():
            for c in chebis:
                self.participant_to_reactions[c].add(rid)

    def reactions_for(self, chebi: str) -> set[str]:
        return self.participant_to_reactions.get(chebi, set())

    def go_terms_for(self, chebi: str) -> set[tuple[str, str]]:
        """GO MF terms reachable from a single ChEBI via its rhea2go reactions."""
        out: set[tuple[str, str]] = set()
        for rid in self.reactions_for(chebi):
            if rid in self.reaction_to_go:
                out.add(self.reaction_to_go[rid])
        return out
