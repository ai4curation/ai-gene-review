"""Tests for standalone ai-gene-review history records.

The history mechanism (append-only session records under ``history/``) is
ported from dismech; see ``docs/history.md``.
"""

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

ROOT_DIR = Path(__file__).parent.parent
HISTORY_SCHEMA_PATH = ROOT_DIR / "src" / "ai_gene_review" / "schema" / "history.yaml"
HISTORY_DIR = ROOT_DIR / "history"
NEW_HISTORY_SCRIPT = ROOT_DIR / "scripts" / "new_history.py"
# Must stay in step with new_history.KIND_DIRS: any kind the generator can write
# is a kind whose placement the layout check has to enforce, or records land in
# an unchecked directory. test_kind_dirs_cover_every_generator_kind pins that.
KIND_DIRS = {
    "gene": "genes",
    "module": "modules",
    "gocam": "gocams",
    "project": "projects",
    "schema": "schema",
    "other": "other",
}


def _safe_load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _load_new_history_module():
    spec = importlib.util.spec_from_file_location("new_history", NEW_HISTORY_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(HISTORY_SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        HISTORY_SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_history_record_has_multivalued_actors(schema_view):
    induced = schema_view.class_induced_slots("HistorySession")
    slots = {slot.name: slot for slot in induced}

    assert "actors" in slots
    assert slots["actors"].multivalued is True
    assert slots["actors"].range == "HistoryActor"
    assert slots["actors"].minimum_cardinality == 1


def test_history_record_requires_details(schema_view):
    induced = schema_view.class_induced_slots("HistoryEvent")
    slots = {slot.name: slot for slot in induced}

    assert "details" in slots
    assert slots["details"].required is True


def test_history_actor_preserves_agent_tool_metadata(schema_view):
    induced = schema_view.class_induced_slots("HistoryActor")
    slots = {slot.name: slot for slot in induced}

    assert "model" in slots
    assert "agent_tool" in slots
    assert "agent_version" in slots


def test_history_target_kinds_cover_curated_content(schema_view):
    enum = schema_view.get_enum("HistoryTargetKindEnum")
    for kind in ("gene", "module", "gocam", "project", "schema", "other"):
        assert kind in enum.permissible_values


def test_history_record_validates_multiple_actors(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "gene",
            "slug": "CFAP300",
            "organism": "human",
            "path": "genes/human/CFAP300/CFAP300-ai-review.yaml",
        },
        "session": {
            "id": "2026-08-28T174412Z-claude-code-a3f9c2",
            "timestamp": "2026-08-28T17:44:12Z",
            "actors": [
                {
                    "type": "ai_agent",
                    "name": "claude-code",
                    "agent_tool": "claude-code",
                    "agent_version": "1.0",
                },
                {
                    "type": "human",
                    "name": "cjm",
                },
            ],
        },
        "links": {
            "issues": ["https://github.com/ai4curation/ai-gene-review/issues/2400"],
            "prs": ["https://github.com/ai4curation/ai-gene-review/pull/2500"],
            "urls": [],
        },
        "events": [
            {
                "type": "REVIEW",
                "outcome": "no_change",
                "sections": ["existing_annotations", "core_functions"],
                "summary": "Reviewed annotation actions; no immediate edits needed.",
                "details": "The review found no required changes.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, [e.message for e in errors]


def test_invalid_history_event_type_rejected(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "module",
            "slug": "some_module",
            "path": "modules/some_module.yaml",
        },
        "session": {
            "id": "2026-08-28T174412Z-claude-code-a3f9c2",
            "timestamp": "2026-08-28T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "claude-code"}],
        },
        "events": [
            {
                "type": "MIGRATION",
                "outcome": "changed",
                "summary": "not a valid event type",
                "details": "should fail",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid history event type"


def test_committed_history_records_validate(validator):
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    errors = []
    for path in history_files:
        report = validator.validate(_safe_load(path), target_class="HistoryRecord")
        errors.extend(
            f"{path.relative_to(ROOT_DIR)}: {result.message}"
            for result in report.results
            if result.severity.name == "ERROR"
        )

    assert not errors, "\n".join(errors)


def _layout_errors(record: dict, path: Path) -> list[str]:
    """Check one history record's target against the on-disk repository layout.

    History records are append-only, so a record whose target was later renamed
    keeps its original ``slug``/``path``. Such a record documents the move with
    ``target.superseded_by``; the successor is then what must exist on disk, and
    the record files live under the successor's slug directory. Without
    ``superseded_by``, a missing target is an ordinary error and still fails.
    """
    rel = path.relative_to(ROOT_DIR)
    target = record["target"]
    kind = target["kind"]
    slug = target["slug"]
    organism = target.get("organism")
    superseded_by = target.get("superseded_by")
    errors = []

    # Both generators mint the filename from session.id, and CLAUDE.md tells
    # agents never to hand-write either -- but nothing enforced it, so a
    # hand-edited record could drift the two apart undetected.
    session_id = record.get("session", {}).get("id")
    if session_id is not None and session_id != path.stem:
        errors.append(
            f"{rel} session.id '{session_id}' does not match the filename stem '{path.stem}'"
        )

    if superseded_by:
        successor_slug = superseded_by.get("slug")
        successor_rel = superseded_by.get("path")
        if not successor_slug or not successor_rel:
            return [f"{rel} target.superseded_by needs both a slug and a path"]
        if not (ROOT_DIR / successor_rel).exists():
            errors.append(
                f"{rel} target.superseded_by path does not exist: {successor_rel}"
            )
        if kind == "gene":
            # genes/<org>/<GENE>/<GENE>-ai-review.yaml: the slug is the gene
            # directory, and the organism directory must track the successor.
            parts = Path(successor_rel).parts
            if len(parts) < 3 or parts[0] != "genes" or parts[2] != successor_slug:
                errors.append(
                    f"{rel} target.superseded_by slug '{successor_slug}' does not match "
                    f"the gene directory of its path '{successor_rel}'"
                )
            else:
                organism = superseded_by.get("organism") or parts[1]
        elif Path(successor_rel).stem != successor_slug:
            errors.append(
                f"{rel} target.superseded_by slug '{successor_slug}' does not match "
                f"the stem of its path '{successor_rel}'"
            )
        slug = successor_slug
    elif not (ROOT_DIR / target["path"]).exists():
        errors.append(f"{rel} target does not exist")

    if kind in KIND_DIRS:
        expected_parent = HISTORY_DIR / KIND_DIRS[kind]
        if kind == "gene":
            expected_parent = expected_parent / (organism or "")
        expected_parent = expected_parent / slug
        if path.parent != expected_parent:
            errors.append(
                f"{rel} should live under {expected_parent.relative_to(ROOT_DIR)}"
            )

    return errors


def test_kind_dirs_cover_every_generator_kind():
    """A kind `new_history.py` can write but the layout check does not know is a
    directory nothing enforces. `other` was exactly that: supported by the
    generator and documented in docs/history.md, absent from KIND_DIRS."""
    module = _load_new_history_module()
    assert KIND_DIRS == module.KIND_SUBDIRS


def test_committed_history_records_follow_layout():
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    errors = []
    for path in history_files:
        errors.extend(_layout_errors(_safe_load(path), path))

    assert not errors, "\n".join(errors)


def _supersession_record(successor_path: str, successor_slug: str | None = None) -> dict:
    """Record whose target was renamed. The successor slug defaults to the path
    stem so each negative test below has a single cause; only the slug/stem
    mismatch test overrides it."""
    return {
        "target": {
            "kind": "module",
            "slug": "old_name",
            "path": "modules/old_name.yaml",
            "superseded_by": {
                "slug": successor_slug or Path(successor_path).stem,
                "path": successor_path,
            },
        }
    }


def _existing_module_slug() -> str:
    yamls = sorted((ROOT_DIR / "modules").glob("*.yaml"))
    assert yamls, "expected at least one module YAML for layout tests"
    return yamls[0].stem


def test_layout_rejects_session_id_that_drifts_from_the_filename():
    slug = _existing_module_slug()
    record = {
        "target": {"kind": "module", "slug": slug, "path": f"modules/{slug}.yaml"},
        "session": {"id": "2026-08-02T020640Z-codex-abc123"},
    }
    good = HISTORY_DIR / "modules" / slug / "2026-08-02T020640Z-codex-abc123.yaml"
    bad = HISTORY_DIR / "modules" / slug / "2026-08-02T020640Z-codex-999999.yaml"

    assert _layout_errors(record, good) == []
    (error,) = _layout_errors(record, bad)
    assert "does not match the filename stem" in error


@pytest.mark.parametrize("missing", ["slug", "path"])
def test_target_slug_and_path_are_required(validator, missing):
    """`_layout_errors` and `history_dir_for` both index these unconditionally,
    so a record without them must fail validation rather than KeyError later."""
    record = {
        "history_version": 1,
        "target": {"kind": "module", "slug": "x", "path": "modules/x.yaml"},
        "session": {
            "id": "2026-08-02T020640Z-codex-abc123",
            "timestamp": "2026-08-02T02:06:40Z",
            "actors": [{"type": "ai_agent", "name": "codex"}],
        },
        "events": [
            {"type": "EDIT", "outcome": "changed", "summary": "s", "details": "d"}
        ],
    }
    assert not [
        r
        for r in validator.validate(record, target_class="HistoryRecord").results
        if r.severity.name == "ERROR"
    ]

    del record["target"][missing]
    assert [
        r
        for r in validator.validate(record, target_class="HistoryRecord").results
        if r.severity.name == "ERROR"
    ]


def test_layout_accepts_renamed_target_with_superseded_by():
    slug = _existing_module_slug()
    record = _supersession_record(f"modules/{slug}.yaml")
    path = HISTORY_DIR / "modules" / slug / "2026-08-02T020640Z-codex-abc123.yaml"

    assert _layout_errors(record, path) == []


def test_layout_rejects_superseded_by_pointing_at_missing_target():
    record = _supersession_record("modules/does_not_exist.yaml")
    path = (
        HISTORY_DIR / "modules" / "does_not_exist"
        / "2026-08-02T020640Z-codex-abc123.yaml"
    )

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "superseded_by path does not exist" in errors[0]


def test_layout_rejects_missing_target_without_superseded_by():
    record = {
        "target": {
            "kind": "module",
            "slug": "does_not_exist",
            "path": "modules/does_not_exist.yaml",
        }
    }
    path = (
        HISTORY_DIR / "modules" / "does_not_exist"
        / "2026-08-02T020640Z-codex-abc123.yaml"
    )

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "target does not exist" in errors[0]


def test_layout_rejects_superseded_by_slug_path_mismatch():
    slug = _existing_module_slug()
    record = _supersession_record(f"modules/{slug}.yaml", successor_slug="wrong_slug")
    path = HISTORY_DIR / "modules" / "wrong_slug" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "does not match the stem of its path" in errors[0]


def test_layout_rejects_incomplete_superseded_by_block():
    record = {
        "target": {
            "kind": "module",
            "slug": "old_name",
            "path": "modules/old_name.yaml",
            "superseded_by": {"reason": "no slug or path"},
        }
    }
    path = HISTORY_DIR / "modules" / "old_name" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert any("needs both a slug and a path" in error for error in errors)


def test_layout_requires_record_directory_to_follow_successor_slug():
    slug = _existing_module_slug()
    record = _supersession_record(f"modules/{slug}.yaml")
    path = HISTORY_DIR / "modules" / "old_name" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert any("should live under" in error for error in errors)


def test_layout_gene_records_nest_by_organism():
    gene_dirs = sorted((ROOT_DIR / "genes" / "human").iterdir())
    gene = next(d.name for d in gene_dirs if (d / f"{d.name}-ai-review.yaml").exists())
    record = {
        "target": {
            "kind": "gene",
            "slug": gene,
            "organism": "human",
            "path": f"genes/human/{gene}/{gene}-ai-review.yaml",
        }
    }
    good = HISTORY_DIR / "genes" / "human" / gene / "2026-08-02T020640Z-cc-abc123.yaml"
    assert _layout_errors(record, good) == []

    flat = HISTORY_DIR / "genes" / gene / "2026-08-02T020640Z-cc-abc123.yaml"
    errors = _layout_errors(record, flat)
    assert any("should live under" in error for error in errors)


def test_history_record_with_superseded_by_validates(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "module",
            "slug": "old_name",
            "path": "modules/old_name.yaml",
            "superseded_by": {
                "slug": "new_name",
                "path": "modules/new_name.yaml",
                "reason": "Merged into new_name after boundary review.",
            },
        },
        "session": {
            "id": "2026-08-28T174412Z-claude-code-a3f9c2",
            "timestamp": "2026-08-28T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "claude-code"}],
        },
        "events": [
            {
                "type": "EDIT",
                "outcome": "changed",
                "summary": "Edited the old module before the merge.",
                "details": "Session predates the rename; superseded_by records the move.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, [e.message for e in errors]


def test_superseded_by_requires_reason(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "module",
            "slug": "old_name",
            "path": "modules/old_name.yaml",
            "superseded_by": {
                "slug": "new_name",
                "path": "modules/new_name.yaml",
            },
        },
        "session": {
            "id": "2026-08-28T174412Z-claude-code-a3f9c2",
            "timestamp": "2026-08-28T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "claude-code"}],
        },
        "events": [
            {
                "type": "EDIT",
                "outcome": "changed",
                "summary": "x",
                "details": "x",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for superseded_by without reason"


def test_new_history_scaffolder_emits_valid_record(
    validator, tmp_path, monkeypatch
):
    module = _load_new_history_module()
    monkeypatch.chdir(tmp_path)

    args = module.parse_args(
        [
            "--kind", "gene",
            "--organism", "human",
            "--slug", "CFAP300",
            "--event", "CREATE",
            "--outcome", "changed",
            "--summary", "Create review: CFAP300",
            "--agent-tool", "claude-code",
            "--pr", "2500",
            "--details", "Scaffolder self-test.",
        ]
    )
    record, out_path = module.build_record(args)

    assert record["target"]["path"] == "genes/human/CFAP300/CFAP300-ai-review.yaml"
    assert record["target"]["organism"] == "human"
    assert record["links"]["prs"] == [
        "https://github.com/ai4curation/ai-gene-review/pull/2500"
    ]
    assert out_path.parts[:4] == ("history", "genes", "human", "CFAP300")

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, [e.message for e in errors]


def test_new_history_scaffolder_requires_organism_for_genes():
    module = _load_new_history_module()
    args = module.parse_args(
        ["--kind", "gene", "--slug", "CFAP300", "--summary", "x"]
    )
    with pytest.raises(SystemExit):
        module.build_record(args)


def test_new_history_scaffolder_requires_slug_for_derived_kinds():
    module = _load_new_history_module()
    args = module.parse_args(["--kind", "module", "--summary", "x"])
    with pytest.raises(SystemExit):
        module.build_record(args)


def test_new_history_scaffolder_requires_path_for_schema_kind():
    module = _load_new_history_module()
    args = module.parse_args(["--kind", "schema", "--summary", "x"])
    with pytest.raises(SystemExit):
        module.build_record(args)


def test_new_history_scaffolder_warns_on_missing_target():
    module = _load_new_history_module()
    assert module.target_missing_warning("genes/human/NO_SUCH/NO_SUCH-ai-review.yaml")
    assert module.target_missing_warning("src/ai_gene_review/schema/history.yaml") is None


def test_new_history_writes_multiword_summary_and_details(tmp_path, monkeypatch):
    """A multi-word --summary/--details must survive the CLI into the record.

    Every documented invocation quotes both flags, so this is the round trip
    that the `just` seam (below) has to preserve.
    """
    module = _load_new_history_module()
    monkeypatch.chdir(tmp_path)

    summary = "Create review: CFAP300"
    details = "One-paragraph summary of what the session did."
    module.main(
        [
            "--kind", "module",
            "--slug", "biotin_biosynthesis",
            "--summary", summary,
            "--details", details,
        ]
    )

    written = sorted((tmp_path / "history" / "modules" / "biotin_biosynthesis").glob("*.yaml"))
    assert len(written) == 1, written
    record = _safe_load(written[0])
    assert record["events"][0]["summary"] == summary
    assert record["events"][0]["details"].strip() == details


@pytest.mark.parametrize("recipe", ["new-history", "backfill-history"])
def test_history_justfile_recipes_preserve_argument_quoting(recipe):
    """The `just` seam must not flatten quoted arguments.

    `just` joins a variadic ``*ARGS`` into a single space-separated string, so a
    recipe body that interpolates ``{{ARGS}}`` loses shell quoting: the
    documented ``--summary "Create review: CFAP300"`` reaches argparse as four
    separate tokens and dies with "unrecognized arguments". The repo-wide fix
    idiom is ``[positional-arguments]`` plus ``"$@"``.
    """
    justfile = (ROOT_DIR / "project.justfile").read_text(encoding="utf-8")
    lines = justfile.splitlines()
    starts = [i for i, line in enumerate(lines) if line.startswith(f"{recipe} *ARGS:")]
    assert len(starts) == 1, f"expected exactly one {recipe} recipe, found {len(starts)}"
    start = starts[0]

    attributes = set()
    i = start - 1
    while i >= 0 and lines[i].startswith("["):
        attributes.add(lines[i].strip())
        i -= 1
    assert "[positional-arguments]" in attributes, (
        f"{recipe} must declare [positional-arguments] (attributes must sit "
        f"directly above the recipe, with no comment in between)"
    )

    body = lines[start + 1]
    assert '"$@"' in body, f"{recipe} body must forward arguments with \"$@\": {body}"
    assert "{{ARGS}}" not in body, f"{recipe} body must not interpolate {{{{ARGS}}}}: {body}"


@pytest.mark.parametrize("recipe", ["new-history", "backfill-history"])
def test_history_justfile_recipes_do_not_flatten_quoted_args(recipe):
    """Same invariant as above, but asserted against real `just` expansion."""
    just = shutil.which("just")
    if just is None:
        pytest.skip("just is not installed")

    result = subprocess.run(
        [just, "--dry-run", recipe, "--summary", "Create review: CFAP300"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    expanded = result.stdout + result.stderr
    assert "Create review: CFAP300" not in expanded, (
        f"{recipe} expanded the quoted argument into the command line, so the "
        f"quoting is lost: {expanded.strip()}"
    )
    assert '"$@"' in expanded, expanded.strip()
