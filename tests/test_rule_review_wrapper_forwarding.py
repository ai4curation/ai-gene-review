"""End-to-end tests for rule-review wrapper argument forwarding."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
RENDER_RULE_CODE = (
    "import sys; from pathlib import Path; "
    "from ai_gene_review.etl.rule_analysis import render_rule_review_html; "
    "render_rule_review_html(sys.argv[1], Path(sys.argv[2]))"
)


def write_enriched_rule(cache_dir: Path, rule_id: str) -> Path:
    rule_dir = cache_dir / rule_id
    rule_dir.mkdir(parents=True)
    (rule_dir / f"{rule_id}.enriched.json").write_text(
        json.dumps(
            {
                "rule_set": {"condition_sets": [], "annotations": []},
                "reviewed_protein_count": 0,
                "unreviewed_protein_count": 0,
            }
        )
    )
    return rule_dir


def run_just(
    *args: str,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(extra_env or {})
    return subprocess.run(
        ["just", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=120,
    )


def test_init_rule_review_wrapper_uses_custom_cache_dir(tmp_path: Path) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "rule cache (draft), v1?"
    rule_dir = write_enriched_rule(cache_dir, rule_id)

    result = run_just(
        "init-rule-review",
        rule_id,
        "--cache-dir",
        str(cache_dir),
    )

    assert result.returncode == 0, result.stderr
    review_path = rule_dir / f"{rule_id}-review.yaml"
    review = yaml.safe_load(review_path.read_text())
    assert review["id"] == rule_id
    assert review["rule_type"] == "ARBA"
    assert f"just analyze-rule {rule_id}" in result.stdout
    assert f"just sync-rule-review-single {rule_id}" in result.stdout
    assert f"just render-rule {rule_id}" in result.stdout


def test_init_unirule_omits_unsupported_analysis_next_steps(tmp_path: Path) -> None:
    rule_id = "UR000000070"
    cache_dir = tmp_path / "unirule cache"
    rule_dir = write_enriched_rule(cache_dir, rule_id)

    result = run_just(
        "init-rule-review",
        rule_id,
        "--cache-dir",
        str(cache_dir),
    )

    assert result.returncode == 0, result.stderr
    review = yaml.safe_load((rule_dir / f"{rule_id}-review.yaml").read_text())
    assert review["rule_type"] == "UniRule"
    assert "rules-deep-research-perplexity" in result.stdout
    assert "currently support ARBA IDs only" in result.stdout
    assert "analyze-rule" not in result.stdout
    assert "sync-rule-review-single" not in result.stdout
    assert "render-rule" not in result.stdout


def test_init_rule_review_wrapper_forwards_no_empty_tail(tmp_path: Path) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["RULE_WRAPPER_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    log_path = tmp_path / "argv log.json"
    env = {
        "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
        "RULE_WRAPPER_ARGV_LOG": str(log_path),
    }
    result = run_just(
        "init-rule-review",
        "ARBA00026249",
        extra_env=env,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "ai-gene-review",
        "init-rule-review",
        "ARBA00026249",
    ]


def seed_analysis_outputs(cache_dir: Path, rule_id: str) -> None:
    rule_dir = write_enriched_rule(cache_dir, rule_id)
    (rule_dir / f"{rule_id}-analysis.yaml").write_text("analysis: present\n")
    (rule_dir / f"{rule_id}-review.yaml").write_text(
        f"id: {rule_id}\nrule_type: ARBA\nentries: []\n"
    )


def install_recording_uv(tmp_path: Path) -> tuple[Path, Path]:
    fake_bin = tmp_path / "recording bin"
    fake_bin.mkdir()
    log_path = tmp_path / "uv argv.jsonl"
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

args = sys.argv[1:]
with Path(os.environ["RULE_WRAPPER_ARGV_LOG"]).open("a") as handle:
    handle.write(json.dumps(args) + "\\n")

if "examples/rule_analysis_demo.py" in args and "--output-dir" in args:
    rule_id = args[args.index("examples/rule_analysis_demo.py") + 1]
    output_dir = Path(args[args.index("--output-dir") + 1])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"{rule_id}-analysis.txt").write_text("fake report\\n")
"""
    )
    fake_uv.chmod(0o755)
    return fake_bin, log_path


def run_isolated_just(
    working_directory: Path,
    fake_bin: Path,
    log_path: Path,
    *args: str,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(
        {
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_WRAPPER_ARGV_LOG": str(log_path),
            "JUST_JUSTFILE": str(REPO_ROOT / "justfile"),
            "JUST_WORKING_DIRECTORY": str(working_directory),
        }
    )
    env.update(extra_env or {})
    return subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(working_directory),
            *args,
        ],
        cwd=working_directory,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )


