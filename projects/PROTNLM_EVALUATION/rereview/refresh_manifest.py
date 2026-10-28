"""Refresh the review columns of the ProtNLM2 re-review manifest from the repository.

Each manifest row is keyed by UniProt accession and species directory. This script
finds the review file whose ``id`` is that accession and recomputes ``review`` and
``review_status``, then stamps ``generated_at``. Run it after cohort PRs merge so the
manifest never presents finished genes as pending work.

    uv run python projects/PROTNLM_EVALUATION/rereview/refresh_manifest.py
"""

import datetime
import re
from pathlib import Path

import typer
import yaml

REPO = Path(__file__).resolve().parents[3]
MANIFEST = Path(__file__).with_name("manifest.yaml")
ID_LINE = re.compile(r"^id:\s*(\S+)", re.M)

app = typer.Typer(add_completion=False, help=__doc__)


def review_status(text: str) -> str:
    """Classify a review file's text.

    >>> review_status("id: P1\\ndescription: TODO: Add description for X\\n")
    'stub_or_pending'
    >>> review_status("id: P1\\ndescription: A kinase.\\nexisting_annotations:\\n- review:\\n    action: PENDING\\n")
    'stub_or_pending'
    >>> review_status("id: P1\\ndescription: A kinase.\\nexisting_annotations:\\n- review:\\n    action: ACCEPT\\n")
    'complete'
    """
    if "action: PENDING" in text or re.search(r"^description:\s*'?TODO", text, re.M):
        return "stub_or_pending"
    return "complete"


def index_reviews(repo: Path) -> dict[tuple[str, str], Path]:
    """Map (species dir, UniProt accession) to the review file declaring that id."""
    found: dict[tuple[str, str], Path] = {}
    for path in sorted(repo.glob("genes/*/*/*-ai-review.yaml")):
        head = path.read_text()[:2000]
        m = ID_LINE.search(head)
        if m:
            species = path.parts[-3]
            # Prefer the folder named after the symbol over an accession-suffixed duplicate.
            found.setdefault((species, m.group(1).strip("'\"")), path)
    return found


def refresh(manifest: dict, repo: Path, today: str) -> dict:
    """Recompute ``review``/``review_status`` for every row; returns the updated manifest."""
    reviews = index_reviews(repo)
    for gene in manifest["genes"]:
        path = reviews.get((gene["species"], gene["accession"]))
        if path is None:
            gene["review"] = None
            gene["review_status"] = "missing"
        else:
            gene["review"] = str(path.relative_to(repo))
            gene["review_status"] = review_status(path.read_text())
    manifest["generated_at"] = today
    return manifest


@app.command("refresh")
def refresh_cmd(
    manifest_path: Path = typer.Option(MANIFEST, help="Manifest YAML to update in place"),
    repo: Path = typer.Option(REPO, help="Repository root"),
) -> None:
    """Rewrite the manifest's review columns from the current checkout."""
    data = yaml.safe_load(manifest_path.read_text())
    data = refresh(data, repo, datetime.date.today().isoformat())
    ordered = {k: data[k] for k in ("description", "generated_at", "genes") if k in data}
    ordered.update({k: v for k, v in data.items() if k not in ordered})
    manifest_path.write_text(yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True, width=100))
    counts: dict[str, int] = {}
    for gene in data["genes"]:
        counts[gene["review_status"]] = counts.get(gene["review_status"], 0) + 1
    typer.echo(f"{manifest_path}: {counts}")


if __name__ == "__main__":
    app()
