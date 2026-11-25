"""Prompts, controls, model calls and deterministic checks for a sequence-only read.

The two questions are the FEAT and PSEUDO prompts of fable-sequence-to-function
(fs2f) at commit ``442bd92``, verbatim, so that the results here can be read
against the benchmark numbers of that study. The shuffled sequence uses the same
seed (CRC32 of the accession), and the catalytic/decoy probe follows its decoy
control: the same substitution at an annotated catalytic residue and at a
matched residue with no functional annotation.
"""

from __future__ import annotations

import hashlib
import json
import random
import re
import subprocess
import tempfile
import zlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from Bio import SwissProt  # type: ignore[import-untyped]

FS2F_REPO = "https://github.com/ai4curation/fable-sequence-to-function"
FS2F_COMMIT = "442bd92"
RUN_FORMAT = "sequence-read/1"

DEFAULT_MODEL = "claude-fable-5-2"
DEFAULT_EFFORT = "high"

# experiments/features/ask.py (P), verbatim.
FEAT_PROMPT = (
    "Below is a protein sequence in one-letter amino acid codes. Annotate it using only the sequence. "
    "Reply with a single JSON object and nothing else, with these keys: "
    '"pfam_domains": list of {"accession": "PFxxxxx", "name": Pfam short name, "start": int, "end": int} (1-based residue positions; empty list if none recognised); '
    '"transmembrane_helices": list of [start, end]; "signal_peptide": true or false; '
    '"protein_name": string; "ec_number": string or null; "function": one sentence. '
    "Do not guess identifiers you are not confident of: leave a field empty or null instead.\n\n>sequence\n"
)

# experiments/pseudo/ask.py (P), verbatim.
PSEUDO_PROMPT = (
    "Below is a protein sequence in one-letter amino acid codes. Using only the sequence, decide whether the protein is "
    "likely to be catalytically active. Reply with a single JSON object and nothing else, with these keys: "
    '"protein_name": string; "enzyme_family": string; '
    '"catalytic_residues": list of {"role": string, "residue": one-letter code actually present in this sequence, "position": int (1-based)}; '
    '"substituted_or_missing": list of {"role": string, "expected": string, "found": string, "position": int or null} for any canonical catalytic or '
    "cofactor-binding residue that this sequence lacks (empty list if none); "
    '"catalytically_active": "yes", "no" or "uncertain"; "ec_number": string or null; "reason": one or two sentences.\n\n>sequence\n'
)

KEYS = {
    "features": "pfam_domains transmembrane_helices signal_peptide protein_name ec_number function".split(),
    "activity": "protein_name enzyme_family catalytic_residues substituted_or_missing catalytically_active ec_number reason".split(),
}
PROMPTS = {"features": FEAT_PROMPT, "activity": PSEUDO_PROMPT}

# The revised fs2f route (experiments/common.py): built-in tools off, empty system
# prompt, and no user settings, MCP/connector tools, skills or Chrome attached.
CLI_FLAGS = [
    "--system-prompt",
    "",
    "--tools",
    "",
    "--output-format",
    "json",
    "--setting-sources",
    "",
    "--strict-mcp-config",
    "--disable-slash-commands",
    "--no-chrome",
]

# Per-model counts kept from the tool's ``modelUsage`` record. The tool can list a
# second (helper) model beside the requested one; its counts show how much it did.
MODEL_USAGE_KEYS = (
    "inputTokens",
    "outputTokens",
    "cacheReadInputTokens",
    "cacheCreationInputTokens",
    "thinkingTokens",
    "webSearchRequests",
    "costUSD",
)

# A written-out tool invocation in a reply means it holds no answer (fs2f common.TOOL_CALL).
TOOL_CALL = re.compile(
    r"```(?:bash|sh|shell|shell-session|zsh|console)\b|\bcurl\s+(?:-|https?://)|\bwget\s+(?:-|https?://)"
    r"|\brequests\.(?:get|post)\(|\burlopen\(|<function_calls>|<invoke\b|<tool_call>"
    r"|\"type\"\s*:\s*\"(?:tool_use|function)\""
)

