"""Check function-relevant positions of PTHR10780 members in PANTHER's family alignment.

Run from the repository root:

    uv run python interpro/panther/PTHR10780/msa_check.py

Writes ``<FAMILY>-msa-check.txt`` beside this script. Nothing is hard-coded except the
choice of reference protein: the alignment is PANTHER's own family MSA (``familymsa``
service), the leaves come from the PANTHER tree, and the reference positions are read
from the reference protein's UniProt feature table (its ``MUTAGEN`` features that
mention insertase activity, and its ``TRANSMEM`` features).

For every tree leaf the report gives: sequence length; the number of HMM match columns it
occupies; identity to the reference over match columns both occupy; the residue aligned to
each reference mutagenesis position; and the number of canonical mitochondrial-carrier
signature motifs ``P-x-[DE]-x-x-[KR]`` found in the leaf's own unaligned sequence. A
canonical SLC25 carrier (the ADP/ATP carrier named in CONTROL) is fetched from UniProt and
scanned with the same pattern as a positive control for the motif search.

In PANTHER's MSA upper-case letters are HMM match columns, lower-case letters are
insertions and ``.``/``-`` are gaps; all rows have the same length, so a column index is
comparable between rows.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import TREE_URL, served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
MSA_URL = "https://pantherdb.org/services/oai/pantherdb/familymsa"
REFERENCE = "Q9Y6C9"  # human MTCH2, the member with insertase mutagenesis data
CONTROL = "P12235"  # human SLC25A4 (ADP/ATP carrier 1), a canonical carrier
CARRIER_MOTIF = re.compile(r"(?=P.[DE]..[KR])")


def children(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (the API returns a dict for a single child)."""
    kids = node.get("children", {}).get("annotation_node", [])
    return [kids] if isinstance(kids, dict) else kids


def tree_leaves() -> list[dict]:
    """Leaf nodes of the family tree, refusing a release other than the pinned one."""
    payload = requests.get(TREE_URL, params={"family": FAMILY}, timeout=300).json()
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER serves release {served}, repo is pinned to {PANTHER_RELEASE}")
    leaves: list[dict] = []

    def walk(node: dict) -> None:
        kids = children(node)
        if not kids:
            leaves.append(node)
        for kid in kids:
            walk(kid)

    walk(payload["search"]["tree_topology"]["annotation_node"])
    return leaves


def uniprot_text(accession: str) -> str:
    """The UniProt flat-file record of an accession."""
    response = requests.get(f"https://rest.uniprot.org/uniprotkb/{accession}.txt", timeout=120)
    response.raise_for_status()
    return response.text


def record_sequence(record: str) -> tuple[str, str]:
    """Sequence and sequence version of a UniProt flat-file record."""
    version = re.search(r"^DT .*sequence version (\d+)", record, re.M)
    body = record.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"\s", "", body), version.group(1) if version else "?"


def insertase_mutagenesis(record: str) -> dict[int, str]:
    """Positions of single-residue MUTAGEN features whose note mentions insertase activity."""
    sites: dict[int, str] = {}
    for match in re.finditer(r"^FT   MUTAGEN +(\d+)\n((?:FT {19}.*\n)+)", record, re.M):
        note = " ".join(line[21:].strip() for line in match.group(2).splitlines())
        if "insertase" in note:
            sites[int(match.group(1))] = re.sub(r'/evidence=.*', "", note).replace('/note="', "").strip().rstrip('"')
    return sites


def transmembrane(record: str) -> list[tuple[int, int]]:
    """TRANSMEM feature ranges of a UniProt flat-file record."""
    return [(int(a), int(b)) for a, b in re.findall(r"^FT   TRANSMEM +(\d+)\.\.(\d+)", record, re.M)]


def column_of(row: str, position: int) -> int:
    """Alignment column holding residue ``position`` (1-based) of an aligned row."""
    seen = 0
    for column, char in enumerate(row):
        if char.isalpha():
            seen += 1
            if seen == position:
                return column
    raise SystemExit(f"position {position} is beyond the aligned sequence")


def residue_at(row: str, column: int) -> str:
    """Residue and its own-sequence number at an alignment column, or ``gap``."""
    char = row[column]
    if not char.isalpha():
        return "gap"
    return f"{char.upper()}{sum(c.isalpha() for c in row[: column + 1])}"


