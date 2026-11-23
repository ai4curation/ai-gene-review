#!/usr/bin/env python3
"""Reproducible domain-architecture, transmembrane, and pocket-residue survey of PANTHER PTHR24119.

Reads local PANTHER 19.0 membership (`PTHR24119-entries.csv` and `.cache/panther/panther-members-19.0.tsv`
when available, falling back to the 27-accession union recorded in `member_architectures.tsv`),
parses cached `genes/*/*/*-uniprot.txt` records first and UniProtKB REST `.txt` entries for
remaining members, and writes `member_architectures.tsv` summarizing sequence length, sequence
version, reviewed status, PANTHER subfamily, `IPR000582` (ACB) presence, `InterPro` domain list,
`FT TRANSMEM` intervals, `FT DOMAIN`/`FT REPEAT` intervals, and aligned human `Q9BR61` ACB-pocket
positions (`Tyr69`, `Lys73`, `Lys95`, `Ser106`, `Ser108`, `Tyr114`).
"""

from __future__ import annotations

import csv
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

KNOWN_PTHR24119_SUBFAMILIES = {
    "A0A1L8GMQ7": "PTHR24119:SF0",
    "A0A2K1Y7F9": "PTHR24119:SF0",
    "A0A8J1N1S3": "PTHR24119:SF0",
    "A2VDR2": "PTHR24119:SF0",
    "A3AYR1": "PTHR24119:SF0",
    "B9IDN1": "PTHR24119:SF0",
    "E1C483": "PTHR24119:SF0",
    "G3N0L6": "PTHR24119:SF0",
    "O50999": "PTHR24119:SF0",
    "Q28E11": "PTHR24119:SF0",
    "Q4V869": "PTHR24119:SF0",
    "Q4V8X4": "PTHR24119:SF0",
    "Q54GC8": "PTHR24119:SF0",
    "Q54JS2": "PTHR24119:SF10",
    "Q54VR7": "PTHR24119:SF7",
    "Q54ZJ0": "PTHR24119:SF0",
    "Q55BF3": "PTHR24119:SF10",
    "Q5RJK8": "PTHR24119:SF0",
    "Q66JD7": "PTHR24119:SF0",
    "Q86H58": "PTHR24119:SF0",
    "Q8MP77": "PTHR24119:SF1",
    "Q9BR61": "PTHR24119:SF0",
    "Q9D061": "PTHR24119:SF0",
    "Q9SM23": "PTHR24119:SF0",
    "Q9STP8": "PTHR24119:SF4",
    "Q9VRG6": "PTHR24119:SF0",
    "Q9XVJ0": "PTHR24119:SF0",
}

LOCAL_UNIPROT = {
    "Q9BR61": ROOT / "genes/human/ACBD6/ACBD6-uniprot.txt",
    "Q9D061": ROOT / "genes/mouse/Acbd6/Acbd6-uniprot.txt",
    "Q5RJK8": ROOT / "genes/rat/Acbd6/Acbd6-uniprot.txt",
    "Q4V8X4": ROOT / "genes/DANRE/acbd6/acbd6-uniprot.txt",
    "Q9VRG6": ROOT / "genes/DROME/anox/anox-uniprot.txt",
    "Q9XVJ0": ROOT / "genes/worm/acbp-5/acbp-5-uniprot.txt",
}


def fetch_uniprot_txt(acc: str) -> str:
    if acc in LOCAL_UNIPROT and LOCAL_UNIPROT[acc].exists():
        return LOCAL_UNIPROT[acc].read_text()
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def parse_entry(txt: str) -> dict[str, object]:
    lines = txt.splitlines()
    acc = ""
    reviewed = False
    sv = 1
    gene = ""
    organism = ""
    interpro: list[str] = []
    transmem: list[str] = []
    domains: list[str] = []
    repeats: list[str] = []
    seq_parts: list[str] = []
    in_seq = False

    for i, line in enumerate(lines):
        if line.startswith("ID   "):
            reviewed = "Reviewed;" in line
        elif line.startswith("AC   ") and not acc:
            acc = line[5:].split(";")[0].strip()
        elif line.startswith("DT   ") and "sequence version" in line:
            m = re.search(r"sequence version\s+(\d+)", line)
            if m:
                sv = int(m.group(1))
        elif line.startswith("GN   ") and not gene:
            for key in ("Name=", "ORFNames=", "OrderedLocusNames="):
                if key in line:
                    gene = line.split(key, 1)[1].split(";")[0].split("{")[0].strip()
                    break
        elif line.startswith("OS   ") and not organism:
            organism = line[5:].rstrip(".").split(" (")[0].strip()
        elif line.startswith("DR   InterPro;"):
            parts = [p.strip().rstrip(".") for p in line[5:].split(";")]
            if len(parts) >= 2:
                interpro.append(parts[1])
        elif line.startswith("FT   TRANSMEM"):
            pos = line.split()[2]
            transmem.append(pos)
        elif line.startswith("FT   DOMAIN"):
            pos = line.split()[2]
            note = ""
            j = i + 1
            while j < len(lines) and lines[j].startswith("FT                   "):
                if '/note="' in lines[j]:
                    note = lines[j].split('/note="', 1)[1].split('"', 1)[0]
                    break
                j += 1
            domains.append(f"{note or 'DOMAIN'}:{pos}")
        elif line.startswith("FT   REPEAT"):
            pos = line.split()[2]
            note = ""
            j = i + 1
            while j < len(lines) and lines[j].startswith("FT                   "):
                if '/note="' in lines[j]:
                    note = lines[j].split('/note="', 1)[1].split('"', 1)[0]
                    break
                j += 1
            repeats.append(f"{note or 'REPEAT'}:{pos}")
        elif line.startswith("SQ   "):
            in_seq = True
        elif line.startswith("//"):
            in_seq = False
        elif in_seq:
            seq_parts.append(re.sub(r"\s+", "", line))

    seq = "".join(seq_parts)
    return {
        "accession": acc,
        "status": "reviewed" if reviewed else "unreviewed",
        "sv": sv,
        "length": len(seq),
        "gene": gene or "-",
        "organism": organism,
        "has_ipr000582": "IPR000582" in interpro,
        "interpro_domains": ";".join(interpro) if interpro else "none",
        "ft_transmem": ";".join(transmem) if transmem else "none",
        "ft_domains_repeats": ";".join(domains + repeats) if (domains or repeats) else "none",
        "seq": seq,
    }


