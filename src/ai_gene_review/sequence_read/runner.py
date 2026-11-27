"""Run a sequence-only read for one gene and write its run file.

A run asks up to five questions:

1. ``features``/``real``: Pfam domains with boundaries, TM helices, signal peptide, function.
2. ``features``/``shuffled``: the same question on the shuffled sequence (control).
3. ``activity``/``wild_type``: catalytic residues present or lost, active or not.
4. ``activity``/``catalytic_mutant``: one catalytic residue substituted (probe).
5. ``activity``/``decoy``: the same substitution at an unannotated residue (control).

Questions 4 and 5 are asked only when the wild type is called active and a
catalytic residue can be chosen (``core.choose_probe``).
"""

from __future__ import annotations

import json
import re
import shlex
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any, Callable, Optional

from ai_gene_review.sequence_read import core

Caller = Callable[[str], dict[str, Any]]


def gene_dir(organism: str, gene: str, root: Path = Path("genes")) -> Path:
    """The gene folder.

    >>> gene_dir("human", "PTEN")
    PosixPath('genes/human/PTEN')
    """
    return root / organism / gene


def output_dir(organism: str, gene: str, root: Path = Path("genes")) -> Path:
    """Where runs and the rendered RESULTS.md live.

    >>> output_dir("human", "PTEN")
    PosixPath('genes/human/PTEN/PTEN-bioinformatics/sequence-read')
    """
    return gene_dir(organism, gene, root) / f"{gene}-bioinformatics" / "sequence-read"


def cli_route(cli_version: str) -> str:
    """Provenance string for the claude command-line route."""
    return f"claude CLI {cli_version}, flags: {shlex.join(core.CLI_FLAGS)}"


def run_path(out: Path, model: str, effort: str) -> Path:
    """One run file per model and effort.

    >>> run_path(Path("x"), "claude-fable-5-2", "high")
    PosixPath('x/claude-fable-5-2-high.json')
    """
    return out / f"{model}-{effort}.json"


def _ask(
    caller: Caller, question: str, condition: str, sequence: str, **extra: Any
) -> dict[str, Any]:
    prompt = core.PROMPTS[question] + core.fasta(sequence)
    rec = caller(prompt)
    rec.update(question=question, condition=condition, **extra)
    if "text" in rec:
        rec["answer"] = core.extract_answer(rec["text"], core.KEYS[question])
    return rec


def run_read(
    record: core.ProteinRecord,
    caller: Caller,
    pfam: Optional[list[dict[str, Any]]],
    controls: bool = True,
) -> dict[str, Any]:
    """Ask the questions and check the answers; returns the run document (no metadata)."""
    seq = record.sequence
    reference = core.reference_summary(record, pfam)
    jobs = [("features", "real", seq), ("activity", "wild_type", seq)]
    if controls:
        jobs.append(("features", "shuffled", core.shuffled(seq, record.accession)))
    with ThreadPoolExecutor(len(jobs)) as ex:
        calls = list(ex.map(lambda j: _ask(caller, *j), jobs))
    checks = base_checks(record, calls, reference)
    by = {(c["question"], c["condition"]): c for c in calls}
    wt = by[("activity", "wild_type")]
    probe_note = ""
    if core.usable(wt):
        if not controls:
            probe_note = "controls not requested"
        elif wt["answer"].get("catalytically_active") != "yes":
            probe_note = (
                "wild type not called active, so a substitution cannot change the call"
            )
        else:
            probe, probe_note = core.choose_probe(record, wt["answer"])
            if probe is not None:
                calls += _run_probe(caller, seq, probe, checks)
    else:
        probe_note = "wild-type activity call unusable"
    if probe_note:
        checks["probe"] = {"skipped": probe_note}
    return {"reference": reference, "calls": calls, "checks": checks}


def _run_probe(
    caller: Caller, seq: str, probe: core.Probe, checks: dict[str, Any]
) -> list[dict[str, Any]]:
    jobs = [
        (
            "activity",
            "catalytic_mutant",
            core.substitute(seq, probe.target_position, probe.new_residue),
            probe.label(probe.target_position),
        )
    ]
    if probe.decoy_position is not None:
        jobs.append(
            (
                "activity",
                "decoy",
                core.substitute(seq, probe.decoy_position, probe.new_residue),
                probe.label(probe.decoy_position),
            )
        )
    with ThreadPoolExecutor(len(jobs)) as ex:
        calls = list(
            ex.map(lambda j: _ask(caller, j[0], j[1], j[2], substitution=j[3]), jobs)
        )
    checks["probe"] = probe_summary(
        calls,
        checks["activity"]["catalytically_active"],
        probe.target_source,
        probe.decoy_candidates,
    )
    return calls


