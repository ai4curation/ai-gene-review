"""Draw the reproducible sample of PW definition-citation mappings for spot checking.

The population is every generated row whose only ``curation_rule`` is
``pw2go:src/PW_DEFINITION_XREF`` (a live GO biological process cited in a PW
definition, with no QA flag), sorted by (subject_id, object_id). The sample is
``random.Random(SEED).sample(population, SIZE)``. The verdicts are recorded by hand
in ``data/pw_def_xref_spot_check.yaml``; ``--check`` confirms that file lists exactly
this sample.

    python projects/RGD_PATHWAY_ONTOLOGY/scripts/sample_def_xref_spot_check.py [--check]
"""

import argparse
import random
import sys
from pathlib import Path

import yaml

DATA = Path(__file__).resolve().parents[1] / "data"
SEED = 20261123
SIZE = 50


def sample(mappings: list[dict], seed: int = SEED, size: int = SIZE) -> list[tuple[str, str]]:
    """The spot-check sample, as (subject_id, object_id) pairs sorted by subject.

    >>> rows = [{"subject_id": f"PW:{i}", "object_id": f"GO:{i}",
    ...          "curation_rule": ["pw2go:src/PW_DEFINITION_XREF"]} for i in range(5)]
    >>> rows.append({"subject_id": "PW:9", "object_id": "GO:9",
    ...              "curation_rule": ["pw2go:src/PW_DEFINITION_XREF", "pw2go:qa/OBSOLETE_TARGET"]})
    >>> len(sample(rows, size=5)), ("PW:9", "GO:9") in sample(rows, size=5)
    (5, False)
    """
    pop = sorted((m["subject_id"], m["object_id"]) for m in mappings
                 if m.get("curation_rule") == ["pw2go:src/PW_DEFINITION_XREF"])
    return sorted(random.Random(seed).sample(pop, size))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="compare with the recorded spot check")
    args = ap.parse_args()
    ms = yaml.safe_load((DATA / "pw_go_mappings.sssom.yaml").read_text())["mappings"]
    pairs = sample(ms)
    if not args.check:
        for s, o in pairs:
            print(s, o)
        return 0
    rec = yaml.safe_load((DATA / "pw_def_xref_spot_check.yaml").read_text())
    got = sorted((r["subject_id"], r["object_id"]) for r in rec["rows"])
    if got != pairs:
        print(f"spot check lists {len(got)} pairs; sample has {len(pairs)}; "
              f"missing {sorted(set(pairs) - set(got))}, extra {sorted(set(got) - set(pairs))}",
              file=sys.stderr)
        return 1
    print(f"spot check matches the {len(pairs)}-row sample")
    return 0


if __name__ == "__main__":
    sys.exit(main())
