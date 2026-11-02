# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review analysis for cod tbc1d14 (A0A8C5FPT8).

1. Resolve which Ensembl gene each cod 'tbc1d14' UniProt entry belongs to
   (are they isoforms of one gene?).
2. Align the target with TBC1D14 and TBC1D12 orthologs across vertebrates
   (MAFFT), report pairwise identity and a neighbour-joining tree, to test
   whether the PANTHER SF15 (TBC1D12) placement reflects orthology.

Run: uv run compare_sequences_rereview.py > RESULTS-rereview.txt
"""
import io
import subprocess
import tempfile

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.fasta"
ENSEMBL = "https://rest.ensembl.org/lookup/id/{}?content-type=application/json"

COD_TBC1D14_ENTRIES = {
    "A0A8C5FCB4": "ENSGMOT00000030993",
    "A0A8C4Z0Q4": "ENSGMOT00000003673",
    "A0A8C5A8S4": "ENSGMOT00000049459",
    "A0A8C5B8M0": "ENSGMOT00000024630",
    "A0A8C4ZRU6": "ENSGMOT00000020168",
    "A0A8C5C0A0": "ENSGMOT00000029003",
    "A0A8C5FPT8": "ENSGMOT00000039892",
    "A0A8C5BG38": "ENSGMOT00000026390",
    "A0A8C5AUF9": "ENSGMOT00000061201",
    "A0A8C5BUI9": "ENSGMOT00000055917",
}

PANEL = {
    "cod_tbc1d14_A0A8C5FPT8": "A0A8C5FPT8",
    "cod_tbc1d14_A0A8C5FCB4": "A0A8C5FCB4",
    "human_TBC1D14_Q9P2M4": "Q9P2M4",
    "mouse_Tbc1d14_Q8CGA2": "Q8CGA2",
    "chicken_TBC1D14_A0A8V0YBQ2": "A0A8V0YBQ2",
    "xentr_tbc1d14_A0A8J0R045": "A0A8J0R045",
    "zebrafish_tbc1d14_A0A8N7TAE1": "A0A8N7TAE1",
    "coelacanth_TBC1D14_H3AI10": "H3AI10",
    "human_TBC1D12_O60347": "O60347",
    "mouse_Tbc1d12_Q6A039": "Q6A039",
    "xentr_tbc1d12_Q0IHY4": "Q0IHY4",
    "zebrafish_tbc1d12b_E7FDW4": "E7FDW4",
    "cod_TBC1D12like_A0A8C5BBR7": "A0A8C5BBR7",
}


def fetch_seq(acc: str) -> str:
    r = requests.get(UNIPROT.format(acc), timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def gene_of_transcript(tid: str) -> str:
    r = requests.get(ENSEMBL.format(tid), timeout=60)
    if r.status_code != 200:
        return f"lookup-failed({r.status_code})"
    return r.json().get("Parent", "?")


def identity(a: str, b: str) -> tuple[float, int]:
    """Identity over columns where both sequences have a residue."""
    both = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    if not both:
        return 0.0, 0
    same = sum(1 for x, y in both if x == y)
    return 100.0 * same / len(both), len(both)


def main() -> None:
    print("## 1. Ensembl gene of each cod tbc1d14 UniProt entry")
    for acc, tid in COD_TBC1D14_ENTRIES.items():
        seq = fetch_seq(acc)
        print(f"{acc}\t{tid}\tgene={gene_of_transcript(tid)}\tlen={len(seq)}")

    seqs = {name: fetch_seq(acc) for name, acc in PANEL.items()}
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for name, s in seqs.items():
            fh.write(f">{name}\n{s}\n")
        path = fh.name
    aln_txt = subprocess.run(
        ["mafft", "--auto", "--quiet", path], capture_output=True, text=True, check=True
    ).stdout
    with open("panel_rereview.aln.fa", "w") as out:
        out.write(aln_txt)
    aln = AlignIO.read(io.StringIO(aln_txt), "fasta")
    rec = {r.id: str(r.seq) for r in aln}
    target = rec["cod_tbc1d14_A0A8C5FPT8"]

    print("\n## 2. Identity of target to panel (aligned residue pairs)")
    for name in rec:
        if name == "cod_tbc1d14_A0A8C5FPT8":
            continue
        pid, n = identity(target, rec[name])
        print(f"{name}\t{pid:.1f}%\tover {n} aligned positions\tlen={len(seqs[name])}")

    print("\n## 3. Neighbour-joining tree (identity distance)")
    tree = DistanceTreeConstructor().nj(DistanceCalculator("identity").get_distance(aln))
    tree.root_with_outgroup("cod_TBC1D12like_A0A8C5BBR7")
    Phylo.draw_ascii(tree)
    buf = io.StringIO()
    Phylo.write(tree, buf, "newick")
    print(buf.getvalue())

    print("## 4. Termini: target vs sister cod model A0A8C5FCB4 vs human TBC1D14")
    for name in ("cod_tbc1d14_A0A8C5FPT8", "cod_tbc1d14_A0A8C5FCB4", "human_TBC1D14_Q9P2M4"):
        print(f"{name}\tN40={seqs[name][:40]}\tC60={seqs[name][-60:]}")
    pid, n = identity(rec["cod_tbc1d14_A0A8C5FCB4"], rec["human_TBC1D14_Q9P2M4"])
    print(f"A0A8C5FCB4 vs human TBC1D14: {pid:.1f}% over {n} aligned positions")

    print("\n## 5. Human TBC1D14 landmarks mapped onto cod models")
    h = rec["human_TBC1D14_Q9P2M4"]
    cods = ("cod_tbc1d14_A0A8C5FPT8", "cod_tbc1d14_A0A8C5FCB4")
    pos = {"human": 0, **{c: 0 for c in cods}}
    hmap = {}
    for col in range(len(h)):
        if h[col] != "-":
            pos["human"] += 1
        for c in cods:
            if rec[c][col] != "-":
                pos[c] += 1
        if h[col] != "-":
            hmap[pos["human"]] = {c: (rec[c][col], pos[c]) if rec[c][col] != "-" else ("-", None) for c in cods}
    for hp, label in ((472, "catalytic Arg (R472)"), (508, "catalytic Gln (Q508)")):
        print(f"human {label}: " + "; ".join(f"{c}={hmap[hp][c][0]}{hmap[hp][c][1]}" for c in cods))
    for lo, hi in ((1, 50), (120, 223), (650, 693)):
        for c in cods:
            pairs = [(h_res, hmap[p][c][0]) for p in range(lo, hi + 1) for h_res in [h.replace("-", "")[p - 1]]]
            aligned = [x for x in pairs if x[1] != "-"]
            same = sum(1 for a, b in aligned if a == b)
            print(f"human {lo}-{hi} vs {c}: {len(aligned)} aligned, {same} identical")


if __name__ == "__main__":
    main()
