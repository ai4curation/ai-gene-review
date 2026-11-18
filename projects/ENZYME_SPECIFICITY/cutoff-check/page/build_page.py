"""Build the cutoff-check results page from results.yaml.

The page (published as a Claude artifact and linked from the project manifest) embeds
the evaluation rows as JSON; its counts, headline and case-card scores are computed from
them in the page, so nothing in it is hand-entered.

    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/page/build_page.py OUT.html
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
FIELDS = [
    "gene",
    "go",
    "label",
    "ec",
    "action",
    "verdict",
    "best_target_family",
    "best_target_score",
    "best_target_tc",
    "better_fitting_families",
    "target_scores",
]


def main(out: Path) -> None:
    """Fill the template with the evaluation rows and the NCBIfam release."""
    rows = yaml.safe_load((HERE.parent / "results.yaml").read_text())
    releases = {r["ncbifam_release"] for r in rows}
    if len(releases) != 1:
        raise ValueError(f"results.yaml mixes NCBIfam releases: {sorted(releases)}")
    data = json.dumps([{k: r[k] for k in FIELDS} for r in rows], ensure_ascii=False)
    page = (HERE / "template.html").read_text()
    page = page.replace("__DATA__", data).replace("__RELEASE__", releases.pop())
    out.write_text(page)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