def read_argv_log(log_path: Path) -> list[list[str]]:
    return [json.loads(line) for line in log_path.read_text().splitlines()]


@pytest.mark.parametrize("recipe", ["render-rule", "sync-rule-review-single"])
def test_rule_wrapper_analysis_dependency_uses_custom_cache(
    tmp_path: Path,
    recipe: str,
) -> None:
    rule_id = "ARBA00026249"
    working_directory = tmp_path / "isolated working directory"
    working_directory.mkdir()
    cache_dir = working_directory / "custom cache"
    seed_analysis_outputs(cache_dir, rule_id)
    fake_bin, log_path = install_recording_uv(tmp_path)

    result = run_isolated_just(
        working_directory,
        fake_bin,
        log_path,
        recipe,
        rule_id,
        "custom cache",
    )

    assert result.returncode == 0, result.stderr
    assert "skipping expensive rebuild" in result.stdout
    invocations = read_argv_log(log_path)
    assert not any("examples/rule_analysis_demo.py" in argv for argv in invocations)
    assert not (working_directory / "rules" / "arba" / rule_id).exists()
    if recipe == "render-rule":
        assert invocations == [
            [
                "run",
                "python",
                "-c",
                RENDER_RULE_CODE,
                rule_id,
                "custom cache",
            ]
        ]
    else:
        assert invocations == [
            [
                "run",
                "ai-gene-review",
                "rules-sync",
                f"custom cache/{rule_id}/{rule_id}-review.yaml",
            ]
        ]


def test_render_all_rules_analysis_dependency_uses_custom_cache(
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    working_directory = tmp_path / "isolated working directory"
    working_directory.mkdir()
    cache_dir = working_directory / "custom-cache"
    seed_analysis_outputs(cache_dir, rule_id)
    fake_bin, log_path = install_recording_uv(tmp_path)

    result = run_isolated_just(
        working_directory,
        fake_bin,
        log_path,
        "render-all-rules",
        "custom-cache",
    )

    assert result.returncode == 0, result.stderr
    assert "Rendered 1 rule reviews" in result.stdout
    invocations = read_argv_log(log_path)
    assert not any("examples/rule_analysis_demo.py" in argv for argv in invocations)
    render_invocations = [argv for argv in invocations if argv[:3] == ["run", "python", "-c"]]
    assert len(render_invocations) == 1
    assert not (working_directory / "rules" / "arba" / rule_id).exists()


def test_sync_rule_review_single_preserves_default_cache_argument(
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    working_directory = tmp_path / "isolated working directory"
    working_directory.mkdir()
    seed_analysis_outputs(working_directory / "rules" / "arba", rule_id)
    fake_bin, log_path = install_recording_uv(tmp_path)

    result = run_isolated_just(
        working_directory,
        fake_bin,
        log_path,
        "sync-rule-review-single",
        rule_id,
    )

    assert result.returncode == 0, result.stderr
    assert read_argv_log(log_path) == [
        [
            "run",
            "ai-gene-review",
            "rules-sync",
            f"rules/arba/{rule_id}/{rule_id}-review.yaml",
        ]
    ]


@pytest.mark.parametrize(
    ("cache_name", "extra_env"),
    [
        ("rules/arba", {}),
        ("custom $RULE_RENDER_CACHE_TOKEN", {"RULE_RENDER_CACHE_TOKEN": "expanded"}),
    ],
)
def test_render_rule_passes_cache_as_opaque_argument(
    tmp_path: Path,
    cache_name: str,
    extra_env: dict[str, str],
) -> None:
    rule_id = "ARBA00026249"
    working_directory = tmp_path / "isolated working directory"
    working_directory.mkdir()
    seed_analysis_outputs(working_directory / cache_name, rule_id)
    fake_bin, log_path = install_recording_uv(tmp_path)

    recipe_args = ["render-rule", rule_id]
    if cache_name != "rules/arba":
        recipe_args.append(cache_name)
    result = run_isolated_just(
        working_directory,
        fake_bin,
        log_path,
        *recipe_args,
        extra_env=extra_env,
    )

    assert result.returncode == 0, result.stderr
    assert read_argv_log(log_path) == [
        ["run", "python", "-c", RENDER_RULE_CODE, rule_id, cache_name]
    ]
