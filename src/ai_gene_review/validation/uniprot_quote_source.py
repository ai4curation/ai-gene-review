"""Checks on *what kind* of UniProt statement a supporting_text quotes.

``local_source_text`` checks that a quote from a ``-uniprot.txt`` file is
verbatim. This module asks what the quoted statement is, because a UniProt
record mixes evidence with restated annotation:

* Kinetics, binding and active sites, and curated free text tied to a
  publication are evidence of a different kind from a GO annotation, and are
  good support.
* Protein names, keywords, database cross-references (including the record's
  own GO lines) and family-membership notes restate a classification. Quoting
  them supports an annotation with another form of the same claim.
* Statements whose only evidence is an ARBA rule are machine output. Quoting
  them as support for anything, ARBA annotations above all, is circular.

Two checks follow, both reported as warnings:

``uniprot_quote_arba_sourced``
    The quoted statement's evidence names ARBA, and nothing else supports it:
    every other source is automatic (``ECO:0000256``, ``ECO:0000259``,
    ``ECO:0000313``, ``ECO:0007...``, or ``IEA:`` on a GO cross-reference) and
    is not one of UniProt's curated rule systems (``CURATED_RULES``).
``uniprot_quote_restating_field``
    The quote comes from a field listed in ``RESTATING_FIELDS`` or a comment
    topic listed in ``RESTATING_CC_TOPICS``.

A quote that occurs in several places is flagged only when every occurrence
would be flagged, so a phrase that is also in an experimentally supported
comment is not reported. Quotes that cannot be located are left to the
verbatim check.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    _validator,
    iter_local_quotes,
    resolve_local_source,
)
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

ARBA_CHECK = "uniprot_quote_arba_sourced"
FIELD_CHECK = "uniprot_quote_restating_field"

#: Line codes whose content restates identity or classification rather than
#: giving evidence: identifiers, names, gene names, taxonomy, keywords,
#: database cross-references and the sequence.
RESTATING_FIELDS = frozenset(
    {"ID", "AC", "DT", "DE", "GN", "OS", "OG", "OC", "OX", "OH", "KW", "DR", "PE", "SQ"}
)
#: Comment topics that restate classification ("Belongs to the X family").
RESTATING_CC_TOPICS = frozenset({"SIMILARITY"})

FIELD_LABELS = {
    "DE": "protein name or EC number", "KW": "keyword", "DR": "database cross-reference",
    "GN": "gene name", "OS": "organism", "OC": "taxonomy", "OX": "taxonomy",
    "ID": "entry identifier", "AC": "accession", "DT": "entry date", "PE": "protein existence",
    "SQ": "sequence", "OG": "organelle", "OH": "host",
}

#: Evidence prefixes that mark machine-generated assertions.
AUTOMATIC_EVIDENCE = ("ECO:0000256", "ECO:0000259", "ECO:0000313", "ECO:0007", "IEA:")
#: UniProt rule systems written by curators (UniRule and its components). A
#: statement these also support is not ARBA output alone.
CURATED_RULES = ("RuleBase", "HAMAP", "PIRNR", "PIRSR", "NCBIfam", "PROSITE-ProRule", "SAM:")

_BRACE = re.compile(r"(?:Evidence=)?\{(ECO:[^{}]*)\}")
#: Evidence tokens left over when a quote cuts through a brace.
_STRAY_EVIDENCE = re.compile(r"(?:Evidence=)?\{?ECO:\d{7}(?:\|[^\s,;}]*)?[,;}]?|[{}]")
_FT_EVIDENCE = re.compile(r'/evidence="([^"]*)"')
_REFERENCE_CODES = frozenset({"RN", "RP", "RC", "RX", "RG", "RA", "RT", "RL"})


@dataclass(frozen=True)
class Statement:
    """One evidence-bearing unit of a UniProt record.

    ``field`` is the line code (``CC``, ``DE``, ``FT`` ...; ``REF`` for a
    citation block), ``topic`` the comment topic, feature key or
    cross-referenced database, and ``evidence`` the evidence strings attached
    to the statement.
    """

    field: str
    topic: str
    text: str
    evidence: Tuple[str, ...]

    @property
    def is_arba(self) -> bool:
        """True when ARBA is a source and nothing else supports the statement.

        >>> Statement("CC", "FUNCTION", "x", ("ECO:0000256|ARBA:ARBA00003800",)).is_arba
        True
        >>> Statement("DR", "GO", "x", ("IEA:UniProtKB-ARBA",)).is_arba
        True
        >>> Statement("DE", "", "x", ("ECO:0000256|ARBA:ARBA1", "ECO:0000313|EMBL:AAN1.1")).is_arba
        True

        A curated UniProt rule or an experimental source also supports these:

        >>> Statement("KW", "", "x", ("ECO:0000256|ARBA:ARBA00023002", "ECO:0000256|RuleBase:RU003719")).is_arba
        False
        >>> Statement("CC", "FUNCTION", "x", ("ECO:0000256|ARBA:ARBA00003800", "ECO:0000269|PubMed:1")).is_arba
        False
        """
        arba = [e for e in self.evidence if "ARBA" in e]
        others = [e for e in self.evidence if "ARBA" not in e]
        return bool(arba) and not any(_independent(e) for e in others)

    @property
    def is_restating(self) -> bool:
        """True for fields and comment topics that restate classification.

        >>> Statement("DE", "", "RecName: Full=X", ()).is_restating
        True
        >>> Statement("CC", "SIMILARITY", "Belongs to the X family", ()).is_restating
        True
        >>> Statement("CC", "BIOPHYSICOCHEMICAL PROPERTIES", "KM=2 uM", ()).is_restating
        False
        """
        return self.field in RESTATING_FIELDS or (
            self.field == "CC" and self.topic in RESTATING_CC_TOPICS
        )


def _independent(evidence: str) -> bool:
    """True for evidence that is not machine output, or comes from a curated rule.

    >>> _independent("ECO:0000269|PubMed:1"), _independent("ECO:0000256|HAMAP-Rule:MF_1")
    (True, True)
    >>> _independent("ECO:0000313|EMBL:AAN1.1"), _independent("ECO:0000259|Pfam:PF1")
    (False, False)
    """
    if not evidence.startswith(AUTOMATIC_EVIDENCE):
        return True
    return any(rule in evidence.replace(" ", "") for rule in CURATED_RULES)


def _split_evidence(text: str) -> Tuple[str, ...]:
    return tuple(e.strip() for e in text.split(",") if e.strip())


def _chunk(field: str, topic: str, text: str) -> List[Statement]:
    """Split a block into statements, each ending at its evidence brace.

    >>> [(s.text, s.evidence) for s in _chunk("KW", "", "NAD {ECO:1}; Oxidoreductase {ECO:2, ECO:3}.")]
    [('NAD', ('ECO:1',)), ('; Oxidoreductase', ('ECO:2', 'ECO:3'))]
    """
    out: List[Statement] = []
    prev = 0
    for m in _BRACE.finditer(text):
        piece = text[prev:m.start()].strip()
        if piece:
            out.append(Statement(field, topic, piece, _split_evidence(m.group(1))))
        prev = m.end()
    rest = text[prev:].strip()
    if re.search(r"\w", rest):
        out.append(Statement(field, topic, rest, ()))
    return out


def parse_uniprot_statements(raw: str) -> List[Statement]:
    """Parse a UniProt flat file into statements with their evidence.

    >>> flat = (
    ...     "DE   RecName: Full=Kinase {ECO:0000256|ARBA:ARBA1};\\n"
    ...     "CC   -!- FUNCTION: Binds DNA. {ECO:0000269|PubMed:1}.\\n"
    ...     "DR   GO; GO:0003677; F:DNA binding; IEA:UniProtKB-ARBA.\\n"
    ...     "FT   BINDING         10\\n"
    ...     'FT                   /evidence="ECO:0000269|PubMed:2"\\n'
    ... )
    >>> [(s.field, s.topic, s.evidence) for s in parse_uniprot_statements(flat)]
    [('DE', '', ('ECO:0000256|ARBA:ARBA1',)), ('CC', 'FUNCTION', ('ECO:0000269|PubMed:1',)), ('DR', 'GO', ('IEA:UniProtKB-ARBA',)), ('FT', 'BINDING', ('ECO:0000269|PubMed:2',))]
    """
    blocks: List[Tuple[str, str, List[str]]] = []

    def start(field: str, topic: str, body: str) -> None:
        blocks.append((field, topic, [body]))

    for line in raw.splitlines():
        if line.startswith("//"):
            continue
        code, body = line[:2], line[5:].strip()
        if code == "  ":
            code = "SQ"
        if code == "CC":
            if body.startswith("-!-"):
                topic = body[3:].split(":", 1)[0].strip()
                start("CC", topic, body)
            elif body.startswith("---"):
                start("CC", "COPYRIGHT", body)
            elif blocks and blocks[-1][0] == "CC":
                blocks[-1][2].append(body)
            else:
                start("CC", "", body)
        elif code == "FT":
            if line[5:6] != " ":
                start("FT", line[5:21].strip(), line[21:].strip())
            elif blocks and blocks[-1][0] == "FT":
                blocks[-1][2].append(body)
        elif code == "DR":
            start("DR", body.split(";", 1)[0].strip(), body)
        elif code in _REFERENCE_CODES:
            if code == "RN" or not blocks or blocks[-1][0] != "REF":
                start("REF", "", body)
            else:
                blocks[-1][2].append(body)
        elif blocks and blocks[-1][0] == code:
            blocks[-1][2].append(body)
        else:
            start(code, "", body)

    statements: List[Statement] = []
    for field, topic, lines in blocks:
        text = " ".join(lines)
        if field == "FT":
            evidence = tuple(e for m in _FT_EVIDENCE.finditer(text) for e in _split_evidence(m.group(1)))
            statements.append(Statement(field, topic, text, evidence))
        elif field == "DR" and topic == "GO":
            source = text.rstrip(".").rsplit(";", 1)[-1].strip()
            statements.append(Statement(field, topic, text, (source,)))
        elif field in ("DR", "REF", "SQ"):
            statements.append(Statement(field, topic, text, ()))
        else:
            statements.extend(_chunk(field, topic, text))
    return statements


@lru_cache(maxsize=256)
def _indexed(path: Path, mtime_ns: int, size: int) -> Tuple[Tuple[Statement, ...], str, Tuple[int, ...]]:
    """Statements of *path*, their normalised concatenation, and each one's start offset."""
    statements = tuple(parse_uniprot_statements(path.read_text(encoding="utf-8")))
    normalize = _validator().normalize_text
    starts: List[int] = []
    pieces: List[str] = []
    offset = 0
    for s in statements:
        piece = normalize(s.text)
        starts.append(offset)
        pieces.append(piece)
        offset += len(piece) + 1
    return statements, " ".join(pieces), tuple(starts)


