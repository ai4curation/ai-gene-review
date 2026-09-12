"""Job C: module-member discovery scan.

For each curated module, query Europe PMC for recent papers about that module's
distinctive topic, flag whether each paper is already cited in the module's
evidence, and surface membership-novelty sentences. The packet is a lead list
for downstream triage (e.g. a haiku filter that decides which papers actually
propose a new member); this scan never edits a module.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any

from ai_gene_review.litscan import europepmc
from ai_gene_review.litscan.module_index import ModuleEntity, load_modules
from ai_gene_review.litscan.scoring import (
    MEMBERSHIP_SIGNALS,
    build_query,
    extract_signal_sentences,
    select_query_terms,
)


def default_date_range(days: int) -> tuple[str, str]:
    today = dt.datetime.now(dt.timezone.utc).date()
    return (today - dt.timedelta(days=days)).isoformat(), today.isoformat()


def _signal_score(signals: list[dict[str, Any]]) -> int:
    return sum(len(s.get("categories", [])) for s in signals)


def scan_module(
    entity: ModuleEntity,
    date_from: str,
    date_to: str,
    *,
    max_records: int,
    max_terms: int,
    timeout: float,
) -> dict[str, Any]:
    """Scan one module and return its query, hit count, and ranked records."""
    chosen_terms = select_query_terms(entity.terms, max_terms=max_terms)
    query = build_query(chosen_terms, date_from, date_to)
    hit_count, publications = europepmc.search(
        query, max_records=max_records, timeout=timeout
    )
    records: list[dict[str, Any]] = []
    for pub in publications:
        signals = extract_signal_sentences(
            f"{pub.title}. {pub.abstract}", MEMBERSHIP_SIGNALS
        )
        records.append(
            {
                "pmid": pub.pmid,
                "doi": pub.doi,
                "title": pub.title,
                "journal": pub.journal,
                "publication_date": pub.publication_date,
                "authors": pub.authors,
                "pubmed_url": pub.pubmed_url,
                "europe_pmc_url": pub.europe_pmc_url,
                "abstract": pub.abstract,
                "already_cited": pub.reference_id in entity.cited_pmids,
                "membership_score": _signal_score(signals),
                "membership_signals": signals,
            }
        )
    # new (not-yet-cited) first, then strongest membership signal, then newest.
    # europepmc.search returns newest-first (sort="P_PDATE_D desc"); Python's sort
    # is stable, so omitting publication_date from the key preserves that order.
    records.sort(key=lambda r: (r["already_cited"], -int(r["membership_score"])))
    return {
        "module_id": entity.id,
        "module_title": entity.title,
        "module_path": entity.path,
        "query": query,
        "query_terms": chosen_terms,
        "hit_count": hit_count,
        "cited_pmid_count": len(entity.cited_pmids),
        "record_count": len(records),
        "records": records,
    }


def run(
    modules_dir: Path,
    *,
    days: int = 90,
    date_from: str = "",
    date_to: str = "",
    max_records: int = 40,
    max_terms: int = 10,
    timeout: float = 30.0,
) -> dict[str, Any]:
    """Run the module-member scan over every module and return a packet dict."""
    if date_from and date_to:
        start, end = date_from, date_to
    else:
        start, end = default_date_range(days)

    entities = load_modules(modules_dir)
    modules = [
        scan_module(
            e, start, end, max_records=max_records, max_terms=max_terms, timeout=timeout
        )
        for e in entities
    ]
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "job": "module-member",
        "date_from": start,
        "date_to": end,
        "module_count": len(modules),
        "total_records": sum(m["record_count"] for m in modules),
        "modules": modules,
    }


def _blockquote(text: str, *, max_chars: int = 1200) -> str:
    if not text:
        return "> (no abstract available)"
    snippet = text[:max_chars].rstrip()
    if len(text) > max_chars:
        snippet += " …"
    return "> " + snippet


def render_markdown(packet: dict[str, Any]) -> str:
    """Render a per-record packet with everything an issue handoff needs verbatim."""
    lines = [
        "# LitScan: Module-Member Discovery Packet",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Date range: {packet['date_from']} to {packet['date_to']}",
        f"- Modules scanned: {packet['module_count']}",
        f"- Total candidate papers: {packet['total_records']}",
        "",
        "Deterministic high-recall lead list. `[NEW]` = not yet cited in the module's",
        "evidence. Most records are false positives; triage before acting.",
        "",
    ]
    for module in packet["modules"]:
        new_count = sum(1 for r in module["records"] if not r["already_cited"])
        lines += [
            f"## {module['module_title']} (`{module['module_id']}`)",
            "",
            f"- Module file: `{module['module_path']}`",
            f"- Europe PMC hits: {module['hit_count']}; in packet: "
            f"{module['record_count']} ({new_count} not yet cited)",
            f"- Query terms: {', '.join(module['query_terms'])}",
            "",
        ]
        if not module["records"]:
            lines += ["_No records._", ""]
            continue
        for rec in module["records"]:
            flag = "NEW" if not rec["already_cited"] else "cited"
            pmid = f"PMID:{rec['pmid']}" if rec["pmid"] else "(no PMID)"
            lines += [
                f"### [{flag}] {pmid} — {rec['title']}",
                "",
                f"- Date: {rec['publication_date']} | Journal: {rec['journal']} "
                f"| DOI: {rec['doi'] or '(none)'}",
                f"- PubMed: {rec['pubmed_url'] or '(none)'} | "
                f"Europe PMC: {rec.get('europe_pmc_url') or '(none)'}",
                f"- Membership score: {rec['membership_score']}",
                "",
            ]
            if rec["membership_signals"]:
                lines.append("Membership signals:")
                for sig in rec["membership_signals"]:
                    cats = ", ".join(sig["categories"])
                    lines.append(f"- [{cats}] {sig['sentence']}")
                lines.append("")
            lines += ["Abstract:", "", _blockquote(rec["abstract"]), ""]
    return "\n".join(lines).rstrip() + "\n"


def write_packet(packet: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = packet["date_to"]
    json_path = output_dir / f"{stamp}-module-member.json"
    md_path = output_dir / f"{stamp}-module-member.md"
    json_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    md_path.write_text(render_markdown(packet), encoding="utf-8")
    return json_path, md_path
