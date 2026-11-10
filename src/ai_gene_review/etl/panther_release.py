"""PANTHER release trees and family alignments, read from the TreeGrafter data bundle.

A PAINT curator places an IBD on a node of a PANTHER family tree while looking at the
whole tree (speciation, duplication and transfer events, branch lengths) and at the family
alignment. ``IBD.gaf`` and the per-family ``<PTHR>-paint.tsv`` slices keep only the node
id, the term and the seed list, so a reviewer who wants to argue with a node placement has
nothing to argue from. This module reads the release files that hold the rest:

``PANTHER<release>_data.tar.gz`` (https://data.pantherdb.org/ftp/downloads/TreeGrafter/)

* ``Tree_MSF/<PTHR>.tree`` -- Newick with NHX annotations on every internal node
  (``Ev=0>1`` speciation with ``S=<taxon>``, ``Ev=1>0`` duplication, ``Ev=0>0`` horizontal
  transfer, ``ID=AN<n>``), then one ``AN<n>:<ORG>|<DB>=<id>|UniProtKB=<ACC>;`` line per leaf;
* ``Tree_MSF/<PTHR>.AN.fasta`` -- the family alignment, one aligned row per leaf;
* ``PAINT_Annotations/PAINT_Annotatations_TOTAL.txt`` -- for every node, its persistent
  ``PTN`` id and its subfamily.

``PANTHER<release>_fasta.tgz`` (https://data.pantherdb.org/ftp/panther_library/)

* ``<PTHR>.fasta`` -- the full-length sequence of every leaf. The alignment rows hold only
  the residues PANTHER placed in the family model's match columns (inserted stretches are
  dropped), so a residue's number in its own protein cannot be read by counting along a
  row. :func:`embed_row` recovers it by laying the row back onto the full sequence.

The live ``treeinfo`` and ``familymsa`` services return the same information one family at
a time, but time out on many families; the bundle is release-pinned and read once.
``fetch_release`` streams it into one SQLite file under the git-ignored ``.cache/``
(the three wanted parts come first in the archive, so the download stops after them
unless ``full`` is set). ``PantherRelease`` then answers "which family and node is this
PTN", "which leaf is this protein", and hands back a :class:`FamilyTree` or an alignment.

Usage:
    uv run python -m ai_gene_review.etl.panther_release fetch
    uv run python -m ai_gene_review.etl.panther_release info
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
import tarfile
import zlib
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import IO, Iterable, Iterator, NamedTuple, Sequence, cast

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE

BUNDLE_URL = (
    "https://data.pantherdb.org/ftp/downloads/TreeGrafter/"
    f"PANTHER{PANTHER_RELEASE}_data.tar.gz"
)
SEQUENCES_URL = (
    f"https://data.pantherdb.org/ftp/panther_library/{PANTHER_RELEASE}/"
    f"PANTHER{PANTHER_RELEASE}_fasta.tgz"
)
DEFAULT_DB = Path(".cache") / "panther_release" / f"PANTHER{PANTHER_RELEASE}.sqlite"

#: UniProt's Arabidopsis reference proteome with ordered locus names. GOA writes
#: Arabidopsis seeds as ``AGI_LocusCode:AT5G16440``, an identifier the PANTHER long ids
#: (``ARATH|TAIR=locus=...|UniProtKB=...``) do not carry.
ARATH_LOCUS_URL = (
    "https://rest.uniprot.org/uniprotkb/stream"
    "?query=%28proteome%3AUP000006548%29&fields=accession%2Cgene_oln&format=tsv"
)

NODE_TABLE_MEMBER = "/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt"
TREE_DIR = "/Tree_MSF/"

#: NHX ``Ev=<duplications>><speciations>`` codes used in PANTHER tree files.
EVENTS = {"0>1": "SPECIATION", "1>0": "DUPLICATION", "0>0": "HORIZONTAL_TRANSFER"}
LEAF = "LEAF"
UNKNOWN = "UNKNOWN"

#: PANTHER long-id database name -> prefix GO uses for the same identifier in WITH/FROM.
GO_PREFIX = {
    "MGI": "MGI",
    "RGD": "RGD",
    "SGD": "SGD",
    "FlyBase": "FB",
    "WormBase": "WB",
    "ZFIN": "ZFIN",
    "PomBase": "PomBase",
    "dictyBase": "dictyBase",
    "TAIR": "TAIR",
    "CGD": "CGD",
    "Xenbase": "Xenbase",
    "HGNC": "HGNC",
}

_NHX = re.compile(r"^&&NHX:(.*)$")
_STOP = frozenset(",():[;")


@dataclass(frozen=True)
class TreeNode:
    """One node of a PANTHER family tree.

    ``event`` is SPECIATION, DUPLICATION, HORIZONTAL_TRANSFER or UNKNOWN for an internal
    node and LEAF for a leaf. ``taxon`` is the ``S=`` label, which PANTHER writes on
    speciation nodes only. ``long_id`` is the leaf's ``ORG|DB=id|UniProtKB=ACC`` string.
    """

    an: str
    parent: str | None
    children: tuple[str, ...]
    branch_length: float | None
    event: str
    taxon: str = ""
    long_id: str = ""


class LeafId(NamedTuple):
    """The parts of a PANTHER long id ``ORG|DB=id|UniProtKB=ACC``."""

    organism: str
    db: str
    gene_id: str
    accession: str

    def keys(self) -> set[str]:
        """Identifiers a GOA WITH/FROM column may use for this leaf.

        >>> sorted(parse_long_id("RAT|RGD=620403|UniProtKB=Q9JK72").keys())
        ['RGD:620403', 'UniProtKB:Q9JK72']
        """
        local = self.gene_id.replace("=", ":")
        out = {f"{self.db}:{local}"}
        if self.accession:
            out.add(f"UniProtKB:{self.accession}")
        if self.db in GO_PREFIX:
            out.add(f"{GO_PREFIX[self.db]}:{local}")
        return out


def parse_long_id(long_id: str) -> LeafId:
    """Split a PANTHER long id into organism, gene database, gene id and accession.

    >>> parse_long_id("HUMAN|HGNC=1613|UniProtKB=O14618")
    LeafId(organism='HUMAN', db='HGNC', gene_id='1613', accession='O14618')
    """
    parts = long_id.split("|")
    organism = parts[0]
    db, gene_id, accession = "", "", ""
    for part in parts[1:]:
        name, _, value = part.partition("=")
        if name == "UniProtKB":
            accession = value
        elif not db:
            db, gene_id = name, value
    return LeafId(organism, db, gene_id, accession)


def _nhx_attributes(comment: str) -> dict[str, str]:
    """Key/value pairs of one ``&&NHX:...`` comment (empty for any other comment)."""
    match = _NHX.match(comment)
    if not match:
        return {}
    pairs = (item.partition("=") for item in match.group(1).split(":"))
    return {key: value for key, sep, value in pairs if sep}


def parse_tree(text: str) -> dict[str, TreeNode]:
    """Parse a PANTHER ``.tree`` file into ``{AN id: TreeNode}``.

    The first line is the Newick string; the following lines map each leaf to its long
    id. Internal nodes take their id from the NHX ``ID`` attribute, so one without it is
    an error rather than a silently renumbered node. The parser is iterative: PANTHER
    trees can be thousands of leaves deep on one side.

    >>> t = parse_tree("(AN1:0.5,AN2:0.25)[&&NHX:Ev=1>0:ID=AN0];\\nAN1:A|Gene=x|UniProtKB=P1;\\nAN2:A|Gene=y|UniProtKB=P2;")
    >>> t["AN0"].event, t["AN0"].children, t["AN2"].branch_length, t["AN2"].long_id
    ('DUPLICATION', ('AN1', 'AN2'), 0.25, 'A|Gene=y|UniProtKB=P2')
    """
    lines = text.strip().split("\n")
    newick = lines[0].strip()
    long_ids: dict[str, str] = {}
    for line in lines[1:]:
        line = line.strip().rstrip(";")
        if line:
            an, _, long_id = line.partition(":")
            long_ids[an] = long_id

    raw: dict[str, dict] = {}
    open_children: list[list[str]] = []
    i, n = 0, len(newick)

    def read_suffix(pos: int) -> tuple[float | None, dict[str, str], int]:
        """Read ``[label][:length][[comment]]`` after a leaf name or a ``)``."""
        while pos < n and newick[pos] not in _STOP:  # an internal label, unused by PANTHER
            pos += 1
        length: float | None = None
        if pos < n and newick[pos] == ":":
            end = pos + 1
            while end < n and newick[end] not in _STOP:
                end += 1
            length = float(newick[pos + 1 : end])
            pos = end
        attrs: dict[str, str] = {}
        if pos < n and newick[pos] == "[":
            end = newick.index("]", pos)
            attrs = _nhx_attributes(newick[pos + 1 : end])
            pos = end + 1
        return length, attrs, pos

    def attach(an: str) -> None:
        if open_children:
            open_children[-1].append(an)

    while i < n:
        char = newick[i]
        if char == "(":
            open_children.append([])
            i += 1
        elif char == ")":
            children = open_children.pop()
            length, attrs, i = read_suffix(i + 1)
            if "ID" not in attrs:
                raise ValueError(f"internal node with children {children[:3]} has no NHX ID")
            an = attrs["ID"]
            event = EVENTS.get(attrs.get("Ev", ""), UNKNOWN)
            raw[an] = {
                "children": tuple(children),
                "length": length,
                "event": event,
                "taxon": attrs.get("S", ""),
            }
            for child in children:
                raw[child]["parent"] = an
            attach(an)
        elif char in ",;":
            i += 1
        else:
            end = i
            while end < n and newick[end] not in _STOP:
                end += 1
            an = newick[i:end]
            length, _, i = read_suffix(end)
            raw[an] = {"children": (), "length": length, "event": LEAF, "taxon": ""}
            attach(an)

    return {
        an: TreeNode(
            an=an,
            parent=item.get("parent"),
            children=item["children"],
            branch_length=item["length"],
            event=item["event"],
            taxon=item["taxon"],
            long_id=long_ids.get(an, ""),
        )
        for an, item in raw.items()
    }


def parse_node_table(lines: Iterable[str]) -> dict[str, dict[str, tuple[str, str]]]:
    """Parse node-table lines into ``{family: {AN id: (PTN id, subfamily id)}}``.

    Each line is ``<PTHR>:<AN>\\t<PTHR>:<SF>  <GO ids>\\t<PTN>``. The ``root`` line repeats
    ``AN0`` and is skipped.

    >>> parse_node_table(["PTHR1:root\\tPTHR1:SF2  GO:1;  \\tPTN9", "PTHR1:AN0\\tPTHR1:SF2  GO:1;  \\tPTN9"])
    {'PTHR1': {'AN0': ('PTN9', 'PTHR1:SF2')}}
    """
    table: dict[str, dict[str, tuple[str, str]]] = {}
    for line in lines:
        for family, an, ptn, subfamily in _node_rows([line]):
            table.setdefault(family, {})[an] = (ptn, subfamily)
    return table


def _node_rows(lines: Iterable[str]) -> Iterator[tuple[str, str, str, str]]:
    """Yield ``(family, AN, PTN, subfamily)`` for each node-table line except ``root``."""
    for line in lines:
        cols = line.rstrip("\n").split("\t")
        if len(cols) < 3:
            continue
        family, _, an = cols[0].partition(":")
        if an == "root":
            continue
        yield family, an, cols[2].strip(), cols[1].split(" ", 1)[0].strip()


def parse_fasta(text: str) -> dict[str, str]:
    """Parse an aligned FASTA into ``{AN id: aligned row}``.

    >>> parse_fasta(">AN1\\nMK-\\nL\\n>AN2\\nMKQL\\n")
    {'AN1': 'MK-L', 'AN2': 'MKQL'}
    """
    rows: dict[str, list[str]] = {}
    current: list[str] | None = None
    for line in text.splitlines():
        if line.startswith(">"):
            current = rows.setdefault(line[1:].strip(), [])
        elif current is not None:
            current.append(line.strip())
    return {name: "".join(parts) for name, parts in rows.items()}


@dataclass(frozen=True)
class AlignmentStats:
    """How two rows of one alignment compare, from the first row's point of view.

    Regions are 1-based inclusive ranges counted along the row's own residues (the row
    with gaps removed). A row leaves out the stretches PANTHER did not align, so these are
    not positions in the protein: convert them with :func:`embed_row` before reporting.
    """

    aligned: int
    identical: int
    self_length: int
    other_length: int
    self_regions_missing_in_other: list[tuple[int, int]]
    other_regions_missing_in_self: list[tuple[int, int]]

    @property
    def identity(self) -> float:
        """Identical residues over columns where both rows have a residue."""
        return self.identical / self.aligned if self.aligned else 0.0

    @property
    def coverage_of_self(self) -> float:
        """Share of the first row's residues aligned to a residue of the other row."""
        return self.aligned / self.self_length if self.self_length else 0.0

    @property
    def coverage_of_other(self) -> float:
        """Share of the other row's residues aligned to a residue of the first row."""
        return self.aligned / self.other_length if self.other_length else 0.0


