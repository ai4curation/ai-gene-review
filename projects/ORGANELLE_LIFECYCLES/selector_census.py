"""Census of module PANTHER selectors across organisms, from PANTHER's sequence classification files.

For each module named on the command line, every family descriptor (an annoton participant or a
protein-complex unit) is read from the module YAML, and the number of proteins its PANTHER family or
subfamily ids select is counted in each organism's PANTHER release-pinned sequence classification file.
Satisfiability comes from the module engine (``ai_gene_review.module_logic``), so optional parts,
variant sets and module references count as the engine reads them: a step holds in an organism when one
of its PANTHER family or subfamily ids selects a protein there (a step with no PANTHER id falls back to its
UniProt accessions, and a protein-complex step holds when every active unit's PANTHER ids do, because
the engine's atom for a complex carries no unit selectors). The ``unsatisfied_gaps`` of an organism are
the engine's innermost gaps. Every step of the compiled module is classified once, before any organism
is evaluated: ``unevaluable_steps`` lists the steps this oracle cannot evaluate at all (a step with
neither a PANTHER id nor an accession), which never hold, and ``mixed_complex_steps`` the complexes
whose units mix PANTHER-keyed and gene-keyed selectors, which are evaluated on their PANTHER-keyed
units alone. A family step that also names an InterPro domain (``domain`` or ``required_domain``) holds only
when a selected protein carries that domain in UniProt's InterPro cross-references, fetched once and
cached in ``.cache/panther/uniprot-interpro.json``; such rows also report
``proteins_with_required_domains_per_organism``. Annoton functions are not checked. Each descriptor row's ``required`` flag marks only whether its top-level part
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
import json
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Literal

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
    required_domains: tuple[str, ...] = ()


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
    >>> doc = {"parts": [{"node": {"id": "n", "annotons": [{"id": "a", "participant": {
    ...     "family": {"term": {"id": "PANTHER:PTHR9"}},
    ...     "required_domain": {"term": {"id": "InterPro:IPR1"}}}}]}}]}
    >>> [d.required_domains for d in descriptors(doc)]
    [('IPR1',)]
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
                yield Descriptor(
                    str(here),
                    family_ids(family),
                    required,
                    interpro_ids([obj.get("domain"), obj.get("required_domain")]),
                )
            for key, value in obj.items():
                if key != "family":
                    yield from walk(value, str(here), required)
        elif isinstance(obj, list):
            for value in obj:
                yield from walk(value, path, required)

    for part in module.get("parts", []):
        yield from walk(part["node"], "", not part.get("optional", False))


def interpro_ids(descriptors: list[object]) -> tuple[str, ...]:
    """InterPro ids of domain descriptors, without the ``InterPro:`` prefix; other ids are ignored.

    >>> interpro_ids([{"term": {"id": "InterPro:IPR018966"}}, None, {"term": {"id": "PF09359"}}])
    ('IPR018966',)
    """
    ids = [
        d["term"]["id"]
        for d in descriptors
        if isinstance(d, dict) and isinstance(d.get("term"), dict)
    ]
    return tuple(i.removeprefix("InterPro:") for i in ids if i.startswith("InterPro:"))


UNIPROT_ACCESSIONS_URL = "https://rest.uniprot.org/uniprotkb/accessions"


@dataclass(frozen=True)
class DomainLookup:
    """InterPro entries per accession, with what UniProt did not answer and the releases it answered from."""

    domains: dict[str, set[str]]
    unanswered: tuple[str, ...]
    uniprot_releases: tuple[str, ...]


def parse_interpro_tsv(text: str) -> dict[str, list[str]]:
    r"""Parse UniProt's ``accession,xref_interpro`` TSV into accession -> InterPro ids.

    >>> parse_interpro_tsv("Entry\tInterPro\nP1\tIPR1;IPR2;\nP2\t\n")
    {'P1': ['IPR1', 'IPR2'], 'P2': []}
    """
    found = {}
    for row in text.splitlines()[1:]:
        acc, _, ipr = row.partition("\t")
        found[acc] = [i for i in ipr.split(";") if i]
    return found


def fetch_interpro_domains(accessions: set[str], cache_file: Path) -> DomainLookup:
    """Look up the InterPro entries of UniProt accessions, caching answers in ``cache_file``.

    Only accessions UniProt actually returned are cached, each with the UniProt release it came
    from, so an accession missing from a response (obsolete, merged, or a failed request) is asked
    again on the next run instead of being remembered as having no domains. Accessions still
    unanswered are reported in :attr:`DomainLookup.unanswered`; a step needing a domain does not
    hold for them.
    """
    cached = json.loads(cache_file.read_text()) if cache_file.exists() else {}
    entries: dict[str, dict] = cached.get("accessions", {})
    missing = sorted(accessions - set(entries))
    for start in range(0, len(missing), 200):
        batch = missing[start : start + 200]
        query = urllib.parse.urlencode(
            {
                "accessions": ",".join(batch),
                "fields": "accession,xref_interpro",
                "format": "tsv",
            }
        )
        with urllib.request.urlopen(f"{UNIPROT_ACCESSIONS_URL}?{query}") as response:
            release = response.headers.get("X-UniProt-Release", "unknown")
            found = parse_interpro_tsv(response.read().decode())
        entries.update(
            {
                acc: {"interpro": found[acc], "uniprot_release": release}
                for acc in batch
                if acc in found
            }
        )
        # Written after every batch, so a failure in a later batch keeps the earlier answers.
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(
            json.dumps({"accessions": entries}, sort_keys=True, indent=0)
        )
    answered = accessions & set(entries)
    return DomainLookup(
        domains={acc: set(entries[acc]["interpro"]) for acc in answered},
        unanswered=tuple(sorted(accessions - answered)),
        uniprot_releases=tuple(
            sorted({entries[acc]["uniprot_release"] for acc in answered})
        ),
    )


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


def panther_ids(atom: Atom) -> list[str]:
    """PANTHER family and subfamily ids of a step, without the ``PANTHER:`` prefix.

    >>> panther_ids(Atom("a", "a", None, None, family_ids=("PANTHER:PTHR1:SF2", "PF00001")))
    ['PTHR1:SF2']
    """
    return [
        f.removeprefix("PANTHER:")
        for f in atom.family_ids
        if f.startswith("PANTHER:PTHR")
    ]


StepKind = Literal["family", "complex", "mixed_complex", "accession", "unevaluable"]


def step_kind(atom: Atom, units: dict[str, list[tuple[str, ...]]]) -> StepKind:
    """How :func:`atom_holds` evaluates a step, independent of organism.

    ``family`` (the step's own PANTHER ids), ``complex`` (every active unit has PANTHER ids),
    ``mixed_complex`` (some units have PANTHER ids and some do not, so only the family-keyed units are
    evaluated), ``accession`` (UniProt accessions only) or ``unevaluable`` (nothing this oracle reads).

    >>> units = {"cx": [("PTHR1",), ("PTHR2",)], "mx": [("PTHR1",), ()], "gx": [(), ()]}
    >>> [step_kind(Atom(i, i, None, None), units) for i in ("cx", "mx", "gx")]
    ['complex', 'mixed_complex', 'unevaluable']
    >>> step_kind(Atom("a", "a", None, None, family_ids=("PANTHER:PTHR1",)), units)
    'family'
    >>> step_kind(Atom("b", "b", None, "P1"), units)
    'accession'
    """
    if panther_ids(atom):
        return "family"
    unit_ids = units.get(atom.node_id, [])
    if any(unit_ids):
        return "complex" if all(unit_ids) else "mixed_complex"
    return "accession" if atom.uniprots else "unevaluable"


def atom_holds(
    index: dict[str, set[str]],
    units: dict[str, list[tuple[str, ...]]] | None = None,
    accessions: set[str] | None = None,
    domains: dict[str, set[str]] | None = None,
) -> Callable[[Atom], bool]:
    """Oracle for one organism: a step holds when its PANTHER family ids select a protein.

    A family step that also names InterPro domains (``domain`` or ``required_domain``) holds only when
    one selected protein carries every such domain in ``domains``, which maps accessions to their
    InterPro entries (see :func:`fetch_interpro_domains`).

    A protein-complex step (its id in ``units``, keyed as the engine names atoms) holds when every
    active unit that has PANTHER ids selects a protein; units without PANTHER ids are not evaluated
    (:func:`step_kind` reports such complexes as ``mixed_complex``). A step with neither falls back to
    its UniProt accessions, which hold when the organism's classification file lists one of them. A
    step this oracle cannot evaluate at all does not hold (:func:`step_kind` reports it as
    ``unevaluable``, so it is listed rather than read as an absence).

    >>> holds = atom_holds({"PTHR1": {"P1"}, "PTHR2:SF3": {"P2"}}, {"cx": [("PTHR1",), ("PTHR9",)]})
    >>> holds(Atom("a", "a", None, None, family_ids=("PANTHER:PTHR1",)))
    True
    >>> holds(Atom("b", "b", None, None, family_ids=("PANTHER:PTHR9",)))
    False
    >>> holds(Atom("c", "c", None, "P2"))
    True
    >>> holds(Atom("cx", "cx", None, None))
    False
    >>> atom_holds({})(Atom("f", "f", None, None, function_ids=("GO:1",)))
    False
    >>> vtc = Atom("v", "v", None, None, family_ids=("PANTHER:PTHR1",), domain_ids=("InterPro:IPR9",))
    >>> atom_holds({"PTHR1": {"P1"}}, domains={"P1": {"IPR2"}})(vtc)
    False
    >>> atom_holds({"PTHR1": {"P1", "P3"}}, domains={"P1": {"IPR2"}, "P3": {"IPR9"}})(vtc)
    True
    """
    if accessions is None:
        accessions = set().union(*index.values()) if index else set()
    units = units or {}

    def holds(atom: Atom) -> bool:
        kind = step_kind(atom, units)
        if kind == "family":
            selected = set().union(*(index.get(f, set()) for f in panther_ids(atom)))
            needed = set(interpro_ids([{"term": {"id": d}} for d in atom.domain_ids]))
            if not needed:
                return bool(selected)
            return any(needed <= (domains or {}).get(acc, set()) for acc in selected)
        if kind in ("complex", "mixed_complex"):
            return all(
                any(index.get(f) for f in unit) for unit in units[atom.node_id] if unit
            )
        if kind == "accession":
            return any(acc in accessions for acc in atom.uniprots)
        return False

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
        circuit = compile_module_file(repo_root / "modules" / f"{name}.yaml")
        domain_families = [
            d.selectors for d in descriptors(doc["module"]) if d.required_domains
        ] + [
            tuple(panther_ids(a))
            for a in iter_atoms(circuit)
            if a.domain_ids and panther_ids(a)
        ]
        for a in iter_atoms(circuit):
            if (
                a.domain_ids
                and panther_ids(a)
                and len(interpro_ids([{"term": {"id": d}} for d in a.domain_ids]))
                < len(a.domain_ids)
            ):
                raise SystemExit(
                    f"{name}: step {a.node_id} names a domain the census cannot check "
                    f"({', '.join(a.domain_ids)}); use an InterPro id"
                )
        candidates = {
            o.slug: {
                acc
                for selectors in domain_families
                for f in selectors
                for acc in data[o.slug].get(f, set())
            }
            for o in ORGANISMS
        }
        lookup = fetch_interpro_domains(
            set().union(*candidates.values()), cache / "uniprot-interpro.json"
        )
        domains = lookup.domains
        rows = []
        for d in descriptors(doc["module"]):
            selected = {
                o.slug: set().union(*(data[o.slug].get(s, set()) for s in d.selectors))
                for o in ORGANISMS
            }
            row = {
                "descriptor": d.path,
                "required": d.required,
                "selectors": list(d.selectors),
                "proteins_per_organism": {k: len(v) for k, v in selected.items()},
            }
            if d.required_domains:
                row["required_domains"] = [f"InterPro:{i}" for i in d.required_domains]
                row["proteins_with_required_domains_per_organism"] = {
                    k: sum(
                        set(d.required_domains) <= domains.get(acc, set()) for acc in v
                    )
                    for k, v in selected.items()
                }
            rows.append(row)
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
        kinds = {a.node_id: step_kind(a, units) for a in iter_atoms(circuit)}
        met, gaps = {}, {}
        for o in ORGANISMS:
            holds = atom_holds(data[o.slug], units, all_accessions[o.slug], domains)
            met[o.slug] = is_satisfied(circuit, holds)
            if not met[o.slug]:
                gaps[o.slug] = ["/".join(g.path) for g in gap_report(circuit, holds)]
        modules.append(
            {
                "module": name,
                "descriptors": rows,
                "required_parts_met": met,
                "unsatisfied_gaps": gaps,
                "unevaluable_steps": sorted(
                    k for k, v in kinds.items() if v == "unevaluable"
                ),
                "mixed_complex_steps": sorted(
                    k for k, v in kinds.items() if v == "mixed_complex"
                ),
                **(
                    {
                        "domain_lookup": {
                            "source": "UniProt InterPro cross-references",
                            "uniprot_releases": list(lookup.uniprot_releases),
                            "unanswered_accessions": list(lookup.unanswered),
                            "unanswered_by_organism": {
                                o.slug: sorted(
                                    set(lookup.unanswered) & candidates[o.slug]
                                )
                                for o in ORGANISMS
                                if set(lookup.unanswered) & candidates[o.slug]
                            },
                        }
                    }
                    if domain_families
                    else {}
                ),
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
