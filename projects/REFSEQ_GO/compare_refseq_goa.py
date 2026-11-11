#!/usr/bin/env python3
"""Compare NCBI RefSeq (PGAP) GO annotations with GOA for one prokaryotic genome.

NCBI attaches GO terms to protein family models (NCBIFam/TIGRFAM HMMs, wrapped
Pfam HMMs, BlastRules, and CDD/SPARCLE domain architectures) and propagates them
only to the proteins each model *names*, so every protein carries GO from a
single evidence source. GOA/UniProt instead unions several pipelines
(InterPro2GO, TreeGrafter, ARBA, UniRule, EC2GO, Rhea, SubCell, ...). This script
joins the two at the gene level and measures where they agree, including whether
agreement depends on which NCBI evidence type supplied the term.

Join path (gene models are compared, not assumed identical)::

    RefSeq WP_ --(CDS old_locus_tag, from the GenBank record or feature table)--> PP_xxxx
    UniProt accession --(ordered locus name in Gene Names)--> PP_xxxx

The assembly is resolved with the NCBI Datasets v2 REST API: a versionless
accession resolves to the current version, and a superseded accession is
rejected. NCBI's Python client (``ncbi-datasets-pylib``) was retired in December
2024, so the REST API is called directly.

NCBI GO can come from two places (``--ncbi-source``):

* ``live`` (default): the RefSeq GenBank record of each assembly sequence, from
  E-utilities. CDS features carry ``/GO_function``, ``/GO_process`` and
  ``/GO_component``; this is the annotation shown on the NCBI website. The
  genome record does not say which family model named each protein, so that
  comes from the ``Evidence-For-Name-Assignment`` block of the WP_ protein
  records, fetched in batches.
* ``wp``: the WP_ protein records themselves, reached through the UniProt
  entries' RefSeq cross-references. PGAP assigns GO per non-redundant protein,
  so a WP_ record carries the same GO in every genome that encodes it, plus its
  naming model. This compares protein by protein and works for genomes PGAP
  does not annotate (the curated references, e.g. *E. coli* K-12 MG1655),
  because their proteins are identical to WP_ proteins PGAP annotates elsewhere.
  Gene models are not compared in this mode.
* ``ftp``: the per-assembly GAF and feature table in ``genomes/all``. These can
  lag the live record by a full annotation release (for KT2440 in October 2026,
  ``RS_2025_02_17`` on FTP and in Datasets against ``RS_2026_02_04`` live).
  Datasets genome packages have no GO option, so there is no third route.

Inputs are downloaded into ``--cache-dir/<assembly>/`` on first use, or
re-downloaded with ``--refresh``:

* live: ``live/<sequence>.gbk`` (efetch gbwithparts), ``live/wp_records.gp``
* wp:   ``wp/wp_records.gp`` (efetch GenPept for every cross-referenced WP_)
* ftp:  ``ftp-<release>/ncbi.gaf.gz``, ``ftp-<release>/feature_table.txt.gz``
* GOA           QuickGO ``annotation/downloadSearch`` for the taxon
* UniProt       REST ``uniprotkb/stream`` for the proteome (accession, genes, RefSeq)

Counterfactual (``--union-models family|all``): PGAP passes on GO only from the one model
that names a protein. With this flag the NCBI side also gets the GO of every
other NCBIfam/TIGRFAM HMM the protein matches, including NCBI's copies of Pfam
models with ``all`` (``hmm_PGAP.tsv``). Matches are InterPro's, as recorded in each UniProt
entry's NCBIfam and Pfam cross-references, since PGAP does not publish its own
hit lists. Added terms are labelled ``added:<model type>``. CDD/SPARCLE
architectures cannot be added: only the winning architecture is visible.

Term comparison is closure-aware over is_a + part_of using the oaklib GO
sqlite (``sqlite:obo:go``): an NCBI term is ``exact`` if GOA has the same term,
``goa_more_specific`` if GOA has a proper descendant, ``goa_more_general`` if
GOA has only a proper ancestor, otherwise ``ncbi_only`` (and symmetrically for
GOA terms).

Usage::

    uv run python projects/REFSEQ_GO/compare_refseq_goa.py \\
        --accession GCF_000007565 --taxon 160488 \\
        --proteome UP000000556 --locus-regex 'PP_\\d+' \\
        --out-dir projects/REFSEQ_GO/results/PSEPK
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import typer
import yaml

app = typer.Typer(add_completion=False)

NCBI_FTP = "https://ftp.ncbi.nlm.nih.gov/genomes/all"
DATASETS_API = "https://api.ncbi.nlm.nih.gov/datasets/v2"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
GO_QUALIFIER_ASPECT = {"GO_function": "F", "GO_process": "P", "GO_component": "C"}
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
HMM_PGAP_URL = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv"
UNIPROT_STREAM = "https://rest.uniprot.org/uniprotkb/stream"

# GO_REF -> GOA/UniProt pipeline label (electronic pipelines only; the rest are
# reported by evidence code).
GOREF_PIPELINE = {
    "GO_REF:0000002": "InterPro2GO",
    "GO_REF:0000003": "EC2GO",
    "GO_REF:0000033": "IBA (PAINT)",
    "GO_REF:0000041": "UniPathway2GO",
    "GO_REF:0000043": "UniProtKB-KW2GO",
    "GO_REF:0000044": "UniProtKB-SubCell2GO",
    "GO_REF:0000104": "UniRule",
    "GO_REF:0000107": "Ensembl Compara",
    "GO_REF:0000108": "GO inter-ontology links",
    "GO_REF:0000116": "Rhea2GO",
    "GO_REF:0000117": "ARBA",
    "GO_REF:0000118": "TreeGrafter",
    "GO_REF:0000120": "Combined IEA (Rhea/EC/...)",
}


def ncbi_source_type(with_from: str) -> str:
    """Classify the single NCBI WITH/FROM evidence token.

    >>> ncbi_source_type("HMM:NF008114.0")
    'HMM:NF'
    >>> ncbi_source_type("HMM:TIGR00417.1")
    'HMM:TIGR'
    >>> ncbi_source_type("ArchId:10112604")
    'ArchId (CDD/SPARCLE)'
    >>> ncbi_source_type("NBR000289")
    'BlastRule'
    >>> ncbi_source_type("cluster:879959")
    'cluster'
    >>> ncbi_source_type("")
    'none'
    """
    if not with_from:
        return "none"
    if with_from.startswith("HMM:"):
        return "HMM:" + re.sub(r"[\d.]+$", "", with_from[4:])
    if with_from.startswith("ArchId:"):
        return "ArchId (CDD/SPARCLE)"
    if with_from.startswith("NBR"):
        return "BlastRule"
    return with_from.split(":")[0]


def goa_source(evidence: str, reference: str) -> str:
    """Label a GOA row by pipeline (electronic) or evidence code (otherwise).

    >>> goa_source("IEA", "GO_REF:0000002")
    'InterPro2GO'
    >>> goa_source("IDA", "PMID:123")
    'IDA'
    """
    if evidence == "IEA":
        return GOREF_PIPELINE.get(reference, f"IEA {reference}")
    return evidence


def fetch(
    url: str, dest: Path, accept: str | None = None, refresh: bool = False
) -> Path:
    if dest.exists() and not refresh:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"Accept": accept} if accept else {})
    with urllib.request.urlopen(req, timeout=300) as resp:
        dest.write_bytes(resp.read())
    return dest


def resolve_assembly(accession: str) -> dict:
    """Resolve a RefSeq accession to its current version and annotation release."""
    # all_assemblies makes superseded versions resolvable, so they can be reported
    # as superseded rather than as unknown (matches `datasets summary genome accession`).
    url = (
        f"{DATASETS_API}/genome/accession/{accession}/dataset_report"
        "?filters.assembly_version=all_assemblies"
    )
    with urllib.request.urlopen(url, timeout=120) as resp:
        reports = json.load(resp).get("reports", [])
    if not reports:
        raise typer.BadParameter(
            f"NCBI Datasets has no assembly report for {accession}"
        )
    r = reports[0]
    if r["accession"] != r["current_accession"]:
        raise typer.BadParameter(
            f"{r['accession']} is superseded by {r['current_accession']}"
        )
    ann = r.get("annotation_info", {})
    return {
        "accession": r["current_accession"],
        "assembly_dir": f"{r['current_accession']}_{r['assembly_info']['assembly_name']}",
        "annotation_release": ann.get("name"),
        "annotation_release_date": ann.get("release_date"),
        "annotation_pipeline": f"{ann.get('pipeline')} {ann.get('software_version')}",
    }


def gaf_header(path: Path) -> dict[str, str]:
    """Return ``key: value`` pairs from the GAF's ``!`` header lines."""
    out = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if not line.startswith("!"):
                break
            key, sep, value = line[1:].partition(":")
            if sep and value.strip() and not key.startswith("#"):
                out[key.strip()] = value.strip()
    return out


