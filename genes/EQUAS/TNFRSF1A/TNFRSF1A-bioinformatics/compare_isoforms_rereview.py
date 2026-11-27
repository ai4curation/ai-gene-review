# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare the two donkey TNFRSF1A gene models (A0A9L0JKX4, A0A8C4MD74).

Fetches both UniProt sequences and the Ensembl exon structure of the gene
ENSEASG00005016176, then reports whether the shorter model equals the longer
one minus a contiguous block, and which exon(s) the shorter transcript lacks.

Usage: uv run --script compare_isoforms_rereview.py
"""

import json
import urllib.request
from pathlib import Path

SHORT = "A0A9L0JKX4"
LONG = "A0A8C4MD74"
GENE = "ENSEASG00005016176"


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def uniprot_seq(acc: str) -> str:
    fa = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(fa.splitlines()[1:])


def main() -> None:
    s, l = uniprot_seq(SHORT), uniprot_seq(LONG)
    # longest common prefix and suffix
    p = 0
    while p < min(len(s), len(l)) and s[p] == l[p]:
        p += 1
    q = 0
    while q < min(len(s), len(l)) - p and s[-1 - q] == l[-1 - q]:
        q += 1
    contiguous_deletion = p + q == len(s)
    deleted = l[p : len(l) - q] if contiguous_deletion else None
    gene = json.loads(
        fetch(
            f"https://rest.ensembl.org/lookup/id/{GENE}?expand=1;content-type=application/json"
        )
    )
    transcripts = {}
    for t in gene["Transcript"]:
        transcripts[t["id"]] = {
            "is_canonical": t.get("is_canonical"),
            "translation_length": t.get("Translation", {}).get("length"),
            "exons": [(e["id"], e["start"], e["end"]) for e in t["Exon"]],
        }
    by_len = {v["translation_length"]: k for k, v in transcripts.items()}
    long_ex = transcripts[by_len[len(l)]]["exons"]
    short_ids = {e[0] for e in transcripts[by_len[len(s)]]["exons"]}
    skipped = [
        {"exon": e[0], "index_1based": i + 1, "length_nt": e[2] - e[1] + 1}
        for i, e in enumerate(long_ex)
        if e[0] not in short_ids
    ]
    res = {
        "short": SHORT,
        "short_length": len(s),
        "long": LONG,
        "long_length": len(l),
        "short_equals_long_minus_one_block": contiguous_deletion,
        "deleted_block_long_1based": [p + 1, len(l) - q] if contiguous_deletion else None,
        "deleted_block_sequence": deleted,
        "ensembl_gene": GENE,
        "transcripts": transcripts,
        "exons_in_long_missing_from_short": skipped,
    }
    out = Path(__file__).resolve().parent / "results-isoforms-rereview.json"
    out.write_text(json.dumps(res, indent=2) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k != "transcripts"}, indent=2))


if __name__ == "__main__":
    main()
