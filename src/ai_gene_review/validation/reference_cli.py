"""Run the upstream reference CLI with the repo's pinned-release compatibility."""

from ai_gene_review.validation.reference_cache_compat import (
    install_reference_cache_compatibility,
)


def main():
    install_reference_cache_compatibility()
    from linkml_reference_validator.cli import main as upstream_main

    return upstream_main()


if __name__ == "__main__":
    raise SystemExit(main())