def _unmatched_regions(row: str, partner: str, min_region: int) -> list[tuple[int, int]]:
    """Runs of at least ``min_region`` residues of ``row`` with no aligned ``partner`` residue.

    A run ends only at a column where both rows have a residue, so an insertion in
    ``partner`` inside the run does not split it.
    """
    regions: list[tuple[int, int]] = []
    position = 0
    start: int | None = None
    for a, b in zip(row, partner):
        if a == "-":
            continue
        position += 1
        if b == "-":
            if start is None:
                start = position
        elif start is not None:
            if position - start >= min_region:
                regions.append((start, position - 1))
            start = None
    if start is not None and position - start + 1 >= min_region:
        regions.append((start, position))
    return regions


def pairwise_alignment_stats(self_row: str, other_row: str, min_region: int = 30) -> AlignmentStats:
    """Compare two rows of the same alignment column by column.

    >>> s = pairwise_alignment_stats("MKL-", "MRLQ")
    >>> s.aligned, s.identical, round(s.identity, 3), s.coverage_of_other
    (3, 2, 0.667, 0.75)
    """
    if len(self_row) != len(other_row):
        raise ValueError("alignment rows must have the same length")
    aligned = identical = 0
    for a, b in zip(self_row, other_row):
        if a != "-" and b != "-":
            aligned += 1
            identical += a == b
    return AlignmentStats(
        aligned=aligned,
        identical=identical,
        self_length=len(self_row) - self_row.count("-"),
        other_length=len(other_row) - other_row.count("-"),
        self_regions_missing_in_other=_unmatched_regions(self_row, other_row, min_region),
        other_regions_missing_in_self=_unmatched_regions(other_row, self_row, min_region),
    )


