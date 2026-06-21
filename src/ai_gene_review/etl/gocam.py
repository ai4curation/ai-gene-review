"""ETL for fetching and caching GO-CAM (Gene Ontology Causal Activity Model) data.

GO-CAMs are curated causal activity models. There are ~2,000 "production"
(reviewed, published) models, enumerated by the canonical index at
:data:`PRODUCTION_INDEX_URL`. Each model is fetched as low-level Minerva JSON,
translated into the clean ``gocam-py`` :class:`~gocam.datamodel.Model`
(activity-centric / annoton view), and cached as YAML under::

    gocams/<model_id>/<model_id>-src.yaml

The per-model folder leaves room for reviewer-authored companion files such as
``<model_id>-review.yaml`` and ``<model_id>-notes.md`` (mirroring the gene and
reactome caching conventions). ``-src.yaml`` is the canonical fetched artifact
and should not be hand-edited.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Optional

import csv
import requests
import yaml

from gocam.datamodel import Model
from gocam.translation.minerva_wrapper import MinervaWrapper

#: Canonical list of production (reviewed) GO-CAM models (~2k entries).
PRODUCTION_INDEX_URL = "https://go-public.s3.amazonaws.com/files/gocam-models.json"

#: Per-model low-level Minerva JSON product.
LOW_LEVEL_URL_TEMPLATE = (
    "https://live-go-cam.geneontology.io/product/json/low-level/{model_id}.json"
)

#: Default top-level cache directory.
DEFAULT_CACHE_DIR = Path("gocams")

#: Columns of the generated gene/activity index TSV.
INDEX_COLUMNS = [
    "gene_product",
    "gene_label",
    "model_id",
    "model_title",
    "taxon",
    "activity_id",
    "molecular_function",
    "mf_label",
    "biological_process",
    "bp_label",
    "cellular_component",
    "cc_label",
]


def normalize_gocam_id(value: str) -> str:
    """Return the bare local GO-CAM model id, stripping prefixes and URLs.

    Examples:
        >>> normalize_gocam_id('gomodel:568b0f9600000284')
        '568b0f9600000284'
        >>> normalize_gocam_id('http://model.geneontology.org/568b0f9600000284')
        '568b0f9600000284'
        >>> normalize_gocam_id('568b0f9600000284')
        '568b0f9600000284'
        >>> normalize_gocam_id('GO_CAM:gomodel:568b0f9600000284')
        '568b0f9600000284'
        >>> normalize_gocam_id(' 568b0f9600000284 ')
        '568b0f9600000284'
    """
    text = str(value).strip().rstrip("/")
    # URL form: take the last path segment.
    text = text.split("/")[-1]
    # CURIE/prefixed form: take the segment after the last colon.
    if ":" in text:
        text = text.split(":")[-1]
    return text


@dataclass
class GoCamActivityRow:
    """One row of the GO-CAM gene/activity index (a single annoton).

    Each production GO-CAM activity ("annoton") couples a gene product
    (``enabled_by``) to a molecular function and, optionally, a biological
    process (``part_of``) and cellular component (``occurs_in``).
    """

    gene_product: Optional[str]
    gene_label: Optional[str]
    model_id: str
    model_title: Optional[str]
    taxon: Optional[str]
    activity_id: str
    molecular_function: Optional[str]
    mf_label: Optional[str]
    biological_process: Optional[str]
    bp_label: Optional[str]
    cellular_component: Optional[str]
    cc_label: Optional[str]

    def as_index_row(self) -> list[Optional[str]]:
        """Return the values ordered to match :data:`INDEX_COLUMNS`."""
        return [
            self.gene_product,
            self.gene_label,
            self.model_id,
            self.model_title,
            self.taxon,
            self.activity_id,
            self.molecular_function,
            self.mf_label,
            self.biological_process,
            self.bp_label,
            self.cellular_component,
            self.cc_label,
        ]


def model_dir(model_id: str, cache_dir: Path = DEFAULT_CACHE_DIR) -> Path:
    """Return the per-model cache directory for a model id."""
    return Path(cache_dir) / normalize_gocam_id(model_id)


def src_path(model_id: str, cache_dir: Path = DEFAULT_CACHE_DIR) -> Path:
    """Return the canonical ``-src.yaml`` path for a model id.

    Examples:
        >>> src_path('gomodel:568b0f9600000284', cache_dir=Path('gocams')).as_posix()
        'gocams/568b0f9600000284/568b0f9600000284-src.yaml'
    """
    mid = normalize_gocam_id(model_id)
    return model_dir(mid, cache_dir) / f"{mid}-src.yaml"


def list_production_models(
    index_url: str = PRODUCTION_INDEX_URL,
    session: Optional[requests.Session] = None,
) -> list[dict]:
    """Fetch the canonical list of production GO-CAM models.

    Returns:
        A list of dicts with keys ``id`` (bare local id), ``title``, ``date``,
        and ``groups`` (list of group names).
    """
    getter = session.get if session is not None else requests.get
    response = getter(index_url, timeout=60)
    response.raise_for_status()
    entries = response.json()
    models = []
    for entry in entries:
        models.append(
            {
                "id": normalize_gocam_id(entry.get("gocam", "")),
                "title": entry.get("title"),
                "date": entry.get("date"),
                "groups": entry.get("groupnames") or [],
            }
        )
    return models


def fetch_minerva_json(
    model_id: str, session: Optional[requests.Session] = None
) -> dict:
    """Fetch the low-level Minerva JSON for a single model."""
    mid = normalize_gocam_id(model_id)
    url = LOW_LEVEL_URL_TEMPLATE.format(model_id=mid)
    getter = session.get if session is not None else requests.get
    response = getter(url, timeout=60)
    response.raise_for_status()
    return response.json()


def minerva_json_to_model(raw: dict) -> Model:
    """Translate low-level Minerva JSON into a ``gocam-py`` :class:`Model`."""
    return MinervaWrapper().minerva_object_to_model(raw)


def model_to_yaml(model: Model) -> str:
    """Serialize a :class:`Model` to canonical YAML (omitting null fields)."""
    return yaml.dump(
        model.model_dump(exclude_none=True, mode="json"),
        sort_keys=False,
        allow_unicode=True,
    )


def load_cached_model(
    model_id: str, cache_dir: Path = DEFAULT_CACHE_DIR
) -> Optional[Model]:
    """Load a cached ``-src.yaml`` back into a :class:`Model`, or None if absent."""
    path = src_path(model_id, cache_dir)
    if not path.exists():
        return None
    data = yaml.safe_load(path.read_text())
    return Model(**data)


def cache_gocam_model(
    model_id: str,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    force: bool = False,
    session: Optional[requests.Session] = None,
) -> Path:
    """Fetch, translate, and cache a single GO-CAM model as ``-src.yaml``.

    Args:
        model_id: GO-CAM model id (bare, ``gomodel:`` CURIE, or model URL).
        cache_dir: Top-level cache directory (default ``gocams/``).
        force: Re-fetch even if the cache file already exists.
        session: Optional requests session for connection reuse.

    Returns:
        Path to the written (or already-cached) ``-src.yaml`` file.
    """
    mid = normalize_gocam_id(model_id)
    out = src_path(mid, cache_dir)
    if out.exists() and not force:
        return out
    raw = fetch_minerva_json(mid, session=session)
    model = minerva_json_to_model(raw)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(model_to_yaml(model))
    return out


def cache_all_production_models(
    cache_dir: Path = DEFAULT_CACHE_DIR,
    force: bool = False,
    limit: Optional[int] = None,
    progress: Optional[Callable[[int, int, int, int], None]] = None,
    session: Optional[requests.Session] = None,
) -> dict:
    """Cache every production GO-CAM model.

    Args:
        cache_dir: Top-level cache directory.
        force: Re-fetch models already cached.
        limit: Only process the first ``limit`` models (for testing).
        progress: Optional callback ``(done, total, ok, failed)``.
        session: Optional requests session (one is created if omitted).

    Returns:
        Summary dict with ``total``, ``ok``, ``failed``, and ``failures``
        (a list of ``(model_id, error)`` tuples).
    """
    sess = session or requests.Session()
    models = list_production_models(session=sess)
    if limit is not None:
        models = models[:limit]
    total = len(models)
    ok = 0
    failed = 0
    failures: list[tuple[str, str]] = []
    for index, entry in enumerate(models):
        mid = entry["id"]
        try:
            cache_gocam_model(mid, cache_dir=cache_dir, force=force, session=sess)
            ok += 1
        except Exception as exc:  # external systems: don't abort the whole batch
            failed += 1
            failures.append((mid, str(exc)))
        if progress is not None:
            progress(index + 1, total, ok, failed)
    return {"total": total, "ok": ok, "failed": failed, "failures": failures}


def _clean_field(value: Optional[str]) -> str:
    """Collapse internal whitespace so a field stays on one TSV line.

    Examples:
        >>> _clean_field(None)
        ''
        >>> _clean_field('a\\tb\\nc  d')
        'a b c d'
    """
    if value is None:
        return ""
    return " ".join(str(value).split())


def iter_activity_rows(model: Model) -> Iterator[GoCamActivityRow]:
    """Yield one :class:`GoCamActivityRow` per activity (annoton) in a model."""
    objects = {obj.id: obj for obj in (model.objects or [])}

    def label(term: Optional[str]) -> Optional[str]:
        obj = objects.get(term) if term else None
        return obj.label if obj is not None else None

    mid = normalize_gocam_id(model.id)
    taxon = getattr(model, "taxon", None)
    title = getattr(model, "title", None)
    for activity in model.activities or []:
        enabled_by = activity.enabled_by.term if activity.enabled_by else None
        mf = activity.molecular_function.term if activity.molecular_function else None
        bp = activity.part_of.term if activity.part_of else None
        cc = activity.occurs_in.term if activity.occurs_in else None
        yield GoCamActivityRow(
            gene_product=enabled_by,
            gene_label=label(enabled_by),
            model_id=mid,
            model_title=title,
            taxon=taxon,
            activity_id=activity.id,
            molecular_function=mf,
            mf_label=label(mf),
            biological_process=bp,
            bp_label=label(bp),
            cellular_component=cc,
            cc_label=label(cc),
        )


def build_gene_index(
    cache_dir: Path = DEFAULT_CACHE_DIR,
    output: Optional[Path] = None,
) -> Path:
    """Build a TSV mapping gene products to GO-CAM activities across the cache.

    Scans every ``<model>/<model>-src.yaml`` under ``cache_dir`` and writes one
    row per activity (annoton) to ``cache_dir/index.tsv`` (or ``output``). This
    is the join key used to relate GO-CAM annotons to gene reviews and modules.

    Returns:
        Path to the written TSV.
    """
    cache_dir = Path(cache_dir)
    out = Path(output) if output is not None else cache_dir / "index.tsv"
    rows: list[GoCamActivityRow] = []
    for src in sorted(cache_dir.glob("*/*-src.yaml")):
        model = Model(**yaml.safe_load(src.read_text()))
        rows.extend(iter_activity_rows(model))
    # Deterministic global ordering so regenerating the index produces a stable
    # byte-for-byte file (no diff churn) regardless of filesystem traversal or
    # upstream activity ordering. activity_id is unique, making the key total.
    # Field values are whitespace-collapsed so every activity is exactly one
    # physical line (titles can contain embedded newlines/tabs), keeping the TSV
    # safe for line-based tooling (grep/awk/cut) and avoiding quoting churn.
    table = sorted(
        ([_clean_field(v) for v in row.as_index_row()] for row in rows),
        key=lambda values: (values[2], values[5], values[0]),  # model, activity, gene
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as handle:
        # Force LF line endings (csv defaults to CRLF) to avoid cross-platform churn.
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(INDEX_COLUMNS)
        writer.writerows(table)
    return out
