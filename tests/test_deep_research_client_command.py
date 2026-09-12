"""Regression coverage for tool interpreter selection (issue #2977)."""

import importlib
from pathlib import Path

import pytest


@pytest.fixture(params=[
    "deep_research_wrapper",
    "module_deep_research_wrapper",
    "module_pathway_taxon_deep_research_wrapper",
])
def wrapper(request, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "scripts"))
    monkeypatch.delenv("DEEP_RESEARCH_CLIENT_CMD", raising=False)
    monkeypatch.delenv("DEEP_RESEARCH_CLIENT_UVX_FROM", raising=False)
    return importlib.import_module(request.param)


def test_uvx_selects_supported_python_despite_ambient_default(wrapper, monkeypatch):
    monkeypatch.setenv("UV_PYTHON", "3.11")

    cmd = wrapper.deep_research_client_command()

    assert cmd[0] == "uvx"
    assert cmd[cmd.index("--python") + 1] == "3.12"
    assert cmd[-1] == "deep-research-client"


def test_package_override_preserves_interpreter_selection(wrapper, monkeypatch):
    monkeypatch.setenv("DEEP_RESEARCH_CLIENT_UVX_FROM", "custom-client-package")

    cmd = wrapper.deep_research_client_command()

    assert cmd[cmd.index("--from") + 1] == "custom-client-package"
    assert cmd[cmd.index("--python") + 1] == "3.12"


def test_custom_command_controls_its_own_interpreter(wrapper, monkeypatch):
    monkeypatch.setenv(
        "DEEP_RESEARCH_CLIENT_CMD", '"/custom path/python" -m deep_research_client'
    )

    assert wrapper.deep_research_client_command() == [
        "/custom path/python", "-m", "deep_research_client"
    ]
