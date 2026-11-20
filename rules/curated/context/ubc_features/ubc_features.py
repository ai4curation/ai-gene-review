"""Eukaryote-like features of archaeal UBC-domain (E2) proteins.

Aligns each archaeal UniProtKB protein matching IPR000608 (UBC catalytic core), plus
eukaryotic controls, to human UBE2D1 (P51668, UbcH5a) and reports, at the UBE2D1
positions of the HPN oxyanion-hole motif (H75, P76, N77) and the active-site
cysteine (C85), which residue each protein has. Also reports global identity to
UBE2D1.

Data are fetched live from UniProt REST, so results can change between releases.
Run: uv run python rules/curated/context/ubc_features/ubc_features.py > ubc_features.tsv
Pass accessions as arguments to skip the search (each entry is then fetched directly).
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REFERENCE = "P51668"  # human UBE2D1
POSITIONS = {"H75": 75, "P76": 76, "N77": 77, "C85": 85}
CONTROLS = ["P51668", "P15731"]  # human UBE2D1, yeast UBC4
QUERY = "xref:interpro-IPR000608 AND taxonomy_id:2157"


def fetch_tsv(query: str) -> list[dict]:
    """UniProtKB entries (accession, organism, sequence) for a query."""
    params = urllib.parse.urlencode(
        {"query": query, "fields": "accession,organism_name,length,sequence", "format": "tsv"}
    )
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/stream?{params}", timeout=300) as r:
        return list(csv.DictReader(io.StringIO(r.read().decode()), delimiter="\t"))


def _fetch_one(acc: str) -> dict:
    """One entry as FASTA from UniProt REST, falling back to the EBI Proteins API."""
    try:
        with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=120) as r:
            header, *lines = r.read().decode().splitlines()
        organism = re.search(r" OS=(.+?) OX=", header)
        return {"Entry": header.split("|")[1], "Organism": organism.group(1) if organism else "",
                "Sequence": "".join(lines)}
    except urllib.error.HTTPError:
        req = urllib.request.Request(f"https://www.ebi.ac.uk/proteins/api/proteins/{acc}",
                                     headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        names = d["organism"]["names"]
        sci = next((x["value"] for x in names if x["type"] == "scientific"), "")
        return {"Entry": d["accession"], "Organism": sci, "Sequence": d["sequence"]["sequence"]}


def fetch_entries(accessions: list[str]) -> list[dict]:
    """Fetch entries one by one (sequence and organism)."""
    rows = []
    for acc in accessions:
        row = _fetch_one(acc)
        row["Length"] = str(len(row["Sequence"]))
        rows.append(row)
    return rows


def aligner() -> Align.PairwiseAligner:
    """Global aligner, BLOSUM62, affine gaps."""
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def ref_to_target(aln: Align.Alignment) -> dict[int, int]:
    """Map 1-based reference positions (seqA) to 1-based target positions (seqB)."""
    mapping: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            mapping[a0 + i + 1] = b0 + i + 1
    return mapping


def identity(aln: Align.Alignment, ref: str, tgt: str) -> float:
    """Identical aligned residues over the shorter sequence length."""
    same = sum(
        ref[a0 + i] == tgt[b0 + i]
        for (a0, a1), (b0, _b1) in zip(*aln.aligned)
        for i in range(a1 - a0)
    )
    return same / min(len(ref), len(tgt))


def main() -> None:
    """Print one TSV row per protein."""
    given = sys.argv[1:]
    rows = fetch_entries(CONTROLS) + (fetch_entries(given) if given else fetch_tsv(QUERY))
    ref = next(r for r in rows if r["Entry"] == REFERENCE)["Sequence"]
    a = aligner()
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["accession", "organism", "length", "identity_to_UBE2D1", *POSITIONS, "HPN", "active_Cys"])
    for r in rows:
        seq = r["Sequence"]
        aln = a.align(ref, seq)[0]
        m = ref_to_target(aln)
        res = {k: (seq[m[p] - 1] if p in m else "-") for k, p in POSITIONS.items()}
        w.writerow([
            r["Entry"], r["Organism"], r["Length"], f"{identity(aln, ref, seq):.3f}",
            *res.values(),
            res["H75"] + res["P76"] + res["N77"] == "HPN",
            res["C85"] == "C",
        ])


if __name__ == "__main__":
    main()
