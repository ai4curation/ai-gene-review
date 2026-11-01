"""Consistency checks for proposed ontology changes.

A ``proposed_ontology_changes`` entry asks an ontology to change a term that
already exists -- obsolete it, merge it, fix its definition, move it, drop a
mapping. The entry is modelled on KGCL (Knowledge Graph Change Language), so
each ``change_type`` names a KGCL class and the structured slots carry that
class's own fields. The checks here enforce what each kind of change needs in
order to be emittable as KGCL at all, which is also what a term tracker needs
in order to act on it:

- an obsoletion *with* a direct replacement, and a merge, must name the
  surviving term; one *without* must not;
- a change that replaces a value (definition, label, synonym, mapping
  predicate) needs both the old and the new value, and they must differ;
- an edge change needs the other end of the edge and the relation, since
  reparenting a term and adding a ``part_of`` link to the same term are
  different requests;
- nothing may be replaced by itself;
- ``COMPLEX_CHANGE`` and ``OTHER`` carry no KGCL semantics, so the
  justification is all a curator has and a one-liner will not do;
- a report recorded as filed should link the tracker issue it was filed as;
- ``change_dsl``, where given, must agree with the structured slots -- it is
  deliberately redundant so that a disagreement is detectable;
- the review must not ask for a term's obsoletion while ``ACCEPT``-ing that same
  term on an annotation row, which is a straight contradiction.

Severity is WARNING throughout, like the ND and protein-binding policies: these
guide a reviewer rather than block a file.

Note what is *not* checked. Whether the ontology should actually make the change
is a curatorial judgement no rule can settle, and whether ``about_node`` exists
and carries the stated label is the term validator's job, not this module's.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Dict, Iterator, List, Optional, Tuple

#: Change types that must name a surviving/replacing term.
NEEDS_DIRECT_REPLACEMENT = frozenset(
    {"NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT", "NODE_DIRECT_MERGE"}
)

#: Change types that must *not* name a direct replacement (that is their point).
FORBIDS_DIRECT_REPLACEMENT = frozenset({"NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT"})

#: Change types that replace one value with another.
VALUE_CHANGES = frozenset(
    {
        "NODE_TEXT_DEFINITION_CHANGE",
        "NODE_RENAME",
        "MAPPING_PREDICATE_CHANGE",
    }
)

#: Change types that act on an edge, so they need its other end and its relation.
EDGE_CHANGES = frozenset(
    {
        "EDGE_CREATION",
        "EDGE_DELETION",
        "NODE_MOVE",
        "NODE_DEEPENING",
        "NODE_SHALLOWING",
    }
)

#: Change types with no KGCL semantics to lean on, so the prose must carry the case.
PROSE_ONLY = frozenset({"COMPLEX_CHANGE", "OTHER"})

#: Words below which a PROSE_ONLY justification is not an argument.
MIN_JUSTIFICATION_WORDS = 20

#: Report statuses that mean the request reached the ontology.
FILED_STATUSES = frozenset({"REPORTED", "ACKNOWLEDGED", "FIXED", "DECLINED"})


def _term_id(value: Any) -> Optional[str]:
    """The ``id`` of an inlined term, or None.

    >>> _term_id({"id": "GO:1", "label": "x"})
    'GO:1'
    >>> _term_id(None) is None
    True
    """
    if isinstance(value, dict):
        got = value.get("id")
        return str(got) if got else None
    return None


#: change_type -> the KGCL class name its DSL must parse as, for the types that
#: have a DSL form at all. Mirrors the `meaning` bindings in the schema's
#: OntologyChangeTypeEnum.
_KGCL_CLASS: Dict[str, str] = {
    "NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT": "NodeObsoletionWithDirectReplacement",
    "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT": "NodeObsoletion",
    "NODE_RENAME": "NodeRename",
    "NODE_TEXT_DEFINITION_CHANGE": "NodeTextDefinitionChange",
    "NEW_SYNONYM": "NewSynonym",
    "EDGE_CREATION": "EdgeCreation",
    "EDGE_DELETION": "EdgeDeletion",
    "NODE_DEEPENING": "NodeDeepening",
    "NODE_SHALLOWING": "NodeShallowing",
    "NODE_MOVE": "NodeMove",
}

#: Candidate DSL templates per change type. KGCL's grammar (kgcl.lark) has no
#: form for a merge, a mapping change or a mapping removal, so those render no
#: DSL at all rather than a string that looks like KGCL and does not parse.
#: Every string built here is parsed with KGCL's own parser before being
#: returned, so the grammar -- not this module -- decides what is valid.
_DSL_BUILDERS: Dict[str, Any] = {
    "NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT": lambda f: (
        f"obsolete {f['about']} with replacement {f['direct']}" if f["direct"] else None
    ),
    "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT": lambda f: f"obsolete {f['about']}",
    "NODE_RENAME": lambda f: (
        f"rename {f['about']} from '{f['old']}' to '{f['new']}'"
        if f["old"] and f["new"]
        else None
    ),
    "NODE_TEXT_DEFINITION_CHANGE": lambda f: (
        f"change definition of {f['about']} to '{f['new']}'" if f["new"] else None
    ),
    "NEW_SYNONYM": lambda f: (
        f"create synonym '{f['new']}' for {f['about']}" if f["new"] else None
    ),
    "EDGE_CREATION": lambda f: (
        f"create edge {f['about']} {f['predicate']} {f['subject']}"
        if f["subject"] and f["predicate"]
        else None
    ),
    "EDGE_DELETION": lambda f: (
        f"delete edge {f['about']} {f['predicate']} {f['subject']}"
        if f["subject"] and f["predicate"]
        else None
    ),
    "NODE_DEEPENING": lambda f: (
        f"deepen {f['about']} from {f['old']} to {f['subject']}"
        if f["subject"] and f["old"]
        else None
    ),
    "NODE_SHALLOWING": lambda f: (
        f"shallow {f['about']} from {f['old']} to {f['subject']}"
        if f["subject"] and f["old"]
        else None
    ),
    "NODE_MOVE": lambda f: (
        f"move {f['about']} {f['predicate']} {f['subject']} from {f['old']} to {f['subject']}"
        if f["subject"] and f["predicate"] and f["old"]
        else None
    ),
}


def parse_kgcl(statement: str) -> Optional[Any]:
    """Parse a KGCL DSL statement, returning the change object or None if invalid.

    Delegates to KGCL's own lark grammar, so this module never has to encode
    what the DSL accepts.

    >>> type(parse_kgcl("obsolete GO:1")).__name__
    'NodeObsoletion'
    >>> parse_kgcl("merge GO:1 into GO:2") is None
    True
    """
    from kgcl_schema.grammar.parser import parse_statement

    try:
        return parse_statement(statement)
    except Exception:
        # The grammar raises a variety of lark errors; any of them means the
        # statement is not KGCL, which is all the caller needs to know.
        return None


def kgcl_dsl(change: Dict[str, Any]) -> Optional[str]:
    """Render a change in KGCL's controlled-English DSL, or None if it has none.

    Only a string that KGCL's own parser accepts is returned. Change types the
    grammar has no form for -- ``NODE_DIRECT_MERGE``, ``MAPPING_PREDICATE_CHANGE``,
    ``REMOVE_MAPPING``, ``COMPLEX_CHANGE``, ``OTHER`` -- yield None, and their
    structured slots and justification carry the request instead.

    >>> kgcl_dsl({"change_type": "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
    ...           "about_node": {"id": "GO:1"}})
    'obsolete GO:1'
    >>> kgcl_dsl({"change_type": "NODE_DIRECT_MERGE", "about_node": {"id": "GO:1"},
    ...           "has_direct_replacement": {"id": "GO:2"}}) is None
    True
    >>> kgcl_dsl({"change_type": "NEW_SYNONYM", "about_node": {"id": "GO:1"},
    ...           "new_value": "tethering"})
    "create synonym 'tethering' for GO:1"
    """
    builder = _DSL_BUILDERS.get(str(change.get("change_type")))
    about = _term_id(change.get("about_node"))
    if builder is None or not about:
        return None
    fields = {
        "about": about,
        "direct": _term_id(change.get("has_direct_replacement")),
        "subject": _term_id(change.get("subject")),
        "predicate": change.get("predicate"),
        "old": change.get("old_value"),
        "new": change.get("new_value"),
    }
    candidate = builder(fields)
    if not candidate:
        return None
    return candidate if parse_kgcl(candidate) is not None else None


@lru_cache(maxsize=1)
def _schema() -> Dict[str, Any]:
    """The gene-review schema, parsed once.

    Read as raw YAML rather than through SchemaView, which takes ten seconds to
    build and is not needed for the three facts below. The schema file stays the
    single source of truth either way.
    """
    import yaml

    from ai_gene_review.validation.validator import get_schema_path

    with open(get_schema_path(), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@lru_cache(maxsize=1)
def allowed_change_fields() -> frozenset[str]:
    """Attribute names ``ProposedOntologyChange`` declares.

    >>> "has_nondirect_replacement" in allowed_change_fields()
    True
    """
    attrs = _schema()["classes"]["ProposedOntologyChange"]["attributes"]
    return frozenset(attrs)


@lru_cache(maxsize=1)
def required_change_fields() -> frozenset[str]:
    """Attribute names ``ProposedOntologyChange`` marks required.

    >>> sorted(required_change_fields())[:2]
    ['about_node', 'change_type']
    """
    attrs = _schema()["classes"]["ProposedOntologyChange"]["attributes"]
    return frozenset(n for n, a in attrs.items() if (a or {}).get("required"))


@lru_cache(maxsize=1)
def allowed_change_types() -> frozenset[str]:
    """Permissible values of ``OntologyChangeTypeEnum``.

    >>> "NODE_DIRECT_MERGE" in allowed_change_types()
    True
    """
    enum = _schema()["enums"]["OntologyChangeTypeEnum"]["permissible_values"]
    return frozenset(enum)


#: Fields whose value is an inlined term, so a bare string or a label-only
#: mapping is a mistake rather than a shorthand.
_TERM_FIELDS = ("about_node", "has_direct_replacement", "subject")


def validate_change_entries(
    changes: Any,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Split a list of proposed changes into usable entries and structural errors.

    This is the structural gate for places LinkML never sees -- chiefly project
    page frontmatter, which is markdown rather than a schema-validated document.
    Gene and module reviews get the same checks from ``linkml-validate``.

    Only *structural* problems exclude an entry: a missing required field, an
    unknown field, a ``change_type`` outside the enum, or a term field without
    an id. Those make the entry unusable. Policy violations are advisory and
    reported separately by :func:`change_policy_warnings`, matching how they are
    treated on gene and module reviews, where they are WARNING-severity and
    exclude nothing.

    >>> valid, errors = validate_change_entries([{"change_type": "OTHER"}])
    >>> valid
    []
    >>> errors[0].startswith("proposed_ontology_changes[0] is missing")
    True
    >>> # a policy nit does not exclude the entry
    >>> entry = {"change_type": "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
    ...          "ontology": "GO", "about_node": {"id": "GO:1", "label": "x"},
    ...          "justification": "j", "confidence": "PROBABLE",
    ...          "report_status": "FIXED"}
    >>> valid, errors = validate_change_entries([entry])
    >>> len(valid), errors
    (1, [])
    """
    if not isinstance(changes, list):
        return [], ["proposed_ontology_changes must be a list"]
    errors: List[str] = []
    valid: List[Dict[str, Any]] = []
    for index, change in enumerate(changes):
        where = f"proposed_ontology_changes[{index}]"
        if not isinstance(change, dict):
            errors.append(f"{where} must be a mapping")
            continue
        problems: List[str] = []
        missing = sorted(required_change_fields() - set(change))
        if missing:
            problems.append(f"is missing required field(s) {missing}")
        unknown = sorted(set(change) - allowed_change_fields())
        if unknown:
            problems.append(
                f"has unknown field(s) {unknown}; allowed fields are "
                f"{sorted(allowed_change_fields())}"
            )
        kind = change.get("change_type")
        if kind is not None and kind not in allowed_change_types():
            problems.append(
                f"has change_type {kind!r}, which is not an OntologyChangeTypeEnum value"
            )
        for field in _TERM_FIELDS:
            value = change.get(field)
            if value is not None and not _term_id(value):
                problems.append(f"{field} needs a mapping with a non-empty 'id'")
        for problem in problems:
            errors.append(f"{where} {problem}")
        if not problems:
            valid.append(change)
    return valid, errors


