"""Receipt checks for rule reviews (``rules/**/<ID>-review.yaml``).

A rule review ends in a verdict on somebody else's annotation rule. The schema
check only says the file is well formed; these checks ask whether the verdict
comes with *receipts*: facts in fields a program can test. They were written
after an audit of 78 ARBA reviews (2026-11) found the same reasoning errors
again and again, almost all of them detectable from the file alone:

- a verdict on a rule whose condition sets were never recorded;
- an InterPro or GO identifier given the name of a different entry;
- the number of condition sets (or this repository's own analysis cap of 12)
  offered as evidence that the annotation is false;
- ``literature_support: CONTRADICTED`` backed only by the review's own notes;
- DEPRECATE with no protein shown to be wrongly annotated;
- a "false positive" that already carries the term on experimental evidence.

Offline checks need no network. ``--online`` adds two checks against UniProt and
QuickGO: that no alleged false positive carries an experimental annotation to
the consequent, and that the embedded rule is still the rule UniProt serves.
See ``docs/rule_review_receipts.md``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Set, Tuple

import yaml

from ai_gene_review.validation.local_source_text import PROJECT_ROOT
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

CATEGORY = "RuleReviewReceipts"

#: Subtrees that hold quotations or machine output, not the reviewer's claims.
_NOT_PROSE_KEYS = {
    "corrections",
    "supporting_text",
    "entries",
    "pairwise_overlap",
    "references",
    "interpro2go_redundancy",
}

_ID_RE = re.compile(r"\b(IPR\d{6}|GO:\d{7})\b")
_NAME_AFTER_ID = re.compile(r"\b(IPR\d{6}|GO:\d{7})\s*\(([^()]{3,140})\)")
_NAME_BEFORE_ID = re.compile(r"([A-Za-z0-9][^()\n.;:]{2,90}?)\s*\((IPR\d{6}|GO:\d{7})\)")

_SIZE_AS_EVIDENCE = re.compile(
    r"(?:limit|threshold|maximum|max|cap)\s+of\s+(?:12|20|30|50)\b"
    r"|\b12[- ]condition[- ]set"
    r"|>\s*12\s+condition"
    r"|recommended\s+(?:maximum|limit|threshold)"
    r"|analysis\s+(?:threshold|limit)s?"
    r"|exceed\w*\s+(?:the\s+|our\s+)?(?:manageable|established|recommended|analysis)",
    re.IGNORECASE,
)

_REFERENCE_PREFIXES = (
    "PMID:",
    "PMC:",
    "PMCID:",
    "DOI:",
    "doi:",
    "file:",
    "GO_REF:",
    "Reactome:",
    "UniProtKB:",
    "InterPro:",
    "GO:",
    "RHEA:",
    "https://",
    "http://",
    "url:",
)
_LITERATURE_PREFIXES = ("PMID:", "PMC:", "PMCID:", "DOI:", "doi:", "Reactome:", "GO_REF:")

_ACCESSION_RE = re.compile(
    r"^(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})(?:-\d+)?$"
)

_STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "type", "like", "domain",
    "domains", "family", "families", "superfamily", "protein", "proteins", "site",
    "conserved", "terminal", "activity", "process", "containing", "such", "are",
    "its", "both", "all", "any", "not", "into", "via", "class", "related",
}

NEGATIVE_ASSESSMENTS = {"INCORRECT", "PARTIALLY_CORRECT"}

#: Actions that fault the rule. Naming the analysis cap is only an error in
#: support of one of these; saying "12 of 343 sets were read, so UNDECIDED" is right.
_VERDICTS_AGAINST = {"DEPRECATE", "MODIFY", "SPLIT", "MERGE"}


# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------


@lru_cache(maxsize=4)
def load_labels(labels_file: Optional[Path] = None) -> Dict[str, Dict[str, str]]:
    """Official labels from the committed cache ``rules/_labels.json``.

    >>> labels = load_labels()
    >>> labels["interpro"]["IPR000999"]
    'Ribonuclease III domain'
    """
    path = labels_file or PROJECT_ROOT / "rules" / "_labels.json"
    if not path.exists():
        return {"interpro": {}, "go": {}, "funfam": {}}
    data = json.loads(path.read_text())
    return {
        "interpro": data.get("interpro_labels", {}),
        "go": data.get("go_labels", {}),
        "funfam": data.get("funfam_labels", {}),
    }


def _norm(text: str) -> str:
    """Case- and punctuation-insensitive form of a label.

    >>> _norm("Zinc finger,  CCCH-type")
    'zinc finger ccch type'
    >>> _norm("obsolete amide catabolic process")
    'amide catabolic process'
    """
    words = re.findall(r"[a-z0-9]+", text.lower())
    return " ".join(words[1:] if words[:1] == ["obsolete"] else words)


def _tokens(text: str) -> Set[str]:
    """Content words of a phrase, lower-cased, with a plural ``s`` removed.

    >>> sorted(_tokens("Ribonuclease III domain"))
    ['iii', 'ribonuclease']
    >>> sorted(_tokens("protein kinases"))
    ['kinase']
    """
    return {
        word[:-1] if word.endswith("s") and len(word) > 4 else word
        for word in re.findall(r"[a-z0-9]+", text.lower())
        if len(word) > 2 and word not in _STOPWORDS
    }


def labels_agree(stated: str, official: str) -> bool:
    """Whether a name written beside an identifier fits the official label.

    The stated name may be a shortening or a paraphrase, so the test is that it
    shares content words with the official label, not that it is identical.

    >>> labels_agree("ribonucleoside-diphosphate reductase", "Ribonuclease III domain")
    False
    >>> labels_agree("the RNase III domain", "Ribonuclease III domain")
    True
    >>> labels_agree("negative regulation of gene expression", "negative regulation of gene expression")
    True
    >>> labels_agree("kinases", "Zinc finger, CCCH-type")
    False
    """
    if _norm(stated) == _norm(official) or _norm(official) in _norm(stated):
        return True
    stated_tokens, official_tokens = _tokens(stated), _tokens(official)
    if not stated_tokens or not official_tokens:
        return True  # nothing to compare; do not guess
    return bool(stated_tokens & official_tokens)


_NOT_A_NAME = re.compile(
    r"[=%|;/]|\.(?:tsv|txt|ya?ml|md|json|py)\b|\b(?:jaccard|containment|overlap|subset|proteins?\b.*\d|quickgo|ipr2go|interpro2go|uniprotkb|quer(?:y|ies))\b"
    r"|^(?:or|for|a|an|the|its|see|already|as|in|cs\d*|iea|ida|imp)\b",
    re.IGNORECASE,
)


def looks_like_a_name(text: str) -> bool:
    """Whether a parenthesis after an identifier is meant as the entry's name.

    Statistics, cross-references and bare abbreviations are not names, and
    comparing them with the official label would only raise false alarms.

    >>> looks_like_a_name("N-acetylglucosaminyltransferase activity")
    True
    >>> looks_like_a_name("100% containment")
    False
    >>> looks_like_a_name("or GO:0036092")
    False
    >>> looks_like_a_name("TLC domain")
    False
    >>> looks_like_a_name("rule_redundancy.tsv")
    False
    """
    if _NOT_A_NAME.search(text.strip()):
        return False
    return any(len(word) >= 6 for word in _tokens(text))


_SET_REFERENCE = re.compile(
    r"\b(?:condition\s+sets?|sets?|CS)\s*((?:\d+(?!\d))(?:\s*(?:,|and|or|to|-)\s*\d+(?!\d))*)(?!\s*(?:of|condition|sets?|entries|proteins|%))",
    re.IGNORECASE,
)


def cited_set_numbers(text: str) -> Set[int]:
    """Condition-set numbers a sentence refers to.

    >>> sorted(cited_set_numbers("relevant to condition sets 1, 8 and 21"))
    [1, 8, 21]
    >>> sorted(cited_set_numbers("CS18 and set 37 are sound; sets 1 to 7 too"))
    [1, 7, 18, 37]
    >>> cited_set_numbers("12 of 343 sets were read")
    set()
    >>> cited_set_numbers("matches across the screened sets 46,549")
    set()
    >>> cited_set_numbers("set 900 matches 3 entries")
    {900}
    >>> cited_set_numbers("in sets 40 entries were reviewed")
    set()
    """
    found: Set[int] = set()
    # "46,549" is a count written with a thousands separator, not sets 46 and 549.
    text = re.sub(r"\b\d{1,3}(?:,\d{3})+\b", "#", text)
    for match in _SET_REFERENCE.finditer(text):
        found.update(int(number) for number in re.findall(r"\d+", match.group(1)))
    return found


def _official_label(identifier: str, labels: Dict[str, Dict[str, str]]) -> Optional[str]:
    if identifier.startswith("IPR"):
        return labels["interpro"].get(identifier)
    if identifier.startswith("GO:"):
        return labels["go"].get(identifier)
    return labels["funfam"].get(identifier)


@lru_cache(maxsize=2)
def _redundancy_table(path: Optional[Path] = None) -> Dict[str, Dict[str, str]]:
    """Rows of ``projects/ARBA_REVIEW/rule_redundancy.tsv`` keyed by rule id."""
    table = path or PROJECT_ROOT / "projects" / "ARBA_REVIEW" / "rule_redundancy.tsv"
    if not table.exists():
        return {}
    lines = table.read_text().splitlines()
    header = lines[0].split("\t")
    return {cells[0]: dict(zip(header, cells)) for cells in (line.split("\t") for line in lines[1:]) if cells and cells[0]}


def redundancy_row(rule_id: str) -> Optional[Dict[str, str]]:
    """The redundancy measurements for one rule, if the table has it.

    >>> redundancy_row("ARBA00026480")["term"]
    'GO:0010605'
    >>> redundancy_row("ARBA99999999") is None
    True
    """
    return _redundancy_table().get(rule_id)


# ---------------------------------------------------------------------------
# Walking the review
# ---------------------------------------------------------------------------


def iter_prose(node: Any, path: str = "") -> Iterator[Tuple[str, str]]:
    """Yield ``(path, text)`` for every string the reviewer wrote as a claim.

    Quotations, machine-generated entries and the ``corrections`` list (which
    quotes withdrawn claims on purpose) are skipped.

    >>> list(iter_prose({"review_summary": "a", "corrections": [{"withdrawn_claim": "b"}]}))
    [('review_summary', 'a')]
    """
    if isinstance(node, dict):
        for key, value in node.items():
            if key in _NOT_PROSE_KEYS:
                continue
            yield from iter_prose(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_prose(value, f"{path}[{index}]")
    elif isinstance(node, str) and path.rsplit(".", 1)[-1].split("[")[0] in {
        "description",
        "review_summary",
        "action_rationale",
        "suggested_modifications",
        "notes",
        "statement",
    }:
        yield path, node


def iter_supported_by(node: Any, path: str = "") -> Iterator[Tuple[str, Dict[str, Any]]]:
    """Yield ``(path, item)`` for every ``supported_by`` entry outside ``corrections``."""
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}.{key}" if path else str(key)
            if key == "supported_by" and isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        yield f"{here}[{index}]", item
            elif key != "corrections":
                yield from iter_supported_by(value, here)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_supported_by(value, f"{path}[{index}]")


def _resolve_file_reference(reference_id: str, project_root: Path) -> Optional[Path]:
    """Path a ``file:`` reference names, or None when nothing is there."""
    relative = reference_id[len("file:") :].strip()
    for base in (project_root, project_root / "genes"):
        candidate = base / relative
        if candidate.exists():
            return candidate
    return None


def _is_own_notes(reference_id: str) -> bool:
    """Whether a reference is reviewer- or AI-written narrative, not a source.

    >>> _is_own_notes("file:rules/arba/ARBA00026480/ARBA00026480-deep-research-manual.md")
    True
    >>> _is_own_notes("file:rules/arba/ARBA00067001/RESULTS.md")
    False
    """
    name = reference_id.rsplit("/", 1)[-1].lower()
    return reference_id.startswith("file:") and bool(
        re.search(r"deep-research|manual|-notes\.md$|analysis[-_]notes|-summary\.md$|recommendations", name)
    )


# ---------------------------------------------------------------------------
# Offline checks
# ---------------------------------------------------------------------------


def check_review(
    data: Dict[str, Any],
    report: ValidationReport,
    project_root: Path = PROJECT_ROOT,
    labels: Optional[Dict[str, Dict[str, str]]] = None,
) -> None:
    """Run every offline receipt check on one parsed review.

    >>> report = ValidationReport(is_valid=True)
    >>> check_review({"id": "ARBA1", "action": "DEPRECATE", "confidence": 0.95,
    ...               "rule": {"rule_id": "ARBA1", "condition_sets": []},
    ...               "review_summary": "343 sets exceeds the analysis threshold of 12."},
    ...              report)
    >>> sorted({issue.check_type for issue in report.issues if issue.is_error()})
    ['deprecate_without_counterexample', 'missing_rule_snapshot', 'size_as_evidence', 'verdict_without_conditions', 'verdict_without_meaning']
    >>> ok = ValidationReport(is_valid=True)
    >>> check_review({"id": "ARBA1", "action": "UNDECIDED",
    ...               "rule": {"rule_id": "ARBA1", "condition_sets": [], "retrieved_date": "2026-11-10"}}, ok)
    >>> ok.issues
    []
    """
    labels = labels or load_labels()
    rule = data.get("rule") or {}
    action = data.get("action")
    condition_sets = rule.get("condition_sets") or []
    withdrawn = bool(rule.get("withdrawn"))
    assessments = data.get("annotation_assessments") or []

    def add(severity: ValidationSeverity, check: str, message: str, path: str, suggestion: Optional[str] = None) -> None:
        report.add_issue(
            severity,
            message,
            path=path,
            suggestion=suggestion,
            validation_category=CATEGORY,
            check_type=check,
        )

    error, warning = ValidationSeverity.ERROR, ValidationSeverity.WARNING

    # 1. A verdict needs the thing it is a verdict on.
    if action and action != "UNDECIDED" and not condition_sets and not (withdrawn and action in {"DEPRECATE", "WITHDRAWN"}):
        add(
            error,
            "verdict_without_conditions",
            f"action is {action} but rule.condition_sets is empty: the review records no condition it examined",
            "rule.condition_sets",
            "Record the condition sets examined (from the fetched rule), or set action to UNDECIDED.",
        )
    total = rule.get("source_condition_set_count")
    if action == "ACCEPT" and isinstance(total, int) and total > len(condition_sets):
        add(
            error,
            "accept_on_partial_examination",
            f"action is ACCEPT but only {len(condition_sets)} of {total} condition sets are recorded",
            "rule.condition_sets",
            "ACCEPT covers the whole rule; record every set or use UNDECIDED and say which sets were sound.",
        )
    decided = bool(action) and action != "UNDECIDED"
    if not rule.get("retrieved_date"):
        add(
            error if decided else warning,
            "missing_rule_snapshot",
            "rule.retrieved_date is not set: the review does not say which version of the rule it describes",
            "rule.retrieved_date",
        )
    if decided and not isinstance(total, int) and not withdrawn:
        add(
            error,
            "missing_rule_snapshot",
            f"action is {action} but rule.source_condition_set_count is not set, so nothing shows how much of "
            "the rule was examined",
            "rule.source_condition_set_count",
            "Record the number of condition sets in the rule as fetched. Leaving a receipt field out is not a pass.",
        )

    # 2. The label is the checksum of the identifier.
    for set_index, condition_set in enumerate(condition_sets):
        for cond_index, condition in enumerate((condition_set or {}).get("conditions") or []):
            value, stated = str(condition.get("value", "")), condition.get("label")
            official = _official_label(value, labels)
            if stated and official and _norm(stated) != _norm(official):
                add(
                    error,
                    "condition_label_mismatch",
                    f"{value} is labelled {stated!r}; its official name is {official!r}",
                    f"rule.condition_sets[{set_index}].conditions[{cond_index}].label",
                    "Copy the label from InterPro or CATH; never write it from memory.",
                )
    for index, annotation in enumerate(rule.get("go_annotations") or []):
        go_id, stated = annotation.get("go_id", ""), annotation.get("go_label")
        official = labels["go"].get(go_id)
        if stated and official and _norm(stated) != _norm(official):
            add(error, "go_label_mismatch", f"{go_id} is labelled {stated!r}; GO calls it {official!r}",
                f"rule.go_annotations[{index}].go_label")

    for path, text in iter_prose(data):
        flat = " ".join(text.split())
        for match in _NAME_AFTER_ID.finditer(flat):
            identifier, stated = match.group(1), match.group(2)
            official = _official_label(identifier, labels)
            if official and looks_like_a_name(stated) and not labels_agree(stated, official):
                add(error, "prose_identifier_label_mismatch",
                    f"{identifier} is described as {stated!r}; its official name is {official!r}", path,
                    "Look the identifier up and correct the name, or correct the identifier.")
        for match in _NAME_BEFORE_ID.finditer(flat):
            stated, identifier = " ".join(match.group(1).split()[-6:]), match.group(2)
            official = _official_label(identifier, labels)
            if official and looks_like_a_name(stated) and not labels_agree(stated, official):
                add(warning, "prose_identifier_label_mismatch",
                    f"{identifier} follows the words {stated!r}; its official name is {official!r}", path,
                    "Check the identifier; write it as 'ID (official name)'.")
        # 3. Size is not evidence.
        size = _SIZE_AS_EVIDENCE.search(flat) if action in _VERDICTS_AGAINST else None
        if size:
            add(error, "size_as_evidence",
                f"appeals to a condition-set limit ({size.group(0)!r}); the cap of 12 is this repository's "
                "analysis default, not a property of correct rules", path,
                "Argue from what the sets match. A large rule that was not examined is UNDECIDED.")

    # 4. Sources must exist and must be sources.
    for path, item in iter_supported_by(data):
        reference_id = str(item.get("reference_id") or "")
        if not reference_id.startswith(_REFERENCE_PREFIXES):
            add(error, "unresolvable_reference",
                f"supported_by cites {reference_id!r}, which is not a resolvable reference", path,
                "Cite a PMID, DOI, database record or a file in this repository.")
        elif reference_id.startswith("file:"):
            if _resolve_file_reference(reference_id, project_root) is None:
                add(error, "missing_cited_file", f"supported_by cites {reference_id}, which does not exist", path)
            elif _is_own_notes(reference_id):
                add(warning, "own_notes_as_support",
                    f"supported_by cites {reference_id}: notes and AI research files are not independent sources", path,
                    "Cite the paper or database record the note relies on.")

    # A numbered condition set must exist in the rule the review describes.
    numbers = [cs.get("number") for cs in condition_sets if isinstance((cs or {}).get("number"), int)]
    highest = max([total if isinstance(total, int) else 0, *numbers], default=0)
    if highest:
        statements = [
            (f"references[{r}].findings[{f}].statement", str(finding.get("statement") or ""))
            for r, reference in enumerate(data.get("references") or [])
            if isinstance(reference, dict)
            for f, finding in enumerate(reference.get("findings") or [])
            if isinstance(finding, dict)
        ]
        for path, text in [*iter_prose(data), *statements]:
            for set_number in sorted(cited_set_numbers(text)):
                if set_number > highest:
                    add(error, "condition_set_out_of_range",
                        f"refers to condition set {set_number}, but the rule as recorded has {highest}", path,
                        "The text may describe an earlier version of the rule; re-read it against the recorded sets.")

    literature = data.get("literature_support") or {}
    if literature.get("assessment") in {"STRONG", "MODERATE", "CONTRADICTED"}:
        cited = [str(item.get("reference_id") or "") for item in literature.get("supported_by") or [] if isinstance(item, dict)]
        # A publication or pathway named in the note is a checkable receipt too.
        cited += re.findall(r"PMID:\d+|PubMed:\d+|PMC\d+|R-HSA-\d+|DOI:\S+", str(literature.get("notes") or ""))
        if not any(ref.startswith(_LITERATURE_PREFIXES + ("PMC", "R-HSA-", "PubMed:")) for ref in cited):
            add(error, "literature_verdict_without_literature",
                f"literature_support is {literature.get('assessment')} but the block cites no publication or "
                "curated pathway record in its supported_by or notes", "literature_support",
                "Cite the literature, or remove the block: not having searched is not a finding.")

    # 5. A negative verdict names a protein.
    def has_counterexample(assessment: Dict[str, Any]) -> bool:
        return bool(assessment.get("incorrect_examples")) or assessment.get("consequent_obsolete") is True

    negative = [a for a in assessments if isinstance(a, dict) and a.get("assessment") in NEGATIVE_ASSESSMENTS]
    obsolete = any(isinstance(a, dict) and a.get("consequent_obsolete") is True for a in assessments)
    # A rule whose every set is also matched by a rule for a more specific term emits
    # nothing (UniProt keeps the most specific ARBA term), so it can go on parsimony alone.
    covered = (data.get("biological_meaning") or {}).get("sets_covered_by_more_specific_rule")
    does_no_work = isinstance(covered, int) and isinstance(total, int) and total > 0 and covered >= total
    if (action == "DEPRECATE" and not withdrawn and not obsolete and not does_no_work
            and not any(has_counterexample(a) for a in negative)):
        add(error, "deprecate_without_counterexample",
            "action is DEPRECATE but the review names no wrongly annotated protein (incorrect_examples), no "
            "obsolete consequent (consequent_obsolete: true), and does not show that every condition set is "
            "covered by a rule for a more specific term (biological_meaning.sets_covered_by_more_specific_rule)",
            "annotation_assessments",
            "Show the false positives with accessions, or that the rule emits nothing. A true but general "
            "term whose sets are not all covered is SPLIT or MODIFY.")
    for index, assessment in enumerate(negative):
        if not has_counterexample(assessment):
            add(warning, "negative_assessment_without_example",
                f"assessment {assessment.get('assessment')} has no incorrect_examples",
                f"annotation_assessments[{index}]")
    for index, assessment in enumerate(assessments):
        for key in ("correct_examples", "incorrect_examples", "would_match_examples"):
            for accession in (assessment or {}).get(key) or []:
                if not _ACCESSION_RE.match(str(accession)):
                    add(error, "example_not_an_accession", f"{accession!r} is not a UniProt accession",
                        f"annotation_assessments[{index}].{key}")
    if action in {"MODIFY", "SPLIT", "MERGE"} and not data.get("suggested_modifications"):
        add(error, "modify_without_modification", f"action is {action} but suggested_modifications is empty",
            "suggested_modifications")

    # 6. Confidence is confidence in the verdict.
    confidence = data.get("confidence")
    if action and action not in {"UNDECIDED", "WITHDRAWN"} and not isinstance(confidence, (int, float)):
        add(error, "verdict_without_confidence",
            f"action is {action} but no confidence is stated", "confidence",
            "State how sure you are that the action is right; below 0.5, use UNDECIDED.")
    if action and action != "UNDECIDED" and isinstance(confidence, (int, float)) and confidence < 0.5:
        add(error, "low_confidence_verdict",
            f"action is {action} at confidence {confidence}: a verdict held below 0.5 is UNDECIDED",
            "confidence", "confidence is confidence that the action is right, not confidence in the rule.")

    # 7. Withdrawal is a fact about the rule, not a verdict on it.
    if action == "WITHDRAWN" and not withdrawn:
        add(error, "withdrawn_action_mismatch",
            "action is WITHDRAWN but rule.withdrawn is not true", "action",
            "WITHDRAWN means UniProt no longer serves the rule; record rule.withdrawn and retrieved_date.")
    if action == "DEPRECATE" and withdrawn:
        add(error, "withdrawn_action_mismatch",
            "the rule is withdrawn, so the action is WITHDRAWN, not DEPRECATE", "action",
            "DEPRECATE is for a rule that is still served and should be retired.")

    check_meaning(data, add, labels)


def check_meaning(data: Dict[str, Any], add: Any, labels: Dict[str, Dict[str, str]]) -> None:
    """Checks on the second axis: is the rule a meaningful, parsimonious statement?

    Accuracy (is each annotation true?) is not enough for a verdict. A rule whose
    sets are each true for one umbrella term can still say nothing, so every
    decided verdict states a judgement of meaning, and the judgement names the
    biological units and the terms it rests on.

    >>> issues = []
    >>> def add(severity, check, message, path, suggestion=None):
    ...     issues.append(check)
    >>> check_meaning({"action": "ACCEPT", "rule": {"condition_sets": [{"number": 1}]},
    ...                "biological_meaning": {"assessment": "TRUE_BUT_UNINFORMATIVE"}}, add, load_labels())
    >>> sorted(set(issues))
    ['accept_of_uninformative_rule', 'accept_without_parsimony', 'uninformative_without_units']
    """
    error, warning = ValidationSeverity.ERROR, ValidationSeverity.WARNING
    action = data.get("action")
    rule = data.get("rule") or {}
    meaning = data.get("biological_meaning") or {}
    assessment = meaning.get("assessment")
    units = [u for u in data.get("biological_units") or [] if isinstance(u, dict)]
    parsimony = (data.get("parsimony") or {}).get("assessment")

    if action in {"ACCEPT", "MODIFY", "SPLIT", "MERGE", "DEPRECATE"} and not assessment:
        add(error, "verdict_without_meaning",
            f"action is {action} but biological_meaning is not recorded: the review judges whether "
            "annotations are true, not whether the rule is a meaningful statement", "biological_meaning",
            "Group the condition sets into biological units, find each unit's most informative term, "
            "and record the judgement. See docs/rule_review_receipts.md.")
    if action in {"ACCEPT", "SPLIT"} and assessment == "NOT_ASSESSED":
        add(error, "verdict_without_meaning",
            f"action is {action} but biological_meaning is NOT_ASSESSED", "biological_meaning.assessment",
            "ACCEPT and SPLIT are judgements of meaning; without one the action is UNDECIDED or MODIFY.")
    if action == "ACCEPT" and assessment in {"TRUE_BUT_UNINFORMATIVE", "HETEROGENEOUS"}:
        add(error, "accept_of_uninformative_rule",
            f"action is ACCEPT but biological_meaning is {assessment}", "action",
            "A true but uninformative rule is SPLIT toward the specific terms; a heterogeneous one is SPLIT or MODIFY.")
    if action == "ACCEPT" and parsimony not in {"PARSIMONIOUS", "ACCEPTABLE"}:
        add(error, "accept_without_parsimony",
            f"action is ACCEPT but parsimony is {parsimony or 'not recorded'}", "parsimony",
            "ACCEPT needs a parsimony judgement of PARSIMONIOUS or ACCEPTABLE, with the numbers in notes.")

    with_term = [u for u in units if u.get("most_informative_term_id")]
    if action == "SPLIT" and len(with_term) < 2:
        add(error, "split_without_units",
            f"action is SPLIT but {len(with_term)} biological unit(s) carry a term to split toward",
            "biological_units", "Name at least two units, each with its most informative term.")
    relations = {u.get("term_relation") for u in units}
    if assessment == "TRUE_BUT_UNINFORMATIVE" and "DESCENDANT_OF_CONSEQUENT" not in relations:
        add(error, "uninformative_without_units",
            "biological_meaning is TRUE_BUT_UNINFORMATIVE but no biological unit carries a more specific "
            "descendant term", "biological_units",
            "Show the more specific term on at least one unit, with the curated annotation behind it.")
    if assessment == "HETEROGENEOUS" and "OUTSIDE_CONSEQUENT" not in relations and len(units) < 2:
        add(error, "heterogeneous_without_units",
            "biological_meaning is HETEROGENEOUS but the units that differ are not named", "biological_units")
    if assessment == "COHERENT" and not units:
        add(warning, "coherent_without_units",
            "biological_meaning is COHERENT but no biological unit is named", "biological_units")

    numbers = [cs.get("number") for cs in rule.get("condition_sets") or [] if isinstance((cs or {}).get("number"), int)]
    total = rule.get("source_condition_set_count")
    highest = max([total if isinstance(total, int) else 0, *numbers], default=0)
    for index, unit in enumerate(units):
        path = f"biological_units[{index}]"
        term_id, stated = unit.get("most_informative_term_id"), unit.get("most_informative_term_label")
        if term_id:
            official = labels["go"].get(str(term_id))
            if not stated:
                add(error, "unit_term_without_label", f"{term_id} has no label", f"{path}.most_informative_term_label")
            elif official and _norm(str(stated)) != _norm(official):
                add(error, "unit_term_label_mismatch",
                    f"{term_id} is labelled {stated!r}; GO calls it {official!r}", f"{path}.most_informative_term_label")
            if not unit.get("evidence") and unit.get("term_relation") != "NONE_KNOWN":
                add(error, "unit_term_without_evidence",
                    f"unit {unit.get('name')!r} names {term_id} with no curated annotation as evidence", f"{path}.evidence",
                    "Give an accession, GO id, evidence code and reference.")
        for number in unit.get("condition_sets") or []:
            if highest and isinstance(number, int) and number > highest:
                add(error, "condition_set_out_of_range",
                    f"unit {unit.get('name')!r} refers to condition set {number}, but the rule as recorded has {highest}",
                    f"{path}.condition_sets")
        for accession in unit.get("example_proteins") or []:
            if not _ACCESSION_RE.match(str(accession)):
                add(error, "example_not_an_accession", f"{accession!r} is not a UniProt accession",
                    f"{path}.example_proteins")

    # The generality and coverage figures are copied from the project's redundancy table; check the copy.
    go_ids = [a.get("go_id") for a in rule.get("go_annotations") or [] if a.get("go_id")]
    row = redundancy_row(str(rule.get("rule_id") or data.get("id") or ""))
    if row and len(go_ids) == 1 and row["term"] == go_ids[0]:
        for field, column in (("consequent_descendant_count", "go_descendants"),
                              ("sets_covered_by_more_specific_rule", "covered_sets")):
            stated_value = meaning.get(field)
            if isinstance(stated_value, int) and stated_value != int(row[column]):
                add(error, "redundancy_receipt_mismatch",
                    f"biological_meaning.{field} is {stated_value}; rule_redundancy.tsv gives {row[column]}",
                    f"biological_meaning.{field}")


# ---------------------------------------------------------------------------
# Online checks
# ---------------------------------------------------------------------------


def _get_json(url: str, timeout: int = 30, attempts: int = 5) -> Any:
    """GET a JSON document, waiting and retrying when the server asks us to slow down."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed https hosts
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in (408, 429, 500, 502, 503, 504) or attempt == attempts - 1:
                raise
            time.sleep(2 ** (attempt + 1))
        except TimeoutError:
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise AssertionError("unreachable")


