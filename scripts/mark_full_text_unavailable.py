#!/usr/bin/env python3
"""Set full_text_unavailable: true on supported_by entries where the cited
publication is abstract-only/unavailable AND the supporting_text fails strict
substring validation.

This honestly documents cases where the curator couldn't verify the quote
because full text wasn't accessible (not that the quote is a valid paraphrase).

Usage:
    uv run python scripts/mark_full_text_unavailable.py --dry-run
    uv run python scripts/mark_full_text_unavailable.py
"""

import sys
from pathlib import Path

import yaml as pyyaml
from ruamel.yaml import YAML

from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)
from linkml_reference_validator.models import ReferenceValidationConfig

yaml_rt = YAML()
yaml_rt.preserve_quotes = True
yaml_rt.width = 80


def load_pub_metadata(pub_path: Path) -> dict | None:
    """Load just the YAML frontmatter from a publication markdown file."""
    try:
        with open(pub_path) as f:
            text = f.read()
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        return pyyaml.safe_load(text[3:end])
    except pyyaml.YAMLError:
        return None


def pub_has_full_text(pub_path: Path) -> bool:
    """Check if a cached publication has full text content."""
    meta = load_pub_metadata(pub_path)
    if meta is None:
        return False
    # content_type trumps full_text_available
    content_type = meta.get("content_type")
    if content_type in ("abstract_only", "unavailable"):
        return False
    if content_type in ("full_text_xml", "html"):
        return True
    # Fall back to full_text_available boolean
    return bool(meta.get("full_text_available", False))


def ref_to_cache_path(ref_id: str, cache_dir: Path) -> Path | None:
    """Convert a reference ID (PMID:123 or DOI:10.xxx/yyy) to cache path."""
    if not ref_id or ":" not in ref_id:
        return None
    prefix, rest = ref_id.split(":", 1)
    if prefix == "PMID":
        return cache_dir / f"PMID_{rest}.md"
    if prefix == "DOI":
        return cache_dir / f"DOI_{rest.replace('/', '_')}.md"
    return None


def main():
    dry_run = "--dry-run" in sys.argv
    cache_dir = Path("publications")

    # Build a ref_id -> has_full_text cache
    full_text_cache: dict[str, bool] = {}

    def check_full_text(ref_id: str) -> bool | None:
        """Returns True/False if cached, None if pub doesn't exist."""
        if ref_id in full_text_cache:
            return full_text_cache[ref_id]
        pub_path = ref_to_cache_path(ref_id, cache_dir)
        if pub_path is None or not pub_path.exists():
            full_text_cache[ref_id] = None  # type: ignore
            return None
        has_ft = pub_has_full_text(pub_path)
        full_text_cache[ref_id] = has_ft
        return has_ft

    # Set up LRV to check if supporting_text passes strict validation
    config = ReferenceValidationConfig(
        cache_dir="publications",
        literal_bracket_patterns=[r"[^a-zA-Z\s]", r"^[A-Z]{2,5}$"],
    )
    lrv = SupportingTextValidator(config)

    total_marked = 0
    files_changed = 0

    for filepath in sorted(Path("genes").rglob("*-ai-review.yaml")):
        try:
            with open(filepath) as f:
                data = yaml_rt.load(f)
        except Exception as e:
            print(f"  SKIP {filepath}: {e}", file=sys.stderr)
            continue

        if not data:
            continue

        file_marks = 0

        def walk(obj):
            nonlocal file_marks
            if hasattr(obj, "get") and hasattr(obj, "__setitem__"):
                if "supported_by" in obj and isinstance(obj["supported_by"], list):
                    for sb in obj["supported_by"]:
                        if not (hasattr(sb, "get") and hasattr(sb, "__setitem__")):
                            continue
                        # Skip if already marked
                        if sb.get("full_text_unavailable"):
                            continue
                        ref_id = sb.get("reference_id", "")
                        text = sb.get("supporting_text", "")
                        if not ref_id or not text:
                            continue
                        # Only mark PMID/DOI refs
                        prefix = ref_id.split(":", 1)[0] if ":" in ref_id else ""
                        if prefix not in ("PMID", "DOI"):
                            continue
                        # Does cached pub have full text?
                        has_ft = check_full_text(ref_id)
                        if has_ft is None:
                            continue  # pub not cached, can't judge
                        if has_ft:
                            continue  # full text available; curator should fix
                        # No full text. Does supporting_text currently fail?
                        result = lrv.validate(text, ref_id)
                        if result.is_valid:
                            continue  # passes strict check, no need to mark
                        # Mark it
                        sb["full_text_unavailable"] = True
                        file_marks += 1
                for v in obj.values():
                    walk(v)
            elif isinstance(obj, list):
                for item in obj:
                    walk(item)

        walk(data)

        if file_marks > 0:
            rel = filepath
            print(f"{rel}: marked {file_marks} entries")
            total_marked += file_marks
            if not dry_run:
                with open(filepath, "w") as f:
                    yaml_rt.dump(data, f)
                files_changed += 1

    print(f"\nTotal: {total_marked} entries marked in {files_changed} files")
    if dry_run:
        print("(dry run - no files modified)")


if __name__ == "__main__":
    main()
