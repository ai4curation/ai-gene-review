"""Tests for the centralized agent-config model resolution.

`.github/agent-config.yaml` is the single source of truth for which Claude model
backs each agentic workflow. These tests pin the resolver's behaviour and, more
importantly, keep the config honest: every key must map to a real workflow that
actually sources its model from the config, and no workflow may pin a model of
its own — a stale or retired model id breaks every run of that workflow, and one
config file is a much smaller place to keep current than twenty-odd call sites.
"""

import importlib.util
import re
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTION_DIR = REPO_ROOT / ".github" / "actions" / "resolve-agent-config"
CONFIG_PATH = REPO_ROOT / ".github" / "agent-config.yaml"
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

_SPEC = importlib.util.spec_from_file_location(
    "resolve_agent_config", ACTION_DIR / "resolve_agent_config.py"
)
assert _SPEC is not None and _SPEC.loader is not None
resolver = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = resolver
_SPEC.loader.exec_module(resolver)


@pytest.fixture
def config() -> dict:
    return resolver.load_config(CONFIG_PATH)


def test_single_model_resolves_from_config(config):
    assert resolver.resolve_model(config, "pr-shepherd") == "claude-opus-5"


def test_override_wins(config):
    assert (
        resolver.resolve_model(config, "pr-shepherd", "claude-sonnet-5")
        == "claude-sonnet-5"
    )
    # whitespace-only override is treated as no override
    assert resolver.resolve_model(config, "pr-shepherd", "  ") == "claude-opus-5"


def test_default_model_fallback():
    cfg = {"default_model": "claude-opus-5", "workflows": {"x": {}}}
    assert resolver.resolve_model(cfg, "x") == "claude-opus-5"


def test_unknown_workflow_errors(config):
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(config, "does-not-exist")


def test_missing_model_and_default_errors():
    cfg = {"workflows": {"x": {}}}
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(cfg, "x")


def test_matrix_mode_round_trips():
    cfg = {
        "workflows": {
            "fan-out": {
                "matrix": [
                    {"effort": "low_effort", "model": "claude-haiku-4-5-20251001"},
                    {"effort": "high_effort", "model": "claude-opus-5"},
                ]
            }
        }
    }
    matrix = resolver.resolve_matrix(cfg, "fan-out")
    assert [entry["model"] for entry in matrix] == [
        "claude-haiku-4-5-20251001",
        "claude-opus-5",
    ]


def test_single_model_mode_rejects_matrix_workflow():
    cfg = {"workflows": {"fan-out": {"matrix": [{"model": "claude-opus-5"}]}}}
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(cfg, "fan-out")


def test_every_config_workflow_file_exists(config):
    """Each key under workflows: must map to a real workflow file."""
    for stem in config["workflows"]:
        candidates = [WORKFLOW_DIR / f"{stem}.yml", WORKFLOW_DIR / f"{stem}.yaml"]
        assert any(c.exists() for c in candidates), f"no workflow file for '{stem}'"


def _workflow_texts() -> dict[str, str]:
    return {path.stem: path.read_text() for path in WORKFLOW_DIR.glob("*.y*ml")}


# Escape hatch for a workflow not yet migrated onto the central config. Now
# empty: every agentic workflow resolves its model from agent-config.yaml. An
# entry here must correspond to a real pin (a stale entry fails the test), so
# the list can only shrink.
UNMIGRATED_MODEL_PINS: set[str] = set()

# Model families, plus the bare aliases the CLI also accepts (`--model opus`).
_MODEL_VALUE = (
    r"(?:claude-(?:haiku|sonnet|opus|fable)[\w.-]*|\b(?:opus|sonnet|haiku|fable)\b)"
)
# A `--model` flag resolved from anything other than AGENT_MODEL. Matching the
# whole line (not just the token after the flag) catches the common
# `--model ${{ inputs.model || 'claude-opus-4-7' }}` shape.
_CLI_PIN = re.compile(rf"--model\b(?!.*env\.AGENT_MODEL).*{_MODEL_VALUE}")
# A YAML `*model:` key pinned to a literal model. Catches the action's `model:`
# input, `strategy.matrix` entries, and `env:` indirection such as
# `ISSUE_HANDOFF_MODEL: ${{ inputs.model || 'claude-haiku-...' }}`.
_YAML_PIN = re.compile(rf"^\s*[\w-]*model:\s*.*{_MODEL_VALUE}", re.IGNORECASE)
# A workflow_dispatch input whose `default:` is a model: a dispatch default is
# always sent, so it silently overrides the central config on every manual run.
_DEFAULT_PIN = re.compile(rf"^\s*default:\s*['\"]?{_MODEL_VALUE}")