def locate_acb_pocket(seq: str, acb_domains: str, ref_acb: str) -> str:
    """Align target ACB region (or full sequence) to human Q9BR61[42..127] via BLOSUM62."""
    m_dom = re.search(r"ACB:(\d+)\.\.(\d+)", acb_domains)
    offset = 0
    target_sub = seq
    if m_dom:
        start = max(1, int(m_dom.group(1)) - 5)
        end = min(len(seq), int(m_dom.group(2)) + 5)
        offset = start - 1
        target_sub = seq[offset:end]

    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    if not m_dom:
        al.target_end_gap_score = 0.0
    aln = al.align(target_sub, ref_acb)[0]

    # Map 1-based human Q9BR61 positions (where ref_acb[0] is Q9BR61 pos 42) -> 1-based target pos
    q_to_t: dict[int, int] = {}
    t_blocks, q_blocks = aln.aligned
    for (ts, te), (qs, qe) in zip(t_blocks, q_blocks):
        for k in range(qe - qs):
            q_to_t[42 + qs + k] = offset + ts + k + 1

    out = []
    for hpos in (69, 73, 95, 106, 108, 114):
        tpos = q_to_t.get(hpos)
        out.append(f"{seq[tpos - 1]}{tpos}" if tpos is not None else "-")
    return "/".join(out)


def main() -> None:
    subfams = dict(KNOWN_PTHR24119_SUBFAMILIES)
    panther_tsv = ROOT / ".cache/panther/panther-members-19.0.tsv"
    if panther_tsv.exists():
        with open(panther_tsv) as f:
            for line in f:
                if "PTHR24119" in line:
                    parts = line.rstrip("\n").split("\t")
                    if len(parts) >= 2 and parts[1].startswith("PTHR24119"):
                        subfams[parts[0]] = parts[1]

    out_tsv = HERE / "member_architectures.tsv"
    fieldnames = [
        "accession",
        "status",
        "sv",
        "length",
        "subfamily",
        "gene",
        "organism",
        "has_ipr000582",
        "interpro_domains",
        "ft_transmem",
        "ft_domains_repeats",
        "pocket_y69_k73_k95_s106_s108_y114",
    ]
    ref_rec = parse_entry(fetch_uniprot_txt("Q9BR61"))
    ref_acb = str(ref_rec["seq"])[41:127]
    rows = []
    for acc in sorted(subfams):
        rec = parse_entry(fetch_uniprot_txt(acc))
        pocket = (
            locate_acb_pocket(str(rec["seq"]), str(rec["ft_domains_repeats"]), ref_acb)
            if rec["has_ipr000582"]
            else "no_ACB_domain"
        )
        rows.append(
            {
                "accession": acc,
                "status": rec["status"],
                "sv": rec["sv"],
                "length": rec["length"],
                "subfamily": subfams[acc],
                "gene": rec["gene"],
                "organism": rec["organism"],
                "has_ipr000582": rec["has_ipr000582"],
                "interpro_domains": rec["interpro_domains"],
                "ft_transmem": rec["ft_transmem"],
                "ft_domains_repeats": rec["ft_domains_repeats"],
                "pocket_y69_k73_k95_s106_s108_y114": pocket,
            }
        )

    with open(out_tsv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    for r in rows:
        print("\t".join(str(r[k]) for k in fieldnames))


if __name__ == "__main__":
    main()
