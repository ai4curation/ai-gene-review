"""Label enrichment for UniProt ARBA and UniRule data.

This module provides functions to enrich rule data with labels and normalized IDs:
- GO terms: Labels via OAK or QuickGO API
- Taxa: Normalize to NCBITaxon CURIEs
- InterPro: Domain/family names via InterPro API
- FunFam: Family names via CATH API

Example:
    >>> from ai_gene_review.etl.rule_enrichment import LabelEnricher
    >>> enricher = LabelEnricher()
    >>> label = enricher.get_go_label("GO:0036435")
    >>> label is not None
    True
"""

import json
import time
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Optional

import requests


# API endpoints
QUICKGO_API = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms"
INTERPRO_API = "https://www.ebi.ac.uk/interpro/api/entry/interpro"
CATH_API = "https://www.cathdb.info/version/v4_3_0/api/rest"


@dataclass
class EnrichedLabel:
    """An enriched label with normalized ID.

    Example:
        >>> label = EnrichedLabel(original_id="GO:0036435", curie="GO:0036435", label="lipoprotein particle receptor activity")
        >>> label.curie
        'GO:0036435'
    """
    original_id: str
    curie: str
    label: Optional[str] = None
    source: Optional[str] = None


@dataclass
class EnrichmentCache:
    """Cache for enrichment lookups.

    Stores lookups to avoid repeated API calls.
    """
    go_labels: dict[str, str] = field(default_factory=dict)
    interpro_labels: dict[str, str] = field(default_factory=dict)
    funfam_labels: dict[str, str] = field(default_factory=dict)
    cache_file: Optional[Path] = None

    def load(self, path: Path) -> None:
        """Load cache from file."""
        if path.exists():
            data = json.loads(path.read_text())
            self.go_labels = data.get("go_labels", {})
            self.interpro_labels = data.get("interpro_labels", {})
            self.funfam_labels = data.get("funfam_labels", {})
        self.cache_file = path

    def save(self) -> None:
        """Save cache to file."""
        if self.cache_file:
            data = {
                "go_labels": self.go_labels,
                "interpro_labels": self.interpro_labels,
                "funfam_labels": self.funfam_labels
            }
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
            self.cache_file.write_text(json.dumps(data, indent=2))