def embed_row(row: str, full: str) -> list[tuple[int, bool]] | None:
    """Lay an alignment row back onto its full-length sequence.

    Returns one ``(position, certain)`` pair per alignment column: the 1-based position in
    ``full`` of the residue in that column (0 for a gap), and whether that position is
    forced. A row is the full sequence with some stretches left out, so its residues are a
    subsequence of ``full``; where the same residue could sit on either side of a
    left-out stretch the earliest position is given and ``certain`` is False. An ``X`` in
    the row stands for any residue (PANTHER writes selenocysteine that way). Returns None
    when the row is not a subsequence of ``full`` at all (a different sequence version).

    >>> embed_row("-KL-M", "MAKLGM")
    [(0, True), (3, True), (4, True), (0, True), (6, True)]
    >>> embed_row("AG", "AGG")       # which G is not determined
    [(1, True), (2, False)]
    >>> embed_row("GXG", "MGUGK")    # X is the selenocysteine
    [(2, True), (3, True), (4, True)]
    >>> embed_row("AW", "AGG") is None
    True
    """
    residues = [c for c in row if c != "-"]
    left: list[int] = []
    cursor = 0
    for residue in residues:
        if residue != "X":
            cursor = full.find(residue, cursor)
        if cursor < 0 or cursor >= len(full):
            return None
        cursor += 1
        left.append(cursor)
    right: list[int] = []
    cursor = len(full)
    for residue in reversed(residues):
        cursor = cursor - 1 if residue == "X" else full.rfind(residue, 0, cursor)
        right.append(cursor + 1)
    right.reverse()
    out: list[tuple[int, bool]] = []
    index = 0
    for char in row:
        if char == "-":
            out.append((0, True))
        else:
            out.append((left[index], left[index] == right[index]))
            index += 1
    return out