def position_of(label: Optional[str]) -> Optional[int]:
    """The position in a substitution label.

    >>> position_of("C124A"), position_of(None)
    (124, None)
    """
    m = re.fullmatch(r"[A-Z](\d+)[A-Z]", label or "")
    return int(m.group(1)) if m else None


def probe_summary(
    calls: list[dict[str, Any]],
    wild_type_call: Optional[str],
    target_source: str,
    decoy_candidates: Optional[int],
) -> dict[str, Any]:
    """Checks and verdict for the catalytic-mutant and decoy calls of a probe."""
    by = {c["condition"]: c for c in calls if c["question"] == "activity"}

    def label(cond: str) -> Optional[str]:
        c = by.get(cond)
        return c.get("substitution") if c else None

    def call_of(cond: str) -> Optional[str]:
        c = by.get(cond)
        return c["answer"].get("catalytically_active") if c and core.usable(c) else None

    def reports(cond: str) -> bool:
        c = by.get(cond)
        pos = position_of(label(cond))
        return bool(
            pos is not None
            and c
            and core.usable(c)
            and core.reports_position(c["answer"], pos)
        )

    return {
        "target": label("catalytic_mutant"),
        "target_source": target_source,
        "decoy": label("decoy"),
        "decoy_candidates": decoy_candidates,
        "wild_type_call": wild_type_call,
        "mutant_call": call_of("catalytic_mutant"),
        "decoy_call": call_of("decoy"),
        "mutant_reports_position": reports("catalytic_mutant"),
        "decoy_reports_position": reports("decoy"),
        "verdict": core.probe_verdict(
            wild_type_call,
            call_of("catalytic_mutant"),
            call_of("decoy"),
            reports("catalytic_mutant"),
            reports("decoy"),
        ),
    }


def base_checks(
    record: core.ProteinRecord,
    calls: list[dict[str, Any]],
    reference: dict[str, Any],
) -> dict[str, Any]:
    """Checks of the features, shuffled and wild-type activity calls."""
    by = {(c["question"], c["condition"]): c for c in calls}
    checks: dict[str, Any] = {}
    real = by.get(("features", "real"))
    if real is not None and core.usable(real):
        checks["features"] = core.check_features(real["answer"], reference)
    shuf = by.get(("features", "shuffled"))
    if shuf is not None and core.usable(shuf):
        checks["shuffled"] = {
            "pfam_domains": len(shuf["answer"].get("pfam_domains") or []),
            "transmembrane_helices": len(
                shuf["answer"].get("transmembrane_helices") or []
            ),
        }
    shuf_act = by.get(("activity", "shuffled"))
    if shuf_act is not None and core.usable(shuf_act):
        checks["shuffled_activity"] = {
            "catalytically_active": shuf_act["answer"].get("catalytically_active"),
            "enzyme_family": shuf_act["answer"].get("enzyme_family"),
        }
    wt = by.get(("activity", "wild_type"))
    if wt is not None and core.usable(wt):
        checks["activity"] = core.check_activity(
            wt["answer"], record.sequence, reference
        )
    return checks


def write_run(
    organism: str,
    gene: str,
    record: core.ProteinRecord,
    body: dict[str, Any],
    model: str,
    effort: str,
    route: str,
    path: Path,
) -> Path:
    """Write the run document with its provenance."""
    doc = {
        "format": core.RUN_FORMAT,
        "label": "Sequence-only language-model read; not literature evidence",
        "organism": organism,
        "gene": gene,
        "accession": record.accession,
        "sequence_length": len(record.sequence),
        "sequence_crc64": record.crc64,
        "sequence_version": record.sequence_version,
        "model": model,
        "effort": effort,
        "route": route,
        "run_date": date.today().isoformat(),
        "prompts_from": f"{core.FS2F_REPO} @ {core.FS2F_COMMIT}",
        **body,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return path
