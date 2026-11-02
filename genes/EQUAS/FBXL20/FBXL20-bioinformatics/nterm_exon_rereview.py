# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Compare the N-terminal region of FBXL20 gene products upstream of the conserved
F-box-proximal motif MFSNSDEAV, to tell alternative first exons from insertions.

Usage: uv run --script nterm_exon_rereview.py > nterm_exon_rereview_output.txt
"""
import requests

ACCESSIONS = [
    "A0A9L0IQA3",  # donkey benchmark target
    "Q96IG2",  # human canonical (reviewed)
    "Q9CZV8",  # mouse canonical (reviewed)
    "Q58DG6",  # bovine canonical (reviewed)
    "F6YIL4",  # horse
    "A0A5F5PIX0",  # horse
    "A0A9L0IZC9",  # donkey
    "A0A9L0JDR0",  # donkey
    "A0A9L0J589",  # donkey
    "A2A536",  # mouse unreviewed
]
MOTIF = "MFSNSDEAV"
CAAX_TAIL = "CCIIL"


def fetch(acc: str) -> tuple[str, str]:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    return lines[0], "".join(lines[1:])


for acc in ACCESSIONS:
    header, seq = fetch(acc)
    pos = seq.find(MOTIF)
    prefix = seq[:pos] if pos >= 0 else "(motif absent)"
    print(
        f"{acc}\tlen={len(seq)}\tmotif_start={pos + 1 if pos >= 0 else 'NA'}\t"
        f"prefix={prefix}\tcaax_tail={'yes' if seq.endswith(CAAX_TAIL) else 'no'}\t"
        f"after_motif_len={len(seq) - pos if pos >= 0 else 'NA'}"
    )
