"""Fast parsing must preserve LinkML's validation and instance boundaries."""

from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner
from linkml.validator.cli import cli
from linkml.validator.loaders import YamlLoader

from ai_gene_review.validation.schema_batch import FastYamlLoader, main
from ai_gene_review.yaml_utils import safe_load


@pytest.fixture
def schema(tmp_path):
    path = tmp_path / "schema.yaml"
    path.write_text("""id: https://example.org/test
name: example
prefixes:
  linkml: https://w3id.org/linkml/
imports: [linkml:types]
classes:
  Record:
    attributes:
      id:
        range: string
        required: true
      score:
        range: integer
        minimum_value: 0
""")
    return path


@pytest.mark.parametrize("content", [
    "id: valid\nscore: 2\n",
    "id: invalid\nscore: -1\n",
    "score: 2\n",
    "id: invalid\nunknown: disallowed\n",
    "- {id: valid}\n- {id: invalid, score: -1}\n",
    "id: first\n---\nid: second\nscore: -1\n",
    "id: duplicate\nscore: -1\nscore: 2\n",
    "- &record {id: αβ, score: 1}\n- *record\n",
    "null\n",
    "[]\n",
])
def test_same_diagnostics_and_exit_as_linkml(tmp_path, schema, capsys, content):
    source = tmp_path / "review with spaces.yaml"
    source.write_text(content)
    args = ["--schema", str(schema), "--target-class", "Record", str(source)]
    old = CliRunner().invoke(cli, args)
    code = main(args)
    output = capsys.readouterr().out
    assert code == old.exit_code
    assert output == old.output
    assert list(FastYamlLoader(source).iter_instances()) == list(YamlLoader(source).iter_instances())


def test_error_in_second_file_remains_blocking(tmp_path, schema, capsys):
    paths = [tmp_path / f"{n}.yaml" for n in range(3)]
    for path, text in zip(paths, ["id: first", "id: invalid\nscore: -1", "id: last\nextra: bad"]):
        path.write_text(text)
    assert main(["-s", str(schema), "-C", "Record", *map(str, paths)]) == 1
    output = capsys.readouterr().out
    assert str(paths[1]) in output and str(paths[2]) in output


@pytest.mark.parametrize("text", ["id: [unterminated", "!!python/object/apply:builtins.str [1]"])
def test_malformed_and_unsafe_yaml_are_rejected(tmp_path, schema, text):
    path = tmp_path / "bad.yaml"
    path.write_text(text)
    assert CliRunner().invoke(cli, ["-s", str(schema), "-C", "Record", str(path)]).exit_code != 0
    with pytest.raises(yaml.YAMLError):
        main(["-s", str(schema), "-C", "Record", str(path)])
    with pytest.raises(yaml.YAMLError):
        safe_load(text)


def test_safe_constructor_semantics():
    text = """date: 2026-10-12
boolean: yes
octal: 012
null_value: null
base: &base {id: GO:0008150, score: 2}
merged: {<<: *base, score: 3}
unicode: β-catenin
"""
    assert safe_load(text) == yaml.safe_load(text)


def test_queue_and_full_gene_validation_use_fast_schema_loader():
    root = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((root / ".github/workflows/main.yaml").read_text())
    step = next(s for s in workflow["jobs"]["validation"]["steps"] if s.get("name") == "Validate all gene schemas (merge queue)")
    assert "ai_gene_review.validation.schema_batch" in step["run"]
    recipe = (root / "project.justfile").read_text().split("\nvalidate-all:\n", 1)[1].split("\nvalidate-all-summary:", 1)[0]
    assert "ai_gene_review.validation.schema_batch" in recipe
