#!/usr/bin/env python3
"""Wrapper for deep-research-client for open-ended biological concepts.

This script:
1. Accepts a concept string and provider
2. Builds a unix-friendly slug for filenames
3. Calls deep-research-client with a concept-specific template
4. Outputs to terms/<slug>/<slug>-deep-research-<provider>.md
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to a unix-friendly slug.

    Keeps lowercase letters and numbers, replaces other runs with underscores.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    if not cleaned:
        return "concept"
    return cleaned.lower()


def run_deep_research(
    concept: str,
    concept_slug: str,
    provider: str,
    output_path: Path,
    template_path: Path,
    extra_args: list | None = None,
    use_template: bool = True,
) -> int:
    """Run deep-research-client with proper arguments."""
    # Map internal provider names to deep-research-client provider names
    actual_provider = "perplexity" if provider == "perplexity-lite" else provider

    if use_template:
        cmd = [
            "uv",
            "run",
            "deep-research-client",
            "research",
            "--template",
            str(template_path),
            "--var",
            f"concept={concept}",
            "--var",
            f"concept_slug={concept_slug}",
            "--provider",
            actual_provider,
            "--output",
            str(output_path),
        ]
    else:
        query = (
            f"Research the biological concept '{concept}'. "
            "Provide a clear definition, core components, and a gene/protein list. "
            "Prioritize human gene symbols if the concept is relevant to human biology; "
            "otherwise prioritize the most studied organisms for the concept. "
            "Distinguish core vs accessory components and cite primary literature."
        )
        cmd = [
            "uv",
            "run",
            "deep-research-client",
            "research",
            query,
            "--provider",
            actual_provider,
            "--param",
            "reasoning_effort=low",
            "--param",
            "model=sonar-pro",
            "--output",
            str(output_path),
        ]

    if extra_args:
        cmd.extend(extra_args)

    print(f"Running: {' '.join(cmd[:12])}...")
    result = subprocess.run(cmd)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deep research wrapper for open-ended biological concepts"
    )
    parser.add_argument("concept", help="Concept or pathway name (quote if it has spaces)")
    parser.add_argument(
        "provider",
        choices=["openai", "perplexity", "perplexity-lite", "falcon", "cyberian"],
        help="Deep research provider",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("terms"),
        help="Base output directory (default: terms)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("templates/concept_research.md.j2"),
        help="Template file for concept research",
    )
    parser.add_argument(
        "--slug",
        help="Override slug used for output directory and filename",
    )
    parser.add_argument(
        "--extra-args",
        nargs=argparse.REMAINDER,
        help="Extra args to pass to deep-research-client",
    )

    args = parser.parse_args()

    concept_slug = slugify(args.slug or args.concept)

    # Determine output path
    output_dir = args.output_dir / concept_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.provider == "perplexity-lite":
        output_file = output_dir / f"{concept_slug}-deep-research-perplexity-lite.md"
        use_template = False
    else:
        output_file = output_dir / f"{concept_slug}-deep-research-{args.provider}.md"
        use_template = True

    print(f"Concept: {args.concept}")
    print(f"Slug: {concept_slug}")
    print(f"Provider: {args.provider}")
    print(f"Output: {output_file}")

    return run_deep_research(
        concept=args.concept,
        concept_slug=concept_slug,
        provider=args.provider,
        output_path=output_file,
        template_path=args.template,
        extra_args=args.extra_args,
        use_template=use_template,
    )


if __name__ == "__main__":
    sys.exit(main())
