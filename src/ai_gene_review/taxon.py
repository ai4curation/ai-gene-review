"""NCBITaxon helpers for the ``taxon`` slot of gene and prediction reviews.

The ``taxon`` slot is bound to the ``NCBITaxonEnum`` dynamic enum, so term
validation requires a real ``NCBITaxon:<digits>`` id and its NCBITaxon label,
verbatim. These helpers produce or reuse such values and raise instead of
falling back to a placeholder (for example a UniProt species code).
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import yaml

NCBITAXON_CURIE = re.compile(r"NCBITaxon:\d+")
DEFAULT_ADAPTER = "ols:ncbitaxon"


def is_ncbitaxon_curie(value: object) -> bool:
    """Return True for a well-formed ``NCBITaxon:<digits>`` CURIE.

    >>> is_ncbitaxon_curie("NCBITaxon:3055")
    True
    >>> is_ncbitaxon_curie("NCBITaxon:DESVH")
    False
    >>> is_ncbitaxon_curie("uniprot:ARATH")
    False
    """
    return isinstance(value, str) and NCBITAXON_CURIE.fullmatch(value) is not None


@lru_cache(maxsize=None)
def ncbitaxon_label(curie: str, adapter_spec: str = DEFAULT_ADAPTER) -> str:
    """Return the NCBITaxon label for ``curie``.

    Raises:
        ValueError: if the CURIE is malformed or the taxon cannot be resolved.
    """
    if not is_ncbitaxon_curie(curie):
        raise ValueError(f"Not an NCBITaxon CURIE: {curie!r}")
    from oaklib import get_adapter

    label = get_adapter(adapter_spec).label(curie)
    if not label:
        raise ValueError(f"Could not resolve {curie} in NCBITaxon ({adapter_spec})")
    return label


def ncbitaxon_term(taxon_id: int | str, adapter_spec: str = DEFAULT_ADAPTER) -> dict[str, str]:
    """Build a ``{"id", "label"}`` taxon term from a numeric NCBI taxonomy id."""
    curie = f"NCBITaxon:{taxon_id}"
    return {"id": curie, "label": ncbitaxon_label(curie, adapter_spec)}


def review_taxon(review_file: Path) -> dict[str, str]:
    """Return the taxon term recorded in a gene review YAML.

    Prediction reviews reuse their gene review's taxon rather than deriving one
    from a UniProt species code.

    Raises:
        ValueError: if the review is missing or its taxon is not an NCBITaxon term.
    """
    if not review_file.exists():
        raise ValueError(f"No gene review to take the taxon from: {review_file}")
    data = yaml.safe_load(review_file.read_text()) or {}
    taxon = data.get("taxon") or {}
    curie, label = taxon.get("id"), taxon.get("label")
    if not isinstance(curie, str) or not is_ncbitaxon_curie(curie) or not isinstance(label, str) or not label:
        raise ValueError(f"{review_file} has no NCBITaxon taxon: {taxon!r}")
    return {"id": curie, "label": label}
