"""LitScan gene-gap scan: rank recent papers by the function-knowledge gap they close.

The scan is a deterministic lead generator in the dismech literature-scan
pattern. It

1. runs each Europe PMC query profile in ``conf/litscan/gene_gap.yaml`` over a
   date window (MEDLINE, optionally preprints), excluding reviews;
2. drops papers that an issue (open or closed) already names;
3. finds gene symbols in each title and abstract (Europe PMC text mining plus
   symbol-shaped title tokens) and resolves them to one UniProtKB entry in the
   paper's species;
4. measures the gap for each gene product: QuickGO annotation counts by evidence
   class, unknown-function domains and name, and whether any member of its
   PANTHER family is experimentally annotated;
5. drops pairs whose ai-gene-review review already cites the paper, scores the
   rest with the config's rules, ranks them and caps the issue handoffs.

It writes a packet (JSON valid against ``GeneGapPacket``, plus markdown) and one
ready-to-file issue body per eligible candidate. It never writes to GitHub; the
workflow files the ranks selected in triage. See ``docs/litscan_gene_gap.md``.
"""

from __future__ import annotations

import datetime as dt
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

from ai_gene_review.litscan import gene_gap_sources as sources
from ai_gene_review.litscan.europepmc import Publication, search
from ai_gene_review.litscan.polite import PoliteClient

DEFAULT_CONFIG = Path("conf/litscan/gene_gap.yaml")
DEFAULT_OUTPUT = Path("reports/litscan/gene-gap")
JOB = "gene-gap"
MARKER_PREFIX = "litscan-gene-gap"
ISSUE_LABELS = ["curation", "litscan", "gene-gap"]

_REFERENCE_RE = re.compile(
    r"(?:PMID[:_ ]+|pubmed\.ncbi\.nlm\.nih\.gov/|europepmc\.org/article/MED/)(?P<pmid>\d+)"
    r"|(?:\bdoi:\s*|doi\.org/)(?P<doi>10\.\d{4,9}/[^\s\x22\x27<>|]+)"
    r"|\b(?P<ppr>PPR\d+)\b",
    re.I,
)
_REVIEW_ID_RE = re.compile(r"^id:\s*['\"]?(?:UniProtKB:)?([A-Za-z0-9_.-]+)", re.M)
_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]{1,14}")
_BACTERIAL_SYMBOL_RE = re.compile(r"[a-z]{3}[A-Z][0-9]*|[A-Z][a-z]{2}[A-Z][0-9]*")


# --------------------------------------------------------------------- config
def load_config(path: Path = DEFAULT_CONFIG) -> dict[str, Any]:
    """Load a GeneGapScanConfig YAML file."""
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def default_date_range(days: int, today: dt.date | None = None) -> tuple[str, str]:
    """``(from, to)`` ISO dates covering the last ``days`` days.

    >>> default_date_range(30, dt.date(2026, 11, 26))
    ('2026-10-28', '2026-11-26')
    """
    end = today or dt.datetime.now(dt.timezone.utc).date()
    return (end - dt.timedelta(days=days - 1)).isoformat(), end.isoformat()


def build_query(
    profile_query: str,
    date_from: str,
    date_to: str,
    *,
    exclude_title_terms: Iterable[str] = (),
    include_preprints: bool = False,
) -> str:
    """Europe PMC query for one profile within the window, reviews excluded.

    >>> q = build_query('TITLE_ABS:"x"', "2026-01-01", "2026-01-31",
    ...                 exclude_title_terms=["erratum"])
    >>> q
    'SRC:MED AND FIRST_PDATE:[2026-01-01 TO 2026-01-31] AND (TITLE_ABS:"x") NOT PUB_TYPE:"review" NOT (TITLE:erratum)'
    >>> build_query("x", "a", "b", include_preprints=True).startswith("(SRC:MED OR SRC:PPR)")
    True
    """
    source = "(SRC:MED OR SRC:PPR)" if include_preprints else "SRC:MED"
    query = (
        f"{source} AND FIRST_PDATE:[{date_from} TO {date_to}] "
        f'AND ({" ".join(profile_query.split())}) NOT PUB_TYPE:"review"'
    )
    excluded = [f"TITLE:{term}" for term in exclude_title_terms]
    if excluded:
        query += f" NOT ({' OR '.join(excluded)})"
    return query


