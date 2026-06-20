"""Ingest PANTHER PAINT (PTN node-level) GO annotations.

PANTHER/GO PAINT annotations are made *at internal phylogenetic tree nodes*
(``PTN...`` ids) rather than at leaf genes. These node annotations are the
*source* of every downstream IBA (``GO_REF:0000033``) annotation seen on leaf
proteins: an IBA on a gene is just the projection onto that leaf of an
annotation curated on one of its ancestral nodes.

The authoritative file is ``IBD.gaf`` from the PANTHER FTP. Each row's subject
is a ``PTN`` node. Most rows carry one of three PAINT evidence codes:

* ``IBD`` - Inferred from Biological aspect of Descendant: a function annotated
  *at* the node (seeded by experimental annotations on descendants). Source of
  positive IBAs.
* ``IRD`` - Inferred from Reviewed Descendant: a function *lost / diverged* at
  the node (a ``NOT`` annotation). Source of negated IBAs.
* ``IKR`` - Inferred from Key Residues: loss inferred from key-residue change.

A *loss* is therefore any ``NOT`` annotation: usually ``IRD``/``IKR``, but
occasionally a rare ``NOT|IBD``. A small number of rows also carry plain ``IBA``
on a ``PTN`` node. All are legitimate in the current PANTHER data and are
parsed/retained as-is (we do not filter by evidence code, only require a ``PTN``
subject).

``IBD.gaf`` is keyed by node and carries no ``PTHR`` family id, so to slice it
per family we resolve which ``PTN`` nodes belong to a family by joining:

1. the family's member UniProt ids (from the cached ``<FAM>-entries.csv``), and
2. the leaf IBA GAF (``gene_association.paint_uniprot.gaf.gz``), which maps each
   leaf UniProt to the ancestral ``PTN`` nodes it was annotated from.

The union of ancestral nodes cited by a family's members is that family's node
set. We then slice ``IBD.gaf`` to those nodes and write a per-family
``<FAM>-paint.tsv`` (parsed, one row per node annotation).

Both source files are cached (gitignored ``.cache/`` by default); only the
small per-family slices are intended to be committed.
"""

from __future__ import annotations

import csv
import gzip
from dataclasses import dataclass, field
from pathlib import Path
from typing import IO, Dict, Iterable, List, Optional, Set, Tuple

import requests

PAINT_BASE = "https://data.pantherdb.org/ftp/downloads/paint/current"
IBD_GAF_URL = f"{PAINT_BASE}/IBD.gaf"
LEAF_GAF_URL = f"{PAINT_BASE}/gene_association.paint_uniprot.gaf.gz"

# GAF column indices (0-based), per the GAF 2.x spec.
_COL_OBJECT_ID = 1
_COL_QUALIFIER = 3
_COL_GO_ID = 4
_COL_EVIDENCE = 6
_COL_WITH_FROM = 7
_COL_ASPECT = 8
_COL_TAXON = 12
_COL_DATE = 13

_TSV_HEADER = [
    "family",
    "node",
    "go_id",
    "aspect",
    "evidence",
    "negated",
    "seeds",
    "taxon",
    "date",
]


@dataclass
class IBDRecord:
    """A single PANTHER node-level (PAINT) annotation.

    Attributes:
        node: The ``PTN`` tree-node id the annotation is made on.
        go_id: The GO term id.
        aspect: GAF aspect (``F`` molecular function, ``P`` process, ``C`` component).
        evidence: PAINT evidence code (usually ``IBD``, ``IRD``, or ``IKR``;
            occasionally ``IBA`` on a node, which is retained as-is).
        negated: True for loss annotations (``NOT`` qualifier; IRD/IKR).
        seeds: Full CURIEs in the with/from field (experimental seeds for IBD;
            the ancestral node for IRD/IKR), preserved verbatim (e.g.
            ``UniProtKB:P20248``, ``MGI:MGI:88314``).
        taxon: Taxon constraint from the GAF (may be empty).
        date: Annotation date (YYYYMMDD).
        raw_line: The original GAF line, preserved for faithful re-emission.
    """

    node: str
    go_id: str
    aspect: str
    evidence: str
    negated: bool
    seeds: List[str] = field(default_factory=list)
    taxon: str = ""
    date: str = ""
    raw_line: str = ""