def assembly_url(assembly: str, suffix: str) -> str:
    acc = assembly.split("_")[0] + "_" + assembly.split("_")[1]
    digits = acc.split("_")[1].split(".")[0]
    path = "/".join([acc[:3], digits[0:3], digits[3:6], digits[6:9], assembly])
    return f"{NCBI_FTP}/{path}/{assembly}_{suffix}"


def naming_evidence(gp_record: str) -> str:
    r"""Return the naming model of a GenPept record as a GAF-style WITH/FROM token.

    >>> naming_evidence("Evidence Category  :: HMM\nEvidence Accession :: NF015431.7")
    'HMM:NF015431.7'
    >>> naming_evidence(
    ...     "Evidence Category  :: Conserved Domain (CDD)\n"
    ...     "Evidence Accession :: Domain architecture ID 11426483"
    ... )
    'ArchId:11426483'
    >>> naming_evidence("Evidence Category  :: BlastRule\nEvidence Accession :: NBR000289")
    'NBR000289'
    >>> naming_evidence("no evidence block")
    ''
    """
    cat = re.search(r"Evidence Category\s*::\s*(.+)", gp_record)
    acc = re.search(r"Evidence Accession\s*::\s*(.+)", gp_record)
    if not cat or not acc:
        return ""
    category, accession = cat.group(1).strip(), acc.group(1).strip()
    if category == "HMM":
        return f"HMM:{accession}"
    if category.startswith("Conserved Domain"):
        return f"ArchId:{accession.split()[-1]}"
    if category == "BlastRule":
        return accession
    return f"{category}:{accession}"