# UniProt features near which a decoy substitution is not placed (fs2f decoy rule).
SITE_FEATURES = {
    "ACT_SITE",
    "BINDING",
    "SITE",
    "MOD_RES",
    "DISULFID",
    "CROSSLNK",
    "LIPID",
    "CARBOHYD",
    "MUTAGEN",
}
CATALYTIC_ROLE = re.compile(
    r"catalytic|nucleophile|\bacid\b|\bbase\b|proton (?:donor|acceptor)", re.I
)
CLEAVED_FEATURES = {"SIGNAL", "PROPEP", "TRANSIT", "PEPTIDE"}
DECOY_MARGIN = 3


@dataclass
class Feature:
    """A UniProt feature with 1-based inclusive coordinates."""

    type: str
    start: int
    end: int
    note: str = ""
    evidence: str = ""


@dataclass
class ProteinRecord:
    """The parts of a UniProt entry a sequence-only read is compared with."""

    accession: str
    sequence: str
    crc64: str
    sequence_version: Optional[int]
    features: list[Feature] = field(default_factory=list)
    pfam_accessions: list[str] = field(default_factory=list)

    def of_type(self, *types: str) -> list[Feature]:
        """Features of the given UniProt types."""
        return [f for f in self.features if f.type in types]


def read_uniprot(path: Path) -> ProteinRecord:
    """Read a UniProt flat file (``GENE-uniprot.txt``) into a ProteinRecord.

    >>> r = read_uniprot(Path("genes/human/PTEN/PTEN-uniprot.txt"))
    >>> r.accession, len(r.sequence), r.sequence[123]
    ('P60484', 403, 'C')
    >>> [(f.start, f.end) for f in r.of_type("ACT_SITE")]
    [(124, 124)]
    """
    with path.open() as fh:
        rec = SwissProt.read(fh)
    feats = []
    for f in rec.features:
        start, end = f.location.start, f.location.end
        if start is None or end is None:
            continue
        feats.append(
            Feature(
                type=f.type,
                start=int(start) + 1,
                end=int(end),
                note=str(f.qualifiers.get("note", "")),
                evidence=str(f.qualifiers.get("evidence", "")),
            )
        )
    pfam = [x[1] for x in rec.cross_references if x[0] == "Pfam"]
    version = rec.sequence_update[1] if rec.sequence_update else None
    return ProteinRecord(
        accession=rec.accessions[0],
        sequence=rec.sequence,
        crc64=rec.seqinfo[2],
        sequence_version=version,
        features=feats,
        pfam_accessions=pfam,
    )


def fasta(seq: str, width: int = 60) -> str:
    """Wrap a sequence as fs2f did (60 per line, no header beyond the prompt's).

    >>> fasta("ACDEFGHIK", width=4)
    'ACDE\\nFGHI\\nK'
    """
    return "\n".join(seq[i : i + width] for i in range(0, len(seq), width))


def shuffled(seq: str, accession: str) -> str:
    """The fs2f shuffled control: same composition, seeded by the accession's CRC32.

    >>> s = shuffled("MKTAYIAKQR", "P00001")
    >>> sorted(s) == sorted("MKTAYIAKQR"), s == shuffled("MKTAYIAKQR", "P00001")
    (True, True)
    """
    r = list(seq)
    random.Random(zlib.crc32(accession.encode())).shuffle(r)
    return "".join(r)


def substitute(seq: str, position: int, new: str) -> str:
    """Replace the residue at a 1-based position.

    >>> substitute("MKCA", 3, "A")
    'MKAA'
    """
    return seq[: position - 1] + new + seq[position:]


def json_objects(text: str, keys: list[str]) -> list[dict[str, Any]]:
    """Complete JSON objects in a reply that carry at least two of ``keys``.

    >>> json_objects('x {"a": 1, "b": 2} y {"a": 3}', ["a", "b"])
    [{'a': 1, 'b': 2}]
    """
    dec = json.JSONDecoder()
    out, i = [], 0
    while (i := text.find("{", i)) >= 0:
        try:
            obj, n = dec.raw_decode(text[i:])
        except ValueError:
            i += 1
            continue
        if isinstance(obj, dict) and sum(k in obj for k in keys) >= 2:
            out.append(obj)
        i += n
    return out