def experimental_annotations(accession: str, go_id: str) -> List[str]:
    """Experimental GOA rows putting ``accession`` on ``go_id`` or a descendant (network)."""
    query = urllib.parse.urlencode(
        {
            "geneProductId": accession,
            "goId": go_id,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "evidenceCode": "ECO:0000269",
            "evidenceCodeUsage": "descendants",
            "limit": 10,
        }
    )
    results = _get_json(f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?{query}").get("results", [])
    return [f"{row['goId']} {row['goEvidence']} {row['reference']} ({row['assignedBy']})" for row in results]


def go_ancestors(go_id: str) -> Set[str]:
    """The is_a/part_of ancestors of a GO term, from QuickGO (the term itself excluded)."""
    data = _get_json(
        "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
        + urllib.parse.quote(go_id)
        + "/ancestors?relations=is_a,part_of"
    )
    results = data.get("results") or []
    if not results:
        raise ValueError(f"QuickGO does not know {go_id}")
    return set(results[0].get("ancestors") or []) - {go_id}


# term_relation value -> predicate(unit term, consequent, ancestors of the unit term)
_RELATION_HOLDS: Dict[str, Any] = {
    "SAME_AS_CONSEQUENT": lambda term, consequent, ancestors: term == consequent,
    "DESCENDANT_OF_CONSEQUENT": lambda term, consequent, ancestors: term != consequent and consequent in ancestors,
    "OUTSIDE_CONSEQUENT": lambda term, consequent, ancestors: term != consequent and consequent not in ancestors,
}


def check_review_online(data: Dict[str, Any], report: ValidationReport) -> None:
    """Checks that need UniProt and QuickGO; failures to connect are reported, not raised."""

    def add(severity: ValidationSeverity, check: str, message: str, path: str) -> None:
        report.add_issue(severity, message, path=path, validation_category=CATEGORY, check_type=check)

    rule = data.get("rule") or {}
    go_ids = [a.get("go_id") for a in rule.get("go_annotations") or [] if a.get("go_id")]
    for index, assessment in enumerate(data.get("annotation_assessments") or []):
        targets = [assessment["value"]] if str(assessment.get("value", "")).startswith("GO:") else go_ids
        for accession in assessment.get("incorrect_examples") or []:
            for go_id in targets:
                try:
                    rows = experimental_annotations(str(accession), go_id)
                except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                    add(ValidationSeverity.WARNING, "online_check_failed", f"QuickGO lookup failed: {exc}",
                        f"annotation_assessments[{index}]")
                    continue
                if rows:
                    add(ValidationSeverity.ERROR, "false_positive_has_experimental_annotation",
                        f"{accession} is listed as wrongly annotated with {go_id} but carries it, or a descendant, "
                        f"on experimental evidence: {'; '.join(rows[:3])}",
                        f"annotation_assessments[{index}].incorrect_examples")

    for index, assessment in enumerate(data.get("annotation_assessments") or []):
        value = str(assessment.get("value", ""))
        if assessment.get("consequent_obsolete") is True and value.startswith("GO:"):
            try:
                terms = _get_json(
                    "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + urllib.parse.quote(value)
                ).get("results") or []
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                add(ValidationSeverity.WARNING, "online_check_failed", f"QuickGO lookup failed: {exc}",
                    f"annotation_assessments[{index}]")
                continue
            if terms and not terms[0].get("isObsolete"):
                add(ValidationSeverity.ERROR, "consequent_not_obsolete",
                    f"{value} is marked consequent_obsolete but QuickGO serves it as a current term",
                    f"annotation_assessments[{index}].consequent_obsolete")

    # A unit's stated relation to the consequent is a claim about the ontology; check it.
    if len(go_ids) == 1:
        consequent = go_ids[0]
        for index, unit in enumerate(data.get("biological_units") or []):
            term_id, relation = unit.get("most_informative_term_id"), unit.get("term_relation")
            if not term_id or relation not in _RELATION_HOLDS:
                continue
            try:
                ancestors = go_ancestors(str(term_id))
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                add(ValidationSeverity.WARNING, "online_check_failed", f"QuickGO lookup failed: {exc}",
                    f"biological_units[{index}]")
                continue
            if not _RELATION_HOLDS[relation](str(term_id), consequent, ancestors):
                add(ValidationSeverity.ERROR, "unit_term_relation_mismatch",
                    f"unit {unit.get('name')!r}: {term_id} is stated to be {relation} ({consequent}), "
                    "which the ontology does not bear out", f"biological_units[{index}].term_relation")

    rule_id = str(rule.get("rule_id") or "")
    if rule_id.startswith("ARBA"):
        try:
            live = _get_json(f"https://rest.uniprot.org/arba/{rule_id}")
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                add(ValidationSeverity.WARNING, "online_check_failed",
                    f"UniProt lookup failed with HTTP {exc.code}; the rule's state was not checked", "rule")
            elif not rule.get("withdrawn"):
                add(ValidationSeverity.WARNING, "rule_withdrawn_upstream",
                    f"UniProt no longer serves {rule_id}; set rule.withdrawn and re-read the verdict", "rule")
            return
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            add(ValidationSeverity.WARNING, "online_check_failed", f"UniProt lookup failed: {exc}", "rule")
            return
        if rule.get("withdrawn"):
            add(ValidationSeverity.ERROR, "withdrawn_but_served",
                f"rule.withdrawn is true but UniProt serves {rule_id}; a verdict that rests on withdrawal has no basis",
                "rule.withdrawn")
        live_sets = len((live.get("mainRule") or {}).get("conditionSets") or [])
        live_modified = (live.get("information") or {}).get("modifiedDate") or live.get("modifiedDate")
        recorded = rule.get("source_condition_set_count")
        if isinstance(recorded, int) and recorded != live_sets:
            add(ValidationSeverity.WARNING, "stale_rule_snapshot",
                f"the review describes {recorded} condition sets; UniProt now serves {live_sets}"
                + (f" (modified {live_modified})" if live_modified else ""), "rule.source_condition_set_count")


def fetch_official_label(identifier: str) -> Optional[str]:
    """Current official name of an InterPro entry or GO term (network).

    Returns None when the source does not know the identifier.
    """
    try:
        if identifier.startswith("IPR"):
            data = _get_json(f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{identifier}")
            return data["metadata"]["name"]["name"]
        data = _get_json(
            "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + urllib.parse.quote(identifier)
        )
        results = data.get("results") or []
        return results[0]["name"] if results else None
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 410, 204):
            return None
        raise
    except json.JSONDecodeError:
        return None  # InterPro answers 204 with an empty body for a deleted entry


def refresh_labels(files: Sequence[Path], labels_file: Optional[Path] = None) -> Dict[str, Tuple[Optional[str], str]]:
    """Re-fetch cached labels that disagree with a review, or are missing.

    The cache is the reference the label checks compare against, so it has to
    follow InterPro and GO renames. Only identifiers whose recorded label
    differs from the cache (or that the cache lacks) are fetched: either the
    cache is stale, and is updated, or the review is wrong, and still fails.
    Returns ``{id: (old label, new label)}`` for each entry that changed.
    """
    path = labels_file or PROJECT_ROOT / "rules" / "_labels.json"
    cache = json.loads(path.read_text())
    labels = load_labels(labels_file)
    identifiers: Set[str] = set()
    for review in files:
        data = yaml.safe_load(Path(review).read_text()) or {}
        rule = data.get("rule") or {}
        stated = [
            (str(condition.get("value", "")), condition.get("label"))
            for condition_set in rule.get("condition_sets") or []
            for condition in (condition_set or {}).get("conditions") or []
        ]
        stated += [(a.get("go_id", ""), a.get("go_label")) for a in rule.get("go_annotations") or []]
        stated += [
            (str(unit.get("most_informative_term_id") or ""), unit.get("most_informative_term_label"))
            for unit in data.get("biological_units") or []
        ]
        for identifier, label in stated:
            if not _ID_RE.fullmatch(identifier):
                continue
            official = _official_label(identifier, labels)
            if official is None or (label and _norm(label) != _norm(official)):
                identifiers.add(identifier)
    changed: Dict[str, Tuple[Optional[str], str]] = {}
    for identifier in sorted(identifiers):
        section = cache["interpro_labels"] if identifier.startswith("IPR") else cache["go_labels"]
        label = fetch_official_label(identifier)
        if label and section.get(identifier) != label:
            changed[identifier] = (section.get(identifier), label)
            section[identifier] = label
    if changed:
        path.write_text(json.dumps(cache, indent=2))
        load_labels.cache_clear()
    return changed


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------


def validate_rule_review_receipts(
    yaml_file: Path, report: ValidationReport, online: bool = False, project_root: Path = PROJECT_ROOT
) -> None:
    """Add receipt issues for ``yaml_file`` to ``report``."""
    try:
        data = yaml.safe_load(Path(yaml_file).read_text())
    except (OSError, yaml.YAMLError):
        return  # the schema check reports unreadable files
    if not isinstance(data, dict):
        return
    check_review(data, report, project_root=project_root)
    if online:
        check_review_online(data, report)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--all", action="store_true", help="check every rules/**/*-review.yaml")
    parser.add_argument("--online", action="store_true", help="also check against UniProt and QuickGO")
    parser.add_argument("--summary", action="store_true", help="print counts per check instead of every issue")
    parser.add_argument(
        "--refresh-labels",
        action="store_true",
        help="first update rules/_labels.json from InterPro and QuickGO for the ids these reviews use",
    )
    args = parser.parse_args(argv)
    files = sorted((PROJECT_ROOT / "rules").rglob("*-review.yaml")) if args.all else args.files
    if not files:
        parser.error("give review files or --all")
    if args.refresh_labels:
        for identifier, (before, after) in refresh_labels(files).items():
            print(f"label updated: {identifier}: {before!r} -> {after!r}")
    counts: Dict[str, int] = {}
    failed = 0
    for path in files:
        report = ValidationReport(file_path=path, is_valid=True)
        validate_rule_review_receipts(path, report, online=args.online)
        failed += not report.is_valid
        for issue in report.issues:
            counts[f"{issue.severity} {issue.check_type}"] = counts.get(f"{issue.severity} {issue.check_type}", 0) + 1
        if not args.summary and report.issues:
            print(path)
            for issue in report.issues:
                print(f"  {issue}")
    if args.summary:
        for key in sorted(counts):
            print(f"{counts[key]:5d}  {key}")
    print(f"{failed} of {len(files)} review(s) fail receipt checks")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