def _model_pins(text: str) -> list[str]:
    """Lines that pin a model, ignoring `choice` option lists and comments.

    A dispatch dropdown may legitimately *list* models as `- claude-...`
    options; only the effective value is a pin.
    """
    pins = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- claude-") or stripped.startswith("#"):
            continue
        if _CLI_PIN.search(line) or _YAML_PIN.match(line) or _DEFAULT_PIN.match(line):
            pins.append(stripped)
    return pins


def test_no_workflow_pins_a_model_inline():
    """No workflow should pin a model; models must come from the config.

    A stale or retired model id breaks every run of that workflow, so the set of
    places that have to be kept current should be exactly one.
    """
    offenders = {
        stem: pins
        for stem, text in _workflow_texts().items()
        if (pins := _model_pins(text))
    }

    new = {
        stem: pins
        for stem, pins in offenders.items()
        if stem not in UNMIGRATED_MODEL_PINS
    }
    assert not new, "pinned model found (should use AGENT_MODEL):\n" + "\n".join(
        f"{stem}: {line}" for stem, pins in new.items() for line in pins
    )

    stale = UNMIGRATED_MODEL_PINS - set(offenders)
    assert not stale, (
        "these workflows no longer pin a model; drop them from "
        f"UNMIGRATED_MODEL_PINS: {sorted(stale)}"
    )


def test_managed_workflows_use_the_resolver_action():
    """Every workflow in agent-config.yaml must actually source its model from
    the config: single-model workflows `uses:` the composite action; matrix
    workflows instead call the resolver script from a setup job."""
    config = yaml.safe_load(CONFIG_PATH.read_text())
    texts = _workflow_texts()
    for stem, entry in config["workflows"].items():
        text = texts.get(stem, "")
        if isinstance(entry, dict) and entry.get("matrix"):
            assert (
                "resolve-agent-config/resolve_agent_config.py" in text
                and "--matrix" in text
            ), f"matrix workflow '{stem}' does not emit its matrix from the config"
        else:
            assert "uses: ./.github/actions/resolve-agent-config" in text, (
                f"workflow '{stem}' is in agent-config.yaml but does not `uses:` "
                f"the resolve-agent-config action"
            )


# The SHA these input/output sets were read from. If a workflow bumps the pin,
# the sets below may no longer describe the action —
# test_claude_action_pin_matches_the_recorded_sets fails so the bump comes with
# a refresh rather than silently invalidating both guards.
CLAUDE_ACTION_PINNED_SHA = "be7b93b1907a4abad570368f3c74b6fe3807510b"

# Inputs declared by anthropics/claude-code-action at that SHA. Refresh with:
#   gh api "/repos/anthropics/claude-code-action/contents/action.yml?ref=<sha>" \
#     --jq .content | base64 -d | python3 -c \
#     "import sys,yaml;print(sorted(yaml.safe_load(sys.stdin)['inputs']))"
# The v0 names `mode`, `direct_prompt`, `model`, `mcp_config`, `allowed_tools`
# and `custom_instructions` are NOT here. GitHub only warns about an unexpected
# input, so passing one silently drops it — arba-issue-monitor never delivered
# its prompt and claude.yml never applied its model, MCP servers or tool
# allowlist, both for months, both green the whole time.
CLAUDE_ACTION_V1_INPUTS = {
    "additional_permissions", "allowed_bots", "allowed_non_write_users",
    "anthropic_api_key", "anthropic_federation_rule_id", "anthropic_oidc_audience",
    "anthropic_organization_id", "anthropic_service_account_id",
    "anthropic_workspace_id", "assignee_trigger", "base_branch", "bot_id",
    "bot_name", "branch_name_template", "branch_prefix",
    "classify_inline_comments", "claude_args", "claude_code_oauth_token",
    "display_report", "exclude_comments_by_actor", "github_token",
    "include_comments_by_actor", "include_fix_links", "label_trigger",
    "path_to_bun_executable", "path_to_claude_code_executable",
    "plugin_marketplaces", "plugins", "prompt", "settings", "show_full_output",
    "ssh_signing_key", "track_progress", "trigger_phrase", "use_bedrock",
    "use_commit_signing", "use_foundry", "use_sticky_comment", "use_vertex",
}

