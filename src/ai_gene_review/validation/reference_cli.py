"""Stable project entry point for the upstream reference validator CLI.

Before handing over, it lets literature quotes match the cached record's title
(see ``title_matching``), so ``scripts/run_reference_validator.sh`` judges a
quote the same way as the repo's own validator.
"""


def main():
    from linkml_reference_validator.cli import main as upstream_main

    from ai_gene_review.validation.title_matching import install_title_matching

    install_title_matching()
    return upstream_main()


if __name__ == "__main__":
    raise SystemExit(main())