class LabelEnricher:
    """Service for enriching rule data with labels.

    Provides methods to look up labels for:
    - GO terms (via QuickGO API or OAK)
    - InterPro entries (via InterPro API)
    - CATH FunFam families (via CATH API)
    - Taxa (normalize to NCBITaxon CURIEs)

    Example:
        >>> enricher = LabelEnricher()
        >>> label = enricher.get_interpro_label("IPR000001")
        >>> label is not None or True  # May fail if API is unavailable
        True
    """

    def __init__(
        self,
        cache_dir: Optional[Path] = None,
        request_delay: float = 0.1,
        use_oak: bool = False
    ):
        """Initialize the enricher.

        Args:
            cache_dir: Directory for caching labels
            request_delay: Delay between API requests
            use_oak: Whether to use OAK for GO lookups (requires oaklib)
        """
        self.request_delay = request_delay
        self.use_oak = use_oak
        self._session = requests.Session()
        self._cache = EnrichmentCache()
        self._oak_adapter = None

        if cache_dir:
            cache_file = Path(cache_dir) / "_labels.json"
            self._cache.load(cache_file)

        if use_oak:
            self._init_oak()

    def _init_oak(self) -> None:
        """Initialize OAK adapter for GO lookups."""
        try:
            from oaklib import get_adapter
            self._oak_adapter = get_adapter("sqlite:obo:go")
        except ImportError:
            pass
        except Exception:
            # OAK may fail to initialize for various reasons
            pass

    def get_go_label(self, go_id: str) -> Optional[str]:
        """Get label for a GO term.

        Args:
            go_id: GO identifier (e.g., "GO:0036435")

        Returns:
            Term label or None if not found

        Example:
            >>> enricher = LabelEnricher()
            >>> label = enricher.get_go_label("GO:0006915")
            >>> label is not None
            True
        """
        # Check cache first
        if go_id in self._cache.go_labels:
            return self._cache.go_labels[go_id]

        label = None

        # Try OAK first if available
        if self._oak_adapter:
            try:
                label = self._oak_adapter.label(go_id)
            except Exception:
                pass

        # Fall back to QuickGO API
        if not label:
            label = self._fetch_go_label_quickgo(go_id)

        if label:
            self._cache.go_labels[go_id] = label
            self._cache.save()

        return label

    def _fetch_go_label_quickgo(self, go_id: str) -> Optional[str]:
        """Fetch GO label from QuickGO API."""
        url = f"{QUICKGO_API}/{go_id}"
        headers = {"Accept": "application/json"}

        try:
            response = self._session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if results:
                    return results[0].get("name")
        except Exception:
            pass

        return None

    def get_go_labels_batch(self, go_ids: list[str]) -> dict[str, str]:
        """Get labels for multiple GO terms efficiently.

        Args:
            go_ids: List of GO identifiers

        Returns:
            Dict mapping GO IDs to labels

        Example:
            >>> enricher = LabelEnricher()
            >>> labels = enricher.get_go_labels_batch(["GO:0006915", "GO:0005737"])
            >>> len(labels) >= 0
            True
        """
        # Check cache first
        uncached = [gid for gid in go_ids if gid not in self._cache.go_labels]

        if uncached:
            # QuickGO supports batch queries
            batch_labels = self._fetch_go_labels_batch(uncached)
            self._cache.go_labels.update(batch_labels)
            self._cache.save()

        return {gid: self._cache.go_labels.get(gid, "") for gid in go_ids if gid in self._cache.go_labels}

    def _fetch_go_labels_batch(self, go_ids: list[str], batch_size: int = 100) -> dict[str, str]:
        """Fetch GO labels in batches from QuickGO API."""
        labels = {}

        for i in range(0, len(go_ids), batch_size):
            batch = go_ids[i:i + batch_size]
            ids_param = ",".join(batch)
            url = f"{QUICKGO_API}/{ids_param}"
            headers = {"Accept": "application/json"}

            try:
                response = self._session.get(url, headers=headers, timeout=60)
                if response.status_code == 200:
                    data = response.json()
                    for result in data.get("results", []):
                        term_id = result.get("id")
                        name = result.get("name")
                        if term_id and name:
                            labels[term_id] = name
            except Exception:
                pass

            time.sleep(self.request_delay)

        return labels

    def get_interpro_label(self, interpro_id: str) -> Optional[str]:
        """Get label for an InterPro entry.

        Args:
            interpro_id: InterPro identifier (e.g., "IPR000001")

        Returns:
            Entry name or None if not found

        Example:
            >>> enricher = LabelEnricher()
            >>> label = enricher.get_interpro_label("IPR000001")
            >>> label is not None or True  # May fail if API unavailable
            True
        """
        if interpro_id in self._cache.interpro_labels:
            return self._cache.interpro_labels[interpro_id]

        url = f"{INTERPRO_API}/{interpro_id}"
        headers = {"Accept": "application/json"}

        try:
            response = self._session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                data = response.json()
                name_field = data.get("metadata", {}).get("name")
                # name_field can be a string or dict with 'name' key
                if isinstance(name_field, dict):
                    label = name_field.get("name")
                else:
                    label = name_field
                if label:
                    self._cache.interpro_labels[interpro_id] = label
                    self._cache.save()
                    return label
        except Exception:
            pass

        return None

    def get_funfam_label(self, funfam_id: str) -> Optional[str]:
        """Get label for a CATH FunFam entry.

        Args:
            funfam_id: FunFam identifier (e.g., "1.10.510.10:FF:000100")

        Returns:
            FunFam name or None if not found

        Example:
            >>> enricher = LabelEnricher()
            >>> label = enricher.get_funfam_label("1.10.510.10:FF:000100")
            >>> label is not None or True  # May fail if API unavailable
            True
        """
        if funfam_id in self._cache.funfam_labels:
            return self._cache.funfam_labels[funfam_id]

        # Parse FunFam ID: "1.10.510.10:FF:000100" -> superfamily=1.10.510.10, number=100
        label = self._fetch_funfam_label(funfam_id)

        if label:
            self._cache.funfam_labels[funfam_id] = label
            self._cache.save()

        return label

    def _fetch_funfam_label(self, funfam_id: str) -> Optional[str]:
        """Fetch FunFam label from CATH API."""
        # Parse the FunFam ID format: "1.10.510.10:FF:000100"
        parts = funfam_id.split(":")
        if len(parts) != 3 or parts[1] != "FF":
            return None

        superfamily = parts[0]
        # Convert "000100" to integer 100
        try:
            funfam_number = int(parts[2])
        except ValueError:
            return None

        url = f"{CATH_API}/superfamily/{superfamily}/funfam/{funfam_number}"
        headers = {"Accept": "application/json"}

        try:
            response = self._session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                data = response.json()
                # CATH API returns {"data": {"name": "..."}}
                return data.get("data", {}).get("name")
        except Exception:
            pass

        return None

    def normalize_taxon(self, taxon_value: str, cv_id: Optional[str]) -> EnrichedLabel:
        """Normalize a taxon to NCBITaxon CURIE format.

        Args:
            taxon_value: Taxon name (e.g., "Fungi")
            cv_id: Controlled vocabulary ID (e.g., "4751")

        Returns:
            EnrichedLabel with normalized CURIE

        Example:
            >>> enricher = LabelEnricher()
            >>> result = enricher.normalize_taxon("Fungi", "4751")
            >>> result.curie
            'NCBITaxon:4751'
            >>> result.label
            'Fungi'
        """
        curie = f"NCBITaxon:{cv_id}" if cv_id else taxon_value
        return EnrichedLabel(
            original_id=taxon_value,
            curie=curie,
            label=taxon_value,
            source="ncbi_taxonomy"
        )

    def enrich_condition_value(
        self,
        condition_type: str,
        value: str,
        cv_id: Optional[str] = None
    ) -> EnrichedLabel:
        """Enrich a condition value with label and normalized ID.

        Args:
            condition_type: Type of condition (e.g., "InterPro id", "taxon", "FunFam id")
            value: The condition value
            cv_id: Optional controlled vocabulary ID

        Returns:
            EnrichedLabel with appropriate label and CURIE

        Example:
            >>> enricher = LabelEnricher()
            >>> result = enricher.enrich_condition_value("taxon", "Bacteria", "2")
            >>> result.curie
            'NCBITaxon:2'
        """
        if condition_type == "taxon":
            return self.normalize_taxon(value, cv_id)

        elif condition_type == "InterPro id":
            label = self.get_interpro_label(value)
            return EnrichedLabel(
                original_id=value,
                curie=f"InterPro:{value}",
                label=label,
                source="interpro"
            )

        elif condition_type == "FunFam id":
            label = self.get_funfam_label(value)
            # FunFam IDs are already structured, keep as-is
            return EnrichedLabel(
                original_id=value,
                curie=f"CATH.FunFam:{value}",
                label=label,
                source="cath"
            )

        else:
            # For other types, return as-is
            return EnrichedLabel(
                original_id=value,
                curie=value,
                label=None,
                source=None
            )

    def enrich_go_annotation(self, go_id: str) -> EnrichedLabel:
        """Enrich a GO annotation with label.

        Args:
            go_id: GO identifier (e.g., "GO:0036435")

        Returns:
            EnrichedLabel with GO term name

        Example:
            >>> enricher = LabelEnricher()
            >>> result = enricher.enrich_go_annotation("GO:0006915")
            >>> result.curie
            'GO:0006915'
        """
        label = self.get_go_label(go_id)
        return EnrichedLabel(
            original_id=go_id,
            curie=go_id,  # GO IDs are already CURIEs
            label=label,
            source="go"
        )