# --------------------------------------------------------------- repo indexes
@dataclass
class ReviewIndex:
    """ai-gene-review reviews by UniProt accession, with the publication identifiers each cites."""

    paths: dict[str, str] = field(default_factory=dict)
    cited: dict[str, set[str]] = field(default_factory=dict)

    @classmethod
    def build(cls, genes_dir: Path) -> "ReviewIndex":
        """Scan ``genes/*/*/*-ai-review.yaml`` with regexes (fast, no YAML parse)."""
        index = cls()
        for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
            text = path.read_text(encoding="utf-8")
            match = _REVIEW_ID_RE.search(text)
            if not match:
                continue
            accession = match.group(1)
            index.paths.setdefault(accession, str(path))
            index.cited.setdefault(accession, set()).update(reference_ids(text))
        return index


def reference_ids(text: str) -> set[str]:
    """Canonical publication identifiers in review YAML, issue prose or URLs."""
    found = set()
    for match in _REFERENCE_RE.finditer(text):
        if pmid := match["pmid"]:
            found.add(f"PMID:{pmid}")
        elif doi := match["doi"]:
            doi = doi.rstrip(".,;:`]}").lower()
            if doi.endswith(")") and doi.count(")") > doi.count("("):
                doi = doi[:-1]
            found.add(f"DOI:{doi}")
        else:
            found.add(f"PPR:{match['ppr'].upper()}")
    return found


def paper_ids(pub: Publication) -> set[str]:
    identifiers = {pub.reference_id} if pub.reference_id else set()
    if pub.doi:
        identifiers.add(f"DOI:{pub.doi.lower()}")
    if pub.source == "PPR":
        identifiers.add(sources.article_id(pub.source, pub.record_id))
    return identifiers


def ledger_references(issues: Iterable[dict[str, Any]]) -> set[str]:
    return {
        ref
        for issue in issues
        for field_name in ("title", "body")
        for ref in reference_ids(issue.get(field_name) or "")
    }