def parse_ptn_nodes(with_from: str) -> List[str]:
    """Extract ``PTN`` node ids from a GAF with/from field, order-preserving.

    Handles both ``PANTHER:PTN...`` prefixed tokens and bare ``PTN...`` tokens;
    ignores non-PTN tokens (e.g. ``UniProtKB:P12345`` seeds).

    >>> parse_ptn_nodes("PANTHER:PTN000019791|UniProtKB:P20248|PTN000000001")
    ['PTN000019791', 'PTN000000001']
    >>> parse_ptn_nodes("UniProtKB:P20248")
    []
    """
    nodes: List[str] = []
    for tok in with_from.split("|"):
        tok = tok.strip()
        if not tok:
            continue
        ident = tok.split(":", 1)[1] if ":" in tok else tok
        if ident.startswith("PTN"):
            nodes.append(ident)
    return nodes


def parse_ibd_gaf(lines: Iterable[str]) -> Dict[str, List[IBDRecord]]:
    """Parse IBD.gaf content into a ``node -> [IBDRecord, ...]`` index.

    Header/comment lines (starting with ``!``) and short/blank lines are skipped.

    >>> data = [
    ...     "!gaf-version: 2.1",
    ...     "PANTHER\\tPTN1\\tPTN1\\t\\tGO:0016538\\tGO_REF:0000033\\tIBD\\t"
    ...     "UniProtKB:P1|UniProtKB:P2\\tF\\t\\t\\tprotein\\ttaxon:\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> idx = parse_ibd_gaf(data)
    >>> idx["PTN1"][0].go_id, idx["PTN1"][0].evidence, idx["PTN1"][0].seeds
    ('GO:0016538', 'IBD', ['UniProtKB:P1', 'UniProtKB:P2'])
    """
    index: Dict[str, List[IBDRecord]] = {}
    for line in lines:
        if not line or line.startswith("!"):
            continue
        cols = line.rstrip("\n").split("\t")
        if len(cols) <= _COL_ASPECT:
            continue
        node = cols[_COL_OBJECT_ID]
        if not node.startswith("PTN"):
            continue
        qualifier = cols[_COL_QUALIFIER]
        rec = IBDRecord(
            node=node,
            go_id=cols[_COL_GO_ID],
            aspect=cols[_COL_ASPECT],
            evidence=cols[_COL_EVIDENCE],
            negated="NOT" in qualifier,
            seeds=[t for t in cols[_COL_WITH_FROM].split("|") if t],
            taxon=cols[_COL_TAXON] if len(cols) > _COL_TAXON else "",
            date=cols[_COL_DATE] if len(cols) > _COL_DATE else "",
            raw_line=line.rstrip("\n"),
        )
        index.setdefault(node, []).append(rec)
    return index


def family_member_ids(entries_csv: Path) -> Set[str]:
    """Return the set of member UniProt ids from a cached ``<FAM>-entries.csv``.

    Rows with an empty ``id`` are ignored.
    """
    members: Set[str] = set()
    with entries_csv.open() as fh:
        for row in csv.DictReader(fh):
            ident = (row.get("id") or "").strip()
            if ident:
                members.add(ident)
    return members


def family_member_subfamilies(entries_csv: Path) -> Dict[str, str]:
    """Return ``member UniProt id -> subfamily accession`` from a member table.

    Members with an empty ``subfamily`` map to ``""``. Rows with an empty ``id``
    are ignored.
    """
    out: Dict[str, str] = {}
    with entries_csv.open() as fh:
        for row in csv.DictReader(fh):
            ident = (row.get("id") or "").strip()
            if ident:
                out[ident] = (row.get("subfamily") or "").strip()
    return out


def iter_losses(
    ibd_index: Dict[str, List[IBDRecord]],
) -> Iterable[Tuple[IBDRecord, List[str]]]:
    """Yield ``(loss_record, ancestral_nodes)`` for every loss record.

    A loss is any negated (``NOT``) annotation — usually ``IRD``/``IKR``, but
    occasionally a rare ``NOT|IBD``. It is annotated *on* the node where the
    function diverged, with the ancestral (gain) node carried in the with/from
    field. The ancestral nodes are parsed out so callers can pair the loss with
    where the function was present.

    >>> data = [
    ...     "PANTHER\\tPTNa\\tPTNa\\tNOT\\tGO:1\\tGO_REF:0000033\\tIRD\\t"
    ...     "PANTHER:PTNb\\tF\\t\\t\\tprotein\\ttaxon:1\\t20250101\\tGO_Central\\t\\t",
    ...     "PANTHER\\tPTNc\\tPTNc\\t\\tGO:2\\tGO_REF:0000033\\tIBD\\t"
    ...     "UniProtKB:P1\\tF\\t\\t\\tprotein\\ttaxon:\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> idx = parse_ibd_gaf(data)
    >>> [(r.node, r.go_id, anc) for r, anc in iter_losses(idx)]
    [('PTNa', 'GO:1', ['PTNb'])]
    """
    for recs in ibd_index.values():
        for rec in recs:
            if rec.negated or rec.evidence in ("IRD", "IKR"):
                yield rec, parse_ptn_nodes("|".join(rec.seeds))