def main() -> None:
    """Write the alignment check report for FAMILY."""
    payload = requests.get(MSA_URL, params={"family": FAMILY}, timeout=300).json()
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER MSA is for release {served}, repo is pinned to {PANTHER_RELEASE}")
    rows = {s["persistent_id"]: s["sequence"] for s in payload["search"]["MSA_list"]["sequence_info"]}
    leaves = tree_leaves()
    info = {}
    for leaf in leaves:
        parts = leaf["node_name"].split("|")
        info[leaf["persistent_id"]] = {
            "org": parts[0],
            "acc": parts[-1].split("=", 1)[1],
            "symbol": leaf.get("gene_symbol") or "-",
            "sf": leaf.get("sf_id") or leaf.get("prop_sf_id"),
        }
    missing = [pid for pid in info if pid not in rows]
    ref_pid = next(pid for pid, i in info.items() if i["acc"] == REFERENCE)
    ref_row = rows[ref_pid]
    record = uniprot_text(REFERENCE)
    ref_seq, ref_version = record_sequence(record)
    aligned_ref = re.sub(r"[^A-Za-z]", "", ref_row).upper()
    sites = insertase_mutagenesis(record)
    if not sites:
        raise SystemExit(f"no insertase MUTAGEN feature found on {REFERENCE}; nothing to check")
    columns = {pos: column_of(ref_row, pos) for pos in sites}
    match_columns = [i for i, c in enumerate(ref_row) if c.isupper() or c == "-"]
    tms = transmembrane(record)

    control_seq, control_version = record_sequence(uniprot_text(CONTROL))
    control_hits = [m.start() + 1 for m in CARRIER_MOTIF.finditer(control_seq)]
    if not control_hits:
        raise SystemExit("carrier motif search found nothing in the canonical carrier; pattern cannot be trusted")

    out = [
        f"alignment: PANTHER {PANTHER_RELEASE} familymsa for {FAMILY}; rows {len(rows)} (leaves and ancestral nodes); "
        f"columns {len(ref_row)}; tree leaves {len(info)}; leaves without an MSA row {len(missing)}",
        f"reference UniProtKB:{REFERENCE} sequence version {ref_version} length {len(ref_seq)}; "
        f"MSA row identical to UniProt sequence: {aligned_ref == ref_seq}",
        "reference TRANSMEM features (UniProt numbering): " + " ".join(f"{a}-{b}" for a, b in tms),
    ]
    for pos, note in sorted(sites.items()):
        in_tm = next((f"TM{n + 1}" for n, (a, b) in enumerate(tms) if a <= pos <= b), "outside TRANSMEM features")
        out.append(f"reference site {ref_seq[pos - 1]}{pos} ({in_tm}): {note}")
    out.append(
        f"carrier signature motif P-x-[DE]-x-x-[KR] positive control UniProtKB:{CONTROL} sequence version "
        f"{control_version} length {len(control_seq)}: {len(control_hits)} motifs at "
        + ",".join(f"{control_seq[p - 1:p + 5]}{p}" for p in control_hits)
    )
    out += ["", "leaf\taccession\torganism\tsymbol\tsubfamily\tlength\tmatch_columns\tidentity_to_reference\t"
            + "\t".join(f"ref_{ref_seq[p - 1]}{p}" for p in sorted(sites)) + "\tcarrier_motifs"]
    tally: dict[tuple[str, int], Counter] = {}
    motif_tally: dict[str, Counter] = {}
    for pid, i in info.items():
        if pid in missing:
            out.append(f"{pid}\t{i['acc']}\t{i['org']}\t{i['symbol']}\t{i['sf']}\tNO_MSA_ROW")
            continue
        row = rows[pid]
        seq = re.sub(r"[^A-Za-z]", "", row).upper()
        both = [c for c in match_columns if row[c].isalpha() and ref_row[c].isalpha()]
        same = sum(row[c].upper() == ref_row[c].upper() for c in both)
        cells = []
        for pos in sorted(sites):
            cell = residue_at(row, columns[pos])
            cells.append(cell)
            tally.setdefault((i["sf"], pos), Counter())[cell[0] if cell != "gap" else "gap"] += 1
        motifs = [f"{seq[m.start():m.start() + 6]}{m.start() + 1}" for m in CARRIER_MOTIF.finditer(seq)]
        motif_tally.setdefault(i["sf"], Counter())[len(motifs)] += 1
        out.append(
            f"{pid}\t{i['acc']}\t{i['org']}\t{i['symbol']}\t{i['sf']}\t{len(seq)}\t"
            f"{sum(row[c].isalpha() for c in match_columns)}\t{same}/{len(both)}\t" + "\t".join(cells)
            + f"\t{len(motifs)}:{','.join(motifs) or '-'}"
        )
    out += ["", "== residue at each reference site, by subfamily =="]
    for (sf, pos), counts in sorted(tally.items()):
        out.append(f"{sf} ref {ref_seq[pos - 1]}{pos}: " + " ".join(f"{k}={v}" for k, v in counts.most_common()))
    out += ["", "== number of P-x-[DE]-x-x-[KR] motifs per sequence, by subfamily (motifs=leaves) =="]
    for sf, counts in sorted(motif_tally.items()):
        out.append(f"{sf}: " + " ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    (HERE / f"{FAMILY}-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-msa-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
