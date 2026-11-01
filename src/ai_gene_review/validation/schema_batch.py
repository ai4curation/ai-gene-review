"""Batch LinkML schema validation with libyaml input parsing.

Validation remains LinkML's closed JSON Schema plugin. Only the YAML scanner
changes; source filenames, multi-document/list inputs and error exit status are
retained. Strict duplicate-key checks remain a separate CI check, as before.
"""

from collections.abc import Iterator
from pathlib import Path
from typing import Any

import click
import yaml
from linkml.validator import Validator
from linkml.validator.loaders import YamlLoader
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from ai_gene_review.yaml_utils import SafeLoader


class FastYamlLoader(YamlLoader):
    """LinkML's YAML instance boundaries, parsed by PyYAML's safe C loader."""

    def iter_instances(self) -> Iterator[Any]:
        with open(self.source) as stream:
            for document in yaml.load_all(stream, Loader=SafeLoader):
                if isinstance(document, list):
                    yield from document
                else:
                    yield document


@click.command()
@click.option("-s", "--schema", type=click.Path(path_type=Path), required=True)
@click.option("-C", "--target-class", required=True)
@click.argument("files", nargs=-1, type=click.Path(path_type=Path), required=True)
def cli(schema: Path, target_class: str, files: tuple[Path, ...]) -> int:
    """Validate FILES with LinkML's closed schema and safe libyaml parsing."""
    validator = Validator(
        schema, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    issues = 0
    failed = False
    for path in files:
        for result in validator.iter_results_from_source(FastYamlLoader(path), target_class):
            issues += 1
            failed |= result.severity == Severity.ERROR
            print(f"[{result.severity.value}] [{path}/{result.instance_index}] {result.message}")
    if not issues:
        print("No issues found")
    return int(failed)


def main(argv: list[str] | None = None) -> int:
    return cli.main(args=argv, standalone_mode=False)


if __name__ == "__main__":
    raise SystemExit(main())
