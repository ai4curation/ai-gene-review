"""Compare all horse PTPRN2 UniProt/Ensembl models with human and mouse PTPRN2.

Re-review analysis (2026-10-20). Stdlib only; run with `uv run --python 3.12 compare_horse_models_rereview.py`.

For each protein it reports length, the PTP signature motif (HC..G..R[ST]G) and the
position of its catalytic Cys, and whether the residues after the motif match the
human Q92932 C-terminal tail. For the benchmark transcript and the canonical one it
also reports the Ensembl 3'-most coding exons, so a divergent tail can be traced to the
gene model. Results are written to results-rereview.json; nothing is hardcoded.
"""

from __future__ import annotations

import json
import re
import urllib.request

HUMAN = "Q92932"
MOUSE = "P80560"
HORSE = [
    "A0A9L0T4W6",  # benchmark accession, ENSECAT00000094767
    "A0A9L0RAE3",
    "A0A9L0R212",
    "A0A9L0RHF7",
    "F6S989",
    "A0A9L0RER4",
    "A0A9L0R2U6",
    "A0A9L0T2L9",
]
TRANSCRIPTS = {"A0A9L0T4W6": "ENSECAT00000094767", "A0A9L0RAE3": "ENSECAT00000125162"}
CANONICAL_FASTA = (
    "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/"
    "reference_proteomes/Eukaryota/UP000002281/UP000002281_9796.fasta.gz"
)
MOTIF = re.compile(r"HC[SD].G..R[ST]G")


def fetch(url: str, headers: dict | None = None) -> bytes:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as r:
        return r.read()


def fasta_seq(acc: str) -> str:
    text = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").decode()
    return "".join(text.splitlines()[1:])


def canonical_members() -> list[str]:
    import gzip

    text = gzip.decompress(fetch(CANONICAL_FASTA)).decode()
    return [a for a in HORSE if f"|{a}|" in text]


def tail_after_motif(seq: str) -> tuple[str | None, int | None, str]:
    m = MOTIF.search(seq)
    if not m:
        return None, None, ""
    return m.group(), m.start() + 2, seq[m.end():]  # catalytic Cys is motif position 2 (1-based)


def matched_prefix(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def last_coding_exons(tid: str) -> list[dict]:
    d = json.loads(
        fetch(
            f"https://rest.ensembl.org/lookup/id/{tid}?expand=1",
            {"Content-Type": "application/json"},
        )
    )
    tr = d["Translation"]
    exons = sorted(d["Exon"], key=lambda e: e["start"], reverse=d["strand"] == -1)
    coding = [e for e in exons if e["end"] >= tr["start"] and e["start"] <= tr["end"]]
    return [
        {"exon": e["id"], "start": e["start"], "end": e["end"], "length": e["end"] - e["start"] + 1}
        for e in coding[-3:]
    ] + [{"translation_start": tr["start"], "translation_end": tr["end"], "gene_display": d.get("display_name")}]


def main() -> None:
    seqs = {a: fasta_seq(a) for a in [HUMAN, MOUSE] + HORSE}
    _, _, human_tail = tail_after_motif(seqs[HUMAN])
    rows = []
    for acc, s in seqs.items():
        motif, cys, tail = tail_after_motif(s)
        n = matched_prefix(tail, human_tail)
        rows.append(
            {
                "accession": acc,
                "length": len(s),
                "ptp_motif": motif,
                "catalytic_cys_position": cys,
                "tail_length_after_motif": len(tail),
                "tail_identical_prefix_with_human": n,
                "tail_fully_identical_to_human": tail == human_tail,
                "c_terminal_30": s[-30:],
            }
        )
        print(acc, len(s), motif, cys, len(tail), n, tail == human_tail, s[-30:])
    canon = canonical_members()
    print("Horse model(s) in UniProt gene-centric canonical proteome:", canon)
    exons = {acc: last_coding_exons(t) for acc, t in TRANSCRIPTS.items()}
    for acc, ex in exons.items():
        print(acc, TRANSCRIPTS[acc], ex)
    out = {"human_tail_after_motif": human_tail, "proteins": rows, "canonical_proteome_members": canon, "ensembl_3prime_coding_exons": exons}
    with open("results-rereview.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