def iter_leaf_rows(
    lines: Iterable[str],
) -> Iterable[Tuple[str, str, List[str]]]:
    """Yield ``(object_id, go_id, ancestral_PTN_nodes)`` per leaf IBA GAF row.

    A public streaming primitive over the (large) leaf GAF so callers do not need
    the column-index internals. Header/comment and short lines are skipped.

    >>> leaf = [
    ...     "UniProtKB\\tP14635\\tCCNB1\\tinvolved_in\\tGO:0016538\\tGO_REF:0000033\\tIBA\\t"
    ...     "PANTHER:PTN1|UniProtKB:P2\\tF\\t\\t\\tprotein\\ttaxon:9606\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> list(iter_leaf_rows(leaf))
    [('P14635', 'GO:0016538', ['PTN1'])]
    """
    for line in lines:
        if not line or line.startswith("!"):
            continue
        cols = line.split("\t")
        if len(cols) <= _COL_WITH_FROM:
            continue
        yield (
            cols[_COL_OBJECT_ID],
            cols[_COL_GO_ID],
            parse_ptn_nodes(cols[_COL_WITH_FROM]),
        )


def leaf_nodes_for_members(lines: Iterable[str], members: Set[str]) -> Set[str]:
    """Stream the leaf IBA GAF and collect ancestral ``PTN`` nodes for members.

    For every leaf row whose object id is in ``members``, the ancestral ``PTN``
    node(s) in the with/from field are collected. Streaming keeps memory flat
    over the ~4.6M-line leaf GAF.

    >>> leaf = [
    ...     "UniProtKB\\tP14635\\tCCNB1\\tinvolved_in\\tGO:0016538\\tGO_REF:0000033\\tIBA\\t"
    ...     "PANTHER:PTN1|UniProtKB:P2\\tF\\t\\t\\tprotein\\ttaxon:9606\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> sorted(leaf_nodes_for_members(leaf, {"P14635"}))
    ['PTN1']
    """
    nodes: Set[str] = set()
    for obj_id, _go, anc_nodes in iter_leaf_rows(lines):
        if obj_id in members:
            nodes.update(anc_nodes)
    return nodes