# Outputs it declares. Notably there is no `result`: workflows that wrote
# `${{ steps.<id>.outputs.result }}` were emitting an empty string, which is why
# run reports go through .github/actions/agent-run-summary instead.
CLAUDE_ACTION_V1_OUTPUTS = {
    "branch_name", "execution_file", "github_token", "session_id",
    "structured_output",
}


def _action_definition_files():
    """Every file that can invoke an action: workflows and composite actions."""
    # Everything under .github/ that can declare steps. Deliberately broad: a
    # step file in an unexpected place (.github/copilot-setup-steps.yml) is
    # exactly the kind of thing a narrower glob misses. Files with no steps —
    # agent-config.yaml, cron-profiles.yaml, dependabot.yml — simply yield none.
    return sorted((REPO_ROOT / ".github").rglob("*.y*ml"))


def _definition_name(path: Path) -> str:
    """A composite action is named by its directory, a workflow by its stem."""
    return path.parent.name if path.stem == "action" else path.stem


def _steps(doc: dict):
    """Yield steps from a workflow (jobs.*.steps) or a composite action (runs.steps)."""
    for job in (doc.get("jobs") or {}).values():
        yield from (job or {}).get("steps") or []
    yield from ((doc.get("runs") or {}).get("steps") or [])


def _claude_action_steps():
    """Yield (file stem, step mapping) for every claude-code-action step."""
    for path in _action_definition_files():
        doc = yaml.safe_load(path.read_text()) or {}
        for step in _steps(doc):
            if ((step or {}).get("uses") or "").startswith(
                "anthropics/claude-code-action@"
            ):
                yield _definition_name(path), step


def test_no_workflow_passes_an_undeclared_input_to_claude_code_action():
    offenders = []
    for stem, step in _claude_action_steps():
        for key in (step.get("with") or {}):
            if key not in CLAUDE_ACTION_V1_INPUTS:
                offenders.append(f"{stem}: with.{key}")
    assert not offenders, (
        "input(s) not declared by the pinned claude-code-action; GitHub only "
        "warns, so these are silently dropped:\n" + "\n".join(offenders)
    )


def test_no_workflow_reads_an_undeclared_claude_code_action_output():
    """`steps.<id>.outputs.result` does not exist; it renders as empty."""
    offenders = []
    for path in _action_definition_files():
        doc = yaml.safe_load(path.read_text()) or {}
        ids = {
            step.get("id")
            for step in _steps(doc)
            if (step or {}).get("uses", "").startswith("anthropics/claude-code-action@")
        }
        text = path.read_text()
        for step_id in filter(None, ids):
            for ref in re.findall(
                rf"steps\.{re.escape(step_id)}\.outputs\.([A-Za-z_][A-Za-z0-9_]*)", text
            ):
                if ref not in CLAUDE_ACTION_V1_OUTPUTS:
                    offenders.append(f"{path.stem}: steps.{step_id}.outputs.{ref}")
    assert not offenders, (
        "claude-code-action output(s) that do not exist (these expand to an "
        "empty string):\n" + "\n".join(offenders)
    )


def test_every_claude_code_action_workflow_is_in_the_agent_config():
    """The reverse of test_managed_workflows_use_the_resolver_action.

    An empty pin-allowlist does not by itself mean every agent is centrally
    modelled: a workflow that pins no model AND is absent from the config is
    invisible to both other tests.
    """
    config = yaml.safe_load(CONFIG_PATH.read_text())
    managed = set(config["workflows"])
    # Only workflows: agent-config keys are workflow stems, and
    # test_every_config_workflow_file_exists requires a matching workflow file,
    # so a composite action must not be demanded as a config key.
    workflow_stems = {p.stem for p in WORKFLOW_DIR.glob("*.y*ml")}
    using = {stem for stem, _ in _claude_action_steps()} & workflow_stems
    assert not (using - managed), (
        "workflow(s) run claude-code-action but are not in agent-config.yaml, so "
        f"their model is not centrally configured: {sorted(using - managed)}"
    )