def post(url: str, data: dict[str, str]) -> bytes:
    body = urllib.parse.urlencode(data).encode()
    with urllib.request.urlopen(url, data=body, timeout=300) as resp:
        return resp.read()


def assembly_sequences(accession: str) -> list[str]:
    """RefSeq accessions of the assembly's sequences (chromosomes and plasmids)."""
    url = f"{DATASETS_API}/genome/accession/{accession}/sequence_reports"
    with urllib.request.urlopen(url, timeout=120) as resp:
        reports = json.load(resp).get("reports", [])
    return [r["refseq_accession"] for r in reports if r.get("refseq_accession")]


def genbank_annotation(path: Path) -> dict[str, str]:
    """Annotation Name/Date/Software revision from a GenBank structured comment."""
    out = {}
    with path.open() as fh:
        for line in fh:
            if line.startswith("FEATURES"):
                break
            m = re.match(r"\s+(Annotation [A-Za-z ]+?)\s+::\s+(.+)", line)
            if m:
                out[m.group(1)] = m.group(2).strip()
    return out


@dataclass
class Annot:
    term: str
    aspect: str
    source: str


@dataclass
class NcbiData:
    """NCBI annotation for one assembly, from either source."""

    annot: dict[str, list[Annot]]  # WP_ -> GO annotations
    wp_to_loci: dict[str, set[str]]  # WP_ -> old (or current) locus tags
    products: dict[str, str]  # WP_ -> RefSeq product name
    naming: dict[str, str]  # WP_ -> naming model (GAF WITH/FROM style)
    counts: Counter
    provenance: dict
    files: list[Path]
    sequences: dict[str, str] = field(default_factory=dict)  # WP_ -> protein sequence


@dataclass
class Gene:
    locus: str
    wp: set[str] = field(default_factory=set)
    accessions: set[str] = field(default_factory=set)
    ncbi: list[Annot] = field(default_factory=list)
    goa: list[Annot] = field(default_factory=list)


