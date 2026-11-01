"""Emit a MOD's curated gene description as a deep-research source file.

Model organism databases (WormBase, FlyBase, SGD, MGI, RGD, ZFIN, Xenbase) write
a short hand-curated description for many genes; the Alliance of Genome
Resources serves it as the ``MOD_provided_gene_description`` note. This module
writes that text to ``genes/<org>/<GENE>/<GENE>-deep-research-<mod>.md`` so the
review workflow picks it up like any other deep-research provider (falcon,
perplexity, affinage), and reviews cite it as a ``file:`` reference.

Design follows ``projects/AFFINAGE_EVALUATION/affinage_deep_research.py``: the
file is a faithful, unedited rendering of what the provider returned. It
carries no AIGR judgment; trust (staleness, correctness, which claims were
traced to papers) belongs in the gene review's ``references[].reference_review``.

Only the curated note is written. The Alliance automated description is
generated from GO annotations, so treating it as a source would cite the
annotations under review as evidence for themselves.

The Alliance note has no citations and no authoring date, so the file says so;
every claim must be traced to a publication before it supports an annotation.

Examples:
    >>> render_mod_deep_research(
    ...     "worm", "rab-11.1", "WormBase", "WB:WBGene00004274",
    ...     "rab-11.1 encodes a small GTPase.", "2026-10-30",
    ...     url="https://www.wormbase.org/db/get?name=WBGene00004274;class=Gene",
    ...     uniprot_accession="Q94986",
    ... ).splitlines()[1]
    'provider: wormbase'
"""

import logging
import re
import time
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from ai_gene_review.etl.descriptions import (
    ALLIANCE_API_BASE,
    ORGANISM_CONFIG,
    extract_uniprot_id,
    extract_uniprot_xref,
    fetch_alliance_description,
    looks_automated,
)
from ai_gene_review.mod_providers import MOD_PROVIDER, is_mod_description_file  # noqa: F401  (re-export)

logger = logging.getLogger(__name__)



def uniprot_gene_names(uniprot_data: str) -> set[str]:
    """All names on the UniProt GN lines (Name, Synonyms, OrderedLocusNames, ORFNames).

    >>> sorted(uniprot_gene_names('''GN   Name=rab-11.1 {ECO:0000312|WormBase:F53G12.1};
    ... GN   ORFNames=F53G12.1 {ECO:0000312|WormBase:F53G12.1};'''))
    ['F53G12.1', 'rab-11.1']
    """
    gn = " ".join(line[5:] for line in uniprot_data.splitlines() if line.startswith("GN   "))
    gn = re.sub(r"\{[^}]*\}", "", gn)
    names: set[str] = set()
    for m in re.finditer(r"(?:Name|Synonyms|OrderedLocusNames|ORFNames)=([^;]+);", gn):
        names.update(n.strip() for n in m.group(1).split(",") if n.strip())
    return names


def identity_gate(
    gene: str, uniprot_data: str, alliance_symbol: Optional[str], alliance_systematic: Optional[str]
) -> Optional[str]:
    """Return a blocking message if the Alliance record does not name this gene.

    The Alliance id comes from the UniProt cross-reference, so a mismatch means the
    folder, the UniProt entry and the MOD record disagree about which gene this is.

    >>> identity_gate("rab-11.1", "GN   Name=rab-11.1;", "rab-11.1", "F53G12.1") is None
    True
    >>> identity_gate("rab-11.1", "GN   Name=rab-11.1;", "rab-10", "T23H2.5")
    'Alliance record names rab-10/T23H2.5, but neither matches the folder (rab-11.1) or the UniProt gene names (rab-11.1).'
    >>> identity_gate("J7SF87", "", "lin-4", None)
    'Alliance record names lin-4, but neither matches the folder (J7SF87) or the UniProt gene names (none).'
    """
    uniprot = uniprot_gene_names(uniprot_data)
    found = {n for n in (alliance_symbol, alliance_systematic) if n}
    if not found or found & (uniprot | {gene}):
        return None
    uniprot_names = ", ".join(sorted(uniprot)) or "none"
    return (
        f"Alliance record names {'/'.join(n for n in (alliance_symbol, alliance_systematic) if n)}, "
        f"but neither matches the folder ({gene}) or the UniProt gene names ({uniprot_names})."
    )


