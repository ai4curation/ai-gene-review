"""Analyses supporting the GO annotation review of human APLN (apelin, Q9ULZ1).

The three analyses are top-level scripts in this directory rather than library code,
because each is a single question answered once; see README.md and RESULTS.md.
"""


def main() -> None:
    print(
        "APLN bioinformatics: run the analyses directly --\n"
        "  uv run python cterm_conservation.py\n"
        "  uv run python resolve_withfrom.py\n"
        "  uv run python check_goa_reconciliation.py"
    )