def load_ncbi_ftp(resolved: dict, cache: Path, refresh: bool) -> NcbiData:
    assembly = resolved["assembly_dir"]
    sub = cache / f"ftp-{resolved['annotation_release']}"
    gaf = fetch(
        assembly_url(assembly, "gene_ontology.gaf.gz"),
        sub / "ncbi.gaf.gz",
        refresh=refresh,
    )
    ft = fetch(
        assembly_url(assembly, "feature_table.txt.gz"),
        sub / "feature_table.txt.gz",
        refresh=refresh,
    )
    annot: dict[str, list[Annot]] = defaultdict(list)
    naming: dict[str, str] = {}
    with gzip.open(gaf, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if "NOT" in c[3]:
                continue
            annot[c[1]].append(Annot(c[4], c[8], ncbi_source_type(c[7])))
            naming[c[1]] = c[7]
    rs_to_old: dict[str, str] = {}
    cds: list[tuple[str, str]] = []
    products: dict[str, str] = {}
    counts: Counter = Counter()
    with gzip.open(ft, "rt") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if row[0].startswith("#"):
                continue
            feature, klass, locus, attrs = row[0], row[1], row[16], row[19]
            counts[f"{feature}:{klass}"] += 1
            if feature == "gene":
                m = re.search(r"old_locus_tag=([^;]+)", attrs)
                if m:
                    rs_to_old[locus] = m.group(1)
            elif feature == "CDS" and row[10]:
                cds.append((row[10], locus))
                products[row[10]] = row[13]
    wp_to_loci: dict[str, set[str]] = defaultdict(set)
    for wp, locus in cds:
        wp_to_loci[wp].add(rs_to_old.get(locus, locus))
    header = gaf_header(gaf)
    provenance = {
        "ncbi_source": "ftp",
        "annotation_release": resolved["annotation_release"],
        "annotation_release_date": resolved["annotation_release_date"],
        "annotation_pipeline": resolved["annotation_pipeline"],
        "ncbi_gaf_date_generated": header.get("date-generated"),
        "ncbi_gaf_go_version": header.get("GO version"),
    }
    return NcbiData(annot, wp_to_loci, products, naming, counts, provenance, [gaf, ft])


def parse_genpept(text: str) -> dict[str, dict]:
    r"""Parse GenPept text into WP_ -> {product, naming, date, go: [(term, aspect)]}.

    >>> rec = parse_genpept(
    ...     "LOCUS       WP_1   5 aa  linear   BCT 06-AUG-2026\n"
    ...     "VERSION     WP_1.1\n"
    ...     "            Evidence Category  :: HMM\n"
    ...     "            Evidence Accession :: TIGR02348.1\n"
    ...     "FEATURES             Location/Qualifiers\n"
    ...     "     Protein         1..5\n"
    ...     '                     /product="chaperonin GroEL"\n'
    ...     '                     /GO_function="GO:0140662 - ATP-dependent protein folding\n'
    ...     '                     chaperone [Evidence IEA]"\n'
    ...     '                     /GO_process="GO:0042026 - protein refolding [Evidence IEA]"\n'
    ...     "//\n"
    ... )
    >>> rec["WP_1.1"]["naming"], rec["WP_1.1"]["product"], rec["WP_1.1"]["date"]
    ('HMM:TIGR02348.1', 'chaperonin GroEL', '06-AUG-2026')
    >>> rec["WP_1.1"]["go"]
    [('GO:0140662', 'F'), ('GO:0042026', 'P')]
    """
    out: dict[str, dict] = {}
    for record in text.split("\n//"):
        version = re.search(r"^VERSION\s+(\S+)", record, re.M)
        if not version:
            continue
        date = re.search(r"^LOCUS.*?(\d{2}-[A-Z]{3}-\d{4})\s*$", record, re.M)
        product = re.search(r'/product="(.*?)"', record, re.S)
        go = []
        for qual, value in re.findall(
            r'/(GO_function|GO_process|GO_component)="(.*?)"', record, re.S
        ):
            for term in re.findall(r"GO:\d{7}", value):
                go.append((term, GO_QUALIFIER_ASPECT[qual]))
        out[version.group(1)] = {
            "naming": naming_evidence(record),
            "product": " ".join(product.group(1).split()) if product else "",
            "date": date.group(1) if date else "",
            "go": go,
        }
    return out


def fetch_wp_records(wps: list[str], dest: Path, refresh: bool) -> dict[str, dict]:
    """Fetch GenPept records for WP_ accessions (cached as one text file) and parse them."""
    if refresh or not dest.exists():
        chunks = []
        for i in range(0, len(wps), 200):
            chunks.append(
                post(
                    f"{EUTILS}/efetch.fcgi",
                    {
                        "db": "protein",
                        "rettype": "gp",
                        "retmode": "text",
                        "id": ",".join(wps[i : i + 200]),
                    },
                ).decode()
            )
            typer.echo(f"  WP_ records {min(i + 200, len(wps))}/{len(wps)}", err=True)
            time.sleep(0.4)  # E-utilities allows 3 requests/s without an API key
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("".join(chunks))
    records = parse_genpept(dest.read_text())
    missing = set(wps) - set(records)
    if missing:
        raise RuntimeError(
            f"{len(missing)} WP_ records not returned, e.g. {sorted(missing)[:3]}"
        )
    return records


def load_ncbi_live(resolved: dict, cache: Path, refresh: bool) -> NcbiData:
    from Bio import SeqIO

    sub = cache / "live"
    records = [
        fetch(
            f"{EUTILS}/efetch.fcgi?db=nuccore&id={seq}&rettype=gbwithparts&retmode=text",
            sub / f"{seq}.gbk",
            refresh=refresh,
        )
        for seq in assembly_sequences(resolved["accession"])
    ]
    annot: dict[str, list[Annot]] = defaultdict(list)
    wp_to_loci: dict[str, set[str]] = defaultdict(set)
    products: dict[str, str] = {}
    sequences: dict[str, str] = {}
    counts: Counter = Counter()
    for path in records:
        for rec in SeqIO.parse(path, "genbank"):
            for f in rec.features:
                q = f.qualifiers
                if f.type == "gene":
                    counts["gene:pseudogene" if "pseudo" in q else "gene"] += 1
                if f.type != "CDS":
                    continue
                if "protein_id" not in q:
                    counts["CDS:without_protein"] += 1
                    continue
                counts["CDS:with_protein"] += 1
                wp = q["protein_id"][0]
                wp_to_loci[wp].add(q.get("old_locus_tag", q["locus_tag"])[0])
                products[wp] = q.get("product", [""])[0]
                if "translation" in q:
                    sequences[wp] = q["translation"][0]
                if wp in annot:  # identical protein at another locus: same GO
                    continue
                for qual, aspect in GO_QUALIFIER_ASPECT.items():
                    for value in q.get(qual, []):
                        for term in re.findall(r"GO:\d{7}", value):
                            annot[wp].append(Annot(term, aspect, ""))
    wp_records = fetch_wp_records(sorted(products), sub / "wp_records.gp", refresh)
    naming = {wp: r["naming"] for wp, r in wp_records.items()}
    for wp, annots in annot.items():
        for a in annots:
            a.source = ncbi_source_type(naming.get(wp, ""))
    ann = genbank_annotation(records[0])
    provenance = {
        "ncbi_source": "live",
        "annotation_release": ann.get("Annotation Name"),
        "annotation_date": ann.get("Annotation Date"),
        "annotation_pipeline": ann.get("Annotation Software revision"),
        "datasets_annotation_release": resolved["annotation_release"],
    }
    files = records + [sub / "wp_records.gp"]
    return NcbiData(
        annot, wp_to_loci, products, naming, counts, provenance, files, sequences
    )


def load_ncbi_wp(
    uniprot: dict[str, tuple[set[str], set[str]]], cache: Path, refresh: bool
) -> NcbiData:
    """NCBI GO from the WP_ records that the UniProt entries cross-reference."""
    wp_to_loci: dict[str, set[str]] = defaultdict(set)
    for loci, wps in uniprot.values():
        for wp in wps:
            wp_to_loci[wp] |= loci
    dest = cache / "wp" / "wp_records.gp"
    wp_records = fetch_wp_records(sorted(wp_to_loci), dest, refresh)
    annot: dict[str, list[Annot]] = defaultdict(list)
    for wp, r in wp_records.items():
        source = ncbi_source_type(r["naming"])
        annot[wp] = [Annot(term, aspect, source) for term, aspect in r["go"]]
    dates = sorted(
        (r["date"] for r in wp_records.values() if r["date"]),
        key=lambda d: datetime.strptime(d, "%d-%b-%Y"),
    )
    counts = Counter(
        {
            "uniprot_entries": len(uniprot),
            "uniprot_entries_with_wp": sum(1 for _, w in uniprot.values() if w),
            "wp_records": len(wp_records),
            "wp_records_with_go": sum(1 for r in wp_records.values() if r["go"]),
        }
    )
    provenance = {
        "ncbi_source": "wp",
        "annotation_release": "current WP_ records",
        "wp_record_dates": {"oldest": dates[0], "newest": dates[-1]} if dates else {},
    }
    return NcbiData(
        annot,
        wp_to_loci,
        {wp: r["product"] for wp, r in wp_records.items()},
        {wp: r["naming"] for wp, r in wp_records.items()},
        counts,
        provenance,
        [dest],
    )


def read_uniprot_sequences(path: Path) -> dict[str, str]:
    """UniProt accession -> sequence."""
    with path.open() as fh:
        return {r["Entry"]: r["Sequence"] for r in csv.DictReader(fh, delimiter="\t")}


def read_uniprot(
    path: Path, locus_re: re.Pattern
) -> dict[str, tuple[set[str], set[str]]]:
    """Return accession -> (ordered locus names, RefSeq WP_ xrefs)."""
    out = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            loci = set(locus_re.findall(row["Gene Names"] or ""))
            # Keep only non-redundant WP_ proteins; reference genomes also list
            # their genome-specific NP_ records, which carry no PGAP GO.
            # Entries can carry an isoform tag: "WP_000083955.1 [Q59385-1]".
            wps = {
                w.split()[0]
                for w in (row["RefSeq"] or "").split(";")
                if w.startswith("WP_")
            }
            out[row["Entry"]] = (loci, wps)
    return out


# WITH/FROM prefix -> pipeline, for GO_REF:0000120 rows (terms agreed by several
# IEA methods), so each contributing pipeline is credited.
WITH_PREFIX_PIPELINE = {
    "InterPro": "InterPro2GO",
    "PANTHER": "TreeGrafter",
    "UniRule": "UniRule",
    "ARBA": "ARBA",
    "EC": "EC2GO",
    "RHEA": "Rhea2GO",
    "UniProtKB-SubCell": "UniProtKB-SubCell2GO",
    "UniPathway": "UniPathway2GO",
    "UniProtKB-KW": "UniProtKB-KW2GO",
    "GO": "GO inter-ontology links",
}


def combined_pipelines(with_from: str) -> list[str]:
    """Pipelines behind a combined (GO_REF:0000120) row, from its WITH/FROM.

    >>> combined_pipelines("InterPro:IPR000847|InterPro:IPR058163|PANTHER:PTN009110665")
    ['InterPro2GO', 'TreeGrafter']
    >>> combined_pipelines("RHEA:47992|EC:7.1.1.1")
    ['EC2GO', 'Rhea2GO']
    """
    out = {
        WITH_PREFIX_PIPELINE.get(x.split(":")[0], "Combined IEA (other)")
        for x in with_from.split("|")
        if x
    }
    return sorted(out) or ["Combined IEA (other)"]


def read_goa(path: Path) -> dict[str, list[Annot]]:
    out: dict[str, list[Annot]] = defaultdict(list)
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if "NOT" in row["QUALIFIER"]:
                continue
            if row["REFERENCE"] == "GO_REF:0000120":
                sources = combined_pipelines(row["WITH/FROM"])
            else:
                sources = [goa_source(row["GO EVIDENCE CODE"], row["REFERENCE"])]
            for source in sources:
                out[row["GENE PRODUCT ID"]].append(
                    Annot(row["GO TERM"], row["GO ASPECT"], source)
                )
    return out


class Closure:
    def __init__(self) -> None:
        from oaklib import get_adapter
        from oaklib.datamodels.vocabulary import IS_A, PART_OF

        self.adapter = get_adapter("sqlite:obo:go")
        self.preds = [IS_A, PART_OF]
        self.cache: dict[str, set[str]] = {}

    def ancestors(self, term: str) -> set[str]:
        if term not in self.cache:
            self.cache[term] = set(
                self.adapter.ancestors(term, predicates=self.preds, reflexive=True)
            )
        return self.cache[term]


def relation(term: str, others: set[str], closure: Closure) -> str:
    if term in others:
        return "exact"
    anc = closure.ancestors(term)
    if any(term in closure.ancestors(o) for o in others):
        return "other_more_specific"
    if anc & others:
        return "other_more_general"
    return "only"


def union_model_go(
    accessions: set[str],
    xrefs: dict[str, set[str]],
    model_go: dict[str, list[str]],
    pfam_copies: dict[str, list[str]],
) -> list[tuple[str, str]]:
    """(term, model type) for every GO-bearing NCBI HMM matched by these UniProt entries.

    >>> union_model_go(
    ...     {"P1"},
    ...     {"P1": {"TIGR02275", "PF00501"}},
    ...     {"TIGR02275": ["GO:0008668"], "NF000001": ["GO:0016874"]},
    ...     {"PF00501": ["NF000001"]},
    ... )
    [('GO:0008668', 'HMM:TIGR'), ('GO:0016874', 'HMM:NF (Pfam copy)')]
    """
    out = set()
    for acc in accessions:
        for model in xrefs.get(acc, ()):
            if model.startswith("PF"):
                for nf in pfam_copies.get(model, []):
                    out |= {(t, "HMM:NF (Pfam copy)") for t in model_go.get(nf, [])}
            else:
                kind = "HMM:TIGR" if model.startswith("TIGR") else "HMM:NF"
                out |= {(t, kind) for t in model_go.get(model, [])}
    return sorted(out)


def read_hmm_pgap(path: Path) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Model -> GO terms, and Pfam accession -> NCBI's wrapping NF models (no versions)."""
    model_go: dict[str, list[str]] = {}
    pfam_copies: dict[str, list[str]] = defaultdict(list)
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            acc = row["#ncbi_accession"].split(".")[0]
            if row["go_terms"]:
                model_go[acc] = row["go_terms"].split(",")
            src = row["source_identifier"]
            if src.startswith("PF"):
                pfam_copies[src.split(".")[0]].append(acc)
    return model_go, pfam_copies


def read_uniprot_models(path: Path) -> dict[str, set[str]]:
    """UniProt accession -> NCBIfam/TIGRFAM and Pfam accessions it matches."""
    out = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ids = (row["NCBIfam"] or "") + ";" + (row["Pfam"] or "")
            out[row["Entry"]] = {x.strip() for x in ids.split(";") if x.strip()}
    return out


@app.command()
def main(
    accession: str = typer.Option(
        ...,
        help="RefSeq assembly accession; versionless resolves to current, e.g. GCF_000007565",
    ),
    taxon: int = typer.Option(..., help="NCBI taxon id for the GOA query"),
    proteome: str = typer.Option(..., help="UniProt proteome id"),
    locus_regex: str = typer.Option(
        ..., help="Regex matching ordered locus names, e.g. 'PP_\\d+'"
    ),
    out_dir: Path = typer.Option(
        ..., help="Directory for summary.yaml and comparison TSV"
    ),
    cache_dir: Path = typer.Option(Path(".cache/refseq_go"), help="Download cache"),
    refresh: bool = typer.Option(False, help="Re-download all inputs"),
    ncbi_source: str = typer.Option(
        "live",
        help="'live' (GenBank record), 'wp' (WP_ protein records) or 'ftp' (GAF)",
    ),
    union_models: str = typer.Option(
        "none",
        help="Counterfactual: 'family' adds GO from every matched NCBIfam/TIGRFAM HMM; "
        "'all' also from NCBI's copies of Pfam models; 'none' (default) adds nothing",
    ),
) -> None:
    resolved = resolve_assembly(accession)
    assembly = resolved["assembly_dir"]
    cache = cache_dir / assembly
    up_path = fetch(
        f"{UNIPROT_STREAM}?query=proteome:{proteome}&format=tsv&fields=accession,gene_names,xref_refseq,sequence",
        cache / "uniprot_seq.tsv",
        refresh=refresh,
    )
    locus_re = re.compile(locus_regex)
    uniprot = read_uniprot(up_path, locus_re)
    if ncbi_source == "live":
        nd = load_ncbi_live(resolved, cache, refresh)
    elif ncbi_source == "wp":
        nd = load_ncbi_wp(uniprot, cache, refresh)
    elif ncbi_source == "ftp":
        nd = load_ncbi_ftp(resolved, cache, refresh)
    else:
        raise typer.BadParameter(
            f"--ncbi-source must be live, wp or ftp, not {ncbi_source}"
        )
    # Entries with no ordered locus name are joined by identical sequence to a
    # RefSeq protein (live mode, where translations are available).
    up_seqs = read_uniprot_sequences(up_path)
    seq_to_wp: dict[str, str] = {}
    for wp, sq in nd.sequences.items():
        seq_to_wp.setdefault(sq, wp)
    joined_by_sequence = 0
    for acc, (loci, wps) in list(uniprot.items()):
        wp = seq_to_wp.get(up_seqs.get(acc, ""))
        if not loci and wp:
            uniprot[acc] = (set(nd.wp_to_loci[wp]), wps)
            joined_by_sequence += 1
    goa_path = fetch(
        f"{QUICKGO}?taxonId={taxon}&taxonUsage=exact&downloadLimit=2000000"
        "&selectedFields=geneProductId,symbol,qualifier,goId,goAspect,goEvidence,reference,withFrom,assignedBy",
        cache / "goa.tsv",
        accept="text/tsv",
        refresh=refresh,
    )

    ncbi, wp_to_loci, ft_counts = nd.annot, nd.wp_to_loci, nd.counts
    goa = read_goa(goa_path)

    genes: dict[str, Gene] = {}

    def gene(locus: str) -> Gene:
        return genes.setdefault(locus, Gene(locus))

    for wp, loci in wp_to_loci.items():
        for locus in loci:
            gene(locus).wp.add(wp)
    for acc, (loci, _) in uniprot.items():
        for locus in loci:
            gene(locus).accessions.add(acc)
    for g in genes.values():
        # A WP_ shared by several loci (identical paralogs) gives each locus the same GO.
        g.ncbi = [a for wp in g.wp for a in ncbi.get(wp, [])]
        g.goa = [a for acc in g.accessions for a in goa.get(acc, [])]

    closure = Closure()
    union_stats: dict[str, Counter] = defaultdict(Counter)
    if union_models not in ("none", "family", "all"):
        raise typer.BadParameter("--union-models must be none, family or all")
    if union_models != "none":
        model_go, pfam_copies = read_hmm_pgap(
            fetch(HMM_PGAP_URL, cache_dir / "hmm_PGAP.tsv", refresh=refresh)
        )
        xrefs = read_uniprot_models(
            fetch(
                f"{UNIPROT_STREAM}?query=proteome:{proteome}&format=tsv&fields=accession,xref_ncbifam,xref_pfam",
                cache / "uniprot_models.tsv",
                refresh=refresh,
            )
        )
        roots = {"GO:0003674": "F", "GO:0008150": "P", "GO:0005575": "C"}
        for g in genes.values():
            if not (g.wp and g.accessions):
                continue
            have = {a.term for a in g.ncbi}
            naming = "|".join(sorted({a.source for a in g.ncbi})) or "no GO"
            added = 0
            for term, kind in union_model_go(
                g.accessions, xrefs, model_go, pfam_copies
            ):
                if union_models == "family" and kind == "HMM:NF (Pfam copy)":
                    continue
                if term in have:
                    continue
                aspect = next(
                    (a for r, a in roots.items() if r in closure.ancestors(term)), None
                )
                if aspect is None:
                    continue  # obsolete, or unknown to the local GO build
                g.ncbi.append(Annot(term, aspect, f"added:{kind}"))
                have.add(term)
                added += 1
                union_stats["terms_added_by_model_type"][kind] += 1
            union_stats["genes_by_original_naming_source"][naming] += 1
            if added:
                union_stats["genes_gaining_terms_by_original_naming_source"][
                    naming
                ] += 1

    unjoined_up = [a for a, (loci, _) in uniprot.items() if not loci]
    gene_models = {
        "feature_counts": dict(sorted(ft_counts.items())),
        "loci_total": len(genes),
        "loci_with_refseq_protein": sum(1 for g in genes.values() if g.wp),
        "loci_with_uniprot_entry": sum(1 for g in genes.values() if g.accessions),
        "loci_in_both": sum(1 for g in genes.values() if g.wp and g.accessions),
        "loci_refseq_only": sum(1 for g in genes.values() if g.wp and not g.accessions),
        "loci_uniprot_only": sum(
            1 for g in genes.values() if g.accessions and not g.wp
        ),
        "uniprot_entries_joined_by_sequence": joined_by_sequence,
        "uniprot_entries_without_locus_tag": len(unjoined_up),
        "wp_shared_by_multiple_loci": sum(
            1 for loci in wp_to_loci.values() if len(loci) > 1
        ),
        "uniprot_entries_lacking_refseq_xref": sum(
            1 for _, wps in uniprot.values() if not wps
        ),
    }

    both = [g for g in genes.values() if g.wp and g.accessions]
    coverage = {
        "loci_compared": len(both),
        "with_ncbi_go": sum(1 for g in both if g.ncbi),
        "with_goa_go": sum(1 for g in both if g.goa),
        "with_goa_iea_go": sum(
            1
            for g in both
            if any(
                a.source in GOREF_PIPELINE.values() or a.source.startswith("IEA")
                for a in g.goa
            )
        ),
        "with_both": sum(1 for g in both if g.ncbi and g.goa),
        "ncbi_annotations": sum(len({(a.term) for a in g.ncbi}) for g in both),
        "goa_annotations": sum(len({(a.term) for a in g.goa}) for g in both),
    }

    rows = []
    ncbi_rel: dict[str, Counter] = defaultdict(Counter)
    goa_rel: dict[str, Counter] = defaultdict(Counter)
    for g in sorted(both, key=lambda x: x.locus):
        for aspect in "FPC":
            n_terms = {a.term: a.source for a in g.ncbi if a.aspect == aspect}
            g_terms: dict[str, set[str]] = defaultdict(set)
            for a in g.goa:
                if a.aspect == aspect:
                    g_terms[a.term].add(a.source)
            # Only compare where both sides annotate the protein in this aspect,
            # so absence of a whole aspect is reported via coverage, not as disagreement.
            if not n_terms or not g_terms:
                for t, src in n_terms.items():
                    rows.append(
                        (g.locus, aspect, "ncbi", t, src, "other_side_no_aspect")
                    )
                    ncbi_rel[src]["other_side_no_aspect"] += 1
                for t, srcs in g_terms.items():
                    rows.append(
                        (
                            g.locus,
                            aspect,
                            "goa",
                            t,
                            "|".join(sorted(srcs)),
                            "other_side_no_aspect",
                        )
                    )
                    for s in srcs:
                        goa_rel[s]["other_side_no_aspect"] += 1
                continue
            for t, src in n_terms.items():
                rel = relation(t, set(g_terms), closure)
                rows.append((g.locus, aspect, "ncbi", t, src, rel))
                ncbi_rel[src][rel] += 1
            for t, srcs in g_terms.items():
                rel = relation(t, set(n_terms), closure)
                rows.append((g.locus, aspect, "goa", t, "|".join(sorted(srcs)), rel))
                for s in srcs:
                    goa_rel[s][rel] += 1

    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "term_comparison.tsv").open("w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(
            ["locus", "aspect", "side", "go_id", "source", "relation_to_other_side"]
        )
        w.writerows(rows)
    with (out_dir / "loci.tsv").open("w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["locus", "refseq_proteins", "uniprot_accessions", "ncbi_sources"])
        for g in sorted(genes.values(), key=lambda x: x.locus):
            w.writerow(
                [
                    g.locus,
                    "|".join(sorted(g.wp)),
                    "|".join(sorted(g.accessions)),
                    "|".join(sorted({a.source for a in g.ncbi})),
                ]
            )
    with (out_dir / "ncbi_proteins.tsv").open("w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["refseq_protein", "loci", "product", "naming_evidence", "go_terms"])
        for wp in sorted(nd.products):
            w.writerow(
                [
                    wp,
                    "|".join(sorted(nd.wp_to_loci.get(wp, ()))),
                    nd.products[wp],
                    nd.naming.get(wp, ""),
                    "|".join(sorted({a.term for a in ncbi.get(wp, [])})),
                ]
            )

    summary = {
        "assembly": assembly,
        **nd.provenance,
        "inputs_fetched_utc": {
            p.name: datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).isoformat(
                timespec="seconds"
            )
            for p in (*nd.files, goa_path, up_path)
        },
        "taxon": taxon,
        "proteome": proteome,
        "gene_models": gene_models,
        "coverage": coverage,
        "union_models": {
            "mode": union_models,
            **{k: dict(v) for k, v in union_stats.items()},
        },
        "ncbi_terms_by_source_vs_goa": {
            k: dict(v) for k, v in sorted(ncbi_rel.items())
        },
        "goa_terms_by_source_vs_ncbi": {k: dict(v) for k, v in sorted(goa_rel.items())},
    }
    with (out_dir / "summary.yaml").open("w") as fh:
        yaml.safe_dump(summary, fh, sort_keys=False)
    typer.echo(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    app()
