"""Re-review analysis for horse CACNB3 benchmark accession A0A5F5PZM5.

1. Paralog test: is the horse protein closer to human CACNB3 than to the other
   three human calcium-channel beta paralogs (CACNB1/2/4)? Compared over the
   conserved SH3-HOOK-GK core, which excludes the variable N-terminal exon.
2. Gene-model test: compare A0A5F5PZM5 with the other UniProt products of the
   same horse gene (Ensembl ENSECAG00000012018) to locate where they differ.

Run from the repository root:
    uv run python genes/HORSE/CACNB3/CACNB3-bioinformatics/compare_paralogs_rereview.py
Sequences are fetched live from the UniProt REST API; nothing is hardcoded.
"""

import json
from pathlib import Path
from urllib.request import urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
TARGET = "A0A5F5PZM5"
HUMAN_PARALOGS = {
    "CACNB1": "Q02641",
    "CACNB2": "Q08289",
    "CACNB3": "P54284",
    "CACNB4": "O00305",
}
HORSE_MODELS = ["A0A3Q2HUK8", "A0A5F5PR94", "F6SZ27", "A0A5F5PX04"]
# Conserved core motif shared by the beta subunits (start of the SH3 region
# in human CACNB3, "GSADSYTSRPS..."); the N-terminal segment before it is the
# alternatively spliced exon.
CORE_ANCHOR = "SYTSRPS"


def fetch(acc: str) -> str:
    """Fetch a UniProt sequence as a plain string."""
    with urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as fh:
        lines = fh.read().decode().splitlines()
    return "".join(lines[1:])


def identity(a: str, b: str) -> dict:
    """Global alignment identity over aligned (paired) positions."""
    aligner = Align.PairwiseAligner(
        mode="global",
        match_score=2,
        mismatch_score=-1,
        open_gap_score=-10,
        extend_gap_score=-0.5,
    )
    aln = aligner.align(a, b)[0]
    pairs = [
        (i, j)
        for (s, e), (t, u) in zip(*aln.aligned)
        for i, j in zip(range(s, e), range(t, u))
    ]
    same = sum(a[i] == b[j] for i, j in pairs)
    return {
        "paired": len(pairs),
        "identical": same,
        "identity_percent": round(100 * same / len(pairs), 2),
        "coverage_of_first_percent": round(100 * len(pairs) / len(a), 2),
    }


def main() -> None:
    target = fetch(TARGET)
    out: dict = {"target": TARGET, "target_length": len(target)}
    anchor = target.find(CORE_ANCHOR)
    out["core_anchor_position_1based"] = anchor + 1 if anchor >= 0 else None
    out["target_n_terminal_segment"] = target[: anchor - 3] if anchor > 3 else ""

    def core(seq: str) -> str:
        k = seq.find(CORE_ANCHOR)
        return seq[k:] if k >= 0 else seq

    tcore = core(target)
    out["paralog_core_identity"] = {}
    for sym, acc in HUMAN_PARALOGS.items():
        seq = fetch(acc)
        out["paralog_core_identity"][f"{sym}|{acc}"] = identity(tcore, core(seq))
    out["horse_models"] = {}
    for acc in HORSE_MODELS:
        seq = fetch(acc)
        k = seq.find(CORE_ANCHOR)
        out["horse_models"][acc] = {
            "length": len(seq),
            "n_terminal_segment": seq[: k - 3] if k > 3 else "",
            "core_identity_to_target": identity(tcore, core(seq)),
        }
    (HERE / "results-rereview.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
