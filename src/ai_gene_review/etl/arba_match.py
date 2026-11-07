"""Evaluate ARBA rule conditions against a protein.

An ARBA rule fires on a protein when every condition of at least one of its
condition sets holds. ARBA uses four condition types: InterPro, PANTHER,
FunFam and taxon. This module answers "does rule X fire on protein Y, and if
not, which conditions fail?", and checks the ARBA rows (``GO_REF:0000117``)
of a cached GOA file against the rules they cite. Conditions are tested with
the same :func:`ai_gene_review.curated_rules.condition_holds` used for this
project's own curated rules.

ARBA serves only the current version of a rule, and GOA can be built from rule
data newer or older than the public UniProt release. A GOA row whose cited rule
does not match today is therefore only a real mismatch when the rule has not
been edited since the row was loaded; otherwise the result is
``RULE_EDITED_SINCE_LOAD``.

Example:
    >>> from ai_gene_review.etl.arba import ARBARule
    >>> rule = ARBARule.from_json({
    ...     "uniRuleId": "ARBA00000001",
    ...     "mainRule": {"conditionSets": [{"conditions": [
    ...         {"type": "InterPro id", "conditionValues": [{"value": "IPR000873"}]},
    ...         {"type": "taxon", "conditionValues": [{"value": "Glires", "cvId": "314147"}]},
    ...     ]}], "annotations": []},
    ...     "modifiedDate": "2026-07-18",
    ... })
    >>> bacterium = ProteinFeatures({"INTERPRO": {"IPR000873"}}, {"NCBITaxon:2", "NCBITaxon:160488"})
    >>> result = evaluate_rule(rule, bacterium)
    >>> result.matched, result.closest_failure
    (False, 'TAXON_ONLY')
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import requests

from ai_gene_review.curated_rules import ProteinFeatures, condition_holds
from ai_gene_review.etl.arba import ARBAClient, ARBARule, Condition, ConditionSet
from ai_gene_review.export.propagation_rows import read_goa_rows

UNIPROT_REST = "https://rest.uniprot.org"
ARBA_GO_REF = "GO_REF:0000117"

# ARBA condition types, as curated-rule condition types.
ARBA_CONDITION_TYPES = {
    "InterPro id": "INTERPRO",
    "PANTHER id": "PANTHER",
    "FunFam id": "FUNFAM",
    "taxon": "TAXON",
}

# UniProtKB cross-reference databases, as curated-rule condition types.
UNIPROT_SIGNATURE_DBS = {"InterPro": "INTERPRO", "PANTHER": "PANTHER", "FunFam": "FUNFAM"}

# Closest-failure kinds, best (nearest to matching) first.
FAILURE_KINDS = ("TAXON_ONLY", "PARTIAL_SIGNATURE", "NO_SIGNATURE")


def arba_condition_holds(condition: Condition, features: ProteinFeatures) -> bool:
    """Test one ARBA condition: any of its values present, inverted if negative.

    Taxon conditions match on the NCBI id (``cvId``).

    >>> from ai_gene_review.etl.arba import ConditionValue
    >>> f = ProteinFeatures({"PANTHER": {"PTHR1", "PTHR1:SF2"}}, {"NCBITaxon:9606", "NCBITaxon:2759"})
    >>> arba_condition_holds(Condition("taxon", [ConditionValue("Eukaryota", "2759")]), f)
    True
    >>> arba_condition_holds(Condition("PANTHER id", [ConditionValue("PTHR1")], is_negative=True), f)
    False
    """
    ctype = ARBA_CONDITION_TYPES[condition.condition_type]
    values = [f"NCBITaxon:{cv.cv_id}" if ctype == "TAXON" else cv.value for cv in condition.values]
    present = any(condition_holds({"condition_type": ctype, "value": v}, features) for v in values)
    return present != condition.is_negative


@dataclass
class ConditionResult:
    condition: Condition
    holds: bool


@dataclass
class ConditionSetResult:
    index: int
    conditions: list[ConditionResult]

    @property
    def matched(self) -> bool:
        return all(c.holds for c in self.conditions)

    @property
    def failure_kind(self) -> Optional[str]:
        """Classify a failing set: taxon only, some signatures, or no signatures.

        >>> from ai_gene_review.etl.arba import ConditionValue
        >>> sig = Condition("InterPro id", [ConditionValue("IPR1")])
        >>> tax = Condition("taxon", [ConditionValue("Glires", "314147")])
        >>> ConditionSetResult(0, [ConditionResult(sig, True), ConditionResult(tax, False)]).failure_kind
        'TAXON_ONLY'
        >>> ConditionSetResult(0, [ConditionResult(sig, False), ConditionResult(tax, True)]).failure_kind
        'NO_SIGNATURE'
        """
        if self.matched:
            return None
        signatures = [c.holds for c in self.conditions if c.condition.condition_type != "taxon"]
        if all(signatures):
            return "TAXON_ONLY"
        if any(signatures):
            return "PARTIAL_SIGNATURE"
        return "NO_SIGNATURE"


@dataclass
class RuleMatch:
    rule_id: str
    rule_modified: str
    sets: list[ConditionSetResult]

    @property
    def matched(self) -> bool:
        return any(s.matched for s in self.sets)

    @property
    def matching_sets(self) -> list[int]:
        return [s.index for s in self.sets if s.matched]

    @property
    def closest_failure(self) -> Optional[str]:
        if self.matched or not self.sets:
            return None
        kinds = [s.failure_kind for s in self.sets]
        return min((k for k in kinds if k), key=FAILURE_KINDS.index)

    @property
    def closest_sets(self) -> list[ConditionSetResult]:
        """The failing sets of the closest failure kind, for reporting."""
        kind = self.closest_failure
        return [s for s in self.sets if s.failure_kind == kind]


def evaluate_condition_set(index: int, condition_set: ConditionSet, features: ProteinFeatures) -> ConditionSetResult:
    return ConditionSetResult(
        index=index,
        conditions=[ConditionResult(c, arba_condition_holds(c, features)) for c in condition_set.conditions],
    )


def evaluate_rule(rule: ARBARule, features: ProteinFeatures) -> RuleMatch:
    """Evaluate every condition set of ``rule`` against ``features``."""
    return RuleMatch(
        rule_id=rule.uni_rule_id,
        rule_modified=rule.modified_date,
        sets=[evaluate_condition_set(i, cs, features) for i, cs in enumerate(rule.condition_sets)],
    )


def load_status(match: RuleMatch, load_date: str) -> str:
    """Judge a GOA row against the current rule, allowing for rule edits.

    ``load_date`` is the GOA DATE column (``YYYYMMDD``); ``rule_modified`` is
    ARBA's ``modifiedDate`` (``YYYY-MM-DD``).

    >>> m = RuleMatch("ARBA1", "2026-07-18", [])
    >>> load_status(m, "20260601")
    'RULE_EDITED_SINCE_LOAD'
    >>> load_status(m, "20260727")
    'MISMATCH'
    """
    if match.matched:
        return "MATCH"
    if match.rule_modified.replace("-", "") > load_date:
        return "RULE_EDITED_SINCE_LOAD"
    return "MISMATCH"


@dataclass
class UniProtProtein:
    """A UniProtKB entry's identity plus the features ARBA conditions test."""

    accession: str
    taxon_id: str
    uniprot_release: str
    features: ProteinFeatures


