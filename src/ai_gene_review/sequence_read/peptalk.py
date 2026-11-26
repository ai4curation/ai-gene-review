"""The isolated blind control through peptalk-llm (direct API calls), and its import.

peptalk (``pip install peptalk-llm``; https://github.com/ai4curation/peptalk) asks
the fs2f prompts as one direct API call per question, with no system prompt, no
tools and, with ``--context blind``, nothing but ``>sequence`` in the header. It
also checks that the provider counted no input beyond the prompt. That makes it a
cleaner blind control than the ``claude`` command-line route, which adds context of
its own and, in our runs, a helper-model side call.

This module writes the FASTA files to give peptalk (the wild type, and the
catalytic mutant and decoy of the fs2f probe) and converts peptalk's JSONL records
into a run file, so the same checks and ``RESULTS.md`` apply.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from ai_gene_review.sequence_read import core, runner

TASKS = {"features": "features", "active-site": "activity"}


def fasta_record(name: str, seq: str) -> str:
    """One FASTA record (60 per line)."""
    return f">{name}\n{core.fasta(seq)}\n"


def probe_for(
    record: core.ProteinRecord, position: Optional[int], kinase: bool = False
) -> Optional[core.Probe]:
    """The probe for a blind control: at ``position``, else the first UniProt ACT_SITE.

    >>> r = core.read_uniprot(Path("genes/human/PTEN/PTEN-uniprot.txt"))
    >>> p = probe_for(r, None)
    >>> p.label(p.target_position), p.target_source
    ('C124A', 'UniProt ACT_SITE')
    """
    family = "kinase" if kinase else ""
    if position is not None:
        return core.probe_at(record, position, "position chosen by the curator", family)
    for f in record.of_type("ACT_SITE"):
        if f.start == f.end and core.replacement_for(
            record.sequence[f.start - 1], family
        ):
            return core.probe_at(record, f.start, "UniProt ACT_SITE", family)
    return None


def write_fastas(
    record: core.ProteinRecord, out: Path, gene: str, probe: Optional[core.Probe]
) -> list[Path]:
    """Write ``GENE-blind.fasta`` (wild type) and, with a probe, ``GENE-probe.fasta``.

    Record names encode the condition and substitution, e.g.
    ``Q8NDY3.catalytic_mutant.D58A``; with ``--context blind`` peptalk sends the
    model ``>sequence`` only, so the names never reach it.
    """
    out.mkdir(parents=True, exist_ok=True)
    acc, seq = record.accession, record.sequence
    paths = [out / f"{gene}-blind.fasta"]
    paths[0].write_text(fasta_record(f"{acc}.wild_type", seq))
    if probe is not None:
        recs = [
            fasta_record(
                f"{acc}.catalytic_mutant.{probe.label(probe.target_position)}",
                core.substitute(seq, probe.target_position, probe.new_residue),
            )
        ]
        if probe.decoy_position is not None:
            recs.append(
                fasta_record(
                    f"{acc}.decoy.{probe.label(probe.decoy_position)}",
                    core.substitute(seq, probe.decoy_position, probe.new_residue),
                )
            )
        paths.append(out / f"{gene}-probe.fasta")
        paths[1].write_text("".join(recs))
    return paths


def _call(rec: dict[str, Any], record: core.ProteinRecord) -> dict[str, Any]:
    """Convert one peptalk record into a call record of the run file."""
    if rec.get("context") != "blind":
        raise ValueError(
            f"{rec.get('id')}: peptalk context is {rec.get('context')!r}; the control needs --context blind"
        )
    if rec["task"] not in TASKS:
        raise ValueError(
            f"{rec['id']}: task {rec['task']!r} is not features or active-site"
        )
    acc, cond, *sub = rec["id"].split(".")
    if acc != record.accession:
        raise ValueError(f"{rec['id']}: not a record of {record.accession}")
    question = TASKS[rec["task"]]
    seq = record.sequence
    substitution = sub[0] if sub else None
    if rec["condition"] == "shuffled":
        if cond != "wild_type":
            raise ValueError(
                f"{rec['id']}: a shuffled control must be of the wild type"
            )
        condition = "shuffled"
        if sorted(rec["sequence"]) != sorted(seq):
            raise ValueError(f"{rec['id']}: shuffled sequence has another composition")
    else:
        if cond == "wild_type":
            condition = "real" if question == "features" else "wild_type"
            expected = seq
        else:
            condition = cond
            pos = runner.position_of(substitution)
            if cond not in ("catalytic_mutant", "decoy") or pos is None:
                raise ValueError(f"{rec['id']}: not a name written by blind-fasta")
            assert substitution is not None
            expected = core.substitute(seq, pos, substitution[-1])
        if rec["sequence"] != expected:
            raise ValueError(f"{rec['id']}: sequence does not match the UniProt record")
    if rec.get("prompt_sha256") != core.sha256(
        core.PROMPTS[question] + core.fasta(rec["sequence"])
    ):
        raise ValueError(
            f"{rec['id']}: peptalk prompt is not the fs2f {question} prompt verbatim"
        )
    usage = rec.get("usage") or {}
    checks = rec.get("checks") or []
    # True: peptalk counted the prompt and the call sent nothing else; False: it sent
    # more; None: peptalk did not check (e.g. --no-verify-input), so not verified.
    input_checks = [c["passed"] for c in checks if c["name"] == "input_tokens_match"]
    blind_verified = all(input_checks) if input_checks else None
    out: dict[str, Any] = {
        "question": question,
        "condition": condition,
        "prompt_sha256": rec.get("prompt_sha256"),
        "peptalk_prompt_version": rec.get("prompt_version"),
        "asked_at": rec.get("finished_at"),
        "text": rec.get("text") or "",
        "answer": rec.get("answer"),
        "is_error": rec.get("error") is not None,
        "cost_usd": rec.get("cost_usd"),
        "served": [rec.get("served_model")],
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "thinking_tokens": usage.get("thinking_tokens"),
        "context_tokens_high": blind_verified is False,
        "context_unverified": blind_verified is None,
        "peptalk_checks": checks,
        "peptalk_confidence": rec.get("confidence"),
    }
    if rec.get("error"):
        out["error"] = str(rec["error"])
    if substitution:
        out["substitution"] = substitution
    return out


def probe_from_calls(
    record: core.ProteinRecord, calls: list[dict[str, Any]]
) -> core.Probe:
    """The probe the imported records encode, with its decoy checked against the rule.

    The target comes from the catalytic-mutant record's name (``...catalytic_mutant.C124A``);
    its source is UniProt ACT_SITE only when UniProt annotates that position as one.
    ``core.probe_at`` then re-derives the decoy, which must be the imported one.
    """
    by = {c["condition"]: c for c in calls if c["question"] == "activity"}
    if "catalytic_mutant" not in by:
        raise ValueError("a decoy was imported without its catalytic mutant")
    label = by["catalytic_mutant"]["substitution"]
    pos = runner.position_of(label)
    assert pos is not None
    act = {f.start for f in record.of_type("ACT_SITE") if f.start == f.end}
    source = (
        "UniProt ACT_SITE"
        if pos in act
        else "position chosen by the curator (blind-fasta --position)"
    )
    family = "kinase" if label[-1] in "NM" and label[0] in "DK" else ""
    probe = core.probe_at(record, pos, source, family)
    if probe.label(pos) != label:
        raise ValueError(f"{label} is not the substitution blind-fasta makes at {pos}")
    decoy = by.get("decoy", {}).get("substitution")
    want = probe.label(probe.decoy_position) if probe.decoy_position else None
    if decoy is not None and decoy != want:
        raise ValueError(f"decoy {decoy} is not the one the decoy rule gives ({want})")
    return probe


def import_records(
    record: core.ProteinRecord,
    rows: list[dict[str, Any]],
    pfam: Optional[list[dict[str, Any]]],
) -> tuple[dict[str, Any], str, str, str]:
    """Build the run body from peptalk records; returns (body, model, effort, route)."""
    for key in ("model", "effort", "provider", "annotator_version"):
        if len({r.get(key) for r in rows}) != 1:
            raise ValueError(f"peptalk records mix more than one {key}")
    calls = [_call(r, record) for r in rows]
    reference = core.reference_summary(record, pfam)
    checks = runner.base_checks(record, calls, reference)
    conds = {c["condition"] for c in calls}
    if {"catalytic_mutant", "decoy"} & conds:
        probe = probe_from_calls(record, calls)
        checks["probe"] = runner.probe_summary(
            calls,
            checks.get("activity", {}).get("catalytically_active"),
            probe.target_source,
            probe.decoy_candidates,
        )
    else:
        checks["probe"] = {"skipped": "no probe records imported"}
    r0 = rows[0]
    route = (
        f"peptalk-llm {r0['annotator_version']}, direct {r0['provider']} API call, "
        "--context blind (header reduced to >sequence)"
    )
    return (
        {"reference": reference, "calls": calls, "checks": checks},
        r0["model"],
        r0["effort"],
        route,
    )


def read_jsonl(paths: list[Path]) -> list[dict[str, Any]]:
    """All records of the given peptalk JSONL files."""
    return [
        json.loads(line)
        for p in paths
        for line in p.read_text().splitlines()
        if line.strip()
    ]