def column_of_position(embedding: list[tuple[int, bool]], position: int) -> int | None:
    """The alignment column that holds a sequence position, or None when it is not aligned.

    >>> column_of_position([(0, True), (3, True), (4, False)], 3)
    1
    >>> column_of_position([(0, True), (3, True), (4, False)], 5) is None
    True
    """
    for column, (pos, _) in enumerate(embedding):
        if pos == position:
            return column
    return None


@dataclass
class FamilyTree:
    """A PANTHER family tree with its persistent node ids and subfamilies.

    Nodes are addressed by their ``AN`` id; ``ptn_of`` and ``an_of`` translate to and from
    the persistent ``PTN`` ids that PAINT and GOA use.
    """

    family: str
    nodes: dict[str, TreeNode]
    root: str
    ptn_of: dict[str, str]
    subfamily_of: dict[str, str]
    an_of: dict[str, str] = field(default_factory=dict)
    _leaf_keys: dict[str, str] = field(default_factory=dict, repr=False)
    _leaves_below: dict[str, list[str]] = field(default_factory=dict, repr=False)

    @classmethod
    def build(
        cls, family: str, nodes: dict[str, TreeNode], table: dict[str, tuple[str, str]]
    ) -> "FamilyTree":
        """Join parsed tree nodes with the family's node-table rows."""
        roots = [an for an, node in nodes.items() if node.parent is None]
        if len(roots) != 1:
            raise ValueError(f"{family}: expected one root, found {len(roots)}")
        ptn_of = {an: ptn for an, (ptn, _) in table.items() if an in nodes}
        tree = cls(
            family=family,
            nodes=nodes,
            root=roots[0],
            ptn_of=ptn_of,
            subfamily_of={an: sf for an, (_, sf) in table.items() if an in nodes},
            an_of={ptn: an for an, ptn in ptn_of.items()},
        )
        for an, node in nodes.items():
            if node.event == LEAF and node.long_id:
                for key in parse_long_id(node.long_id).keys():
                    tree._leaf_keys.setdefault(key, an)
        return tree

    def is_leaf(self, an: str) -> bool:
        """True when ``an`` is a leaf."""
        return self.nodes[an].event == LEAF

    def leaf(self, an: str) -> LeafId:
        """The parsed long id of leaf ``an``."""
        return parse_long_id(self.nodes[an].long_id)

    def lineage(self, an: str) -> list[str]:
        """Nodes from the root down to ``an``, both included."""
        path = [an]
        while (parent := self.nodes[path[-1]].parent) is not None:
            path.append(parent)
        return path[::-1]

    def depth(self, an: str) -> int:
        """Number of edges between the root and ``an``."""
        return len(self.lineage(an)) - 1

    def is_ancestor(self, ancestor: str, an: str) -> bool:
        """True when ``ancestor`` is ``an`` or lies above it."""
        return ancestor in self.lineage(an)

    def path(self, ancestor: str, an: str) -> list[str]:
        """Nodes from ``ancestor`` down to ``an``, both included."""
        lineage = self.lineage(an)
        if ancestor not in lineage:
            raise ValueError(f"{ancestor} is not an ancestor of {an} in {self.family}")
        return lineage[lineage.index(ancestor) :]

    def mrca(self, a: str, b: str) -> str:
        """Most recent common ancestor of two nodes (a node is its own ancestor)."""
        on_a = set(self.lineage(a))
        node: str | None = b
        while node is not None and node not in on_a:
            node = self.nodes[node].parent
        if node is None:
            raise ValueError(f"{a} and {b} share no ancestor in {self.family}")
        return node

    def root_distance(self, an: str) -> float:
        """Sum of branch lengths from the root to ``an``."""
        return sum(self.nodes[x].branch_length or 0.0 for x in self.lineage(an))

    def distance(self, a: str, b: str) -> float:
        """Sum of branch lengths on the path between two nodes."""
        top = self.mrca(a, b)
        return self.root_distance(a) + self.root_distance(b) - 2 * self.root_distance(top)

    def leaves_below(self, an: str) -> list[str]:
        """Leaves at or below ``an``, in tree order."""
        if an in self._leaves_below:
            return self._leaves_below[an]
        out: list[str] = []
        stack = [an]
        while stack:
            node = stack.pop()
            children = self.nodes[node].children
            if children:
                stack.extend(reversed(children))
            else:
                out.append(node)
        self._leaves_below[an] = out
        return out

    def find_leaf(self, token: str) -> str | None:
        """The leaf a GOA WITH/FROM token names, or None.

        Tokens are matched exactly on the identifiers in the leaf long ids
        (``UniProtKB:ACC``, ``MGI:MGI:n``, ``FB:FBgn...``). A token from a database
        PANTHER does not use is matched on its local id when exactly one leaf carries it.
        """
        if token in self._leaf_keys:
            return self._leaf_keys[token]
        prefix, _, local = token.partition(":")
        if not local or prefix in GO_PREFIX.values() or prefix == "UniProtKB":
            return None
        hits = [
            an
            for an, node in self.nodes.items()
            if node.event == LEAF and node.long_id and parse_long_id(node.long_id).gene_id == local
        ]
        return hits[0] if len(hits) == 1 else None

    def taxon_bounds(self, an: str) -> tuple[str, list[str]]:
        """Where a node sits in the species tree: ``(postdates, predates)``.

        PANTHER labels only speciation nodes with a taxon. A speciation node is its own
        bound. A duplication or transfer node happened after the nearest speciation above
        it (``postdates``) and before the first speciation on each branch below it
        (``predates``; a branch that reaches a leaf first contributes that leaf's
        organism code).
        """
        node = self.nodes[an]
        if node.event == "SPECIATION" and node.taxon:
            return node.taxon, [node.taxon]
        postdates = ""
        parent = node.parent
        while parent is not None:
            above = self.nodes[parent]
            if above.event == "SPECIATION" and above.taxon:
                postdates = above.taxon
                break
            parent = above.parent
        predates: set[str] = set()
        stack = list(node.children) if node.children else [an]
        while stack:
            below = self.nodes[stack.pop()]
            if below.event == "SPECIATION" and below.taxon:
                predates.add(below.taxon)
            elif below.event == LEAF:
                predates.add(parse_long_id(below.long_id).organism)
            else:
                stack.extend(below.children)
        return postdates, sorted(predates)


_SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT) WITHOUT ROWID;
CREATE TABLE family (family TEXT PRIMARY KEY, tree BLOB, msa BLOB, sequences BLOB) WITHOUT ROWID;
CREATE TABLE node (ptn TEXT NOT NULL, family TEXT NOT NULL, an TEXT NOT NULL, subfamily TEXT NOT NULL);
CREATE TABLE leaf (accession TEXT NOT NULL, family TEXT NOT NULL, an TEXT NOT NULL);
CREATE TABLE alias (key TEXT NOT NULL, accession TEXT NOT NULL);
"""
_INDEXES = """
CREATE INDEX node_ptn ON node (ptn);
CREATE INDEX node_family ON node (family);
CREATE INDEX leaf_accession ON leaf (accession);
CREATE INDEX alias_key ON alias (key);
"""


def _pack(text: str) -> bytes:
    return zlib.compress(text.encode(), 6)


def _unpack(blob: bytes) -> str:
    return zlib.decompress(blob).decode()


def _store(con: sqlite3.Connection, family: str, column: str, text: str) -> None:
    """Set one text column of a family row, creating the row when needed."""
    con.execute(
        f"INSERT INTO family (family, {column}) VALUES (?, ?) "  # noqa: S608 - column is a literal
        f"ON CONFLICT(family) DO UPDATE SET {column} = excluded.{column}",
        (family, _pack(text)),
    )


def _store_node_table(con: sqlite3.Connection, lines: Iterable[bytes], batch: int = 50000) -> int:
    """Store every node-table row; returns the number of nodes.

    A family's rows are not contiguous in PANTHER's file (its internal nodes and its
    leaves sit in different places), so rows go into one indexed table rather than into
    a per-family record written when the family name changes.
    """
    count = 0
    rows: list[tuple[str, str, str, str]] = []
    statement = "INSERT INTO node (ptn, family, an, subfamily) VALUES (?, ?, ?, ?)"
    for family, an, ptn, subfamily in _node_rows(raw.decode() for raw in lines):
        rows.append((ptn, family, an, subfamily))
        count += 1
        if len(rows) >= batch:
            con.executemany(statement, rows)
            rows = []
    con.executemany(statement, rows)
    return count


def parse_locus_table(lines: Iterable[str]) -> Iterator[tuple[str, str]]:
    """Yield ``(AGI_LocusCode:<locus>, accession)`` from UniProt's accession/locus TSV.

    One protein can carry several loci (identical histone genes, for example), written
    ``At1g09200; At3g27360``. The header row and proteins without a locus are skipped.

    >>> list(parse_locus_table(["Entry\\tGene Names (ordered locus)", "Q38929\\tAt5g16440",
    ...                         "P59226\\tAt1g09200; At3g27360", "A0A1\\t"]))
    [('AGI_LocusCode:AT5G16440', 'Q38929'), ('AGI_LocusCode:AT1G09200', 'P59226'), ('AGI_LocusCode:AT3G27360', 'P59226')]
    """
    for line in lines:
        accession, _, loci = line.rstrip("\n").partition("\t")
        if accession == "Entry":
            continue
        for locus in re.split(r"[;\s]+", loci.strip()):
            if locus:
                yield f"AGI_LocusCode:{locus.upper()}", accession


def store_aliases(con: sqlite3.Connection, pairs: Iterable[tuple[str, str]]) -> int:
    """Insert ``(identifier, accession)`` aliases; returns how many were stored."""
    rows = list(pairs)
    con.executemany("INSERT INTO alias (key, accession) VALUES (?, ?)", rows)
    return len(rows)


def store_sequences(con: sqlite3.Connection, bundle: IO[bytes]) -> int:
    """Store each ``<PTHR>.fasta`` of a full-sequence archive; returns how many families."""
    count = 0
    with tarfile.open(fileobj=bundle, mode="r|gz") as tar:
        for member in tar:
            if not (member.isfile() and member.name.endswith(".fasta")):
                continue
            handle = tar.extractfile(member)
            assert handle is not None
            _store(con, Path(member.name).name[: -len(".fasta")], "sequences", handle.read().decode())
            count += 1
    return count


def build_database(
    bundle: IO[bytes], db_path: Path, *, release: str, source: str, full: bool = False
) -> dict[str, str]:
    """Stream a PANTHER data bundle into a new SQLite file and return its manifest.

    Only the node table, the ``.tree`` files and the ``.AN.fasta`` alignments are kept.
    They come first in PANTHER's archive, so reading stops at the first member outside
    them once both have been seen; ``full`` reads to the end instead. A bundle that names
    families in its node table without giving their trees is refused: a partial database
    would silently report those families as absent.
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    con.executescript("PRAGMA journal_mode = OFF; PRAGMA synchronous = OFF;" + _SCHEMA)
    nodes = trees = alignments = leaves = 0
    with tarfile.open(fileobj=bundle, mode="r|gz") as tar:
        for member in tar:
            if not member.isfile():
                continue
            name = member.name
            if name.endswith(NODE_TABLE_MEMBER):
                handle = tar.extractfile(member)
                assert handle is not None
                nodes = _store_node_table(con, handle)
            elif TREE_DIR in name and name.endswith(".tree"):
                handle = tar.extractfile(member)
                assert handle is not None
                text = handle.read().decode()
                family = Path(name).name[: -len(".tree")]
                _store(con, family, "tree", text)
                rows = []
                for line in text.strip().split("\n")[1:]:
                    an, _, long_id = line.strip().rstrip(";").partition(":")
                    accession = parse_long_id(long_id).accession
                    if accession:
                        rows.append((accession, family, an))
                con.executemany("INSERT INTO leaf (accession, family, an) VALUES (?, ?, ?)", rows)
                leaves += len(rows)
                trees += 1
            elif TREE_DIR in name and name.endswith(".AN.fasta"):
                handle = tar.extractfile(member)
                assert handle is not None
                _store(con, Path(name).name[: -len(".AN.fasta")], "msa", handle.read().decode())
                alignments += 1
            elif TREE_DIR not in name and trees and nodes and not full:
                break
    if not nodes:
        con.close()
        db_path.unlink()
        raise RuntimeError(f"bundle has no node table ({NODE_TABLE_MEMBER.lstrip('/')})")
    con.executescript(_INDEXES)
    missing = con.execute(
        "SELECT COUNT(*) FROM (SELECT DISTINCT family FROM node) AS n WHERE NOT EXISTS "
        "(SELECT 1 FROM family AS f WHERE f.family = n.family AND f.tree IS NOT NULL)"
    ).fetchone()[0]
    if missing:
        con.close()
        db_path.unlink()
        raise RuntimeError(
            f"{missing} families are in the node table without a tree; the archive is "
            "incomplete or laid out differently. Retry with --full."
        )
    manifest = {
        "release": release,
        "source": source,
        "families": str(trees),
        "alignments": str(alignments),
        "nodes": str(nodes),
        "leaves": str(leaves),
    }
    con.executemany("INSERT INTO meta (key, value) VALUES (?, ?)", manifest.items())
    con.commit()
    con.close()
    return manifest


