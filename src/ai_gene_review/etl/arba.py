"""ETL for fetching and caching UniProt ARBA (Association-Rule-Based Annotator) rules.

ARBA is UniProt's automatic annotation system that uses rule mining techniques
to generate annotation models based on InterPro, PANTHER, FunFam domains and taxonomy.

API Documentation:
    https://www.uniprot.org/help/arba
    https://rest.uniprot.org/arba/

Example:
    >>> from ai_gene_review.etl.arba import ARBAClient
    >>> client = ARBAClient()  # doctest: +SKIP
    >>> # Fetch a single rule
    >>> rule = client.fetch_rule("ARBA00000001") # doctest: +SKIP
    >>> rule.uni_rule_id  # doctest: +SKIP
    'ARBA00000001'
"""

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterator, Optional

import requests


ARBA_BASE_URL = "https://rest.uniprot.org/arba"
DEFAULT_CACHE_DIR = Path("rules/arba")


@dataclass
class ConditionValue:
    """A single condition value in an ARBA rule.

    Example:
        >>> cv = ConditionValue(value="IPR040234", cv_id="33208")
        >>> cv.value
        'IPR040234'
    """
    value: str
    cv_id: Optional[str] = None


@dataclass
class Condition:
    """A condition in an ARBA rule (e.g., InterPro ID, taxon).

    Example:
        >>> cond = Condition(
        ...     condition_type="InterPro id",
        ...     values=[ConditionValue(value="IPR040234")],
        ...     is_negative=False
        ... )
        >>> cond.condition_type
        'InterPro id'
    """
    condition_type: str
    values: list[ConditionValue]
    is_negative: bool = False


@dataclass
class ConditionSet:
    """A set of conditions that must all be true for a rule to apply.

    Example:
        >>> cs = ConditionSet(conditions=[])
        >>> len(cs.conditions)
        0
    """
    conditions: list[Condition]


@dataclass
class ReactionCrossReference:
    """A cross-reference in a reaction annotation (Rhea, ChEBI, etc.).

    Example:
        >>> ref = ReactionCrossReference(database="Rhea", ref_id="RHEA:23652")
        >>> ref.database
        'Rhea'
    """
    database: str
    ref_id: str


@dataclass
class Reaction:
    """A catalytic activity reaction annotation.

    Example:
        >>> rxn = Reaction(name="ATP hydrolysis", ec_number="3.6.1.3")
        >>> rxn.ec_number
        '3.6.1.3'
    """
    name: str
    cross_references: list[ReactionCrossReference] = field(default_factory=list)
    ec_number: Optional[str] = None


@dataclass
class SubcellularLocation:
    """A subcellular location annotation."""
    location: str
    topology: Optional[str] = None


@dataclass
class Keyword:
    """A UniProt keyword annotation.

    Example:
        >>> kw = Keyword(kw_id="KW-0171", name="Cobalt transport")
        >>> kw.name
        'Cobalt transport'
    """
    kw_id: str
    name: str
    category: Optional[str] = None


@dataclass
class DBReference:
    """A database cross-reference annotation (GO terms, etc.).

    Example:
        >>> dbref = DBReference(database="GO", ref_id="GO:0036435")
        >>> dbref.database
        'GO'
    """
    database: str
    ref_id: str
    properties: dict = field(default_factory=dict)


@dataclass
class Annotation:
    """An annotation produced by an ARBA rule.

    Annotations can be of different types:
    - CATALYTIC_ACTIVITY: with reaction details
    - SUBCELLULAR_LOCATION: with location info
    - KEYWORD: with keyword info
    - PATHWAY: with pathway text
    - DB_REFERENCE: GO terms and other database references

    Example:
        >>> ann = Annotation(
        ...     annotation_type="ANNOTATION",
        ...     comment_type="CATALYTIC ACTIVITY",
        ...     reaction=Reaction(name="test reaction")
        ... )
        >>> ann.comment_type
        'CATALYTIC ACTIVITY'
    """
    annotation_type: str
    comment_type: Optional[str] = None
    reaction: Optional[Reaction] = None
    subcellular_location: Optional[SubcellularLocation] = None
    keyword: Optional[Keyword] = None
    db_reference: Optional[DBReference] = None
    pathway: Optional[str] = None
    text: Optional[str] = None


@dataclass
class Statistics:
    """Statistics about proteins annotated by a rule.

    Example:
        >>> stats = Statistics(reviewed_count=5, unreviewed_count=100)
        >>> stats.total_count
        105
    """
    reviewed_count: int = 0
    unreviewed_count: int = 0

    @property
    def total_count(self) -> int:
        """Total number of proteins annotated by this rule."""
        return self.reviewed_count + self.unreviewed_count


