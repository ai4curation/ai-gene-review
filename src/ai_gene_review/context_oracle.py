"""Proteome oracle for MODULE_CONTEXT conditions in curated rules.

A detector file (``rules/curated/context/<module>.yaml``) maps each step of a
module to InterPro signatures. Given which signatures a UniProt proteome contains,
the module is evaluated with :mod:`ai_gene_review.module_logic`:

- ``True``  - satisfiable: every required step (and extra step) has a signature;
- ``False`` - unsatisfiable, reported ONLY for a complete proteome;
- ``None``  - not satisfiable but the proteome is not complete enough to say so.

This matches the exclusion-only semantics of MODULE_CONTEXT conditions: an
incomplete proteome never blocks an annotation.

>>> from ai_gene_review.module_logic import And, Atom
>>> det = Detector(module_id="MODULE:m", module_path=Path("x.yaml"),
...     steps={"a": ["IPR1"]}, extra_steps={"mod": ["IPR9"]})
>>> circuit = And("m", [Atom("a", "a", None, None)])
>>> evaluate_module(det, {"IPR1": True, "IPR9": True}, complete=True, circuit=circuit)
True
>>> evaluate_module(det, {"IPR1": True, "IPR9": False}, complete=True, circuit=circuit)
False
>>> evaluate_module(det, {"IPR1": False, "IPR9": True}, complete=False, circuit=circuit) is None
True

CLI: ``python -m ai_gene_review.context_oracle DETECTOR UPID... [--rule RULE] [--refresh]``
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Optional

import yaml

from ai_gene_review.curated_rules import to_uniprot_query
from ai_gene_review.module_logic import Circuit, compile_module_file, is_satisfied, iter_atoms

UNIPROT = "https://rest.uniprot.org"


@dataclass
class Completeness:
    """Thresholds a proteome must meet before absence can be trusted."""

    proteome_types: tuple[str, ...] = ("Reference proteome", "Representative proteome")
    min_busco: float = 95.0
    assembly_level: str = "full"


@dataclass
class Detector:
    """Signatures that detect each step of a module in a proteome."""

    module_id: str
    module_path: Path
    steps: dict[str, list[str]]
    extra_steps: dict[str, list[str]] = field(default_factory=dict)
    completeness: Completeness = field(default_factory=Completeness)

    @property
    def signatures(self) -> list[str]:
        """Every signature the detector uses, in first-seen order."""
        sigs = [s for group in (*self.steps.values(), *self.extra_steps.values()) for s in group]
        return list(dict.fromkeys(sigs))


@dataclass
class ProteomeInfo:
    """The UniProt proteome fields that decide completeness."""

    upid: str
    organism: str
    taxon_id: int
    proteome_type: str
    busco_score: Optional[float]
    assembly_level: Optional[str]

    def is_complete(self, c: Completeness) -> bool:
        """True when the proteome meets every completeness threshold.

        >>> p = ProteomeInfo("UP1", "x", 1, "Reference proteome", 99, "full")
        >>> p.is_complete(Completeness())
        True
        >>> ProteomeInfo("UP2", "x", 1, "Reference proteome", 89, "full").is_complete(Completeness())
        False
        """
        return (
            self.proteome_type in c.proteome_types
            and self.busco_score is not None
            and self.busco_score >= c.min_busco
            and self.assembly_level == c.assembly_level
        )


def load_detector(path: Path) -> Detector:
    """Load a detector YAML file."""
    with open(path) as f:
        data = yaml.safe_load(f)
    comp = data.get("completeness", {})
    return Detector(
        module_id=data["module"],
        module_path=Path(data["module_path"]),
        steps={k: list(v["signatures"]) for k, v in data["steps"].items()},
        extra_steps={k: list(v["signatures"]) for k, v in (data.get("extra_steps") or {}).items()},
        completeness=Completeness(
            proteome_types=tuple(comp.get("proteome_types", Completeness.proteome_types)),
            min_busco=float(comp.get("min_busco", Completeness.min_busco)),
            assembly_level=comp.get("assembly_level", Completeness.assembly_level),
        ),
    )


def check_detector(det: Detector, circuit: Circuit) -> list[str]:
    """Every module step must have a detector entry, and no entry may name an unknown step."""
    atom_ids = {a.node_id for a in iter_atoms(circuit)}
    errors = [f"step {a!r} has no detector" for a in sorted(atom_ids - set(det.steps))]
    errors += [f"detector names unknown step {s!r}" for s in sorted(set(det.steps) - atom_ids)]
    errors += [f"signature {s!r} is not an InterPro id" for s in det.signatures if not s.startswith("IPR")]
    return errors


def evaluate_module(
    det: Detector,
    presence: Mapping[str, bool],
    complete: bool,
    circuit: Optional[Circuit] = None,
) -> Optional[bool]:
    """Evaluate the module from signature presence; see the module docstring."""
    circuit = circuit if circuit is not None else compile_module_file(det.module_path)

    def step_present(sigs: list[str]) -> bool:
        return any(presence.get(s, False) for s in sigs)

    satisfied = is_satisfied(circuit, lambda atom: step_present(det.steps.get(atom.node_id, []))) and all(
        step_present(sigs) for sigs in det.extra_steps.values()
    )
    if satisfied:
        return True
    return False if complete else None


def _get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=120) as resp:
        return json.load(resp)


def _count(query: str, attempts: int = 4) -> int:
    """UniProtKB hit count for ``query``, retrying transient network failures."""
    params = urllib.parse.urlencode({"query": query, "size": 1, "format": "list"})
    url = f"{UNIPROT}/uniprotkb/search?{params}"
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=180) as resp:
                return int(resp.headers["X-Total-Results"])
        except (TimeoutError, OSError):
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise AssertionError("unreachable")


def fetch_proteome(upid: str) -> ProteomeInfo:
    """Fetch completeness fields for a UniProt proteome (network)."""
    d = _get_json(f"{UNIPROT}/proteomes/{upid}.json")
    busco = (d.get("proteomeCompletenessReport") or {}).get("buscoReport") or {}
    return ProteomeInfo(
        upid=d["id"],
        organism=d["taxonomy"]["scientificName"],
        taxon_id=int(d["taxonomy"]["taxonId"]),
        proteome_type=d["proteomeType"],
        busco_score=busco.get("score"),
        assembly_level=(d.get("genomeAssembly") or {}).get("level"),
    )


def fetch_presence(upid: str, signatures: list[str]) -> dict[str, int]:
    """Number of proteome members matching each InterPro signature (network)."""
    return {s: _count(f"proteome:{upid} AND xref:interpro-{s}") for s in signatures}


def cache_path(detector_path: Path) -> Path:
    """Committed cache file for a detector."""
    return detector_path.parent / "cache" / f"{detector_path.stem}.yaml"


def load_cache(detector_path: Path) -> dict:
    """Cached proteome info and signature counts, keyed by proteome id."""
    path = cache_path(detector_path)
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def save_cache(detector_path: Path, cache: dict) -> None:
    """Write the cache file."""
    path = cache_path(detector_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.safe_dump(cache, f, sort_keys=True)


def resolve(
    detector_path: Path, upids: list[str], refresh: bool = False, rule_path: Optional[Path] = None
) -> dict:
    """Ensure the cache holds each proteome (fetching if needed) and return it."""
    det = load_detector(detector_path)
    cache = load_cache(detector_path)
    rule = yaml.safe_load(rule_path.read_text()) if rule_path else None
    for upid in upids:
        entry = cache.get(upid)
        if refresh or entry is None or set(det.signatures) - set(entry.get("signature_counts", {})):
            info = fetch_proteome(upid)
            entry = {
                "fetched": datetime.date.today().isoformat(),
                "proteome": info.__dict__,
                "signature_counts": fetch_presence(upid, det.signatures),
            }
        if rule is not None and rule["id"] not in entry.get("rule_matches", {}):
            matches = _count(f"proteome:{upid} AND ({to_uniprot_query(rule)})")
            entry.setdefault("rule_matches", {})[rule["id"]] = matches
        cache[upid] = entry
        save_cache(detector_path, cache)
    return cache


def evaluate_cached(det: Detector, entry: dict, circuit: Optional[Circuit] = None) -> Optional[bool]:
    """Evaluate the module for one cached proteome entry."""
    info = ProteomeInfo(**entry["proteome"])
    presence = {s: n > 0 for s, n in entry["signature_counts"].items()}
    return evaluate_module(det, presence, info.is_complete(det.completeness), circuit)


def main(argv: Optional[list[str]] = None) -> int:
    """Resolve proteomes and print the module verdict (and rule effect) for each."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("detector", type=Path)
    parser.add_argument("upids", nargs="*", help="UniProt proteome ids (default: all cached)")
    parser.add_argument("--rule", type=Path, help="curated rule to report match counts for")
    parser.add_argument("--refresh", action="store_true", help="re-fetch cached proteomes")
    args = parser.parse_args(argv)

    det = load_detector(args.detector)
    circuit = compile_module_file(det.module_path)
    errors = check_detector(det, circuit)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    upids = args.upids or sorted(load_cache(args.detector))
    cache = resolve(args.detector, upids, args.refresh, args.rule)
    rule_id = yaml.safe_load(args.rule.read_text())["id"] if args.rule else None
    for upid in upids:
        entry = cache[upid]
        p = entry["proteome"]
        verdict = evaluate_cached(det, entry, circuit)
        line = f"{upid}\t{p['organism']}\t{verdict}"
        if rule_id:
            n = entry["rule_matches"][rule_id]
            effect = "blocks" if verdict is False else "annotates"
            line += f"\t{rule_id} {effect} {n}"
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
