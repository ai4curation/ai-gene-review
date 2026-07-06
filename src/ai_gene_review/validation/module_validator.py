"""Term-label validation for module (``ModuleReview``) YAML files.

The repository delegates gene-review term-label checking to the external
``linkml-term-validator``, but that tool only inspects slots bound to dynamic
enums or binding constraints. ``ModuleReview`` has neither, so the ``term``
descriptors scattered through a module document (``concepts``, ``function``,
``substrates``/``products``, ``locations``, ``processes``,
``anatomical_locations``, ...) are otherwise unchecked: a wrong label sails
through structural validation.

This validator closes that gap. It walks a module YAML, collects every
``{id, label}`` term, routes each id by prefix through the same
``conf/oak_config.yaml`` mapping used for gene reviews, resolves the id with
OAK, and reports:

* an ERROR when the provided label does not match the ontology's primary label
  or any of its aliases (case-insensitively), and
* an ERROR when the id cannot be found in the configured ontology.

Prefixes mapped to ``null`` (e.g. ``PMID``, ``UniProtKB``, ``file``) are skipped
silently; prefixes absent from the config are skipped with a warning, matching
the documented ``oak_config.yaml`` semantics.

It also enforces **bundle-scoped conformance**: any node declaring
``conforms_to`` a template motif is checked (via ``module_qc``) so that an
``error``-severity mismatch -- a wrong/missing tier, a broken relay topology,
or an unresolvable template -- blocks validation, while declared
``WITH_DEVIATIONS`` deviations surface as advisory warnings.

It also runs an **advisory reaction-chaining check**: for each ``PRECEDES``
connection it resolves both reactions' GO molecular-function terms to RHEA (via
the GO->RHEA mapping) and warns when the upstream reaction's product is not the
downstream reaction's substrate. This NEVER blocks; a ``chaining_status``
override on the connection (e.g. ``KNOWLEDGE_GAP``, ``MAPPING_GAP``) acknowledges
a real break and suppresses its warning.

Structural (schema) validation is handled separately by ``linkml-validate``
(see ``just validate-modules``); this module adds term-label, conformance, and
chaining checking.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Set, Tuple

import yaml

# A resolver answers: given a CURIE, return (status, primary_label, aliases).
# status is "ok" when the id resolved, "not_found" when the ontology was
# consulted but the id is absent, and "unavailable" when the ontology itself
# could not be loaded/queried (e.g. transient download failure) - the latter is
# advisory so CI does not go red on flaky ontology fetches. Implemented as a
# plain callable so it can be dependency-injected in tests without mocking.
Resolver = Callable[[str], Tuple[str, Optional[str], Set[str]]]


@dataclass
class ModuleValidationResult:
    """Result of validating a single module file's term labels."""

    path: Path
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """True when there are no errors (warnings are advisory)."""
        return not self.errors


