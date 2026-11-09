"""Check rule-assigned transmembrane segments against hydropathy.

For each HAMAP rule given, fetch the UniProtKB entries that carry the rule
(``xref:hamap-MF_xxxxx``) with their TRANSMEM features and sequence, and
compute the mean Kyte-Doolittle hydropathy of every TRANSMEM segment whose
evidence names that HAMAP rule. Genuine transmembrane helices average well
above 1; the MtrA case that motivated this check (O27134, MF_01093, residues
102-118) averages 0.49. A segment below the threshold is reported as a
candidate false transmembrane assignment. The threshold is a screening
heuristic, not a test: flagged entries still need review.

Data come live from UniProt REST, so counts change between releases.

Usage:
    python projects/HAMAP/check_rule_tm_segments.py MF_01093 [MF_... ...] > out.tsv
    python projects/HAMAP/check_rule_tm_segments.py --from-scan projects/HAMAP/hamap_rule_scan.yaml > out.tsv
"""

from __future__ import annotations

import csv
import io
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
THRESHOLD = 1.0
TRANSMEM = re.compile(r"TRANSMEM (\d+)\.\.(\d+);([^T]*?)(?=TRANSMEM|\Z)")


def mean_hydropathy(segment: str) -> float:
    """Mean Kyte-Doolittle hydropathy of a peptide.

    >>> round(mean_hydropathy("DLETGRIIGATGAIPYI"), 2)
    0.49
    >>> mean_hydropathy("LLLL")
    3.8
    """
    vals = [KD[a] for a in segment if a in KD]
    return sum(vals) / len(vals) if vals else 0.0


def rule_segments(ft_transmem: str, rule: str) -> list[tuple[int, int]]:
    """TRANSMEM spans whose evidence cites the given HAMAP rule.

    >>> rule_segments('TRANSMEM 102..118; /note="Helical"; /evidence="ECO:0000255|HAMAP-Rule:MF_01093"', "MF_01093")
    [(102, 118)]
    >>> rule_segments('TRANSMEM 5..25; /note="Helical"; /evidence="ECO:0000256|SAM:Phobius"', "MF_01093")
    []
    """
    out = []
    for m in TRANSMEM.finditer(ft_transmem or ""):
        if f"HAMAP-Rule:{rule}" in m.group(3):
            out.append((int(m.group(1)), int(m.group(2))))
    return out


def fetch(rule: str) -> list[dict]:
    """UniProtKB entries carrying the rule, with TRANSMEM features and sequence."""
    params = urllib.parse.urlencode({
        "query": f"xref:hamap-{rule}",
        "fields": "accession,reviewed,organism_name,length,ft_transmem,sequence",
        "format": "tsv",
    })
    url = f"https://rest.uniprot.org/uniprotkb/stream?{params}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=600) as r:
                return list(csv.DictReader(io.StringIO(r.read().decode()), delimiter="\t"))
        except Exception:  # network errors from the external service
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
    return []


def rules_from_scan(path: Path) -> list[str]:
    """Candidate rule accessions from the scan_hamap_rules.py output."""
    import yaml

    d = yaml.safe_load(path.read_text())
    return [r["rule"] for r in d["candidates"]["rules"]]


def main(argv: list[str]) -> None:
    """Print one TSV row per rule-assigned TRANSMEM segment."""
    rules = rules_from_scan(Path(argv[1])) if argv[0] == "--from-scan" else argv
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["rule", "accession", "reviewed", "organism", "length", "start", "end",
                "segment", "mean_kd", "below_threshold"])
    for rule in rules:
        for e in fetch(rule):
            seq = e["Sequence"]
            for start, end in rule_segments(e["Transmembrane"], rule):
                seg = seq[start - 1:end]
                kd = mean_hydropathy(seg)
                w.writerow([rule, e["Entry"], e["Reviewed"], e["Organism"], e["Length"], start, end,
                            seg, f"{kd:.2f}", kd < THRESHOLD])


if __name__ == "__main__":
    main(sys.argv[1:])
