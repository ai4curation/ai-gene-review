"""Stable project entry point for the upstream reference validator CLI."""


def main():
    from linkml_reference_validator.cli import main as upstream_main

    return upstream_main()


if __name__ == "__main__":
    raise SystemExit(main())