def _occurrences(part: str, statements, text: str, starts) -> List[List[Statement]]:
    """Every whole-word place *part* occurs, as the list of statements each occurrence spans.

    Normalised text is space-separated words, so padding both sides with a
    space keeps "nad" from matching inside "canadensis".
    """
    padded, needle = f" {text} ", f" {part} "
    ends = list(starts[1:]) + [len(text) + 1]
    found = []
    i = padded.find(needle)
    while i >= 0:
        # padded[i] is the space before the match, so the match starts at text[i]
        end = i + len(part)
        found.append([s for s, a, b in zip(statements, starts, ends) if a < end and b - 1 > i])
        i = padded.find(needle, i + 1)
    return found


def _quote_parts(quote: str) -> List[str]:
    """Normalised ``...``-separated parts of a quote, without evidence tags.

    >>> _quote_parts("Oxidoreductase {ECO:0000256|ARBA:ARBA00023002, ... NAD {ECO:0000256|ARBA:ARBA1};")
    ['oxidoreductase', 'nad']
    """
    validator = _validator()
    stripped = _STRAY_EVIDENCE.sub(" ", _BRACE.sub(" ", quote))
    return [p for p in (validator.normalize_text(x) for x in validator._split_query(stripped)) if p]


def _index(path: Path):
    stat = path.stat()
    return _indexed(path, stat.st_mtime_ns, stat.st_size)


