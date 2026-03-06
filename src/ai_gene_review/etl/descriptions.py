"""Gene descriptions ETL module.

Fetches gene descriptions from external sources (Alliance_Imported, Alliance_Automated, UniProt, NCBI/RefSeq)
and stores them as sidecar YAML files.

Storage mode:
- Per-gene: genes/<organism>/<gene>/<gene>-descriptions.yaml

Example:
    >>> from ai_gene_review.etl.descriptions import fetch_gene_descriptions
    >>> result = fetch_gene_descriptions("yeast", "CAT2")  # doctest: +SKIP
"""

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional, List, Dict, Any
import re
import logging
import time

import requests
import yaml

logger = logging.getLogger(__name__)

# Maps organism short names to Alliance species names and MOD prefixes
ORGANISM_CONFIG: Dict[str, Dict[str, str]] = {
    "yeast": {
        "alliance_species": "Saccharomyces cerevisiae",
        "mod": "SGD",
        "uniprot_xref": "SGD",
        "taxon_id": "NCBITaxon:559292",
    },
    "human": {
        "alliance_species": "Homo sapiens",
        "mod": "HGNC",
        "uniprot_xref": "HGNC",
        "taxon_id": "NCBITaxon:9606",
    },
    "mouse": {
        "alliance_species": "Mus musculus",
        "mod": "MGI",
        "uniprot_xref": "MGI",
        "taxon_id": "NCBITaxon:10090",
    },
    "rat": {
        "alliance_species": "Rattus norvegicus",
        "mod": "RGD",
        "uniprot_xref": "RGD",
        "taxon_id": "NCBITaxon:10116",
    },
    "fly": {
        "alliance_species": "Drosophila melanogaster",
        "mod": "FB",
        "uniprot_xref": "FlyBase",
        "taxon_id": "NCBITaxon:7227",
    },
    "worm": {
        "alliance_species": "Caenorhabditis elegans",
        "mod": "WB",
        "uniprot_xref": "WormBase",
        "taxon_id": "NCBITaxon:6239",
    },
    "zebrafish": {
        "alliance_species": "Danio rerio",
        "mod": "ZFIN",
        "uniprot_xref": "ZFIN",
        "taxon_id": "NCBITaxon:7955",
    },
    "frog": {
        "alliance_species": "Xenopus",
        "mod": "Xenbase",
        "uniprot_xref": "Xenbase",
        "taxon_id": "NCBITaxon:8364",
    },
}

# -------------------------------------------------------------------
# Data model
# -------------------------------------------------------------------


@dataclass
class DescriptionReviewRubric:
    """A scored review on a single rubric dimension.

    Examples:
        >>> r = DescriptionReviewRubric(rubric="correctness", score=4, notes="Accurate but missing transport detail")
        >>> r.rubric
        'correctness'
    """

    rubric: str
    score: Optional[int] = None  # 1-5 scale, None if not yet reviewed
    notes: Optional[str] = None


@dataclass
class DescriptionReview:
    """Review of a single source description.

    Examples:
        >>> dr = DescriptionReview(
        ...     reviewer="AI",
        ...     rubrics=[DescriptionReviewRubric(rubric="correctness", score=4)],
        ...     overall_notes="Good curated description",
        ... )
        >>> dr.reviewer
        'AI'
    """

    reviewer: Optional[str] = None
    rubrics: List[DescriptionReviewRubric] = field(default_factory=list)
    overall_notes: Optional[str] = None

    # Standard rubric names for convenience
    RUBRIC_NAMES = [
        "correctness",
        "utility",
        "compactness",
        "completeness",
        "specificity",
    ]


@dataclass
class SourceDescription:
    """A gene description from a single external source.

    Examples:
        >>> sd = SourceDescription(
        ...     source="Alliance_Imported",
        ...     source_type="curated",
        ...     text="Carnitine acetyl-CoA transferase",
        ...     url="https://www.alliancegenome.org/gene/SGD:S000004506",
        ... )
        >>> sd.source
        'Alliance_Imported'
    """

    source: str  # e.g. "Alliance_Imported", "Alliance_Automated", "UniProt", "RefSeq"
    text: str
    source_type: Optional[str] = None  # "curated", "automated", "computational"
    url: Optional[str] = None
    source_id: Optional[str] = None  # e.g. SGD:S000004506, HGNC:28188
    review: Optional[DescriptionReview] = None