def render_mod_deep_research(
    organism: str,
    gene: str,
    mod_name: str,
    mod_id: str,
    text: str,
    fetch_date: str,
    url: Optional[str] = None,
    uniprot_accession: Optional[str] = None,
) -> str:
    """Render the curated MOD description as a deep-research Markdown file."""
    slug = mod_name.lower()
    lines = [
        "---",
        f"provider: {slug}",
        f"authorship: {mod_name} curators (hand-written gene description)",
        f"source_url: {ALLIANCE_API_BASE}/gene/{mod_id}",
        "source_field: relatedNotes[noteType=MOD_provided_gene_description]",
        f"mod_gene_id: {mod_id}",
        f"mod_gene_page: {url or ''}",
        f"uniprot_accession: {uniprot_accession or ''}",
        f"fetch_date: '{fetch_date}'",
        "citations_provided: false",
        "authoring_date_provided: false",
        "note: >-",
        f"  Verbatim machine-fetched {mod_name} curated gene description, as served by",
        "  the Alliance of Genome Resources, reproduced as-is as an external",
        "  deep-research source. It is written by database curators, not generated",
        "  for this review; the source supplies no citations and no authoring date.",
        "  Curatorial assessment of this text (relevance, correctness, staleness,",
        "  which claims were traced to publications) is the reviewer's and belongs in",
        "  the gene review's references[].reference_review, not in this file.",
        "---",
        "",
        f"# {mod_name} gene description for {gene} ({organism})",
        "",
        text.strip(),
        "",
    ]
    return "\n".join(lines)


def emit_mod_deep_research(
    organism: str,
    gene: str,
    base_path: Optional[Path] = None,
    write: bool = False,
    force: bool = False,
) -> Tuple[str, Optional[Path], str]:
    """Fetch and render (optionally write) one gene's curated MOD description.

    Returns ``(status, path, message)`` where status is one of ``written``,
    ``rendered``, ``no_curated``, ``skipped`` or ``blocked``.
    """
    base = base_path or Path.cwd()
    config = ORGANISM_CONFIG.get(organism)
    if not config or config["mod"] not in MOD_PROVIDER:
        return "skipped", None, f"no MOD provider configured for organism '{organism}'"
    if organism == "human":
        return "skipped", None, "human is out of scope (HGNC is not a MOD description source)"
    slug, mod_name = MOD_PROVIDER[config["mod"]]

    gene_dir = base / "genes" / organism / gene
    up_file = gene_dir / f"{gene}-uniprot.txt"
    if not up_file.exists():
        return "skipped", None, f"missing {up_file}"
    uniprot_data = up_file.read_text(encoding="utf-8")
    xref = extract_uniprot_xref(uniprot_data, config["uniprot_xref"])
    if not xref:
        return "skipped", None, f"no {config['uniprot_xref']} cross-reference in UniProt entry"
    mod_id = xref if xref.startswith(f"{config['mod']}:") else f"{config['mod']}:{xref}"

    data = fetch_alliance_description(mod_id)
    text = data.get("curated_synopsis")
    if not text:
        return "no_curated", None, f"{mod_id} has no curated description"
    if looks_automated(text, data.get("automated_synopsis")):
        return "no_curated", None, f"{mod_id}: the MOD-provided description is automated (GO-derived) text"

    problem = identity_gate(gene, uniprot_data, data.get("symbol"), data.get("systematic_name"))
    doc = render_mod_deep_research(
        organism, gene, mod_name, mod_id, text, date.today().isoformat(),
        url=data.get("url"), uniprot_accession=extract_uniprot_id(uniprot_data),
    )
    if not write:
        return "rendered", None, doc
    if problem and not force:
        return "blocked", None, problem
    dest = gene_dir / f"{gene}-deep-research-{slug}.md"
    dest.write_text(doc, encoding="utf-8")
    return "written", dest, problem or "ok"


def emit_organism(
    organism: str,
    genes: Optional[List[str]] = None,
    base_path: Optional[Path] = None,
    force: bool = False,
    delay: float = 0.3,
) -> Dict[str, List[str]]:
    """Write MOD deep-research files for the given genes (default: every gene folder)."""
    base = base_path or Path.cwd()
    org_dir = base / "genes" / organism
    targets = genes or sorted(p.name for p in org_dir.iterdir() if p.is_dir())
    results: Dict[str, List[str]] = {}
    for gene in targets:
        try:
            status, _, msg = emit_mod_deep_research(organism, gene, base, write=True, force=force)
        except Exception as e:  # network or parse failure for one gene
            status, msg = "error", str(e)
        results.setdefault(status, []).append(gene)
        if status in ("blocked", "error", "skipped"):
            logger.warning("%s %s: %s", gene, status, msg)
        elif status == "written" and msg != "ok":
            logger.warning("%s written despite identity check (--force): %s", gene, msg)
        if status != "skipped":
            time.sleep(delay)
    return results