def locate_quote(quote: str, path: Path) -> List[Statement]:
    """Statements spanned by the first occurrence of each part of *quote*; [] if not located."""
    statements, text, starts = _index(path)
    located: List[Statement] = []
    for part in _quote_parts(quote):
        occ = _occurrences(part, statements, text, starts)
        if not occ:
            return []
        located.extend(s for s in occ[0] if s not in located)
    return located


def classify_quote(quote: str, path: Path) -> Optional[Tuple[bool, bool, List[Statement]]]:
    """``(arba_sourced, restating, statements)`` for a quote, or None if not located.

    A flag holds only if it holds for every occurrence of every part.
    """
    statements, text, starts = _index(path)
    parts = _quote_parts(quote)
    if not parts:
        return None
    arba = restating = True
    first: List[Statement] = []
    for part in parts:
        occ = _occurrences(part, statements, text, starts)
        if not occ:
            return None
        first.extend(s for s in occ[0] if s not in first)
        arba &= all(all(s.is_arba for s in o) for o in occ)
        restating &= all(all(s.is_restating for s in o) for o in occ)
    return arba, restating, first


@dataclass(frozen=True)
class QuoteFinding:
    """A flagged UniProt quote."""

    path: str
    reference_id: str
    check_type: str
    statements: Tuple[Statement, ...]


