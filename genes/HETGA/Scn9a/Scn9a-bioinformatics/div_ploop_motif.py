#!/usr/bin/env python3
"""Compare the naked mole-rat NaV1.7 (SCN9A) domain IV P-loop motif with other mammals.

Background
----------
Smith et al. (PMID:22174253) reported that the naked mole-rat (NMR) carries a
species-specific variant of NaV1.7 that is potently blocked by protons. Smith,
Park & Lewin (PMID:32206859) describe the variant as a charge-changing
substitution in a "trio of amino acids" in domain IV: KKV (+/+/0) in mouse and
human becomes EKD or EKE (-/+/-) in subterranean African mole-rats.

This script checks that claim directly against the UniProt sequence used in this
review (G9DCX3, the mRNA submitted by the Smith et al. authors) and a panel of
other mammalian NaV1.7 sequences, and reports where the NMR fragment starts and
ends relative to the full-length human protein.

Nothing is hard-coded: the motif is located by a regular expression anchored on
the flanking conserved residues of the domain IV extracellular P-loop, so a sequence that
does not contain the anchor is reported as NOT FOUND rather than silently
mis-assigned.

Usage
-----
    python3 div_ploop_motif.py

Downloads are cached under ./data/ so re-runs are offline. Standard library only.
"""

from __future__ import annotations

import difflib
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
NMR_UNIPROT_TXT = HERE.parent / "Scn9a-uniprot.txt"

# Orthologue panel. Accessions were obtained by querying the UniProt REST search
# endpoint for gene:SCN9A restricted to each organism_id (see README notes).
PANEL = {
    "human (Homo sapiens)": "Q15858",
    "mouse (Mus musculus)": "Q62205",
    "rat (Rattus norvegicus)": "O08562",
    "rabbit (Oryctolagus cuniculus)": "Q28644",
    "guinea pig (Cavia porcellus)": "H0VMS3",
    "13-lined ground squirrel (Ictidomys tridecemlineatus)": "I3M736",
}

# Domain IV extracellular P-loop (between S5 and S6). The anchors either side of the triplet
# ("D[CS][DN]P" and "HPG") are invariant across the whole panel.
MOTIF_RE = re.compile(r"D[CS][DN]P(?P<triplet>...)HPG")


def fetch_fasta(accession: str) -> str:
    """Return the bare amino-acid sequence for a UniProt accession, caching locally."""
    cached = DATA / f"{accession}.fasta"
    if not cached.exists():
        DATA.mkdir(parents=True, exist_ok=True)
        url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
        cached.write_bytes(urllib.request.urlopen(url).read())
    text = cached.read_text()
    return "".join(line.strip() for line in text.splitlines()[1:])


def read_uniprot_flatfile_sequence(path: Path) -> str:
    """Extract the sequence from a UniProt flat-file (.txt) record."""
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ "))
    return "".join(
        line.replace(" ", "") for line in lines[start + 1 :] if not line.startswith("//")
    )


def find_triplet(seq: str) -> tuple[str, int] | None:
    """Return (triplet, 1-based start position of the triplet) or None."""
    match = MOTIF_RE.search(seq)
    if match is None:
        return None
    return match.group("triplet"), match.start("triplet") + 1


def align_span(query: str, subject: str) -> tuple[int, int, float]:
    """Rough ungapped-block alignment of query onto subject.

    Returns the 1-based subject start and end covered by the query, and the
    fraction of query residues that fall in an identical matching block.
    """
    matcher = difflib.SequenceMatcher(a=query, b=subject, autojunk=False)
    blocks = [b for b in matcher.get_matching_blocks() if b.size > 0]
    identical = sum(b.size for b in blocks)
    # Ignore incidental 1-4 residue blocks when deciding where the fragment starts
    # and ends, otherwise a chance single-residue match anchors the span at 1.
    anchors = [b for b in blocks if b.size >= 5] or blocks
    return anchors[0].b + 1, anchors[-1].b + anchors[-1].size, identical / len(query)


def main() -> int:
    if not NMR_UNIPROT_TXT.exists():
        print(f"missing {NMR_UNIPROT_TXT}", file=sys.stderr)
        return 1

    nmr = read_uniprot_flatfile_sequence(NMR_UNIPROT_TXT)
    sequences = {"naked mole-rat (Heterocephalus glaber)": nmr}
    sequences.update({name: fetch_fasta(acc) for name, acc in PANEL.items()})
    accessions = {"naked mole-rat (Heterocephalus glaber)": "G9DCX3", **PANEL}

    print("Domain IV extracellular P-loop triplet (anchored on D[CS][DN]P...HPG)")
    print(f"{'species':<55} {'acc':<10} {'len':>5}  {'triplet':<8} {'pos':>6}  context")
    for name, seq in sequences.items():
        found = find_triplet(seq)
        if found is None:
            print(f"{name:<55} {accessions[name]:<10} {len(seq):>5}  {'NOT FOUND':<8}")
            continue
        triplet, pos = found
        context = seq[pos - 9 : pos + 11]
        print(
            f"{name:<55} {accessions[name]:<10} {len(seq):>5}  {triplet:<8} {pos:>6}  {context}"
        )

    human = sequences["human (Homo sapiens)"]
    start, end, ident = align_span(nmr, human)
    print()
    print("Extent of the naked mole-rat fragment relative to full-length human Q15858")
    print(f"  G9DCX3 length                     : {len(nmr)} aa (UniProt flags it a Fragment)")
    print(f"  Q15858 length                     : {len(human)} aa")
    print(f"  fragment spans human residues     : ~{start}-{end}")
    print(f"  human residues missing at N-term  : {start - 1}")
    print(f"  human residues missing at C-term  : {len(human) - end}")
    print(f"  identical residues in matched blocks: {ident:.1%} of the fragment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
