"""CLI tests for rendering individual module documents."""

from pathlib import Path

from typer.testing import CliRunner

from ai_gene_review.cli import app


runner = CliRunner()


def _stub_renderer(monkeypatch, output_dir: Path):
    rendered: list[Path] = []

    def render_module(module_file: Path, **kwargs):
        rendered.append(module_file)
        return output_dir / f"{module_file.stem}.html", []

    monkeypatch.setattr("ai_gene_review.render_modules.render_module", render_module)
    return rendered


def test_render_modules_accepts_module_stem(tmp_path, monkeypatch):
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    module_file = modules_dir / "example.yaml"
    module_file.write_text("id: MODULE:example\n")
    output_dir = tmp_path / "output"
    rendered = _stub_renderer(monkeypatch, output_dir)

    result = runner.invoke(
        app,
        [
            "render-modules",
            "example",
            "--modules-dir",
            str(modules_dir),
            "--output-dir",
            str(output_dir),
        ],
    )

    assert result.exit_code == 0, result.output
    assert rendered == [module_file]


def test_render_modules_accepts_full_path(tmp_path, monkeypatch):
    module_file = tmp_path / "example.yaml"
    module_file.write_text("id: MODULE:example\n")
    output_dir = tmp_path / "output"
    rendered = _stub_renderer(monkeypatch, output_dir)

    result = runner.invoke(
        app,
        ["render-modules", str(module_file), "--output-dir", str(output_dir)],
    )

    assert result.exit_code == 0, result.output
    assert rendered == [module_file]


def test_render_modules_missing_file_fails(tmp_path):
    result = runner.invoke(
        app,
        [
            "render-modules",
            "missing",
            "--modules-dir",
            str(tmp_path / "modules"),
        ],
    )

    assert result.exit_code == 1
    assert "Error: File not found: missing" in result.output
