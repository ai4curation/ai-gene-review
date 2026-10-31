"""Audit local Swiss-Prot reviews outside their exact taxon's reference proteomes.

Run with ``python -m ai_gene_review.analysis.orphan_curated --help``. Membership
comes from release-stamped UniProt API responses, never from the absence of a
keyword in an old local flat file. GO statistics describe cached source GOA rows,
not reviewer proposals. This audit does not establish loss of biological genes.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timedelta, timezone
import hashlib
import html
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import yaml


API = "https://rest.uniprot.org"
REVIEWED = "UniProtKB reviewed (Swiss-Prot)"
EXPERIMENTAL = frozenset("EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP".split())
EVIDENCE_CODES = "EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP IBA IBD IKR IRD ISS ISO ISA ISM IGC RCA TAS NAS IC ND IEA".split()
REPO_URL = "https://github.com/ai4curation/ai-gene-review/blob/main/"
ENTRY_FIELDS = "accession,id,reviewed,gene_names,protein_name,organism_id,organism_name,xref_proteomes"


def discover_reviews(root: Path, species: str | None = None) -> dict[str, list[dict]]:
    """Index primary review YAML files by accession, retaining duplicate paths."""
    reviews: dict[str, list[dict]] = defaultdict(list)
    directory = root / "genes"
    paths = (
        (directory / species).glob("*/*-ai-review.yaml")
        if species
        else directory.glob("*/*/*-ai-review.yaml")
    )
    for path in sorted(paths):
        data = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if (
            not isinstance(data, dict)
            or not data.get("id")
            or not (data.get("taxon") or {}).get("id")
        ):
            raise ValueError(f"Missing accession or taxon in {path}")
        original_id = str(data["id"])
        accession = original_id.removeprefix("UniProtKB:")
        if "_" in accession and not accession.startswith("URS"):
            flatfile = path.with_name(
                path.name.replace("-ai-review.yaml", "-uniprot.txt")
            )
            if flatfile.exists():
                text = flatfile.read_text()
                entry_name = re.search(r"^ID\s+(\S+)", text, re.MULTILINE)
                primary = re.search(r"^AC\s+([A-Z0-9]+);", text, re.MULTILINE)
                if entry_name and primary and entry_name[1] == accession:
                    accession = primary[1]
        reviews[accession].append(
            {
                "path": path.relative_to(root).as_posix(),
                "species": path.parent.parent.name,
                "gene": data.get("gene_symbol", path.parent.name),
                "original_id": original_id,
                "taxon": int(str(data["taxon"]["id"]).removeprefix("NCBITaxon:")),
            }
        )
    if not reviews:
        raise ValueError(
            f"No gene reviews found under {directory} (species={species!r})"
        )
    return dict(reviews)


class UniProtClient:
    """Paginated, retrying API client with dated query caches and offline replay."""

    def __init__(self, cache: Path, *, refresh: bool = False, offline: bool = False):
        self.cache = cache
        self.refresh = refresh
        self.offline = offline
        self.sources: list[dict] = []

    def search(
        self, endpoint: str, query: str, fields: str | None = None
    ) -> list[dict]:
        """Fetch a complete query or fail; partial results are never cached."""
        params = {"query": query, "format": "json", "size": "500"}
        if fields:
            params["fields"] = fields
        url = f"{API}/{endpoint}/search?{urlencode(params)}"
        key = hashlib.sha256(url.encode()).hexdigest()
        path = self.cache / f"{key}.json"
        cached = json.loads(path.read_text()) if path.exists() else None
        now = datetime.now(timezone.utc)
        if (
            cached
            and not self.refresh
            and (
                self.offline
                or now - datetime.fromisoformat(cached["fetched_at"])
                < timedelta(days=7)
            )
        ):
            self.sources.append({k: v for k, v in cached.items() if k != "results"})
            return cached["results"]
        if self.offline:
            raise ValueError(f"Offline cache missing for {endpoint} query: {query}")
        results: list[dict] = []
        releases: set[str] = set()
        next_url: str | None = url
        seen: set[str] = set()
        expected = None
        with requests.Session() as session:
            session.mount(
                "https://",
                HTTPAdapter(
                    max_retries=Retry(
                        total=4,
                        backoff_factor=1,
                        status_forcelist=[429, 500, 502, 503, 504],
                    )
                ),
            )
            while next_url:
                if next_url in seen or not next_url.startswith(API + "/"):
                    raise ValueError(f"Invalid pagination URL: {next_url}")
                seen.add(next_url)
                response = session.get(next_url, timeout=60)
                response.raise_for_status()
                if expected is None:
                    expected = int(response.headers["x-total-results"])
                releases.add(response.headers["x-uniprot-release"])
                results.extend(response.json()["results"])
                next_url = response.links.get("next", {}).get("url")
        if len(results) != expected or len(releases) != 1:
            raise ValueError(f"Incomplete or mixed-release UniProt response for {url}")
        payload = {
            "url": url,
            "fetched_at": now.isoformat(),
            "release": releases.pop(),
            "results": results,
        }
        self.cache.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(payload))
        temporary.replace(path)
        self.sources.append({k: v for k, v in payload.items() if k != "results"})
        return results


def fetch_batches(
    client: UniProtClient,
    endpoint: str,
    values: list,
    field: str,
    *,
    reference: bool = False,
) -> list[dict]:
    """Query bounded OR batches with four workers, preserving pagination."""
    queries = [
        "(" + " OR ".join(f"{field}:{v}" for v in values[i : i + 50]) + ")"
        for i in range(0, len(values), 50)
    ]
    if reference:
        queries = ["reference:true AND " + q for q in queries]
    print(
        f"Fetching {endpoint}: {len(values)} identifiers in {len(queries)} batches",
        file=sys.stderr,
    )

    def fetch(query: str) -> list[dict]:
        return client.search(
            endpoint, query, ENTRY_FIELDS if endpoint == "uniprotkb" else None
        )

    with ThreadPoolExecutor(max_workers=4) as pool:
        return [record for records in pool.map(fetch, queries) for record in records]


def goa_counts(
    accession: str, reviews: list[dict], root: Path, diagnostics: list[str]
) -> dict:
    """Union identical source rows across duplicate caches; retain all evidence."""
    rows: dict[tuple, dict] = {}
    sources = []
    missing = 0
    for review in reviews:
        path = root / review["path"].replace("-ai-review.yaml", "-goa.tsv")
        if not path.exists():
            missing += 1
            diagnostics.append(
                f"{accession}: missing GOA cache {path.relative_to(root)}"
            )
            continue
        raw_content = path.read_bytes()
        content = raw_content.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(content), delimiter="\t")
        required = {"GENE PRODUCT ID", "GO TERM", "GO EVIDENCE CODE", "QUALIFIER"}
        if not required.issubset(reader.fieldnames or []):
            missing += 1
            diagnostics.append(
                f"{accession}: invalid/empty GOA cache {path.relative_to(root)}"
            )
            continue
        sources.append(
            {
                "path": path.relative_to(root).as_posix(),
                "sha256": hashlib.sha256(raw_content).hexdigest(),
            }
        )
        other_ids = set()
        for row in reader:
            product = row["GENE PRODUCT ID"].removeprefix("UniProtKB:")
            if product != accession and not product.startswith(accession + "-"):
                other_ids.add(product)
                continue
            if (
                not row.get("GO TERM")
                or not row.get("GO EVIDENCE CODE")
                or None in row
                or any(v is None for v in row.values())
            ):
                raise ValueError(f"Malformed GOA row in {path}: {row}")
            rows[tuple(sorted(row.items()))] = row
        if other_ids:
            diagnostics.append(
                f"{accession}: ignored foreign GOA products in {path.relative_to(root)}: {', '.join(sorted(other_ids))}"
            )
    counts = Counter(row["GO EVIDENCE CODE"] for row in rows.values())
    dates = sorted(row["DATE"] for row in rows.values() if row.get("DATE"))
    known = bool(sources)
    return {
        "goa_status": ("partial" if missing else "available") if known else "missing",
        "goa_sources": sources,
        "goa_rows": len(rows) if known else None,
        "go_terms": len({row["GO TERM"] for row in rows.values()}) if known else None,
        "non_iea_rows": sum(v for k, v in counts.items() if k != "IEA")
        if known
        else None,
        "experimental_rows": sum(v for k, v in counts.items() if k in EXPERIMENTAL)
        if known
        else None,
        "not_rows": sum(
            "NOT" in re.split(r"[|, ]+", row["QUALIFIER"]) for row in rows.values()
        )
        if known
        else None,
        "evidence_counts": dict(sorted(counts.items())),
        "goa_date_min": dates[0] if dates else "",
        "goa_date_max": dates[-1] if dates else "",
    }


def build_report(
    reviews: dict[str, list[dict]],
    entries: list[dict],
    references: dict[int, set[str]],
    root: Path,
) -> dict:
    """Classify each unique local accession using live taxonomy and membership."""
    by_id = {e["primaryAccession"]: e for e in entries}
    scope = dict.fromkeys(
        [
            "review_files",
            "accessions",
            "swissprot",
            "unreviewed",
            "unresolved",
            "non_protein",
            "no_exact_taxon_reference",
            "in_reference_proteome",
        ],
        0,
    )
    scope.update(review_files=sum(map(len, reviews.values())), accessions=len(reviews))
    candidates = []
    diagnostics: list[str] = []
    for accession, local in sorted(reviews.items()):
        if accession.startswith("URS") or accession.startswith("RNAcentral:"):
            scope["non_protein"] += 1
            continue
        for record in local:
            if record["original_id"].removeprefix("UniProtKB:") != accession:
                diagnostics.append(
                    f"{record['path']}: resolved local entry name {record['original_id']} to {accession} using its matching cached UniProt ID/AC lines."
                )
        entry = by_id.get(accession)
        if entry is None:
            scope["unresolved"] += 1
            diagnostics.append(
                f"{accession}: not returned as a primary accession; check deletion, merge, secondary accession or isoform. Membership unknown."
            )
            continue
        if entry["entryType"] != REVIEWED:
            scope["unreviewed"] += 1
            continue
        scope["swissprot"] += 1
        taxon = entry["organism"]["taxonId"]
        local_taxa = {r["taxon"] for r in local}
        if local_taxa != {taxon}:
            diagnostics.append(
                f"{accession}: local taxon(s) {sorted(local_taxa)} disagree with live taxon {taxon}; live taxonomy used."
            )
        reference_ids = references.get(taxon, set())
        if not reference_ids:
            scope["no_exact_taxon_reference"] += 1
            continue
        proteomes = {
            r["id"]
            for r in entry.get("uniProtKBCrossReferences", [])
            if r["database"] == "Proteomes"
        }
        if proteomes & reference_ids:
            scope["in_reference_proteome"] += 1
            continue
        description = entry.get("proteinDescription", {})
        name: dict = description.get("recommendedName") or next(
            iter(description.get("submissionNames", [])), {}
        )
        candidates.append(
            {
                "accession": accession,
                "gene": "; ".join(sorted({r["gene"] for r in local})),
                "species": "; ".join(sorted({r["species"] for r in local})),
                "taxon_id": taxon,
                "organism": entry["organism"]["scientificName"],
                "protein": name.get("fullName", {}).get("value", ""),
                "reference_proteomes": sorted(reference_ids),
                "entry_proteomes": sorted(proteomes),
                "review_paths": [r["path"] for r in local],
                "local_ids": sorted({r["original_id"] for r in local}),
                **goa_counts(accession, local, root, diagnostics),
            }
        )
    return {"scope": scope, "candidates": candidates, "diagnostics": diagnostics}


def render_csv(report: dict) -> str:
    """One row per candidate, with evidence columns and provenance for reuse."""
    rows = report["candidates"]
    codes = sorted(
        set(EVIDENCE_CODES) | {c for r in rows for c in r["evidence_counts"]}
    )
    fields = [
        "accession",
        "gene",
        "species",
        "taxon_id",
        "organism",
        "protein",
        "reference_proteomes",
        "entry_proteomes",
        "goa_status",
        "goa_rows",
        "go_terms",
        "non_iea_rows",
        "experimental_rows",
        "not_rows",
        "goa_date_min",
        "goa_date_max",
        *[f"goa_{c}" for c in codes],
        "review_paths",
        "local_ids",
        "goa_sources",
        "generated_at",
        "uniprot_releases",
        "uniprot_fetched_at_min",
        "uniprot_fetched_at_max",
    ]
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    sources = report.get("sources", [])
    dates = sorted(s["fetched_at"] for s in sources)
    for row in rows:
        data = {k: v for k, v in row.items() if k in fields}
        for key in [
            "reference_proteomes",
            "entry_proteomes",
            "review_paths",
            "local_ids",
        ]:
            data[key] = ";".join(data[key])
        data["goa_sources"] = json.dumps(data["goa_sources"], sort_keys=True)
        data.update(
            {
                f"goa_{c}": row["evidence_counts"].get(c, 0)
                if row["goa_rows"] is not None
                else None
                for c in codes
            }
        )
        data.update(
            generated_at=report["generated_at"],
            uniprot_releases=";".join(sorted({s["release"] for s in sources})),
            uniprot_fetched_at_min=dates[0] if dates else "",
            uniprot_fetched_at_max=dates[-1] if dates else "",
        )
        writer.writerow(data)
    return output.getvalue()


def cell(value: object) -> str:
    """Escape untrusted labels for a GitHub Markdown table."""
    return (
        html.escape(str(value))
        .replace("|", "&#124;")
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("[", "&#91;")
        .replace("]", "&#93;")
    )


def render_markdown(report: dict) -> str:
    """Issue-ready report with linked entries, evidence totals, and limitations."""
    rows, scope = report["candidates"], report["scope"]
    counts: Counter[str] = Counter()
    for row in rows:
        counts.update(row["evidence_counts"])
    available = sum(r["goa_status"] != "missing" for r in rows)
    total = sum(counts.values())
    sources = report.get("sources", [])
    dates = sorted(s["fetched_at"] for s in sources)
    lines = [
        "# Curated entries outside their reference proteomes",
        "",
        f"Generated: {report['generated_at']}. Scope: {report['selection']}.",
        "",
        "Select **live Swiss-Prot accessions** in our local gene-review set whose **exact NCBI taxon** has a UniProt reference proteome, but whose accession belongs to none of those reference proteomes. All local review statuses, including drafts, are included; duplicate accessions are counted once.",
        "",
        "## Summary",
        "",
        f"- Local review files: **{scope['review_files']:,}**; unique identifiers: **{scope['accessions']:,}**.",
        f"- Live Swiss-Prot: **{scope['swissprot']:,}**; unreviewed: **{scope['unreviewed']:,}**; unresolved accessions: **{scope['unresolved']:,}**.",
        f"- RNAcentral/non-protein identifiers: **{scope['non_protein']:,}** (excluded from Swiss-Prot audit).",
        f"- Swiss-Prot already in an exact-taxon reference proteome: **{scope['in_reference_proteome']:,}**.",
        f"- Swiss-Prot with no exact-taxon reference proteome: **{scope['no_exact_taxon_reference']:,}** (excluded; this can be expected for non-reference species/strains).",
        f"- **Candidates: {len(rows):,} accessions across {len({r['taxon_id'] for r in rows}):,} taxa.**",
        f"- Local GOA available for **{available}/{len(rows)}** candidates; **{sum(r['goa_status'] == 'partial' for r in rows)}** have partial cache coverage.",
        f"- Cached GOA rows: **{total:,}**, including **{total - counts['IEA']:,} non-IEA**, **{sum(counts[c] for c in EXPERIMENTAL):,} experimental**, and **{sum(r['not_rows'] or 0 for r in rows):,} NOT** rows.",
        "",
        "## GO evidence on candidate accessions",
        "",
        "These are original cached GOA annotation rows, regardless of our review decisions. Reviewer-proposed NEW annotations are excluded. Exact duplicate rows across caches are counted once per accession. Non-IEA is not synonymous with experimental; IBA remains separately visible as phylogenetic curation. Missing caches are unknown, not zero.",
        "",
        "| Evidence code | Annotation rows |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {code} | {count} |" for code, count in sorted(counts.items()))
    if not counts:
        lines.append("| No available annotation rows | 0 |")
    lines += [
        "",
        "## Candidate entries",
        "",
        "| Accession | Local gene | Organism | Protein | Reference proteome(s) | Other proteome membership | GOA rows | Non-IEA | Experimental | Evidence counts | Links |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        accession = row["accession"]
        refs = ", ".join(
            f"[{p}](https://www.uniprot.org/proteomes/{p})"
            for p in row["reference_proteomes"]
        )
        others = (
            ", ".join(
                f"[{p}](https://www.uniprot.org/proteomes/{p})"
                for p in row["entry_proteomes"]
            )
            or "None"
        )
        links = [
            f"[GOA](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3A{accession})"
        ]
        local_genes = "; ".join(
            f"[{cell(Path(p).parts[1])}/{cell(Path(p).parts[2])}]({REPO_URL}{quote(p)})"
            for p in row["review_paths"]
        )
        values = [
            f"[{accession}](https://www.uniprot.org/uniprotkb/{accession}/entry)",
            local_genes,
            f"[{cell(row['organism'])}](https://www.uniprot.org/taxonomy/{row['taxon_id']})",
            cell(row["protein"]),
            refs,
            others,
            *[
                str(row[k]) if row[k] is not None else "unknown"
                for k in ["goa_rows", "non_iea_rows", "experimental_rows"]
            ],
            cell(
                "; ".join(f"{k}: {v}" for k, v in row["evidence_counts"].items())
                or ("unknown" if row["goa_rows"] is None else "none")
            ),
            "; ".join(links),
        ]
        lines.append("| " + " | ".join(values) + " |")
    lines += [
        "",
        "## Interpretation and requested follow-up",
        "",
        "Please check whether these curated accessions should be linked to the reference proteome, or whether another accession represents the same locus/sequence. If a TrEMBL counterpart exists, assess sequence equivalence and preservation of experimentally supported and other non-IEA GO annotations before changing the accession used in our reviews.",
        "",
        "Absence of an accession does **not** establish absence of its gene, sequence, or GO annotations from the reference proteome, and does not imply planned deletion from Swiss-Prot. This report has not mapped alternative accessions or measured unique annotation loss. Different strains and descendant taxa are not treated as the same taxon.",
        "",
        "## Provenance",
        "",
        f"UniProt release(s): {', '.join(sorted({s['release'] for s in sources})) or 'not recorded'}. API retrieval range: {dates[0] if dates else 'not recorded'} to {dates[-1] if dates else 'not recorded'}.",
        "",
        "Membership uses the UniProtKB Proteomes cross-references and the Proteomes API's reference classification. API query caches expire after seven days; `--refresh` fetches anew and `--offline` reuses dated caches. Network/pagination failures abort instead of inferring absence. The CSV records GOA source paths and SHA-256 hashes; annotation dates below are GOA DATE values, not download timestamps.",
        "",
        "| Accession | Local GOA source | GOA annotation date range | Cache status |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        source_links = (
            "; ".join(
                f"[{cell(s['path'])}]({REPO_URL}{quote(s['path'])})"
                for s in row["goa_sources"]
            )
            or "Missing"
        )
        lines.append(
            f"| {row['accession']} | {source_links} | {row['goa_date_min']}–{row['goa_date_max']} | {row['goa_status']} |"
        )
    if report["diagnostics"]:
        lines += ["", "## Data diagnostics", ""]
        lines += [f"- {cell(d)}" for d in report["diagnostics"]]
    return "\n".join(lines) + "\n"


def main() -> None:
    """Generate CSV, Markdown, or both without modifying cached gene sources."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    parser.add_argument(
        "--species", help="Restrict to one local species directory, e.g. POPTR"
    )
    parser.add_argument("--format", choices=["csv", "markdown", "both"], default="both")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("projects/ORPHAN_CURATED/reports")
    )
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/orphan-curated"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--refresh", action="store_true", help="Refresh all API query caches"
    )
    mode.add_argument(
        "--offline",
        action="store_true",
        help="Use existing API caches only, even if older than seven days",
    )
    args = parser.parse_args()
    if args.species and (
        Path(args.species).name != args.species or args.species in {".", ".."}
    ):
        parser.error("--species must be a single directory name")
    root = args.root.resolve()
    print(f"Reading local reviews under {root / 'genes'}", file=sys.stderr)
    reviews = discover_reviews(root, args.species)
    client = UniProtClient(
        root / args.cache_dir, refresh=args.refresh, offline=args.offline
    )
    accessions = [
        a
        for a in sorted(reviews)
        if not a.startswith("URS") and re.fullmatch(r"[A-Z0-9]+(?:-[0-9]+)?", a)
    ]
    entries = fetch_batches(client, "uniprotkb", accessions, "accession")
    taxa = sorted(
        {e["organism"]["taxonId"] for e in entries if e["entryType"] == REVIEWED}
    )
    proteomes = fetch_batches(client, "proteomes", taxa, "taxonomy_id", reference=True)
    references: dict[int, set[str]] = defaultdict(set)
    for proteome in proteomes:
        if proteome["proteomeType"] == "Reference proteome":
            references[proteome["taxonomy"]["taxonId"]].add(proteome["id"])
    if len({s["release"] for s in client.sources}) > 1:
        raise ValueError("Mixed UniProt releases in API caches; rerun with --refresh")
    report = build_report(reviews, entries, references, root)
    report.update(
        generated_at=datetime.now(timezone.utc).isoformat(),
        sources=sorted(client.sources, key=lambda s: s["url"]),
        selection=f"genes/{args.species}"
        if args.species
        else "all repository gene reviews",
    )
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    for fmt, suffix, renderer in [
        ("csv", "csv", render_csv),
        ("markdown", "md", render_markdown),
    ]:
        if args.format in {fmt, "both"}:
            path = output / f"orphan-curated.{suffix}"
            temporary = path.with_suffix(path.suffix + ".tmp")
            temporary.write_text(renderer(report))
            temporary.replace(path)
            print(f"Wrote {path}", file=sys.stderr)
    print(
        f"{len(report['candidates'])} candidates; {len(report['diagnostics'])} diagnostics",
        file=sys.stderr,
    )
    for diagnostic in report["diagnostics"]:
        print(diagnostic, file=sys.stderr)


if __name__ == "__main__":
    main()
