"""Build per-gene sandboxes for the AGENT_REVIEW condition of a benchmark.

Each sandbox is a self-contained folder, outside the repository, holding only
what was knowable at the benchmark's baseline date:

- ``genes/<org>/<GENE>/<GENE>-goa.tsv``: the baseline-release GOA rows exported
  by ``ai-gene-review benchmark export`` (target annotations are absent);
- ``genes/<org>/<GENE>/<GENE>-uniprot.txt``: the UniProt entry version that was
  current at the baseline date, from UniSave;
- ``genes/<org>/<GENE>/<GENE>-ai-review.yaml``: a stub seeded from the baseline
  GOA with ``ai-gene-review seed-goa``;
- ``publications/``: cached papers cited by the baseline GOA whose publication
  year is before the baseline year;
- ``.claude/skills/sequence-read``: the sequence-read skill;
- ``tools/``: offline GO term lookup and the residue checker.

Usage::

    uv run python projects/SEQFUN_BENCHMARK/scripts/agent_review_sandbox.py \\
        benchmarks/human-goa-2025-06/human-goa-2025-06.yaml SANDBOX_ROOT
"""

import csv
import json
import shutil
import subprocess
import urllib.request
from datetime import date, datetime
from pathlib import Path

import typer
import yaml

REPO = Path(__file__).resolve().parents[3]
UNISAVE = "https://rest.uniprot.org/unisave/{acc}"

app = typer.Typer()


def unisave_version_at(acc: str, cutoff: date) -> int:
    """Return the UniProt entry version that was current on ``cutoff``."""
    with urllib.request.urlopen(UNISAVE.format(acc=acc) + "?format=json") as fh:
        versions = json.load(fh)["results"]
    dated = [
        (datetime.strptime(v["firstReleaseDate"], "%d-%b-%Y").date(), v["entryVersion"])
        for v in versions
    ]
    return max((d, v) for d, v in dated if d < cutoff)[1]


def unisave_text(acc: str, version: int) -> str:
    url = UNISAVE.format(acc=acc) + f"?format=txt&versions={version}"
    with urllib.request.urlopen(url) as fh:
        return fh.read().decode()


def cited_pmids(goa: Path) -> set[str]:
    """PMIDs in the REFERENCE column of a GOA TSV.

    >>> import tempfile
    >>> p = Path(tempfile.mkdtemp()) / "x.tsv"
    >>> _ = p.write_text("GO TERM\\tREFERENCE\\nGO:1\\tPMID:12|GO_REF:1\\n")
    >>> sorted(cited_pmids(p))
    ['12']
    """
    with goa.open(newline="") as fh:
        return {
            ref.split(":", 1)[1]
            for row in csv.DictReader(fh, delimiter="\t")
            for ref in row["REFERENCE"].split("|")
            if ref.startswith("PMID:")
        }


def pub_year(path: Path) -> int | None:
    meta = yaml.safe_load(path.read_text().split("---")[1])
    year = str(meta.get("year") or "")[:4]
    return int(year) if year.isdigit() else None


@app.command()
def main(
    benchmark_file: Path,
    sandbox_root: Path,
    organism: str = "human",
    only: list[str] = typer.Option([], help="Gene symbols to build (default all)."),
) -> None:
    benchmark = yaml.safe_load(benchmark_file.read_text())
    baseline = date.fromisoformat(str(benchmark["spec"]["baseline_release"]))
    run_inputs = benchmark_file.parent / "run-inputs" / "baseline-goa"
    manifest = []
    for item in benchmark["items"]:
        gene = item["gene_symbol"]
        if only and gene not in only:
            continue
        acc = item["protein"].split(":", 1)[1]
        box = sandbox_root / gene
        gdir = box / "genes" / organism / gene
        gdir.mkdir(parents=True, exist_ok=True)
        goa = gdir / f"{gene}-goa.tsv"
        shutil.copy(run_inputs / f"{acc}-goa.tsv", goa)
        version = unisave_version_at(acc, baseline)
        (gdir / f"{gene}-uniprot.txt").write_text(unisave_text(acc, version))
        review = gdir / f"{gene}-ai-review.yaml"
        if not review.exists():
            review.write_text(
                yaml.safe_dump(
                    {
                        "id": acc,
                        "gene_symbol": gene,
                        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
                        "description": "TODO",
                    },
                    sort_keys=False,
                )
            )
            subprocess.run(
                [
                    "uv",
                    "run",
                    "ai-gene-review",
                    "seed-goa",
                    str(review),
                    "--goa",
                    str(goa),
                    "--no-fetch-titles",
                ],
                cwd=REPO,
                check=True,
                capture_output=True,
            )
        pubs = box / "publications"
        pubs.mkdir(exist_ok=True)
        kept = []
        for pmid in sorted(cited_pmids(goa)):
            src = REPO / "publications" / f"PMID_{pmid}.md"
            year = pub_year(src) if src.exists() else None
            if year is not None and year < baseline.year:
                shutil.copy(src, pubs / src.name)
                kept.append(pmid)
        skill = box / ".claude" / "skills" / "sequence-read"
        if not skill.exists():
            shutil.copytree(REPO / ".claude" / "skills" / "sequence-read", skill)
        tools = box / "tools"
        tools.mkdir(exist_ok=True)
        for tool in ("go_term.py", "residues.sh"):
            shutil.copy(Path(__file__).parent / tool, tools / tool)
        manifest.append(
            {
                "gene": gene,
                "accession": acc,
                "uniprot_entry_version": version,
                "publications_copied": len(kept),
                "cited_pmids": len(cited_pmids(goa)),
            }
        )
        typer.echo(f"{gene} {acc} v{version} pubs {len(kept)}/{len(cited_pmids(goa))}")
    (sandbox_root / "sandbox-manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False)
    )


if __name__ == "__main__":
    app()
