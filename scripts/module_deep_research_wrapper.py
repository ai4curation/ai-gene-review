#!/usr/bin/env python3
"""Wrapper for deep-research-client for module documents.

The wrapper resolves a module YAML document, summarizes its current structure,
and sends a biology-oriented outline to a module-specific research template.
Research output is written beside the module YAML by default.

Some small path/YAML/descriptor helpers intentionally mirror render_modules.py
so this wrapper can remain usable as a standalone script.
"""

from __future__ import annotations

import argparse
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


PROVIDERS = ("openai", "perplexity", "perplexity-lite", "falcon", "cyberian", "codex", "asta")
DEFAULT_DRC_PACKAGE = "deep-research-client[cyberian]==0.2.7rc1"
UNRESOLVED_PLACEHOLDER_PATTERNS = (
    "{module_title}",
    "{module_summary}",
    "{module_outline}",
    "{module_connections}",
    "{{ module_title }}",
    "{{ module_summary }}",
    "{{ module_outline }}",
    "{{ module_connections }}",
)


def deep_research_client_command() -> list[str]:
    """Return the command prefix for invoking deep-research-client."""
    override = os.environ.get("DEEP_RESEARCH_CLIENT_CMD")
    if override:
        return shlex.split(override)
    package = os.environ.get("DEEP_RESEARCH_CLIENT_UVX_FROM", DEFAULT_DRC_PACKAGE)
    return ["uvx", "--from", package, "deep-research-client"]


def as_list(value: Any) -> list[Any]:
    """Return a value as a list, treating null and missing values as empty."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def slugify(text: str, *, separator: str = "-") -> str:
    """Convert text to a stable filename-ish slug."""
    cleaned = re.sub(r"[^a-zA-Z0-9]+", separator, text.strip())
    cleaned = re.sub(rf"{re.escape(separator)}+", separator, cleaned).strip(separator)
    return cleaned.lower() or "module"


def normalized_id(value: Any) -> str:
    """Normalize IDs and names for fuzzy module lookup."""
    return slugify(str(value or "").replace(":", "-"), separator="-")


def load_module_yaml(path: Path) -> dict[str, Any]:
    """Load a module YAML file."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Module YAML must contain a mapping: {path}")
    if "module" not in data:
        raise ValueError(f"Module YAML is missing top-level 'module': {path}")
    return data


def iter_module_files(modules_dir: Path) -> list[Path]:
    """Return module YAML files under modules_dir."""
    if not modules_dir.exists():
        return []
    return sorted(
        {
            path
            for pattern in ("*.yaml", "*.yml")
            for path in modules_dir.rglob(pattern)
            if path.is_file()
        }
    )


def resolve_module_path(module_ref: str, modules_dir: Path = Path("modules")) -> Path:
    """Resolve a module reference to a YAML path.

    The reference may be a path, a root-level filename stem, a top-level module
    document id, or the nested module.id.
    """
    raw_path = Path(module_ref)
    if raw_path.exists():
        return raw_path

    candidates: list[Path] = []
    if raw_path.suffix in {".yaml", ".yml"}:
        candidates.append(raw_path)
    else:
        candidates.extend(
            [
                modules_dir / f"{module_ref}.yaml",
                modules_dir / f"{module_ref}.yml",
                modules_dir / f"{slugify(module_ref)}.yaml",
                modules_dir / f"{slugify(module_ref)}.yml",
            ]
        )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    module_files = iter_module_files(modules_dir)
    ref_norm = normalized_id(module_ref)

    stem_matches = [
        path for path in module_files if normalized_id(path.stem) == ref_norm
    ]
    if len(stem_matches) == 1:
        return stem_matches[0]
    if len(stem_matches) > 1:
        matches = ", ".join(str(path) for path in stem_matches)
        raise ValueError(f"Ambiguous module reference {module_ref!r}: {matches}")

    id_matches: list[Path] = []
    for path in module_files:
        data = load_module_yaml(path)
        module = data.get("module") if isinstance(data.get("module"), dict) else {}
        known_ids = {
            data.get("id"),
            module.get("id"),
            module.get("label"),
            data.get("title"),
        }
        if ref_norm in {normalized_id(value) for value in known_ids if value}:
            id_matches.append(path)

    if len(id_matches) == 1:
        return id_matches[0]
    if len(id_matches) > 1:
        matches = ", ".join(str(path) for path in id_matches)
        raise ValueError(f"Ambiguous module reference {module_ref!r}: {matches}")

    checked = ", ".join(str(path) for path in candidates[:4])
    raise FileNotFoundError(
        f"Could not resolve module {module_ref!r}; checked {checked} and ids under {modules_dir}"
    )


def descriptor_text(descriptor: Any) -> str:
    """Return a compact label for a descriptor-like mapping."""
    if not isinstance(descriptor, dict):
        return ""
    term = descriptor.get("term") if isinstance(descriptor.get("term"), dict) else {}
    text = descriptor.get("preferred_term") or term.get("label") or term.get("id")
    if not text:
        text = descriptor.get("description", "")
    return str(text or "")


