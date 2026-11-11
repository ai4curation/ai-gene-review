"""Phylogenetic extracts: where each IBA row, and each PAINT node, sits in the PANTHER tree.

An IBA is a PAINT curator's judgement that a function arose at one node of a family
tree. Reviewing it means arguing with that placement, and that needs what the curator
saw: the node's position among speciation and duplication events, which leaves are
below it, where the seeds sit relative to the gene under review, and how the gene's
sequence compares with the seeds in the family alignment. The GOA row gives only the
node id and the seed ids.

Two derived files (like ``GENE-goa.tsv``; do not edit) state those facts, computed from
the PANTHER release trees and alignments read by :mod:`ai_gene_review.etl.panther_release`.

``genes/<org>/<GENE>/<GENE>-phylo.yaml`` -- for every IBA row of one gene:

``trees[].target``, ``trees[].lineage``
    The gene's leaf and every node from the family root down to it, with event, taxon
    and branch length.
``trees[].nodes``
    Each IBD node the gene's rows cite: its event and taxon, how many leaves, species
    and subfamilies it covers, and the branches directly below it.
``trees[].seeds``
    Each seed any row cites: its leaf, how it is related to the gene by the tree
    (``ORTHOLOG`` when the two join at a speciation node, ``PARALOG`` at a duplication,
    ``XENOLOG`` at a horizontal transfer; ``duplications_between`` says whether either
    lineage duplicated since), their tree distance, and their identity and coverage in
    the family alignment.
``trees[].rows``
    One entry per IBA row: steps and duplications between the node and the gene, where
    the seeds' own common ancestor sits relative to the node and to the gene, PAINT
    losses on the path, and a one-line ``summary`` that a review can quote in
    ``supported_by``.

``interpro/panther/<PTHR>/<PTHR>-tree-nodes.yaml`` -- for every node of the family's
PAINT slice: the same node description, and for each term asserted there how its seeds
are spread over the branches below the node. A family review's node assessment quotes
its ``summary`` lines.

Usage:
    uv run python -m ai_gene_review.etl.gene_phylo human CIRBP
    uv run python -m ai_gene_review.etl.gene_phylo --genes-file genes.txt
    uv run python -m ai_gene_review.etl.gene_phylo --family PTHR48034
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Sequence

import yaml

from ai_gene_review.etl.panther_release import (
    DEFAULT_DB,
    LEAF,
    FamilyTree,
    PantherRelease,
    column_of_position,
    embed_row,
    pairwise_alignment_stats,
)

ASPECT_CODE = {"molecular_function": "F", "biological_process": "P", "cellular_component": "C"}
LOSS_CODES = ("IRD", "IKR")
EVENT_PHRASE = {
    "SPECIATION": "speciation",
    "DUPLICATION": "duplication",
    "HORIZONTAL_TRANSFER": "horizontal-transfer",
    "UNKNOWN": "unclassified",
}

#: UniProt ``DR`` database -> prefix of the matching WITH/FROM style identifier.
DR_PREFIX = {
    "HGNC": "HGNC",
    "MGI": "MGI",
    "RGD": "RGD",
    "SGD": "SGD",
    "FlyBase": "FB",
    "ZFIN": "ZFIN",
    "PomBase": "PomBase",
    "dictyBase": "dictyBase",
    "CGD": "CGD",
    "Xenbase": "Xenbase",
}


@dataclass(frozen=True)
class IbaRow:
    """One IBA row of a ``GENE-goa.tsv`` file."""

    accession: str
    term_id: str
    term_label: str
    aspect: str
    qualifier: str
    negated: bool
    with_from: str
    nodes: list[str]
    seeds: list[str]


def read_iba_rows(goa_path: Path) -> list[IbaRow]:
    """Read the IBA rows of a QuickGO-style GOA TSV, in file order."""
    rows: list[IbaRow] = []
    with goa_path.open(encoding="utf-8", newline="") as handle:
        for rec in csv.DictReader(handle, delimiter="\t"):
            if rec.get("GO EVIDENCE CODE") != "IBA":
                continue
            tokens = [t for t in (rec.get("WITH/FROM") or "").split("|") if t]
            qualifier = rec.get("QUALIFIER") or ""
            rows.append(
                IbaRow(
                    accession=rec["GENE PRODUCT ID"],
                    term_id=rec["GO TERM"],
                    term_label=rec.get("GO NAME") or "",
                    aspect=ASPECT_CODE.get(rec.get("GO ASPECT") or "", ""),
                    qualifier=qualifier,
                    negated=qualifier.startswith("NOT"),
                    with_from="|".join(tokens),
                    nodes=[t.split(":", 1)[1] for t in tokens if t.startswith("PANTHER:PTN")],
                    seeds=[t for t in tokens if not t.startswith("PANTHER:")],
                )
            )
    return rows


@lru_cache(maxsize=4)
def _panther_names(obo_path: Path, mtime_ns: int) -> dict[str, str]:
    """``{PANTHER:PTHRnnnnn[:SFn]: name}`` from the committed ``panther.obo``."""
    names: dict[str, str] = {}
    current = ""
    with obo_path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("id: PANTHER:"):
                current = line[4:].strip()
            elif line.startswith("name: ") and current:
                names[current] = line[6:].strip()
                current = ""
    return names


def panther_names(root: Path) -> dict[str, str]:
    """PANTHER family and subfamily names, or an empty map when the OBO is absent."""
    obo = root / "interpro" / "panther" / "panther.obo"
    return _panther_names(obo, obo.stat().st_mtime_ns) if obo.exists() else {}


def uniprot_identifiers(uniprot_txt: str) -> list[tuple[str, str]]:
    """Other identifiers of the entry, as ``(token, how it was found)``, in file order.

    >>> uniprot_identifiers("AC   P1; Q2;\\nDR   HGNC; HGNC:1982; CIRBP.\\nDR   MGI; MGI:101769; Bcl2.\\n"
    ...                     "DR   WormBase; C06A1.1; CE02114; WBGene00000423; cdc-48.1.\\n")
    [('UniProtKB:P1', 'secondary accession P1'), ('UniProtKB:Q2', 'secondary accession Q2'), ('HGNC:1982', 'gene id HGNC:1982'), ('MGI:MGI:101769', 'gene id MGI:MGI:101769'), ('WB:WBGene00000423', 'gene id WB:WBGene00000423')]
    """
    out: list[tuple[str, str]] = []
    for line in uniprot_txt.splitlines():
        if line.startswith("AC   "):
            for accession in re.findall(r"[A-Z0-9]+", line[5:]):
                out.append((f"UniProtKB:{accession}", f"secondary accession {accession}"))
        elif line.startswith("DR   "):
            fields = [f.strip().rstrip(".") for f in line[5:].split(";")]
            db = fields[0]
            token = ""
            if db == "WormBase":
                gene = next((f for f in fields[1:] if f.startswith("WBGene")), "")
                token = f"WB:{gene}" if gene else ""
            elif db in DR_PREFIX and len(fields) > 1:
                local = fields[1]
                if db == "HGNC":
                    local = local.removeprefix("HGNC:")
                token = f"{DR_PREFIX[db]}:{local}"
            if token:
                out.append((token, f"gene id {token}"))
    return out


def _round(value: float) -> float:
    return round(value, 3)


def _count(n: int, noun: str) -> str:
    """A count with its noun in the right number.

    >>> _count(1, "leaf"), _count(3, "leaf"), _count(2, "species"), _count(2, "subfamily"), _count(0, "step")
    ('1 leaf', '3 leaves', '2 species', '2 subfamilies', '0 steps')
    """
    if n == 1 or noun.endswith("species"):
        return f"{n} {noun}"
    if noun.endswith("f"):
        return f"{n} {noun[:-1]}ves"
    if noun.endswith("y"):
        return f"{n} {noun[:-1]}ies"
    return f"{n} {noun}s"


@dataclass
class FamilyAlignment:
    """A family's alignment rows with the full-length sequences they were cut from.

    PANTHER's rows hold only the residues in the model's match columns. ``embedding`` lays
    a row back onto the leaf's full sequence, so that columns can be reported as positions
    in the protein itself; it is None when the release has no full sequence for the leaf
    or the row does not fit it.
    """

    tree: FamilyTree
    rows: dict[str, str]
    full: dict[str, str]
    _embeddings: dict[str, list[tuple[int, bool]] | None] = field(default_factory=dict)

    def sequence(self, an: str) -> str | None:
        """The leaf's full-length sequence, when the release has it."""
        return self.full.get(self.tree.nodes[an].long_id)

    def embedding(self, an: str) -> list[tuple[int, bool]] | None:
        """``(position in the full sequence, certain)`` for each column of the leaf's row."""
        if an not in self._embeddings:
            sequence = self.sequence(an)
            row = self.rows.get(an)
            self._embeddings[an] = embed_row(row, sequence) if row and sequence else None
        return self._embeddings[an]

    def native_regions(self, an: str, regions: list[tuple[int, int]]) -> list[str] | None:
        """Row-residue ranges as ``start-end`` in the protein's own numbering; None if unknown."""
        embedding = self.embedding(an)
        if embedding is None:
            return None
        positions = [pos for pos, _ in embedding if pos]
        return [f"{positions[start - 1]}-{positions[end - 1]}" for start, end in regions]