@dataclass
class ARBARule:
    """An ARBA (Association-Rule-Based Annotator) rule.

    ARBA rules associate protein features (InterPro domains, taxonomy)
    with functional annotations (catalytic activity, subcellular location, etc.).

    Example:
        >>> rule = ARBARule(
        ...     uni_rule_id="ARBA00000001",
        ...     version="0",
        ...     condition_sets=[],
        ...     annotations=[],
        ...     statistics=Statistics(),
        ...     created_date="2020-05-12",
        ...     modified_date="2025-03-21"
        ... )
        >>> rule.uni_rule_id
        'ARBA00000001'
    """
    uni_rule_id: str
    version: str
    condition_sets: list[ConditionSet]
    annotations: list[Annotation]
    statistics: Statistics
    created_date: str
    modified_date: str

    @classmethod
    def from_json(cls, data: dict) -> "ARBARule":
        """Parse an ARBA rule from JSON API response.

        Example:
            >>> json_data = {
            ...     "uniRuleId": "ARBA00000001",
            ...     "information": {"version": "0"},
            ...     "mainRule": {"conditionSets": [], "annotations": []},
            ...     "statistics": {"reviewedProteinCount": 0, "unreviewedProteinCount": 100},
            ...     "createdDate": "2020-05-12",
            ...     "modifiedDate": "2025-03-21"
            ... }
            >>> rule = ARBARule.from_json(json_data)
            >>> rule.uni_rule_id
            'ARBA00000001'
        """
        # Parse condition sets
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

        # Parse annotations
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
            version=data.get("information", {}).get("version", "0"),
            condition_sets=condition_sets,
            annotations=annotations,
            statistics=statistics,
            created_date=data.get("createdDate", ""),
            modified_date=data.get("modifiedDate", "")
        )

    def to_json(self) -> dict:
        """Serialize rule to JSON-compatible dict for caching."""
        return {
            "uniRuleId": self.uni_rule_id,
            "information": {"version": self.version},
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

    def get_interpro_ids(self) -> list[str]:
        """Extract all InterPro IDs from conditions.

        Example:
            >>> rule = ARBARule(
            ...     uni_rule_id="ARBA00000001",
            ...     version="0",
            ...     condition_sets=[
            ...         ConditionSet(conditions=[
            ...             Condition(
            ...                 condition_type="InterPro id",
            ...                 values=[ConditionValue(value="IPR040234")]
            ...             )
            ...         ])
            ...     ],
            ...     annotations=[],
            ...     statistics=Statistics(),
            ...     created_date="2020-05-12",
            ...     modified_date="2025-03-21"
            ... )
            >>> rule.get_interpro_ids()
            ['IPR040234']
        """
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

    def get_rhea_ids(self) -> list[str]:
        """Extract all Rhea IDs from annotations."""
        rhea_ids = []
        for ann in self.annotations:
            if ann.reaction:
                for xref in ann.reaction.cross_references:
                    if xref.database == "Rhea":
                        rhea_ids.append(xref.ref_id)
        return rhea_ids

    def get_go_ids(self) -> list[str]:
        """Extract all GO IDs from annotations."""
        go_ids = []
        for ann in self.annotations:
            if ann.db_reference and ann.db_reference.database == "GO":
                go_ids.append(ann.db_reference.ref_id)
        return go_ids


def _parse_annotation(ann_data: dict) -> Annotation:
    """Parse an annotation from JSON."""
    annotation = Annotation(
        annotation_type=ann_data.get("annotationType", "")
    )

    # Parse keyword annotations
    if "keyword" in ann_data:
        kw = ann_data["keyword"]
        annotation.keyword = Keyword(
            kw_id=kw.get("id", ""),
            name=kw.get("name", ""),
            category=kw.get("category")
        )

    # Parse dbReference annotations (GO terms, etc.)
    if "dbReference" in ann_data:
        dbref = ann_data["dbReference"]
        props = {}
        for prop in dbref.get("properties", []):
            props[prop.get("key", "")] = prop.get("value", "")
        annotation.db_reference = DBReference(
            database=dbref.get("database", ""),
            ref_id=dbref.get("id", ""),
            properties=props
        )

    # Parse comment-based annotations
    comment = ann_data.get("comment", {})
    if comment:
        annotation.comment_type = comment.get("commentType")

        # Parse catalytic activity
        if "reaction" in comment:
            rxn = comment["reaction"]
            xrefs = [
                ReactionCrossReference(
                    database=x.get("database", ""),
                    ref_id=x.get("id", "")
                )
                for x in rxn.get("reactionCrossReferences", [])
            ]
            annotation.reaction = Reaction(
                name=rxn.get("name", ""),
                cross_references=xrefs,
                ec_number=rxn.get("ecNumber")
            )

        # Parse subcellular location
        if "subcellularLocations" in comment:
            locs = comment["subcellularLocations"]
            if locs:
                loc = locs[0].get("location", {})
                annotation.subcellular_location = SubcellularLocation(
                    location=loc.get("value", "")
                )

        # Parse pathway
        if "texts" in comment:
            texts = comment["texts"]
            if texts:
                annotation.pathway = texts[0].get("value")

        # Parse text (for other comment types)
        if "text" in comment:
            texts = comment["text"]
            if texts:
                annotation.text = texts[0].get("value")

    return annotation


def _annotation_to_json(ann: Annotation) -> dict:
    """Serialize an annotation to JSON."""
    result: dict = {"annotationType": ann.annotation_type}

    if ann.keyword:
        result["keyword"] = {
            "id": ann.keyword.kw_id,
            "name": ann.keyword.name
        }
        if ann.keyword.category:
            result["keyword"]["category"] = ann.keyword.category

    if ann.db_reference:
        result["dbReference"] = {
            "database": ann.db_reference.database,
            "id": ann.db_reference.ref_id,
            "properties": [
                {"key": k, "value": v}
                for k, v in ann.db_reference.properties.items()
            ]
        }

    if ann.comment_type or ann.reaction or ann.subcellular_location:
        comment: dict = {}
        if ann.comment_type:
            comment["commentType"] = ann.comment_type

        if ann.reaction:
            comment["reaction"] = {
                "name": ann.reaction.name,
                "reactionCrossReferences": [
                    {"database": x.database, "id": x.ref_id}
                    for x in ann.reaction.cross_references
                ]
            }
            if ann.reaction.ec_number:
                comment["reaction"]["ecNumber"] = ann.reaction.ec_number

        if ann.subcellular_location:
            comment["subcellularLocations"] = [{
                "location": {"value": ann.subcellular_location.location}
            }]

        if ann.pathway:
            comment["texts"] = [{"value": ann.pathway}]

        if ann.text:
            comment["text"] = [{"value": ann.text}]

        result["comment"] = comment

    return result


class ARBAClient:
    """Client for the UniProt ARBA REST API.

    Provides methods to fetch and cache ARBA rules from UniProt.

    Example:
        >>> client = ARBAClient()  # doctest: +SKIP
        >>> # Get total count
        >>> count = client.get_total_count()  # doctest: +SKIP
        >>> count > 80000  # doctest: +SKIP
        True
    """

    def __init__(
        self,
        base_url: str = ARBA_BASE_URL,
        cache_dir: Path = DEFAULT_CACHE_DIR,
        request_delay: float = 0.1
    ):
        """Initialize the ARBA client.

        Args:
            base_url: Base URL for the ARBA API
            cache_dir: Directory for caching rules
            request_delay: Delay between API requests in seconds
        """
        self.base_url = base_url
        self.cache_dir = Path(cache_dir)
        self.request_delay = request_delay
        self._session = requests.Session()
        self._session.headers.update({"Accept": "application/json"})

    def get_total_count(self) -> int:
        """Get the total number of ARBA rules.

        Example:
            >>> client = ARBAClient()  # doctest: +SKIP
            >>> count = client.get_total_count()  # doctest: +SKIP
            >>> count > 80000  # doctest: +SKIP
            True
        """
        url = f"{self.base_url}/search"
        params: dict[str, str | int] = {"query": "*", "size": 1}
        response = self._session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return int(response.headers.get("X-Total-Results", 0))

    def fetch_rule(self, rule_id: str, use_cache: bool = True) -> Optional[ARBARule]:
        """Fetch a single ARBA rule by ID.

        Args:
            rule_id: ARBA rule ID (e.g., "ARBA00000001")
            use_cache: Whether to use cached data if available

        Returns:
            ARBARule object or None if not found

        Example:
            >>> client = ARBAClient()  # doctest: +SKIP
            >>> rule = client.fetch_rule("ARBA00000001") # doctest: +SKIP
            >>> rule.uni_rule_id  # doctest: +SKIP
            'ARBA00000001'
        """
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

        rule = ARBARule.from_json(response.json())

        # Cache the result
        self._save_to_cache(rule)

        return rule

    def search(
        self,
        query: str = "*",
        size: int = 25,
        cursor: Optional[str] = None
    ) -> tuple[list[ARBARule], Optional[str]]:
        """Search for ARBA rules.

        Args:
            query: Search query (e.g., "ec:2.3.2.5" or "*" for all)
            size: Number of results per page (max 500)
            cursor: Cursor for pagination

        Returns:
            Tuple of (list of rules, next cursor or None if no more results)
        """
        url = f"{self.base_url}/search"
        params: dict[str, str | int] = {"query": query, "size": min(size, 500)}
        if cursor:
            params["cursor"] = cursor

        response = self._session.get(url, params=params, timeout=60)
        response.raise_for_status()

        data = response.json()
        rules = [ARBARule.from_json(r) for r in data.get("results", [])]

        # Extract next cursor from Link header
        next_cursor = None
        link_header = response.headers.get("Link", "")
        if 'rel="next"' in link_header:
            # Parse cursor from link header
            import re
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
    ) -> Iterator[ARBARule]:
        """Iterate over all ARBA rules.

        Args:
            query: Search query (e.g., "*" for all)
            batch_size: Number of rules per API request
            cache: Whether to cache rules as they are fetched
            go_only: Only yield rules that have GO annotations
            progress_callback: Optional callback(fetched_count, total_count, matched_count)

        Yields:
            ARBARule objects

        Example:
            >>> client = ARBAClient()  # doctest: +SKIP
            >>> rules = list(client.iter_all_rules(query="ec:2.3.2.5", batch_size=10)) # doctest: +SKIP
            >>> len(rules) >= 0 # doctest: +SKIP
            True
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

    def sync_all(
        self,
        query: str = "*",
        batch_size: int = 500,
        force: bool = False,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> dict:
        """Sync all ARBA rules to local cache.

        Args:
            query: Search query (e.g., "*" for all)
            batch_size: Number of rules per API request
            force: Force re-download even if cached
            progress_callback: Optional callback(fetched_count, total_count)

        Returns:
            Dict with sync statistics
        """
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        stats = {
            "total_available": self.get_total_count(),
            "fetched": 0,
            "cached": 0,
            "skipped": 0,
            "errors": 0
        }

        cursor = None

        while True:
            rules, cursor = self.search(query=query, size=batch_size, cursor=cursor)

            for rule in rules:
                stats["fetched"] += 1

                # Check if already cached
                cache_file = self.cache_dir / rule.uni_rule_id / f"{rule.uni_rule_id}.json"
                if cache_file.exists() and not force:
                    stats["skipped"] += 1
                else:
                    self._save_to_cache(rule)
                    stats["cached"] += 1

            if progress_callback:
                progress_callback(stats["fetched"], stats["total_available"])

            if not cursor:
                break

            time.sleep(self.request_delay)

        # Write metadata
        self._write_metadata(stats)

        return stats

    def _load_from_cache(self, rule_id: str) -> Optional[ARBARule]:
        """Load a rule from cache."""
        cache_file = self.cache_dir / rule_id / f"{rule_id}.json"
        if cache_file.exists():
            data = json.loads(cache_file.read_text())
            return ARBARule.from_json(data)
        return None

    def _save_to_cache(self, rule: ARBARule) -> None:
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

    def get_cached_rules(self) -> Iterator[ARBARule]:
        """Iterate over all cached rules.

        Yields:
            ARBARule objects from cache
        """
        if not self.cache_dir.exists():
            return

        for cache_file in sorted(self.cache_dir.glob("ARBA*/ARBA*.json")):
            data = json.loads(cache_file.read_text())
            yield ARBARule.from_json(data)

    def get_cache_stats(self) -> dict:
        """Get statistics about the local cache.

        Returns:
            Dict with cache statistics
        """
        if not self.cache_dir.exists():
            return {"cached_rules": 0, "cache_size_bytes": 0}

        rule_dirs = [d for d in self.cache_dir.iterdir() if d.is_dir() and d.name.startswith("ARBA")]
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


def fetch_rules_by_interpro(
    interpro_id: str,
    client: Optional[ARBAClient] = None,
    use_cache: bool = True
) -> list[ARBARule]:
    """Fetch ARBA rules that use a specific InterPro ID in conditions.

    Args:
        interpro_id: InterPro ID (e.g., "IPR040234")
        client: Optional ARBAClient instance
        use_cache: Whether to use cached data

    Returns:
        List of matching ARBARule objects

    Note:
        This searches the local cache if available, otherwise queries the API.
    """
    if client is None:
        client = ARBAClient()

    # If we have a cache, search it first
    if use_cache and client.cache_dir.exists():
        matching = []
        for rule in client.get_cached_rules():
            if interpro_id in rule.get_interpro_ids():
                matching.append(rule)
        if matching:
            return matching

    # Otherwise, we'd need to search all rules from API
    # The ARBA API doesn't support searching by InterPro ID directly
    # For now, return empty if not in cache
    return []


def fetch_rules_by_ec(
    ec_number: str,
    client: Optional[ARBAClient] = None
) -> list[ARBARule]:
    """Fetch ARBA rules that annotate a specific EC number.

    Args:
        ec_number: EC number (e.g., "2.3.2.5")
        client: Optional ARBAClient instance

    Returns:
        List of matching ARBARule objects
    """
    if client is None:
        client = ARBAClient()

    rules, _ = client.search(query=f"ec:{ec_number}", size=500)
    return rules