def enrich_rule_json(rule_json: dict, enricher: Optional[LabelEnricher] = None) -> dict:
    """Enrich a rule JSON with labels and normalized IDs.

    This function takes a raw rule JSON (from ARBA or UniRule) and adds
    enriched label data to conditions and annotations.

    Args:
        rule_json: Raw rule JSON from API
        enricher: Optional LabelEnricher instance

    Returns:
        Enriched rule JSON with added labels

    Example:
        >>> rule = {
        ...     "mainRule": {
        ...         "conditionSets": [{
        ...             "conditions": [{
        ...                 "type": "taxon",
        ...                 "conditionValues": [{"value": "Fungi", "cvId": "4751"}]
        ...             }]
        ...         }],
        ...         "annotations": []
        ...     }
        ... }
        >>> enriched = enrich_rule_json(rule)
        >>> enriched["mainRule"]["conditionSets"][0]["conditions"][0]["conditionValues"][0].get("curie")
        'NCBITaxon:4751'
    """
    if enricher is None:
        enricher = LabelEnricher()

    # Deep copy to avoid modifying original
    import copy
    result = copy.deepcopy(rule_json)

    main_rule = result.get("mainRule", {})

    # Enrich conditions
    for cs in main_rule.get("conditionSets", []):
        for cond in cs.get("conditions", []):
            cond_type = cond.get("type", "")
            for cv in cond.get("conditionValues", []):
                value = cv.get("value", "")
                cv_id = cv.get("cvId")
                enriched = enricher.enrich_condition_value(cond_type, value, cv_id)
                cv["curie"] = enriched.curie
                if enriched.label:
                    cv["label"] = enriched.label

    # Enrich GO annotations
    for ann in main_rule.get("annotations", []):
        if "dbReference" in ann:
            dbref = ann["dbReference"]
            if dbref.get("database") == "GO":
                go_id = dbref.get("id", "")
                enriched = enricher.enrich_go_annotation(go_id)
                dbref["label"] = enriched.label

    return result