def change_policy_warnings(changes: Any) -> List[str]:
    """Advisory policy messages for a bare list of proposed changes.

    The same checks :func:`iter_ontology_change_violations` applies to a review,
    phrased for a context that has no annotation rows to cross-check against.

    >>> change_policy_warnings([{"change_type": "NODE_DIRECT_MERGE",
    ...     "ontology": "GO", "about_node": {"id": "GO:1"}, "justification": "j",
    ...     "confidence": "PROBABLE"}])
    ['proposed_ontology_changes[0] missing_direct_replacement: NODE_DIRECT_MERGE names no replacement term']
    >>> change_policy_warnings("not a list")
    []
    """
    if not isinstance(changes, list):
        return []
    usable = [c for c in changes if isinstance(c, dict)]
    return [
        f"proposed_ontology_changes[{index}] {code}: {message}"
        for index, _field, code, message, _suggestion in (
            iter_ontology_change_violations({"proposed_ontology_changes": usable})
        )
    ]


def _accepted_terms(data: Dict[str, Any]) -> Dict[str, int]:
    """Map term id -> row index for annotation rows this review ACCEPTs outright."""
    accepted: Dict[str, int] = {}
    for index, ann in enumerate(data.get("existing_annotations") or []):
        review = ann.get("review") or {}
        if review.get("action") != "ACCEPT":
            continue
        term_id = _term_id(ann.get("term"))
        if term_id and term_id not in accepted:
            accepted[term_id] = index
    return accepted