def parse_uniprot_entry(entry: dict, lineage: set[str], release: str = "") -> UniProtProtein:
    """Build a protein from a UniProtKB JSON entry and its NCBITaxon lineage.

    PANTHER subfamilies also contribute their family id, so a family condition
    matches a protein classified to one of its subfamilies.

    >>> entry = {"primaryAccession": "P1", "organism": {"taxonId": 9606},
    ...          "uniProtKBCrossReferences": [
    ...              {"database": "PANTHER", "id": "PTHR1:SF2"},
    ...              {"database": "FunFam", "id": "3.30.300.30:FF:000005"}]}
    >>> p = parse_uniprot_entry(entry, {"NCBITaxon:9606"})
    >>> sorted(p.features.signatures["PANTHER"]), sorted(p.features.signatures["FUNFAM"])
    (['PTHR1', 'PTHR1:SF2'], ['3.30.300.30:FF:000005'])
    """
    signatures: dict[str, set[str]] = {ctype: set() for ctype in UNIPROT_SIGNATURE_DBS.values()}
    for ref in entry.get("uniProtKBCrossReferences", []):
        if ref["database"] in UNIPROT_SIGNATURE_DBS:
            signatures[UNIPROT_SIGNATURE_DBS[ref["database"]]].add(ref["id"])
    signatures["PANTHER"] |= {p.split(":")[0] for p in signatures["PANTHER"]}
    return UniProtProtein(
        accession=entry["primaryAccession"],
        taxon_id=str(entry["organism"]["taxonId"]),
        uniprot_release=release,
        features=ProteinFeatures(signatures, lineage),
    )