def node_place(tree: FamilyTree, an: str) -> dict[str, Any]:
    """Event and position in the species tree of one node.

    A speciation node carries ``taxon``. Any other internal node carries ``after`` (the
    nearest speciation above it) and ``before`` (the first speciation, or leaf organism,
    on each branch below it).
    """
    node = tree.nodes[an]
    place: dict[str, Any] = {"event": node.event}
    if node.event == LEAF:
        place["organism"] = tree.leaf(an).organism
    elif node.event == "SPECIATION" and node.taxon:
        place["taxon"] = node.taxon
    else:
        after, before = tree.taxon_bounds(an)
        if after:
            place["after"] = after
        place["before"] = before
    return place


def place_phrase(tree: FamilyTree, an: str) -> str:
    """A node's event and taxon as prose, e.g. ``a duplication node after Eumetazoa``."""
    place = node_place(tree, an)
    kind = EVENT_PHRASE.get(place["event"], "unclassified")
    article = "an" if kind[0] in "aeiou" else "a"
    if "taxon" in place:
        return f"{article} {kind} node at {place['taxon']}"
    parts = [f"{article} {kind} node"]
    if place.get("after"):
        parts.append(f"after {place['after']}")
    if place.get("before"):
        parts.append("before " + "/".join(place["before"][:3]) + ("/..." if len(place["before"]) > 3 else ""))
    return " ".join(parts)


def _species(tree: FamilyTree, an: str) -> int:
    return len({tree.leaf(leaf).organism for leaf in tree.leaves_below(an)})


