# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Evolutionary grounding for canonical human RHOJ (Q9H4E5).

1. PANTHER subfamily placement (PANTHER geneinfo REST service, live).
2. G-domain motif scan of the canonical UniProt sequence (live UniProt REST).
3. PAINT IBD nodes in the repository's cached PTHR24072 PAINT table, listing
   which nodes carry IBD assertions and whether Q9H4E5 is itself a seed.

Run: uv run --script evolutionary_grounding.py
"""

import json
import re
import urllib.request
from pathlib import Path

ACC = "Q9H4E5"
REPO = Path(__file__).resolve().parents[4]
PAINT = REPO / "interpro/panther/PTHR24072/PTHR24072-paint.tsv"


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def panther() -> None:
    url = f"https://pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList={ACC}&organism=9606"
    data = json.loads(get(url))
    mapped = data["search"]["mapped_genes"]["gene"]
    genes = mapped if isinstance(mapped, list) else [mapped]
    for g in genes:
        print(f"PANTHER: accession={g['accession']} family={g.get('family_id')} "
              f"subfamily={g.get('sf_id')} name={g.get('family_name')} / {g.get('sf_name')}")


MOTIFS = {
    "G1 P-loop GxxxxGK(S/T)": r"G....GK[ST]",
    "G2 switch I PTVFD": r"PTVFD",
    "G3 switch II DT(A/V)GQ": r"DT[AV]GQ",
    "G4 (T/N)(K/Q)xD": r"[TN][KQ].D",
    "G5 (C/S)SA(L/K)": r"[CS]SA[LK]",
    "C-terminal CAAX": r"C[A-Z]{3}$",
}


def motifs() -> None:
    fasta = get(f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta")
    seq = "".join(fasta.splitlines()[1:])
    print(f"Sequence length: {len(seq)}")
    for name, pat in MOTIFS.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, seq)]
        # G4 pattern is short; report only hits after the switch II region
        if name.startswith("G4"):
            hits = [h for h in hits if 110 < h[0] < 150]
        if name.startswith("G5"):
            hits = [h for h in hits if 160 < h[0] < 190]
        print(f"  {name}: {hits if hits else 'absent'}")


def paint() -> None:
    rows = [line.rstrip("\n").split("\t") for line in PAINT.open()]
    header, body = rows[0], rows[1:]
    idx = {h: i for i, h in enumerate(header)}
    print(f"PAINT table: {PAINT.relative_to(REPO)} ({len(body)} IBD rows)")
    for r in body:
        seeds = r[idx["seeds"]].split("|")
        if r[idx["node"]] in {"PTN000632671", "PTN008604840", "PTN008604842"}:
            print(f"  {r[idx['node']]} {r[idx['go_id']]} aspect={r[idx['aspect']]} "
                  f"taxon={r[idx['taxon']]} n_seeds={len(seeds)} "
                  f"Q9H4E5_is_seed={'UniProtKB:' + ACC in seeds}")


if __name__ == "__main__":
    panther()
    motifs()
    paint()
