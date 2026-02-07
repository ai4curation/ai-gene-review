"""ETL for fetching and caching UniProt UniRule rules.

UniRules are expert-curated annotation rules that provide high-quality
automatic annotations based on protein signatures (InterPro, Pfam, etc.).

API Documentation:
    https://www.uniprot.org/help/unirule
    https://rest.uniprot.org/unirule/

Example:
    >>> from ai_gene_review.etl.unirule import UniRuleClient
    >>> client = UniRuleClient()  # doctest: +SKIP
    >>> # Fetch a single rule
    >>> rule = client.fetch_rule("UR000000070") # doctest: +SKIP
    >>> rule.uni_rule_id  # doctest: +SKIP
    'UR000000070'
"""

import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Optional

import requests

# Reuse data classes from ARBA module
from ai_gene_review.etl.arba import (
    Annotation,
    Condition,
    ConditionSet,
    ConditionValue,
    Statistics,
    _parse_annotation,
    _annotation_to_json,
)


UNIRULE_BASE_URL = "https://rest.uniprot.org/unirule"
DEFAULT_CACHE_DIR = Path("rules/unirule")


@dataclass
class UniRuleInfo:
    """Additional information specific to UniRules.

    Example:
        >>> info = UniRuleInfo(version="0", old_rule_num="RU361164", data_class="Protein")
        >>> info.old_rule_num
        'RU361164'
    """
    version: str
    old_rule_num: Optional[str] = None
    data_class: Optional[str] = None


@dataclass
class UniRule:
    """A UniRule (expert-curated annotation rule).

    UniRules provide high-quality automatic annotations based on
    protein signatures like InterPro, Pfam, PRINTS, etc.

    Example:
        >>> rule = UniRule(
        ...     uni_rule_id="UR000000070",
        ...     info=UniRuleInfo(version="0"),
        ...     condition_sets=[],
        ...     annotations=[],
        ...     statistics=Statistics(),
        ...     created_date="2020-05-12",
        ...     modified_date="2025-03-21"
        ... )
        >>> rule.uni_rule_id
        'UR000000070'
    """
    uni_rule_id: str
    info: UniRuleInfo
    condition_sets: list[ConditionSet]
    annotations: list[Annotation]
    statistics: Statistics
    created_date: str
    modified_date: str

    @classmethod
    def from_json(cls, data: dict) -> "UniRule":
        """Parse a UniRule from JSON API response."""
        # Parse information
        info_data = data.get("information", {})
        info = UniRuleInfo(
            version=info_data.get("version", "0"),
            old_rule_num=info_data.get("oldRuleNum"),
            data_class=info_data.get("dataClass")
        )

        # Parse condition sets (same as ARBA)
        condition_sets = []
        main_rule = data.get("mainRule", {})
        for cs_data in main_rule.get("conditionSets", []):
            conditions = []
            for cond_data in cs_data.get("conditions", []):
                values = [
                    ConditionValue(
                        value=cv.get("value", ""),
                        cv_id=cv.get("cvId")
                    )
                    for cv in cond_data.get("conditionValues", [])
                ]
                conditions.append(Condition(
                    condition_type=cond_data.get("type", ""),
                    values=values,
                    is_negative=cond_data.get("isNegative", False)
                ))
            condition_sets.append(ConditionSet(conditions=conditions))

        # Parse annotations (same as ARBA)
        annotations = []
        for ann_data in main_rule.get("annotations", []):
            annotation = _parse_annotation(ann_data)
            annotations.append(annotation)

        # Parse statistics
        stats_data = data.get("statistics", {})
        statistics = Statistics(
            reviewed_count=stats_data.get("reviewedProteinCount", 0),
            unreviewed_count=stats_data.get("unreviewedProteinCount", 0)
        )

        return cls(
            uni_rule_id=data.get("uniRuleId", ""),
            info=info,
            condition_sets=condition_sets,
            annotations=annotations,
            statistics=statistics,
            created_date=data.get("createdDate", ""),
            modified_date=data.get("modifiedDate", "")
        )

    def to_json(self) -> dict:
        """Serialize rule to JSON-compatible dict for caching."""
        info_dict: dict = {"version": self.info.version}
        if self.info.old_rule_num:
            info_dict["oldRuleNum"] = self.info.old_rule_num
        if self.info.data_class:
            info_dict["dataClass"] = self.info.data_class

        return {
            "uniRuleId": self.uni_rule_id,
            "information": info_dict,
            "mainRule": {
                "conditionSets": [
                    {
                        "conditions": [
                            {
                                "type": c.condition_type,
                                "conditionValues": [
                                    {"value": cv.value, "cvId": cv.cv_id} if cv.cv_id else {"value": cv.value}
                                    for cv in c.values
                                ],
                                "isNegative": c.is_negative
                            }
                            for c in cs.conditions
                        ]
                    }
                    for cs in self.condition_sets
                ],
                "annotations": [_annotation_to_json(a) for a in self.annotations]
            },
            "statistics": {
                "reviewedProteinCount": self.statistics.reviewed_count,
                "unreviewedProteinCount": self.statistics.unreviewed_count
            },
            "createdDate": self.created_date,
            "modifiedDate": self.modified_date
        }

    def get_go_ids(self) -> list[str]:
        """Extract all GO IDs from annotations."""
        go_ids = []
        for ann in self.annotations:
            if ann.db_reference and ann.db_reference.database == "GO":
                go_ids.append(ann.db_reference.ref_id)
        return go_ids

    def get_interpro_ids(self) -> list[str]:
        """Extract all InterPro IDs from conditions."""
        interpro_ids = []
        for cs in self.condition_sets:
            for cond in cs.conditions:
                if cond.condition_type == "InterPro id":
                    for cv in cond.values:
                        interpro_ids.append(cv.value)
        return interpro_ids

    def get_ec_numbers(self) -> list[str]:
        """Extract all EC numbers from annotations."""
        ec_numbers = []
        for ann in self.annotations:
            if ann.reaction and ann.reaction.ec_number:
                ec_numbers.append(ann.reaction.ec_number)
        return ec_numbers


