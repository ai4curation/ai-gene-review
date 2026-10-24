"""Is the apelin-13 peptide, and specifically its C-terminal Phe, conserved across the
PANTHER apelin family (PTHR15953)?

Why this is answerable without a multiple sequence alignment: every bioactive apelin
peptide (apelin-36/-31/-28/-17/-13) is released from the *C-terminus* of the precursor,
so "the last N residues" is an exact, alignment-free anchor. Human apelin-13 is
UniProt PEPTIDE 65..77 of a 77-residue precursor, i.e. exactly the last 13 residues.

Three questions are measured, each falsifiable:

  Q1  How conserved is the apelin-13 region (last 13 residues) across the family,
      column by column, compared with an equally sized window taken from the signal
      peptide (the internal negative control)?
  Q2  Does the human C-terminus match the ACE2 substrate consensus reported by
      Vickers et al. (PMID:11815627), "Pro-X(1-3)-Pro-Hydrophobic, where hydrolysis
      occurs between proline and the hydrophobic amino acid", and does that consensus
      hold across the family?
  Q3  Is the terminal Phe (human Phe77, a UniProt SITE "Important for the balance
      between G(i) and beta-arrestin pathways") retained in each ortholog?

Everything is fetched live from UniProt REST. Nothing is hardcoded; delete cache/ and
re-run to regenerate every number.

    uv run python cterm_conservation.py     # -> cterm_conservation.tsv
"""

from __future__ import annotations

import collections
import json
import pathlib
import sys

import requests

CACHE = pathlib.Path(__file__).parent / "cache"
OUT = pathlib.Path(__file__).parent / "cterm_conservation.tsv"

HUMAN = "Q9ULZ1"
PANTHER_FAMILY = "PTHR15953"
PEPTIDE_LEN = 13  # apelin-13; UniProt PEPTIDE 65..77 on the 77-residue human precursor
HYDROPHOBIC = set("AVLIPFMWYC")


def _cached_get(url: str, params: dict, key: str) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{key}.txt"
    if path.exists():
        return path.read_text()
    resp = requests.get(url, params=params, timeout=120)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.text


def fetch_family() -> list[dict]:
    """Every UniProtKB entry PANTHER classifies into PTHR15953, with its sequence."""
    text = _cached_get(
        "https://rest.uniprot.org/uniprotkb/search",
        {
            "query": f"xref:panther-{PANTHER_FAMILY}",
            "fields": "accession,id,protein_name,organism_name,organism_id,reviewed,sequence,ft_peptide",
            "format": "json",
            "size": "500",
        },
        f"uniprot_{PANTHER_FAMILY}",
    )
    return json.loads(text)["results"]


def column_counts(seqs: list[str], width: int, from_end: bool) -> list[collections.Counter]:
    cols: list[collections.Counter] = [collections.Counter() for _ in range(width)]
    for s in seqs:
        window = s[-width:] if from_end else s[:width]
        if len(window) != width:
            continue
        for i, aa in enumerate(window):
            cols[i][aa] += 1
    return cols