def iter_terms(obj: object) -> Iterator[Tuple[str, str]]:
    """Yield every ontology ``(id, label)`` pair from a parsed module document.

    In the schema, ontology grounding only ever appears as the value of a
    ``term`` key (``Descriptor.term``, range ``Term``). Module *nodes* and
    *annotons* also carry ``id``/``label`` fields, but those are
    document-scoped identifiers, not ontology terms, so they must NOT be
    collected. We therefore yield only dicts reached via a ``term`` key that
    carry a string ``id`` and ``label``.

    >>> doc = {"term": {"id": "GO:1", "label": "x"}}
    >>> list(iter_terms(doc))
    [('GO:1', 'x')]
    >>> list(iter_terms({"id": "some_node", "label": "a node"}))
    []
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if (
                key == "term"
                and isinstance(value, dict)
                and isinstance(value.get("id"), str)
                and isinstance(value.get("label"), str)
            ):
                yield (value["id"], value["label"])
            yield from iter_terms(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_terms(item)


def compare_label(
    curie: str, provided: str, primary: Optional[str], aliases: Set[str]
) -> Optional[str]:
    """Return an error message if ``provided`` does not match the ontology.

    A match is exact or case-insensitive against the primary label or any alias.

    >>> compare_label("X:1", "root", "root", set()) is None
    True
    >>> compare_label("X:1", "wrong", "root", set()) is not None
    True
    """
    candidates = {c for c in ([primary] if primary else []) + list(aliases)}
    if provided in candidates:
        return None
    lowered = {c.lower() for c in candidates}
    if provided.lower() in lowered:
        return None
    shown = primary if primary is not None else "<no label>"
    return (
        f"Label mismatch for {curie}: module says '{provided}' "
        f"but ontology label is '{shown}'"
    )


def validate_terms(
    terms: List[Tuple[str, str]],
    adapter_map: Dict[str, Optional[str]],
    resolver: Resolver,
) -> Tuple[List[str], List[str]]:
    """Validate a list of ``(id, label)`` terms, returning (errors, warnings).

    ``adapter_map`` maps a prefix to an OAK adapter string, to ``None`` (skip
    silently), or omits it (skip with a warning). ``resolver`` performs the
    actual ontology lookup for configured prefixes.
    """
    errors: List[str] = []
    warnings: List[str] = []
    unconfigured_seen: Set[str] = set()

    for curie, label in terms:
        prefix = curie.split(":", 1)[0] if ":" in curie else curie
        if prefix not in adapter_map:
            if prefix not in unconfigured_seen:
                unconfigured_seen.add(prefix)
                warnings.append(
                    f"Prefix '{prefix}' (e.g. {curie}) is not in oak_config.yaml; "
                    f"term label not validated"
                )
            continue
        if adapter_map[prefix] is None:
            continue  # explicitly skipped (null), no warning
        status, primary, aliases = resolver(curie)
        if status == "unavailable":
            warnings.append(
                f"Could not consult ontology for {curie} "
                f"(ontology unavailable); label not validated"
            )
            continue
        if status == "not_found":
            errors.append(f"Term id {curie} not found in configured ontology")
            continue
        err = compare_label(curie, label, primary, aliases)
        if err:
            errors.append(err)

    return errors, warnings


def load_oak_adapter_map(config_path: Path) -> Dict[str, Optional[str]]:
    """Load the prefix -> adapter mapping from an ``oak_config.yaml``."""
    with open(config_path) as f:
        data = yaml.safe_load(f) or {}
    adapters = data.get("ontology_adapters", {})
    return {str(k): (None if v is None else str(v)) for k, v in adapters.items()}


def _build_oak_resolver(adapter_map: Dict[str, Optional[str]]) -> Resolver:
    """Build a resolver backed by real OAK adapters (lazily created, cached).

    Adapter creation and lookups touch external ontology databases, so failures
    (network/download issues) degrade to ``not_found`` would be wrong here;
    instead such terms are treated as resolvable-but-unknown and reported by the
    caller. We keep one adapter per adapter string.
    """
    from oaklib import get_adapter  # imported lazily; heavy dependency

    cache: Dict[str, object] = {}
    # Adapter strings that failed to load are remembered so we don't retry (and
    # re-log) them per term.
    failed: Set[str] = set()

    def get(adapter_string: str):
        if adapter_string in failed:
            return None
        if adapter_string not in cache:
            # External system (ontology download/db): tolerate failures and
            # degrade to "unavailable" rather than crashing the whole run.
            try:
                cache[adapter_string] = get_adapter(adapter_string)
            except Exception:  # noqa: BLE001 - external system
                failed.add(adapter_string)
                return None
        return cache[adapter_string]

    def resolve(curie: str) -> Tuple[str, Optional[str], Set[str]]:
        prefix = curie.split(":", 1)[0]
        adapter_string = adapter_map[prefix]
        assert adapter_string is not None  # routed only for configured prefixes
        adapter = get(adapter_string)
        if adapter is None:
            return ("unavailable", None, set())
        try:  # external system: ontology query may fail transiently
            primary = adapter.label(curie)
            if primary is None:
                return ("not_found", None, set())
            aliases: Set[str] = set()
            # entity_aliases includes synonyms; tolerate adapters lacking it.
            alias_fn = getattr(adapter, "entity_aliases", None)
            if callable(alias_fn):
                aliases = {a for a in alias_fn(curie) if isinstance(a, str)}
            return ("ok", primary, aliases)
        except Exception:  # noqa: BLE001 - external system
            return ("unavailable", None, set())

    return resolve


def validate_module_file(
    path: Path,
    config_path: Optional[Path] = None,
    resolver: Optional[Resolver] = None,
) -> ModuleValidationResult:
    """Validate term labels in a single module YAML file.

    ``resolver`` may be injected for testing; otherwise a real OAK-backed
    resolver is built from ``config_path`` (defaults to ``conf/oak_config.yaml``
    relative to the repository root).
    """
    path = Path(path)
    if config_path is None:
        config_path = Path(__file__).resolve().parents[3] / "conf" / "oak_config.yaml"
    adapter_map = load_oak_adapter_map(config_path)

    with open(path) as f:
        doc = yaml.safe_load(f)

    terms = list(iter_terms(doc))
    if resolver is None:
        resolver = _build_oak_resolver(adapter_map)
    errors, warnings = validate_terms(terms, adapter_map, resolver)

    # Conformance: verify every `conforms_to` bundle against its template motif.
    # Templates are sibling module files, so they are resolved from the file's
    # own directory. Errors block; warnings/info are advisory.
    conformance_errors, conformance_warnings = validate_conformance(doc, path.parent)
    errors.extend(conformance_errors)
    warnings.extend(conformance_warnings)

    # Reaction chaining: advisory only (never blocks). A `chaining_status`
    # override on a connection acknowledges a known gap and suppresses its
    # warning. Resolution touches the GO/RHEA ontology DBs, so it degrades to
    # "no findings" when those are unavailable.
    warnings.extend(validate_chaining(doc))

    # Supporting-text snippets: every EvidenceItem literature quote (PMID/DOI
    # source_id paired with supporting_text) must be a verbatim (normalized)
    # substring of the cached publication. Mismatches block; unfetchable or
    # uncached references degrade to advisory warnings.
    st_errors, st_warnings = validate_supporting_text(doc)
    errors.extend(st_errors)
    warnings.extend(st_warnings)

    return ModuleValidationResult(path=path, errors=errors, warnings=warnings)


# Literature source_id prefixes whose supporting_text quotes are checked
# verbatim against a cached publication. Everything else (GO, file:, PANTHER,
# Reactome, UniProtKB, ...) is provenance grounding, not a fetchable quote.
_LITERATURE_PREFIXES = {"PMID", "DOI"}


def iter_evidence_snippets(obj: object) -> Iterator[Tuple[str, str]]:
    """Yield ``(source_id, supporting_text)`` for every EvidenceItem-like dict.

    An EvidenceItem is recognised structurally as any mapping carrying both a
    ``source_id`` and a non-empty ``supporting_text``. Only literature sources
    (``PMID:``/``DOI:``) are yielded, since only those have a fetchable text to
    check the quote against.

    >>> doc = {"evidence": [{"source_id": "PMID:1", "supporting_text": "x"},
    ...                     {"source_id": "GO:0001", "supporting_text": "y"}]}
    >>> list(iter_evidence_snippets(doc))
    [('PMID:1', 'x')]
    """
    if isinstance(obj, dict):
        source_id = obj.get("source_id")
        supporting_text = obj.get("supporting_text")
        if (
            isinstance(source_id, str)
            and isinstance(supporting_text, str)
            and supporting_text.strip()
        ):
            prefix = source_id.split(":", 1)[0].upper()
            if prefix in _LITERATURE_PREFIXES:
                yield (source_id, supporting_text)
        for value in obj.values():
            yield from iter_evidence_snippets(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_evidence_snippets(item)


def validate_supporting_text(
    doc: object,
    publications_dir: Optional[Path] = None,
) -> Tuple[List[str], List[str]]:
    """Verify every EvidenceItem literature quote against the cached publication.

    Uses ``linkml-reference-validator``'s own ``SupportingTextValidator`` (the
    same normalize + deterministic-substring matcher gene reviews use), reading
    from the ``publications/`` cache. Returns ``(errors, warnings)``:

    - a quote that is not a substring of the fetched/cached publication is an
      **error** (blocks validation);
    - a reference that cannot be fetched or is not cached is a **warning**
      (advisory, so offline/rate-limited runs do not hard-fail).

    The check is a no-op (returns empty) when the reference validator is not
    installed, so it degrades gracefully.
    """
    if not isinstance(doc, dict):
        return [], []

    snippets = list(iter_evidence_snippets(doc))
    if not snippets:
        return [], []

    try:
        from linkml_reference_validator.models import ReferenceValidationConfig
        from linkml_reference_validator.validation.supporting_text_validator import (
            SupportingTextValidator,
        )
    except ImportError:
        return [], []

    if publications_dir is None:
        publications_dir = (
            Path(__file__).resolve().parents[3] / "publications"
        )

    config = ReferenceValidationConfig(
        cache_dir=publications_dir,
        fetch_full_text=False,
    )
    validator = SupportingTextValidator(config)

    errors: List[str] = []
    warnings: List[str] = []
    for source_id, supporting_text in snippets:
        result = validator.validate(supporting_text, source_id)
        if result.is_valid:
            continue
        message = str(getattr(result, "message", "") or "")
        if "could not fetch" in message.lower() or "no records found" in message.lower():
            warnings.append(f"Supporting text unverified ({source_id}): {message}")
        else:
            errors.append(f"Supporting text mismatch ({source_id}): {message}")
    return errors, warnings


def validate_chaining(doc: object) -> List[str]:
    """Return advisory chaining warnings for a module document.

    Only ``warning``-severity findings are surfaced (an unacknowledged break
    where the upstream reaction's product is not the downstream substrate).
    ``info`` findings -- verified continuity or an acknowledged ``chaining_status``
    gap -- are not reported. This check NEVER produces errors.
    """
    from ai_gene_review.module_qc import reaction_chaining_findings

    if not isinstance(doc, dict):
        return []
    return [
        f"Reaction chaining: {f['message']}"
        for f in reaction_chaining_findings(doc)
        if f.get("severity") == "warning"
    ]


def validate_conformance(doc: object, modules_dir: Path) -> Tuple[List[str], List[str]]:
    """Check every ``conforms_to`` bundle against its template motif.

    Returns ``(errors, warnings)`` where ``error``-severity conformance
    violations block validation and ``warning``/``info`` ones are advisory.
    Templates are resolved relative to ``modules_dir`` (the document's own
    directory, since template motifs are sibling module files).
    """
    # Imported here to avoid a heavy import at module load and any import cycle.
    from ai_gene_review.module_qc import conformance_violations

    if not isinstance(doc, dict):
        return [], []

    errors: List[str] = []
    warnings: List[str] = []
    for violation in conformance_violations(doc, modules_dir=modules_dir):
        message = (
            f"Conformance [{violation['node_id']} -> {violation['template']}]: "
            f"{violation['message']}"
        )
        if violation["severity"] == "error":
            errors.append(message)
        else:
            warnings.append(message)
    return errors, warnings


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point: validate one or more module files. Returns exit code."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate term labels in module (ModuleReview) YAML files."
    )
    parser.add_argument("files", nargs="+", type=Path, help="Module YAML files")
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=None,
        help="Path to oak_config.yaml (default: conf/oak_config.yaml)",
    )
    args = parser.parse_args(argv)

    exit_code = 0
    for path in args.files:
        result = validate_module_file(path, config_path=args.config)
        for w in result.warnings:
            print(f"⚠️  WARN  {path}: {w}")
        for e in result.errors:
            print(f"❌ ERROR {path}: {e}")
        if result.is_valid:
            print(f"✅ {path}: term labels OK ({len(result.warnings)} warnings)")
        else:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
