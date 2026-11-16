"""Census of module PANTHER selectors across organisms, from PANTHER's sequence classification files.

For each module named on the command line, every family descriptor (an annoton participant or a
protein-complex unit) is read from the module YAML, and the number of proteins its PANTHER family or
subfamily ids select is counted in each organism's PANTHER release-pinned sequence classification file.
Satisfiability comes from the module engine (``ai_gene_review.module_logic``), so optional parts,
variant sets and module references count as the engine reads them: a step holds in an organism when one
of its PANTHER family or subfamily ids selects a protein there (a step with no PANTHER id falls back to its
UniProt accessions, and a protein-complex step holds when every active unit's PANTHER ids do, because
the engine's atom for a complex carries no unit selectors). The ``unsatisfied_gaps`` of an organism are
the engine's innermost gaps, and ``unevaluable_steps`` lists the steps this oracle cannot evaluate at all
(a step with neither a PANTHER id nor an accession), which never hold. Annoton functions are not checked. Each descriptor row's ``required`` flag marks only whether its top-level part
is ``optional``; it is a reading aid, not the verdict. Classification rows with an empty
accession column are skipped, so they cannot turn a zero count into a hit.

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
from typing import Callable, Iterator

import yaml

from ai_gene_review.etl.panther_families import (
    PANTHER_RELEASE,
    fetch_sequence_classification,
)
from ai_gene_review.module_logic import (
    Atom,
    compile_module_file,
    gap_report,
    iter_atoms,
    is_satisfied,
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
            if not fields[1].strip():
                continue
            index[fields[3]].add(fields[1])
            index[fields[3].split(":")[0]].add(fields[1])
    return index


def complex_units(module: dict) -> dict[str, list[tuple[str, ...]]]:
    """Map each protein-complex annoton id to the PANTHER ids of its active units, one tuple per unit.

    The module engine compiles a protein-complex annoton into one atom without its units' selectors,
    so a family-keyed oracle needs them supplied separately.

    >>> complex_units({"parts": [{"node": {"id": "n", "annotons": [{"id": "c", "participant": {
    ...     "protein_complex": {"active_units": [
    ...         {"participant": {"family": {"term": {"id": "PANTHER:PTHR1"}}}},
    ...         {"participant": {"family": {"term": {"id": "PANTHER:PTHR2"}}}}]}}}]}}]})
    {'c': [('PTHR1',), ('PTHR2',)]}
    """
    out: dict[str, list[tuple[str, ...]]] = {}

    def walk(obj: object) -> None:
        if isinstance(obj, dict):
            units = ((obj.get("participant") or {}).get("protein_complex") or {}).get(
                "active_units"
            )
            if units and isinstance(obj.get("id"), str):
                out[obj["id"]] = [
                    family_ids((u.get("participant") or {}).get("family") or {})
                    for u in units
                ]
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)

    walk(module)
    return out


def atom_holds(
    index: dict[str, set[str]],
    units: dict[str, list[tuple[str, ...]]] | None = None,
    accessions: set[str] | None = None,
    unevaluable: set[str] | None = None,
) -> Callable[[Atom], bool]:
    """Oracle for one organism: a step holds when its PANTHER family ids select a protein.

    A protein-complex step (its id in ``units``, keyed as the engine names atoms) holds when every
    active unit's PANTHER ids select a protein. A step with neither falls back to its UniProt
    accessions, which hold when the organism's classification file lists one of them. A step this
    oracle cannot evaluate (no PANTHER id, no accession, or a complex none of whose units has a PANTHER
    id) does not hold, and its id is added to ``unevaluable`` so it is reported rather than read as an
    absence.

    >>> holds = atom_holds({"PTHR1": {"P1"}, "PTHR2:SF3": {"P2"}}, {"cx": [("PTHR1",), ("PTHR9",)]})
    >>> holds(Atom("a", "a", None, None, family_ids=("PANTHER:PTHR1",)))
    True
    >>> holds(Atom("b", "b", None, None, family_ids=("PANTHER:PTHR9",)))
    False
    >>> holds(Atom("c", "c", None, "P2"))
    True
    >>> holds(Atom("cx", "cx", None, None))
    False
    >>> seen: set[str] = set()
    >>> atom_holds({}, unevaluable=seen)(Atom("f", "f", None, None, function_ids=("GO:1",)))
    False
    >>> seen
    {'f'}
    """
    if accessions is None:
        accessions = set().union(*index.values()) if index else set()
    units = units or {}

    def holds(atom: Atom) -> bool:
        panther = [
            f.removeprefix("PANTHER:")
            for f in atom.family_ids
            if f.startswith("PANTHER:PTHR")
        ]
        if panther:
            return any(index.get(f) for f in panther)
        if atom.node_id in units and any(units[atom.node_id]):
            return all(
                any(index.get(f) for f in unit) for unit in units[atom.node_id] if unit
            )
        if not atom.uniprots:
            if unevaluable is not None:
                unevaluable.add(atom.node_id)
            return False
        return any(acc in accessions for acc in atom.uniprots)

    return holds


def census(module_names: list[str], repo_root: Path, cache: Path) -> dict:
    """Build the census document for the named modules."""
    data = {}
    for org in ORGANISMS:
        path = fetch_sequence_classification(org.slug, cache)
        if path is None:
            raise SystemExit(f"no PANTHER classification file for {org.slug}")
        data[org.slug] = load_classification(path, org.mnemonic)
    all_accessions = {
        slug: set().union(*index.values()) for slug, index in data.items()
    }
    modules = []
    for name in module_names:
        doc = yaml.safe_load((repo_root / "modules" / f"{name}.yaml").read_text())
        rows = []
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
        circuit = compile_module_file(repo_root / "modules" / f"{name}.yaml")
        units = dict(complex_units(doc["module"]))
        for ref in sorted(
            {
                a.node_id.rpartition("#")[0]
                for a in iter_atoms(circuit)
                if "#" in a.node_id
            }
        ):
            ref_doc = yaml.safe_load(
                (repo_root / "modules" / f"{ref}.yaml").read_text()
            )
            units.update(
                {f"{ref}#{k}": v for k, v in complex_units(ref_doc["module"]).items()}
            )
        met, gaps = {}, {}
        unevaluable: set[str] = set()
        for o in ORGANISMS:
            holds = atom_holds(data[o.slug], units, all_accessions[o.slug], unevaluable)
            met[o.slug] = is_satisfied(circuit, holds)
            if not met[o.slug]:
                gaps[o.slug] = ["/".join(g.path) for g in gap_report(circuit, holds)]
        modules.append(
            {
                "module": name,
                "descriptors": rows,
                "required_parts_met": met,
                "unsatisfied_gaps": gaps,
                "unevaluable_steps": sorted(unevaluable),
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