def test_claude_action_pin_matches_the_recorded_sets():
    """Every workflow must pin the SHA the input/output sets were read from.

    The two guards above are only as good as their hardcoded vocabulary. Tying
    them to the pin means bumping the action forces a deliberate refresh instead
    of quietly turning both tests into no-ops.
    """
    pins = set()
    for path in _action_definition_files():
        pins.update(
            re.findall(r"anthropics/claude-code-action@([0-9a-f]{40})", path.read_text())
        )
    unexpected = pins - {CLAUDE_ACTION_PINNED_SHA}
    assert not unexpected, (
        "claude-code-action is pinned to a SHA the recorded input/output sets "
        f"were not read from: {sorted(unexpected)}. Re-read them from that SHA "
        "and update CLAUDE_ACTION_PINNED_SHA."
    )


def test_claude_code_action_is_always_sha_pinned():
    """A moved tag could swap in code that exfiltrates the App token."""
    floating = []
    for path in _action_definition_files():
        for ref in re.findall(r"anthropics/claude-code-action@(\S+)", path.read_text()):
            if not re.fullmatch(r"[0-9a-f]{40}", ref):
                floating.append(f"{path.stem}: @{ref}")
    assert not floating, "claude-code-action must be SHA-pinned:\n" + "\n".join(floating)


def test_every_checkout_is_non_persisting():
    """No `actions/checkout` anywhere under .github/ may leave a token on disk.

    `actions/checkout` writes an HTTP Basic `extraheader` into `.git/config`
    unless told not to, which is the exact path by which the PAT was read out of
    a runner and disclosed. A per-FILE grep is not enough — it passes a file
    with two checkouts where only one is flagged, and it misses composite
    actions entirely, which is how a second token-persisting checkout survived
    inside claude-issue-{summarize,triage}-action.
    """
    offenders = []
    for path in _action_definition_files():
        doc = yaml.safe_load(path.read_text()) or {}
        for i, step in enumerate(_steps(doc)):
            uses = (step or {}).get("uses") or ""
            if not uses.startswith("actions/checkout@"):
                continue
            with_ = (step or {}).get("with") or {}
            if with_.get("persist-credentials") not in (False, "false"):
                name = (step or {}).get("name") or f"step {i}"
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {name}")
    assert not offenders, (
        "checkout(s) that persist credentials into .git/config:\n"
        + "\n".join(offenders)
    )


def test_no_action_manifest_field_contains_a_github_expression():
    """`action.yml` manifest fields are template-evaluated when the action loads.

    A GitHub expression outside `runs:` — even an illustrative one inside a
    `description:` — is parsed for real. `steps` is not a valid manifest context,
    so the action fails to load with "Unrecognized named-value: 'steps'" and
    every workflow that uses it hard-fails. This is exactly how
    agent-run-summary shipped broken: the prose explaining the bug it fixes
    contained the expression it was warning about, which took down the summary
    step in seven workflows at once.

    Expressions inside `runs.steps` are fine — those are evaluated at run time
    with a real context — so only the manifest-level fields are checked.
    """
    offenders = []
    for path in (REPO_ROOT / ".github" / "actions").rglob("action.y*ml"):
        doc = yaml.safe_load(path.read_text()) or {}
        fields = {
            "name": doc.get("name"),
            "description": doc.get("description"),
        }
        for section in ("inputs", "outputs"):
            for key, spec in (doc.get(section) or {}).items():
                for sub in ("description", "default"):
                    fields[f"{section}.{key}.{sub}"] = (spec or {}).get(sub)
        for field, value in fields.items():
            if isinstance(value, str) and "${{" in value:
                offenders.append(f"{path.relative_to(REPO_ROOT)}: {field}")
    assert not offenders, (
        "GitHub expression in an action manifest field; it is evaluated at load "
        "time and will break the action:\n" + "\n".join(offenders)
    )