def quote_source_findings(data: Any, project_root: Path = PROJECT_ROOT) -> List[QuoteFinding]:
    """Flagged UniProt quotes in a review document."""
    findings: List[QuoteFinding] = []
    for path, reference_id, quote in iter_local_quotes(data):
        source = resolve_local_source(reference_id, project_root)
        if source is None or not source.name.endswith("-uniprot.txt"):
            continue
        result = classify_quote(quote, source)
        if result is None:
            continue
        arba, restating, statements = result
        if arba:
            findings.append(QuoteFinding(path, reference_id, ARBA_CHECK, tuple(statements)))
        if restating:
            findings.append(QuoteFinding(path, reference_id, FIELD_CHECK, tuple(statements)))
    return findings


def _describe(statements: Tuple[Statement, ...]) -> str:
    labels: Dict[str, None] = {}
    for s in statements:
        if s.field == "CC":
            labels[f"comment ({s.topic})"] = None
        elif s.field == "DR":
            labels[f"{FIELD_LABELS['DR']} ({s.topic})"] = None
        else:
            labels[FIELD_LABELS.get(s.field, s.field)] = None
    return ", ".join(labels)


def validate_uniprot_quote_sources(
    data: Any, report: ValidationReport, project_root: Path = PROJECT_ROOT
) -> None:
    """Warn on UniProt quotes that are ARBA output or restate classification."""
    for f in quote_source_findings(data, project_root):
        where = _describe(f.statements)
        if f.check_type == ARBA_CHECK:
            sources = sorted({e for s in f.statements for e in s.evidence if "ARBA" in e})
            message = (
                f"Supporting text quotes a UniProt {where} whose only evidence is an ARBA rule "
                f"({', '.join(sources)}); ARBA output is not independent evidence"
            )
            suggestion = (
                "Cite an experimental or curated statement, a publication, or your own "
                "analysis instead of rule-generated UniProt text"
            )
        else:
            message = (
                f"Supporting text quotes a UniProt {where}, which restates a classification "
                "rather than giving evidence for it"
            )
            suggestion = (
                "Quote evidence of a different kind: kinetics, binding or active sites, or "
                "curated free text tied to a publication"
            )
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f.path,
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=f.check_type,
        )