def extract_answer(text: str, keys: list[str]) -> Optional[dict[str, Any]]:
    """The fs2f reading rule: the last qualifying JSON object; none if a tool call was written out.

    >>> extract_answer('{"a": 1, "b": 2} then {"a": 5, "b": 6}', ["a", "b"])
    {'a': 5, 'b': 6}
    >>> extract_answer('```bash\\ncurl -s https://x\\n``` {"a": 1, "b": 2}', ["a", "b"]) is None
    True
    """
    if TOOL_CALL.search(text):
        return None
    objs = json_objects(text, keys)
    return objs[-1] if objs else None


def sha256(text: str) -> str:
    """Hex SHA-256 of a prompt, stored so a row can be matched to its question."""
    return hashlib.sha256(text.encode()).hexdigest()


def cli_version(claude_bin: str) -> str:
    """Version string of the ``claude`` command-line tool."""
    p = subprocess.run(
        [claude_bin, "--version"], capture_output=True, text=True, check=True
    )
    return p.stdout.strip()


def call_model(
    claude_bin: str, model: str, effort: str, prompt: str, timeout: int = 3600
) -> dict[str, Any]:
    """Ask one question on the revised fs2f route and return a call record.

    The call runs in an empty temporary directory so no project instructions are
    loaded. A reply whose input is larger than the question allows (the tool's own
    ~600-token context plus the question) is marked ``context_tokens_high``: it may
    have carried attached context and should not be used.
    """
    with tempfile.TemporaryDirectory() as cwd:
        p = subprocess.run(
            [claude_bin, "-p", "--model", model, "--effort", effort, *CLI_FLAGS],
            input=prompt,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=timeout,
        )
    rec: dict[str, Any] = {
        "prompt_sha256": sha256(prompt),
        "asked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    if p.returncode != 0 and not p.stdout.strip():
        rec["error"] = (p.stderr or "")[-500:]
        return rec
    j = json.loads(p.stdout)
    usage = j.get("usage") or {}
    input_tokens = sum(
        int(usage.get(k) or 0)
        for k in (
            "input_tokens",
            "cache_creation_input_tokens",
            "cache_read_input_tokens",
        )
    )
    rec.update(
        text=j.get("result") or "",
        is_error=bool(j.get("is_error")),
        cost_usd=j.get("total_cost_usd"),
        num_turns=j.get("num_turns"),
        served=list((j.get("modelUsage") or {}).keys()),
        model_usage={
            m: {k: v.get(k) for k in MODEL_USAGE_KEYS}
            for m, v in (j.get("modelUsage") or {}).items()
            if isinstance(v, dict)
        },
        input_tokens=input_tokens,
        output_tokens=int(usage.get("output_tokens") or 0),
        thinking_tokens=(usage.get("output_tokens_details") or {}).get(
            "thinking_tokens"
        ),
        context_tokens_high=input_tokens > 1500 + len(prompt),
    )
    return rec


def usable(call: dict[str, Any]) -> bool:
    """Whether a call record holds an answer that can be read."""
    return (
        "error" not in call
        and not call.get("is_error")
        and not call.get("context_tokens_high")
        and call.get("answer") is not None
    )


def overlap(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Residues shared by two inclusive ranges.

    >>> overlap((1, 10), (5, 20)), overlap((1, 4), (5, 9))
    (6, 0)
    """
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


def iou(a: tuple[int, int], b: tuple[int, int]) -> float:
    """Intersection over union of two inclusive ranges, as fs2f scored boundaries.

    >>> round(iou((1, 10), (6, 15)), 3)
    0.333
    """
    inter = overlap(a, b)
    return inter / ((a[1] - a[0] + 1) + (b[1] - b[0] + 1) - inter)


def fetch_pfam_locations(accession: str) -> list[dict[str, Any]]:
    """Pfam matches with boundaries for a UniProt accession, from the InterPro API."""
    import requests

    url = f"https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{accession}/"
    r = requests.get(url, timeout=60)
    if r.status_code == 204:
        return []
    r.raise_for_status()
    out = []
    for res in r.json()["results"]:
        md = res["metadata"]
        for prot in res["proteins"]:
            for loc in prot["entry_protein_locations"]:
                frags = loc["fragments"]
                out.append(
                    {
                        "accession": md["accession"],
                        "name": md["name"],
                        "start": min(f["start"] for f in frags),
                        "end": max(f["end"] for f in frags),
                    }
                )
    return sorted(out, key=lambda d: d["start"])


def reference_summary(
    record: ProteinRecord, pfam: Optional[list[dict[str, Any]]]
) -> dict[str, Any]:
    """The curated features a read is checked against, as stored in the run file."""
    seq = record.sequence
    return {
        "pfam": pfam,
        "pfam_source": "InterPro API" if pfam is not None else None,
        "pfam_accessions_uniprot": record.pfam_accessions,
        "transmembrane": [[f.start, f.end] for f in record.of_type("TRANSMEM")],
        "signal_peptide": [[f.start, f.end] for f in record.of_type("SIGNAL")],
        "active_sites": [
            {
                "position": f.start,
                "residue": seq[f.start - 1],
                "note": f.note,
                "evidence": f.evidence,
            }
            for f in record.of_type("ACT_SITE")
            if f.start == f.end
        ],
        "binding_sites": sorted(
            {p for f in record.of_type("BINDING") for p in range(f.start, f.end + 1)}
        ),
    }


@dataclass
class Probe:
    """A catalytic-residue substitution and its matched decoy."""

    target_position: int
    target_residue: str
    new_residue: str
    target_source: str
    decoy_position: Optional[int]
    decoy_candidates: int

    def label(self, position: int) -> str:
        """Substitution in the usual notation, e.g. C124A."""
        return f"{self.target_residue}{position}{self.new_residue}"


def replacement_for(residue: str, enzyme_family: str) -> Optional[str]:
    """The fs2f substitution: kinase Asp to Asn and Lys to Met, otherwise Ala.

    >>> replacement_for("D", "Protein kinase"), replacement_for("C", "PTP"), replacement_for("A", "x")
    ('N', 'A', None)
    """
    if "kinase" in enzyme_family.lower() and residue in "DK":
        return {"D": "N", "K": "M"}[residue]
    return None if residue == "A" else "A"


def choose_probe(
    record: ProteinRecord, wild_type_answer: dict[str, Any]
) -> tuple[Optional[Probe], str]:
    """Pick a catalytic residue to substitute and a matched decoy position.

    The target is the first single-residue UniProt ACT_SITE, else the first
    residue the model named that is really present at that position, preferring
    one whose stated role is catalytic (nucleophile, acid/base) over a
    cofactor- or substrate-binding one.
    The decoy is a residue of the same type, inside the same UniProt DOMAIN when
    there is one, at least ``DECOY_MARGIN`` residues from any annotated site,
    any residue the model named, and outside cleaved peptides. Returns the probe,
    or None with the reason no probe was made.
    """
    seq = record.sequence
    family = str(wild_type_answer.get("enzyme_family") or "")
    named = [
        r
        for r in wild_type_answer.get("catalytic_residues") or []
        if isinstance(r, dict) and isinstance(r.get("position"), int)
    ]
    target: Optional[tuple[int, str]] = None
    for f in record.of_type("ACT_SITE"):
        if f.start == f.end and replacement_for(seq[f.start - 1], family):
            target = (f.start, "UniProt ACT_SITE")
            break
    if target is None:
        # residues whose stated role is catalytic come before cofactor/binding ones
        for r in sorted(
            named, key=lambda r: not CATALYTIC_ROLE.search(str(r.get("role")))
        ):
            pos = r["position"]
            if 1 <= pos <= len(seq) and seq[pos - 1] == str(r.get("residue")):
                if replacement_for(seq[pos - 1], family):
                    target = (pos, "residue named by the model (no UniProt ACT_SITE)")
                    break
    if target is None:
        return None, "no catalytic residue from UniProt or the model to substitute"
    pos, source = target
    residue = seq[pos - 1]
    new = replacement_for(residue, family)
    assert new is not None
    blocked: set[int] = set()
    for f in record.of_type(*SITE_FEATURES):
        blocked.update(range(f.start - DECOY_MARGIN, f.end + DECOY_MARGIN + 1))
    for r in named + [
        r
        for r in wild_type_answer.get("substituted_or_missing") or []
        if isinstance(r, dict) and isinstance(r.get("position"), int)
    ]:
        p = r["position"]
        blocked.update(range(p - DECOY_MARGIN, p + DECOY_MARGIN + 1))
    for f in record.of_type(*CLEAVED_FEATURES):
        blocked.update(range(f.start, f.end + 1))
    candidates = [
        i + 1 for i, aa in enumerate(seq) if aa == residue and i + 1 not in blocked
    ]
    domains = [f for f in record.of_type("DOMAIN") if f.start <= pos <= f.end]
    if domains:
        inside = [c for c in candidates if domains[0].start <= c <= domains[0].end]
        candidates = inside or candidates
    decoy = (
        random.Random(zlib.crc32(f"{record.accession}:{pos}".encode())).choice(
            candidates
        )
        if candidates
        else None
    )
    return (
        Probe(
            target_position=pos,
            target_residue=residue,
            new_residue=new,
            target_source=source,
            decoy_position=decoy,
            decoy_candidates=len(candidates),
        ),
        "",
    )


def check_features(answer: dict[str, Any], reference: dict[str, Any]) -> dict[str, Any]:
    """Compare a FEAT answer with the curated features.

    >>> ref = {"pfam": [{"accession": "PF00001", "name": "x", "start": 10, "end": 50}],
    ...        "transmembrane": [[60, 80]], "signal_peptide": []}
    >>> ans = {"pfam_domains": [{"accession": "PF00001", "start": 12, "end": 50},
    ...                         {"accession": "PF09999", "start": 90, "end": 99}],
    ...        "transmembrane_helices": [[61, 79], [100, 120]], "signal_peptide": False}
    >>> c = check_features(ans, ref)
    >>> [(d["accession"], d["verdict"]) for d in c["pfam"]], c["pfam_missed"]
    ([('PF00001', 'MATCH'), ('PF09999', 'NOT_IN_REFERENCE')], [])
    >>> c["tm_recovered"], c["tm_reference"], c["tm_predicted"], c["signal_peptide_agrees"]
    (1, 1, 2, True)
    """
    ref_pfam = reference.get("pfam")
    pfam_rows = []
    for d in answer.get("pfam_domains") or []:
        if not isinstance(d, dict):
            continue
        acc = str(d.get("accession") or "")
        row: dict[str, Any] = {
            "accession": acc,
            "name": d.get("name"),
            "start": d.get("start"),
            "end": d.get("end"),
        }
        if ref_pfam is None:
            in_up = acc in reference.get("pfam_accessions_uniprot", [])
            row["verdict"] = "IN_UNIPROT" if in_up else "NOT_IN_REFERENCE"
        else:
            same = [r for r in ref_pfam if r["accession"] == acc]
            if not same and acc in reference.get("pfam_accessions_uniprot", []):
                # InterPro and the UniProt record can be on different Pfam releases
                row["verdict"] = "IN_UNIPROT_NOT_INTERPRO"
            elif not same:
                row["verdict"] = "NOT_IN_REFERENCE"
            else:
                row["verdict"] = "MATCH"
                if isinstance(d.get("start"), int) and isinstance(d.get("end"), int):
                    row["iou"] = round(
                        max(
                            iou((d["start"], d["end"]), (r["start"], r["end"]))
                            for r in same
                        ),
                        2,
                    )
        pfam_rows.append(row)
    named = {r["accession"] for r in pfam_rows}
    if ref_pfam is not None:
        missed = [r["accession"] for r in ref_pfam if r["accession"] not in named]
    else:
        missed = [
            a for a in reference.get("pfam_accessions_uniprot", []) if a not in named
        ]
    pred_tm = [
        tuple(h)
        for h in answer.get("transmembrane_helices") or []
        if isinstance(h, list) and len(h) == 2 and all(isinstance(x, int) for x in h)
    ]
    ref_tm = [tuple(h) for h in reference.get("transmembrane", [])]
    recovered = sum(1 for r in ref_tm if any(overlap(r, p) > 0 for p in pred_tm))
    sp = answer.get("signal_peptide")
    return {
        "pfam": pfam_rows,
        "pfam_missed": sorted(set(missed)),
        "tm_reference": len(ref_tm),
        "tm_predicted": len(pred_tm),
        "tm_recovered": recovered,
        "signal_peptide_predicted": sp,
        "signal_peptide_reference": bool(reference.get("signal_peptide")),
        "signal_peptide_agrees": (
            bool(sp) == bool(reference.get("signal_peptide"))
            if isinstance(sp, bool)
            else None
        ),
    }


def check_activity(
    answer: dict[str, Any], sequence: str, reference: dict[str, Any]
) -> dict[str, Any]:
    """Check each catalytic residue the model named against the sequence and UniProt.

    >>> ref = {"active_sites": [{"position": 3, "residue": "C"}], "binding_sites": [5]}
    >>> a = {"catalytic_residues": [{"role": "nucleophile", "residue": "C", "position": 3},
    ...                             {"role": "base", "residue": "H", "position": 4}],
    ...      "substituted_or_missing": [], "catalytically_active": "yes"}
    >>> c = check_activity(a, "MKCAH", ref)
    >>> [(r["position"], r["present_in_sequence"], r["uniprot"]) for r in c["catalytic_residues"]]
    [(3, True, 'ACT_SITE'), (4, False, None)]
    >>> c["uniprot_active_sites_not_named"]
    []
    """
    rows = []
    for r in answer.get("catalytic_residues") or []:
        if not isinstance(r, dict):
            continue
        pos = r.get("position")
        ok = isinstance(pos, int) and 1 <= pos <= len(sequence)
        here = sequence[pos - 1] if ok and isinstance(pos, int) else None
        present = here is not None and here == str(r.get("residue"))
        uni = None
        if ok and any(s["position"] == pos for s in reference.get("active_sites", [])):
            uni = "ACT_SITE"
        elif ok and pos in reference.get("binding_sites", []):
            uni = "BINDING"
        rows.append(
            {
                "role": r.get("role"),
                "residue": r.get("residue"),
                "position": pos,
                "residue_in_sequence": here,
                "present_in_sequence": present,
                "uniprot": uni,
            }
        )
    named = {r["position"] for r in rows}
    return {
        "catalytically_active": answer.get("catalytically_active"),
        "catalytic_residues": rows,
        "substituted_or_missing": [
            dict(r, found_in_sequence=_found_matches(r, sequence))
            for r in answer.get("substituted_or_missing") or []
            if isinstance(r, dict)
        ],
        "uniprot_active_sites_not_named": [
            s["position"]
            for s in reference.get("active_sites", [])
            if s["position"] not in named
        ],
    }


def _found_matches(r: dict[str, Any], sequence: str) -> Optional[bool]:
    """Whether the residue a model says it found is at that position (None if no position).

    >>> _found_matches({"found": "N", "position": 2}, "MNK"), _found_matches({"found": "A", "position": None}, "MNK")
    (True, None)
    """
    pos = r.get("position")
    if not isinstance(pos, int) or not 1 <= pos <= len(sequence):
        return None
    return sequence[pos - 1] == str(r.get("found"))


def reports_position(answer: dict[str, Any], position: int) -> bool:
    """Whether an activity answer lists a residue at ``position`` (within one) as lost.

    >>> reports_position({"substituted_or_missing": [{"position": 125}]}, 124)
    True
    """
    return any(
        isinstance(r, dict)
        and isinstance(r.get("position"), int)
        and abs(r["position"] - position) <= 1
        for r in answer.get("substituted_or_missing") or []
    )


def probe_verdict(
    wild_type: Optional[str],
    mutant: Optional[str],
    decoy: Optional[str],
    mutant_reports: bool,
    decoy_reports: bool,
) -> str:
    """Summarise the probe as the fs2f decoy control reads it.

    >>> probe_verdict("yes", "no", "yes", True, False)
    'TRACKS_CATALYTIC_RESIDUE'
    >>> probe_verdict("yes", "no", "no", True, True)
    'REJECTS_ANY_CHANGE'
    >>> probe_verdict("yes", "yes", "yes", False, False)
    'INSENSITIVE'
    """
    if wild_type != "yes":
        return "WILD_TYPE_NOT_CALLED_ACTIVE"
    if mutant is None or decoy is None:
        return "INCOMPLETE"
    if decoy != "yes" or decoy_reports:
        return "REJECTS_ANY_CHANGE"
    if mutant == "no" or mutant_reports:
        return "TRACKS_CATALYTIC_RESIDUE"
    return "INSENSITIVE"