class UniRuleClient:
    """Client for the UniProt UniRule REST API.

    Example:
        >>> client = UniRuleClient()  # doctest: +SKIP
        >>> count = client.get_total_count()  # doctest: +SKIP
        >>> count > 9000  # doctest: +SKIP
        True
    """

    def __init__(
        self,
        base_url: str = UNIRULE_BASE_URL,
        cache_dir: Path = DEFAULT_CACHE_DIR,
        request_delay: float = 0.1
    ):
        """Initialize the UniRule client."""
        self.base_url = base_url
        self.cache_dir = Path(cache_dir)
        self.request_delay = request_delay
        self._session = requests.Session()
        self._session.headers.update({"Accept": "application/json"})

    def get_total_count(self) -> int:
        """Get the total number of UniRules."""
        url = f"{self.base_url}/search"
        params: dict[str, str | int] = {"query": "*", "size": 1}
        response = self._session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return int(response.headers.get("X-Total-Results", 0))

    def fetch_rule(self, rule_id: str, use_cache: bool = True) -> Optional[UniRule]:
        """Fetch a single UniRule by ID."""
        # Check cache first
        if use_cache:
            cached = self._load_from_cache(rule_id)
            if cached:
                return cached

        # Fetch from API
        url = f"{self.base_url}/{rule_id}"
        response = self._session.get(url, timeout=30)

        if response.status_code == 404:
            return None
        response.raise_for_status()

        rule = UniRule.from_json(response.json())

        # Cache the result
        self._save_to_cache(rule)

        return rule

    def search(
        self,
        query: str = "*",
        size: int = 25,
        cursor: Optional[str] = None
    ) -> tuple[list[UniRule], Optional[str]]:
        """Search for UniRules."""
        url = f"{self.base_url}/search"
        params: dict[str, str | int] = {"query": query, "size": min(size, 500)}
        if cursor:
            params["cursor"] = cursor

        response = self._session.get(url, params=params, timeout=60)
        response.raise_for_status()

        data = response.json()
        rules = [UniRule.from_json(r) for r in data.get("results", [])]

        # Extract next cursor from Link header
        next_cursor = None
        link_header = response.headers.get("Link", "")
        if 'rel="next"' in link_header:
            match = re.search(r'cursor=([^&>]+)', link_header)
            if match:
                next_cursor = match.group(1)

        return rules, next_cursor

    def iter_all_rules(
        self,
        query: str = "*",
        batch_size: int = 500,
        cache: bool = True,
        go_only: bool = False,
        progress_callback: Optional[Callable[[int, int, int], None]] = None
    ) -> Iterator[UniRule]:
        """Iterate over all UniRules.

        Args:
            query: Search query
            batch_size: Number of rules per API request
            cache: Whether to cache rules as they are fetched
            go_only: Only yield rules that have GO annotations
            progress_callback: Optional callback(fetched_count, total_count, matched_count)
        """
        cursor = None
        total = self.get_total_count()
        fetched = 0
        matched = 0

        while True:
            rules, cursor = self.search(query=query, size=batch_size, cursor=cursor)

            for rule in rules:
                fetched += 1

                # Filter for GO annotations if requested
                if go_only and not rule.get_go_ids():
                    continue

                matched += 1
                if cache:
                    self._save_to_cache(rule)
                yield rule

            if progress_callback:
                progress_callback(fetched, total, matched)

            if not cursor:
                break

            time.sleep(self.request_delay)

    def _load_from_cache(self, rule_id: str) -> Optional[UniRule]:
        """Load a rule from cache."""
        cache_file = self.cache_dir / rule_id / f"{rule_id}.json"
        if cache_file.exists():
            data = json.loads(cache_file.read_text())
            return UniRule.from_json(data)
        return None

    def _save_to_cache(self, rule: UniRule) -> None:
        """Save a rule to cache."""
        rule_dir = self.cache_dir / rule.uni_rule_id
        rule_dir.mkdir(parents=True, exist_ok=True)
        cache_file = rule_dir / f"{rule.uni_rule_id}.json"
        cache_file.write_text(json.dumps(rule.to_json(), indent=2))

    def _write_metadata(self, stats: dict) -> None:
        """Write sync metadata."""
        import datetime
        metadata = {
            "last_sync": datetime.datetime.now().isoformat(),
            "stats": stats
        }
        meta_file = self.cache_dir / "_metadata.json"
        meta_file.write_text(json.dumps(metadata, indent=2))

    def get_cached_rules(self) -> Iterator[UniRule]:
        """Iterate over all cached rules."""
        if not self.cache_dir.exists():
            return

        for cache_file in sorted(self.cache_dir.glob("UR*/UR*.json")):
            data = json.loads(cache_file.read_text())
            yield UniRule.from_json(data)

    def get_cache_stats(self) -> dict:
        """Get statistics about the local cache."""
        if not self.cache_dir.exists():
            return {"cached_rules": 0, "cache_size_bytes": 0}

        rule_dirs = [d for d in self.cache_dir.iterdir() if d.is_dir() and d.name.startswith("UR")]
        total_size = sum(
            f.stat().st_size
            for d in rule_dirs
            for f in d.glob("*.json")
        )

        return {
            "cached_rules": len(rule_dirs),
            "cache_size_bytes": total_size,
            "cache_size_mb": round(total_size / (1024 * 1024), 2)
        }
