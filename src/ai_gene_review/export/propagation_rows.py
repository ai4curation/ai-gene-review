"""Offline extraction of homology-propagated GO annotations from cached GOA files.

A *propagated* annotation is one whose evidence is a function observed on some
other gene product and carried to the target: ISO/ISS/ISA transfers, PAINT IBA,
and the orthology components of the electronic pipelines (Ensembl Compara,
TreeGrafter). This module only parses what is already on disk
(``genes/*/*/*-goa.tsv`` and the matching ``*-ai-review.yaml``); resolving the
donor identifiers and checking the donor's current annotations happens in
:mod:`ai_gene_review.tools.refresh_propagation_sources`, which writes a cache
that the browser and stats builders read.

Method labels follow the GO_REF definitions in geneontology/go-site
``metadata/gorefs.yaml``.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Iterator, Optional

#: Evidence codes that transfer a function from a named donor gene product.
DONOR_EVIDENCE = {"ISO", "ISS", "ISA"}

#: GO_REF -> (method label, propagation class). Only GO_REFs listed here, plus
#: PMID-referenced ISO/ISS/ISA rows, are treated as homology propagation.
METHODS: dict[tuple[str, str], tuple[str, str]] = {
    ("ISO", "GO_REF:0000119"): ("Alliance human→mouse ISO", "ORTHOLOGY"),
    ("ISO", "GO_REF:0000096"): ("Alliance mouse↔rat ISO", "ORTHOLOGY"),
    ("ISO", "GO_REF:0000121"): ("RGD ISO from other mammals", "ORTHOLOGY"),
    ("ISO", "GO_REF:0000008"): ("MGI curated orthology", "ORTHOLOGY"),
    ("ISO", "GO_REF:0000024"): ("Manual ortholog transfer", "ORTHOLOGY"),
    ("ISS", "GO_REF:0000024"): ("Manual ortholog transfer", "SEQUENCE_SIMILARITY"),
    ("ISS", "GO_REF:0000114"): ("Manual complex transfer", "SEQUENCE_SIMILARITY"),
    ("ISO", "GO_REF:0000114"): ("Manual complex transfer", "ORTHOLOGY"),
    ("ISA", "GO_REF:0000113"): ("TFClass DbTF classification", "SEQUENCE_ALIGNMENT"),
    ("ISA", "GO_REF:0000024"): ("Manual ortholog transfer", "SEQUENCE_ALIGNMENT"),
    ("IBA", "GO_REF:0000033"): ("PAINT phylogenetic (IBA)", "PHYLOGENETIC"),
    ("IEA", "GO_REF:0000107"): ("Ensembl Compara (IEA)", "ELECTRONIC_ORTHOLOGY"),
    ("IEA", "GO_REF:0000118"): ("TreeGrafter (IEA)", "ELECTRONIC_PHYLOGENETIC"),
    ("IEA", "GO_REF:0000120"): ("Combined IEA (orthology component)", "ELECTRONIC_ORTHOLOGY"),
}

PAPER_METHOD_CLASS = {
    "ISO": "ORTHOLOGY",
    "ISS": "SEQUENCE_SIMILARITY",
    "ISA": "SEQUENCE_ALIGNMENT",
}

#: WITH/FROM prefixes that name a donor gene or gene product.
GENE_PREFIXES = {
    "UniProtKB", "MGI", "RGD", "SGD", "FB", "PomBase", "WB", "ZFIN", "TAIR",
    "dictyBase", "Xenbase", "EcoCyc", "CGD", "AspGD", "HGNC", "NCBIGene",
}

#: Species implied by MOD prefixes (used only when the donor is unresolved).
#: RGD is deliberately absent: it hosts genes for several mammals.
PREFIX_SPECIES = {
    "MGI": "Mus musculus",
    "SGD": "Saccharomyces cerevisiae",
    "FB": "Drosophila melanogaster",
    "PomBase": "Schizosaccharomyces pombe",
    "WB": "Caenorhabditis elegans",
    "ZFIN": "Danio rerio",
    "TAIR": "Arabidopsis thaliana",
    "dictyBase": "Dictyostelium discoideum",
    "Xenbase": "Xenopus",
    "HGNC": "Homo sapiens",
}

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}


@dataclass
class PropagatedRow:
    """One GOA row whose evidence is a transfer from other gene products."""

    species_dir: str
    gene_dir: str
    target_id: str
    target_symbol: str
    target_taxon: str
    target_taxon_label: str
    qualifier: str
    term_id: str
    term_label: str
    aspect: str
    evidence: str
    reference: str
    with_from: str
    assigned_by: str
    date: str
    method: str
    method_class: str
    donors: list[str] = field(default_factory=list)
    nodes: list[str] = field(default_factory=list)
    other_with: list[str] = field(default_factory=list)

    @property
    def negated(self) -> bool:
        return self.qualifier.startswith("NOT")


def classify(evidence: str, reference: str, with_from: str) -> Optional[tuple[str, str]]:
    """Return (method label, class) if the row is homology propagation.

    >>> classify("ISO", "GO_REF:0000119", "UniProtKB:P0DP25")
    ('Alliance human→mouse ISO', 'ORTHOLOGY')
    >>> classify("ISS", "PMID:123", "UniProtKB:P1")
    ('Paper-referenced ISS', 'SEQUENCE_SIMILARITY')
    >>> classify("IEA", "GO_REF:0000002", "InterPro:IPR1") is None
    True

    Combined IEA rows only count when an orthology source contributed, i.e.
    WITH/FROM carries Ensembl protein ids (Compara) or a PANTHER node.

    >>> classify("IEA", "GO_REF:0000120", "InterPro:IPR002048") is None
    True
    """
    method = METHODS.get((evidence, reference))
    if method:
        if reference == "GO_REF:0000120" and not re.search(
            r"(^|\|)(ensembl|PANTHER):", with_from
        ):
            return None
        return method
    if evidence in PAPER_METHOD_CLASS and reference.startswith("PMID:"):
        return f"Paper-referenced {evidence}", PAPER_METHOD_CLASS[evidence]
    return None


def split_with_from(with_from: str) -> tuple[list[str], list[str], list[str]]:
    """Split WITH/FROM into donor genes, PANTHER nodes, and other xrefs.

    >>> split_with_from("MGI:MGI:1|PANTHER:PTN0001|UniProtKB:P1-2|ensembl:ENSP1")
    (['MGI:MGI:1', 'UniProtKB:P1-2'], ['PANTHER:PTN0001'], ['ensembl:ENSP1'])
    """
    donors: list[str] = []
    nodes: list[str] = []
    other: list[str] = []
    for part in re.split(r"[|,]", with_from or ""):
        part = part.strip()
        if not part:
            continue
        prefix = part.split(":", 1)[0]
        if prefix == "PANTHER":
            nodes.append(part)
        elif prefix in GENE_PREFIXES:
            donors.append(part)
        else:
            other.append(part)
    return donors, nodes, other


def uniprot_base(xref: str) -> Optional[str]:
    """Return the canonical accession for a UniProtKB xref (isoform stripped).

    >>> uniprot_base("UniProtKB:P0DP25-2")
    'P0DP25'
    >>> uniprot_base("MGI:MGI:1") is None
    True
    """
    if not xref.startswith("UniProtKB:"):
        return None
    return xref.split(":", 1)[1].split("-", 1)[0]


def iter_goa_files(genes_dir: Path) -> Iterator[Path]:
    yield from sorted(genes_dir.glob("*/*/*-goa.tsv"))


def read_goa_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def iter_propagated_rows(genes_dir: Path) -> Iterator[PropagatedRow]:
    """Yield every homology-propagated row from the cached GOA files."""
    for path in iter_goa_files(genes_dir):
        species_dir, gene_dir = path.parent.parent.name, path.parent.name
        for row in read_goa_rows(path):
            evidence = row.get("GO EVIDENCE CODE", "")
            reference = row.get("REFERENCE", "")
            with_from = row.get("WITH/FROM", "") or ""
            method = classify(evidence, reference, with_from)
            if method is None:
                continue
            donors, nodes, other = split_with_from(with_from)
            yield PropagatedRow(
                species_dir=species_dir,
                gene_dir=gene_dir,
                target_id=f"{row.get('GENE PRODUCT DB', '')}:{row.get('GENE PRODUCT ID', '')}",
                target_symbol=row.get("SYMBOL", "") or gene_dir,
                target_taxon=row.get("TAXON ID", ""),
                target_taxon_label=row.get("TAXON NAME", ""),
                qualifier=row.get("QUALIFIER", ""),
                term_id=row.get("GO TERM", ""),
                term_label=row.get("GO NAME", ""),
                aspect=row.get("GO ASPECT", ""),
                evidence=evidence,
                reference=reference,
                with_from=with_from,
                assigned_by=row.get("ASSIGNED BY", ""),
                date=row.get("DATE", ""),
                method=method[0],
                method_class=method[1],
                donors=donors,
                nodes=nodes,
                other_with=other,
            )


def iter_target_evidence(genes_dir: Path) -> Iterator[tuple[str, str, str, str]]:
    """Yield (species_dir, gene_dir, term_id, evidence) for every GOA row.

    Used to ask whether a target already has IBA or experimental support for
    a term that it also receives by ISO.
    """
    for path in iter_goa_files(genes_dir):
        species_dir, gene_dir = path.parent.parent.name, path.parent.name
        for row in read_goa_rows(path):
            if (row.get("QUALIFIER") or "").startswith("NOT"):
                continue
            yield species_dir, gene_dir, row.get("GO TERM", ""), row.get("GO EVIDENCE CODE", "")
