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
    by = {(c["question"], c["condition"]): c for c in calls}

    checks: dict[str, Any] = {}
    real = by[("features", "real")]
    if core.usable(real):
        checks["features"] = core.check_features(real["answer"], reference)
    shuf = by.get(("features", "shuffled"))
    if shuf is not None and core.usable(shuf):
        checks["shuffled"] = {
            "pfam_domains": len(shuf["answer"].get("pfam_domains") or []),
            "transmembrane_helices": len(
                shuf["answer"].get("transmembrane_helices") or []
            ),
        }
    wt = by[("activity", "wild_type")]
    probe_note = ""
    if core.usable(wt):
        checks["activity"] = core.check_activity(wt["answer"], seq, reference)
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
    by = {c["condition"]: c for c in calls}

    def call_of(cond: str) -> Optional[str]:
        c = by.get(cond)
        return c["answer"].get("catalytically_active") if c and core.usable(c) else None

    def reports(cond: str, pos: Optional[int]) -> bool:
        c = by.get(cond)
        return bool(
            pos is not None
            and c
            and core.usable(c)
            and core.reports_position(c["answer"], pos)
        )

    mutant_reports = reports("catalytic_mutant", probe.target_position)
    decoy_reports = reports("decoy", probe.decoy_position)
    checks["probe"] = {
        "target": probe.label(probe.target_position),
        "target_source": probe.target_source,
        "decoy": probe.label(probe.decoy_position) if probe.decoy_position else None,
        "decoy_candidates": probe.decoy_candidates,
        "wild_type_call": checks["activity"]["catalytically_active"],
        "mutant_call": call_of("catalytic_mutant"),
        "decoy_call": call_of("decoy"),
        "mutant_reports_position": mutant_reports,
        "decoy_reports_position": decoy_reports,
        "verdict": core.probe_verdict(
            checks["activity"]["catalytically_active"],
            call_of("catalytic_mutant"),
            call_of("decoy"),
            mutant_reports,
            decoy_reports,
        ),
    }
    return calls


def write_run(
    organism: str,
    gene: str,
    record: core.ProteinRecord,
    body: dict[str, Any],
    model: str,
    effort: str,
    cli_version: str,
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
        "route": f"claude CLI {cli_version}, flags: {shlex.join(core.CLI_FLAGS)}",
        "run_date": date.today().isoformat(),
        "prompts_from": f"{core.FS2F_REPO} @ {core.FS2F_COMMIT}",
        **body,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return path