def main() -> int:
    entries = fetch_family()
    records = []
    for e in entries:
        seq = e["sequence"]["value"]
        records.append(
            {
                "accession": e["primaryAccession"],
                "organism": e["organism"]["scientificName"],
                "taxon": e["organism"]["taxonId"],
                "reviewed": e["entryType"].startswith("UniProtKB reviewed"),
                "length": len(seq),
                "seq": seq,
            }
        )
    if not records:
        print("no family members returned by UniProt", file=sys.stderr)
        return 1

    by_acc = {r["accession"]: r for r in records}
    if HUMAN not in by_acc:
        print(f"human {HUMAN} absent from the {PANTHER_FAMILY} member set", file=sys.stderr)
        return 1
    human = by_acc[HUMAN]

    # Assertion, not assumption: the human precursor must be the 77-mer this review is about.
    assert human["length"] == 77, f"human APLN length is {human['length']}, expected 77"
    human_cterm = human["seq"][-PEPTIDE_LEN:]
    # apelin-13 numbering: position 77 - PEPTIDE_LEN + 1 .. 77
    first_pos = human["length"] - PEPTIDE_LEN + 1

    # Only sequences long enough to carry both windows are scored, so the two windows
    # always come from the same set of proteins.
    scored = [r for r in records if r["length"] >= 2 * PEPTIDE_LEN]
    seqs = [r["seq"] for r in scored]
    cterm_cols = column_counts(seqs, PEPTIDE_LEN, from_end=True)
    nterm_cols = column_counts(seqs, PEPTIDE_LEN, from_end=False)

    lines = [
        "\t".join(
            [
                "window",
                "offset_from_window_start",
                "human_position",
                "human_residue",
                "modal_residue",
                "modal_count",
                "n_scored",
                "pct_identical_to_human",
            ]
        )
    ]

    def emit(label: str, cols: list[collections.Counter], human_window: str, pos0: int | None) -> list[float]:
        pcts = []
        for i, counter in enumerate(cols):
            total = sum(counter.values())
            hum = human_window[i]
            pct = 100.0 * counter[hum] / total if total else 0.0
            pcts.append(pct)
            modal, modal_n = counter.most_common(1)[0]
            lines.append(
                "\t".join(
                    [
                        label,
                        str(i + 1),
                        str(pos0 + i) if pos0 is not None else "NA",
                        hum,
                        modal,
                        str(modal_n),
                        str(total),
                        f"{pct:.1f}",
                    ]
                )
            )
        return pcts

    cterm_pct = emit("apelin-13 (C-terminal 13)", cterm_cols, human_cterm, first_pos)
    nterm_pct = emit("signal-peptide control (N-terminal 13)", nterm_cols, human["seq"][:PEPTIDE_LEN], 1)

    OUT.write_text("\n".join(lines) + "\n")

    # Q2: ACE2 consensus Pro-X(1-3)-Pro-Hydrophobic at the extreme C-terminus.
    def ace2_motif(seq: str) -> bool:
        tail = seq[-6:]
        if len(tail) < 4 or tail[-1] not in HYDROPHOBIC:
            return False
        if tail[-2] != "P":
            return False
        return "P" in tail[:-2]

    with_motif = [r for r in scored if ace2_motif(r["seq"])]

    # Q3: terminal residue identity.
    term_counter = collections.Counter(r["seq"][-1] for r in scored)

    n_rev = sum(1 for r in scored if r["reviewed"])
    print(f"family {PANTHER_FAMILY}: {len(records)} UniProt members, {len(scored)} scored "
          f"(length >= {2 * PEPTIDE_LEN}); {n_rev} Swiss-Prot reviewed")
    print(f"human {HUMAN} length {human['length']}; apelin-13 = residues {first_pos}-{human['length']} = {human_cterm}")
    print()
    print(f"mean % identity to human, apelin-13 window          : {sum(cterm_pct) / len(cterm_pct):.1f}%")
    print(f"mean % identity to human, N-terminal control window : {sum(nterm_pct) / len(nterm_pct):.1f}%")
    print()
    print("per-column identity to human across the apelin-13 window:")
    for i, pct in enumerate(cterm_pct):
        print(f"  pos {first_pos + i:>2} {human_cterm[i]}  {pct:5.1f}%")
    print()
    print(f"human C-terminal hexapeptide          : {human['seq'][-6:]}")
    print(f"ACE2 consensus Pro-X(1-3)-Pro-phi hit : {ace2_motif(human['seq'])}")
    print(f"family members matching that consensus: {len(with_motif)}/{len(scored)} "
          f"({100.0 * len(with_motif) / len(scored):.1f}%)")
    print()
    print("terminal residue across the family:")
    for aa, n in term_counter.most_common():
        print(f"  {aa}  {n:>4}  ({100.0 * n / len(scored):.1f}%)")
    print()
    print("Swiss-Prot reviewed members, C-terminal 13:")
    for r in sorted((r for r in scored if r["reviewed"]), key=lambda r: r["accession"]):
        print(f"  {r['accession']:<8} {r['organism']:<32} len={r['length']:>3}  {r['seq'][-PEPTIDE_LEN:]}")
    print()
    # Q4: do the rodent/bovine orthologs used in the pharmacology literature carry the
    # *same* mature peptides as human? If they do, a synthetic "rat apelin-17" is the
    # human gene product, and peptide pharmacology transfers exactly.
    print("identity of the mature peptides to human, per reviewed ortholog:")
    print(f"  {'accession':<9}{'organism':<26}{'apelin-13':<15}{'apelin-17':<19}{'apelin-36'}")
    for r in sorted((r for r in scored if r["reviewed"]), key=lambda r: r["accession"]):
        cells = []
        for width in (13, 17, 36):
            same = r["seq"][-width:] == human["seq"][-width:]
            diffs = sum(1 for a, b in zip(r["seq"][-width:], human["seq"][-width:]) if a != b)
            cells.append("identical" if same else f"{diffs} diff")
        print(f"  {r['accession']:<9}{r['organism'][:25]:<26}{cells[0]:<15}{cells[1]:<19}{cells[2]}")
    print()
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
