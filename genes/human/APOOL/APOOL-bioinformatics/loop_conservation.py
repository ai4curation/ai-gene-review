"""Is the basic inter-transmembrane loop of human APOOL/MIC27 conserved across the
MIC26/MIC27 (PANTHER PTHR14564) family?

Motivation
----------
Weber et al. 2013 (PMID:23704930) showed recombinant human APOOL binds cardiolipin
and not its precursor phosphatidylglycerol, and described APOOL as "two putative
transmembrane helices connected by a positively charged stretch of amino acids".
Brown et al. 2026 (PMID:42647630) proposed from AlphaFold3 models and multiscale MD
that Mic10, Mic26 and Mic27 "strongly recruit cardiolipin at conserved positive loop
motifs".

Neither claim has been checked against the actual family alignment in this repository.
This script does that, from live data only:

1. fetch the PTHR14564 representative member sequences (accessions read from
   ``interpro/panther/PTHR14564/PTHR14564-entries.csv``) plus the Drosophila protein
   that seeds the family's PAINT IBD node, from the UniProt REST API;
2. assert every fetched sequence has the length the family index records (the fly
   seed is not in that index, so its length is only reported);
3. read the human APOOL transmembrane/topology features from the local UniProt flat
   file rather than re-predicting them;
4. align the family with FAMSA and project the human inter-TM loop columns onto every
   member;
5. report, per member, the aligned loop segment, its K+R count and its net charge.

Nothing is hard-coded except identifiers. An inconclusive alignment is a legitimate
result and is reported as such.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from pyfamsa import Aligner, Sequence

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
FAMILY = "PTHR14564"
ENTRIES_CSV = REPO_ROOT / "interpro" / "panther" / FAMILY / f"{FAMILY}-entries.csv"
UNIPROT_TXT = GENE_DIR / "APOOL-uniprot.txt"

HUMAN = "Q6UXV4"  # APOOL / MIC27
MIC26_HUMAN = "Q9BUR5"  # APOO / MIC26, the other human paralogue and an IBD seed
FLY_SEED = "Q9VEY5"  # Dmel CG5903 / Mic26-27, the FB:FBgn0038400 IBD seed

BASIC = set("KR")
ACIDIC = set("DE")


@dataclass
class Member:
    accession: str
    gene: str
    organism: str
    indexed_length: int | None
    sequence: str


def fetch_uniprot_json(accession: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    with urllib.request.urlopen(url, timeout=60) as handle:
        return json.load(handle)


def read_family_index() -> dict[str, dict[str, str]]:
    rows = {}
    with ENTRIES_CSV.open() as handle:
        for row in csv.DictReader(handle):
            rows[row["id"]] = row
    return rows


def parse_topology(uniprot_txt: Path) -> list[tuple[str, int, int, str]]:
    """Return (feature_key, start, end, note) for TRANSMEM/TOPO_DOM/TRANSIT features."""
    features: list[tuple[str, int, int, str]] = []
    key = None
    span: tuple[int, int] | None = None
    for line in uniprot_txt.read_text().splitlines():
        if not line.startswith("FT   ") and not line.startswith("FT       "):
            continue
        header = re.match(r"^FT   (\w+)\s+(\d+)\.\.(\d+)$", line)
        single = re.match(r"^FT   (\w+)\s+(\d+)$", line)
        if header:
            key, span = header.group(1), (int(header.group(2)), int(header.group(3)))
            continue
        if single:
            key, span = single.group(1), (int(single.group(2)), int(single.group(2)))
            continue
        note = re.match(r'^FT\s+/note="([^"]*)"', line)
        if note and key and span and key in {"TRANSMEM", "TOPO_DOM", "TRANSIT"}:
            features.append((key, span[0], span[1], note.group(1)))
            key, span = None, None
    return features


def human_inter_tm_loop(features: list[tuple[str, int, int, str]]) -> tuple[int, int]:
    transmem = sorted((s, e) for k, s, e, _ in features if k == "TRANSMEM")
    if len(transmem) != 2:
        raise SystemExit(
            f"expected exactly 2 TRANSMEM features in {UNIPROT_TXT.name}, got {len(transmem)}"
        )
    (_, end_tm1), (start_tm2, _) = transmem
    return end_tm1 + 1, start_tm2 - 1


def net_charge(segment: str) -> int:
    return sum(1 for c in segment if c in BASIC) - sum(1 for c in segment if c in ACIDIC)


def main() -> None:
    index = read_family_index()
    accessions = list(index) + [FLY_SEED]
    if HUMAN not in index:
        raise SystemExit(f"{HUMAN} is absent from {ENTRIES_CSV}; family index changed")

    members: list[Member] = []
    for accession in accessions:
        record = fetch_uniprot_json(accession)
        sequence = record["sequence"]["value"]
        row = index.get(accession)
        indexed_length = int(row["length"]) if row else None
        if indexed_length is not None and indexed_length != len(sequence):
            raise SystemExit(
                f"{accession}: UniProt length {len(sequence)} != family index length "
                f"{indexed_length}; the index is stale, refusing to align"
            )
        gene = (
            row["gene"]
            if row
            else (record.get("genes") or [{}])[0].get("geneName", {}).get("value", "?")
        )
        members.append(
            Member(
                accession=accession,
                gene=gene,
                organism=record["organism"]["scientificName"],
                indexed_length=indexed_length,
                sequence=sequence,
            )
        )

    features = parse_topology(UNIPROT_TXT)
    loop_start, loop_end = human_inter_tm_loop(features)
    human = next(m for m in members if m.accession == HUMAN)
    human_loop = human.sequence[loop_start - 1 : loop_end]

    print(f"# {FAMILY} inter-transmembrane loop conservation")
    print()
    print(f"Members fetched: {len(members)} "
          f"({len(index)} from the family index + the fly PAINT seed {FLY_SEED})")
    print("Length check (live UniProt vs family index; a mismatch aborts the run):")
    for member in members:
        if member.indexed_length is None:
            print(f"  {member.accession}: {len(member.sequence):>4} aa (not in the index)")
        else:
            print(
                f"  {member.accession}: {len(member.sequence):>4} aa == "
                f"{member.indexed_length} in {ENTRIES_CSV.name}"
            )
    print()
    print("## Human APOOL topology (from APOOL-uniprot.txt, not re-predicted)")
    for key, start, end, note in features:
        print(f"  {key:9s} {start:>4}..{end:<4} {note}")
    print()
    print(
        f"Inter-TM loop = residues {loop_start}-{loop_end} = {human_loop} "
        f"(K/R={sum(1 for c in human_loop if c in BASIC)}, net charge={net_charge(human_loop):+d})"
    )
    print()

    aligner = Aligner(guide_tree="upgma")
    msa = aligner.align(
        Sequence(m.accession.encode(), m.sequence.encode()) for m in members
    )
    aligned = {s.id.decode(): s.sequence.decode() for s in msa}

    # Map human loop residue positions onto alignment columns.
    columns: list[int] = []
    residue_index = 0
    for column, char in enumerate(aligned[HUMAN]):
        if char == "-":
            continue
        residue_index += 1
        if loop_start <= residue_index <= loop_end:
            columns.append(column)
    if len(columns) != loop_end - loop_start + 1:
        raise SystemExit("failed to project every human loop residue onto a column")

    first_col, last_col = columns[0], columns[-1]
    print("## Aligned loop segment per family member")
    print()
    print(f"{'accession':<10} {'gene':<10} {'organism':<34} {'span':<12} {'segment':<16} K+R  net")
    conserved = 0
    mic26_loop_positions: list[tuple[int, str]] = []
    for member in members:
        row = aligned[member.accession]
        segment = row[first_col : last_col + 1]
        ungapped = segment.replace("-", "")
        # walk the aligned row to get native coordinates of the block
        pos = 0
        block_positions = []
        for column, char in enumerate(row):
            if char == "-":
                continue
            pos += 1
            if first_col <= column <= last_col:
                block_positions.append((pos, char))
        span = (
            f"{block_positions[0][0]}-{block_positions[-1][0]}"
            if block_positions
            else "gap"
        )
        kr = sum(1 for c in ungapped if c in BASIC)
        charge = net_charge(ungapped)
        if kr >= 2 and charge > 0:
            conserved += 1
        print(
            f"{member.accession:<10} {member.gene:<10} {member.organism:<34} "
            f"{span:<12} {ungapped:<16} {kr:<4} {charge:+d}"
        )
        if member.accession == MIC26_HUMAN:
            mic26_loop_positions = block_positions

    print()
    print(
        f"Members whose aligned inter-TM block carries >=2 K/R and a net positive charge: "
        f"{conserved}/{len(members)}"
    )
    print()
    print("## Human MIC26 (APOO) residues aligned to the human APOOL loop")
    if mic26_loop_positions:
        for pos, char in mic26_loop_positions:
            print(f"  {MIC26_HUMAN} {char}{pos}")
    else:
        print(f"  {MIC26_HUMAN} aligns to gaps across the human APOOL loop columns")

    print()
    print("## Per-position human APOOL loop residues")
    for offset, char in enumerate(human_loop):
        print(f"  {HUMAN} {char}{loop_start + offset}")

    sys.stdout.flush()


if __name__ == "__main__":
    main()
