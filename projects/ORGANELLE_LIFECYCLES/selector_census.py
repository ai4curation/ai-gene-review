"""Census of module PANTHER selectors across organisms, from PANTHER's sequence classification files.

For each module named on the command line, every family descriptor (an annoton participant or a
protein-complex unit) is read from the module YAML, and the number of proteins its PANTHER family or
subfamily ids select is counted in each organism's PANTHER release-pinned sequence classification file.
A descriptor sits under a required part unless the top-level part holding it is ``optional: true``; an
organism meets the module's required parts when every required descriptor selects at least one of its
proteins. That is a scratch satisfiability reading of the selectors only: it ignores annoton functions,
``ONE_OR_MORE`` variant logic and module references.

Usage (from the repository root)::

    uv run python projects/ORGANELLE_LIFECYCLES/selector_census.py \
        phagosome_maturation synaptic_vesicle_cycle \
        -o projects/ORGANELLE_LIFECYCLES/selector-census.yaml

The classification files are downloaded once into the git-ignored ``.cache/panther``.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import yaml

from ai_gene_review.etl.panther_families import (
    PANTHER_RELEASE,
    fetch_sequence_classification,
)


@dataclass(frozen=True)
class Organism:
    """A PANTHER sequence-classification file, optionally restricted to one UniProt mnemonic.

    >>> Organism("green_algae", "Chlamydomonas reinhardtii", "CHLRE").slug
    'green_algae'
    """

    slug: str
    label: str
    mnemonic: str | None = None


ORGANISMS: tuple[Organism, ...] = (
    Organism("human", "Homo sapiens"),
    Organism("fruit_fly", "Drosophila melanogaster"),
    Organism("nematode_worm", "Caenorhabditis elegans"),
    Organism("nematostella", "Nematostella vectensis"),
    Organism("trichoplax", "Trichoplax adhaerens"),
    Organism("monosiga", "Monosiga brevicollis"),
    Organism("chytrid", "Batrachochytrium dendrobatidis"),
    Organism("green_algae", "Chlamydomonas reinhardtii", "CHLRE"),
    Organism("moss", "Physcomitrium patens"),
    Organism("t_brucei", "Trypanosoma brucei"),
    Organism("leishmania", "Leishmania major"),
    Organism("giardia", "Giardia intestinalis"),
    Organism("trichomonas", "Trichomonas vaginalis"),
    Organism("paramecium", "Paramecium tetraurelia"),
    Organism("phytophthora", "Phytophthora ramorum"),
    Organism("plasmodium", "Plasmodium falciparum"),
    Organism("thalassiosira", "Thalassiosira pseudonana"),
    Organism("arabidopsis", "Arabidopsis thaliana"),
    Organism("rice", "Oryza sativa"),
    Organism("budding_yeast", "Saccharomyces cerevisiae"),
    Organism("fission_yeast", "Schizosaccharomyces pombe"),
    Organism("neurospora", "Neurospora crassa"),
    Organism("dictyostelium", "Dictyostelium discoideum"),
    Organism("e_histolytica", "Entamoeba histolytica"),
)


@dataclass(frozen=True)
class Descriptor:
    """One family descriptor in a module: where it sits, its PANTHER ids and whether it is required."""

    path: str
    selectors: tuple[str, ...]
    required: bool


def family_ids(family: dict) -> tuple[str, ...]:
    """PANTHER ids of a family descriptor, without the ``PANTHER:`` prefix.

    >>> family_ids({"term": {"id": "PANTHER:PTHR1:SF2"}})
    ('PTHR1:SF2',)
    >>> family_ids({"family_terms": [{"id": "PANTHER:PTHR1"}, {"id": "PANTHER:PTHR2"}]})
    ('PTHR1', 'PTHR2')
    >>> family_ids({"preferred_term": "no id"})
    ()
    """
    ids = (
        [family["term"]["id"]]
        if "term" in family
        else [t["id"] for t in family.get("family_terms", [])]
    )
    return tuple(i.removeprefix("PANTHER:") for i in ids if i.startswith("PANTHER:"))


def descriptors(module: dict) -> Iterator[Descriptor]:
    """Yield every family descriptor under the module's parts, with its required flag.

    >>> doc = {"parts": [{"optional": True, "node": {"id": "n", "annotons": [{"id": "a",
    ...     "participant": {"family": {"term": {"id": "PANTHER:PTHR9"}}}}]}}]}
    >>> [(d.path, d.selectors, d.required) for d in descriptors(doc)]
    [('n/a', ('PTHR9',), False)]
    """

    def walk(obj: object, path: str, required: bool) -> Iterator[Descriptor]:
        if isinstance(obj, dict):
            here = (
                f"{path}/{obj['id']}"
                if isinstance(obj.get("id"), str) and path
                else obj.get("id", path)
            )
            family = obj.get("family")
            if isinstance(family, dict) and family_ids(family):
                yield Descriptor(str(here), family_ids(family), required)
            for key, value in obj.items():
                if key != "family":
                    yield from walk(value, str(here), required)
        elif isinstance(obj, list):
            for value in obj:
                yield from walk(value, path, required)

    for part in module.get("parts", []):
        yield from walk(part["node"], "", not part.get("optional", False))


def load_classification(path: Path, mnemonic: str | None) -> dict[str, set[str]]:
    """Map each PANTHER family and subfamily id to the UniProt accessions it holds in one file."""
    index: dict[str, set[str]] = defaultdict(set)
    with path.open() as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 4 or not fields[3].startswith("PTHR"):
                continue
            if mnemonic and not fields[0].startswith(f"{mnemonic}|"):
                continue
            index[fields[3]].add(fields[1])
            index[fields[3].split(":")[0]].add(fields[1])
    return index


def census(module_names: list[str], repo_root: Path, cache: Path) -> dict:
    """Build the census document for the named modules."""
    data = {}
    for org in ORGANISMS:
        path = fetch_sequence_classification(org.slug, cache)
        if path is None:
            raise SystemExit(f"no PANTHER classification file for {org.slug}")
        data[org.slug] = load_classification(path, org.mnemonic)
    modules = []
    for name in module_names:
        doc = yaml.safe_load((repo_root / "modules" / f"{name}.yaml").read_text())
        rows, failures = [], defaultdict(list)
        for d in descriptors(doc["module"]):
            counts = {
                o.slug: len(
                    set().union(*(data[o.slug].get(s, set()) for s in d.selectors))
                )
                for o in ORGANISMS
            }
            rows.append(
                {
                    "descriptor": d.path,
                    "required": d.required,
                    "selectors": list(d.selectors),
                    "proteins_per_organism": counts,
                }
            )
            if d.required:
                for slug, n in counts.items():
                    if n == 0:
                        failures[slug].append(d.path)
        modules.append(
            {
                "module": name,
                "descriptors": rows,
                "required_parts_met": {o.slug: not failures[o.slug] for o in ORGANISMS},
                "required_descriptors_unmet": {
                    o.slug: failures[o.slug] for o in ORGANISMS if failures[o.slug]
                },
            }
        )
    return {
        "panther_release": PANTHER_RELEASE,
        "source": "PANTHER sequence classification files, one per organism (green_algae restricted to CHLRE)",
        "organisms": [
            {
                "slug": o.slug,
                "label": o.label,
                **({"mnemonic": o.mnemonic} if o.mnemonic else {}),
            }
            for o in ORGANISMS
        ],
        "modules": modules,
    }


def main() -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("modules", nargs="+", help="module file stems under modules/")
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/panther"))
    args = parser.parse_args()
    doc = census(args.modules, Path.cwd(), args.cache_dir)
    args.output.write_text(
        "# Generated by selector_census.py; do not edit by hand.\n"
        + yaml.safe_dump(doc, sort_keys=False, width=110)
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
