"""Verify the lint successor without rewriting historical release manifests."""

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "module-final-source-closure-20261107"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def normalized_ast(text):
    tree = ast.parse(text)
    body = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name != "csv":
                    body.append(ast.Import(names=[alias]))
        else:
            body.append(node)
    tree.body = body
    return ast.dump(tree, include_attributes=False)


def main():
    changes = read(HERE / "successor.json")["scripts"]
    allowed = {}
    for row in changes:
        old = ROOT / row["original_archive"]
        new = ROOT / row["path"]
        assert digest(old) == row["before_sha256"]
        assert digest(new) == row["after_sha256"]
        assert normalized_ast(old.read_text()) == normalized_ast(new.read_text())
        allowed[row["path"]] = row

    checked = 0
    for manifest in (PRIOR / "inputs.json", PRIOR / "handoff.json"):
        values = read(manifest)
        if manifest.name == "handoff.json":
            values = values["files"]
        for name, expected in values.items():
            if name in allowed:
                row = allowed[name]
                assert expected == row["before_sha256"], name
                target = ROOT / row["original_archive"]
            else:
                target = ROOT / name
            assert digest(target) == expected, name
            checked += 1
    for row in read(PRIOR / "release-preservation.json"):
        name = row["archive_if_superseded"] or row["path"]
        if name in allowed:
            name = allowed[name]["original_archive"]
        assert digest(ROOT / name) == row["expected"], name
        checked += 1
    print(
        json.dumps(
            {
                "result": "PASS",
                "historical_hash_entries_verified": checked,
                "helper_successors": len(changes),
                "scientific_inputs_unchanged": True,
                "prior_handoff_sha256": digest(PRIOR / "handoff.json"),
                "successor_sha256": digest(HERE / "successor.json"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
