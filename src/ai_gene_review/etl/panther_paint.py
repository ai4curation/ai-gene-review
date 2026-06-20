"""Ingest PANTHER PAINT (PTN node-level) GO annotations.

PANTHER/GO PAINT annotations are made *at internal phylogenetic tree nodes*
(``PTN...`` ids) rather than at leaf genes. These node annotations are the
*source* of every downstream IBA (``GO_REF:0000033``) annotation seen on leaf
proteins: an IBA on a gene is just the projection onto that leaf of an
annotation curated on one of its ancestral nodes.

The authoritative file is ``IBD.gaf`` from the PANTHER FTP. Each row's subject
is a ``PTN`` node, with one of three evidence codes:

* ``IBD`` - Inferred from Biological aspect of Descendant: a function annotated
  *at* the node (seeded by experimental annotations on descendants). Source of
  positive IBAs.
* ``IRD`` - Inferred from Reviewed Descendant: a function *lost / diverged* at
  the node (a ``NOT`` annotation). Source of negated IBAs.
* ``IKR`` - Inferred from Key Residues: loss inferred from key-residue change.

``IBD.gaf`` is keyed by node and carries no ``PTHR`` family id, so to slice it
per family we resolve which ``PTN`` nodes belong to a family by joining:

1. the family's member UniProt ids (from the cached ``<FAM>-entries.csv``), and
2. the leaf IBA GAF (``gene_association.paint_uniprot.gaf.gz``), which maps each
   leaf UniProt to the ancestral ``PTN`` nodes it was annotated from.

The union of ancestral nodes cited by a family's members is that family's node
set. We then slice ``IBD.gaf`` to those nodes and write a per-family
``<FAM>-paint.gaf`` (raw GAF) plus a parsed ``<FAM>-paint.tsv`` sidecar.

Both source files are cached (gitignored ``.cache/`` by default); only the
small per-family slices are intended to be committed.
"""

from __future__ import annotations

import csv
import gzip
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import requests

PAINT_BASE = "http://data.pantherdb.org/ftp/downloads/paint/current"
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
        evidence: PAINT evidence code (``IBD``, ``IRD``, or ``IKR``).
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


def leaf_nodes_for_members(lines: Iterable[str], members: Set[str]) -> Set[str]:
    """Stream the leaf IBA GAF and collect ancestral ``PTN`` nodes for members.

    For every leaf row whose object id (column 2) is in ``members``, the
    ancestral ``PTN`` node(s) in the with/from field are collected. Streaming
    keeps memory flat over the ~4.6M-line leaf GAF.

    >>> leaf = [
    ...     "UniProtKB\\tP14635\\tCCNB1\\tinvolved_in\\tGO:0016538\\tGO_REF:0000033\\tIBA\\t"
    ...     "PANTHER:PTN1|UniProtKB:P2\\tF\\t\\t\\tprotein\\ttaxon:9606\\t20250101\\tGO_Central\\t\\t",
    ... ]
    >>> sorted(leaf_nodes_for_members(leaf, {"P14635"}))
    ['PTN1']
    """
    nodes: Set[str] = set()
    for line in lines:
        if not line or line.startswith("!"):
            continue
        cols = line.split("\t")
        if len(cols) <= _COL_WITH_FROM:
            continue
        if cols[_COL_OBJECT_ID] in members:
            nodes.update(parse_ptn_nodes(cols[_COL_WITH_FROM]))
    return nodes


def write_family_paint(
    family: str,
    nodes: Set[str],
    ibd_index: Dict[str, List[IBDRecord]],
    out_dir: Path,
) -> Tuple[Path, Path]:
    """Write the per-family PAINT slice as ``<FAM>-paint.gaf`` and ``-paint.tsv``.

    The ``.gaf`` is the raw subset of IBD.gaf rows for the family's nodes
    (with a provenance header); the ``.tsv`` is a parsed, easier-to-consume
    sidecar. Returns ``(gaf_path, tsv_path)``.
    """
    gaf_path = out_dir / f"{family}-paint.gaf"
    tsv_path = out_dir / f"{family}-paint.tsv"

    # Stable ordering: by node, then aspect, then GO id.
    selected = [rec for node in nodes for rec in ibd_index.get(node, [])]
    selected.sort(key=lambda r: (r.node, r.aspect, r.go_id))

    with gaf_path.open("w") as fh:
        fh.write("!gaf-version: 2.1\n")
        fh.write(f"!PANTHER PAINT node annotations for family {family}\n")
        fh.write(f"!nodes: {len(nodes)}; annotations: {len(selected)}\n")
        fh.write(f"!source: {IBD_GAF_URL}\n")
        for rec in selected:
            fh.write(rec.raw_line + "\n")

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

    return gaf_path, tsv_path


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


def _open_text(path: Path):
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
) -> Tuple[Path, Path, Set[str]]:
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
        ``(gaf_path, tsv_path, nodes)`` where ``nodes`` is the resolved set of
        ``PTN`` nodes for the family.
    """
    members = family_member_ids(entries_csv)
    if extra_uniprot:
        members.update(extra_uniprot)

    leaf_path = download_cached(LEAF_GAF_URL, cache_dir, force=force_download)
    ibd_path = download_cached(IBD_GAF_URL, cache_dir, force=force_download)

    with _open_text(leaf_path) as fh:
        nodes = leaf_nodes_for_members(fh, members)

    with _open_text(ibd_path) as fh:
        ibd_index = parse_ibd_gaf(fh)

    out_dir.mkdir(parents=True, exist_ok=True)
    gaf_path, tsv_path = write_family_paint(family, nodes, ibd_index, out_dir)
    return gaf_path, tsv_path, nodes