def fetch_release(
    db_path: Path = DEFAULT_DB,
    url: str = BUNDLE_URL,
    *,
    full: bool = False,
    force: bool = False,
    aliases: bool = True,
    sequences: bool = True,
) -> Path:
    """Download the PANTHER data bundle into ``db_path`` unless it is already there.

    With ``sequences`` the full-length leaf sequences are stored too, which is what lets
    alignment columns be reported in each protein's own numbering. With ``aliases`` the
    Arabidopsis locus names are fetched from UniProt, so that ``AGI_LocusCode`` seeds can
    be found in the trees.
    """
    if db_path.exists() and not force:
        return db_path
    part = db_path.with_name(db_path.name + ".part")
    with requests.get(url, stream=True, timeout=300) as response:
        response.raise_for_status()
        bundle = cast(IO[bytes], response.raw)
        manifest = build_database(bundle, part, release=PANTHER_RELEASE, source=url, full=full)
        extra = {"source_last_modified": response.headers.get("Last-Modified", "")}
    con = sqlite3.connect(part)
    if sequences:
        with requests.get(SEQUENCES_URL, stream=True, timeout=300) as response:
            response.raise_for_status()
            count = store_sequences(con, cast(IO[bytes], response.raw))
            extra |= {
                "sequence_families": str(count),
                "sequence_source": SEQUENCES_URL,
                "sequence_source_last_modified": response.headers.get("Last-Modified", ""),
            }
    if aliases:
        with requests.get(ARATH_LOCUS_URL, stream=True, timeout=300) as response:
            response.raise_for_status()
            count = store_aliases(con, parse_locus_table(response.iter_lines(decode_unicode=True)))
        extra |= {
            "aliases": str(count),
            "alias_source": ARATH_LOCUS_URL,
            "alias_fetched": date.today().isoformat(),
        }
    con.executemany("INSERT INTO meta (key, value) VALUES (?, ?)", extra.items())
    con.commit()
    con.close()
    part.replace(db_path)
    print(f"{db_path}: {manifest['families']} trees, {manifest['nodes']} nodes", file=sys.stderr)
    return db_path