# ---------------------------------------------------------- text extraction
def detect_species(text: str, species: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Configured species mentioned in ``text``, most mentions first.

    >>> sp = [{"taxon_id": 9606, "label": "Homo sapiens", "folder": "human",
    ...        "patterns": [r"\\bhuman\\b"]},
    ...       {"taxon_id": 83333, "label": "E. coli", "folder": "ECOLI",
    ...        "patterns": [r"\\bE\\. coli\\b"]}]
    >>> [s["folder"] for s in detect_species("E. coli and E. coli vs human", sp)]
    ['ECOLI', 'human']
    """
    counts = []
    for order, sp in enumerate(species):
        n = sum(len(re.findall(p, text, flags=re.IGNORECASE)) for p in sp["patterns"])
        if n:
            counts.append((-n, order, sp))
    return [sp for _, _, sp in sorted(counts, key=lambda c: (c[0], c[1]))]


def looks_like_symbol(token: str, stoplist: set[str]) -> bool:
    """Whether a title token is shaped like a gene symbol.

    >>> stop = {"dna", "crispr"}
    >>> [t for t in ["YqcI", "TP53", "ftsZ", "Pex3", "DNA", "Protein", "CRISPR", "SLC25A51"]
    ...  if looks_like_symbol(t, stop)]
    ['YqcI', 'TP53', 'ftsZ', 'Pex3', 'SLC25A51']
    """
    if token.lower() in stoplist or len(token) < 3:
        return False
    if _BACTERIAL_SYMBOL_RE.fullmatch(token):
        return True
    uppers = sum(c.isupper() for c in token)
    digits = any(c.isdigit() for c in token)
    return uppers >= 2 or (digits and token[0].isupper())


def candidate_symbols(
    title: str,
    gene_mentions: list[tuple[str, str]],
    stoplist: set[str],
    limit: int,
) -> list[tuple[str, bool]]:
    """Ordered ``(symbol, in_title)`` candidates for one paper.

    Title mentions come first (text-mined, then symbol-shaped title tokens), then
    abstract mentions seen at least twice, most frequent first.

    >>> candidate_symbols("YqcI/YcgG heme monooxygenases",
    ...                   [("heme monooxygenases", "title"), ("CsdA", "abstract"),
    ...                    ("CsdA", "abstract"), ("once", "abstract")], set(), 5)
    [('YqcI', True), ('YcgG', True), ('CsdA', False)]
    """
    out: list[tuple[str, bool]] = []
    seen: set[str] = set()

    def add(symbol: str, in_title: bool) -> None:
        key = symbol.lower()
        if (
            key in seen
            or key in stoplist
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", symbol)
            or not (2 < len(symbol) <= 15)
        ):
            return
        seen.add(key)
        out.append((symbol, in_title))

    for exact, kind in gene_mentions:
        if kind == "title":
            for part in exact.split("/"):
                add(part.strip(), True)
    for token in _TOKEN_RE.findall(title):
        if looks_like_symbol(token, stoplist):
            add(token, True)
    abstract_counts = Counter(
        exact.strip() for exact, kind in gene_mentions if kind == "abstract"
    )
    for exact, n in sorted(abstract_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        if n >= 2:
            add(exact, False)
    return out[:limit]


# ------------------------------------------------------------------ scoring
def band_score(count: int, bands: list[dict[str, Any]]) -> dict[str, Any] | None:
    """The first band whose ``max`` is at least ``count`` (open band last).

    >>> bands = [{"max": 0, "points": 5, "label": "none"}, {"points": -1, "label": "many"}]
    >>> band_score(0, bands)["points"], band_score(7, bands)["points"]
    (5, -1)
    """
    for band in bands:
        if band.get("max") is None or count <= band["max"]:
            return band
    return None


def informative_experimental(counts: dict[str, int]) -> int:
    """Experimental annotations other than bare protein binding."""
    return counts["experimental"] - counts["experimental_protein_binding"]


def _matches_any(patterns: Iterable[str], text: str) -> bool:
    return any(re.search(p, text, flags=re.IGNORECASE) for p in patterns)


def score_gene(gene: dict[str, Any], scoring: dict[str, Any]) -> list[dict[str, Any]]:
    """Gene-side score components (see ``gene_scoring`` in the config).

    Pairs whose review already cites the paper are suppressed before scoring, so
    an existing review here never cites it.
    """
    counts = gene["annotation_counts"]
    components: list[dict[str, Any]] = []

    def add(rule: str, spec: dict[str, Any] | None) -> None:
        if spec and spec["points"]:
            components.append(
                {"rule": rule, "points": spec["points"], "label": spec["label"]}
            )

    add(
        "experimental_annotations",
        band_score(
            informative_experimental(counts), scoring["experimental_annotation_bands"]
        ),
    )
    if counts["experimental_mf"] - counts["experimental_protein_binding"] <= 0:
        add("no_experimental_mf", scoring["no_experimental_mf"])
    if counts["total"] and counts["iba"] + counts["iea"] == counts["total"]:
        add("electronic_only", scoring["electronic_only"])
    if _matches_any(
        scoring["uncharacterized_name"]["patterns"], gene.get("protein_name", "")
    ):
        add("uncharacterized_name", scoring["uncharacterized_name"])
    if gene.get("unknown_function_domains"):
        add("duf_domain", scoring["duf_domain"])
    family = gene.get("family")
    if (
        family
        and family["member_count"] > 0
        and family.get("experimental_member_count") is not None
    ):
        add(
            "family_experimental",
            band_score(
                family["experimental_member_count"],
                scoring["family_experimental_bands"],
            ),
        )
    if gene.get("review_path"):
        add("existing_review_not_citing", scoring["existing_review_not_citing"])
    if gene.get("paper_in_goa"):
        add("already_in_goa", scoring["already_in_goa"])
    return components


def score_paper(
    title: str, abstract: str, rules: list[dict[str, Any]], *, gene_in_title: bool
) -> list[dict[str, Any]]:
    """Paper-side score components; each rule fires at most once.

    >>> rules = [{"id": "t", "points": 2, "label": "in title", "field": "gene_title"},
    ...          {"id": "r", "points": -5, "label": "review", "field": "title",
    ...           "patterns": [r"\\breview\\b"]}]
    >>> [c["rule"] for c in score_paper("A review", "", rules, gene_in_title=True)]
    ['t', 'r']
    """
    components = []
    for rule in rules:
        if rule["field"] == "gene_title":
            fired = gene_in_title
        elif rule["field"] == "title":
            fired = _matches_any(rule["patterns"], title)
        else:
            fired = _matches_any(rule["patterns"], f"{title} {abstract}")
        if fired:
            components.append(
                {"rule": rule["id"], "points": rule["points"], "label": rule["label"]}
            )
    return components


def ledger_marker(reference_id: str, accession: str) -> str:
    """Hidden marker that ends each issue body.

    >>> ledger_marker("PMID:1", "P04637")
    '<!-- litscan-gene-gap: PMID:1 UniProtKB:P04637 -->'
    """
    return f"<!-- {MARKER_PREFIX}: {reference_id} UniProtKB:{accession} -->"


def rank_candidates(
    candidates: list[dict[str, Any]], limits: dict[str, Any]
) -> list[dict[str, Any]]:
    """Sort by score, keep ``max_candidates`` and mark the issue-eligible ones.

    Ties break on fewer informative experimental annotations, then reference
    and accession, so a re-run over the same data gives the same order.
    """
    ordered = sorted(
        candidates,
        key=lambda c: (
            -c["score"],
            informative_experimental(c["gene"]["annotation_counts"]),
            c["paper"]["reference_id"],
            c["gene"]["accession"],
        ),
    )[: limits["max_candidates"]]
    per_paper: Counter[str] = Counter()
    issued = 0
    for rank, cand in enumerate(ordered, start=1):
        cand["rank"] = rank
        ref = cand["paper"]["reference_id"]
        eligible = (
            cand["score"] >= limits["min_issue_score"]
            and issued < limits["max_issues"]
            and per_paper[ref] < limits["max_issues_per_paper"]
        )
        cand["issue_eligible"] = eligible
        if eligible:
            issued += 1
            per_paper[ref] += 1
    return ordered


# ------------------------------------------------------------------ the run
def _paper_record(pub: Publication, profiles: list[str]) -> dict[str, Any]:
    return {
        "pmid": pub.pmid,
        "reference_id": pub.reference_id or f"{pub.source}:{pub.record_id}",
        "title": pub.title,
        "journal": pub.journal,
        "publication_date": pub.publication_date,
        "doi": pub.doi,
        "source": pub.source,
        "pubmed_url": pub.pubmed_url,
        "europe_pmc_url": pub.europe_pmc_url,
        "abstract": pub.abstract,
        "profiles": profiles,
        "is_preprint": pub.source == "PPR",
    }


def _unknown_function_domains(
    pfam_names: list[str], scoring: dict[str, Any]
) -> list[str]:
    patterns = scoring["duf_domain"]["patterns"]
    return [n for n in pfam_names if _matches_any(patterns, n)]


def run(
    config: dict[str, Any],
    *,
    date_from: str,
    date_to: str,
    genes_dir: Path = Path("genes"),
    ledger: list[dict[str, Any]] | None = None,
    include_preprints: bool = False,
    client: PoliteClient | None = None,
    config_path: str = "",
    log: Any = print,
) -> dict[str, Any]:
    """Run the scan and return a GeneGapPacket dict."""
    client = client or PoliteClient.from_config(config)
    limits = config["limits"]
    stoplist = {s.lower() for s in config.get("symbol_stoplist") or []}
    scoring = config["gene_scoring"]

    # 1. retrieve
    queries = []
    papers: dict[str, Publication] = {}
    profiles_by_key: dict[str, list[str]] = {}
    for profile in config["query_profiles"]:
        query = build_query(
            profile["query"],
            date_from,
            date_to,
            exclude_title_terms=config.get("exclude_title_terms") or [],
            include_preprints=include_preprints,
        )
        hit_count, pubs = search(
            query,
            max_records=limits["max_records_per_profile"],
            sort="",
            client=client,
        )
        queries.append(
            {
                "profile": profile["name"],
                "query": query,
                "hit_count": hit_count,
                "fetched": len(pubs),
            }
        )
        for pub in pubs:
            key = sources.article_id(pub.source, pub.record_id)
            papers.setdefault(key, pub)
            profiles_by_key.setdefault(key, []).append(profile["name"])
        log(f"{profile['name']}: {hit_count} hits, fetched {len(pubs)}")

    # 2. ledger
    suppressed: list[dict[str, Any]] = []
    seen_refs = ledger_references(ledger or [])
    for key in list(papers):
        if paper_ids(papers[key]) & seen_refs:
            suppressed.append(
                {
                    "reference_id": papers[key].reference_id or key,
                    "reason": "LEDGER",
                    "detail": "named by an existing issue",
                }
            )
            del papers[key]

    # 3. mentions and resolution
    mentions = sources.fetch_mentions(client, papers)
    log(f"{len(papers)} papers; fetched text-mined mentions")
    resolved_cache: dict[tuple[str, int, bool], dict[str, Any] | None] = {}
    pairs: list[tuple[str, dict[str, Any], str, bool, dict[str, Any]]] = []
    for n, (key, pub) in enumerate(papers.items(), start=1):
        if n % 50 == 0:
            log(f"  resolving genes: {n}/{len(papers)} papers, {client.calls} calls")
        text = f"{pub.title} {pub.abstract}"
        species = detect_species(text, config.get("species") or [])
        taxa: list[tuple[int, dict[str, Any]]] = [
            (int(sp["taxon_id"]), sp) for sp in species[:2]
        ]
        if not taxa:
            organisms = Counter(
                tax for tax, _ in mentions[key]["organisms"] if tax.isdigit()
            )
            configured = {sp["taxon_id"]: sp for sp in config["species"]}
            taxa = [
                (int(t), configured[int(t)])
                for t, _ in organisms.most_common()
                if int(t) in configured
            ][:2]
        symbols = candidate_symbols(
            pub.title, mentions[key]["genes"], stoplist, limits["max_symbols_per_paper"]
        )
        title_symbols = {s.lower() for s, in_title in symbols if in_title}
        for taxon, _ in taxa:
            todo = [
                s
                for s, title in symbols
                if (s.lower(), taxon, title) not in resolved_cache
            ]
            batch = sources.resolve_symbols(
                client,
                todo,
                taxon,
                limits["max_resolution_hits"],
                fallback=title_symbols,
            )
            for sym_key, entry in batch.items():
                resolved_cache[(sym_key, taxon, sym_key in title_symbols)] = entry
        found: dict[str, Any] = {}
        for symbol, in_title in symbols:
            if len(found) >= limits["max_genes_per_paper"]:
                break
            for taxon, sp in taxa:
                entry = resolved_cache[(symbol.lower(), taxon, in_title)]
                if entry and entry["accession"] not in found:
                    found[entry["accession"]] = (entry, symbol, in_title, sp)
                    break
        if not found:
            suppressed.append(
                {
                    "reference_id": pub.reference_id or key,
                    "reason": "UNRESOLVED",
                    "detail": ", ".join(s for s, _ in symbols) or "no symbol",
                }
            )
        for entry, symbol, in_title, sp in found.values():
            pairs.append((key, entry, symbol, in_title, sp))
    log(f"resolved {len(pairs)} (paper, gene) pairs")

    # 4. gap evidence
    reviews = ReviewIndex.build(genes_dir)
    profiles: dict[str, sources.AnnotationProfile] = {}
    family_cache: dict[str, dict[str, Any]] = {}
    candidates = []
    for n, (key, entry, symbol, in_title, sp) in enumerate(pairs, start=1):
        if n % 50 == 0:
            log(f"  gap evidence: {n}/{len(pairs)} pairs, {client.calls} calls")
        pub = papers[key]
        accession = entry["accession"]
        cites = paper_ids(pub) & reviews.cited.get(accession, set())
        if cites:
            suppressed.append(
                {
                    "reference_id": pub.reference_id or key,
                    "accession": accession,
                    "reason": "ALREADY_CITED",
                    "detail": reviews.paths[accession],
                }
            )
            continue
        if accession not in profiles:
            profiles[accession] = sources.annotation_profile(client, accession)
        family = None
        if entry["panther_id"]:
            if entry["panther_id"] not in family_cache:
                family_cache[entry["panther_id"]] = sources.family_status(
                    client, entry["panther_id"], entry["panther_name"]
                )
            family = family_cache[entry["panther_id"]]
        gene = {
            "accession": accession,
            "entry_name": entry["entry_name"],
            "symbol": entry["symbol"] or symbol,
            "matched_symbol": symbol,
            "matched_in_title": in_title,
            "protein_name": entry["protein_name"],
            "organism": entry["organism"],
            "taxon_id": entry["taxon_id"],
            "folder": sp["folder"],
            "reviewed": entry["reviewed"],
            "protein_existence": entry["protein_existence"],
            "annotation_counts": profiles[accession].counts,
            "evidence_codes": [
                {"code": code, "count": count}
                for code, count in profiles[accession].evidence_codes.items()
            ],
            "family": family,
            "unknown_function_domains": _unknown_function_domains(
                entry["pfam_names"], scoring
            ),
            "review_path": reviews.paths.get(accession),
            "paper_in_goa": bool(pub.pmid)
            and f"PMID:{pub.pmid}" in profiles[accession].references,
        }
        gene = {k: v for k, v in gene.items() if v is not None}
        components = score_gene(gene, scoring) + score_paper(
            pub.title,
            pub.abstract,
            config["paper_scoring"],
            gene_in_title=in_title,
        )
        paper = _paper_record(pub, profiles_by_key[key])
        candidates.append(
            {
                "score": sum(c["points"] for c in components),
                "action": "UPDATE_REVIEW" if gene.get("review_path") else "NEW_REVIEW",
                "ledger_marker": ledger_marker(paper["reference_id"], accession),
                "paper": paper,
                "gene": gene,
                "score_components": components,
            }
        )
    log(f"scored {len(candidates)} candidates; {client.calls} HTTP calls")

    ranked = rank_candidates(candidates, limits)
    for cand in ranked:
        cand["issue_title"] = issue_title(cand)
        cand["issue_labels"] = issue_labels(cand)
    return {
        "job": JOB,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "date_from": date_from,
        "date_to": date_to,
        "include_preprints": include_preprints,
        "config_path": config_path,
        "queries": queries,
        "paper_count": len(papers),
        "resolved_gene_count": len({p[1]["accession"] for p in pairs}),
        "suppressed": suppressed,
        "candidates": ranked,
    }


# -------------------------------------------------------------- rendering
def _short(text: str, n: int = 80) -> str:
    """Truncate at a word boundary.

    >>> _short("alpha beta gamma", 12)
    'alpha beta…'
    >>> _short("abc", 10)
    'abc'
    """
    if len(text) <= n:
        return text
    return text[:n].rsplit(" ", 1)[0] + "…"


def issue_title(cand: dict[str, Any]) -> str:
    """``[litscan:gene-gap] SYMBOL (organism): short paper title``."""
    gene, paper = cand["gene"], cand["paper"]
    return (
        f"[litscan:gene-gap] {gene['symbol']} ({gene['organism']}): "
        f"{_short(paper['title'], 70)}"
    )


def issue_labels(cand: dict[str, Any]) -> list[str]:
    """Issue labels; an update to an existing review is medium effort.

    >>> issue_labels({"action": "UPDATE_REVIEW"})
    ['curation', 'litscan', 'gene-gap', 'medium_effort']
    >>> issue_labels({"action": "NEW_REVIEW"})
    ['curation', 'litscan', 'gene-gap']
    """
    extra = ["medium_effort"] if cand["action"] == "UPDATE_REVIEW" else []
    return ISSUE_LABELS + extra


def gap_evidence_lines(gene: dict[str, Any]) -> list[str]:
    """Markdown lines summarising the gene's annotation state."""
    c = gene["annotation_counts"]
    lines = [
        "| GO annotations (QuickGO) | count |",
        "| --- | ---: |",
        f"| total | {c['total']} |",
        f"| experimental (EXP/IDA/IPI/IMP/IGI/IEP/HT*) | {c['experimental']} |",
        f"| of which bare protein binding (GO:0005515) | {c['experimental_protein_binding']} |",
        f"| experimental molecular function | {c['experimental_mf']} |",
        f"| IBA | {c['iba']} |",
        f"| IEA | {c['iea']} |",
        f"| other (ISS/ISO/TAS/NAS/IC/ND...) | {c['other']} |",
        "",
    ]
    codes = ", ".join(
        f"{c['code']} {c['count']}" for c in gene.get("evidence_codes", [])
    )
    lines.append(f"- Source evidence codes: {codes or 'none'}")
    family = gene.get("family")
    if family:
        lines.append(
            f"- PANTHER family: {family['panther_id']} "
            f"({family.get('panther_name') or 'unnamed'}): "
            f"{family['member_count']} UniProtKB members, "
            f"{family['experimental_member_count']} with experimental GO"
        )
    else:
        lines.append("- PANTHER family: none assigned")
    domains = gene.get("unknown_function_domains") or []
    lines.append(
        f"- Unknown-function domains: {', '.join(domains) if domains else 'none'}"
    )
    lines.append(
        f"- UniProt: {'reviewed' if gene['reviewed'] else 'unreviewed'}; "
        f"existence: {gene.get('protein_existence') or 'n/a'}"
    )
    lines.append(
        "- Paper already a GOA reference for this entry: "
        f"{'yes' if gene.get('paper_in_goa') else 'no'}"
    )
    return lines


def _blockquote(text: str, limit: int = 2500) -> str:
    if not text:
        return "> (no abstract available)"
    return "> " + _short(text, limit)


def issue_body(cand: dict[str, Any]) -> str:
    """The full issue body for one candidate, ending with its ledger marker."""
    gene, paper = cand["gene"], cand["paper"]
    ref = paper["reference_id"]
    if cand["action"] == "UPDATE_REVIEW":
        objective = (
            f"Update the review of {gene['symbol']} (`{gene['review_path']}`) with "
            f"{ref}. Read the paper, then revisit the existing annotations and "
            "core functions it bears on: add or modify annotations it supports, and "
            "flag any it refutes."
        )
    else:
        objective = (
            f"Review gene {gene['symbol']} ({gene['organism']}, "
            f"UniProtKB:{gene['accession']}) using {ref}: "
            f"`just fetch-gene {gene['folder']} {gene['symbol']} --uniprot-id {gene['accession']}`, then review its "
            "existing annotations and propose what the paper supports."
        )
    preprint = (
        [
            "",
            "_This is a preprint: it is not peer reviewed and must not be the sole "
            "support for a claim._",
        ]
        if paper.get("is_preprint")
        else []
    )
    lines = [
        "## Paper",
        "",
        f"- {ref}: {paper['title']}",
        f"- Journal/date: {paper.get('journal') or 'n/a'}, {paper.get('publication_date') or 'n/a'}",
        f"- DOI: {paper.get('doi') or 'n/a'}",
        f"- Links: {paper.get('pubmed_url') or 'n/a'} | {paper['europe_pmc_url']}",
        *preprint,
        "",
        "Abstract:",
        "",
        _blockquote(paper.get("abstract", "")),
        "",
        "## Gene",
        "",
        f"- UniProtKB:{gene['accession']} ({gene.get('entry_name') or ''}) "
        f"{gene['symbol']}: {gene.get('protein_name') or 'n/a'}",
        f"- Organism: {gene['organism']} (NCBITaxon:{gene['taxon_id']})",
        f"- Matched as `{gene['matched_symbol']}` in the "
        f"{'title' if gene['matched_in_title'] else 'abstract'}",
        f"- ai-gene-review review: {gene.get('review_path') or 'none'}",
        "",
        "## Gap evidence",
        "",
        *gap_evidence_lines(gene),
        "",
        f"## Score: {cand['score']}",
        "",
        *[f"- {c['points']:+d} {c['label']}" for c in cand["score_components"]],
        "",
        "## Handoff objective",
        "",
        objective,
        "",
        "Question to answer first: does this paper report an experimental function "
        f"(or refute an annotated one) for {gene['symbol']} itself, rather than "
        "mention it in passing?",
        "",
        cand["ledger_marker"],
    ]
    return "\n".join(lines) + "\n"


def render_markdown(packet: dict[str, Any]) -> str:
    """Human/agent-readable packet: queries, ranked candidates, suppressions."""
    eligible = [c for c in packet["candidates"] if c.get("issue_eligible")]
    lines = [
        "# LitScan: Gene-Gap Packet",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Date range: {packet['date_from']} to {packet['date_to']}",
        f"- Preprints included: {packet['include_preprints']}",
        f"- Papers retrieved: {packet['paper_count']}; gene products resolved: "
        f"{packet['resolved_gene_count']}",
        f"- Candidates ranked: {len(packet['candidates'])}; issue-eligible: {len(eligible)}",
        f"- Suppressed: {dict(Counter(s['reason'] for s in packet['suppressed']))}",
        "",
        "Deterministic lead list. Scores come from `conf/litscan/gene_gap.yaml`;",
        "a candidate is a (paper, gene product) pair, and the gene match can be wrong.",
        "",
        "## Queries",
        "",
    ]
    for q in packet["queries"]:
        lines.append(
            f"- `{q['profile']}`: {q['hit_count']} hits, {q['fetched']} fetched"
        )
    lines += [
        "",
        "## Ranked candidates",
        "",
        "| # | score | gene | organism | exp (informative) | family exp members | action | paper | issue |",
        "| ---: | ---: | --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for c in packet["candidates"]:
        gene, paper = c["gene"], c["paper"]
        fam = gene.get("family") or {}
        lines.append(
            f"| {c['rank']} | {c['score']} | {gene['symbol']} ({gene['accession']}) "
            f"| {gene['organism']} | {informative_experimental(gene['annotation_counts'])} "
            f"| {fam.get('experimental_member_count', 'n/a')} | {c['action']} "
            f"| {paper['reference_id']}: {_short(paper['title'], 60)} "
            f"| {'yes' if c.get('issue_eligible') else ''} |"
        )
    lines += ["", "## Issue handoffs", ""]
    for c in eligible:
        lines += [
            f"### {c['rank']}. {c['issue_title']}",
            "",
            f"- Labels: {','.join(c['issue_labels'])}",
            f"- Body file: `{c.get('issue_body_path', '')}`",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def write_packet(packet: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    """Write ``<date>-gene-gap.{json,md}`` and ``issues/<rank>-<acc>.md`` bodies."""
    output_dir.mkdir(parents=True, exist_ok=True)
    issues_dir = output_dir / "issues"
    issues_dir.mkdir(exist_ok=True)
    for stale in issues_dir.glob("*.md"):
        stale.unlink()
    for cand in packet["candidates"]:
        if not cand.get("issue_eligible"):
            continue
        path = issues_dir / f"{cand['rank']:02d}-{cand['gene']['accession']}.md"
        path.write_text(issue_body(cand), encoding="utf-8")
        cand["issue_body_path"] = str(path)
    stamp = packet["date_to"]
    json_path = output_dir / f"{stamp}-{JOB}.json"
    md_path = output_dir / f"{stamp}-{JOB}.md"
    json_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    md_path.write_text(render_markdown(packet), encoding="utf-8")
    return json_path, md_path


SCHEMA = Path(__file__).resolve().parent.parent / "schema" / "litscan_gene_gap.yaml"


def validate_files(paths: Iterable[Path]) -> list[str]:
    """Validate configs (``.yaml``) and packets (``.json``) against the LinkML schema."""
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    validator = Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    problems = []
    for path in paths:
        if path.suffix == ".json":
            data, target = json.loads(path.read_text()), "GeneGapPacket"
        else:
            data, target = yaml.safe_load(path.read_text()), "GeneGapScanConfig"
        problems += [
            f"{path}: {r.message}" for r in validator.validate(data, target).results
        ]
    return problems