def describe_node(
    tree: FamilyTree, an: str, names: dict[str, str], target: str | None = None
) -> dict[str, Any]:
    """What one tree node covers: leaves, species, subfamilies and the branches below it."""
    leaves = tree.leaves_below(an)
    subfamilies = Counter(tree.subfamily_of.get(leaf, "") for leaf in leaves)
    subfamilies.pop("", None)
    out: dict[str, Any] = {"node": tree.ptn_of.get(an, an), **node_place(tree, an)}
    out["is_root"] = an == tree.root
    out["depth"] = tree.depth(an)
    out["leaves"] = len(leaves)
    out["species"] = _species(tree, an)
    out["subfamilies"] = len(subfamilies)
    out["top_subfamilies"] = [
        {"id": sf, "leaves": n, "name": names.get(f"PANTHER:{sf}", "")}
        for sf, n in sorted(subfamilies.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    ]
    branches = []
    for child in tree.nodes[an].children:
        branch: dict[str, Any] = {"node": tree.ptn_of.get(child, child), **node_place(tree, child)}
        branch["leaves"] = len(tree.leaves_below(child))
        branch["species"] = _species(tree, child)
        if target is not None:
            branch["has_target"] = tree.is_ancestor(child, target)
        branches.append(branch)
    out["branches"] = branches
    return out


def _lineage(tree: FamilyTree, target: str) -> list[dict[str, Any]]:
    """The nodes from the root down to the target leaf."""
    out = []
    for an in tree.lineage(target):
        entry: dict[str, Any] = {"node": tree.ptn_of.get(an, an), **node_place(tree, an)}
        length = tree.nodes[an].branch_length
        if length is not None:
            entry["branch"] = _round(length)
        if tree.nodes[an].event != LEAF:
            entry["leaves"] = len(tree.leaves_below(an))
        out.append(entry)
    return out


def _relation(tree: FamilyTree, seed: str, target: str) -> tuple[str, str, int, int]:
    """How a seed leaf is related to the target.

    Returns ``(relation, MRCA, duplications between, transfers between)``. The relation is
    the event at the node where the two leaves join: speciation makes them orthologs,
    duplication paralogs, horizontal transfer xenologs. Events strictly between that node
    and either leaf are only counted: a transfer node on the way says that one of its
    branches was transferred, not which one, so it is reported rather than interpreted.
    """
    if seed == target:
        return "SELF", target, 0, 0
    top = tree.mrca(seed, target)
    between = tree.path(top, seed)[1:-1] + tree.path(top, target)[1:-1]
    events = [tree.nodes[an].event for an in between]
    relation = {
        "SPECIATION": "ORTHOLOG",
        "DUPLICATION": "PARALOG",
        "HORIZONTAL_TRANSFER": "XENOLOG",
    }.get(tree.nodes[top].event, "UNRESOLVED")
    return relation, top, events.count("DUPLICATION"), events.count("HORIZONTAL_TRANSFER")


def _seed_entry(
    token: str,
    tree: FamilyTree,
    leaf: str,
    target: str | None,
    alignment: FamilyAlignment,
    how: str,
) -> dict[str, Any]:
    """One resolved seed: its leaf and, when the target is placed, how the two relate."""
    info = tree.leaf(leaf)
    entry: dict[str, Any] = {
        "id": token,
        "leaf": tree.ptn_of.get(leaf, leaf),
        "organism": info.organism,
        "gene_id": f"{info.db}={info.gene_id}",
        "accession": info.accession,
        "subfamily": tree.subfamily_of.get(leaf, ""),
    }
    if how:
        entry["resolved_by"] = how
    if target is None:
        return entry
    relation, top, duplications, transfers = _relation(tree, leaf, target)
    entry["relation"] = relation
    if relation == "SELF":
        return entry
    entry["mrca"] = tree.ptn_of.get(top, top)
    place = node_place(tree, top)
    entry["mrca_event"] = place.pop("event")
    for key, value in place.items():
        entry[f"mrca_{key}"] = value
    entry["mrca_depth"] = tree.depth(top)
    if duplications:
        entry["duplications_between"] = duplications
    if transfers:
        entry["transfers_between"] = transfers
    entry["tree_distance"] = _round(tree.distance(leaf, target))
    rows = alignment.rows
    if target in rows and leaf in rows:
        stats = pairwise_alignment_stats(rows[target], rows[leaf])
        entry["identity"] = _round(stats.identity)
        entry["aligned"] = stats.aligned
        seed_sequence, target_sequence = alignment.sequence(leaf), alignment.sequence(target)
        if seed_sequence and target_sequence:
            entry["length"] = len(seed_sequence)
            entry["covers_target"] = _round(stats.aligned / len(target_sequence))
            entry["covers_seed"] = _round(stats.aligned / len(seed_sequence))
        seed_only = alignment.native_regions(leaf, stats.other_regions_missing_in_self)
        if seed_only:
            entry["seed_regions_without_target"] = seed_only
        target_only = alignment.native_regions(target, stats.self_regions_missing_in_other)
        if target_only:
            entry["target_regions_without_seed"] = target_only
    return entry


def resolve_seed(token: str, tree: FamilyTree, release: PantherRelease) -> tuple[str | None, str]:
    """Find the leaf a seed token names: ``(leaf, how)``; ``how`` is empty for a direct hit."""
    leaf = tree.find_leaf(token)
    if leaf is not None:
        return leaf, ""
    for accession in release.alias_accessions(token):
        leaf = tree.find_leaf(f"UniProtKB:{accession}")
        if leaf is not None:
            return leaf, f"UniProt locus name ({accession})"
    return None, ""


def _find_target(
    tree: FamilyTree, accession: str, uniprot_txt: str
) -> tuple[str | None, str]:
    """The gene's leaf in ``tree``: ``(leaf, matched_by)``."""
    leaf = tree.find_leaf(f"UniProtKB:{accession}")
    if leaf is not None:
        return leaf, "accession"
    for token, how in uniprot_identifiers(uniprot_txt):
        if token == f"UniProtKB:{accession}":
            continue
        leaf = tree.find_leaf(token)
        if leaf is not None:
            return leaf, how
    return None, ""


def read_paint_slice(paint_tsv: Path) -> list[dict[str, str]] | None:
    """The rows of a family's ``<PTHR>-paint.tsv`` slice; None when the family has no local slice."""
    if not paint_tsv.exists():
        return None
    with paint_tsv.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _is_loss(rec: dict[str, str]) -> bool:
    """True for a PAINT loss row: IRD, IKR, or any negated row."""
    return rec["evidence"] in LOSS_CODES or rec["negated"] == "true"


def losses_on_path(
    paint_rows: list[dict[str, str]], term: str, path_below_node: list[str]
) -> list[dict[str, str]]:
    """PAINT losses of ``term`` on the nodes between an IBD node and the gene.

    ``path_below_node`` lists the persistent ids from just below the IBD node down to the
    gene's leaf. A loss stops the term descending; when PAINT asserts the same term again
    on a node further down the same path the block is lifted for the gene, and the loss
    records that node as ``reasserted_below``.

    >>> rows = [{"node": "PTN2", "go_id": "GO:1", "evidence": "IRD", "negated": "true", "date": "20240101"},
    ...         {"node": "PTN3", "go_id": "GO:1", "evidence": "IBD", "negated": "false", "date": "20240102"}]
    >>> losses_on_path(rows, "GO:1", ["PTN2", "PTN3", "PTN4"])
    [{'node': 'PTN2', 'evidence': 'IRD', 'date': '20240101', 'reasserted_below': 'PTN3'}]
    >>> losses_on_path(rows, "GO:1", ["PTN3", "PTN4"])
    []
    """
    order = {ptn: index for index, ptn in enumerate(path_below_node)}
    gains = sorted(
        order[rec["node"]]
        for rec in paint_rows
        if rec["go_id"] == term and not _is_loss(rec) and rec["node"] in order
    )
    out = []
    for rec in paint_rows:
        if rec["go_id"] != term or not _is_loss(rec) or rec["node"] not in order:
            continue
        loss = {"node": rec["node"], "evidence": rec["evidence"], "date": rec["date"]}
        lower = [index for index in gains if index > order[rec["node"]]]
        if lower:
            loss["reasserted_below"] = path_below_node[lower[0]]
        out.append(loss)
    return sorted(out, key=lambda item: order[item["node"]])


def _join(items: list[str]) -> str:
    """``a``, ``a and b``, ``a, b and c``.

    >>> _join(["1 ortholog"]), _join(["1 ortholog", "2 paralogs"]), _join(["a", "b", "c"])
    ('1 ortholog', '1 ortholog and 2 paralogs', 'a, b and c')
    """
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def _node_sentence(tree: FamilyTree, node: dict[str, Any]) -> str:
    """``PTN... is a speciation node at X, with N leaves in M species and K subfamilies``."""
    where = "the family root, " if node["is_root"] else ""
    return (
        f"PAINT node {node['node']} is {where}{place_phrase(tree, tree.an_of[node['node']])}, with "
        f"{_count(node['leaves'], 'leaf')} in {_count(node['species'], 'species')} and "
        f"{_count(node['subfamilies'], 'subfamily')}"
    )


def seed_spread(tree: FamilyTree, node_an: str, seed_leaves: list[str]) -> dict[str, Any]:
    """How the seeds of one assertion are spread below its node.

    ``seed_branches`` counts the branches directly below the node that hold a seed; a node
    whose seeds all sit in one branch was placed above the seeds' own common ancestor
    (``seed_mrca``), by ``seed_mrca_steps_below_node`` steps.
    """
    inside = [leaf for leaf in seed_leaves if tree.is_ancestor(node_an, leaf)]
    if not inside:
        return {}
    top = inside[0]
    for leaf in inside[1:]:
        top = tree.mrca(top, leaf)
    children = tree.nodes[node_an].children
    return {
        "seed_branches": len({c for c in children for leaf in inside if tree.is_ancestor(c, leaf)}),
        "node_branches": len(children),
        "seed_mrca": tree.ptn_of.get(top, top),
        "seed_mrca_steps_below_node": len(tree.path(node_an, top)) - 1,
    }


def _spread_sentence(tree: FamilyTree, spread: dict[str, Any], gene: str = "") -> str:
    """Where the seeds of one assertion sit below its node, as one sentence.

    ``spread`` holds the :func:`seed_spread` facts; with ``gene`` it also holds that row's
    facts, and the sentence says how the seeds stand relative to the gene.
    """
    steps = spread["seed_mrca_steps_below_node"]
    top = tree.an_of[spread["seed_mrca"]]
    if steps == 0:
        text = (
            f"They sit in {spread['seed_branches']} of the {spread['node_branches']} branches below "
            "the node, so the node is their common ancestor"
        )
        if gene and spread.get("target_branch"):
            sharing = spread["seeds_on_target_branch"]
            who = "the other seeds" if spread.get("self_seed") else "them"
            count = "none" if sharing == 0 else str(sharing)
            text += (
                f"; {count} of {who} share{'s' if sharing <= 1 else ''} {gene}'s own branch "
                f"below it ({spread['target_branch']})"
            )
    elif tree.is_leaf(top):
        text = f"The single seed leaf {spread['seed_mrca']} is {_count(steps, 'step')} below the PAINT node"
    else:
        text = (
            f"They all sit in one branch below the node: their common ancestor is {spread['seed_mrca']}, "
            f"{place_phrase(tree, top)}, covering {_count(len(tree.leaves_below(top)), 'leaf')}, "
            f"{_count(steps, 'step')} below the PAINT node"
        )
        if gene and "target_in_seed_clade" in spread:
            text += f"; {gene} is {'inside' if spread['target_in_seed_clade'] else 'outside'} that clade"
    return text + "."


def _summary(
    gene: str,
    row: IbaRow,
    tree: FamilyTree,
    node: dict[str, Any],
    target: dict[str, Any] | None,
    facts: dict[str, Any],
    seeds: dict[str, dict[str, Any]],
    release_name: str,
) -> str:
    """The quotable one-line statement of a row's placement."""
    parts = [
        f"{'NOT ' if row.negated else ''}{row.term_id} ({row.term_label}): {_node_sentence(tree, node)}."
    ]
    if target is None:
        parts.append(
            f"{row.accession} is not a leaf of {tree.family} in PANTHER {release_name}, so its "
            "position below the node is not known."
        )
    elif "steps" not in facts:
        parts.append(f"The node is not an ancestor of {gene} ({target['leaf']}) in PANTHER {release_name}.")
    else:
        crossing = _count(facts["duplications_on_path"], "duplication")
        if facts["transfers_on_path"]:
            crossing += f" and {_count(facts['transfers_on_path'], 'horizontal-transfer node')}"
        parts.append(
            f"{gene} ({target['leaf']}, {target['subfamily']}) is {_count(facts['steps'], 'step')} "
            f"below it, across {crossing}; path length {facts['path_length']}."
        )
    if not row.seeds:
        parts.append("The row cites no seed.")
        return " ".join(parts)
    parts.append(f"Seeds: {facts['seeds_resolved']} of {len(row.seeds)} resolved to leaves of this tree.")
    only_self = facts.get("self_seed") and facts["seeds_resolved"] == 1
    if "seed_mrca" in facts and not only_self:
        parts.append(_spread_sentence(tree, facts, gene))
    if facts.get("self_seed"):
        parts.append(
            f"{gene} is itself a seed: its own experimental annotation is among the evidence for the node."
        )
    one_to_one = facts.get("one_to_one_orthologs", 0)
    kinds = [
        (one_to_one, "one-to-one ortholog", "one-to-one orthologs"),
        (
            facts.get("orthologs", 0) - one_to_one,
            "ortholog across later duplications",
            "orthologs across later duplications",
        ),
        (facts.get("paralogs", 0), "paralog", "paralogs"),
        (facts.get("xenologs", 0), "xenolog", "xenologs"),
    ]
    kinds = [kind for kind in kinds if kind[0]]
    other = "other " if facts.get("self_seed") else ""
    if len(kinds) == 1 and kinds[0][0] == 1:
        noun = kinds[0][1]
        parts.append(f"By the tree the {other}seed is {'an' if noun[0] == 'o' else 'a'} {noun} of {gene}.")
    elif kinds:
        listed = _join([f"{n} {singular if n == 1 else plural}" for n, singular, plural in kinds])
        parts.append(f"By the tree the {other}seeds are {listed} of {gene}.")
    nearest = seeds.get(facts.get("nearest_seed") or "")
    if nearest and "mrca" in nearest:
        top = tree.an_of.get(nearest["mrca"], "")
        text = (
            f"The nearest, {nearest['id']} ({nearest['organism']}), joins {gene} at "
            f"{nearest['mrca']}, {place_phrase(tree, top)}, at tree distance {nearest['tree_distance']}"
        )
        if "identity" in nearest:
            text += f"; {round(nearest['identity'] * 100)}% identity over {nearest['aligned']} aligned columns"
        if "covers_target" in nearest:
            text += (
                f", which span {round(nearest['covers_target'] * 100)}% of {gene} and "
                f"{round(nearest['covers_seed'] * 100)}% of the seed"
            )
        parts.append(text + ".")
    for loss in facts.get("paint_losses_on_path") or []:
        text = f"PAINT {loss['evidence']} at {loss['node']} ({loss['date']}) removes this term on the path to {gene}"
        if loss.get("reasserted_below"):
            text += f", and PAINT asserts it again below the loss at {loss['reasserted_below']}"
        parts.append(text + ".")
    return " ".join(parts)


def residue_sites(
    root: Path,
    family: str,
    alignment: FamilyAlignment,
    target_an: str,
    gene: str,
    release_name: str,
) -> list[dict[str, Any]]:
    """Read the family review's curated residue sites off the family alignment for one leaf.

    Each site names an anchor protein and positions in the anchor's own numbering. The
    anchor's row and the target's row of the PANTHER alignment give the residue the target
    has in the same column: ``RETAINED`` when it is one of the expected residues,
    ``SUBSTITUTED`` when it is another, ``ABSENT`` when the target has a gap there.

    Nothing is inferred when the comparison cannot be made soundly: ``ANCHOR_MISMATCH``
    when the anchor's sequence in the release does not carry an expected residue at the
    stated position (another sequence version, or a mis-numbered site), ``NOT_ALIGNED``
    when the anchor residue lies in a stretch PANTHER left out of the alignment, and
    ``AMBIGUOUS`` when the anchor residue cannot be tied to one column.
    """
    review = root / "interpro" / "panther" / family / f"{family}-review.yaml"
    tree = alignment.tree
    if not review.exists() or target_an not in alignment.rows:
        return []
    data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
    reference = (data.get("reference_protein") or {}).get("id", "")
    target_embedding = alignment.embedding(target_an)
    target_row = alignment.rows[target_an]
    out: list[dict[str, Any]] = []
    for site in data.get("residue_sites") or []:
        anchor_id = (site.get("anchor") or {}).get("id") or reference
        name = f"PANTHER:{family}#{site.get('site_id')}"
        title = f"{name} ({site['label']})" if site.get("label") else name
        entry: dict[str, Any] = {"site": name, "label": site.get("label", ""), "anchor": anchor_id}
        terms = [(req.get("term") or {}).get("id") for req in site.get("required_for") or []]
        if any(terms):
            entry["required_for"] = [t for t in terms if t]
        anchor_an = tree.find_leaf(anchor_id) if anchor_id else None
        anchor_sequence = alignment.sequence(anchor_an) if anchor_an else None
        anchor_embedding = alignment.embedding(anchor_an) if anchor_an else None
        if anchor_an is None or anchor_sequence is None or anchor_embedding is None:
            entry["status"] = "ANCHOR_NOT_IN_ALIGNMENT"
            entry["summary"] = (
                f"{title}: anchor {anchor_id or 'unnamed'} has no usable row in the PANTHER "
                f"{release_name} alignment of {family}, so the site cannot be read for {gene}."
            )
            out.append(entry)
            continue
        positions: list[dict[str, Any]] = []
        phrases: list[str] = []
        problems: list[str] = []
        for residue in site.get("residues") or []:
            position = int(residue.get("position") or 0)
            expected = [str(x) for x in residue.get("expected") or []]
            item: dict[str, Any] = {"anchor_position": position}
            anchor_residue = anchor_sequence[position - 1] if 0 < position <= len(anchor_sequence) else ""
            if anchor_residue:
                item["anchor_residue"] = anchor_residue
            item["expected"] = expected
            if residue.get("role"):
                item["role"] = residue["role"]
            positions.append(item)
            if not anchor_residue or (expected and anchor_residue not in expected):
                item["status"] = "ANCHOR_MISMATCH"
                has = f" (it has {anchor_residue})" if anchor_residue else " (the sequence is shorter)"
                problems.append(
                    f"anchor {anchor_id} does not have {'/'.join(expected) or 'a residue'} at position "
                    f"{position} in its PANTHER {release_name} sequence{has}"
                )
                continue
            column = column_of_position(anchor_embedding, position)
            if column is None:
                item["status"] = "NOT_ALIGNED"
                problems.append(
                    f"anchor residue {anchor_residue}{position} is outside the aligned columns of the "
                    f"PANTHER {release_name} family alignment"
                )
                continue
            if not anchor_embedding[column][1]:
                item["status"] = "AMBIGUOUS"
                problems.append(
                    f"anchor residue {anchor_residue}{position} cannot be tied to one alignment column"
                )
                continue
            lead = f"anchor {anchor_id} " if not phrases else ""
            target_residue = target_row[column]
            if target_residue == "-":
                item["target_residue"] = "-"
                item["status"] = "ABSENT"
                phrases.append(f"a gap at {lead}{anchor_residue}{position} (absent)")
                continue
            item["target_residue"] = target_residue
            label = target_residue
            if target_embedding is not None:
                item["target_position"] = target_embedding[column][0]
                label = f"{target_residue}{item['target_position']}"
                if not target_embedding[column][1]:
                    item["target_position_uncertain"] = True
            kept = target_residue in expected if expected else target_residue == anchor_residue
            item["status"] = "RETAINED" if kept else "SUBSTITUTED"
            phrases.append(f"{label} at {lead}{anchor_residue}{position} ({item['status'].lower()})")
        entry["positions"] = positions
        sentences = []
        if phrases:
            sentences.append(f"in the PANTHER {release_name} family alignment {gene} has {_join(phrases)}.")
        sentences += [f"{text}, so that position is not read for {gene}." for text in problems]
        entry["summary"] = f"{title}: " + (" ".join(sentences) if sentences else "no residue listed.")
        out.append(entry)
    return out


def uniprot_sequence(uniprot_txt: str) -> str:
    """The sequence of a UniProt flat-file entry ('' when the text has no SQ block).

    >>> uniprot_sequence("ID   X\\nSQ   SEQUENCE   7 AA;\\n     MKLAG QR\\n//\\n")
    'MKLAGQR'
    >>> uniprot_sequence("ID   X\\n")
    ''
    """
    match = re.search(r"^SQ   .*\n((?:     .*\n?)+)", uniprot_txt, re.M)
    return re.sub(r"\s+", "", match.group(1)) if match else ""


def _target_doc(
    tree: FamilyTree,
    target_an: str,
    matched_by: str,
    alignment: FamilyAlignment,
    names: dict[str, str],
    uniprot_txt: str,
) -> dict[str, Any]:
    """The gene's own leaf."""
    info = tree.leaf(target_an)
    subfamily = tree.subfamily_of.get(target_an, "")
    target: dict[str, Any] = {
        "leaf": tree.ptn_of.get(target_an, target_an),
        "long_id": tree.nodes[target_an].long_id,
        "organism": info.organism,
        "subfamily": subfamily,
        "subfamily_name": names.get(f"PANTHER:{subfamily}", ""),
        "matched_by": matched_by,
        "depth": tree.depth(target_an),
        "root_distance": _round(tree.root_distance(target_an)),
    }
    sequence = alignment.sequence(target_an)
    if sequence:
        target["length"] = len(sequence)
        local = uniprot_sequence(uniprot_txt)
        if local:
            target["same_as_uniprot_file"] = local == sequence
    if target_an in alignment.rows:
        row = alignment.rows[target_an]
        target["aligned_residues"] = len(row) - row.count("-")
        if sequence and alignment.embedding(target_an) is None:
            target["row_fits_sequence"] = False
    return target


def _row_facts(
    row: IbaRow,
    tree: FamilyTree,
    ibd_an: str,
    target_an: str | None,
    seed_leaf: dict[str, str | None],
    seeds: dict[str, dict[str, Any]],
    losses: list[dict[str, str]] | None,
) -> dict[str, Any]:
    """The computed facts of one row: path to the target, seed spread, PAINT losses."""
    resolved = {token: leaf for token in row.seeds if (leaf := seed_leaf[token]) is not None}
    distinct = sorted(set(resolved.values()), key=lambda an: tree.ptn_of.get(an, an))
    facts: dict[str, Any] = {
        "seeds": list(row.seeds),
        "seeds_resolved": len(distinct),
        "seeds_unresolved": len(row.seeds) - len(resolved),
    }
    if facts["seeds_unresolved"]:
        facts["unresolved_seeds"] = [t for t in row.seeds if seed_leaf[t] is None]
    outside = sorted(t for t, leaf in resolved.items() if not tree.is_ancestor(ibd_an, leaf))
    if outside:
        facts["seeds_outside_node"] = outside
    spread = seed_spread(tree, ibd_an, distinct)
    facts.update(spread)
    if target_an is None:
        return facts
    facts["self_seed"] = target_an in distinct
    if spread:
        facts["target_in_seed_clade"] = tree.is_ancestor(tree.an_of[spread["seed_mrca"]], target_an)
    if tree.is_ancestor(ibd_an, target_an):
        path = tree.path(ibd_an, target_an)
        events = [tree.nodes[an].event for an in path[1:-1]]
        facts["steps"] = len(path) - 1
        facts["duplications_on_path"] = events.count("DUPLICATION")
        facts["transfers_on_path"] = events.count("HORIZONTAL_TRANSFER")
        facts["path_length"] = _round(sum(tree.nodes[an].branch_length or 0.0 for an in path[1:]))
        branch = path[1] if len(path) > 1 else None
        facts["target_branch"] = tree.ptn_of.get(branch, branch) if branch else None
        facts["seeds_on_target_branch"] = (
            sum(tree.is_ancestor(branch, leaf) for leaf in distinct if leaf != target_an) if branch else 0
        )
        if losses is not None and not row.negated:
            below = [tree.ptn_of.get(an, an) for an in path[1:]]
            facts["paint_losses_on_path"] = losses_on_path(losses, row.term_id, below)
    first_token = {leaf: token for token, leaf in reversed(list(resolved.items()))}
    others = [seeds[first_token[leaf]] for leaf in distinct if leaf != target_an]
    relations = Counter(seed["relation"] for seed in others)
    facts["orthologs"] = relations.get("ORTHOLOG", 0)
    facts["one_to_one_orthologs"] = sum(
        seed["relation"] == "ORTHOLOG" and not seed.get("duplications_between") for seed in others
    )
    facts["paralogs"] = relations.get("PARALOG", 0)
    facts["xenologs"] = relations.get("XENOLOG", 0)
    if relations.get("UNRESOLVED"):
        facts["unresolved_relations"] = relations["UNRESOLVED"]
    ranked = sorted((seed["tree_distance"], seed["id"]) for seed in others)
    facts["nearest_seed"] = ranked[0][1] if ranked else None
    return facts


def _build_tree_section(
    root: Path,
    gene: str,
    family: str,
    rows: list[tuple[IbaRow, str]],
    release: PantherRelease,
    uniprot_txt: str,
    names: dict[str, str],
    release_name: str,
) -> dict[str, Any]:
    """Everything about the rows whose IBD nodes sit in one family tree."""
    tree = release.tree(family)
    assert tree is not None  # the family came from the release's own node index
    alignment = FamilyAlignment(tree, release.alignment(family), release.sequences(family))
    target_an, matched_by = _find_target(tree, rows[0][0].accession, uniprot_txt)
    section: dict[str, Any] = {"family": family}
    if names.get(f"PANTHER:{family}"):
        section["family_name"] = names[f"PANTHER:{family}"]
    section["tree_leaves"] = len(tree.leaves_below(tree.root))
    section["alignment_columns"] = len(next(iter(alignment.rows.values()))) if alignment.rows else 0
    target = (
        _target_doc(tree, target_an, matched_by, alignment, names, uniprot_txt) if target_an else None
    )
    section["target"] = target
    if target_an is not None:
        section["lineage"] = _lineage(tree, target_an)
    losses = read_paint_slice(root / "interpro" / "panther" / family / f"{family}-paint.tsv")
    section["paint_slice"] = losses is not None

    seeds: dict[str, dict[str, Any]] = {}
    seed_leaf: dict[str, str | None] = {}
    for row, _ in rows:
        for token in row.seeds:
            if token not in seed_leaf:
                leaf, how = resolve_seed(token, tree, release)
                seed_leaf[token] = leaf
                if leaf is not None:
                    seeds[token] = _seed_entry(token, tree, leaf, target_an, alignment, how)

    node_docs: dict[str, dict[str, Any]] = {}
    row_docs: list[dict[str, Any]] = []
    for row, ibd_an in rows:
        ptn = tree.ptn_of.get(ibd_an, ibd_an)
        if ptn not in node_docs:
            node_docs[ptn] = describe_node(tree, ibd_an, names, target_an)
        doc: dict[str, Any] = {
            "term": {"id": row.term_id, "label": row.term_label},
            "aspect": row.aspect,
            "qualifier": row.qualifier,
            "negated": row.negated,
            "ibd_node": ptn,
            "with_from": row.with_from,
        }
        if len(row.nodes) > 1:
            doc["other_nodes"] = [n for n in row.nodes if n != ptn]
        facts = _row_facts(row, tree, ibd_an, target_an, seed_leaf, seeds, losses)
        doc.update(facts)
        doc["summary"] = _summary(gene, row, tree, node_docs[ptn], target, facts, seeds, release_name)
        row_docs.append(doc)

    section["nodes"] = sorted(node_docs.values(), key=lambda n: (n["depth"], n["node"]))
    section["seeds"] = sorted(seeds.values(), key=lambda s: (s.get("tree_distance", -1.0), s["id"]))
    section["rows"] = row_docs
    if target_an is not None:
        sites = residue_sites(root, family, alignment, target_an, gene, release_name)
        if sites:
            section["residue_sites"] = sites
    return section


def build_gene_phylo(
    root: Path, organism: str, gene: str, release: PantherRelease
) -> dict[str, Any] | None:
    """Build the phylogenetic extract of one gene, or None when it has no IBA row."""
    folder = root / "genes" / organism / gene
    rows = read_iba_rows(folder / f"{gene}-goa.tsv")
    if not rows:
        return None
    uniprot = folder / f"{gene}-uniprot.txt"
    uniprot_txt = uniprot.read_text(encoding="utf-8") if uniprot.exists() else ""
    names = panther_names(root)
    manifest = release.manifest()
    release_name = manifest.get("release", "")

    by_family: dict[str, list[tuple[IbaRow, str]]] = {}
    unplaced: list[dict[str, Any]] = []
    for row in rows:
        term = {"id": row.term_id, "label": row.term_label}
        located = [loc for ptn in row.nodes if (loc := release.locate_node(ptn)) is not None]
        if not located:
            reason = (
                f"{row.nodes[0]} is not a node of any PANTHER {release_name} tree"
                if row.nodes
                else "the row cites no PANTHER node"
            )
            unplaced.append({"term": term, "with_from": row.with_from, "reason": reason})
            continue
        # With several nodes, use the one closest to the leaves (the most specific assertion).
        family = located[0][0]
        tree = release.tree(family)
        assert tree is not None
        ibd_an = max((an for fam, an in located if fam == family), key=tree.depth)
        by_family.setdefault(family, []).append((row, ibd_an))

    doc: dict[str, Any] = {
        "gene": f"{organism}/{gene}",
        "accession": f"UniProtKB:{rows[0].accession}",
        "panther_release": release_name,
    }
    if manifest.get("source_last_modified"):
        doc["panther_source_last_modified"] = manifest["source_last_modified"]
    doc["iba_rows"] = len(rows)
    doc["trees"] = [
        _build_tree_section(root, gene, family, family_rows, release, uniprot_txt, names, release_name)
        for family, family_rows in sorted(by_family.items())
    ]
    if unplaced:
        doc["unplaced_rows"] = unplaced
    return doc


def build_family_nodes(root: Path, family: str, release: PantherRelease) -> dict[str, Any] | None:
    """Describe every node of a family's PAINT slice; None when there is no slice or tree.

    For each node: what it covers, and for each term asserted there whether its seeds
    bracket the node or all sit in one branch below it. Nodes of the slice that belong to
    another family's tree are listed under ``other_tree_nodes`` rather than dropped.
    """
    paint_rows = read_paint_slice(root / "interpro" / "panther" / family / f"{family}-paint.tsv")
    tree = release.tree(family)
    if tree is None or paint_rows is None:
        return None
    names = panther_names(root)
    manifest = release.manifest()
    doc: dict[str, Any] = {"family": family}
    if names.get(f"PANTHER:{family}"):
        doc["family_name"] = names[f"PANTHER:{family}"]
    doc["panther_release"] = manifest.get("release", "")
    if manifest.get("source_last_modified"):
        doc["panther_source_last_modified"] = manifest["source_last_modified"]
    doc["tree_leaves"] = len(tree.leaves_below(tree.root))
    doc["tree_species"] = _species(tree, tree.root)

    by_node: dict[str, list[dict[str, str]]] = {}
    for rec in paint_rows:
        by_node.setdefault(rec["node"], []).append(rec)
    nodes: list[dict[str, Any]] = []
    elsewhere: list[str] = []
    for ptn, recs in by_node.items():
        an = tree.an_of.get(ptn)
        if an is None:
            elsewhere.append(ptn)
            continue
        node = describe_node(tree, an, names)
        assertions = []
        for rec in recs:
            negated = rec["evidence"] in LOSS_CODES or rec["negated"] == "true"
            tokens = [t for t in rec["seeds"].split("|") if t]
            item: dict[str, Any] = {
                "term": rec["go_id"],
                "aspect": rec["aspect"],
                "evidence": rec["evidence"],
                "negated": negated,
                "date": rec["date"],
            }
            lead = f"{ptn} {'NOT ' if negated else ''}{rec['go_id']} {rec['evidence']}: {_node_sentence(tree, node)}."
            if negated:
                item["blocks"] = [t.split(":", 1)[1] for t in tokens if t.startswith("PANTHER:")]
                item["summary"] = f"{lead} It stops the term asserted at {_join(item['blocks']) if item['blocks'] else 'an unnamed node'}."
            else:
                seed_tokens = [t for t in tokens if not t.startswith("PANTHER:")]
                leaves = [leaf for t in seed_tokens if (leaf := resolve_seed(t, tree, release)[0]) is not None]
                distinct = sorted(set(leaves), key=lambda x: tree.ptn_of.get(x, x))
                item["seeds"] = len(seed_tokens)
                item["seeds_resolved"] = len(distinct)
                spread = seed_spread(tree, an, distinct)
                item.update(spread)
                text = f"{lead} Seeds: {len(distinct)} of {len(seed_tokens)} resolved to leaves of this tree."
                if spread:
                    text += " " + _spread_sentence(tree, spread)
                item["summary"] = text
            assertions.append(item)
        node["assertions"] = sorted(assertions, key=lambda a: (a["term"], a["evidence"]))
        nodes.append(node)
    doc["nodes"] = sorted(nodes, key=lambda n: (n["depth"], n["node"]))
    if elsewhere:
        doc["other_tree_nodes"] = sorted(elsewhere)
    return doc


class _Literal(str):
    """A string written as a YAML literal block, so its text is in the file verbatim."""


class _Flow(dict):
    """A mapping written on one line."""


class _FlowList(list):
    """A list of scalars written on one line."""


class _Dumper(yaml.SafeDumper):
    """SafeDumper with one-line records and verbatim summaries."""


_Dumper.add_representer(
    _Literal,
    lambda dumper, value: dumper.represent_scalar("tag:yaml.org,2002:str", str(value), style="|"),
)
_Dumper.add_representer(
    _Flow,
    lambda dumper, value: dumper.represent_mapping("tag:yaml.org,2002:map", value.items(), flow_style=True),
)

_Dumper.add_representer(
    _FlowList,
    lambda dumper, value: dumper.represent_sequence("tag:yaml.org,2002:seq", value, flow_style=True),
)

#: Keys whose mapping (or list of mappings) is one record per line.
_FLOW_KEYS = frozenset(
    {"target", "lineage", "seeds", "branches", "top_subfamilies", "term", "paint_losses_on_path", "positions"}
)


def _styled(value: Any, key: str = "") -> Any:
    """Copy data for dumping: records under ``_FLOW_KEYS`` on one line, summaries literal."""
    if isinstance(value, dict):
        if key in _FLOW_KEYS:
            return _Flow(value)
        return {k: _styled(v, k) for k, v in value.items()}
    if isinstance(value, list):
        if key in _FLOW_KEYS and value and all(isinstance(item, dict) for item in value):
            return [_Flow(item) for item in value]
        if value and not any(isinstance(item, (dict, list)) for item in value):
            return _FlowList(value)
        return [_styled(item, "") for item in value]
    if key == "summary" and isinstance(value, str):
        return _Literal(value)
    return value


def _dump(doc: dict[str, Any], header: str) -> str:
    body = yaml.dump(
        _styled(doc),
        Dumper=_Dumper,
        sort_keys=False,
        default_flow_style=False,
        width=1_000_000,
        allow_unicode=True,
    )
    return header + body


def render(doc: dict[str, Any]) -> str:
    """Serialise a gene extract as YAML: one record per line, summaries verbatim."""
    return _dump(
        doc,
        f"# Phylogenetic context of the IBA rows of {doc['gene']}: PANTHER {doc['panther_release']} tree\n"
        "# placement and family-alignment comparison with the seeds. Derived file; do not edit.\n"
        f"# Regenerate with: just phylo {doc['gene'].replace('/', ' ')}\n",
    )


def render_family(doc: dict[str, Any]) -> str:
    """Serialise a family node listing as YAML."""
    return _dump(
        doc,
        f"# PAINT nodes of {doc['family']} in the PANTHER {doc['panther_release']} tree: what each node\n"
        "# covers and how its seeds are spread below it. Derived file; do not edit.\n"
        f"# Regenerate with: just phylo-family {doc['family']}\n",
    )


def phylo_path(root: Path, organism: str, gene: str) -> Path:
    """Where a gene's extract lives."""
    return root / "genes" / organism / gene / f"{gene}-phylo.yaml"


def family_nodes_path(root: Path, family: str) -> Path:
    """Where a family's node listing lives."""
    return root / "interpro" / "panther" / family / f"{family}-tree-nodes.yaml"


def write_gene_phylo(root: Path, organism: str, gene: str, release: PantherRelease) -> Path | None:
    """Write ``GENE-phylo.yaml``; returns its path, or None when the gene has no IBA row."""
    doc = build_gene_phylo(root, organism, gene, release)
    if doc is None:
        return None
    path = phylo_path(root, organism, gene)
    path.write_text(render(doc), encoding="utf-8")
    return path


def write_family_nodes(root: Path, family: str, release: PantherRelease) -> Path | None:
    """Write ``<PTHR>-tree-nodes.yaml``; None when the family has no PAINT slice or no tree."""
    doc = build_family_nodes(root, family, release)
    if doc is None:
        return None
    path = family_nodes_path(root, family)
    path.write_text(render_family(doc), encoding="utf-8")
    return path


def _pairs(args: argparse.Namespace, parser: argparse.ArgumentParser) -> list[tuple[str, str]]:
    """The ``(organism, gene)`` pairs named on the command line or in ``--genes-file``."""
    if args.genes_file:
        pairs = []
        for line in args.genes_file.read_text().splitlines():
            parts = line.replace("/", " ").split()
            if len(parts) >= 2 and not line.startswith("#"):
                pairs.append((parts[0], parts[1]))
        return pairs
    if args.organism and args.gene:
        return [(args.organism, args.gene)]
    parser.error("give ORGANISM GENE, --genes-file or --family")
    return []


def main(argv: Sequence[str] | None = None) -> int:
    """Write the extract for ``ORGANISM GENE``, for ``--genes-file`` pairs, or for ``--family``."""
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    parser.add_argument("organism", nargs="?")
    parser.add_argument("gene", nargs="?")
    parser.add_argument("--genes-file", type=Path, help="lines of 'ORGANISM GENE' (or ORGANISM/GENE)")
    parser.add_argument("--family", action="append", default=[], help="write a family node listing")
    parser.add_argument("--families-file", type=Path, help="one PANTHER family id per line")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--db", type=Path, default=None, help="release database (default: under --root/.cache)")
    args = parser.parse_args(list(argv) if argv is not None else None)
    release = PantherRelease(args.db or args.root / DEFAULT_DB)
    families = list(args.family)
    if args.families_file:
        families += [x.strip() for x in args.families_file.read_text().splitlines() if x.strip()]
    if families:
        written = [f for f in families if write_family_nodes(args.root, f, release) is not None]
        for family in families if len(families) == 1 else []:
            print(family_nodes_path(args.root, family) if written else f"{family}: no PAINT slice or tree")
        if len(families) > 1:
            print(f"{len(written)} of {len(families)} family listings written", file=sys.stderr)
        return 0
    pairs = _pairs(args, parser)
    written_genes = 0
    for organism, gene in pairs:
        path = write_gene_phylo(args.root, organism, gene, release)
        written_genes += path is not None
        if len(pairs) == 1:
            print(path if path else f"{organism}/{gene}: no IBA rows; nothing written")
    if len(pairs) > 1:
        print(f"{written_genes} written, {len(pairs) - written_genes} without IBA rows", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