@dataclass
class Finding:
    """A key finding or observation from comparing descriptions.

    Examples:
        >>> f = Finding(category="discrepancy", text="Alliance and UniProt differ on subcellular location")
        >>> f.category
        'discrepancy'
    """

    category: str  # "consensus", "discrepancy", "gap", "insight"
    text: str
    sources: Optional[List[str]] = None  # which sources support this finding


@dataclass
class GeneDescriptions:
    """Collection of gene descriptions from external sources, with findings and reviews.

    This is the top-level object serialized as the sidecar YAML file.

    Examples:
        >>> gd = GeneDescriptions(
        ...     gene_symbol="CAT2",
        ...     organism="yeast",
        ...     uniprot_id="P32796",
        ... )
        >>> gd.gene_symbol
        'CAT2'
    """

    gene_symbol: str
    organism: str
    uniprot_id: Optional[str] = None
    taxon_id: Optional[str] = None
    status: Optional[str] = None  # computed: STUB, IN_PROGRESS, REVIEWED, COMPLETE
    descriptions: List[SourceDescription] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
    review: Optional[DescriptionReview] = None  # overall review across all sources
    fetch_date: Optional[str] = None


# -------------------------------------------------------------------
# Status computation
# -------------------------------------------------------------------


def compute_description_status(gd: GeneDescriptions) -> str:
    """Compute the review status of a GeneDescriptions object.

    Status levels (analogous to gene review status):
    - STUB: No descriptions have reviews
    - IN_PROGRESS: Some but not all descriptions have reviews
    - REVIEWED: All descriptions have reviews, but no top-level review
    - COMPLETE: All descriptions reviewed AND top-level review present

    Args:
        gd: The gene descriptions object.

    Returns:
        Status string.

    Examples:
        >>> gd = GeneDescriptions(gene_symbol="X", organism="yeast")
        >>> compute_description_status(gd)
        'STUB'
        >>> gd.descriptions = [SourceDescription(source="UniProt", text="A function")]
        >>> compute_description_status(gd)
        'STUB'
        >>> gd.descriptions[0].review = DescriptionReview(reviewer="AI")
        >>> compute_description_status(gd)
        'REVIEWED'
        >>> gd.descriptions.append(SourceDescription(source="RefSeq", text="Another"))
        >>> compute_description_status(gd)
        'IN_PROGRESS'
        >>> gd.descriptions[1].review = DescriptionReview(reviewer="AI")
        >>> compute_description_status(gd)
        'REVIEWED'
        >>> gd.review = DescriptionReview(reviewer="AI", overall_notes="Good")
        >>> compute_description_status(gd)
        'COMPLETE'
    """
    if not gd.descriptions:
        return "STUB"

    reviewed_count = sum(1 for d in gd.descriptions if d.review is not None)
    total = len(gd.descriptions)

    if reviewed_count == 0:
        return "STUB"
    elif reviewed_count < total:
        return "IN_PROGRESS"
    elif gd.review is not None:
        return "COMPLETE"
    else:
        return "REVIEWED"


# -------------------------------------------------------------------
# YAML serialization helpers
# -------------------------------------------------------------------


def _clean_dict(d: Any) -> Any:
    """Remove None values and empty lists/dicts for cleaner YAML output.

    Examples:
        >>> _clean_dict({"a": 1, "b": None, "c": []})
        {'a': 1}
        >>> _clean_dict({"a": {"b": None, "c": 2}})
        {'a': {'c': 2}}
    """
    if isinstance(d, dict):
        return {k: _clean_dict(v) for k, v in d.items() if v is not None and v != [] and v != {}}
    if isinstance(d, list):
        return [_clean_dict(i) for i in d]
    return d


