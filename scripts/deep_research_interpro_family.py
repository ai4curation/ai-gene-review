#!/usr/bin/env python3
"""Wrapper for deep-research-client to research an InterPro entry (family/domain).

This is the InterPro-family analogue of ``scripts/deep_research_wrapper.py`` (which
researches a gene). It:

1. Ensures the InterPro entry metadata is cached under
   ``interpro/<database>/<ID>/<ID>-metadata.yaml`` (fetching it via the existing
   ``fetch_interpro_family_simple`` fetcher if absent).
2. Loads that metadata as research context (name, type, InterPro2GO terms, member
   databases, description, scale).
3. Calls ``deep-research-client research`` with the
   ``templates/interpro_family_research.md`` prompt template, writing the report to
   ``interpro/<database>/<ID>/<ID>-deep-research-<provider>.md``.

Usage::

    python scripts/deep_research_interpro_family.py IPR000719            # falcon (Edison), the default
    python scripts/deep_research_interpro_family.py PTHR10314 openai --database panther

Normally invoked through the ``just deep-research-interpro-family`` recipe.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Optional

import yaml

# Edison (falcon) family research routinely runs 10-15 min; keep a generous default.
DEFAULT_TIMEOUT = 1800
TEMPLATE = "templates/interpro_family_research.md"


def _strip_html(text: str) -> str:
    """Cheap tag/whitespace strip for InterPro description blocks."""
    import re

    text = re.sub(r"\[\[cite:[^\]]+\]\]", "", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_family_context(metadata_path: Path) -> dict:
    """Extract template variables from a cached InterPro entry metadata YAML.

    Args:
        metadata_path: Path to ``<ID>-metadata.yaml``.

    Returns:
        Dict of template variables (all string-valued, never empty).

    Examples:
        >>> import tempfile, yaml, pathlib
        >>> doc = {'metadata': {'accession': 'IPR000719',
        ...   'type': 'domain',
        ...   'name': {'name': 'Protein kinase domain', 'short': 'Prot_kinase_dom'},
        ...   'integrated': None,
        ...   'go_terms': [{'identifier': 'GO:0005524', 'name': 'ATP binding',
        ...                 'category': {'code': 'F'}}],
        ...   'member_databases': {'pfam': {'PF00069': 'Protein kinase domain'}},
        ...   'counters': {'proteins': 100, 'taxa': 40, 'subfamilies': 0},
        ...   'description': [{'text': '<p>The protein kinase domain.</p>'}]}}
        >>> p = pathlib.Path(tempfile.mkdtemp()) / 'IPR000719-metadata.yaml'
        >>> _ = p.write_text(yaml.dump(doc))
        >>> ctx = load_family_context(p)
        >>> ctx['interpro_type']
        'domain'
        >>> 'GO:0005524 ATP binding [F]' in ctx['interpro2go_terms']
        True
        >>> 'PF00069' in ctx['member_databases']
        True
    """
    with metadata_path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    md = data.get("metadata", {}) or {}

    name_info = md.get("name") or {}
    name = name_info.get("name") or md.get("accession") or "Unknown"
    short = name_info.get("short") or "Not specified"

    go_terms = md.get("go_terms") or []
    if go_terms:
        rendered = []
        for t in go_terms:
            code = ((t.get("category") or {}).get("code")) or "?"
            rendered.append(f"{t.get('identifier', '')} {t.get('name', '')} [{code}]")
        interpro2go = "; ".join(rendered)
    else:
        interpro2go = "None mapped (no InterPro2GO terms for this entry)"

    member_dbs = md.get("member_databases") or {}
    db_parts = []
    for db, sigs in member_dbs.items():
        if isinstance(sigs, dict):
            for acc, label in sigs.items():
                db_parts.append(f"{acc} ({db}: {label})")
    members = "; ".join(db_parts) if db_parts else "Not specified"

    counters = md.get("counters") or {}
    description_blocks = md.get("description") or []
    desc_text = ""
    if isinstance(description_blocks, list):
        for block in description_blocks:
            if isinstance(block, dict) and block.get("text"):
                desc_text += " " + _strip_html(block["text"])
    desc_text = desc_text.strip() or "Not specified in InterPro"
    if len(desc_text) > 1500:
        desc_text = desc_text[:1500] + " ..."

    return {
        "interpro_id": md.get("accession") or metadata_path.parent.name,
        "interpro_name": name,
        "interpro_short_name": short,
        "interpro_type": md.get("type") or "Not specified",
        "interpro_integrated": md.get("integrated") or "None (top-level entry)",
        "member_databases": members,
        "n_proteins": str(counters.get("proteins", "unknown")),
        "n_taxa": str(counters.get("taxa", "unknown")),
        "n_subfamilies": str(counters.get("subfamilies", "unknown")),
        "interpro2go_terms": interpro2go,
        "interpro_description": desc_text,
    }


def ensure_metadata(interpro_id: str, database: str) -> Path:
    """Return the cached metadata path, fetching it from InterPro if missing."""
    metadata_path = (
        Path("interpro") / database / interpro_id / f"{interpro_id}-metadata.yaml"
    )
    if metadata_path.exists():
        return metadata_path

    print(f"Metadata not cached; fetching {database} {interpro_id} from InterPro...")
    from ai_gene_review.tools.fetch_interpro_family_simple import (
        InterProFamilyFetcherSimple,
    )

    fetcher = InterProFamilyFetcherSimple(output_dir=".")
    fetcher.fetch_and_save(database, interpro_id, include_proteins=False)
    if not metadata_path.exists():
        raise FileNotFoundError(f"Fetch did not produce {metadata_path}")
    return metadata_path


def build_cmd(
    context: dict, provider: str, output_path: Path, extra_args: Optional[list] = None
) -> list[str]:
    """Build the deep-research-client command for an InterPro family report."""
    actual_provider = "perplexity" if provider == "perplexity-lite" else provider
    cmd = [
        "uv", "run", "deep-research-client", "research",
        "--template", TEMPLATE,
        "--provider", actual_provider,
        "--output", str(output_path),
    ]
    for key, value in context.items():
        cmd.extend(["--var", f"{key}={value}"])
    if extra_args:
        cmd.extend(extra_args)
    return cmd


def run(
    interpro_id: str,
    provider: str,
    database: str,
    fallback: Optional[list[str]],
    timeout: int,
    extra_args: Optional[list[str]],
) -> int:
    metadata_path = ensure_metadata(interpro_id, database)
    context = load_family_context(metadata_path)
    family_dir = metadata_path.parent

    providers_to_try = [provider] + list(fallback or [])
    for i, prov in enumerate(providers_to_try):
        output_path = family_dir / f"{interpro_id}-deep-research-{prov}.md"
        cmd = build_cmd(context, prov, output_path, extra_args)
        label = f"[fallback {i}] " if i else ""
        print(f"{label}Running: {' '.join(cmd)}")
        print(f"{label}Timeout: {timeout}s")
        try:
            result = subprocess.run(cmd, timeout=timeout)
            if result.returncode == 0:
                print(f"✅ Wrote {output_path}")
                return 0
            print(f"Provider {prov} exited with code {result.returncode}", file=sys.stderr)
        except subprocess.TimeoutExpired:
            print(f"Provider {prov} timed out after {timeout}s", file=sys.stderr)
        if i < len(providers_to_try) - 1:
            print(f"Trying fallback provider: {providers_to_try[i + 1]}", file=sys.stderr)

    print("All providers failed", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("interpro_id", help="InterPro/PANTHER/Pfam entry id (e.g. IPR000719)")
    parser.add_argument(
        "provider",
        nargs="?",
        default="falcon",
        help="Provider (default: falcon/Edison; also openai, perplexity, perplexity-lite, ...)",
    )
    parser.add_argument("--database", default="interpro", help="Source database (default: interpro)")
    parser.add_argument("--fallback", nargs="+", metavar="PROVIDER", help="Fallback providers")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--extra-args", nargs=argparse.REMAINDER, help="Extra args for deep-research-client")
    args = parser.parse_args()

    return run(
        interpro_id=args.interpro_id,
        provider=args.provider,
        database=args.database,
        fallback=args.fallback,
        timeout=args.timeout,
        extra_args=args.extra_args,
    )


if __name__ == "__main__":
    sys.exit(main())
