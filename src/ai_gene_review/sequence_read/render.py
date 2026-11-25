"""Render the run files of a gene into ``sequence-read/RESULTS.md``.

Everything in the page is computed from the run files; nothing is typed in by
hand. Each finding is one line so that a review can quote it as
``supporting_text`` from ``file:ORG/GENE/GENE-bioinformatics/sequence-read/RESULTS.md``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ai_gene_review.sequence_read import core

CAVEATS = [
    "This is a language model reading the sequence with no tools, alignment or database; it is not literature and not a curated record.",
    "Its errors are stated as confidently as its correct calls; every position it names is checked below against the sequence and UniProt.",
    "For a well-studied protein the answer may be recall of the entry rather than a reading of the residues; the shuffled and decoy controls test the reading.",
    "A lost catalytic residue suggests, but does not prove, loss of activity: catalytic residues can be displaced, and dead enzymes often have non-catalytic functions.",
    "Intact catalytic motifs do not guarantee detectable activity.",
    "In the fs2f benchmark Fable 5.2 named the exact Pfam family for 8 of 15 obscure DUF proteins and Opus 5.5 for 3, so an empty or wrong domain list for a DUF protein is expected, not informative.",
]


def _range(d: dict[str, Any]) -> str:
    return f"{d.get('start')}-{d.get('end')}"


def render_run(doc: dict[str, Any]) -> list[str]:
    """Markdown lines for one run file."""
    out = [
        f"## {doc['model']} (effort {doc['effort']}), {doc['run_date']}",
        "",
        f"- Sequence: UniProtKB:{doc['accession']} sequence version {doc['sequence_version']}, "
        f"{doc['sequence_length']} aa, CRC64 {doc['sequence_crc64']}.",
        f"- Route: {doc['route']}.",
        f"- Prompts: FEAT and PSEUDO prompts of {doc['prompts_from']}, verbatim.",
        "",
    ]
    calls = doc["calls"]
    checks = doc["checks"]
    helpers = sorted(
        {m for c in calls for m in (c.get("model_usage") or {}) if m != doc["model"]}
    )
    for m in helpers:
        listed = [c for c in calls if m in (c.get("model_usage") or {})]
        main = sum(
            1
            for c in listed
            if c.get("num_turns") == 1
            and (c["model_usage"].get(doc["model"]) or {}).get("outputTokens")
            == c.get("output_tokens")
        )
        out.append(
            f"- The claude tool's usage record lists a second model, {m}, on {len(listed)} of {len(calls)} calls. "
            f"In {main} of them the reply is one turn whose token counts are those of {doc['model']}, "
            "so the second model's request was a side call by the tool; the record cannot show what it was for."
        )
    unusable = [c for c in calls if not core.usable(c)]
    for c in unusable:
        why = c.get("error") or (
            "context_tokens_high"
            if c.get("context_tokens_high")
            else "no readable answer"
        )
        out.append(f"- Unusable call: {c['question']}/{c['condition']} ({why}).")
    if unusable:
        out.append("")
    real = next(
        (c for c in calls if (c["question"], c["condition"]) == ("features", "real")),
        None,
    )
    if real and core.usable(real):
        a = real["answer"]
        out += [
            "### Domains and membrane features (FEAT prompt)",
            "",
            f"- Model protein name: {a.get('protein_name')}.",
            f"- Model function: {a.get('function')}",
            f"- Model EC number: {a.get('ec_number')}.",
        ]
        f = checks["features"]
        src = (
            doc["reference"].get("pfam_source")
            or "UniProt Pfam cross-references (no boundaries)"
        )
        for d in f["pfam"]:
            iou = f", boundary IoU {d['iou']}" if "iou" in d else ""
            out.append(
                f"- Predicted Pfam {d['accession']} ({d.get('name')}) at {_range(d)}: "
                f"{d['verdict']} against {src}{iou}."
            )
        if not f["pfam"]:
            out.append("- Predicted Pfam domains: none.")
        for acc in f["pfam_missed"]:
            out.append(f"- Reference Pfam {acc} not predicted.")
        out.append(
            f"- Transmembrane helices: {f['tm_predicted']} predicted, {f['tm_reference']} in UniProt, "
            f"{f['tm_recovered']} of {f['tm_reference']} UniProt helices overlapped by a prediction."
        )
        out.append(
            f"- Signal peptide: predicted {f['signal_peptide_predicted']}, UniProt "
            f"{f['signal_peptide_reference']}."
        )
        out.append("")
    if "shuffled" in checks:
        s = checks["shuffled"]
        verdict = (
            "passes (no domain assigned to the shuffled sequence)"
            if s["pfam_domains"] == 0
            else "FAILS (a domain was assigned to the shuffled sequence; treat the domain calls above with suspicion)"
        )
        out += [
            "### Shuffled-sequence control",
            "",
            f"- Shuffled sequence: {s['pfam_domains']} Pfam domains and {s['transmembrane_helices']} "
            f"transmembrane helices predicted; control {verdict}.",
            "",
        ]
    wt = next(
        (
            c
            for c in calls
            if (c["question"], c["condition"]) == ("activity", "wild_type")
        ),
        None,
    )
    if wt and core.usable(wt):
        a = wt["answer"]
        act = checks["activity"]
        out += [
            "### Catalytic residues (PSEUDO prompt)",
            "",
            f"- Model enzyme family: {a.get('enzyme_family')}; catalytically active: "
            f"{a.get('catalytically_active')}; EC {a.get('ec_number')}.",
            f"- Model reason: {a.get('reason')}",
        ]
        for r in act["catalytic_residues"]:
            seqtxt = (
                "present in the sequence"
                if r["present_in_sequence"]
                else f"NOT in the sequence (residue there is {r['residue_in_sequence']})"
            )
            uni = (
                f", UniProt {r['uniprot']}" if r["uniprot"] else ", not a UniProt site"
            )
            out.append(
                f"- Named catalytic residue {r['residue']}{r['position']} ({r['role']}): {seqtxt}{uni}."
            )
        for r in act["substituted_or_missing"]:
            out.append(
                f"- Reported lost residue: {r.get('role')}, expected {r.get('expected')}, "
                f"found {r.get('found')} at {r.get('position')}"
                + {
                    True: " (matches the sequence).",
                    False: " (DOES NOT match the sequence).",
                    None: ".",
                }[r.get("found_in_sequence")]
            )
        if not act["substituted_or_missing"]:
            out.append("- Reported lost catalytic or cofactor residues: none.")
        for p in act["uniprot_active_sites_not_named"]:
            out.append(f"- UniProt active site {p} not named by the model.")
        out.append("")
    probe = checks.get("probe")
    if probe:
        out += ["### Catalytic-substitution and decoy probe", ""]
        if "skipped" in probe:
            out.append(f"- Probe not run: {probe['skipped']}.")
        else:
            out += [
                f"- Catalytic substitution {probe['target']} ({probe['target_source']}): "
                f"called active {probe['mutant_call']}; position reported as lost: "
                f"{probe['mutant_reports_position']}.",
                f"- Decoy substitution {probe['decoy']} (drawn from {probe['decoy_candidates']} unannotated "
                f"same-type residues): called active {probe['decoy_call']}; position reported as lost: "
                f"{probe['decoy_reports_position']}.",
                f"- Probe verdict: {probe['verdict']} (wild type called active {probe['wild_type_call']}).",
            ]
        out.append("")
    return out


def render(out_dir: Path, gene: str) -> Path:
    """Write ``RESULTS.md`` for every run file in ``out_dir``; returns its path."""
    runs = sorted(out_dir.glob("*.json"))
    if not runs:
        raise FileNotFoundError(f"no run files in {out_dir}")
    lines = [
        f"# {gene}: sequence-only language-model read",
        "",
        "**Not literature evidence.** A general frontier language model was given only the amino-acid "
        "sequence and asked the FEAT and PSEUDO questions of the fable-sequence-to-function study "
        f"({core.FS2F_REPO}). Use it to flag or corroborate, never as the sole support for an annotation.",
        "",
        "Caveats:",
        "",
        *[f"- {c}" for c in CAVEATS],
        "",
        "Probe verdicts: TRACKS_CATALYTIC_RESIDUE means the call changed for the catalytic substitution and "
        "not for the decoy; REJECTS_ANY_CHANGE means the decoy also changed the call, so the read is not "
        "residue-specific; INSENSITIVE means neither changed it.",
        "",
    ]
    for p in runs:
        lines += render_run(json.loads(p.read_text()))
    path = out_dir / "RESULTS.md"
    path.write_text("\n".join(lines).rstrip() + "\n")
    return path