def write_family_paint(
    family: str,
    nodes: Set[str],
    ibd_index: Dict[str, List[IBDRecord]],
    out_dir: Path,
) -> Path:
    """Write the per-family PAINT slice as ``<FAM>-paint.tsv``.

    One row per node-level annotation (IBD/IRD/IKR, plus any IBA-on-node) for the
    family's ``PTN`` nodes, ordered by node, aspect, GO id. Returns the TSV path.
    """
    tsv_path = out_dir / f"{family}-paint.tsv"

    # Stable ordering: by node, then aspect, then GO id.
    selected = [rec for node in nodes for rec in ibd_index.get(node, [])]
    selected.sort(key=lambda r: (r.node, r.aspect, r.go_id))

    with tsv_path.open("w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(_TSV_HEADER)
        for rec in selected:
            writer.writerow(
                [
                    family,
                    rec.node,
                    rec.go_id,
                    rec.aspect,
                    rec.evidence,
                    "true" if rec.negated else "false",
                    "|".join(rec.seeds),
                    rec.taxon,
                    rec.date,
                ]
            )

    return tsv_path


def download_cached(url: str, cache_dir: Path, *, force: bool = False) -> Path:
    """Download ``url`` into ``cache_dir`` (by basename), reusing an existing copy.

    Streams to disk so large GAFs do not need to be held in memory.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / url.rsplit("/", 1)[1]
    if dest.exists() and not force:
        return dest
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=120) as resp:
        resp.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    tmp.replace(dest)
    return dest


def open_text(path: Path) -> IO[str]:
    """Open a possibly-gzipped text file for line iteration."""
    if path.suffix == ".gz":
        return gzip.open(path, "rt")
    return path.open()


def fetch_family_paint(
    family: str,
    *,
    entries_csv: Path,
    out_dir: Path,
    cache_dir: Path,
    extra_uniprot: Optional[Iterable[str]] = None,
    force_download: bool = False,
) -> Tuple[Path, Set[str]]:
    """Fetch + cache the PAINT GAFs and write a family's node-level slice.

    Args:
        family: PANTHER family id (e.g. ``PTHR10177``).
        entries_csv: Path to the cached ``<FAM>-entries.csv`` (member list).
        out_dir: Directory to write the per-family slice into.
        cache_dir: Directory to cache the downloaded source GAFs in.
        extra_uniprot: Optional extra member UniProt ids (e.g. reviewed genes
            not present as reviewed members in entries.csv).
        force_download: Re-download source GAFs even if cached.

    Returns:
        ``(tsv_path, nodes)`` where ``nodes`` is the resolved set of ``PTN``
        nodes for the family.
    """
    members = family_member_ids(entries_csv)
    if extra_uniprot:
        members.update(extra_uniprot)

    leaf_path = download_cached(LEAF_GAF_URL, cache_dir, force=force_download)
    ibd_path = download_cached(IBD_GAF_URL, cache_dir, force=force_download)

    with open_text(leaf_path) as fh:
        nodes = leaf_nodes_for_members(fh, members)

    with open_text(ibd_path) as fh:
        ibd_index = parse_ibd_gaf(fh)

    out_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = write_family_paint(family, nodes, ibd_index, out_dir)
    return tsv_path, nodes


def load_all_family_members(
    panther_root: Path,
) -> Tuple[Dict[str, Set[str]], Dict[str, Path]]:
    """Scan ``panther_root`` for cached families with a ``<FAM>-entries.csv``.

    Returns ``(member_uniprot -> {families}, family -> family_dir)`` for every
    family directory that has a member table. The inverted member map lets the
    bulk path resolve nodes for all families in a single leaf-GAF pass.
    """
    member_to_families: Dict[str, Set[str]] = {}
    family_dirs: Dict[str, Path] = {}
    for entries in sorted(panther_root.glob("*/*-entries.csv")):
        family = entries.parent.name
        family_dirs[family] = entries.parent
        for uid in family_member_ids(entries):
            member_to_families.setdefault(uid, set()).add(family)
    return member_to_families, family_dirs


def family_nodes_from_leaf(
    lines: Iterable[str], member_to_families: Dict[str, Set[str]]
) -> Dict[str, Set[str]]:
    """One streaming leaf-GAF pass -> ``family -> {PTN nodes}`` for all families.

    >>> leaf = [
    ...     "UniProtKB\\tP14635\\tCCNB1\\tinvolved_in\\tGO:1\\tGO_REF:0000033\\tIBA\\t"
    ...     "PANTHER:PTN1|UniProtKB:P2\\tF\\t\\t\\tprotein\\ttaxon:9606\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> family_nodes_from_leaf(leaf, {"P14635": {"PTHRX"}})
    {'PTHRX': {'PTN1'}}
    """
    family_nodes: Dict[str, Set[str]] = {}
    for obj_id, _go, nodes in iter_leaf_rows(lines):
        families = member_to_families.get(obj_id)
        if not families or not nodes:
            continue
        for family in families:
            family_nodes.setdefault(family, set()).update(nodes)
    return family_nodes


def fetch_all_family_paint(
    panther_root: Path,
    *,
    cache_dir: Path,
    force_download: bool = False,
    skip_empty: bool = True,
) -> Dict[str, int]:
    """Write per-family PAINT slices for every cached family in one pass.

    Does a single streaming pass over the (large) leaf GAF and a single load of
    ``IBD.gaf``, rather than re-reading them per family. Families whose members
    resolve to no node-level annotations are skipped when ``skip_empty`` is True.

    Returns ``family -> number of node-level annotations written`` for each
    family that had at least one (or all families when ``skip_empty`` is False).
    """
    member_to_families, family_dirs = load_all_family_members(panther_root)

    leaf_path = download_cached(LEAF_GAF_URL, cache_dir, force=force_download)
    ibd_path = download_cached(IBD_GAF_URL, cache_dir, force=force_download)

    with open_text(leaf_path) as fh:
        family_nodes = family_nodes_from_leaf(fh, member_to_families)
    with open_text(ibd_path) as fh:
        ibd_index = parse_ibd_gaf(fh)

    counts: Dict[str, int] = {}
    for family, fdir in family_dirs.items():
        nodes = family_nodes.get(family, set())
        n_annotations = sum(len(ibd_index.get(n, [])) for n in nodes)
        if skip_empty and n_annotations == 0:
            continue
        write_family_paint(family, nodes, ibd_index, fdir)
        counts[family] = n_annotations
    return counts


@dataclass
class LossAnalysisInput:
    """Ready-to-run inputs for reconstructing an IKR/IRD function loss.

    A PAINT loss records only the *outcome* (function lost at a node); the
    residue-level rationale a curator saw in the alignment is not published. This
    bundle gathers what a downstream bioinformatics agent needs to reconstruct
    it: the proteins where the function (and its key residues) are characterized
    (``seed_proteins``), the clade that **lost** the function (``loss_clade``),
    and a sister clade that **retained** it (``retaining_clade``). The agent then
    fetches these sequences, aligns them, and compares the key columns.

    Attributes:
        family / go_id / aspect / evidence: identify the loss event.
        ancestral_node: PTN node where the function was gained (IBD).
        loss_node: PTN node where the function was lost (IRD/IKR subject).
        seed_proteins: with/from of the ancestral IBD record - the experimentally
            characterized proteins establishing the function (mixed CURIEs).
        seed_uniprot: the UniProtKB subset of ``seed_proteins`` (bare accessions),
            for direct sequence/feature retrieval.
        loss_clade: ``(accession, subfamily)`` members descending from the loss
            node (the proteins predicted to have lost the function).
        retaining_clade: ``(accession, subfamily)`` family members still annotated
            with the function (the comparison/positive set).
    """

    family: str
    go_id: str
    aspect: str
    evidence: str
    ancestral_node: str
    loss_node: str
    seed_proteins: List[str] = field(default_factory=list)
    seed_uniprot: List[str] = field(default_factory=list)
    loss_clade: List[Tuple[str, str]] = field(default_factory=list)
    retaining_clade: List[Tuple[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Return a plain dict suitable for YAML/JSON serialization."""
        return {
            "family": self.family,
            "go_id": self.go_id,
            "aspect": self.aspect,
            "evidence": self.evidence,
            "ancestral_node": self.ancestral_node,
            "loss_node": self.loss_node,
            "seed_proteins": self.seed_proteins,
            "seed_uniprot": self.seed_uniprot,
            "loss_clade": [
                {"accession": a, "subfamily": s} for a, s in self.loss_clade
            ],
            "retaining_clade": [
                {"accession": a, "subfamily": s} for a, s in self.retaining_clade
            ],
        }


def assemble_loss_input(
    *,
    family: str,
    go_id: str,
    aspect: str,
    evidence: str,
    ancestral_node: str,
    loss_node: str,
    seed_proteins: Iterable[str],
    loss_members: Set[str],
    retaining_members: Set[str],
    member_subfamily: Dict[str, str],
) -> LossAnalysisInput:
    """Assemble a :class:`LossAnalysisInput` from resolved member sets.

    Pure/deterministic: callers supply the seed proteins (from the ancestral IBD
    record) and the loss/retaining member accessions (resolved from the leaf
    GAF). Members appearing in both sets are treated as loss-clade only.

    >>> inp = assemble_loss_input(
    ...     family="PTHR1", go_id="GO:1", aspect="F", evidence="IKR",
    ...     ancestral_node="PTNa", loss_node="PTNb",
    ...     seed_proteins=["UniProtKB:P1", "MGI:MGI:9"],
    ...     loss_members={"Q9"}, retaining_members={"P1", "Q9"},
    ...     member_subfamily={"Q9": "PTHR1:SF2", "P1": "PTHR1:SF1"},
    ... )
    >>> inp.seed_uniprot
    ['P1']
    >>> inp.loss_clade
    [('Q9', 'PTHR1:SF2')]
    >>> inp.retaining_clade
    [('P1', 'PTHR1:SF1')]
    """
    seeds = list(seed_proteins)
    seed_uniprot = [s.split(":", 1)[1] for s in seeds if s.startswith("UniProtKB:")]
    retaining = retaining_members - loss_members

    def _decorate(accs: Set[str]) -> List[Tuple[str, str]]:
        return sorted((a, member_subfamily.get(a, "")) for a in accs)

    return LossAnalysisInput(
        family=family,
        go_id=go_id,
        aspect=aspect,
        evidence=evidence,
        ancestral_node=ancestral_node,
        loss_node=loss_node,
        seed_proteins=seeds,
        seed_uniprot=seed_uniprot,
        loss_clade=_decorate(loss_members),
        retaining_clade=_decorate(retaining),
    )