class PantherRelease:
    """Read access to a release database written by :func:`build_database`."""

    def __init__(self, db_path: Path = DEFAULT_DB, max_trees: int = 64) -> None:
        if not db_path.exists():
            raise FileNotFoundError(
                f"{db_path} not found; run `just fetch-panther-release` to download the "
                f"PANTHER {PANTHER_RELEASE} trees and alignments"
            )
        self.db_path = db_path
        self._con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self._trees: dict[str, FamilyTree | None] = {}
        self._max_trees = max_trees

    def manifest(self) -> dict[str, str]:
        """The release, source and counts recorded when the database was built."""
        return dict(self._con.execute("SELECT key, value FROM meta ORDER BY key"))

    def locate_node(self, ptn: str) -> tuple[str, str] | None:
        """``(family, AN id)`` of a persistent node id, with or without ``PANTHER:``."""
        row = self._con.execute(
            "SELECT family, an FROM node WHERE ptn = ? ORDER BY family, an",
            (ptn.removeprefix("PANTHER:"),),
        ).fetchone()
        return (row[0], row[1]) if row else None

    def locate_accession(self, accession: str) -> list[tuple[str, str]]:
        """Every ``(family, AN id)`` whose leaf carries this UniProt accession."""
        rows = self._con.execute(
            "SELECT family, an FROM leaf WHERE accession = ? ORDER BY family, an",
            (accession.removeprefix("UniProtKB:").split("-")[0],),
        ).fetchall()
        return [(family, an) for family, an in rows]

    def sequences(self, family: str) -> dict[str, str]:
        """Full-length sequences of a family's leaves as ``{long id: sequence}``."""
        row = self._con.execute("SELECT sequences FROM family WHERE family = ?", (family,)).fetchone()
        return parse_fasta(_unpack(row[0])) if row and row[0] else {}

    def alias_accessions(self, token: str) -> list[str]:
        """UniProt accessions recorded for an identifier the trees do not carry."""
        rows = self._con.execute(
            "SELECT accession FROM alias WHERE key = ? ORDER BY accession", (token,)
        ).fetchall()
        return [row[0] for row in rows]

    def tree(self, family: str) -> FamilyTree | None:
        """The family's tree, or None when the release has no such family."""
        if family not in self._trees:
            row = self._con.execute("SELECT tree FROM family WHERE family = ?", (family,)).fetchone()
            if len(self._trees) >= self._max_trees:
                self._trees.pop(next(iter(self._trees)))
            if row is None or row[0] is None:
                self._trees[family] = None
            else:
                table = {
                    an: (ptn, subfamily)
                    for an, ptn, subfamily in self._con.execute(
                        "SELECT an, ptn, subfamily FROM node WHERE family = ?", (family,)
                    )
                }
                self._trees[family] = FamilyTree.build(family, parse_tree(_unpack(row[0])), table)
        return self._trees[family]

    def alignment(self, family: str) -> dict[str, str]:
        """The family alignment as ``{AN id: aligned row}`` (empty when there is none)."""
        row = self._con.execute("SELECT msa FROM family WHERE family = ?", (family,)).fetchone()
        return parse_fasta(_unpack(row[0])) if row and row[0] else {}


def main(argv: Sequence[str] | None = None) -> int:
    """Fetch the release bundle, or print what the local database holds."""
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    parser.add_argument("command", choices=["fetch", "info"])
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--url", default=BUNDLE_URL)
    parser.add_argument("--full", action="store_true", help="read the whole archive")
    parser.add_argument("--force", action="store_true", help="rebuild an existing database")
    parser.add_argument("--no-aliases", action="store_true", help="skip the Arabidopsis locus names")
    parser.add_argument("--no-sequences", action="store_true", help="skip the full-length sequences")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.command == "fetch":
        fetch_release(
            args.db,
            args.url,
            full=args.full,
            force=args.force,
            aliases=not args.no_aliases,
            sequences=not args.no_sequences,
        )
    for key, value in PantherRelease(args.db).manifest().items():
        print(f"{key}\t{value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
