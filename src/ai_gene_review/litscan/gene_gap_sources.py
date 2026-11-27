"""Network lookups for the gene-gap scan: Europe PMC text mining, UniProt, QuickGO.

Every function takes a :class:`PoliteClient`, so a scheduled run is rate limited
and retries transient failures. The functions return plain dicts shaped like the
classes in ``schema/litscan_gene_gap.yaml``.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Iterable

from ai_gene_review.evidence import EXPERIMENTAL_EVIDENCE_CODES, source_evidence_code
from ai_gene_review.litscan.polite import PoliteClient

ANNOTATIONS_URL = (
    "https://www.ebi.ac.uk/europepmc/annotations_api/annotationsByArticleIds"
)
UNIPROT_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO_SEARCH_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# Europe PMC's annotations API accepts at most 8 article ids per call.
ANNOTATION_BATCH = 8

UNIPROT_FIELDS = (
    "accession,id,gene_names,protein_name,organism_name,organism_id,"
    "reviewed,xref_panther,xref_pfam,protein_existence"
)

# GO evidence codes that count as experimental, as UniProt query fields.
UNIPROT_EXPERIMENTAL_FIELDS = sorted(
    f"go_{code.lower()}"
    for code in EXPERIMENTAL_EVIDENCE_CODES
    if not code.startswith("ECO:")
)
PROTEIN_BINDING = "GO:0005515"
# Sequence- and ortholog-based transfers: knowledge that exists for a homolog.
HOMOLOGY_EVIDENCE_CODES = frozenset({"ISS", "ISO", "ISA", "ISM"})


def article_id(source: str, record_id: str) -> str:
    """Europe PMC ``SRC:ID`` article id.

    >>> article_id("MED", "123")
    'MED:123'
    """
    return f"{source}:{record_id}"


def _section_kind(section: str) -> str:
    """Reduce Europe PMC's section label to ``title``, ``abstract`` or ``body``.

    >>> _section_kind("Title (http://purl.org/dc/elements/1.1/title)")
    'title'
    >>> _section_kind("Abstract (http://purl.org/dc/terms/abstract)")
    'abstract'
    >>> _section_kind("Results (http://purl.org/orb/Results)")
    'body'
    """
    lowered = section.lower()
    if lowered.startswith("title"):
        return "title"
    if lowered.startswith("abstract"):
        return "abstract"
    return "body"


def fetch_mentions(
    client: PoliteClient, article_ids: Iterable[str]
) -> dict[str, dict[str, list[tuple[str, str]]]]:
    """Gene/protein and organism mentions in each article's title and abstract.

    Returns ``{article_id: {"genes": [(exact, kind)], "organisms": [(taxon, kind)]}}``.
    Europe PMC's UniProt groundings are ignored: they routinely point at another
    species' ortholog, so the scan resolves symbols itself against the species.
    """
    ids = list(dict.fromkeys(article_ids))
    out: dict[str, dict[str, list[tuple[str, str]]]] = {
        i: {"genes": [], "organisms": []} for i in ids
    }
    for start in range(0, len(ids), ANNOTATION_BATCH):
        batch = ids[start : start + ANNOTATION_BATCH]
        response = client.get(
            ANNOTATIONS_URL,
            params=[
                ("articleIds", ",".join(batch)),
                ("type", "Gene_Proteins"),
                ("type", "Organisms"),
                ("section", "title"),
                ("section", "abstract"),
                ("format", "JSON"),
            ],
        )
        for article in response.json():
            key = article_id(article.get("source", ""), article.get("extId", ""))
            if key not in out:
                continue
            for ann in article.get("annotations", []):
                kind = _section_kind(ann.get("section", ""))
                if kind == "body":
                    continue
                if ann.get("type") == "Gene_Proteins":
                    out[key]["genes"].append((ann.get("exact", ""), kind))
                elif ann.get("type") == "Organisms":
                    for tag in ann.get("tags", []):
                        uri = tag.get("uri", "")
                        if "taxonomy/" in uri:
                            out[key]["organisms"].append((uri.rsplit("/", 1)[-1], kind))
    return out


def _uniprot_entry(result: dict[str, Any]) -> dict[str, Any]:
    """Flatten a UniProt REST JSON result into the fields the scan uses."""
    description = result.get("proteinDescription", {})
    name = (
        description.get("recommendedName", {}).get("fullName", {}).get("value")
        or next(
            (
                n.get("fullName", {}).get("value")
                for n in description.get("submissionNames", [])
            ),
            "",
        )
        or ""
    )
    genes = result.get("genes") or [{}]
    symbol = genes[0].get("geneName", {}).get("value", "")
    panther = [
        x
        for x in result.get("uniProtKBCrossReferences", [])
        if x.get("database") == "PANTHER" and ":" not in x.get("id", "")
    ]
    pfam = [
        x
        for x in result.get("uniProtKBCrossReferences", [])
        if x.get("database") == "Pfam"
    ]

    def entry_name(xref: dict[str, Any]) -> str:
        return next(
            (
                p["value"]
                for p in xref.get("properties", [])
                if p.get("key") == "EntryName"
            ),
            "",
        )

    return {
        "accession": result["primaryAccession"],
        "entry_name": result.get("uniProtkbId", ""),
        "symbol": symbol,
        "names": sorted(gene_names(genes)),
        "protein_name": name,
        "organism": result.get("organism", {}).get("scientificName", ""),
        "taxon_id": result.get("organism", {}).get("taxonId"),
        "reviewed": "reviewed" in result.get("entryType", "").lower()
        and "unreviewed" not in result.get("entryType", "").lower(),
        "protein_existence": result.get("proteinExistence", ""),
        "panther_id": panther[0]["id"] if panther else "",
        "panther_name": entry_name(panther[0]) if panther else "",
        "pfam_names": [entry_name(x) for x in pfam],
    }


def gene_names(genes: list[dict[str, Any]]) -> set[str]:
    """Lower-cased gene names, synonyms, locus and ORF names of a UniProt entry.

    >>> sorted(gene_names([{"geneName": {"value": "TP53"},
    ...                     "synonyms": [{"value": "P53"}],
    ...                     "orderedLocusNames": [{"value": "b0001"}]}]))
    ['b0001', 'p53', 'tp53']
    """
    names: set[str] = set()
    for gene in genes:
        if gene.get("geneName"):
            names.add(gene["geneName"]["value"].lower())
        for key in ("synonyms", "orderedLocusNames", "orfNames"):
            names.update(n["value"].lower() for n in gene.get(key, []))
    return names


def choose_entry(
    entries: list[dict[str, Any]], symbol: str, max_hits: int
) -> dict[str, Any] | None:
    """Pick the one UniProt entry a symbol refers to, or ``None`` if ambiguous.

    Reviewed entries win. Among several, an exact primary-symbol match is
    required, and more than ``max_hits`` candidates is ambiguous.

    >>> e = lambda acc, sym, rev: {"accession": acc, "symbol": sym, "reviewed": rev}
    >>> choose_entry([e("P1", "yqcI", True), e("Q1", "yqcI", False)], "yqcI", 3)["accession"]
    'P1'
    >>> choose_entry([e("P1", "ABC1", True), e("P2", "ABC1", True)], "ABC1", 3) is None
    True
    >>> choose_entry([e("Q1", "x", False), e("Q2", "x", False)], "x", 3) is None
    True
    >>> choose_entry([e("Q1", "foo", False)], "foo", 3)["accession"]
    'Q1'
    >>> choose_entry([], "foo", 3) is None
    True
    """
    reviewed = [x for x in entries if x["reviewed"]]
    pool = reviewed or entries
    if not pool:
        return None
    if not reviewed and len(pool) > 1:
        return None
    exact = [x for x in pool if x["symbol"].lower() == symbol.lower()]
    if len(pool) > 1:
        if len(pool) > max_hits or len(exact) != 1:
            return None
        return exact[0]
    return pool[0]


def _uniprot_gene_search(
    client: PoliteClient, symbols: list[str], taxon_id: int | str, extra: str, size: int
) -> list[dict[str, Any]]:
    genes = " OR ".join(f'gene_exact:"{s}"' for s in symbols)
    response = client.get(
        UNIPROT_SEARCH_URL,
        params={
            "query": f"({genes}) AND (organism_id:{taxon_id}){extra}",
            "fields": UNIPROT_FIELDS,
            "format": "json",
            "size": str(size),
        },
    )
    return [_uniprot_entry(r) for r in response.json().get("results", [])]


def resolve_symbol(
    client: PoliteClient, symbol: str, taxon_id: int | str, max_hits: int
) -> dict[str, Any] | None:
    """Resolve one gene symbol in a taxon, reviewed or not."""
    entries = _uniprot_gene_search(client, [symbol], taxon_id, "", max_hits + 1)
    return choose_entry(
        [entry for entry in entries if symbol.lower() in entry["names"]],
        symbol,
        max_hits,
    )


def resolve_symbols(
    client: PoliteClient,
    symbols: list[str],
    taxon_id: int | str,
    max_hits: int,
    *,
    fallback: Iterable[str] = (),
) -> dict[str, dict[str, Any] | None]:
    """Resolve several symbols in one taxon, keyed by lower-cased symbol.

    One batched query covers the reviewed (Swiss-Prot) entries. Symbols in
    ``fallback`` (the paper's title symbols) that it leaves unresolved get a
    per-symbol query that also admits unreviewed entries, since many dark
    genes have only an unreviewed entry.
    """
    if not symbols:
        return {}
    entries = _uniprot_gene_search(
        client, symbols, taxon_id, " AND (reviewed:true)", 100
    )
    out: dict[str, dict[str, Any] | None] = {}
    for symbol in symbols:
        pool = [e for e in entries if symbol.lower() in e["names"]]
        out[symbol.lower()] = choose_entry(pool, symbol, max_hits)
    wanted = {s.lower() for s in fallback}
    for symbol in symbols:
        if out[symbol.lower()] is None and symbol.lower() in wanted:
            out[symbol.lower()] = resolve_symbol(client, symbol, taxon_id, max_hits)
    return out


ANNOTATION_PAGE = 200


def summarize_annotations(results: list[dict[str, Any]]) -> dict[str, int]:
    """Count QuickGO annotation results by evidence class.

    >>> rows = [{"goEvidence": "IDA", "goId": "GO:0005515", "goAspect": "molecular_function"},
    ...         {"goEvidence": "IMP", "goId": "GO:0006915", "goAspect": "biological_process"},
    ...         {"goEvidence": "IBA", "goId": "GO:0016627", "goAspect": "molecular_function"},
    ...         {"goEvidence": "IEA", "goId": "GO:0005737", "goAspect": "cellular_component"},
    ...         {"goEvidence": "ISS", "goId": "GO:0005737", "goAspect": "cellular_component"}]
    >>> summarize_annotations(rows)["experimental"], summarize_annotations(rows)["other"]
    (2, 0)
    >>> summarize_annotations(rows)["experimental_protein_binding"]
    1
    >>> summarize_annotations(rows)["homology"], summarize_annotations(rows)["experimental_aspects"]
    (1, 1)
    """
    experimental = [
        r
        for r in results
        if source_evidence_code(r.get("goEvidence"), r.get("evidenceCode"))
        in EXPERIMENTAL_EVIDENCE_CODES
    ]
    counts = {
        "total": len(results),
        "experimental": len(experimental),
        "experimental_protein_binding": sum(
            r.get("goId") == PROTEIN_BINDING for r in experimental
        ),
        "experimental_mf": sum(
            r.get("goAspect") == "molecular_function" for r in experimental
        ),
        "experimental_aspects": len(
            {
                r["goAspect"]
                for r in experimental
                if r.get("goAspect") and r.get("goId") != PROTEIN_BINDING
            }
        ),
        "iba": sum(r.get("goEvidence") == "IBA" for r in results),
        "iea": sum(r.get("goEvidence") == "IEA" for r in results),
        # Bare protein binding is as uninformative by ISS as by IPI.
        "homology": sum(
            source_evidence_code(r.get("goEvidence"), r.get("evidenceCode"))
            in HOMOLOGY_EVIDENCE_CODES
            and r.get("goId") != PROTEIN_BINDING
            for r in results
        ),
    }
    counts["other"] = counts["total"] - (
        counts["experimental"] + counts["iba"] + counts["iea"] + counts["homology"]
    )
    return counts


@dataclass
class AnnotationProfile:
    counts: dict[str, int]
    evidence_codes: dict[str, int]
    references: set[str]


def annotation_profile(client: PoliteClient, accession: str) -> AnnotationProfile:
    """Count the same QuickGO rows for every product, preserving source evidence codes."""
    params = {"geneProductId": accession, "limit": str(ANNOTATION_PAGE)}
    rows = []
    total = 0
    page = 1
    while True:
        payload = client.get(
            QUICKGO_SEARCH_URL, params=params, headers={"Accept": "application/json"}
        ).json()
        total = max(total, int(payload["numberOfHits"]))
        rows.extend(payload["results"])
        if len(rows) >= total:
            break
        if not payload["results"]:
            raise ValueError(
                f"Incomplete QuickGO response for {accession}: {len(rows)} of {total} rows"
            )
        page += 1
        params["page"] = str(page)
    codes = Counter(
        source_evidence_code(r.get("goEvidence"), r.get("evidenceCode")) for r in rows
    )
    return AnnotationProfile(
        summarize_annotations(rows),
        dict(sorted(codes.items())),
        {r["reference"] for r in rows},
    )


def _uniprot_total(client: PoliteClient, query: str) -> int:
    response = client.get(
        UNIPROT_SEARCH_URL, params={"query": query, "size": "0", "format": "json"}
    )
    return int(response.headers["X-Total-Results"])


def family_status(
    client: PoliteClient, panther_id: str, panther_name: str = ""
) -> dict[str, Any]:
    """Members of a PANTHER family in UniProtKB, and how many have experimental GO."""
    family = f"xref:panther-{panther_id}"
    experimental = " OR ".join(f"{f}:*" for f in UNIPROT_EXPERIMENTAL_FIELDS)
    return {
        "panther_id": panther_id,
        "panther_name": panther_name,
        "member_count": _uniprot_total(client, family),
        "experimental_member_count": _uniprot_total(
            client, f"({family}) AND ({experimental})"
        ),
    }