class UniProtFeatureClient:
    """Fetch protein signatures and NCBI lineages from the UniProt REST API."""

    def __init__(self, base_url: str = UNIPROT_REST):
        self.base_url = base_url
        self._session = requests.Session()
        self._session.headers.update({"Accept": "application/json"})
        self._lineages: dict[str, set[str]] = {}

    def lineage(self, taxon_id: str) -> set[str]:
        """NCBITaxon CURIEs of the taxon and all its ancestors."""
        if taxon_id not in self._lineages:
            response = self._session.get(f"{self.base_url}/taxonomy/{taxon_id}", timeout=30)
            response.raise_for_status()
            ids = {str(t["taxonId"]) for t in response.json().get("lineage", [])} | {taxon_id}
            self._lineages[taxon_id] = {f"NCBITaxon:{i}" for i in ids}
        return self._lineages[taxon_id]

    def proteins(self, accessions: list[str]) -> dict[str, UniProtProtein]:
        """Fetch up to 100 accessions; accessions absent from UniProtKB are omitted."""
        params: dict[str, str | int] = {
            "accessions": ",".join(accessions),
            "fields": "accession,organism_id,xref_interpro,xref_panther,xref_funfam",
            "format": "json",
            "size": 100,
        }
        response = self._session.get(f"{self.base_url}/uniprotkb/accessions", params=params, timeout=60)
        response.raise_for_status()
        release = response.headers.get("x-uniprot-release", "")
        out = {}
        for entry in response.json()["results"]:
            lineage = self.lineage(str(entry["organism"]["taxonId"]))
            out[entry["primaryAccession"]] = parse_uniprot_entry(entry, lineage, release)
        return out


@dataclass
class GoaArbaCheck:
    """The verdict on one ARBA row of a GOA file."""

    accession: str
    go_id: str
    go_name: str
    load_date: str
    status: str
    matches: list[RuleMatch]


def arba_rule_ids(with_from: str) -> list[str]:
    """Extract ARBA rule ids from a GOA WITH/FROM value.

    >>> arba_rule_ids("ARBA:ARBA00026258|UniProtKB-KW:KW-0548")
    ['ARBA00026258']
    """
    return [v.split(":", 1)[1] for v in with_from.split("|") if v.startswith("ARBA:")]


def arba_goa_rows(goa_file: Path) -> list[dict[str, str]]:
    """Return the ARBA rows (``GO_REF:0000117``) of a cached GOA TSV."""
    return [r for r in read_goa_rows(goa_file) if r.get("REFERENCE") == ARBA_GO_REF]


def check_goa_rows(
    rows: list[dict[str, str]],
    rules: dict[str, Optional[ARBARule]],
    features: dict[str, ProteinFeatures],
) -> list[GoaArbaCheck]:
    """Check GOA ARBA rows against the rules they cite.

    ``rules`` maps every cited rule id to the current rule, or ``None`` when
    ARBA no longer serves it; ``features`` maps accessions to their features
    and omits accessions absent from UniProtKB.

    A row is ``MATCH`` when any cited rule fires; ``RULE_EDITED_SINCE_LOAD``
    and ``MISMATCH`` are decided by :func:`load_status` on the latest-modified
    cited rule. Rules ARBA no longer serves give ``RULE_NOT_FOUND``, and
    accessions absent from UniProtKB give ``PROTEIN_NOT_FOUND``.
    """
    checks = []
    for row in rows:
        accession = row["GENE PRODUCT ID"]
        load_date = row.get("DATE", "")
        cited = [rules[r] for r in arba_rule_ids(row.get("WITH/FROM", ""))]
        found = [r for r in cited if r is not None]
        matches: list[RuleMatch] = []
        if accession not in features:
            status = "PROTEIN_NOT_FOUND"
        elif not found:
            status = "RULE_NOT_FOUND"
        else:
            matches = [evaluate_rule(r, features[accession]) for r in found]
            hit = [m for m in matches if m.matched]
            latest = max(matches, key=lambda m: m.rule_modified)
            status = load_status(hit[0] if hit else latest, load_date)
        checks.append(
            GoaArbaCheck(
                accession=accession,
                go_id=row["GO TERM"],
                go_name=row.get("GO NAME", ""),
                load_date=load_date,
                status=status,
                matches=matches,
            )
        )
    return checks


def check_goa_file(
    goa_file: Path,
    rule_client: ARBAClient,
    feature_client: UniProtFeatureClient,
) -> list[GoaArbaCheck]:
    """Fetch current rules and features, then check a GOA file's ARBA rows.

    Rules are always fetched fresh, since a cached copy may predate an edit.
    """
    rows = arba_goa_rows(goa_file)
    accessions = sorted({r["GENE PRODUCT ID"] for r in rows})
    features: dict[str, ProteinFeatures] = {}
    for i in range(0, len(accessions), 100):
        fetched = feature_client.proteins(accessions[i : i + 100])
        features.update({acc: p.features for acc, p in fetched.items()})
    rule_ids = sorted({rid for r in rows for rid in arba_rule_ids(r.get("WITH/FROM", ""))})
    rules = {rid: rule_client.fetch_rule(rid, use_cache=False) for rid in rule_ids}
    return check_goa_rows(rows, rules, features)