def gene_descriptions_to_yaml(gd: GeneDescriptions) -> str:
    """Serialize GeneDescriptions to YAML string.

    Examples:
        >>> gd = GeneDescriptions(gene_symbol="CAT2", organism="yeast", uniprot_id="P32796")
        >>> y = gene_descriptions_to_yaml(gd)
        >>> "gene_symbol: CAT2" in y
        True
    """
    return yaml.dump(_clean_dict(asdict(gd)), default_flow_style=False, sort_keys=False, allow_unicode=True)


def save_gene_descriptions(gd: GeneDescriptions, path: Path) -> Path:
    """Save GeneDescriptions to a YAML file.

    Args:
        gd: The gene descriptions object.
        path: Path to write the YAML file.

    Returns:
        The path written to.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(gene_descriptions_to_yaml(gd), encoding="utf-8")
    logger.info("Saved descriptions to %s", path)
    return path


def load_gene_descriptions(path: Path) -> GeneDescriptions:
    """Load GeneDescriptions from a YAML file.

    Args:
        path: Path to the YAML file.

    Returns:
        GeneDescriptions object.
    """
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    # Reconstruct nested dataclasses
    descriptions = []
    for d in data.get("descriptions", []):
        review = None
        if d.get("review"):
            rubrics = [DescriptionReviewRubric(**r) for r in d["review"].get("rubrics", [])]
            review = DescriptionReview(
                reviewer=d["review"].get("reviewer"),
                rubrics=rubrics,
                overall_notes=d["review"].get("overall_notes"),
            )
        descriptions.append(
            SourceDescription(
                source=d["source"],
                text=d["text"],
                source_type=d.get("source_type"),
                url=d.get("url"),
                source_id=d.get("source_id"),
                review=review,
            )
        )

    findings = [Finding(**f) for f in data.get("findings", [])]

    overall_review = None
    if data.get("review"):
        rubrics = [DescriptionReviewRubric(**r) for r in data["review"].get("rubrics", [])]
        overall_review = DescriptionReview(
            reviewer=data["review"].get("reviewer"),
            rubrics=rubrics,
            overall_notes=data["review"].get("overall_notes"),
        )

    return GeneDescriptions(
        gene_symbol=data["gene_symbol"],
        organism=data["organism"],
        uniprot_id=data.get("uniprot_id"),
        taxon_id=data.get("taxon_id"),
        status=data.get("status"),
        descriptions=descriptions,
        findings=findings,
        review=overall_review,
        fetch_date=data.get("fetch_date"),
    )


# -------------------------------------------------------------------
# UniProt parsing (from already-downloaded .txt files)
# -------------------------------------------------------------------


def extract_uniprot_function(uniprot_data: str) -> Optional[str]:
    """Extract the FUNCTION comment from UniProt text format.

    Args:
        uniprot_data: Raw UniProt flat-file text.

    Returns:
        The function description text, or None if not found.

    Examples:
        >>> data = '''CC   -!- FUNCTION: Carnitine acetylase is specific for short chain fatty acids.
        ... CC       Carnitine acetylase seems to affect the flux through the pyruvate
        ... CC       dehydrogenase complex. {ECO:0000269|PubMed:8420957}.
        ... CC   -!- CATALYTIC ACTIVITY:'''
        >>> extract_uniprot_function(data)
        'Carnitine acetylase is specific for short chain fatty acids. Carnitine acetylase seems to affect the flux through the pyruvate dehydrogenase complex.'
    """
    lines = uniprot_data.split("\n")
    in_function = False
    func_lines: List[str] = []

    for line in lines:
        if line.startswith("CC   -!- FUNCTION:"):
            in_function = True
            # Get the text after "FUNCTION:"
            text = line[len("CC   -!- FUNCTION:"):].strip()
            if text:
                func_lines.append(text)
        elif in_function:
            if line.startswith("CC   -!-") or not line.startswith("CC"):
                break
            text = line[len("CC"):].strip()
            if text:
                func_lines.append(text)

    if not func_lines:
        return None

    # Join and clean up evidence codes
    full_text = " ".join(func_lines)
    # Remove evidence codes like {ECO:0000269|PubMed:8420957}
    full_text = re.sub(r"\s*\{ECO:\d+\|[^}]*\}\s*", " ", full_text)
    # Remove trailing evidence codes at end of sentences
    full_text = re.sub(r"\s*\{ECO:\d+[^}]*\}", "", full_text)
    # Clean up whitespace
    full_text = re.sub(r"\s+", " ", full_text).strip()
    # Remove trailing period if doubled
    full_text = re.sub(r"\.\s*\.$", ".", full_text)
    return full_text if full_text else None


def extract_uniprot_xref(uniprot_data: str, db: str) -> Optional[str]:
    """Extract a cross-reference ID from UniProt DR lines.

    Args:
        uniprot_data: Raw UniProt flat-file text.
        db: Database name to look for (e.g. "SGD", "HGNC", "GeneID").

    Returns:
        The cross-reference ID, or None if not found.

    Examples:
        >>> data = '''DR   SGD; S000004506; CAT2.
        ... DR   GeneID; 854965; -.'''
        >>> extract_uniprot_xref(data, "SGD")
        'S000004506'
        >>> extract_uniprot_xref(data, "GeneID")
        '854965'
        >>> extract_uniprot_xref(data, "HGNC")
    """
    pattern = rf"^DR\s+{re.escape(db)};\s+([^;]+?);\s"
    match = re.search(pattern, uniprot_data, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def extract_uniprot_id(uniprot_data: str) -> Optional[str]:
    """Extract the primary UniProt accession from the AC line.

    Examples:
        >>> extract_uniprot_id("AC   P32796; D6VZD3;\\n")
        'P32796'
    """
    match = re.search(r"^AC\s+(\w+);", uniprot_data, re.MULTILINE)
    return match.group(1) if match else None


# -------------------------------------------------------------------
# API fetchers
# -------------------------------------------------------------------

ALLIANCE_API_BASE = "https://www.alliancegenome.org/api"
NCBI_ESUMMARY_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_alliance_description(mod_id: str) -> Dict[str, Any]:
    """Fetch gene data from the Alliance of Genome Resources API.

    Args:
        mod_id: Alliance gene ID, e.g. "SGD:S000004506" or "HGNC:11998".

    Returns:
        Dict with keys: curated_synopsis, automated_synopsis, name, url.
        Values are None if not available.

    Examples:
        >>> result = fetch_alliance_description("SGD:S000004506")  # doctest: +SKIP
        >>> "curated_synopsis" in result  # doctest: +SKIP
        True
    """
    url = f"{ALLIANCE_API_BASE}/gene/{mod_id}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    return {
        "curated_synopsis": data.get("geneSynopsis"),
        "automated_synopsis": data.get("automatedGeneSynopsis"),
        "name": data.get("name"),
        "symbol": data.get("symbol"),
        "url": data.get("modCrossRefCompleteUrl"),
    }


def fetch_ncbi_gene_summary(gene_id: str) -> Dict[str, Any]:
    """Fetch gene summary from NCBI Entrez Gene.

    Args:
        gene_id: NCBI Gene ID, e.g. "854965".

    Returns:
        Dict with keys: summary, description, nomenclature_name.

    Examples:
        >>> result = fetch_ncbi_gene_summary("854965")  # doctest: +SKIP
        >>> "summary" in result  # doctest: +SKIP
        True
    """
    resp = requests.get(
        NCBI_ESUMMARY_BASE,
        params={"db": "gene", "id": gene_id, "retmode": "json"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()

    gene_data = data.get("result", {}).get(gene_id, {})
    return {
        "summary": gene_data.get("summary") or None,
        "description": gene_data.get("description") or None,
        "nomenclature_name": gene_data.get("nomenclaturename") or None,
    }


# -------------------------------------------------------------------
# Main fetch orchestration
# -------------------------------------------------------------------


def fetch_gene_descriptions(
    organism: str,
    gene_symbol: str,
    base_path: Optional[Path] = None,
    uniprot_data: Optional[str] = None,
) -> GeneDescriptions:
    """Fetch gene descriptions from all available external sources.

    Reads the UniProt text file if available, then queries Alliance and NCBI APIs.

    Args:
        organism: Organism short name (e.g. "yeast", "human").
        gene_symbol: Gene symbol (e.g. "CAT2", "TP53").
        base_path: Base directory (default: cwd). Gene dir is at genes/<organism>/<gene>/.
        uniprot_data: Pre-loaded UniProt text data. If None, reads from the gene directory.

    Returns:
        GeneDescriptions object with all fetched descriptions.

    Examples:
        >>> gd = fetch_gene_descriptions("yeast", "CAT2")  # doctest: +SKIP
    """
    base = base_path or Path.cwd()
    gene_dir = base / "genes" / organism / gene_symbol
    config = ORGANISM_CONFIG.get(organism, {})

    from datetime import date

    gd = GeneDescriptions(
        gene_symbol=gene_symbol,
        organism=organism,
        taxon_id=config.get("taxon_id"),
        fetch_date=date.today().isoformat(),
    )

    # Load UniProt data if not provided
    if uniprot_data is None:
        uniprot_file = gene_dir / f"{gene_symbol}-uniprot.txt"
        if uniprot_file.exists():
            uniprot_data = uniprot_file.read_text(encoding="utf-8")

    # Extract UniProt info
    uniprot_id = None
    mod_xref = None
    ncbi_gene_id = None

    if uniprot_data:
        uniprot_id = extract_uniprot_id(uniprot_data)
        gd.uniprot_id = uniprot_id

        # UniProt FUNCTION description
        func_text = extract_uniprot_function(uniprot_data)
        if func_text:
            gd.descriptions.append(
                SourceDescription(
                    source="UniProt",
                    source_type="curated",
                    text=func_text,
                    url=f"https://www.uniprot.org/uniprot/{uniprot_id}" if uniprot_id else None,
                    source_id=uniprot_id,
                )
            )

        # Extract cross-references for other APIs
        xref_db = config.get("uniprot_xref")
        if xref_db:
            mod_xref = extract_uniprot_xref(uniprot_data, xref_db)
        ncbi_gene_id = extract_uniprot_xref(uniprot_data, "GeneID")

    # Fetch Alliance description
    if mod_xref and config.get("mod"):
        alliance_id = f"{config['mod']}:{mod_xref}"
        try:
            alliance_data = fetch_alliance_description(alliance_id)

            if alliance_data.get("curated_synopsis"):
                gd.descriptions.append(
                    SourceDescription(
                        source="Alliance_Imported",
                        source_type="curated",
                        text=alliance_data["curated_synopsis"],
                        url=alliance_data.get("url"),
                        source_id=alliance_id,
                    )
                )
            if alliance_data.get("automated_synopsis"):
                gd.descriptions.append(
                    SourceDescription(
                        source="Alliance_Automated",
                        source_type="automated",
                        text=alliance_data["automated_synopsis"],
                        url=alliance_data.get("url"),
                        source_id=alliance_id,
                    )
                )
        except requests.RequestException as e:
            logger.warning("Failed to fetch Alliance description for %s: %s", alliance_id, e)

    # Fetch NCBI Gene summary
    if ncbi_gene_id:
        try:
            ncbi_data = fetch_ncbi_gene_summary(ncbi_gene_id)
            if ncbi_data.get("summary"):
                gd.descriptions.append(
                    SourceDescription(
                        source="RefSeq",
                        source_type="automated",
                        text=ncbi_data["summary"],
                        url=f"https://www.ncbi.nlm.nih.gov/gene/{ncbi_gene_id}",
                        source_id=f"GeneID:{ncbi_gene_id}",
                    )
                )
        except requests.RequestException as e:
            logger.warning("Failed to fetch NCBI Gene summary for %s: %s", ncbi_gene_id, e)

    return gd


def fetch_and_save_gene_descriptions(
    organism: str,
    gene_symbol: str,
    base_path: Optional[Path] = None,
) -> Path:
    """Fetch descriptions and save to the per-gene sidecar file.

    Args:
        organism: Organism short name.
        gene_symbol: Gene symbol.
        base_path: Base directory (default: cwd).

    Returns:
        Path to the saved YAML file.
    """
    base = base_path or Path.cwd()
    gd = fetch_gene_descriptions(organism, gene_symbol, base_path=base)
    out_path = base / "genes" / organism / gene_symbol / f"{gene_symbol}-descriptions.yaml"
    return save_gene_descriptions(gd, out_path)


# -------------------------------------------------------------------
# Bulk fetch for an organism
# -------------------------------------------------------------------


def fetch_organism_descriptions(
    organism: str,
    base_path: Optional[Path] = None,
    delay: float = 0.5,
    gene_symbols: Optional[List[str]] = None,
) -> int:
    """Fetch descriptions for all genes in an organism directory.

    Iterates over genes/<organism>/*/ and fetches descriptions for each gene,
    saving individual per-gene sidecar files.

    Args:
        organism: Organism short name (e.g. "yeast").
        base_path: Base directory (default: cwd).
        delay: Delay between API calls in seconds (to be polite).
        gene_symbols: If provided, only fetch for these genes. Otherwise fetch all.

    Returns:
        Number of genes processed.
    """
    base = base_path or Path.cwd()
    organism_dir = base / "genes" / organism

    if not organism_dir.exists():
        raise FileNotFoundError(f"Organism directory not found: {organism_dir}")

    # Discover genes
    if gene_symbols:
        gene_dirs = [organism_dir / g for g in gene_symbols if (organism_dir / g).is_dir()]
    else:
        gene_dirs = sorted([d for d in organism_dir.iterdir() if d.is_dir()])

    count = 0

    for gene_dir in gene_dirs:
        gene_symbol = gene_dir.name
        logger.info("Fetching descriptions for %s/%s...", organism, gene_symbol)

        try:
            gd = fetch_gene_descriptions(organism, gene_symbol, base_path=base)

            # Save per-gene file
            per_gene_path = gene_dir / f"{gene_symbol}-descriptions.yaml"
            save_gene_descriptions(gd, per_gene_path)

            count += 1

            if delay > 0:
                time.sleep(delay)

        except Exception as e:
            logger.error("Failed to fetch descriptions for %s: %s", gene_symbol, e)
            continue

    logger.info("Fetched descriptions for %d %s genes", count, organism)

    return count


# -------------------------------------------------------------------
# Status reporting
# -------------------------------------------------------------------


@dataclass
class DescriptionStatusReport:
    """Status summary for description files in an organism directory.

    Examples:
        >>> r = DescriptionStatusReport(organism="yeast", total=10, by_status={"STUB": 8, "COMPLETE": 2}, genes=[])
        >>> r.total
        10
    """

    organism: str
    total: int
    by_status: Dict[str, int]
    genes: List[Dict[str, str]]  # [{gene_symbol, status, path}, ...]


def compute_organism_description_status(
    organism: str,
    base_path: Optional[Path] = None,
    update: bool = False,
) -> DescriptionStatusReport:
    """Compute description review status for all genes in an organism directory.

    Args:
        organism: Organism short name (e.g. "yeast").
        base_path: Base directory (default: cwd).
        update: If True, write the computed status back into each YAML file.

    Returns:
        DescriptionStatusReport with per-gene statuses and summary counts.
    """
    base = base_path or Path.cwd()
    organism_dir = base / "genes" / organism

    if not organism_dir.exists():
        raise FileNotFoundError(f"Organism directory not found: {organism_dir}")

    desc_files = sorted(organism_dir.glob("*/*-descriptions.yaml"))
    by_status: Dict[str, int] = {}
    genes: List[Dict[str, str]] = []

    for path in desc_files:
        gd = load_gene_descriptions(path)
        status = compute_description_status(gd)

        if update and gd.status != status:
            gd.status = status
            save_gene_descriptions(gd, path)

        by_status[status] = by_status.get(status, 0) + 1
        genes.append({
            "gene_symbol": gd.gene_symbol,
            "status": status,
            "path": str(path),
        })

    return DescriptionStatusReport(
        organism=organism,
        total=len(desc_files),
        by_status=by_status,
        genes=genes,
    )
