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
import csv
import datetime
import io
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
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
    return _proteome_from_json(_get_json(f"{UNIPROT}/proteomes/{upid}.json"))


def _proteome_from_json(d: dict) -> ProteomeInfo:
    """Completeness fields from a UniProt proteome JSON record."""
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


def _stream(url: str, attempts: int = 4) -> str:
    """GET a UniProt stream endpoint, retrying transient network failures."""
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=600) as resp:
                return resp.read().decode()
        except (TimeoutError, OSError):
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise AssertionError("unreachable")


def proteome_counts(tsv: str) -> tuple[Counter[str], int]:
    r"""Count entries per proteome in a UniProt TSV with a ``Proteomes`` column.

    Returns the per-proteome counts and the number of entries in no proteome.

    >>> tsv = "Entry\tProteomes\nA\tUP1: Chromosome\nB\tUP1: Chromosome\nC\t\n"
    >>> counts, unassigned = proteome_counts(tsv)
    >>> dict(counts), unassigned
    ({'UP1': 2}, 1)
    """
    counts: Counter[str] = Counter()
    unassigned = 0
    for row in csv.DictReader(io.StringIO(tsv), delimiter="\t"):
        upids = [x.split(":")[0].strip() for x in (row.get("Proteomes") or "").split(";") if x.strip()]
        if not upids:
            unassigned += 1
        counts.update(upids)
    return counts, unassigned


def _entry_proteome_counts(query: str) -> tuple[Counter[str], int]:
    """Per-proteome entry counts for a UniProtKB query (network)."""
    params = urllib.parse.urlencode({"query": query, "fields": "accession,xref_proteomes", "format": "tsv"})
    return proteome_counts(_stream(f"{UNIPROT}/uniprotkb/stream?{params}"))


def fetch_proteomes(upids: list[str], batch: int = 100) -> dict[str, ProteomeInfo]:
    """Completeness fields for many proteomes, fetched in batches (network)."""
    out: dict[str, ProteomeInfo] = {}
    for i in range(0, len(upids), batch):
        query = " OR ".join(f"upid:{u}" for u in upids[i:i + batch])
        params = urllib.parse.urlencode({"query": query, "format": "json"})
        for d in json.loads(_stream(f"{UNIPROT}/proteomes/stream?{params}"))["results"]:
            info = _proteome_from_json(d)
            out[info.upid] = info
    return out


def bulk_resolve(detector_path: Path, rule_path: Path, taxon_id: int) -> dict:
    """Resolve every proteome of ``taxon_id`` that has a protein matching the rule.

    Signature counts are taken from entries of ``taxon_id`` only, which is exact
    for proteomes of that taxon. Uses one streamed query per signature instead of
    one count query per (proteome, signature). Returns a summary including the
    number of rule matches that belong to no proteome (these cannot be evaluated).
    """
    det = load_detector(detector_path)
    rule = yaml.safe_load(rule_path.read_text())
    rule_counts, unassigned = _entry_proteome_counts(f"({to_uniprot_query(rule)}) AND taxonomy_id:{taxon_id}")
    sig_counts = {
        s: _entry_proteome_counts(f"xref:interpro-{s} AND taxonomy_id:{taxon_id}")[0] for s in det.signatures
    }
    infos = fetch_proteomes(sorted(rule_counts))
    cache = load_cache(detector_path)
    today = datetime.date.today().isoformat()
    for upid, info in infos.items():
        cache[upid] = {
            "fetched": today,
            "proteome": info.__dict__,
            "signature_counts": {s: sig_counts[s][upid] for s in det.signatures},
            "rule_matches": {rule["id"]: rule_counts[upid]},
        }
    save_cache(detector_path, cache)
    return {
        "rule": rule["id"],
        "taxon_id": taxon_id,
        "proteomes": sorted(infos),
        "missing_proteome_records": sorted(set(rule_counts) - set(infos)),
        "entries_without_proteome": unassigned,
    }


def summarise(det: Detector, cache: dict, upids: list[str], rule_id: str, circuit: Optional[Circuit] = None) -> dict:
    """Count proteomes and rule-matched proteins by module verdict."""
    out = {v: {"proteomes": 0, "proteins": 0} for v in ("satisfiable", "unsatisfiable", "not_evaluated")}
    names = {True: "satisfiable", False: "unsatisfiable", None: "not_evaluated"}
    for upid in upids:
        verdict = names[evaluate_cached(det, cache[upid], circuit)]
        out[verdict]["proteomes"] += 1
        out[verdict]["proteins"] += cache[upid]["rule_matches"][rule_id]
    return out


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
    parser.add_argument("--taxon", type=int,
                        help="with --rule: resolve every proteome of this NCBI taxon id that the rule matches")
    args = parser.parse_args(argv)

    det = load_detector(args.detector)
    circuit = compile_module_file(det.module_path)
    errors = check_detector(det, circuit)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.taxon is not None:
        if args.rule is None:
            parser.error("--taxon requires --rule")
        result = bulk_resolve(args.detector, args.rule, args.taxon)
        cache = load_cache(args.detector)
        print(yaml.safe_dump({
            "rule": result["rule"],
            "taxon_id": result["taxon_id"],
            "proteomes_resolved": len(result["proteomes"]),
            "missing_proteome_records": result["missing_proteome_records"],
            "entries_without_proteome": result["entries_without_proteome"],
            "by_verdict": summarise(det, cache, result["proteomes"], result["rule"], circuit),
        }, sort_keys=False))
        return 0
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
