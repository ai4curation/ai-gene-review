#!/usr/bin/env python3
"""Analyze InterPro architecture patterns for membrane-targeting rule design.

This script is parameterized by an InterPro entry accession and writes all
outputs to a caller-provided directory.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

API_BASE = "https://www.ebi.ac.uk/interpro/api"


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "").strip()


def fetch_json(url: str, timeout: int = 30, retries: int = 5, backoff: float = 1.6) -> Any:
    """Fetch JSON with retries for transient API/network issues."""
    delay = 1.0
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                payload = response.read()
            if not payload:
                return None
            return json.loads(payload.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == retries:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries:
                raise
        time.sleep(delay)
        delay *= backoff
    raise RuntimeError(f"Failed to fetch URL after retries: {url}")


def write_tsv(path: Path, headers: list[str], rows: list[list[Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(headers)
        writer.writerows(rows)


def flatten_feature_fragments(feature_obj: dict[str, Any]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    locations = feature_obj.get("locations", [])
    for loc in locations:
        for frag in loc.get("fragments", []):
            start = frag.get("start")
            end = frag.get("end")
            if isinstance(start, int) and isinstance(end, int):
                out.append((start, end))
    return out


def get_entry_metadata(accession: str) -> dict[str, Any]:
    return fetch_json(f"{API_BASE}/entry/interpro/{accession}/")


def get_architectures(accession: str) -> list[dict[str, Any]]:
    data = fetch_json(f"{API_BASE}/entry/interpro/{accession}/?ida")
    return data.get("results", [])


def get_proteins_for_entry(accession: str, page_size: int = 200) -> list[dict[str, Any]]:
    url = (
        f"{API_BASE}/protein/uniprot/entry/interpro/{accession}/"
        f"?page_size={page_size}&extra_fields=sequence,ida,ida_id"
    )
    proteins: list[dict[str, Any]] = []
    while url:
        data = fetch_json(url)
        proteins.extend(data.get("results", []))
        url = data.get("next")
    return proteins


def get_extra_features(accession: str) -> dict[str, Any]:
    data = fetch_json(f"{API_BASE}/protein/uniprot/{accession}/?extra_features")
    if not isinstance(data, dict):
        return {}
    return data


def get_domain_meta(accession: str) -> dict[str, str]:
    source_db = "pfam" if accession.startswith("PF") else "interpro"
    data = fetch_json(f"{API_BASE}/entry/{source_db}/{accession}/")
    meta = data.get("metadata", {})
    name_field = meta.get("name")
    if isinstance(name_field, dict):
        name = name_field.get("name") or name_field.get("short") or accession
    else:
        name = str(name_field or accession)
    description_list = meta.get("description") or []
    description = ""
    if description_list:
        first = description_list[0]
        if isinstance(first, dict):
            description = strip_html(first.get("text", ""))
        else:
            description = strip_html(str(first))
    return {
        "accession": accession,
        "source_db": source_db,
        "name": name,
        "type": str(meta.get("type", "")),
        "description": description,
    }


def nterm_tm_like(
    sequence: str,
    region_end: int = 70,
    window: int = 19,
    hydrophobic_fraction: float = 0.68,
    max_proline: int = 2,
) -> bool:
    """Heuristic N-terminal TM-like segment detector.

    This is a simple sequence heuristic and is not a replacement for TMHMM.
    """
    hydrophobic = set("AILMFWVYCGT")
    seq = sequence[:region_end].upper()
    if len(seq) < window:
        return False
    minimum_hydrophobic = math.ceil(window * hydrophobic_fraction)
    for idx in range(len(seq) - window + 1):
        chunk = seq[idx : idx + window]
        if chunk.count("P") > max_proline:
            continue
        if sum(aa in hydrophobic for aa in chunk) >= minimum_hydrophobic:
            return True
    return False


def tm_like_region_count(
    sequence: str,
    scan_end: int = 120,
    window: int = 19,
    hydrophobic_fraction: float = 0.68,
) -> int:
    hydrophobic = set("AILMFWVYCGT")
    seq = sequence[:scan_end].upper()
    if len(seq) < window:
        return 0
    threshold = math.ceil(window * hydrophobic_fraction)
    candidate_starts: list[int] = []
    for idx in range(len(seq) - window + 1):
        chunk = seq[idx : idx + window]
        if sum(aa in hydrophobic for aa in chunk) >= threshold and chunk.count("P") <= 2:
            candidate_starts.append(idx + 1)
    if not candidate_starts:
        return 0
    regions = 1
    last = candidate_starts[0]
    for pos in candidate_starts[1:]:
        if pos - last > 12:
            regions += 1
        last = pos
    return regions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True, help="InterPro accession (e.g. IPR025280)")
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for TSV/JSON files (created if missing)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=200,
        help="Page size for protein list retrieval (default: 200)",
    )
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    focal_entry = args.entry
    focal_meta = get_entry_metadata(focal_entry).get("metadata", {})
    focal_member_pfams = set((focal_meta.get("member_databases", {}).get("pfam", {}) or {}).keys())

    architectures = get_architectures(focal_entry)
    total_arch_proteins = sum(int(a.get("unique_proteins", 0)) for a in architectures)

    arch_rows: list[list[Any]] = []
    arch_domain_rows: list[list[Any]] = []
    arch_rep_feature_rows: list[list[Any]] = []

    weighted_domain_counts: Counter[str] = Counter()
    domain_arch_count: Counter[str] = Counter()
    domain_first_pos: defaultdict[str, list[int]] = defaultdict(list)
    all_domain_ids: set[str] = set()

    for arch in sorted(architectures, key=lambda x: int(x.get("unique_proteins", 0)), reverse=True):
        ida_id = arch.get("ida_id", "")
        ida = arch.get("ida", "")
        unique_proteins = int(arch.get("unique_proteins", 0))
        representative = arch.get("representative", {}) or {}
        rep_acc = representative.get("accession", "")
        prevalence = (100.0 * unique_proteins / total_arch_proteins) if total_arch_proteins else 0.0
        arch_rows.append([ida_id, ida, unique_proteins, f"{prevalence:.2f}", rep_acc])

        # Representative extra features (TMhelix, signal peptide, etc.)
        feature_payload = get_extra_features(rep_acc) if rep_acc else {}
        feature_keys = sorted(feature_payload.keys())
        tm_ranges = flatten_feature_fragments(feature_payload.get("TMhelix", {}))
        signal_ranges = flatten_feature_fragments(feature_payload.get("SIGNAL_PEPTIDE", {}))
        arch_rep_feature_rows.append(
            [
                ida_id,
                rep_acc,
                len(tm_ranges),
                ";".join(f"{s}-{e}" for s, e in tm_ranges),
                len(signal_ranges),
                ";".join(f"{s}-{e}" for s, e in signal_ranges),
                ",".join(feature_keys),
            ]
        )

        seen_domain_acc: set[str] = set()
        domains = representative.get("domains", []) or []
        for dom in domains:
            domain_acc = dom.get("accession", "")
            if not domain_acc:
                continue
            domain_name = dom.get("name", "")
            all_domain_ids.add(domain_acc)
            locations = dom.get("coordinates", [])
            if locations and isinstance(locations, list):
                first_frag = (
                    locations[0].get("fragments", [{}])[0]
                    if locations[0].get("fragments")
                    else {}
                )
                start = first_frag.get("start")
                end = first_frag.get("end")
            else:
                start, end = None, None

            arch_domain_rows.append([ida_id, domain_acc, domain_name, start, end])
            if isinstance(start, int):
                domain_first_pos[domain_acc].append(start)

            if domain_acc in seen_domain_acc:
                continue
            seen_domain_acc.add(domain_acc)
            domain_arch_count[domain_acc] += 1

            # Exclude focal accessions from "co-occurring feature" counts.
            if domain_acc == focal_entry or domain_acc in focal_member_pfams:
                continue
            weighted_domain_counts[domain_acc] += unique_proteins

    # Domain metadata lookup for all domain IDs observed in representatives.
    domain_meta: dict[str, dict[str, str]] = {}
    for domain_acc in sorted(all_domain_ids):
        domain_meta[domain_acc] = get_domain_meta(domain_acc)

    domain_meta_rows = [
        [
            d["accession"],
            d["source_db"],
            d["name"],
            d["type"],
            d["description"],
        ]
        for d in domain_meta.values()
    ]

    coocc_rows: list[list[Any]] = []
    for domain_acc, weighted in weighted_domain_counts.most_common():
        prevalence = (100.0 * weighted / total_arch_proteins) if total_arch_proteins else 0.0
        meta = domain_meta.get(domain_acc, {})
        mean_start = (
            sum(domain_first_pos[domain_acc]) / len(domain_first_pos[domain_acc])
            if domain_first_pos.get(domain_acc)
            else float("nan")
        )
        coocc_rows.append(
            [
                domain_acc,
                meta.get("source_db", ""),
                meta.get("name", ""),
                meta.get("type", ""),
                weighted,
                f"{prevalence:.2f}",
                domain_arch_count.get(domain_acc, 0),
                f"{mean_start:.1f}" if not math.isnan(mean_start) else "",
            ]
        )

    proteins = get_proteins_for_entry(focal_entry, page_size=args.page_size)
    total_proteins = len(proteins)
    by_ida_total: Counter[str] = Counter()
    by_ida_tm_like: Counter[str] = Counter()
    by_ida_tm_regions: Counter[str] = Counter()
    overall_tm_like = 0
    overall_tm_regions = 0

    for protein in proteins:
        extra = protein.get("extra_fields", {}) or {}
        sequence = extra.get("sequence", "") or ""
        ida_id = extra.get("ida_id", "") or "UNKNOWN"
        by_ida_total[ida_id] += 1
        is_tm_like = nterm_tm_like(sequence)
        tm_regions = tm_like_region_count(sequence)
        if is_tm_like:
            overall_tm_like += 1
            by_ida_tm_like[ida_id] += 1
        overall_tm_regions += tm_regions
        by_ida_tm_regions[ida_id] += tm_regions

    nterm_tm_rows: list[list[Any]] = []
    for ida_id, total in by_ida_total.most_common():
        tm_like = by_ida_tm_like.get(ida_id, 0)
        tm_pct = (100.0 * tm_like / total) if total else 0.0
        avg_tm_regions = by_ida_tm_regions.get(ida_id, 0) / total if total else 0.0
        nterm_tm_rows.append([ida_id, total, tm_like, f"{tm_pct:.2f}", f"{avg_tm_regions:.3f}"])

    overall_tm_pct = (100.0 * overall_tm_like / total_proteins) if total_proteins else 0.0
    overall_avg_tm_regions = (overall_tm_regions / total_proteins) if total_proteins else 0.0

    summary = {
        "entry": focal_entry,
        "entry_name": (focal_meta.get("name", {}) or {}).get("name", focal_entry)
        if isinstance(focal_meta.get("name"), dict)
        else focal_meta.get("name", focal_entry),
        "architectures_count": len(architectures),
        "architectures_total_unique_proteins": total_arch_proteins,
        "proteins_scanned_for_tm_heuristic": total_proteins,
        "nterm_tm_like_count": overall_tm_like,
        "nterm_tm_like_percent": round(overall_tm_pct, 3),
        "average_tm_like_regions_first120aa": round(overall_avg_tm_regions, 4),
    }

    write_tsv(
        out_dir / "architecture_table.tsv",
        ["ida_id", "ida_signature", "unique_proteins", "prevalence_pct", "representative_accession"],
        arch_rows,
    )
    write_tsv(
        out_dir / "architecture_domains.tsv",
        ["ida_id", "domain_accession", "domain_name", "start", "end"],
        arch_domain_rows,
    )
    write_tsv(
        out_dir / "representative_extra_features.tsv",
        [
            "ida_id",
            "representative_accession",
            "tmhelix_count",
            "tmhelix_ranges",
            "signal_peptide_count",
            "signal_peptide_ranges",
            "feature_keys",
        ],
        arch_rep_feature_rows,
    )
    write_tsv(
        out_dir / "domain_metadata.tsv",
        ["accession", "source_db", "name", "type", "description"],
        domain_meta_rows,
    )
    write_tsv(
        out_dir / "cooccurring_domain_weighted.tsv",
        [
            "domain_accession",
            "source_db",
            "name",
            "type",
            "weighted_proteins",
            "weighted_prevalence_pct",
            "architectures_observed",
            "mean_domain_start_in_representatives",
        ],
        coocc_rows,
    )
    write_tsv(
        out_dir / "nterm_tm_heuristic_by_ida.tsv",
        [
            "ida_id",
            "proteins_in_ida",
            "nterm_tm_like_count",
            "nterm_tm_like_pct",
            "avg_tm_like_regions_first120aa",
        ],
        nterm_tm_rows,
    )
    write_tsv(
        out_dir / "nterm_tm_heuristic_overall.tsv",
        [
            "entry",
            "proteins_scanned",
            "nterm_tm_like_count",
            "nterm_tm_like_pct",
            "avg_tm_like_regions_first120aa",
        ],
        [
            [
                focal_entry,
                total_proteins,
                overall_tm_like,
                f"{overall_tm_pct:.2f}",
                f"{overall_avg_tm_regions:.3f}",
            ]
        ],
    )

    with (out_dir / "summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
