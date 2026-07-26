"""Tests for the cron-cadence profile applier.

The applier does a surgical, line-based rewrite of each managed workflow's
``on.schedule`` block rather than round-tripping the YAML — GitHub's ``on:`` key
parses as the YAML 1.1 boolean ``True``, which a naive re-dump corrupts. These
tests pin the three cases that matters: replace, remove, and re-insert.
"""

from pathlib import Path

import pytest
import yaml

from scripts.apply_cron_profile import (
    DEFAULT_CONFIG,
    load_config,
    resolve_workflow_file,
    rewrite_schedule,
)


def test_rewrite_schedule_replaces_existing_schedule_entries():
    original = """name: Demo

on:
  schedule:
    - cron: "0 0 30 2 *"  # old
  workflow_dispatch:
    inputs:
      note:
        type: string
"""

    updated = rewrite_schedule(
        original,
        [
            {"cron": "0 */4 * * 1-5", "comment": "weekday"},
            {"cron": "0 */8 * * 0,6", "comment": "weekend"},
        ],
        wf_name="demo",
    )

    assert '    - cron: "0 */4 * * 1-5"  # weekday' in updated
    assert '    - cron: "0 */8 * * 0,6"  # weekend' in updated
    assert "workflow_dispatch:" in updated
    assert "0 0 30 2 *" not in updated


def test_rewrite_schedule_removes_schedule_block_for_empty_entries():
    original = """name: Demo

on:
  schedule:
    - cron: "37 * * * *"  # hourly
  workflow_dispatch:
    inputs:
      note:
        type: string
"""

    updated = rewrite_schedule(original, [], wf_name="demo")

    assert "schedule:" not in updated
    assert "cron:" not in updated
    assert "workflow_dispatch:" in updated
    assert "inputs:" in updated


def test_rewrite_schedule_inserts_schedule_block_when_reenabling():
    original = """name: Demo

on:
  workflow_dispatch:
    inputs:
      note:
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
"""

    updated = rewrite_schedule(
        original,
        [{"cron": "37 * * * *", "comment": "hourly"}],
        wf_name="demo",
    )

    assert (
        """on:
  schedule:
    - cron: "37 * * * *"  # hourly
  workflow_dispatch:
"""
        in updated
    )
    assert "jobs:" in updated


def test_repo_config_is_valid_and_every_managed_workflow_exists():
    """The committed profile config must load and name only real workflows."""
    config = load_config(DEFAULT_CONFIG)
    for profile in config["profiles"].values():
        for stem in profile["workflows"]:
            assert resolve_workflow_file(stem).exists()


def test_active_profile_matches_the_committed_workflow_schedules():
    """Applying the active profile must be a no-op.

    If someone hand-edits a `cron:` line instead of going through a profile, the
    committed workflows drift from the config and the next `just cron-profile`
    silently reverts them. Catch that here instead.
    """
    config = load_config(DEFAULT_CONFIG)
    active = str(config["active"])
    for stem, entries in config["profiles"][active]["workflows"].items():
        path = resolve_workflow_file(stem)
        original = path.read_text()
        assert rewrite_schedule(original, entries, wf_name=stem) == original, (
            f"{path.name} has drifted from the '{active}' cron profile; "
            f"run `just cron-profile {active}`"
        )


def test_off_profile_removes_every_schedule():
    config = load_config(DEFAULT_CONFIG)
    for stem, entries in config["profiles"]["off"]["workflows"].items():
        assert entries == []
        updated = rewrite_schedule(
            resolve_workflow_file(stem).read_text(), entries, wf_name=stem
        )
        assert "cron:" not in updated
        # ... and the workflow must still be valid YAML with a dispatch trigger.
        parsed = yaml.safe_load(updated)
        # `on:` parses as the YAML 1.1 boolean True.
        triggers = parsed[True]
        assert "workflow_dispatch" in triggers


def test_main_ci_workflow_is_not_managed():
    """main.yaml's weekly re-validation is CI, not an agent; `off` must not
    disable it."""
    config = load_config(DEFAULT_CONFIG)
    for profile in config["profiles"].values():
        assert "main" not in profile["workflows"]
    assert "cron:" in (Path(".github/workflows/main.yaml")).read_text()


def test_off_then_back_round_trips_every_managed_workflow():
    """`off` must be reversible for every managed workflow, byte for byte.

    The kill switch removes the `on.schedule` block; restoring a profile has to
    take the *insert* path, which is only reachable if `on:` is recognised. It
    was not for workflows written as `on:  # yamllint disable-line rule:truthy`
    (warm-reference-cache, main, deploy-docs), so `off` was one-way for those —
    and because writes happened inside the apply loop, a failure part-way left
    the other workflows rewritten with a stale `active:`. The synthetic bare
    `on:` in the insert test above cannot catch this; the committed files can.
    """
    config = load_config(DEFAULT_CONFIG)
    active = str(config["active"])
    for stem, entries in config["profiles"][active]["workflows"].items():
        path = resolve_workflow_file(stem)
        original = path.read_text()
        disabled = rewrite_schedule(original, [], wf_name=stem)
        assert "cron:" not in disabled, f"{path.name} still scheduled after off"
        restored = rewrite_schedule(disabled, entries, wf_name=stem)
        assert restored == original, (
            f"{path.name} does not survive off -> {active}; the kill switch is "
            f"one-way for it"
        )


def test_on_key_is_recognised_with_a_trailing_comment():
    """The yamllint-pragma form is what broke the insert path."""
    original = """name: Demo

on:  # yamllint disable-line rule:truthy
  workflow_dispatch:
"""
    updated = rewrite_schedule(
        original, [{"cron": "0 4 * * 1", "comment": "weekly"}], wf_name="demo"
    )
    assert '    - cron: "0 4 * * 1"  # weekly' in updated
    assert "# yamllint disable-line rule:truthy" in updated


def test_apply_is_atomic_when_one_workflow_cannot_be_rewritten(tmp_path, monkeypatch):
    """A failure part-way must not leave other workflows rewritten."""
    import scripts.apply_cron_profile as mod

    config = load_config(DEFAULT_CONFIG)
    active = str(config["active"])
    stems = list(config["profiles"][active]["workflows"])
    before = {s: resolve_workflow_file(s).read_text() for s in stems}

    real = mod.rewrite_schedule

    def explode(text, entries, *, wf_name):
        if wf_name == stems[-1]:
            raise mod.ConfigError("simulated failure")
        # force a change so the earlier files would be written if not atomic
        return real(text, [], wf_name=wf_name)

    monkeypatch.setattr(mod, "rewrite_schedule", explode)
    with pytest.raises(SystemExit):
        mod.main([active])

    for stem in stems:
        assert resolve_workflow_file(stem).read_text() == before[stem], (
            f"{stem} was modified despite a failure on {stems[-1]}"
        )