def iter_ontology_change_violations(
    data: Dict[str, Any],
) -> Iterator[Tuple[int, str, str, str, str]]:
    """Yield ``(index, field, code, message, suggestion)`` for each violation.

    >>> list(iter_ontology_change_violations({}))
    []
    >>> bad = {"proposed_ontology_changes": [
    ...     {"change_type": "NODE_DIRECT_MERGE", "about_node": {"id": "GO:1"},
    ...      "justification": "dup", "confidence": "PROBABLE", "ontology": "GO"}]}
    >>> [c for _, _, c, _, _ in iter_ontology_change_violations(bad)]
    ['missing_direct_replacement']
    """
    accepted = _accepted_terms(data)
    for index, change in enumerate(data.get("proposed_ontology_changes") or []):
        if not isinstance(change, dict):
            continue
        kind = change.get("change_type")
        about = _term_id(change.get("about_node"))
        direct = _term_id(change.get("has_direct_replacement"))
        nondirect = [
            _term_id(t) for t in (change.get("has_nondirect_replacement") or [])
        ]
        old, new = change.get("old_value"), change.get("new_value")

        if kind in NEEDS_DIRECT_REPLACEMENT and not direct:
            verb = "merge" if kind == "NODE_DIRECT_MERGE" else "obsoletion"
            yield (
                index,
                "has_direct_replacement",
                "missing_direct_replacement",
                f"{kind} names no replacement term",
                f"A {verb} must name the term that survives. If no single term "
                "replaces it, use NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT and list "
                "alternatives in has_nondirect_replacement",
            )

        if kind in FORBIDS_DIRECT_REPLACEMENT and direct:
            yield (
                index,
                "has_direct_replacement",
                "unexpected_direct_replacement",
                f"{kind} carries a direct replacement",
                "A direct replacement means annotations can be repointed "
                "mechanically, so use NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT, or move "
                "the term to has_nondirect_replacement if it is only advice",
            )

        if kind in VALUE_CHANGES:
            if not old:
                yield (
                    index,
                    "old_value",
                    "missing_old_value",
                    f"{kind} does not record the value being changed",
                    "Copy the current definition, label, synonym or mapping predicate "
                    "from the ontology into old_value, verbatim",
                )
            if not new:
                yield (
                    index,
                    "new_value",
                    "missing_new_value",
                    f"{kind} does not record the proposed value",
                    "Put the proposed replacement in new_value",
                )
            if old and new and str(old).strip() == str(new).strip():
                yield (
                    index,
                    "new_value",
                    "value_unchanged",
                    f"{kind} proposes a value identical to the current one",
                    "State what should differ, or drop the change",
                )

        if kind in EDGE_CHANGES:
            if not _term_id(change.get("subject")):
                yield (
                    index,
                    "subject",
                    "missing_subject",
                    f"{kind} does not name the other end of the edge",
                    "Set subject to the parent or related term the edge points at",
                )
            if not change.get("predicate"):
                yield (
                    index,
                    "predicate",
                    "missing_predicate",
                    f"{kind} does not name the relation",
                    "Set predicate to the relation as a CURIE (rdfs:subClassOf, "
                    "BFO:0000050 part_of, RO:0002211 regulates); reparenting and adding "
                    "a part_of link are different changes",
                )

        if about and (about == direct or about in nondirect):
            yield (
                index,
                "has_direct_replacement"
                if about == direct
                else "has_nondirect_replacement",
                "self_replacement",
                f"{about} is offered as its own replacement",
                "Remove it; a term cannot replace itself",
            )

        if kind in PROSE_ONLY:
            words = len(str(change.get("justification") or "").split())
            if words < MIN_JUSTIFICATION_WORDS:
                yield (
                    index,
                    "justification",
                    "thin_justification",
                    f"{kind} has a {words}-word justification",
                    f"{kind} carries no KGCL semantics, so the justification is the "
                    "whole request. Say what the change is, step by step, in at least "
                    f"{MIN_JUSTIFICATION_WORDS} words. For a class split, name the terms "
                    "that should replace it and what distinguishes them",
                )

        status = change.get("report_status") or "NOT_REPORTED"
        if status in FILED_STATUSES and not (
            change.get("term_tracker_issue") or change.get("pull_request")
        ):
            yield (
                index,
                "term_tracker_issue",
                "missing_tracker_issue",
                f"report_status is {status} but no tracker issue is linked",
                "Add term_tracker_issue (or pull_request) so the upstream discussion can "
                "be found, or set report_status back to NOT_REPORTED",
            )

        dsl = change.get("change_dsl")
        if dsl:
            parsed = parse_kgcl(str(dsl))
            if parsed is None:
                yield (
                    index,
                    "change_dsl",
                    "dsl_unparseable",
                    "change_dsl is not valid KGCL",
                    "KGCL's grammar has no form for a merge, a mapping change or a mapping "
                    "removal, so leave change_dsl unset for those and let the structured "
                    "slots carry the request. Otherwise correct the syntax; the slots here "
                    f"render as: {kgcl_dsl(change) or '(no DSL for this change type)'}",
                )
            else:
                # Compare what the DSL says against the structured slots, using the
                # parsed object rather than string matching. Nondirect replacements
                # are excluded: the grammar has no syntax for them, so they are
                # legitimately absent from a correct DSL.
                parsed_about = getattr(parsed, "about_node", None)
                parsed_direct = getattr(parsed, "has_direct_replacement", None)
                if parsed_about and about and str(parsed_about) != about:
                    yield (
                        index,
                        "change_dsl",
                        "dsl_disagrees",
                        f"change_dsl is about {parsed_about} but about_node is {about}",
                        "The DSL is redundant with the slots on purpose, so one of the two "
                        "is wrong",
                    )
                if parsed_direct and direct and str(parsed_direct) != direct:
                    yield (
                        index,
                        "change_dsl",
                        "dsl_disagrees",
                        f"change_dsl replaces with {parsed_direct} but "
                        f"has_direct_replacement is {direct}",
                        "Correct whichever of the two is wrong",
                    )
                if type(parsed).__name__ != _KGCL_CLASS.get(
                    str(kind), type(parsed).__name__
                ):
                    yield (
                        index,
                        "change_dsl",
                        "dsl_wrong_kind",
                        f"change_dsl parses as KGCL {type(parsed).__name__} but "
                        f"change_type is {kind}",
                        "The DSL and change_type must describe the same kind of change; "
                        f"{kind} renders as: {kgcl_dsl(change) or '(no DSL for this change type)'}",
                    )

        if about and about in accepted and kind and kind.startswith("NODE_OBSOLETION"):
            row = accepted[about]
            yield (
                index,
                "about_node",
                "obsoletion_of_accepted_term",
                f"{about} is proposed for obsoletion but ACCEPTed on "
                f"existing_annotations[{row}]",
                "ACCEPT means the term is a core function of this gene, which contradicts "
                "asking for its obsoletion. Change that row to MODIFY with the replacement "
                "term, or drop the obsoletion proposal",
            )


def check_ontology_change_policy(data: Dict[str, Any], report) -> None:
    """Add a warning for each proposed-ontology-change violation in *data*."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    for index, field, code, message, suggestion in iter_ontology_change_violations(
        data
    ):
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f"proposed_ontology_changes[{index}].{field}",
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=f"ontology_change_{code}",
        )
