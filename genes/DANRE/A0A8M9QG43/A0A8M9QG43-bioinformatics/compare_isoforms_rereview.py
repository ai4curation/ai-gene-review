"""Compare the benchmark dnajc6 entry A0A8M9QG43 with the UniProt gene-centric
canonical dnajc6 product A0A8M9Q6X2 and with human auxilin O75061.

Fetches sequences from the UniProt REST API, aligns them with MAFFT, and reports
(1) indel/substitution blocks between the two zebrafish entries, mapped to
A0A8M9QG43 coordinates, and (2) conservation of the J-domain HPD motif and of the
tensin-type phosphatase P-loop region (human Cys-X5-Arg window).

Usage: python compare_isoforms_rereview.py > RESULTS-rereview.txt
Requires: mafft on PATH (stdlib only otherwise).
"""

import re
import subprocess
import tempfile
import urllib.request

ACCS = ["A0A8M9QG43", "A0A8M9Q6X2", "O75061"]


def fetch(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as fh:
        lines = fh.read().decode().splitlines()
    return "".join(lines[1:])


def parse_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    name = ""
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        else:
            seqs[name] += line.strip()
    return seqs


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    for a, s in seqs.items():
        print(f"{a}\tlength={len(s)}")
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for a, s in seqs.items():
            fh.write(f">{a}\n{s}\n")
        path = fh.name
    out = subprocess.run(["mafft", "--quiet", "--auto", path], capture_output=True, text=True, check=True)
    aln = parse_fasta(out.stdout)
    q, c = aln["A0A8M9QG43"], aln["A0A8M9Q6X2"]
    # difference blocks between the two zebrafish entries
    print("\n# Differences A0A8M9QG43 vs A0A8M9Q6X2 (QG43 residue coordinates)")
    qpos = 0
    block = None
    blocks = []
    for i, (a, b) in enumerate(zip(q, c)):
        if a != "-":
            qpos += 1
        if a != b:
            if block is None:
                block = [i, i, qpos]
            block[1] = i
        elif block is not None:
            blocks.append(block)
            block = None
    if block is not None:
        blocks.append(block)
    for start, end, qp in blocks:
        print(f"aln {start + 1}-{end + 1}\tnear QG43 residue {qp}\tQG43={q[start:end + 1]}\tQ6X2={c[start:end + 1]}")
    print(f"total difference blocks: {len(blocks)}")
    # identity to human over aligned non-gap columns
    for z in ["A0A8M9QG43", "A0A8M9Q6X2"]:
        pairs = [(x, y) for x, y in zip(aln[z], aln["O75061"]) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in pairs)
        print(f"{z} vs O75061: identity {ident}/{len(pairs)} = {ident / len(pairs):.3f}")
    print("\n# Motifs (ungapped sequence coordinates)")
    for a, s in seqs.items():
        hpd = [m.start() + 1 for m in re.finditer("HPD", s)]
        ploop = [(m.start() + 1, m.group()) for m in re.finditer(r"C.{5}R", s)]
        print(f"{a}\tHPD at {hpd}\tlast 120 aa contains HPD: {'HPD' in s[-120:]}")
        print(f"{a}\tCX5R windows (first 400 aa): {[p for p in ploop if p[0] < 400]}")
        short = [(m.start() + 1, m.group()) for m in re.finditer(r"C.{3}R", s) if m.start() < 400]
        print(f"{a}\tCX3R windows (first 400 aa, shortened auxilin-type P-loop): {short}")


if __name__ == "__main__":
    main()