def selector_text(selector: Any) -> str:
    """Return a compact summary of a participant selector."""
    if not isinstance(selector, dict):
        return ""
    for slot in (
        "gene",
        "gene_product",
        "protein_complex",
        "family",
        "domain",
        "homolog_of",
        "ortholog_of",
        "required_function",
        "required_domain",
        "taxon",
    ):
        value = selector.get(slot)
        if isinstance(value, dict):
            text = descriptor_text(value)
            if text:
                return text
    description = selector.get("description")
    if description:
        return str(description)
    return str(selector.get("selector_type") or "").replace("_", " ").lower()


def format_concepts(data: dict[str, Any]) -> str:
    """Format top-level module concepts for prompt context."""
    module = data.get("module") if isinstance(data.get("module"), dict) else {}
    concepts = as_list(module.get("concepts"))
    if not concepts:
        return "No explicit top-level concepts."
    lines = []
    for concept in concepts:
        text = descriptor_text(concept)
        if text:
            lines.append(f"- {text}")
    return "\n".join(lines) or "No explicit top-level concepts."


def format_outline(data: dict[str, Any], *, max_lines: int = 180) -> str:
    """Format a biological outline for the prompt."""
    module = data.get("module") if isinstance(data.get("module"), dict) else {}
    lines: list[str] = []

    def add(line: str) -> None:
        if len(lines) < max_lines:
            lines.append(line)

    def walk(node: dict[str, Any], depth: int = 0) -> None:
        indent = "  " * depth
        label = node.get("label") or node.get("id") or "unnamed process"
        add(f"{indent}- {label}")

        for annoton in as_list(node.get("annotons")):
            if not isinstance(annoton, dict):
                continue
            annoton_label = annoton.get("label") or annoton.get("id") or "unnamed role"
            participant = selector_text(annoton.get("participant"))
            function = descriptor_text(annoton.get("function"))
            details = []
            if participant:
                details.append(f"molecular player: {participant}")
            if function:
                details.append(f"activity or role: {function}")
            detail_text = f" ({'; '.join(details)})" if details else ""
            add(f"{indent}  - {annoton_label}{detail_text}")

        for part in as_list(node.get("parts")):
            if not isinstance(part, dict):
                continue
            role = part.get("role")
            if role:
                order = f"{part.get('order')}. " if part.get("order") else ""
                add(f"{indent}  - {order}{role}")
            child = part.get("node")
            if isinstance(child, dict):
                walk(child, depth + 1)

        for variant_set in as_list(node.get("variant_sets")):
            if not isinstance(variant_set, dict):
                continue
            axis = variant_set.get("axis", "")
            label = variant_set.get("label") or variant_set.get("id") or "variant set"
            if axis:
                add(f"{indent}  - Alternative versions by {axis}: {label}")
            else:
                add(f"{indent}  - Alternative versions: {label}")
            for variant in as_list(variant_set.get("variants")):
                if isinstance(variant, dict):
                    walk(variant, depth + 2)

    if module:
        walk(module)
    if len(lines) >= max_lines:
        lines.append("- ... outline truncated for prompt size")
    return "\n".join(lines) or "No module outline available."


def format_connections(data: dict[str, Any], *, max_lines: int = 80) -> str:
    """Format relationships among biological steps."""
    module = data.get("module") if isinstance(data.get("module"), dict) else {}
    lines: list[str] = []
    labels: dict[str, str] = {}

    def add(line: str) -> None:
        if len(lines) < max_lines:
            lines.append(line)

    def collect_labels(node: dict[str, Any]) -> None:
        node_id = node.get("id")
        if node_id:
            labels[str(node_id)] = str(node.get("label") or node_id).replace("_", " ")
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                labels[str(annoton["id"])] = str(
                    annoton.get("label") or annoton["id"]
                ).replace("_", " ")
        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                collect_labels(part["node"])
        for variant_set in as_list(node.get("variant_sets")):
            if not isinstance(variant_set, dict):
                continue
            for variant in as_list(variant_set.get("variants")):
                if isinstance(variant, dict):
                    collect_labels(variant)

    def label_for(value: Any) -> str:
        key = str(value or "")
        return labels.get(key, key.replace("_", " "))

    def relationship_text(value: Any) -> str:
        text = str(value or "connects to").replace("_", " ").lower()
        return {
            "provides input for": "feeds into",
            "precedes": "precedes",
            "requires": "requires",
            "enables": "enables",
            "negatively regulates": "inhibits",
            "positively regulates": "promotes",
        }.get(text, text)

    def walk(node: dict[str, Any]) -> None:
        for connection in as_list(node.get("connections")):
            if not isinstance(connection, dict):
                continue
            source = connection.get("source", "")
            target = connection.get("target", "")
            kind = relationship_text(connection.get("connection_type", "CONNECTS_TO"))
            description = connection.get("description", "")
            suffix = f": {description}" if description else ""
            add(f"- {label_for(source)} {kind} {label_for(target)}{suffix}")

        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                walk(part["node"])
        for variant_set in as_list(node.get("variant_sets")):
            if not isinstance(variant_set, dict):
                continue
            for variant in as_list(variant_set.get("variants")):
                if isinstance(variant, dict):
                    walk(variant)

    if module:
        collect_labels(module)
        walk(module)
    if len(lines) >= max_lines:
        lines.append("- ... connections truncated for prompt size")
    return "\n".join(lines) or "No explicit connections."


