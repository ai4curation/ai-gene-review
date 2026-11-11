#!/usr/bin/env python3
"""Map reviewed yeast genes onto curated mutant-phenotype annotations.

Joins the ``genes/SCHPO`` and ``genes/yeast`` reviews to the bulk phenotype
files of PomBase (FYPO-coded, single-locus haploid) and SGD (APO-coded), and
reports, per reviewed gene, how many phenotype rows exist and which of them
are nutrient-utilisation phenotypes (growth on a carbon or nitrogen source).
It also counts the IMP rows in each review and what the review did with them,
since IMP is where knockout phenotypes already enter GO.

Used by ``projects/FUNGAL_PHENOTYPES.md``. Nothing is hardcoded: rerun after
corpus or upstream changes and paste the summary.

    uv run python projects/FUNGAL_PHENOTYPES/scripts/phenotype_overlap.py

Downloads are cached in ``--cache`` (default ``tmp/fungal_phenotypes``, which
is gitignored). Gene folders are joined by the PomBase / SGD cross-reference
in each ``*-uniprot.txt``, not by folder name.
"""

from __future__ import annotations

import argparse
import collections
import csv
import re
import sys
import urllib.request
from pathlib import Path

import yaml

POMBASE_PHAF = (
    "https://www.pombase.org/latest_release/phenotypes_and_genotypes/"
    "pombase_single_locus_haploid_phenotype_annotation.phaf.tsv"
)
FYPO_OBO = "http://purl.obolibrary.org/obo/fypo.obo"
SGD_PHENO = "https://downloads.yeastgenome.org/curation/literature/phenotype_data.tab"

# A phenotype counts as nutrient utilisation if its label names growth on, or
# utilisation of, a carbon or nitrogen source. FYPO encodes the source in the
# term label ("decreased cell population growth on galactose carbon source");
# APO puts it in the observable ("utilization of carbon source: absent") with
# the compound in the chemical column.
NUTRIENT_RE = re.compile(r"(carbon|nitrogen) source", re.I)
# Growth on glucose is the standard medium, so a glucose "carbon source"
# phenotype is really a general growth defect; "normal growth on X" rows are
# negative results. Neither says anything about a specific nutrient pathway.
UNINFORMATIVE_RE = re.compile(r"glucose|^normal ", re.I)


def is_nutrient(label: str) -> bool:
    return bool(NUTRIENT_RE.search(label)) and not UNINFORMATIVE_RE.search(label)


def fetch(url: str, dest: Path) -> Path:
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"downloading {url}", file=sys.stderr)
        urllib.request.urlretrieve(url, dest)
    return dest


def fypo_labels(obo: Path) -> dict[str, str]:
    labels, cur = {}, None
    for line in obo.open():
        if line.startswith("[Term]"):
            cur = None
        elif line.startswith("id: FYPO:"):
            cur = line[4:].strip()
        elif line.startswith("name: ") and cur:
            labels[cur] = line[6:].strip()
    return labels


def xref(uniprot: Path, db: str) -> str | None:
    m = re.search(rf"^DR   {db}; (\S+?);", uniprot.read_text(), re.M)
    return m.group(1) if m else None


def reviewed_genes(root: Path, org: str, db: str) -> dict[str, Path]:
    """Map database id -> gene folder for every review with that xref."""
    out = {}
    for folder in sorted((root / "genes" / org).iterdir()):
        up = folder / f"{folder.name}-uniprot.txt"
        if up.exists() and (gid := xref(up, db)):
            out[gid] = folder
    return out


def imp_actions(folder: Path) -> collections.Counter:
    path = folder / f"{folder.name}-ai-review.yaml"
    c: collections.Counter = collections.Counter()
    if not path.exists():
        return c
    doc = yaml.safe_load(path.read_text()) or {}
    for ann in doc.get("existing_annotations") or []:
        if ann.get("evidence_type") == "IMP":
            c[(ann.get("review") or {}).get("action", "NONE")] += 1
    return c


def pombase_rows(phaf: Path, labels: dict[str, str]):
    with phaf.open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if row[0].startswith("#"):
                continue
            label = labels.get(row[2], row[2])
            yield row[1], label, row[17]


def sgd_rows(tab: Path):
    with tab.open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) < 11:
                continue
            label = row[9]
            if row[10]:
                label = f"{label} [{row[10]}]"
            yield row[3], label, row[4].split("|")[-1]


def summarise(name, genes, rows, writer):
    per_gene = collections.defaultdict(list)
    for gid, label, ref in rows:
        if gid in genes:
            per_gene[gid].append((label, ref))
    n_nutr = 0
    for gid, folder in genes.items():
        phen = per_gene.get(gid, [])
        nutr = sorted({lab for lab, _ in phen if is_nutrient(lab)})
        nutr_refs = sorted({ref for lab, ref in phen if is_nutrient(lab)})
        n_nutr += bool(nutr)
        imp = imp_actions(folder)
        writer.writerow(
            [
                name,
                folder.name,
                gid,
                len(phen),
                len({ref for _, ref in phen}),
                len(nutr),
                "; ".join(nutr),
                "; ".join(nutr_refs),
                sum(imp.values()),
                "; ".join(f"{k}={v}" for k, v in sorted(imp.items())),
            ]
        )
    with_any = sum(1 for g in genes if per_gene.get(g))
    print(
        f"{name}: {len(genes)} reviews with xref; {with_any} have phenotype rows; "
        f"{n_nutr} have a non-glucose carbon/nitrogen-source phenotype",
        file=sys.stderr,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--cache", type=Path, default=Path("tmp/fungal_phenotypes"))
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("projects/FUNGAL_PHENOTYPES/data/reviewed_gene_phenotypes.tsv"),
    )
    args = ap.parse_args()

    phaf = fetch(POMBASE_PHAF, args.cache / "pombase_haploid.phaf.tsv")
    obo = fetch(FYPO_OBO, args.cache / "fypo.obo")
    sgd = fetch(SGD_PHENO, args.cache / "sgd_phenotype_data.tab")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(
            [
                "source",
                "gene_folder",
                "db_id",
                "n_phenotype_rows",
                "n_references",
                "n_nutrient_phenotypes",
                "nutrient_phenotypes",
                "nutrient_phenotype_refs",
                "n_IMP_annotations",
                "IMP_review_actions",
            ]
        )
        summarise(
            "PomBase",
            reviewed_genes(args.root, "SCHPO", "PomBase"),
            pombase_rows(phaf, fypo_labels(obo)),
            w,
        )
        summarise(
            "SGD", reviewed_genes(args.root, "yeast", "SGD"), sgd_rows(sgd), w
        )
    print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