def output_path_for_research(
    module_path: Path,
    provider: str,
    output_dir: Path | None = None,
) -> Path:
    """Return the research output path for a module and provider slug."""
    directory = output_dir if output_dir is not None else module_path.parent
    return directory / f"{module_path.stem}-deep-research-{provider}.md"


def build_deep_research_command(
    *,
    module_path: Path,
    data: dict[str, Any],
    provider: str,
    output_path: Path,
    template_path: Path,
    extra_args: list[str] | None = None,
) -> list[str]:
    """Build the deep-research-client command."""
    if provider == "perplexity-lite":
        actual_provider = "perplexity"
    elif provider == "codex":
        actual_provider = "cyberian"
    else:
        actual_provider = provider
    module = data.get("module") if isinstance(data.get("module"), dict) else {}
    variables = {
        "module_title": str(data.get("title") or module.get("label") or module_path.stem),
        "module_summary": str(data.get("description") or module.get("description") or ""),
        "module_outline": format_outline(data),
        "module_connections": format_connections(data),
    }

    cmd = [
        *deep_research_client_command(),
        "research",
        "--template",
        str(template_path),
    ]
    for key, value in variables.items():
        cmd.extend(["--var", f"{key}={value}"])
    cmd.extend(["--provider", actual_provider, "--output", str(output_path)])
    if provider == "codex":
        cmd.extend(["--param", "agent_type=codex"])
    if extra_args:
        cmd.extend(extra_args)
    return cmd


def command_for_log(cmd: list[str]) -> str:
    """Return a shell-ish command string with huge prompt vars redacted."""
    safe_cmd = []
    for item in cmd:
        if len(item) > 500:
            safe_cmd.append(item[:500] + "...<truncated>")
        else:
            safe_cmd.append(item)
    return shlex.join(safe_cmd)


def run_deep_research(
    cmd: list[str],
    output_path: Path,
    *,
    dry_run: bool = False,
    timeout: int | None = None,
) -> int:
    """Run deep-research-client unless dry-run is requested."""
    print(f"Output: {output_path}")
    print(f"Command: {command_for_log(cmd)}")
    if timeout:
        print(f"Timeout: {timeout}s")
    if dry_run:
        print("Dry run only; not running deep-research-client.")
        return 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(cmd, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f"Error: deep-research-client timed out after {timeout}s", file=sys.stderr)
        return 124
    if result.returncode != 0:
        return result.returncode
    if output_contains_unresolved_placeholders(output_path):
        print(
            f"Error: generated report still contains unresolved module template placeholders: {output_path}",
            file=sys.stderr,
        )
        return 1
    return 0


def output_contains_unresolved_placeholders(output_path: Path) -> bool:
    """Return true when a generated report still contains module template placeholders."""
    if not output_path.exists():
        return False
    text = output_path.read_text(encoding="utf-8", errors="replace")
    return any(pattern in text for pattern in UNRESOLVED_PLACEHOLDER_PATTERNS)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deep research wrapper for module KB YAML documents"
    )
    parser.add_argument(
        "module",
        help="Module YAML path, filename stem, top-level id, or module.id",
    )
    parser.add_argument("provider", choices=PROVIDERS, help="Deep research provider")
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=Path("modules"),
        help="Module YAML directory for id/stem lookup (default: modules)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Override output directory (default: beside module YAML)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("templates/module_research.md.j2"),
        help="Template file for module research",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout for deep-research-client subprocess in seconds",
    )
    parser.add_argument(
        "--extra-args",
        nargs=argparse.REMAINDER,
        help="Extra args to pass to deep-research-client",
    )

    args = parser.parse_args()

    module_path = resolve_module_path(args.module, args.modules_dir)
    data = load_module_yaml(module_path)
    output_path = output_path_for_research(module_path, args.provider, args.output_dir)
    cmd = build_deep_research_command(
        module_path=module_path,
        data=data,
        provider=args.provider,
        output_path=output_path,
        template_path=args.template,
        extra_args=args.extra_args,
    )

    print(f"Module: {module_path}")
    print(f"Provider: {args.provider}")
    return run_deep_research(
        cmd,
        output_path,
        dry_run=args.dry_run,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    sys.exit(main())
